#!/usr/bin/env python3
"""Refresh brain/context/jj-activity-snapshot.json from JJ's niche sheets.

Aggregates cold-call activity across all known niche target sheets:
  - Reads `Full Target List` tab columns T (1st Call Date) + V (2nd Call Date)
  - Normalizes date formats (slashes, dots, 2/4-digit years)
  - Buckets dials per day for the last 84 days
  - Computes weekly totals (12 buckets) + this-week / today aggregates

Per `feedback_jj_call_date_from_field_not_tab.md`, dial counts MUST come from
populated Call Date field values, never from tab grouping. Tab names are
estimated batch dates only.

Run via launchd post-shift (Mon-Fri 2:30pm ET) so the dashboard reflects
JJ's day before Kay reviews evening / morning.

Usage:
    GOG_ACCOUNT=... ./refresh_jj_snapshot.py
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import requests

REPO_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT_PATH = REPO_ROOT / "brain" / "context" / "jj-activity-snapshot.json"
GOG_CREDS_PATH = Path.home() / "Library" / "Application Support" / "gogcli" / "credentials.json"
GOG_ACCOUNT = os.environ.get("GOG_ACCOUNT", "kay.s@greenwichandbarrow.com")

# Match Call Log tab names like "Call Log 4.21.26" or "Call Log 04.21.2026".
_CALL_LOG_TAB_RE = re.compile(r"^Call Log\s+\d+[./]\d+[./]\d+$", re.IGNORECASE)

# Known niche target sheets (from .claude/skills/jj-operations/SKILL.md).
# Add more here as new niches activate. Sheet name → sheet ID.
NICHE_SHEETS = {
    "Art Insurance": "15M76-gpcklwc47HDXIwyFC9Tj8K4wDOor4i0uxCYyHQ",
    "Domestic TCI": "1lEAx-3pEshsSc0Rix4KunJ38mzHahjAmV6nQA_cuwLw",
    "IPLC": "1Cdw6yb8-yBQtx5mTB8Hu4rENkJfpmt3t7HZdGqtdylQ",
    "Art Storage": "1PDprJ_gApm7T_kzpNWlWk7qItQ11M95ssL9_UD5sE9g",
    "Art Advisory": "1c6Db21D2qDpiT7LnEQ4l0AROlA-gucDQD1ZGOlrZ-K0",
    "Premium Pest Management": "1Y0ZjEkc2LHhBoO4QGO8Ny9MvG90NpojQn8bloKA291I",
}

# Match anything that looks like a date: digits + (/ or .) + digits + (/ or .) + digits.
# Tolerates double-slashes (4/8//2026), 2- vs 4-digit years, mixed separators.
_DATE_CANDIDATE = re.compile(r"(\d{1,4})[/.]+(\d{1,2})[/.]+(\d{1,4})")


def _normalize_date(raw: str) -> date | None:
    """Parse JJ's inconsistent date formats into a date.

    Examples that should parse: 4/20/26, 4.24.26, 4/13/2026, 4/8//2026.
    Returns None if the string contains no date-like substring.
    """
    if not raw or not isinstance(raw, str):
        return None
    m = _DATE_CANDIDATE.search(raw)
    if not m:
        return None
    a, b, c = m.groups()
    try:
        # Try US format M/D/Y first (JJ's primary convention).
        month = int(a)
        day = int(b)
        year_raw = int(c)
        # 2-digit year → assume 2000s
        year = year_raw + 2000 if year_raw < 100 else year_raw
        return date(year, month, day)
    except (ValueError, TypeError):
        return None


def _get_access_token() -> str | None:
    """Refresh gog's OAuth token to get a fresh Sheets API access token.

    Reads client_id + client_secret from gog's credentials.json, exports the
    refresh_token via `gog auth tokens export`, then POSTs to Google's token
    endpoint. The exported token file is deleted on the same call to avoid
    leaving secrets at rest.
    """
    if not GOG_CREDS_PATH.exists():
        print(f"[refresh-jj] WARN: gog credentials.json not found at {GOG_CREDS_PATH}", file=sys.stderr)
        return None
    try:
        creds = json.loads(GOG_CREDS_PATH.read_text())
    except (OSError, json.JSONDecodeError) as e:
        print(f"[refresh-jj] WARN: failed to read gog creds: {e}", file=sys.stderr)
        return None

    with tempfile.NamedTemporaryFile("r", suffix=".json", delete=False) as tmp:
        tmp_path = Path(tmp.name)
    try:
        export = subprocess.run(
            ["gog", "auth", "tokens", "export", GOG_ACCOUNT, "--out", str(tmp_path), "--overwrite"],
            capture_output=True, text=True, timeout=15,
        )
        if export.returncode != 0:
            print(f"[refresh-jj] WARN: gog token export failed: {export.stderr[:200]}", file=sys.stderr)
            return None
        token_file = json.loads(tmp_path.read_text())
        refresh_token = token_file.get("refresh_token")
        if not refresh_token:
            print("[refresh-jj] WARN: no refresh_token in exported file", file=sys.stderr)
            return None

        resp = requests.post(
            "https://oauth2.googleapis.com/token",
            data={
                "client_id": creds["client_id"],
                "client_secret": creds["client_secret"],
                "refresh_token": refresh_token,
                "grant_type": "refresh_token",
            },
            timeout=15,
        )
        if resp.status_code != 200:
            print(f"[refresh-jj] WARN: token refresh failed: {resp.status_code} {resp.text[:200]}", file=sys.stderr)
            return None
        return resp.json().get("access_token")
    finally:
        try:
            tmp_path.unlink(missing_ok=True)
        except OSError:
            pass


def _list_sheet_tabs(sheet_id: str, access_token: str) -> list[str]:
    """Return all tab (sub-sheet) names in the spreadsheet via Sheets API."""
    resp = requests.get(
        f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}",
        headers={"Authorization": f"Bearer {access_token}"},
        params={"fields": "sheets(properties(title))"},
        timeout=15,
    )
    if resp.status_code != 200:
        print(
            f"[refresh-jj] WARN: tab listing failed for {sheet_id}: "
            f"{resp.status_code} {resp.text[:150]}",
            file=sys.stderr,
        )
        return []
    return [
        s["properties"]["title"]
        for s in resp.json().get("sheets", [])
        if s.get("properties", {}).get("title")
    ]


def _read_sheet_range(sheet_id: str, range_a1: str) -> list[list[str]] | None:
    """Read a range via gog. Returns rows-of-cells or None on failure."""
    try:
        out = subprocess.run(
            ["gog", "sheets", "get", sheet_id, range_a1, "--json"],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        print(f"[refresh-jj] gog call failed for {sheet_id}: {e}", file=sys.stderr)
        return None
    if out.returncode != 0:
        print(
            f"[refresh-jj] WARN: gog returned {out.returncode} for {sheet_id} "
            f"range={range_a1}: {out.stderr[:200]}",
            file=sys.stderr,
        )
        return None
    try:
        data = json.loads(out.stdout)
    except json.JSONDecodeError:
        print(f"[refresh-jj] WARN: bad JSON from gog for {sheet_id}", file=sys.stderr)
        return None
    # gog returns either {"values": [[...]]} or a list directly depending on version
    if isinstance(data, dict):
        return data.get("values") or []
    return data if isinstance(data, list) else []


def _scan_tab_dials(sheet_id: str, tab_name: str | None) -> list[date]:
    """Read T2:V from one tab. tab_name=None defaults to the first tab."""
    range_str = "T2:V" if tab_name is None else f"'{tab_name}'!T2:V"
    rows = _read_sheet_range(sheet_id, range_str)
    if rows is None:
        return []
    dials: list[date] = []
    for row in rows:
        first_call = row[0] if len(row) > 0 else ""
        second_call = row[2] if len(row) > 2 else ""
        for raw in (first_call, second_call):
            d = _normalize_date(raw)
            if d:
                dials.append(d)
    return dials


def _scan_niche_dials(
    sheet_id: str,
    niche_name: str,
    access_token: str | None = None,
) -> list[date]:
    """Aggregate dials across the working tab + every Call Log tab.

    Per `feedback_jj_call_date_from_field_not_tab.md`, dial counts come from
    Call Date field values, but JJ rolls deals through tabs as a working list
    — so a dial logged on a 4.21.26 Call Log tab might have a 4.24.26 date.
    We must scan every tab to find them all.

    Two column schemas in the wild:
      OLD (e.g. Art Storage "Active" tab): T=JJ: Call Date, V=JJ: Owner Sentiment
      NEW (e.g. Premium Pest "Full Target List"): T=JJ: 1st Call Date, V=JJ: 2nd Call Date

    Reading T:V handles both — sentiment text in V on the old schema fails
    the date regex and is filtered out by `_normalize_date`.
    """
    # Always scan the working tab (first tab, no name needed)
    dials = _scan_tab_dials(sheet_id, None)

    # If we have an access token, also enumerate + scan Call Log tabs
    call_log_count = 0
    if access_token:
        tabs = _list_sheet_tabs(sheet_id, access_token)
        call_log_tabs = [t for t in tabs if _CALL_LOG_TAB_RE.match(t)]
        for tab in call_log_tabs:
            dials.extend(_scan_tab_dials(sheet_id, tab))
            call_log_count += 1

    print(
        f"[refresh-jj] {niche_name}: {len(dials)} dials "
        f"(working tab + {call_log_count} Call Log tabs)",
        file=sys.stderr,
    )
    return dials


def _weekly_buckets(end: date, weeks: int = 12) -> list[tuple[date, date]]:
    """Return [oldest .. newest] (week_start, week_end) ranges, each 7 days."""
    out = []
    for offset in range(weeks - 1, -1, -1):
        week_end = end - timedelta(days=offset * 7)
        week_start = week_end - timedelta(days=6)
        out.append((week_start, week_end))
    return out


def _build_snapshot() -> dict:
    today = date.today()
    all_dials: list[date] = []
    per_niche: dict[str, int] = {}

    access_token = _get_access_token()
    if access_token:
        print("[refresh-jj] OAuth refresh ok — Call Log tab enumeration enabled", file=sys.stderr)
    else:
        print("[refresh-jj] OAuth refresh failed — falling back to working-tab-only scan", file=sys.stderr)

    for niche, sheet_id in NICHE_SHEETS.items():
        dials = _scan_niche_dials(sheet_id, niche, access_token=access_token)
        per_niche[niche] = len(dials)
        all_dials.extend(dials)

    # Daily counts (last 90 days for granularity)
    cutoff = today - timedelta(days=90)
    by_day: Counter[str] = Counter()
    for d in all_dials:
        if d >= cutoff:
            by_day[d.isoformat()] += 1

    # Weekly buckets (12)
    buckets = _weekly_buckets(today, weeks=12)
    weekly_counts = []
    for ws, we in buckets:
        n = sum(1 for d in all_dials if ws <= d <= we)
        weekly_counts.append({
            "week_start": ws.isoformat(),
            "week_end": we.isoformat(),
            "dials": n,
        })

    week_start = today - timedelta(days=6)
    dials_today = sum(1 for d in all_dials if d == today)
    dials_this_week = sum(1 for d in all_dials if week_start <= d <= today)
    dials_lifetime = len(all_dials)

    return {
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "niches_scanned": list(NICHE_SHEETS.keys()),
        "per_niche_lifetime": per_niche,
        "dials_today": dials_today,
        "dials_this_week": dials_this_week,
        "dials_lifetime": dials_lifetime,
        "by_day": dict(by_day),
        "weekly_buckets": weekly_counts,
    }


def main() -> int:
    snapshot = _build_snapshot()
    SNAPSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    SNAPSHOT_PATH.write_text(json.dumps(snapshot, indent=2))
    print(
        f"[refresh-jj] wrote {SNAPSHOT_PATH} — "
        f"today={snapshot['dials_today']} · this_week={snapshot['dials_this_week']} · "
        f"lifetime={snapshot['dials_lifetime']} across {len(snapshot['niches_scanned'])} niches",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

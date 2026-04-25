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
import re
import subprocess
import sys
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT_PATH = REPO_ROOT / "brain" / "context" / "jj-activity-snapshot.json"

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


def _scan_niche_dials(sheet_id: str, niche_name: str) -> list[date]:
    """Pull col T + col V from the working tab. Return all dial dates.

    Two schemas exist in the wild:
      OLD (e.g. Art Storage "Active" tab): T=JJ: Call Date, V=JJ: Owner Sentiment
      NEW (e.g. Premium Pest "Full Target List"): T=JJ: 1st Call Date, V=JJ: 2nd Call Date

    Reading T:V handles both — sentiment text in V on the old schema fails the
    date regex and is filtered out by `_normalize_date`. Omitting the tab name
    defaults to the first tab, which is the working tab for every known niche.
    """
    rows = _read_sheet_range(sheet_id, "T2:V")
    if rows is None:
        return []
    dials: list[date] = []
    for row in rows:
        # row may be shorter than 3 cells if trailing cells are empty
        first_call = row[0] if len(row) > 0 else ""
        second_call = row[2] if len(row) > 2 else ""
        for raw in (first_call, second_call):
            d = _normalize_date(raw)
            if d:
                dials.append(d)
    print(f"[refresh-jj] {niche_name}: {len(dials)} dials found", file=sys.stderr)
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

    for niche, sheet_id in NICHE_SHEETS.items():
        dials = _scan_niche_dials(sheet_id, niche)
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

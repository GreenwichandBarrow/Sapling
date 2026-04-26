#!/usr/bin/env python3
"""Saturday archive Sheet export — Phase D of dashboard-as-source pivot.

Reads a weekly tracker vault file, parses metrics, appends one column to
the Weekly Topline tab of the archive Sheet (`1NGGZY...`).

Idempotent — skip if a column with header `Week ending M/D/YY` already
exists. Defaults to --dry-run; pass --commit to actually write to the Sheet.

Scope note: only Weekly Topline is written. Weekly Detail has a hybrid
time-series + per-niche column layout — handled as a follow-up task.
The dashboard's Zone 6 already shows per-niche breakdown.

Usage:
    python3 scripts/export_weekly_archive_to_sheet.py                   # dry-run, last Friday
    python3 scripts/export_weekly_archive_to_sheet.py --commit          # live write
    python3 scripts/export_weekly_archive_to_sheet.py --week-ending 2026-04-24
    python3 scripts/export_weekly_archive_to_sheet.py --week-ending 2026-04-24 --commit
    python3 scripts/export_weekly_archive_to_sheet.py --week-ending 2026-04-24 --commit --force
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

ARCHIVE_SHEET_ID = "1NGGZY_iq9h8cNzLAXSJ1vTcsfXWNU9oin2RiOMtl9NE"
TOPLINE_TAB = "Weekly Topline"
GOG_ACCOUNT = "kay.s@greenwichandbarrow.com"

REPO_ROOT = Path(__file__).resolve().parent.parent
VAULT_TRACKERS_DIR = REPO_ROOT / "brain" / "trackers" / "weekly"

# Mapping from Topline metric label (col A) to vault metric key.
# Each row in Weekly Topline rows 4-8 maps to one entry below in order.
# `vault_key` matches the key in dashboard.snapshot.snapshot_weekly()'s
# metrics dict; `default` is used when key is absent (LOIs Signed today).
TOPLINE_ROWS = [
    # (sheet_row_label, vault_metric_key, default_when_missing)
    ("Meaningful Owner Conversations", "owner_conversations", 0),
    ("NDAs Signed",                    "ndas_signed",         0),
    ("Financials Received",            "financials_received", 0),
    ("LOIs Submitted",                 "lois_submitted",      0),
    ("LOIs Signed",                    None,                   0),  # not yet on dashboard
]


def _last_friday(today: date) -> date:
    delta = (today.isoweekday() - 5) % 7
    return today - timedelta(days=delta)


def _column_letter(col_idx: int) -> str:
    """1-indexed column number → A1 letter (1=A, 27=AA)."""
    s = ""
    while col_idx > 0:
        col_idx, r = divmod(col_idx - 1, 26)
        s = chr(65 + r) + s
    return s


def _gog_get(range_a1: str) -> list[list[str]]:
    out = subprocess.run(
        ["gog", "sheets", "get", "-a", GOG_ACCOUNT, ARCHIVE_SHEET_ID, range_a1, "--json"],
        capture_output=True, text=True, timeout=30,
    )
    if out.returncode != 0:
        raise RuntimeError(f"gog get failed for {range_a1}: {out.stderr[:300]}")
    if not out.stdout.strip():
        return []
    data = json.loads(out.stdout)
    if isinstance(data, dict):
        return data.get("values") or []
    return data if isinstance(data, list) else []


def _gog_update(range_a1: str, values: list[list[str]]) -> None:
    # gog --values-json expects a raw 2D array, not {"values": [...]}.
    payload = json.dumps(values)
    out = subprocess.run(
        ["gog", "sheets", "update", "-a", GOG_ACCOUNT, ARCHIVE_SHEET_ID, range_a1,
         "--values-json", payload, "--input", "USER_ENTERED"],
        capture_output=True, text=True, timeout=30,
    )
    if out.returncode != 0:
        raise RuntimeError(f"gog update failed for {range_a1}: {out.stderr[:400]}")


_FRONTMATTER_DATE_RE = re.compile(r"^date:\s*(\d{4}-\d{2}-\d{2})", re.MULTILINE)
_TABLE_ROW_RE = re.compile(
    r"^\|\s*([A-Za-z][^|]*?)\s*\|\s*([^|]+?)\s*\|", re.MULTILINE
)


def _parse_vault_metrics(week_ending: date) -> dict[str, int]:
    """Parse the dashboard-snapshot tracker file and extract metric ints.

    Tolerates both v2.0.0 (dashboard-source) and the legacy 1.0.0 format —
    the metric labels are stable enough to grep across both.
    """
    path = VAULT_TRACKERS_DIR / f"{week_ending.isoformat()}-weekly-tracker.md"
    if not path.exists():
        raise FileNotFoundError(f"Vault tracker file missing: {path}")
    text = path.read_text(errors="replace")

    # Map "loose" label (lowercased, alphanumeric only) → metric value
    metrics: dict[str, int] = {}
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 2:
            continue
        label = parts[0]
        value_str = parts[1]
        # Extract first integer in the value cell ("3 (plus 8 XPX in Superhuman)" → 3)
        m = re.search(r"-?\d+", value_str)
        if not m:
            continue
        value = int(m.group(0))
        # Normalize label
        key = re.sub(r"[^a-z0-9]", "", label.lower())
        metrics[key] = value

    # Map vault keys back to standard names
    return {
        "owner_conversations": (
            metrics.get("ownerconversations")
            or metrics.get("meaningfulownerconversations")
            or metrics.get("meaningfulowner conversations")
            or 0
        ),
        "ndas_signed": metrics.get("ndassigned", 0),
        "financials_received": metrics.get("financialsreceived", 0),
        "lois_submitted": metrics.get("loissubmitted", 0),
        "lois_signed": metrics.get("loissigned", 0),
    }


def _column_header_for_week(week_ending: date) -> str:
    """Match the Sheet's existing header convention: 'Week ending M/D/YY'.
    Earlier columns drop the year ('Week ending 3/20'); newer ones include
    it ('Week ending 4/17/26'). We always include the year for clarity.
    """
    # %-m / %-d are platform-specific; use lstrip fallback for portability.
    m = str(week_ending.month)
    d = str(week_ending.day)
    yy = week_ending.strftime("%y")
    return f"Week ending {m}/{d}/{yy}"


def _existing_headers() -> list[str]:
    """Return Weekly Topline row 1 (the headers row)."""
    rows = _gog_get(f"'{TOPLINE_TAB}'!A1:Z1")
    if not rows:
        return []
    return rows[0] if rows[0] else []


def _find_existing_column_idx(headers: list[str], target: str) -> int | None:
    for i, h in enumerate(headers):
        if h.strip() == target:
            return i + 1  # 1-indexed
    return None


def _next_empty_column_idx(headers: list[str]) -> int:
    """Right-most non-empty header column + 1 (1-indexed)."""
    last_filled = 0
    for i, h in enumerate(headers):
        if h.strip():
            last_filled = i + 1
    return last_filled + 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Append weekly tracker column to archive Sheet (Phase D)."
    )
    parser.add_argument("--week-ending", help="ISO date YYYY-MM-DD (default: most recent Friday)")
    parser.add_argument("--commit", action="store_true",
                        help="Actually write to Sheet. Without this flag, runs in dry-run mode.")
    parser.add_argument("--force", action="store_true",
                        help="Overwrite existing column even if header already present.")
    args = parser.parse_args()

    week_ending = (
        date.fromisoformat(args.week_ending) if args.week_ending else _last_friday(date.today())
    )
    header_text = _column_header_for_week(week_ending)
    print(f"Target week ending: {week_ending} ({header_text})")
    print(f"Mode: {'COMMIT' if args.commit else 'DRY-RUN'}")

    metrics = _parse_vault_metrics(week_ending)
    print(f"Parsed metrics from vault: {metrics}")

    headers = _existing_headers()
    print(f"Sheet headers in row 1: {headers}")

    existing_col = _find_existing_column_idx(headers, header_text)
    if existing_col is not None and not args.force:
        print(f"Column '{header_text}' already exists at col {_column_letter(existing_col)}; "
              "skipping (idempotent). Pass --force to overwrite.")
        return 0

    target_col = existing_col if existing_col else _next_empty_column_idx(headers)
    target_letter = _column_letter(target_col)
    print(f"Writing to column {target_letter} (col index {target_col})")

    # Build values: header in row 1, blank in row 2-3, metric values in rows 4-8.
    # Sheet rows 4-8 correspond to TOPLINE_ROWS in order.
    values_column = [
        [header_text],          # row 1: header
        [""],                   # row 2: blank
        [""],                   # row 3: blank (KEY METRICS / Target row)
    ]
    for sheet_label, vault_key, default in TOPLINE_ROWS:
        v = metrics.get(vault_key, default) if vault_key else default
        values_column.append([str(v)])

    # Determine A1 range: target_letter + "1:" + target_letter + str(3 + len(TOPLINE_ROWS))
    last_row = 3 + len(TOPLINE_ROWS)
    range_a1 = f"'{TOPLINE_TAB}'!{target_letter}1:{target_letter}{last_row}"
    print(f"Range: {range_a1}")
    print(f"Values to write (one per row, top → bottom):")
    for i, v in enumerate(values_column, start=1):
        print(f"  row {i}: {v[0]!r}")

    if not args.commit:
        print()
        print("DRY-RUN complete. Re-run with --commit to write to Sheet.")
        return 0

    _gog_update(range_a1, values_column)
    print(f"Wrote column {target_letter} ('{header_text}') to '{TOPLINE_TAB}'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

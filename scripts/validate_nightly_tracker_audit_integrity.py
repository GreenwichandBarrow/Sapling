#!/usr/bin/env python3
"""
Wrapper-level integrity validator for nightly-tracker-audit scheduled runs.

Runs as POST_RUN_CHECK after launchd wrapper completes. Independent of skill-internal
validation. Catches silent-success failures where Claude exits 0 but the Industry
Research Tracker WEEKLY REVIEW tab is still dirty (Tabled/Killed rows lingering,
blank gaps, non-sequential rank).

Exit codes:
  0  Pass — WEEKLY REVIEW is clean: no Tabled/Killed rows, no mid-list blanks, sequential rank
  2  Fail — one or more invariants violated

Usage:
  python3 validate_nightly_tracker_audit_integrity.py
"""

import json
import subprocess
import sys


SHEET_ID = "1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins"
TAB = "WEEKLY REVIEW"
DATA_RANGE = "A4:K100"  # Row 3 is headers; data starts row 4
COL_RANK = 0
COL_NICHE = 1
COL_STATUS = 2


def get_data_rows(sheet_id: str, tab: str, rng: str) -> list[list[str]]:
    result = subprocess.run(
        ["gog", "sheets", "get", sheet_id, f"'{tab}'!{rng}", "--json"],
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode != 0:
        raise RuntimeError(f"gog sheets get failed: {result.stderr.strip()}")
    data = json.loads(result.stdout)
    return data.get("values", [])


def is_blank(row: list[str]) -> bool:
    """A row is blank if it has no Niche Hypothesis (Col B)."""
    if len(row) <= COL_NICHE:
        return True
    return not row[COL_NICHE].strip()


def main() -> int:
    try:
        rows = get_data_rows(SHEET_ID, TAB, DATA_RANGE)
    except Exception as e:
        print(f"NIGHTLY-TRACKER-AUDIT VALIDATOR FAILED: could not read sheet: {e}", file=sys.stderr)
        return 2

    failures = []

    # Trim trailing blanks for analysis
    while rows and is_blank(rows[-1]):
        rows.pop()

    if not rows:
        print("NIGHTLY-TRACKER-AUDIT VALIDATOR FAILED: WEEKLY REVIEW has no data rows", file=sys.stderr)
        return 2

    # Check 1: No Tabled/Killed rows
    bad_status_rows = []
    for i, row in enumerate(rows, start=4):  # row index in sheet (data starts row 4)
        if is_blank(row):
            continue
        status = row[COL_STATUS].strip() if len(row) > COL_STATUS else ""
        if status in ("Tabled", "Killed"):
            bad_status_rows.append(f"row {i} ({row[COL_NICHE]}) has status={status!r} — should be in {status.upper()} tab")
    if bad_status_rows:
        failures.append("Tabled/Killed rows still in WEEKLY REVIEW:\n    " + "\n    ".join(bad_status_rows))

    # Check 2: No blank rows in middle
    seen_data = False
    seen_blank_after_data = False
    blank_gap_rows = []
    for i, row in enumerate(rows, start=4):
        if is_blank(row):
            if seen_data:
                seen_blank_after_data = True
        else:
            if seen_blank_after_data:
                blank_gap_rows.append(f"row {i} ({row[COL_NICHE]}) follows a blank gap")
            seen_data = True
    if blank_gap_rows:
        failures.append("Blank gaps between data rows:\n    " + "\n    ".join(blank_gap_rows))

    # Check 3: Rank column is sequential 1, 2, 3, ... for non-blank rows
    rank_issues = []
    expected_rank = 1
    for i, row in enumerate(rows, start=4):
        if is_blank(row):
            continue
        rank_str = row[COL_RANK].strip() if len(row) > COL_RANK else ""
        try:
            actual_rank = int(rank_str)
        except ValueError:
            rank_issues.append(f"row {i} ({row[COL_NICHE]}): rank={rank_str!r} not a valid integer")
            expected_rank += 1
            continue
        if actual_rank != expected_rank:
            rank_issues.append(f"row {i} ({row[COL_NICHE]}): rank={actual_rank}, expected {expected_rank}")
        expected_rank += 1
    if rank_issues:
        failures.append("Rank column not sequential:\n    " + "\n    ".join(rank_issues))

    if failures:
        print("NIGHTLY-TRACKER-AUDIT VALIDATOR FAILED:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 2

    data_count = sum(1 for r in rows if not is_blank(r))
    print(f"NIGHTLY-TRACKER-AUDIT VALIDATOR PASSED")
    print(f"  WEEKLY REVIEW: {data_count} data rows, no blanks, no Tabled/Killed lingering, rank sequential")
    return 0


if __name__ == "__main__":
    sys.exit(main())

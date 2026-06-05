#!/usr/bin/env python3
"""
Wrapper-level integrity validator for weekly-tracker scheduled runs.

Runs as POST_RUN_CHECK after launchd wrapper completes. Independent of any
internal validation hooks the skill itself uses. Catches silent-success
failures where Claude exits 0 but produced no real artifacts.

Exit codes:
  0  Pass — vault snapshot AND sheet column for current week both present
  2  Fail — one or more artifacts missing/stale

Usage:
  python3 validate_weekly_tracker_integrity.py [--week-ending YYYY-MM-DD]

If --week-ending omitted, computes most-recent Friday from today.
"""

import json
import os
import re
import subprocess
import sys
from datetime import date, datetime, timedelta


SHEET_ID = "1NGGZY_iq9h8cNzLAXSJ1vTcsfXWNU9oin2RiOMtl9NE"
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_SCRIPT_DIR)
VAULT_DIR = os.environ.get(
    "WEEKLY_TRACKER_VAULT_DIR",
    os.path.join(_REPO_ROOT, "brain", "trackers", "weekly"),
)

REQUIRED_SECTIONS = [
    "## Key Metrics",
    "## System Throughput",
    "## Signal Quality",
    "## Pipeline Health",
    "## Channel Performance",
    "## Flags",
]
MIN_SNAPSHOT_BYTES = 1000


def most_recent_friday(today: date) -> date:
    """Return today if Friday, else the most recent past Friday."""
    days_since_friday = (today.weekday() - 4) % 7
    return today - timedelta(days=days_since_friday)


def get_sheet_header_row(sheet_id: str, tab: str) -> list[str]:
    """Read row 1 of the given tab and return non-empty cells."""
    result = subprocess.run(
        ["gog", "sheets", "get", sheet_id, f"'{tab}'!1:1", "--json"],
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode != 0:
        raise RuntimeError(f"gog sheets get failed: {result.stderr.strip()}")
    data = json.loads(result.stdout)
    rows = data.get("values", [])
    if not rows:
        return []
    return [c for c in rows[0] if c and c.strip()]


def expected_column_header(week_ending: date) -> str:
    """Format matching existing sheet convention: 'Week ending M/DD/YY'."""
    return f"Week ending {week_ending.month}/{week_ending.day}/{week_ending.strftime('%y')}"


def vault_snapshot_path(week_ending: date) -> str:
    return os.path.join(VAULT_DIR, f"{week_ending.isoformat()}-weekly-tracker.md")


def validate_vault_snapshot(snapshot: str, week_ending: date) -> list[str]:
    failures: list[str] = []
    if not os.path.exists(snapshot):
        failures.append(
            f"vault snapshot missing: {snapshot} "
            f"(weekly-tracker should write per SKILL.md Step 4.5)"
        )
        return failures

    size = os.path.getsize(snapshot)
    if size < MIN_SNAPSHOT_BYTES:
        failures.append(
            f"vault snapshot suspiciously small ({size} bytes < {MIN_SNAPSHOT_BYTES}): {snapshot}"
        )

    with open(snapshot) as f:
        content = f.read()

    if not content.startswith("---"):
        failures.append(f"vault snapshot has no YAML frontmatter: {snapshot}")
    else:
        fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        if not fm_match:
            failures.append(f"vault snapshot frontmatter unterminated: {snapshot}")
        else:
            fm = fm_match.group(1)
            if f"date: {week_ending.isoformat()}" not in fm:
                failures.append(
                    f"vault snapshot frontmatter date does not match {week_ending}"
                )
            if "type: tracker" not in fm:
                failures.append("vault snapshot frontmatter missing 'type: tracker'")
            if "topic/weekly-tracker" not in fm:
                failures.append("vault snapshot frontmatter missing topic/weekly-tracker tag")

    missing_sections = [section for section in REQUIRED_SECTIONS if section not in content]
    if missing_sections:
        failures.append(f"vault snapshot missing required section(s): {missing_sections}")

    return failures


def main() -> int:
    args = sys.argv[1:]
    if "--week-ending" in args:
        idx = args.index("--week-ending")
        week_ending = datetime.fromisoformat(args[idx + 1]).date()
    else:
        week_ending = most_recent_friday(date.today())

    failures = []

    # Check 1: Vault snapshot file exists and has the expected content shape.
    snapshot = vault_snapshot_path(week_ending)
    failures.extend(validate_vault_snapshot(snapshot, week_ending))

    # Check 2: Sheet has a column for this week-ending in 'Weekly Topline'
    expected = expected_column_header(week_ending)
    try:
        headers = get_sheet_header_row(SHEET_ID, "Weekly Topline")
    except Exception as e:
        failures.append(f"could not read sheet header: {e}")
        headers = []

    # Tolerate variant formats: 'Week ending 4/24/26' vs 'Week ending 4/24'
    expected_short = f"Week ending {week_ending.month}/{week_ending.day}"
    found = any(h.startswith(expected_short) for h in headers)
    if not found:
        latest = headers[-1] if headers else "(no headers)"
        failures.append(
            f"sheet column missing for {expected}; latest header is {latest!r}"
        )

    if failures:
        print(
            f"WEEKLY-TRACKER VALIDATOR FAILED for week ending {week_ending}:",
            file=sys.stderr,
        )
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 2

    print(f"WEEKLY-TRACKER VALIDATOR PASSED for week ending {week_ending}")
    print(f"  vault: {snapshot}")
    print(f"  sheet column: {expected}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

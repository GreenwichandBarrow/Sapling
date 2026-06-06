#!/usr/bin/env python3
"""
Integrity validator for the direct weekly dashboard snapshot.

This validates the artifact produced by scripts/snapshot_weekly_to_vault.py.
It is intentionally separate from validate_weekly_tracker_integrity.py, which
checks the agent-driven weekly tracker and its Google Sheet export.

Exit codes:
  0  Pass - direct weekly snapshot is present and shaped correctly
  2  Fail - artifact missing, stale, or malformed

Usage:
  python3 validate_weekly_snapshot_integrity.py [--week-ending YYYY-MM-DD]
"""

from __future__ import annotations

import os
import re
import sys
from datetime import date, datetime, timedelta


_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_SCRIPT_DIR)
VAULT_DIR = os.environ.get(
    "WEEKLY_SNAPSHOT_VAULT_DIR",
    os.path.join(_REPO_ROOT, "brain", "trackers", "weekly"),
)

REQUIRED_SECTIONS = [
    "## Key Metrics",
    "## Channel Performance",
    "## Per-Niche Breakdown",
    "## Data Sources",
    "## Narrative",
]
REQUIRED_SOURCE_LINES = [
    "**Source:** `dashboard.snapshot.snapshot_weekly()`",
    "- Attio snapshot fresh:",
    "- Operations snapshot fetched:",
    "- Pipeline total deal count:",
    "- Prior week tracker present:",
]
MIN_SNAPSHOT_BYTES = 1000


def most_recent_friday(today: date) -> date:
    """Return today if Friday, else the most recent past Friday."""
    days_since_friday = (today.weekday() - 4) % 7
    return today - timedelta(days=days_since_friday)


def snapshot_path(week_ending: date) -> str:
    return os.path.join(VAULT_DIR, f"{week_ending.isoformat()}-weekly-tracker.md")


def validate_snapshot(snapshot: str, week_ending: date) -> list[str]:
    failures: list[str] = []
    if not os.path.exists(snapshot):
        failures.append(f"weekly dashboard snapshot missing: {snapshot}")
        return failures

    size = os.path.getsize(snapshot)
    if size < MIN_SNAPSHOT_BYTES:
        failures.append(
            f"weekly dashboard snapshot suspiciously small ({size} bytes < {MIN_SNAPSHOT_BYTES}): {snapshot}"
        )

    with open(snapshot) as f:
        content = f.read()

    if not content.startswith("---"):
        failures.append(f"weekly dashboard snapshot has no YAML frontmatter: {snapshot}")
    else:
        fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        if not fm_match:
            failures.append(f"weekly dashboard snapshot frontmatter unterminated: {snapshot}")
        else:
            frontmatter = fm_match.group(1)
            if f"date: {week_ending.isoformat()}" not in frontmatter:
                failures.append(
                    f"weekly dashboard snapshot frontmatter date does not match {week_ending}"
                )
            if "type: tracker" not in frontmatter:
                failures.append("weekly dashboard snapshot frontmatter missing 'type: tracker'")
            if "topic/weekly-tracker" not in frontmatter:
                failures.append("weekly dashboard snapshot frontmatter missing topic/weekly-tracker tag")
            if "source/dashboard-snapshot" not in frontmatter:
                failures.append(
                    "weekly dashboard snapshot frontmatter missing source/dashboard-snapshot tag"
                )

    missing_sections = [section for section in REQUIRED_SECTIONS if section not in content]
    if missing_sections:
        failures.append(f"weekly dashboard snapshot missing required section(s): {missing_sections}")

    missing_source_lines = [line for line in REQUIRED_SOURCE_LINES if line not in content]
    if missing_source_lines:
        failures.append(
            f"weekly dashboard snapshot missing data-source line(s): {missing_source_lines}"
        )

    if "| Metric | This Week | Prior Week | Delta |" not in content:
        failures.append("weekly dashboard snapshot missing Key Metrics table")
    if "| Channel | Sent | Reply | Positive |" not in content:
        failures.append("weekly dashboard snapshot missing Channel Performance table")

    return failures


def parse_week_ending(args: list[str]) -> date:
    if "--week-ending" in args:
        idx = args.index("--week-ending")
        try:
            return datetime.fromisoformat(args[idx + 1]).date()
        except IndexError:
            raise SystemExit("--week-ending requires YYYY-MM-DD")
    return most_recent_friday(date.today())


def main() -> int:
    week_ending = parse_week_ending(sys.argv[1:])
    snapshot = snapshot_path(week_ending)
    failures = validate_snapshot(snapshot, week_ending)

    if failures:
        print(
            f"WEEKLY-SNAPSHOT VALIDATOR FAILED for week ending {week_ending}:",
            file=sys.stderr,
        )
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        return 2

    print(f"WEEKLY-SNAPSHOT VALIDATOR PASSED for week ending {week_ending}")
    print(f"  vault: {snapshot}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

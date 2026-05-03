#!/usr/bin/env python3
"""
Wrapper-level integrity validator for deal-aggregator scheduled runs.

Runs as POST_RUN_CHECK after launchd wrapper completes. Independent of skill-internal
validation. Catches silent-success failures where Claude exits 0 but no artifact
landed (4/27 + 4/30 morning incidents — wrapper exited 0, no scan happened, the
afternoon run had to flag "morning artifact missing" the next day).

Three modes (selected by --mode flag):
  morning    → expects brain/context/deal-aggregator-scan-{date}.md
  afternoon  → expects brain/context/deal-aggregator-scan-{date}-afternoon.md
  digest     → expects brain/trackers/weekly/{date}-deal-aggregator-digest.md

All three artifacts share required structural elements:
  - YAML frontmatter
  - Minimum byte threshold (200 bytes)
  - Required section headers per the SKILL.md template

Exit codes:
  0  Pass — artifact exists, has frontmatter, has all required section headers
  2  Fail — artifact missing or malformed

Usage:
  python3 validate_deal_aggregator_integrity.py --mode morning [--date YYYY-MM-DD]
  python3 validate_deal_aggregator_integrity.py --mode afternoon [--date YYYY-MM-DD]
  python3 validate_deal_aggregator_integrity.py --mode digest [--date YYYY-MM-DD]
"""

import argparse
import os
import re
import sys
from datetime import date, datetime


VAULT_DIR = "/Users/kaycschneider/Documents/AI Operations/brain/context"
WEEKLY_DIR = "/Users/kaycschneider/Documents/AI Operations/brain/trackers/weekly"

# Required section headers per SKILL.md "Results File" template (morning + afternoon).
DAILY_SECTIONS = [
    "## Deals Surfaced",
    "## Email Inbound Deals",
    "## Near Misses",
    "## Source Scorecard",
    "## Volume Check",
]

# Required section headers per SKILL.md weekly_digest template.
DIGEST_SECTIONS = [
    "## 1. Source Productivity",
    "## 2. Volume Check",
    "## 3. Proposed Additions",
    "## 4. Proposed Retirements",
    "## 5. Recommended Actions",
]

MIN_BYTES = 200


def validate_artifact(artifact_path: str, required_sections: list, run_date: date) -> list:
    """Return a list of failure strings (empty list = pass)."""
    failures = []

    if not os.path.exists(artifact_path):
        failures.append(f"artifact missing: {artifact_path}")
        return failures

    size = os.path.getsize(artifact_path)
    if size < MIN_BYTES:
        failures.append(f"artifact suspiciously small ({size} bytes < {MIN_BYTES}): {artifact_path}")

    with open(artifact_path) as f:
        content = f.read()

    # Frontmatter check
    if not content.startswith("---"):
        failures.append(f"artifact has no YAML frontmatter (must start with '---'): {artifact_path}")
    else:
        fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        if not fm_match:
            failures.append(f"frontmatter unterminated: {artifact_path}")
        else:
            fm = fm_match.group(1)
            # Date field must match run date
            if f"date: {run_date.isoformat()}" not in fm:
                failures.append(
                    f"frontmatter date does not match run date {run_date} (artifact: {artifact_path})"
                )

    # Section headers — every required section must appear
    missing = [s for s in required_sections if s not in content]
    if missing:
        failures.append(
            f"missing required section header(s) {missing} in {artifact_path}"
        )

    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        required=True,
        choices=["morning", "afternoon", "digest"],
        help="Which deal-aggregator artifact to validate",
    )
    parser.add_argument(
        "--date",
        help="Date in YYYY-MM-DD (default: today)",
    )
    args = parser.parse_args()

    run_date = (
        datetime.fromisoformat(args.date).date() if args.date else date.today()
    )

    if args.mode == "morning":
        artifact = os.path.join(VAULT_DIR, f"deal-aggregator-scan-{run_date.isoformat()}.md")
        sections = DAILY_SECTIONS
    elif args.mode == "afternoon":
        artifact = os.path.join(
            VAULT_DIR, f"deal-aggregator-scan-{run_date.isoformat()}-afternoon.md"
        )
        sections = DAILY_SECTIONS
    else:  # digest
        artifact = os.path.join(
            WEEKLY_DIR, f"{run_date.isoformat()}-deal-aggregator-digest.md"
        )
        sections = DIGEST_SECTIONS

    failures = validate_artifact(artifact, sections, run_date)

    if failures:
        print(
            f"DEAL-AGGREGATOR VALIDATOR FAILED ({args.mode}) for {run_date}:",
            file=sys.stderr,
        )
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 2

    print(f"DEAL-AGGREGATOR VALIDATOR PASSED ({args.mode}) for {run_date}")
    print(f"  artifact: {artifact}")
    print(f"  size: {os.path.getsize(artifact)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())

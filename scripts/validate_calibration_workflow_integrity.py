#!/usr/bin/env python3
"""Validate the Codex headless calibration workflow artifact."""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REQUIRED_HEADINGS = [
    "# Codex Calibration Report - {date}",
    "## Executive Summary",
    "## Trace Inventory",
    "## Findings",
    "## Proposed Changes",
    "## Deferred or Blocked",
    "## Safety Notes",
    "## Validation",
]
ALLOWED_STATUSES = {"proposed", "no_action", "blocked"}


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def validate_report_text(text: str, report_date: str) -> tuple[list[str], str | None]:
    failures: list[str] = []

    if len(text.encode("utf-8")) < 800:
        failures.append("report is shorter than 800 bytes")

    frontmatter = parse_frontmatter(text)
    expected = {
        "date": report_date,
        "type": "output",
        "output_type": "calibration",
        "runtime": "codex",
    }
    for key, value in expected.items():
        if frontmatter.get(key) != value:
            failures.append(f"frontmatter {key}={frontmatter.get(key)!r}, expected {value!r}")

    status = frontmatter.get("status")
    if status not in ALLOWED_STATUSES:
        failures.append(f"frontmatter status={status!r}, expected one of {sorted(ALLOWED_STATUSES)}")

    for heading in REQUIRED_HEADINGS:
        required = heading.format(date=report_date)
        if required not in text:
            failures.append(f"missing heading: {required}")

    lower = text.lower()
    for phrase in ("no email", "no commit", "no slack"):
        if phrase not in lower:
            failures.append(f"safety note missing phrase containing: {phrase}")

    forbidden_waits = [
        r"\bapply all\b",
        r"\bselect 1\b",
        r"\bwant me to\b",
        r"\bshould i\b",
        r"\bwaiting for approval\b",
    ]
    for pattern in forbidden_waits:
        if re.search(pattern, lower):
            failures.append(f"report contains interactive/waiting phrasing matching {pattern!r}")

    return failures, status


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=date.today().isoformat())
    args = parser.parse_args()

    report = REPO_ROOT / "brain" / "outputs" / "calibrations" / f"{args.date}-codex-calibration.md"
    if not report.exists():
        print(f"CALIBRATION VALIDATOR FAILED: missing report {report}", file=sys.stderr)
        return 2

    text = report.read_text(encoding="utf-8")
    failures, status = validate_report_text(text, args.date)

    if failures:
        print("CALIBRATION VALIDATOR FAILED:", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        return 2

    print("CALIBRATION VALIDATOR PASSED")
    print(f"  report: {report.name}, status={status}, bytes={len(text.encode('utf-8'))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

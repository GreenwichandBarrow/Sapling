#!/usr/bin/env python3
"""
Wrapper-level integrity validator for niche-intelligence scheduled Tuesday runs.

Runs as POST_RUN_CHECK after launchd wrapper completes. Independent of skill-internal
validation. Catches silent-success failures where Claude exits 0 but produced no
real artifacts (the failure mode that hit 4/14, 4/21, 4/28 — wrapper fell through
to bare `/niche-intelligence` with no headless prompt).

Validates:
  1. Markdown report exists at brain/outputs/{date}-niche-intelligence-report.md
     - Has YAML frontmatter with matching date and type
     - File ≥500 bytes (sanity floor — empty stubs are not real outputs)
  2. JSON sidecar exists at brain/trackers/niches/niche-intel-{date}.json
     - Parses cleanly
     - Has all required fields (run_date, run_mode, niches_evaluated, etc.)
     - niches_evaluated ≥ 1 (Tuesday run with 0 niches = silent failure)
     - tracker_updated is True
     - runtime_seconds > 0

Exit codes:
  0  Pass — both artifacts present and well-formed
  2  Fail — one or more invariants violated

Usage:
  python3 validate_niche_intelligence_integrity.py [--date YYYY-MM-DD]

If --date omitted, uses today's date.
"""

import json
import os
import re
import sys
from datetime import date, datetime


VAULT_ROOT = "/Users/kaycschneider/Documents/AI Operations/brain"
REPORT_DIR = os.path.join(VAULT_ROOT, "outputs")
SIDECAR_DIR = os.path.join(VAULT_ROOT, "trackers", "niches")

REQUIRED_SIDECAR_FIELDS = [
    "run_date",
    "run_mode",
    "niches_evaluated",
    "niches_identified",
    "one_pagers_written",
    "scorecards_written",
    "tracker_updated",
    "runtime_seconds",
]


def report_path(run_date: date) -> str:
    return os.path.join(REPORT_DIR, f"{run_date.isoformat()}-niche-intelligence-report.md")


def sidecar_path(run_date: date) -> str:
    return os.path.join(SIDECAR_DIR, f"niche-intel-{run_date.isoformat()}.json")


def validate_report(run_date: date, failures: list[str]) -> None:
    path = report_path(run_date)
    if not os.path.exists(path):
        failures.append(f"markdown report missing: {path}")
        return

    size = os.path.getsize(path)
    if size < 500:
        failures.append(
            f"markdown report suspiciously small ({size} bytes) — likely empty stub: {path}"
        )

    with open(path) as f:
        content = f.read()

    if not content.startswith("---"):
        failures.append(f"markdown report has no YAML frontmatter (must start with '---'): {path}")
        return

    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        failures.append(f"markdown report frontmatter unterminated: {path}")
        return

    fm = fm_match.group(1)
    if f"date: {run_date.isoformat()}" not in fm:
        failures.append(
            f"markdown report frontmatter date does not match run date {run_date}"
        )
    if "type: output" not in fm:
        failures.append("markdown report frontmatter missing 'type: output'")


def validate_sidecar(run_date: date, failures: list[str]) -> None:
    path = sidecar_path(run_date)
    if not os.path.exists(path):
        failures.append(f"JSON sidecar missing: {path}")
        return

    try:
        with open(path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        failures.append(f"JSON sidecar does not parse: {path} ({e})")
        return

    if not isinstance(data, dict):
        failures.append(f"JSON sidecar is not an object: {path}")
        return

    missing = [k for k in REQUIRED_SIDECAR_FIELDS if k not in data]
    if missing:
        failures.append(f"JSON sidecar missing required fields: {missing}")
        return

    # Field-level sanity checks
    if data.get("run_date") != run_date.isoformat():
        failures.append(
            f"JSON sidecar run_date={data.get('run_date')!r}, expected {run_date.isoformat()!r}"
        )

    if data.get("run_mode") != "tuesday":
        failures.append(
            f"JSON sidecar run_mode={data.get('run_mode')!r}, expected 'tuesday'"
        )

    niches_evaluated = data.get("niches_evaluated")
    if not isinstance(niches_evaluated, int) or niches_evaluated < 1:
        failures.append(
            f"JSON sidecar niches_evaluated={niches_evaluated!r} — must be int ≥1 "
            "(Tuesday run with 0 niches = silent failure)"
        )

    for int_field in ("niches_identified", "one_pagers_written", "scorecards_written"):
        v = data.get(int_field)
        if not isinstance(v, int) or v < 0:
            failures.append(f"JSON sidecar {int_field}={v!r} — must be int ≥0")

    if not isinstance(data.get("tracker_updated"), bool):
        failures.append(
            f"JSON sidecar tracker_updated={data.get('tracker_updated')!r} — must be bool"
        )
    elif data["tracker_updated"] is not True:
        failures.append(
            "JSON sidecar tracker_updated=False — Step 5 (Industry Research Tracker update) did not run"
        )

    runtime = data.get("runtime_seconds")
    if not isinstance(runtime, (int, float)) or runtime <= 0:
        failures.append(
            f"JSON sidecar runtime_seconds={runtime!r} — must be positive number"
        )


def main() -> int:
    args = sys.argv[1:]
    if args and not args[0].startswith("--"):
        # Positional date arg (matches POST_RUN_CHECK pattern: `... $TODAY`)
        run_date = datetime.fromisoformat(args[0]).date()
    elif "--date" in args:
        idx = args.index("--date")
        run_date = datetime.fromisoformat(args[idx + 1]).date()
    else:
        run_date = date.today()

    failures: list[str] = []
    validate_report(run_date, failures)
    validate_sidecar(run_date, failures)

    if failures:
        print(f"NICHE-INTELLIGENCE VALIDATOR FAILED for {run_date}:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 2

    print(f"NICHE-INTELLIGENCE VALIDATOR PASSED for {run_date}")
    print(f"  report: {report_path(run_date)}")
    print(f"  sidecar: {sidecar_path(run_date)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

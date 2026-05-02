#!/usr/bin/env python3
"""Wrapper-level integrity validator for launchd-debugger scheduled runs.

Runs as POST_RUN_CHECK after launchd wrapper completes. Confirms the daily
artifact at brain/trackers/health/launchd-debugger-{TODAY}.json exists and
contains every required field. Catches the silent-success failure mode where
Claude exits 0 but never wrote the artifact (the morning briefing pipeline
relies on this artifact to know whether overnight self-healing happened).

Required artifact fields:
  date, scan_started_at, scan_finished_at, failures_detected,
  fixes_attempted, fixes_succeeded, surfaces_to_slack, runtime_seconds,
  results

Per-result required fields (when failures_detected > 0):
  job, cause, action

Soft-checks (warn but pass):
  - runtime_seconds in plausible range (10-900)
  - failures_detected == len(results)
  - fixes_attempted >= fixes_succeeded
  - surfaces_to_slack + fixes_succeeded == failures_detected (every failure
    either healed or surfaced; nothing left orphaned)

Exit codes:
  0 — artifact exists and passes all required-field checks
  2 — artifact missing or malformed

Usage:
  python3 validate_launchd_debugger_integrity.py
"""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ARTIFACT_DIR = REPO_ROOT / "brain" / "trackers" / "health"

REQUIRED_TOP_FIELDS = {
    "date",
    "scan_started_at",
    "scan_finished_at",
    "failures_detected",
    "fixes_attempted",
    "fixes_succeeded",
    "surfaces_to_slack",
    "runtime_seconds",
    "results",
}

REQUIRED_RESULT_FIELDS = {"job", "cause", "action"}
ALLOWED_ACTIONS = {"FIX", "SURFACE"}


def main() -> int:
    today = date.today().isoformat()
    artifact_path = ARTIFACT_DIR / f"launchd-debugger-{today}.json"

    if not artifact_path.exists():
        print(
            f"LAUNCHD-DEBUGGER VALIDATOR FAILED: artifact missing at {artifact_path}",
            file=sys.stderr,
        )
        return 2

    try:
        data = json.loads(artifact_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        print(
            f"LAUNCHD-DEBUGGER VALIDATOR FAILED: artifact unreadable: {exc}",
            file=sys.stderr,
        )
        return 2

    failures: list[str] = []

    missing = REQUIRED_TOP_FIELDS - set(data.keys())
    if missing:
        failures.append(f"missing required top-level fields: {sorted(missing)}")

    # Type checks on counts.
    for field in (
        "failures_detected",
        "fixes_attempted",
        "fixes_succeeded",
        "surfaces_to_slack",
        "runtime_seconds",
    ):
        if field in data and not isinstance(data[field], int):
            failures.append(f"{field} is not an int: {type(data[field]).__name__}")

    # Date sanity.
    if data.get("date") != today:
        failures.append(f"date field {data.get('date')!r} does not match today {today!r}")

    # Results structure.
    results = data.get("results")
    if not isinstance(results, list):
        failures.append("results is not a list")
        results = []

    declared = data.get("failures_detected", -1)
    if isinstance(declared, int) and declared >= 0 and declared != len(results):
        failures.append(
            f"failures_detected ({declared}) != len(results) ({len(results)})"
        )

    for i, result in enumerate(results):
        if not isinstance(result, dict):
            failures.append(f"results[{i}] is not a dict")
            continue
        missing_r = REQUIRED_RESULT_FIELDS - set(result.keys())
        if missing_r:
            failures.append(f"results[{i}] missing fields: {sorted(missing_r)}")
        action = result.get("action")
        if action and action not in ALLOWED_ACTIONS:
            failures.append(
                f"results[{i}] action={action!r} not in {ALLOWED_ACTIONS}"
            )

    # Soft accounting check: every failure must either be fixed, surfaced to
    # Slack, OR suppressed (known-incident / cross-day-dedup) — v1.1 added
    # suppression so a SURFACE may legitimately have slack_posted=false.
    # Count suppressed = SURFACE results with slack_posted == False.
    fixes_ok = data.get("fixes_succeeded", 0)
    surfaces = data.get("surfaces_to_slack", 0)
    suppressed_count = sum(
        1
        for r in results
        if isinstance(r, dict)
        and r.get("action") == "SURFACE"
        and r.get("slack_posted") is False
    )
    if (
        isinstance(declared, int)
        and isinstance(fixes_ok, int)
        and isinstance(surfaces, int)
    ):
        if declared > 0 and (fixes_ok + surfaces + suppressed_count) < declared:
            failures.append(
                f"orphan failures: fixes_succeeded ({fixes_ok}) + "
                f"surfaces_to_slack ({surfaces}) + suppressed ({suppressed_count}) "
                f"< failures_detected ({declared})"
            )

    if failures:
        print("LAUNCHD-DEBUGGER VALIDATOR FAILED:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 2

    print("LAUNCHD-DEBUGGER VALIDATOR PASSED")
    print(
        f"  artifact: {artifact_path.name}, failures={declared}, "
        f"fixed={fixes_ok}, surfaced={surfaces}, suppressed={suppressed_count}, "
        f"runtime={data.get('runtime_seconds')}s"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

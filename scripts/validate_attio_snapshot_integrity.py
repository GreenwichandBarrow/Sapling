#!/usr/bin/env python3
"""Post-run integrity validator for `attio-snapshot-refresh`.

Runs after `scripts/refresh-attio-snapshot.sh` completes. Catches the silent-
success failure mode where the refresh script exits 0 but the dashboard's
Active Deal Pipeline / M&A Analytics tiles end up reading a stale or
malformed `brain/context/attio-pipeline-snapshot.json`.

Checks:
  1. Snapshot file exists.
  2. mtime within MAX_AGE_SEC (hourly cadence → 65min headroom for
     one-cycle slip).
  3. File parses as JSON.
  4. Has the required top-level keys (`fetched_at`, `list_id`, `stages`,
     `deals`, `closed_count`).
  5. `deals` is a list (may be empty if pipeline genuinely empty — don't
     fail on size 0; the dashboard handles empty pipeline gracefully).
  6. `stages` is a non-empty list (every Attio list has stages — empty
     stages array signals API contract violation, not a real-world state).

Exit codes:
  0 — pass
  1 — fail (snapshot missing, stale, malformed, or schema-violating)
"""

from __future__ import annotations

import json
import sys
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

REPO_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT = REPO_ROOT / "brain" / "context" / "attio-pipeline-snapshot.json"
BUSINESS_MAX_AGE_SEC = 3900  # 65 minutes — covers hourly cadence + one-cycle slip
OFF_HOURS_MAX_AGE_SEC = 72 * 3600  # Fri evening -> Mon morning monitoring window

REQUIRED_KEYS = ("fetched_at", "list_id", "stages", "deals", "closed_count")


def fail(msg: str) -> int:
    print(f"VALIDATOR FAILED: {msg}", file=sys.stderr)
    return 1


def max_age_seconds() -> int:
    now = datetime.now(ZoneInfo("America/New_York"))
    if now.weekday() < 5 and 8 <= now.hour <= 20:
        return BUSINESS_MAX_AGE_SEC
    return OFF_HOURS_MAX_AGE_SEC


def validate_snapshot_data(data: object) -> list[str]:
    failures: list[str] = []
    if not isinstance(data, dict):
        return [f"snapshot root is {type(data).__name__}, expected dict"]

    missing = [k for k in REQUIRED_KEYS if k not in data]
    if missing:
        return [f"snapshot missing required keys: {missing}"]

    deals = data["deals"]
    if not isinstance(deals, list):
        failures.append(f"`deals` is {type(deals).__name__}, expected list")
        deals = []

    stages = data["stages"]
    if not isinstance(stages, list) or not stages:
        failures.append(
            "`stages` is empty or not a list — Attio API contract violation "
            "(every list has stages)"
        )
        stages = []

    stage_titles = set()
    for idx, stage in enumerate(stages):
        if not isinstance(stage, dict):
            failures.append(f"`stages[{idx}]` is {type(stage).__name__}, expected dict")
            continue
        title = stage.get("title")
        if not isinstance(title, str) or not title.strip():
            failures.append(f"`stages[{idx}].title` missing or blank")
            continue
        stage_titles.add(title)

    for idx, deal in enumerate(deals):
        if not isinstance(deal, dict):
            failures.append(f"`deals[{idx}]` is {type(deal).__name__}, expected dict")
            continue
        stage = deal.get("stage")
        if stage_titles and stage not in stage_titles:
            failures.append(
                f"`deals[{idx}].stage`={stage!r} is not in stage titles {sorted(stage_titles)}"
            )

    closed_count = data.get("closed_count")
    if not isinstance(closed_count, int) or isinstance(closed_count, bool) or closed_count < 0:
        failures.append(f"`closed_count` is {closed_count!r}, expected int >= 0")

    return failures


def main() -> int:
    if not SNAPSHOT.exists():
        return fail(f"snapshot missing: {SNAPSHOT}")

    age = time.time() - SNAPSHOT.stat().st_mtime
    max_age = max_age_seconds()
    if age > max_age:
        return fail(
            f"snapshot stale: {age:.0f}s > {max_age}s "
            f"(file: {SNAPSHOT})"
        )

    try:
        data = json.loads(SNAPSHOT.read_text())
    except json.JSONDecodeError as e:
        return fail(f"snapshot not valid JSON: {e}")

    failures = validate_snapshot_data(data)
    if failures:
        return fail("; ".join(failures))

    stages = data["stages"]
    deal_count = len(data["deals"])
    print(
        f"OK: {SNAPSHOT.name} fresh ({age:.0f}s old) — "
        f"{deal_count} deals, {len(stages)} stages, "
        f"closed_count={data.get('closed_count')}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

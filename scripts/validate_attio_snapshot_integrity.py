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
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT = REPO_ROOT / "brain" / "context" / "attio-pipeline-snapshot.json"
MAX_AGE_SEC = 3900  # 65 minutes — covers hourly cadence + one-cycle slip

REQUIRED_KEYS = ("fetched_at", "list_id", "stages", "deals", "closed_count")


def fail(msg: str) -> int:
    print(f"VALIDATOR FAILED: {msg}", file=sys.stderr)
    return 1


def main() -> int:
    if not SNAPSHOT.exists():
        return fail(f"snapshot missing: {SNAPSHOT}")

    age = time.time() - SNAPSHOT.stat().st_mtime
    if age > MAX_AGE_SEC:
        return fail(
            f"snapshot stale: {age:.0f}s > {MAX_AGE_SEC}s "
            f"(file: {SNAPSHOT})"
        )

    try:
        data = json.loads(SNAPSHOT.read_text())
    except json.JSONDecodeError as e:
        return fail(f"snapshot not valid JSON: {e}")

    if not isinstance(data, dict):
        return fail(
            f"snapshot root is {type(data).__name__}, expected dict"
        )

    missing = [k for k in REQUIRED_KEYS if k not in data]
    if missing:
        return fail(f"snapshot missing required keys: {missing}")

    if not isinstance(data["deals"], list):
        return fail(
            f"`deals` is {type(data['deals']).__name__}, expected list"
        )

    stages = data["stages"]
    if not isinstance(stages, list) or not stages:
        return fail(
            "`stages` is empty or not a list — Attio API contract violation "
            "(every list has stages)"
        )

    deal_count = len(data["deals"])
    print(
        f"OK: {SNAPSHOT.name} fresh ({age:.0f}s old) — "
        f"{deal_count} deals, {len(stages)} stages, "
        f"closed_count={data.get('closed_count')}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

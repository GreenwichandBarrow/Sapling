#!/usr/bin/env python3
"""Post-run integrity validator for `jj-snapshot-refresh`.

Runs after `scripts/refresh-jj-snapshot.sh` completes. Catches the silent-
success failure mode where the refresh script exits 0 but the dashboard's
M&A Analytics JJ row + JJ-dials trend panel end up reading a stale or
malformed `brain/context/jj-activity-snapshot.json`.

Checks:
  1. Snapshot file exists.
  2. mtime within MAX_AGE_SEC. Cadence is 3x daily (Mon-Fri 9am, 2:30pm,
     6pm ET). Longest gap between consecutive same-day fires is ~5.5h
     (9am → 2:30pm). Use 18000s (5h) for the daytime spec; weekend or
     overnight gaps are out-of-scope (the validator only fires post-run,
     so it will always be checking a freshly-written snapshot).
  3. File parses as JSON.
  4. Has the required top-level keys (`fetched_at`, `niches_scanned`,
     `per_niche_lifetime`, `dials_today`, `dials_lifetime`, `by_day`,
     `weekly_buckets`).
  5. `niches_scanned` is a non-empty list (must mirror NICHE_SHEETS map
     in refresh_jj_snapshot.py — empty = the script silently early-
     returned).
  6. `weekly_buckets` is a non-empty list (the trend panel breaks if
     this is empty).

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
SNAPSHOT = REPO_ROOT / "brain" / "context" / "jj-activity-snapshot.json"
MAX_AGE_SEC = 18000  # 5 hours — covers longest 9am→2:30pm same-day gap

REQUIRED_KEYS = (
    "fetched_at",
    "niches_scanned",
    "per_niche_lifetime",
    "dials_today",
    "dials_lifetime",
    "by_day",
    "weekly_buckets",
)


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

    niches = data["niches_scanned"]
    if not isinstance(niches, list) or not niches:
        return fail(
            "`niches_scanned` empty or not a list — refresh script must "
            "have hit an early-return before NICHE_SHEETS iteration"
        )

    weekly = data["weekly_buckets"]
    if not isinstance(weekly, list) or not weekly:
        return fail(
            "`weekly_buckets` empty or not a list — dashboard JJ-dials "
            "trend panel needs this populated"
        )

    print(
        f"OK: {SNAPSHOT.name} fresh ({age:.0f}s old) — "
        f"{len(niches)} niches, dials_today={data.get('dials_today')}, "
        f"dials_lifetime={data.get('dials_lifetime')}, "
        f"{len(weekly)} weekly buckets"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

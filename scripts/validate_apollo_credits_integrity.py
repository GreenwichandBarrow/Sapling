#!/usr/bin/env python3
"""Post-run integrity validator for `apollo-credits-refresh`.

Runs after `scripts/refresh-apollo-credits.sh` completes. Catches the
silent-success failure mode where the refresh script exits 0 but the
dashboard's Infrastructure Zone 3 "Apollo credits" tile ends up reading a
stale or malformed `brain/context/apollo-credits-snapshot.json`.

Schema reminder (Apollo's API-key path doesn't expose monthly/daily
balances, so most numeric fields can legitimately be `null`). The signal
that the refresh actually contacted Apollo is `raw_response.enrich_status
== 200` plus presence of the rate-limit headers in
`raw_response.rate_limit_headers`.

Checks:
  1. Snapshot file exists.
  2. mtime within MAX_AGE_SEC (hourly cadence → 65min headroom for
     one-cycle slip).
  3. File parses as JSON.
  4. Has the required top-level keys (`fetched_at`, `raw_response`).
  5. `raw_response.enrich_status == 200` (anything else = Apollo
     rejected the call; tile would silently show stale numbers).
  6. `raw_response.rate_limit_headers` contains at least
     `x-rate-limit-minute` and `x-minute-usage` (these are the values the
     loader merges onto the tile).

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
SNAPSHOT = REPO_ROOT / "brain" / "context" / "apollo-credits-snapshot.json"
MAX_AGE_SEC = 3900  # 65 minutes — covers hourly cadence + one-cycle slip

REQUIRED_KEYS = ("fetched_at", "raw_response")
REQUIRED_HEADERS = ("x-rate-limit-minute", "x-minute-usage")


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

    raw = data["raw_response"]
    if not isinstance(raw, dict):
        return fail(
            f"`raw_response` is {type(raw).__name__}, expected dict"
        )

    status = raw.get("enrich_status")
    if status != 200:
        return fail(
            f"`raw_response.enrich_status` = {status!r} (expected 200) — "
            "Apollo rejected the enrich call; rate-limit headers may be "
            "absent or stale"
        )

    headers = raw.get("rate_limit_headers")
    if not isinstance(headers, dict):
        return fail(
            f"`raw_response.rate_limit_headers` is "
            f"{type(headers).__name__}, expected dict"
        )

    missing_headers = [h for h in REQUIRED_HEADERS if h not in headers]
    if missing_headers:
        return fail(
            f"rate_limit_headers missing required keys: {missing_headers}"
        )

    print(
        f"OK: {SNAPSHOT.name} fresh ({age:.0f}s old) — "
        f"enrich_status=200, "
        f"rate_limit_minute={headers.get('x-rate-limit-minute')}, "
        f"minute_usage={headers.get('x-minute-usage')}, "
        f"minute_remaining={data.get('minute_remaining')}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

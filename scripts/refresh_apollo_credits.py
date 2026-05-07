#!/usr/bin/env python3
"""Refresh brain/context/apollo-credits-snapshot.json from Apollo's REST API.

Snapshot is the contract between this script (writer) and the dashboard
(reader). It powers the "Apollo credits" tile in Infrastructure Zone 3.

Apollo API reality check (probed 2026-04-26):
  - The documented `/v1/auth/health` endpoint returns ONLY
    `{"healthy": true, "is_logged_in": true}` — no credit fields.
  - The `/v1/usage_stats/api_usage_stats` endpoint requires OAuth (404 with
    API-key auth), so REST API-key callers cannot reach it.
  - Rate-limit / usage telemetry is exposed via response HEADERS on actual
    enrichment endpoints (`x-minute-usage`, `x-minute-requests-left`,
    `x-rate-limit-minute`, `x-rate-limit-hourly`, `x-rate-limit-24-hour`).

Strategy: hit `/v1/auth/health` first (cheap liveness probe, no credit
debit). Then make ONE no-op-style organization enrichment call against an
own-domain target so we can capture the rate-limit headers. The enrichment
call costs at most 1 credit (organizations/enrich on a domain Apollo
already has cached), but it's the only documented path to live usage data.

Run hourly via launchd Mon-Fri 8am-8pm ET.

Usage:
    APOLLO_API_KEY=... ./refresh_apollo_credits.py
    # or sourcing scripts/.env.launchd
"""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT_PATH = REPO_ROOT / "brain" / "context" / "apollo-credits-snapshot.json"
ENV_FILE = REPO_ROOT / "scripts" / ".env.launchd"

API_BASE = "https://api.apollo.io/api/v1"
HEALTH_PATH = "/auth/health"
# Lightweight enrichment that surfaces rate-limit headers. apollo.io is
# already in their dataset, so this is a fixed-cost predictable call.
ENRICH_PATH = "/organizations/enrich"
ENRICH_DOMAIN = "apollo.io"

REQUEST_TIMEOUT = 30  # seconds

# Header names Apollo emits on credit-billing endpoints.
HDR_MINUTE_LIMIT = "x-rate-limit-minute"
HDR_MINUTE_USED = "x-minute-usage"
HDR_MINUTE_LEFT = "x-minute-requests-left"
HDR_HOURLY_LIMIT = "x-rate-limit-hourly"
HDR_DAILY_LIMIT = "x-rate-limit-24-hour"


def _load_env_file(path: Path) -> dict[str, str]:
    """Parse `export KEY=value` lines out of a shell env file.

    We don't depend on launchd having sourced the file — the script reads
    it directly so it works under cron, manual invocation, etc. Lines that
    aren't `export KEY=VALUE` (or `KEY=VALUE`) are ignored. Quotes are
    stripped if balanced.
    """
    out: dict[str, str] = {}
    if not path.exists():
        return out
    pattern = re.compile(r"^\s*(?:export\s+)?([A-Z_][A-Z0-9_]*)=(.*?)\s*$")
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        m = pattern.match(line)
        if not m:
            continue
        key, value = m.group(1), m.group(2)
        # Strip a single matching pair of quotes.
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
            value = value[1:-1]
        out[key] = value
    return out


def _headers(api_key: str) -> dict[str, str]:
    # Apollo accepts the API key via either `x-api-key` header or query
    # string. Header is preferred so the key never lands in URL access logs.
    return {
        "x-api-key": api_key,
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
    }


def _to_int(val) -> int | None:
    """Convert a header string (possibly empty) to int, or None."""
    if val is None:
        return None
    s = str(val).strip()
    if not s:
        return None
    try:
        return int(s)
    except ValueError:
        return None


def _build_snapshot(api_key: str) -> dict:
    # 1) Liveness probe — verifies the API key works.
    health_resp = requests.get(
        f"{API_BASE}{HEALTH_PATH}",
        headers=_headers(api_key),
        timeout=REQUEST_TIMEOUT,
    )
    health_resp.raise_for_status()
    health_body = health_resp.json()
    if not health_body.get("healthy") or not health_body.get("is_logged_in"):
        raise RuntimeError(
            f"Apollo auth/health reported unhealthy: {health_body}"
        )

    # 2) Real enrichment call — costs at most 1 credit but is the ONLY
    # supported path to rate-limit / usage headers under API-key auth.
    enrich_resp = requests.post(
        f"{API_BASE}{ENRICH_PATH}",
        headers=_headers(api_key),
        params={"domain": ENRICH_DOMAIN},
        timeout=REQUEST_TIMEOUT,
    )
    enrich_resp.raise_for_status()

    minute_limit = _to_int(enrich_resp.headers.get(HDR_MINUTE_LIMIT))
    minute_used = _to_int(enrich_resp.headers.get(HDR_MINUTE_USED))
    minute_left = _to_int(enrich_resp.headers.get(HDR_MINUTE_LEFT))
    hourly_limit = _to_int(enrich_resp.headers.get(HDR_HOURLY_LIMIT))
    daily_limit = _to_int(enrich_resp.headers.get(HDR_DAILY_LIMIT))

    # Schema mirrors what the dashboard expects. Field names match the
    # original spec where defensible; we map Apollo's actual telemetry
    # (minute-window rate limits) to the closest semantic equivalent.
    # `current_month_used` / `monthly_limit` / `email_credits_used` are
    # not exposed by the API key path — we surface them as null so the
    # loader can fall back to YAML for those if needed later.
    snapshot = {
        "fetched_at": datetime.now(timezone.utc)
        .astimezone()
        .strftime("%Y-%m-%dT%H:%M:%S%z"),
        "current_month_used": None,
        "monthly_limit": None,
        "daily_limit": daily_limit,
        "credits_used_today": None,
        "email_credits_used": None,
        # Live rate-limit telemetry — what Apollo actually exposes.
        "rate_limit_minute": minute_limit,
        "minute_used": minute_used,
        "minute_remaining": minute_left,
        "rate_limit_hourly": hourly_limit,
        "raw_response": {
            "auth_health": health_body,
            "enrich_status": enrich_resp.status_code,
            "rate_limit_headers": {
                HDR_MINUTE_LIMIT: enrich_resp.headers.get(HDR_MINUTE_LIMIT),
                HDR_MINUTE_USED: enrich_resp.headers.get(HDR_MINUTE_USED),
                HDR_MINUTE_LEFT: enrich_resp.headers.get(HDR_MINUTE_LEFT),
                HDR_HOURLY_LIMIT: enrich_resp.headers.get(HDR_HOURLY_LIMIT),
                HDR_DAILY_LIMIT: enrich_resp.headers.get(HDR_DAILY_LIMIT),
            },
        },
    }
    return snapshot


def main() -> int:
    api_key = os.environ.get("APOLLO_API_KEY")
    if not api_key:
        env_vars = _load_env_file(ENV_FILE)
        api_key = env_vars.get("APOLLO_API_KEY")
    if not api_key:
        print(
            "ERROR: APOLLO_API_KEY not set in env and not found in "
            f"{ENV_FILE}",
            file=sys.stderr,
        )
        return 1

    try:
        snapshot = _build_snapshot(api_key)
    except requests.HTTPError as e:
        # Never echo the API key. Keep error context to status + a short
        # body excerpt that the API itself produced.
        status = e.response.status_code if e.response is not None else "?"
        excerpt = (e.response.text[:300] if e.response is not None else "")
        print(
            f"ERROR: Apollo API call failed (HTTP {status}): {excerpt}",
            file=sys.stderr,
        )
        return 2
    except requests.RequestException as e:
        print(f"ERROR: Apollo network error: {e}", file=sys.stderr)
        return 3
    except Exception as e:
        print(f"ERROR: snapshot build failed: {e}", file=sys.stderr)
        return 4

    SNAPSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    SNAPSHOT_PATH.write_text(json.dumps(snapshot, indent=2))
    print(
        f"[refresh] wrote {SNAPSHOT_PATH} — "
        f"minute_used={snapshot.get('minute_used')}/"
        f"{snapshot.get('rate_limit_minute')}, "
        f"fetched_at={snapshot['fetched_at']}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

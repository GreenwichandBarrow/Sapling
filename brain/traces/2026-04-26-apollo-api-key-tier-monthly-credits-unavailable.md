---
schema_version: 1.1.0
date: 2026-04-26
type: trace
today: "[[notes/daily/2026-04-26]]"
task: Apollo API-key tier doesn't expose monthly credit data — degraded to minute-window rate limits
had_human_override: false
importance: medium
target: scripts/refresh_apollo_credits.py, dashboard Infrastructure Zone 3 Apollo tile
tags: [date/2026-04-26, trace, topic/apollo, topic/api-integration, topic/dashboard, pattern/api-tier-discovery, domain/technical]
---

# Decision Trace: Apollo monthly credit telemetry unavailable to API-key auth

## Context

Phase A Gap 6 / Dashboard Item 2 spec called for live Apollo credit usage on the Infrastructure Zone 3 tile: "current_month_used / monthly_limit / daily_limit." Source endpoint listed as `GET /v1/auth/health`.

Background agent built `scripts/refresh_apollo_credits.py` to fetch + write `apollo-credits-snapshot.json`. On test run, the agent discovered:

1. **`/v1/auth/health` returns only `{"healthy": true, "is_logged_in": true}`** — no credit telemetry whatsoever.
2. **`/v1/usage_stats/api_usage_stats`** (the documented monthly-usage endpoint) **404s under API-key auth** — OAuth-only.
3. **The only credit/usage signal available to API-key callers is via response headers** on real billing endpoints (`x-rate-limit-minute`, `x-minute-usage`, `x-minute-requests-left`, `x-rate-limit-hourly`, `x-rate-limit-24-hour`).

Agent pivoted: probe `/v1/auth/health` for liveness + one `/v1/organizations/enrich?domain=apollo.io` POST per fire to capture rate-limit headers. Cost: ~1 credit/fire = ~65/week. Snapshot now contains minute-window data, monthly fields stay null.

## Decision

Ship the degraded version: minute-window rate-limit (1/1000 used) instead of monthly credit burn. Tile renders "999 remaining / min · 1/1000 used in current minute window · live · refreshed HH:MM."

Surfaced the limitation explicitly to Kay with two paths: (a) accept the degraded metric, (b) move Apollo to OAuth later for monthly visibility (separate effort). Kay accepted (a) by approving the plist load.

## Alternatives Considered

1. **Don't ship Apollo tile at all** — wait for OAuth integration. **Rejected** — tile is currently a `—` placeholder anyway; minute-window data is strictly better than nothing.

2. **Try Apollo's `/billing` or other undocumented endpoints** — agent confirmed several 404. **Rejected** — speculative work, no signal.

3. **Ship degraded with explicit "minute-window proxy" labeling** (chosen) — gives Kay the live-refresh signal she wanted (visual confirmation Apollo isn't broken) without misrepresenting it as monthly burn data.

## Reasoning

- Spec was based on assumed Apollo capabilities. Agent's empirical discovery is the source of truth — went with what actually works.
- Minute-window data is genuinely useful for one thing: detecting Apollo rate-limit issues during heavy enrichment runs (Phase 2 target-discovery, list-builder bulk lookups). Not a perfect substitute for monthly burn, but a real signal.
- Snapshot schema retained the monthly-credit fields as null — if/when OAuth swap happens, no schema migration needed.

## Why This Trace Matters

Future agent attempting to wire Apollo monthly credit data via API key will re-discover this exact limitation, costing ~30min of API exploration. Trace short-circuits that: API-key tier has no monthly telemetry, full stop, OAuth-only.

Also: the snapshot's `daily_limit`, `current_month_used`, `monthly_limit`, `email_credits_used` fields are intentionally null in API-key mode. If a future dashboard panel renders empty for those, that's expected — not a bug.

## Key Insight

Vendor API documentation often describes the *feature surface*, not the *auth-tier surface*. Always probe the actual endpoints under your auth method before committing to a metric. Spec sentences like "Apollo exposes monthly credit data" should be read as "Apollo exposes monthly credit data *somewhere, under some auth mode* — verify it's exposed under yours."

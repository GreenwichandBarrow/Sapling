---
schema_version: 1.1.0
date: 2026-04-25
type: trace
today: "[[notes/daily/2026-04-25]]"
task: Stale-snapshot banner thresholds that don't false-fire on weekends
had_human_override: false
importance: medium
target: dashboard:data_sources
tags: [date/2026-04-25, trace, topic/dashboard, topic/observability, pattern/weekend-aware-thresholds, domain/technical]
---

# Decision Trace: Weekend-aware staleness thresholds for scheduled-job dependent data

## Context

Dashboard reads `attio-pipeline-snapshot.json` and `jj-activity-snapshot.json`. Both refreshed by launchd jobs that fire Mon-Fri only (Attio hourly 8am-8pm, JJ at 9am/2:30pm/6pm). On weekends + overnight, the snapshot legitimately ages because the refresh jobs aren't supposed to fire.

Naive single-threshold approach (e.g., "warn if snapshot >2h old"): banner fires every weekend, every overnight gap. Becomes noise → Kay learns to ignore it → loses ability to detect actual job failure.

## Decisions

### Threshold strategy

**Considered:**
- (a) Single threshold tuned to cover the weekend gap (~60h). Loses sensitivity — silent weekday job failure takes 2.5 days to surface.
- (b) Two thresholds: tight during business hours (2h Attio, 30h JJ), permissive outside (60h Attio, 72h JJ). Lock state at check-time based on current weekday + clock.
- (c) Plist-aware: parse the next expected fire time, threshold = (time since last fire) + grace period. Most accurate but adds plist parsing dependency.

**Chosen:** (b). Implemented `_is_business_hours_et()` (Mon-Fri 8am-8pm) + per-source threshold helpers `_attio_threshold()` / `_jj_threshold()`.

**Reasoning:** (c) is the "correct" answer but the complexity buys little — both jobs run within consistent windows. (b) gets 95% of the value with a 10-line helper. If thresholds turn out to need finer tuning, escalate to (c).

### Health-monitor uses different (more permissive) thresholds

**Chosen:** Dashboard banner threshold = 2h/30h business / 60h/72h off-hours. Health-monitor threshold = 4h/12h business / 60h/80h overall.

**Reasoning:** Two surfaces, two purposes. Dashboard banner = "live alert for users browsing right now" — sensitivity matters. Health-monitor = "nightly canary for breaking systems" — should only fire on genuinely-broken jobs, not the expected hourly gap between runs. Different thresholds avoid both surfaces firing on the same transient.

## Learnings

- **Schedule-dependent thresholds need to know the schedule.** Single-number thresholds are noise generators when the underlying data has cyclical liveness.
- **Multi-surface alerting needs independent threshold tuning.** Dashboard ≠ health-monitor; they serve different humans (Kay browsing now vs. Kay reading Friday brief) with different latency tolerance.
- **Future agent instruction:** when adding any "is data stale?" check, first answer "what is this data's expected refresh cadence and what is its expected gap?" Then set the threshold to (gap + grace) for live-alert surfaces and (cadence × N) for canary surfaces.

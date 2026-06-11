---
schema_version: 1.1.0
date: 2026-06-10
type: trace
task: Preserve deal-aggregator tuning as Phase 2.5 work
had_human_override: true
importance: high
target: skill:deal-aggregator
applied_to: [docs/migrations/2026-06-04-claude-to-codex.md]
tags: [date/2026-06-10, trace, topic/deal-aggregator, topic/phase-2-5, status/done]
---

## Context

The June 10 morning workflow surfaced deal-aggregator tuning as an improvement candidate. Kay clarified that this work should stay on the Phase 2.5 list.

## Decisions

### Keep deal-aggregator open until volume target is met
**AI proposed:** Treat deal-aggregator tuning as a calibration candidate after the goodnight closeout.
**Chosen:** Kay directed that deal-aggregator work remain on the Phase 2.5 running list until it reliably surfaces 1-3 evaluable deals per week.
**Reasoning:** Clean scheduled execution is not the same as business effectiveness. The skill can run successfully and still fail the funnel target if source coverage, screening strictness, active-niche corpus, or surfacing rules suppress real deal flow.
**Pattern:** #outcome-over-green-runs

## Learnings

Do not close deal-aggregator work just because systemd timers, email leg, and validators are green. The success metric is qualified deal volume. Phase 2.5 should focus on funnel effectiveness: source yield, broker-opportunistic review, corpus expansion, blocked source recovery, and surfacing UX.

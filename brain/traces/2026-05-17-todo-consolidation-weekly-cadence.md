---
schema_version: 1.1.0
date: 2026-05-17
type: trace
today: "[[brain/context/continuation-2026-05-17-2]]"
task: To Do tracker consolidation — single tab, Status/Horizon dropdowns
had_human_override: false
review_status: pending
importance: high
target: process
tags: [date/2026-05-17, trace, topic/to-do-consolidation, pattern/match-cadence-to-data-not-ideal, status/done]
---

# Decision Trace: To Do Consolidation — Weekly-Batch Cadence Is the Real Constraint

## Context
The To Do tracker had fragmented into multiple tabs plus a sweep job and donut charts, built around an implicit "live, continuously-updated task surface" model. Kay's actual workflow plans and reviews tasks in weekly batches.

## Decisions

### Consolidate to one tab; drop the live-surface scaffolding
**AI proposed (prior architecture):** Multiple specialized tabs, an automated sweep job, donut-chart progress viz — all premised on a live/daily-updated task surface.
**Chosen:** Single `To Do` tab with two dropdowns (Status: Not Completed / On-going / Completed; Horizon: Short Term / Long Term / Weekly Recurring Mon–Sat). No sweep, no donuts. Retired tabs hidden (not deleted) for a one-week rollback window.
**Reasoning:** The data is inherently weekly-batch — Kay plans the week, works it, reviews at week's end. "Live" was a false premise the prior structure was optimizing for. Once the cadence is correctly identified as weekly, the per-tab fragmentation + sweep automation add structure without adding signal, and the thin boundaries between tabs collapse into one Status/Horizon model.
**Pattern:** #pattern/match-cadence-to-data-not-ideal

## Why This Trace Matters
A future agent maintaining or extending the tracker will be tempted to re-add specialized tabs, automation, or freshness machinery — all of which feel like "better tooling." This trace records that the binding constraint is the data's natural cadence (weekly batch), not tooling sophistication. Building live-surface affordances for weekly-batch data is solving a problem that doesn't exist, and the same false-live premise also drove the (separately rejected) daily-dashboard-freshness expectation this session.

## Key Insight
Before adding structure or automation to a tracking surface, identify the data's natural cadence. If it's weekly-batch, live-surface scaffolding (sweeps, real-time viz, per-state tabs) is overhead that hides signal. Match the tool's cadence to the data's, not to an idealized always-fresh model.

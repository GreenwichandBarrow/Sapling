---
schema_version: 1.1.0
date: 2026-05-01
type: trace
title: "Active Deals 4-cluster triage framework — Dead / Cold-but-live / Process-broken / Genuinely-active"
tags: ["date/2026-05-01", "trace", "topic/active-deals-cleanup", "topic/pipeline-hygiene", "topic/deal-stage-rollback", "domain/process"]
importance: high
target: skill:deal-evaluation
---

# Active Deals 4-cluster triage framework

## Context

Active Deals pipeline had grown to 18 entries, many stale. Cleanup task: separate genuinely-active from stale, archive what's dead, and stage-rollback what's gone cold but might revive. Needed a durable triage framework — not just a one-time clean.

## Decision

**AI proposed (initial):** Single-pass review of each Active Deal, ad-hoc archive/keep call per row.

**Chosen:** 4-cluster framework with cluster-specific decision rules. Each Active Deal gets classified into exactly one cluster, then the cluster determines the action.

**The four clusters:**

1. **Dead** — Zero activity 90+ days, no path forward, no hooks → **archive to Closed/Not Proceeding.**
   - Outcome today: 6 deals (Genser 109d, ARCIS sub-floor, Freedman sub-floor, Clark Fine Art CA, Fine Art Shippers, VF Global)

2. **Cold-but-live** — Last touch >30 days, no Gmail hits in 30d, but still potentially viable → **stage-rollback to Identified, leave note.** Don't archive (revival possible) but don't pretend it's actively progressing.
   - Outcome today: 5 deals stage-rolled-back

3. **Process-broken** — Stuck at a stage with no clear next action; the process itself broke (missing data, ambiguous owner, blocked on external party with no follow-up cadence) → **leave at current stage with explicit note for next sprint to unblock.**
   - Outcome today: 1 deal left as Identified with note

4. **Genuinely-active** — Recent touch + Gmail evidence + clear next action → **leave alone, do not touch.**
   - Outcome today: 12 deals untouched

**Audit method:** **0 Gmail hits in 30 days = stage-rollback default**, only override with explicit reason (e.g., paper-only deal, Slack-only thread, in-person-only relationship).

**Reasoning:** Without a framework, every stale-deal review devolves into per-row debate. The 4-cluster method makes the call defensible (each cluster has explicit criteria) and machine-checkable (Gmail-hit-count + days-since-last-touch are queryable). Stage-rollback (vs archive) is the key innovation — it preserves the deal's history but stops it from polluting active-pipeline metrics.

## Why this matters for future agents

The instinct on a stale deal is binary: keep or kill. **Stage-rollback is the third option** — it acknowledges the deal isn't dead but isn't active either. Without stage-rollback, you either falsely report momentum (keep on Active) or destroy revival optionality (archive). The 4-cluster framework forces the right call.

## How a future agent should apply

When asked to clean up a stale pipeline (Active Deals, prospects, niches, intermediaries):

1. **Run the audit first:** For each entry, capture (a) days since last touch (b) Gmail-hit count in last 30d (c) clear next action y/n.
2. **Classify into 4 clusters** using the criteria above. If unsure, default to Cold-but-live (stage-rollback) — it's the recoverable middle ground.
3. **Apply cluster-specific action** in batch (don't intermix). Archive batch first, stage-rollback batch second, process-broken notes third, genuinely-active untouched.
4. **Report cluster counts** to Kay so she can sanity-check the distribution. If "Genuinely-active" is <30% of original list, you missed something or the pipeline is genuinely cold.

## Concrete numbers from today

Active Deals: 18 → cleanup → 12 in pipeline + 6 archived. Cluster distribution: 12 active / 5 cold-but-live (rolled back) / 1 process-broken / 6 dead. ~67% of original list stayed in pipeline (after rollbacks); 33% archived. Healthy distribution for a 90-day-old pipeline.

## Related

- `feedback_active_deal_urgency` — active deal signals get same-day treatment
- Bead candidate: deal-evaluation skill upgrade to auto-run 4-cluster audit weekly + surface only Cold-but-live and Process-broken to Kay (Dead and Genuinely-active are auto-handled)

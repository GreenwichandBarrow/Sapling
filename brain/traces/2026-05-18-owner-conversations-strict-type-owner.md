---
schema_version: 1.1.0
date: 2026-05-18
type: trace
title: "Owner conversations metric is strict type:owner only — partner calls are Quality"
trace_type: metric-definition
tags: ["date/2026-05-18", "trace", "topic/ma-analytics-tile", "topic/dashboard", "topic/metric-definition", "person/carlos-nieto-dca", "person/krupa-shah"]
---

# Owner conversations metric is strict type:owner only — partner calls are Quality

## Trigger

Redesigning the M&A Analytics landing tile (`dashboard/pages/dashboard_landing.py:_tile_ma_analytics()`). The existing logic counted recorded calls as "Owner conversations," reading 4 this week — but those were [[entities/carlos-nieto-dca|Carlos Nieto]] (DCA, intermediary), [[entities/krupa-shah|Krupa Shah]] (capital-side), and two coaching calls. Kay specified the metric must be technically strict.

## Decision

**Owner conversations** counts ONLY explicit `type: owner` curated entries → reads **0** this week. Partner / intermediary / capital-side calls (Carlos, Krupa) flow to a separate **Quality conversations** metric. Conference/luncheon conversations invisible to `_scan_calls()` are fed via a new `brain/context/quality-conversations-manual.json` (Becky 5/13 Heels-to-Deals, Laura 5/14 ACG seeded `type: quality`). The tile is COLD-funnel only — Kay's warm emails and CEO LinkedIn DMs are deliberately excluded; rows relabeled Cold emails / Cold LinkedIn DM / Cold calls.

## Alternatives considered

1. **Count any recorded call as an owner conversation** — what was happening. Inflates the headline number with intermediaries, capital-side, and coaching calls; the metric stops meaning "I talked to a business owner." Rejected.
2. **Heuristic classification (slug/keyword hints) to guess owner vs partner** — fragile and silently wrong (the coaching misclassification in Task 11 is exactly this failure). Rejected for the headline metric; hints are acceptable only for *exclusion* (coaching), not for *promotion* to owner.
3. **Strict `type: owner` + separate Quality bucket + manual JSON for off-call convos** — chosen. Owner is a curated, intentional label; everything real-but-not-owner is visible as Quality rather than dropped.

## Reasoning

A vanity metric that reads high because it counts the wrong conversations is worse than a strict one that reads 0 — the 0 is informative (no true owner conversations this week), the inflated 4 is misleading. Strictness also makes the number a forcing function: it only moves when Kay actually talks to owners. Quality conversations preserves the signal that partner/conference activity still happened, without laundering it into the owner line.

## Why this trace matters

A future agent "fixing" the tile because "Owner conversations shows 0, that looks broken" will be tempted to broaden the count back to recorded calls. That is the bug, not the fix. The 0 is correct when there were no `type: owner` entries. Recorded owner calls do NOT auto-count (no owner sub-type in call frontmatter yet) — an offered-but-unbuilt schema option (`is_owner: true` on `schemas/vault/call.yaml`) is the only sanctioned path to change this, and needs Kay's go-ahead.

## Key insight

A strict metric reading 0 beats a loose metric reading 4-but-wrong. Promotion to a headline category must be curated/explicit; heuristics may only exclude, never promote.

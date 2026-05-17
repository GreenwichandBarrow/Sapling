---
schema_version: 1.1.0
date: 2026-05-13
type: trace
today: "[[notes/daily/2026-05-13]]"
task: Lock the post-call-analyzer rewrite architecture from Kay's answers
output: "[[context/session-decisions-2026-05-13]]"
had_human_override: true
tags: [date/2026-05-13, trace, topic/post-call-analyzer-rewrite, topic/scheduled-skills, pattern/cadence-matches-volume-not-max-freshness]
---

# Decision Trace: post-call-analyzer Rewrite — Kay's Architecture Overrides

## Context
Goal Kay set: within an hour of a call ending, transcript pulled + reviewed, review-ready tasks created, and specific analysis of implications for the search AND for operations. Claude proposed a spec with several defaults; Kay overrode most of them.

## Decisions

### Polling cadence
**AI proposed:** 5-min server poll (no system-load issue at 0.07% rate-limit capacity).
**Chosen (Kay):** **2 fires/day, 1pm + 6pm ET.** Reasoning: only 1–3 calls/day; 5-min is over-provisioned; 2/day still meets the 1-hour-ish SLA in practice and matches actual call volume.
**Pattern:** #pattern/cadence-matches-volume-not-max-freshness

### Which calls get processed
**AI leaned:** external-only (skip internal/JJ syncs — no Attio writes needed).
**Chosen (Kay):** **all calls with transcripts**, no filter.

### Where analysis lives
**AI proposed:** vault call note as the primary artifact.
**Chosen (Kay):** **1-2 page Google Doc per call in RESEARCH/MEETINGS**; vault note still written for the graph, but the Doc is what Kay reads. Analysis may flag "further analysis to do" pointers but must NOT auto-deep-dive ahead of Kay's review.

### Tasks destination
**Chosen (Kay):** TO DO 5.12.26 sheet, TO DO tab, unscheduled — Kay assigns the day-slot in morning brief. (Not beads, not inbox.)

### Gmail follow-up drafting
**AI had it in scope** (carried from prior spec).
**Chosen (Kay, implicit via "tasks go to TO DO"):** **deprecated** — "send X to Y" becomes a TO DO task, not an auto-draft.

### Slack format
**Chosen (Kay, Path A):** disconnect Granola→Slack; ONE skill message per call to #ai-operations.

### Trigger location
**Chosen (Kay):** server-only — explicitly because "prior launchd jobs failed" and Mac-asleep is unacceptable.

## Alternatives Considered
- Real-time per-call processing (the pre-rewrite design) — rejected for cadence; volume doesn't justify it.
- External-only filtering — rejected; Kay wants every transcript covered.
- Keeping Gmail drafting — rejected; tasks-to-TO-DO is the single review surface.

## Why This Trace Matters
A future agent editing post-call-analyzer will see "real-time / 5-min / external-only / Gmail-drafts" patterns in old memory ([[feedback_post_call_analyzer_realtime_on_granola]]) and may revert. This trace records that Kay deliberately traded freshness for volume-matched cadence, widened scope to all calls, moved the artifact to a Google Doc, and **removed** Gmail drafting. Cadence should match call volume and the review surface Kay actually uses — not maximize freshness.

## Key Insight
Match scheduled-skill cadence to actual event volume and Kay's review rhythm, not to the lowest technically-safe interval. Over-provisioned polling is a cost and a noise source, not a feature.

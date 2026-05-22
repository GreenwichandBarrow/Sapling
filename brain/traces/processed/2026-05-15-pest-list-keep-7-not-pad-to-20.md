---
name: pest-list — keep 7, don't pad to 20
date: 2026-05-15
review_status: applied
type: trace
schema_version: 1.1.0
tags:
  - date/2026-05-15
  - trace
  - topic/pest-management
  - topic/target-refinement
  - topic/women-owned
  - skill/target-discovery
---

# Pest list — keep the 7, don't pad to 20

## Trigger
Harrison Wells advised a highly-custom send (e.g., a cake) to a tight ~20-company refined target list. Kay scoped it: 20 women-owned pest firms within ~1hr of the West Village. The re-run subagent found only **7 verified women-owned** firms in radius (5 HIGH / 2 MEDIUM confidence), with the source list's HQ/Ownership columns empty (all web-researched).

## Decision
Kay: "keep the 7." Ship the list at 7 — do not pad to hit 20, do not widen the radius, do not relax the women-owned criterion.

## Alternatives Considered
- Pad to 20 with lower-confidence or out-of-radius firms to hit the target number.
- Widen the radius (Mt. Kisco / East Brunswick already near the 60-min edge).
- Commission a fresh women-owned-specific pull (Apollo + WBE/MWBE NY/NJ cert directories) before sending.

## Reasoning
The 7-of-20 result is not a research shortfall — pest control is a heavily male-dominated vertical, so the scarcity *is* the finding and is exactly why the women-priority lens applies. Padding to a round number would dilute the very signal the refinement exists to surface and risk a name-personalized gift landing on an unqualified or PE-owned firm (Arrow/Magic were correctly excluded as Rentokil-owned).

## Why This Trace Matters
A future agent running a similar "refine to N targets for a custom send" task will be tempted to treat N as a hard quota and backfill to reach it. Here the human explicitly overrode the numeric target in favor of verified quality. The number was a ceiling, not a floor.

## Key Insight
When a refinement target (N) collides with a scarce qualifying pool, the scarcity is data — report the true count, never pad to the target. Quota is a ceiling, not a floor. See [[brain/outputs/2026-05-15-pest-20-women-owned-west-village]].

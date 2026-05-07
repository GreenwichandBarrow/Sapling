---
schema_version: 1.1.0
date: 2026-05-01
type: trace
title: "Granola summary insufficient for substantive coaching/strategy calls — full transcript re-read recovers buried action items"
people: ["[[entities/harrison-wells]]"]
tags: ["date/2026-05-01", "trace", "person/harrison-wells", "topic/harrison-coaching", "topic/granola", "topic/coaching-call-processing", "domain/process", "had_human_override"]
importance: high
target: skill:email-intelligence
---

# Granola summary insufficient for substantive coaching calls

## Context

Harrison Wells (G&B coach) had a 4/30 coaching session captured in Granola. The Granola summary was processed by email-intelligence as part of the morning workflow. When 5/1 morning briefing surfaced Harrison-related items, the agent initially used only the Granola summary as the source of truth. On closer audit (full transcript re-read of the Granola call note), 5 missed action items + 4 promised emails were recovered that the Granola summary had not surfaced.

## Decision

**AI proposed (initial):** Treat Granola call summary as sufficient input for downstream skills (briefing surfacing, inbox item creation, decision tracing). Trust Granola's automated synthesis.

**Chosen / overridden:** For substantive coaching/strategy calls (Harrison, Guillermo biweekly, Jeff Stevens monthly, investor calls, deal calls), DO NOT trust the Granola summary alone. Always re-read the full transcript and extract action items + promised follow-ups manually before downstream processing.

**Reasoning:** Granola summarization is optimized for general meeting recall (was discussed, what was decided). It systematically under-weighs:
- Specific action items buried in mid-call asides ("oh and one more thing — can you also send me X")
- Promised emails ("I'll send you the link to that tool" / "I'll forward the doc")
- Follow-up commitments tied to a specific person/date that didn't get a clean summary line
- Strategic insights that emerged conversationally rather than as a labeled decision point

For coaching/strategy calls where every offhand remark might be a $1,000-coaching-hour insight, the cost of a missed action item is high. The cost of re-reading 15-20 min of transcript is low.

## Why this matters for future agents

The default behavior of "Granola summary is the call note" is wrong for high-value substantive calls. For routine internal sync calls (JJ daily, vendor check-ins), Granola summary is sufficient. For coaching/strategy/investor/deal calls, transcript re-read is mandatory.

## Concrete failure mode that triggered this trace

Harrison call summary mentioned ~3 action items. Full transcript re-read surfaced:
- 5 action items (vs 3 in summary)
- 4 specific email follow-ups Harrison promised (only 1 in summary)
- 2 strategic recommendations buried in conversational asides (0 in summary)

If the agent had relied on the Granola summary, ~6-7 items would have been silently dropped, leading to dropped balls on Harrison's promised follow-ups (he'd notice — coaching relationship damage) AND missed action items on Kay's side (she'd appear inattentive).

## How a future agent should apply

When email-intelligence or pipeline-manager surfaces a Granola call note for processing:

1. **Classify call type:**
   - Routine sync (JJ daily, vendor, status check) → Granola summary sufficient
   - Substantive (coaching, strategy, investor, deal, intermediary) → MANDATORY full transcript re-read

2. **For substantive calls, the transcript re-read produces:**
   - Comprehensive action items list (vs Granola's filtered version)
   - All promised follow-up emails / sends / introductions
   - Strategic insights worth memory-saving even if not labeled as decisions
   - Exact quotes for any commitment that may need to be referenced back ("you said you'd send X")

3. **Codify in skill:** email-intelligence should flag substantive call types and route to full-transcript processing automatically, not Granola-summary-only.

## Related

- `feedback_vault_single_source` — vault is single source of truth, Granola/Gmail/etc. write to brain/ first
- Harrison engagement renewal decision pending — recovered action items inform renewal calculus
- Bead candidate: email-intelligence skill upgrade to auto-flag substantive call types for transcript-re-read mode

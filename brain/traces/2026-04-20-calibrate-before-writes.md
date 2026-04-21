---
schema_version: 1.1.0
date: 2026-04-20
type: trace
today: "[[notes/daily/2026-04-20]]"
task: "river-guide-builder Phase 3 — Kay-enforced cap before writes"
output: "[[context/session-decisions-2026-04-20]]"
had_human_override: true
importance: high
target: skill:river-guide-builder
tags: [date/2026-04-20, trace, pattern/calibrate-before-writes, domain/process, status/pending]
---

# Decision Trace: Cap-Check Before Mutating State on Bulk Network Scans

## Context

Kay greenlit Phase 3 (Network Matches) execution across 8 niches — "go ahead and cross the niches against the network in attio" — but added a hard cap: "I imagine we have 10 people tops per niche, if any more please flag and pause." AI had two valid paths: (1) execute Phase 3 across all 8 niches in parallel with instruction to each subagent to self-cap at 10, OR (2) run a calibration-only scan first with zero writes, report counts, and only proceed after Kay reviews.

## Decisions

### Execute with self-cap vs calibration-only first
**AI proposed:** Calibration-only scan — pull counts per niche under H-strength filter, write nothing, report back.
**Chosen:** Calibration-only scan. Same as proposed.
**Reasoning:** Kay's cap concern signaled uncertainty about the skill's precision. If the criterion was loose and produced 100 per niche, parallel execution would write 800+ rows to target sheets before Kay could intervene. Cost of the extra round-trip (one message cycle) << cost of un-writing bad rows and damaging tab signal-to-noise. The calibration pass is cheap and reversible; the writes are not.
**Pattern:** #pattern/calibrate-before-writes

### Where to set the hard rule in the subagent prompt
**AI proposed:** "NO writes (no Attio create/update, no Google Sheet writes, no vault file writes). Only READ from Attio via the REST API or MCP search/get tools."
**Chosen:** Same — set write-prohibition as the first hard rule, explicit list of forbidden tool calls.
**Reasoning:** Subagents lack full session context; a vague "don't write yet" can be reinterpreted as "write carefully." Explicit tool-level prohibition is safer.
**Pattern:** #pattern/calibrate-before-writes

## Learnings

- **Default to calibration-before-writes any time a user signals yield uncertainty.** Triggers: "flag and pause if more than X", "I imagine we have ~Y", "make sure we're pulling strong ones", "if it's a lot, let me know". These are calibration requests masquerading as execution greenlights. Treat them as "run calibration, report, await confirmation."
- **Explicitly forbid state-mutating tools in the subagent prompt** when running calibration passes. Do not rely on "don't write" framing alone — list the tool names that are off-limits.
- **Report format matters:** per-niche count + over-cap flag + top-3 sample is exactly the right density for Kay to make a fast keep/tighten call. Full dump of all hits per niche is noise when the count alone determines the decision.
- **Two-sided cap check:** paying attention only to "over cap" misses the opposite failure. When a user expects signal ("I have contacts in this niche") and the skill returns zero, that's equally a signal to pause. Cap check should be `count > expected_max OR count == 0 WHEN signal_expected`.

## Why This Trace Matters

Kay's 10-per-niche cap was itself the surprising input — most bulk-scan skills default to "produce as much as possible" rather than "produce up to N." This pattern (explicit yield ceiling signaling user's expected range) should propagate to other skills that do bulk enumeration against Kay's data: relationship-manager's morning scan, target-discovery's niche-refill runs, warm-intro-finder's ecosystem scans. All of them benefit from a "what did the user expect to see" calibration gate.

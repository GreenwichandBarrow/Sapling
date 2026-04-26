---
schema_version: 1.1.0
date: 2026-04-26
type: trace
today: "[[notes/daily/2026-04-26]]"
task: Codified Friday-only rule for relationship-nurture surfacing
had_human_override: true
importance: high
target: pipeline-manager skill, morning briefing assembly, memory feedback_relationship_cadence_friday_only.md
tags: [date/2026-04-26, trace, topic/morning-briefing, topic/decision-fatigue, topic/relationship-cadence, pattern/memory-graduates-from-violation, domain/operational]
---

# Decision Trace: Relationship-nurture surfacing is Friday-only

## Context

Mid-session, while planning the cadence-debt sweep batch (Carlos + Kanayo + Ashlee + Robert + Lauren → Dormant), Kay said: *"We had said you will only remind me of relationship outreach cadence on fridays. I find all of this noise and very stressful."*

Critically: she said "we had said." This was a rule she had set previously — and I'd been violating it across 4/17, 4/21, 4/24, and 4/26 morning briefings. Each Mon-Thu briefing surfaced ≥3 cadence-debt items as 🟢 dropped-balls. The same names recurred (Ashlee, Robert, Carlos, Kristina) cycle over cycle.

## Decision

Codify as a hard rule in memory: relationship-nurture / overdue-contact / cadence-debt surfacing is **Friday-only**. Mon-Thu briefings must omit the entire category, even when relationship-manager flags items.

Active-deal cadence (NDA awaiting reply, financials chase, post-LOI checkpoints) is explicitly NOT in scope of this rule — those stay daily.

Memory shipped: `feedback_relationship_cadence_friday_only.md`. Index entry added to `MEMORY.md`.

## Alternatives Considered

1. **Per-contact suppression** (just remove Lauren, Ashlee, Robert from briefing surface) — would have reduced today's noise but not addressed the root pattern. Next cycle a different contact ages into the threshold and we're back to Mon-Thu noise. **Rejected** — treats symptom not cause.

2. **Reduce frequency to "twice weekly Tue + Fri"** — meets in the middle. **Rejected** — Kay's word was "stressful," and her preferred bookend is Friday (already runs weekly-tracker + meta-calibration there). Adding Tuesday adds a second stressful surface for marginal benefit.

3. **Friday-only rule (chosen)** — concentrates all relationship-cadence cognitive load into one day that already has the right context (weekly review, calibration). Kay can dedicate mental headspace once.

## Reasoning

- Kay framed this as "noise" + "stressful" — emotional load, not just signal-to-noise. Memory needs to address the emotional cost, not just the analytical question.
- "We had said" implies prior verbal agreement that didn't get codified. Pattern: verbal rules need durable memory backing or they decay.
- Mon-Thu briefings have plenty of legitimate signal (active deals, calendar, calibration items). Cadence noise crowds out the things Kay actually wants to see.
- relationship-manager keeps running daily (writes the artifact), but the BRIEFING surface layer suppresses it Mon-Thu. Don't kill the data pipeline; kill the noise.

## Why This Trace Matters

Future agent sees relationship-manager's artifact flagging overdue contacts on a Tuesday and feels obligated to surface them in the briefing. Without this trace + the memory, that's the natural default (relationship-manager is a daily skill; its output should appear daily, right?). Wrong. The intentional design is daily data collection + Friday-only surfacing. Trace prevents future agent from "fixing" what looks like a missing surface but is actually a deliberate filter.

## Key Insight

When the user has set a rule verbally that you keep violating, the violation count IS the signal that the rule needs to graduate from verbal-agreement to durable memory. Don't wait for the user to say "I've told you N times" — the second violation in a similar context is the calibration trigger.

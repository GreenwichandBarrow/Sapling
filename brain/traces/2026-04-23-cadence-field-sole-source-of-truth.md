---
schema_version: 1.1.0
date: 2026-04-23
type: trace
title: "Cadence Field Is Sole Source of Truth — Don't Read next_action Text as Threshold Override"
tags: ["date/2026-04-23", "trace", "topic/relationship-manager", "topic/skill-calibration", "topic/cadence-rules", "topic/false-positive-overdue", "person/lauren-della-monica", "person/stanley-rodos"]
had_human_override: true
importance: high
target: skill
people: ["[[entities/kay-schneider]]", "[[entities/lauren-della-monica]]", "[[entities/stanley-rodos]]"]
companies: []
---

# Trace: Cadence Field Is Sole Source of Truth

## Context

Morning briefing 2026-04-23 surfaced 5 overdue contacts in the Dropped Balls bucket. Two were false positives Kay caught:

- **Lauren Della Monica:** Cadence changed Quarterly → Occasionally on 2026-03-31 (per [[brain/context/relationship-status-2026-04-01]]). Attio `nurture_cadence` field correctly = Occasionally (213-day threshold). But her Attio `next_action` text still read "Maintain quarterly touchpoint." Relationship-manager skill read the *text* as the cadence rule and surfaced her as 97 days past quarterly threshold. Real status under Occasionally: 195/213 days = NOT overdue, 18 days from threshold. She had been re-surfaced incorrectly for 3+ weeks of morning briefings.
- **Stanley Rodos:** Quarterly cadence, last contact 2026-03-17 = 37 days. Quarterly threshold = 98 days. Within window. Skill surfaced him as "5+ weeks aged commitment, escalates 5/1" because next_action mentioned "Follow up on Art Restoration Services opportunity (Mar 17)." Aged commitment text drove the surfacing, not threshold math.

Kay's correction: "Lauren — you were supposed to have removed. Stanley we meet quarterly so we will likely meet in May. Nothing to do now."

## Decisions

### Cadence field is the ONLY source of truth for thresholds
**AI behavior before today:** Skill read `next_action` text content as a hint about which cadence to apply. If text said "Maintain quarterly touchpoint," skill applied 98-day threshold even when cadence field = Occasionally.
**Chosen rule:** `nurture_cadence` field is the **sole** input for threshold determination. Next_action text is informational only. If text and field conflict (e.g., text says "quarterly" but field is Occasionally), flag the conflict in a "Metadata Drift" section so Kay can decide which to update — but do NOT surface as overdue based on text.
**Reasoning:** Kay's most recent decision lives in the cadence field (when she changes it, it's the binding act). Next_action text drifts behind because it's free-form and rarely re-edited when cadence changes. Reading the text as override means surfacing on stale signal indefinitely until someone catches it. Lauren was re-surfaced for 3 weeks before catch.
**Pattern:** #pattern/structured-field-over-free-text

### Within-cadence commitment drift = NOT a surfacing trigger
**AI behavior before today:** When `next_action` referenced an aged commitment (e.g., "Follow up on X opportunity (Mar 17)"), skill projected forward and surfaced the contact as a "drifting commitment" even when they were well within their cadence window.
**Chosen rule:** Do NOT surface a contact within their cadence window just because next_action references an aged commitment. Trust the cadence — Kay knows when she'll see them next. Named commitments Kay wants tracked separately go in Beads or Motion, not relationship-manager surfacing.
**Reasoning:** Cadence-based contacts are nurture, not commitments. Mixing commitment-drift surfacing into cadence surfacing creates noise that obscures real overdue contacts. Stanley meets Kay quarterly and the next coffee is on the calendar — nothing for relationship-manager to do.
**Pattern:** #pattern/single-purpose-surfacing

## Why This Trace Matters

A future agent running relationship-manager would, by default, read `next_action` text the same way the skill did until today — because text is information-dense and feels authoritative. The field-vs-text conflict is silent: no error, no warning, just the wrong contact in the wrong bucket every morning. Lauren's case is the proof — 3 weeks of false positives before catch.

This trace anchors the rule for any future skill rewrite: structured fields beat free text for rule application, even when free text seems to give more context. Free text is for humans; fields are for agents.

## Key Insight

When a skill reads multiple Attio fields about the same concept, name the **single field** that owns the rule and explicitly demote all other fields to informational. Don't let the agent infer hierarchy from richness of the data — the rule must be hard-coded.

## Closure Mechanism

- Updated `.claude/skills/relationship-manager/SKILL.md` with "Cadence Field Is Sole Source of Truth" + "Within-Cadence Commitment Drift" sections, including the Lauren and Stanley precedents.
- Updated Lauren's Attio `next_action` to remove "quarterly" reference (cleared the offending text).
- New memory `feedback_close_out_executes_mutation.md` covers the upstream root cause (close-outs must mutate source-of-truth, not just log).

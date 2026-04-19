---
schema_version: 1.1.0
date: 2026-04-19
type: trace
title: "Briefing Architecture — Shift from Source-Organized to Action-Keyed 4-Bucket Format"
tags: ["date/2026-04-19", "trace", "topic/briefing-architecture", "topic/decision-fatigue", "topic/skill-design", "person/kay-schneider"]
people: ["[[entities/kay-schneider]]"]
companies: []
---

# Trace: Briefing Architecture Shift to Action-Keyed Buckets

## Trigger

On Sunday 4/19, mid-Sunday session, Kay reviewed her morning brief and reported the existing 5-section format ("Pipeline shifts / Pipeline summary / Action items / Carried items / System Status / Other") was buried in DealsX repeats and required scrolling/re-reading to act on. She didn't read the whole brief — she just saw the noise and tuned out.

The format had evolved organically by source-of-data ("here's what came from email, here's what came from calendar, here's what came from Attio") rather than by Kay's required action ("what must I decide today vs this week vs let drop").

## Decision

Replace the source-organized 5-section briefing format with a 4-bucket action-keyed format:

1. **Today / ASAP** — must ship today
2. **Decisions** — needs Kay's judgment, capped at ≤5 items, Obama framing (RECOMMEND + YES/NO/DISCUSS)
3. **This Week** — must do this week, not today
4. **Dropped Balls** — slipped follow-ups, overdue cadences, warm-intro replies needing recovery

Cluster by entity (one heading per person/deal/niche, not scattered). Label every item with C-suite ownership (CFO/CIO/CMO/CPO/GC). Numbering ascends across all buckets. System Status becomes a compact 1-line-per-skill tail.

Codified as: `feedback_briefing_three_buckets.md`, `feedback_decision_fatigue_minimization.md`, CLAUDE.md morning-workflow Step 9, pipeline-manager SKILL.md "Briefing Format" section + format-enforcement stop hooks, goodmorning command Step 7.

## Rationale

**The framing question is "what does Kay need to do?" not "where did this signal come from."** Source-of-data organization optimizes for the assembler (Claude); action-keyed organization optimizes for the decider (Kay).

**Decision fatigue is the binding constraint.** Kay is CEO + solo parent + sole operator of a 12-investor fund. Her cognitive budget for decisions per day is finite. Every avoidable decision is opportunity cost. The new format codifies an explicit cap (≤5 Decisions) and an explicit pre-decide rule ("default to recommending, not asking; pre-decide whatever is defensible").

**The Obama framing is borrowed from how POTUS staffers presented options.** RECOMMEND + one-sentence reason + YES/NO/DISCUSS lets Kay resolve most items in one keystroke. Bare questions force her to construct the recommendation herself, which is the work the system is supposed to do for her.

**Dropped Balls is the highest-leverage bucket.** A slipped follow-up costs deals; a missed Decision deferred to tomorrow rarely does. Naming the bucket explicitly forces the assembler to look for them rather than only surfacing what came in fresh today.

**Entity clustering is a hygiene rule, not a layout rule.** When 4 DealsX items appear scattered across 3 buckets, the visual noise drowns the actual asks. Clustering under one entity heading reduces re-reading and lets Kay see all asks for that entity at once.

## Alternative Rejected

The existing 5-section format. Kay's tune-out was the evidence — a brief that doesn't get read provides zero leverage no matter how complete it is.

A separate Slack early-warning push for Dropped Balls (the additive proposal) was also rejected — Kay always goes to Mac first in the morning per `feedback_mac_first_not_mobile`. Mobile pushes add a parallel notification stream that doesn't match her actual entry point.

## What Future Agents Should Know

- **Never present a brief in source-organized format.** Always action-keyed buckets.
- **Never present >5 Decisions without pre-deciding the lowest-stakes ones.** If you have 7 Decisions, 2 of them should have already been made via existing patterns — find which 2 and convert to "Done" status silently.
- **Never present a Decisions item as a bare question.** Always RECOMMEND + YES/NO/DISCUSS.
- **Never propose a mobile-first / phone-push enhancement.** Kay's morning entry point is the Cursor terminal on her Mac.
- **Never include the counter-option in the same question** ("or do X, or do Y?"). Ask the primary question alone; follow up if no.
- **Pipeline-manager has format-enforcement stop hooks** that run before output. If you're hand-assembling a brief outside pipeline-manager, run the same checklist mentally before sending.
- **The C-suite labels are not decoration.** They train Kay's mental model of who owns what — when she sees CFO five times in one brief, that's a signal her CFO-owned workload is heavy this week. Skipping the label loses that signal.

## Connected Decisions (same session)

- `feedback_friday_test_write_skills.md` — write skills get Friday dry-run before launchd
- `feedback_golden_examples_stable_deliverables.md` — stable deliverables get examples/ folder with Kay-approved goldens
- `feedback_skill_output_portfolio.md` — every brain/outputs file tagged with skill_origin + kay_approved
- `feedback_no_counter_in_question.md` — never stack counter-options in same question
- `feedback_mac_first_not_mobile.md` — Kay's morning entry is Cursor terminal on Mac, no parallel mobile pushes
- Schema v1.2.0 on `output.yaml` — adds skill_origin and kay_approved fields
- launchd: `com.greenwich-barrow.relationship-manager` loaded, fires Mon-Fri 6:50am ET to pre-warm relationship-status artifact before email-intel runs at 7am

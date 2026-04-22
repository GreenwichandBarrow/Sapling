---
schema_version: 1.1.0
date: 2026-04-21
type: trace
had_human_override: true
importance: high
target: process
tags: ["date/2026-04-21", "trace", "pattern/hypothetical-not-durable", "topic/constraint-framing"]
---

# Decision Trace: Stress-Test Constraint Application (Not Durable Deadline)

## Context

During niche-ranking conversation, Kay introduced a constraint: "We wrap by Feb 2027. Have to acquire in 6 months." Claude used this to reframe the ranking analysis (coffee pivoted from primary GO to backup #2, disqualification language applied to several niches). At session wrap, Claude proposed saving this as `project_six_month_acquisition_deadline.md` — a durable project fact.

## Decisions

### Codifying the 6-month deadline as project memory
**AI proposed:** Save `project_six_month_acquisition_deadline.md` (Feb 2027 fund wrap → Oct 2026 close deadline) as durable fact governing all future niche/DD prioritization.
**Kay's response:** "Project six months was a one off request, not a fact."
**Chosen:** DROP the project memory. Keep the constraint's within-session effects (niche re-ranking, pivot-to-Insurance/Pest) but do not codify as durable reality.
**Reasoning:** The constraint served the analysis as a pressure-test lens. It produced useful reframing (the ranking flipped because cold-pipeline niches lost under time pressure), but Kay did not commit to it as a binding operational deadline. Treating a hypothetical as a fact would lock future briefings into a non-existent deadline.
**Pattern:** #pattern/hypothetical-not-durable

## Learnings

- When Kay introduces a constraint mid-conversation ("what if," "imagine we," "assume," or a specific number that sounds binding), the default interpretation is stress-test framing, NOT a new operating fact.
- Durable codification requires explicit commitment language: "this is our actual deadline," "commit this as our plan," "this is binding."
- Within-session: apply the constraint fully. After-session: do NOT save as `project_*.md` unless committed.
- One direct question resolves ambiguity: "Is this a binding deadline or a stress-test framing for this analysis?"
- Codified as `feedback_stress_test_constraints_not_facts.md`.
- Especially applies to: timelines, budgets, headcount caps, geographic constraints, scope trims.

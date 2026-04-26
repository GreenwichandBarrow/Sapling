---
schema_version: 1.1.0
date: 2026-04-25
type: trace
today: "[[notes/daily/2026-04-25]]"
task: 3-hour scope cut on a 6-9hr launchd-hardening tech-debt block
had_human_override: false
importance: high
target: scripts:run-skill.sh, scripts:validate_phase2_integrity.py, .claude/skills/target-discovery
tags: [date/2026-04-25, trace, topic/launchd-hardening, topic/tech-debt, topic/scope-management, pattern/critical-path-first, domain/operational]
---

# Decision Trace: Cutting a 6-9hr tech-debt plan to 3hr by shipping critical path first

## Context

[[outputs/2026-04-25-saturday-launchd-hardening-plan]] (bead `ai-ops-1`) was a calendared 7-hour Saturday block to fix the launchd silent-failure bug from 4/19. Plan had 4 layers, original estimate 6-9hr:
- L1: Post-run validator in `run-skill.sh` (~2hr)
- L2: Headless prompt for target-discovery Phase 2 (~2-3hr)
- L3: Wire enrichment_integrity_check.py as mandatory (~30min)
- L4: Extend pattern to 4 other nightly mutating skills (~3-4hr)

Saturday afternoon got captured by an unplanned ~6hr Dashboard Session 6 marathon. By the time the calendar miss surfaced (Kay asked twice before I checked the calendar), only ~3hr remained before reasonable end-of-day. Sunday 10pm is the next Phase 2 fire — the canonical first test of any fix.

## Decisions

### Scope: ship L1+L2+L3, defer L4

**Considered:**
- (a) Push for full L1-L4 in 3hr. Original plan estimated 6-9hr. Compressing 3x means cutting tests, skipping per-skill validation logic, copy-paste errors across 5 skills.
- (b) Ship only L1 (the highest-leverage layer per root-cause doc — "Layer 1 alone fixes the Phase 2 silent-success bug"). Faster, but headless prompt (L2) is what stops the AGENT from inventing reasons to exit 0 — wrapper validator only catches the AGENT's mistake after it happened.
- (c) **Ship L1+L2+L3 (target-discovery only). Defer L4.** Critical path: tomorrow's 10pm fire is target-discovery Phase 2; the other 4 skills don't have a fire pending tomorrow.

**Chosen:** (c).

**Reasoning:** The 4/19 incident was target-discovery specifically. Sunday 10pm is the canonical re-test. Hardening that one skill end-to-end (wrapper + agent + skill doc) is more valuable than hardening 5 skills' wrapper-side only. L4 is independent — each skill can be hardened in a 30-45min follow-up block without re-touching the wrapper.

### Approval: pre-grant authorization for the 3hr run

**Trigger:** Kay's "please set so that approval is already received for the 3 hour run" mid-session — implicitly authorizing autonomous execution through commit + plist reload + launchctl reload, without per-step confirmation.

**Reasoning:** Reduces decision-fatigue per `feedback_decision_fatigue_minimization`. Tradeoff: I lose mid-stream course-correction. Mitigated by (a) committing each layer separately (rollback unit = layer), (b) backing up plist before edit, (c) running smoke tests before reload.

## Learnings

- **Critical-path-first beats coverage-first when the blast radius is concentrated.** 4 of the 5 mutating skills had no failure pending tomorrow. Spending equal time on each would have shipped no skill end-to-end.
- **In-loop validator + wrapper validator is defense-in-depth, not redundancy.** L3 (in-loop) is faster (correct mid-run). L1 (wrapper) is the safety net (catches if L3 was skipped). Both are cheap to ship together; either alone leaves a gap.
- **A scope cut is honest reporting, not a failure.** Telling Kay "3hr covers 3 of 4 layers" up front avoided the worse outcome of trying all 4 and shipping none.

## Why This Trace Matters

Future agents under time pressure default to "do everything fast" or "do one thing well." This is a third option: split the plan along blast-radius lines, ship the highest-stakes branch end-to-end, defer the rest with documented rationale. The pattern recurs whenever a calendared plan loses time to unplanned work and the original deadline is non-negotiable.

## Key Insight

**When the budget shrinks, cut by blast radius, not by component depth.** Half-shipping each of 4 layers leaves all 5 skills partially broken. Fully shipping 1 of 4 layers protects the most-likely-to-fail skill completely.

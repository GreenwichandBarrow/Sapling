---
schema_version: 1.1.0
date: 2026-05-01
type: trace
title: "One-off task graduates to specialized skill when lift exceeds Chief-of-Staff bandwidth — task-tracker-manager case"
tags: ["date/2026-05-01", "trace", "topic/skill-graduation", "topic/personal-task-tracker", "domain/process"]
importance: medium
target: process
---

# Skill graduation: when a one-off becomes a managed system

## Context

The TO DO 4.26.26.xlsx personal task tracker was built 2026-04-26 as an explicit one-off — Kay wanted to replace Motion (which generated too much noise), and the system was scoped as a static file with two helper scripts (`build_tasks_excel.py`, `populate_tasks_from_motion.py`). Memory `project_personal_task_tracker.md` recorded "One-off build; **not a skill**."

Five days later, on 2026-05-01, Kay surfaced the friction: she wanted the Chief of Staff (Claude) to handle daily appends, day-row promotion, and the Sunday rollover ceremony — not run a manual ceremony. The lift had grown past one-off territory.

## Decisions

### Graduate to specialized skill, not Chief-of-Staff inline

**AI proposed:** Two paths — (A) Chief of Staff handles tracker writes inline whenever Kay asks, document the patterns in CLAUDE.md, no new skill. (B) Build `task-tracker-manager` skill with verbs (append/promote/archive/reformat/report/gantt-tick), Chief of Staff invokes the skill, skill owns the file.

**Chosen:** **Path B** — full skill graduation. Six verbs, helper script `scripts/task_tracker.py`, SKILL.md with auto-vs-surface decision matrix, hard guardrails (lsof check, backup before write, trace every write).

**Reasoning:** Per CLAUDE.md hierarchy ("Kay → Claude (Chief of Staff) → Skills (specialized subagents, execute one job each)"), grunt-work execution belongs in skills, not Chief of Staff. The pattern Kay surfaced — "we built this as a one-off but as we are increasing the lift engaging with the file we should have a specialized sub agent" — is a clean signal that the file has moved from one-off to managed system. Chief-of-Staff inline writes would scale poorly: every Kay request becomes a fresh judgment call without standardized guardrails.

**Pattern:** Graduate a one-off to a skill when ANY of these are true:
1. Kay asks for the same operation 3+ times in a week
2. The file/process develops invariants that need codification (lsof check, backup-before-write, tab-naming convention)
3. Multiple distinct verbs emerge (here: append, promote, archive, reformat, report, gantt-tick)
4. Kay explicitly names the lift increase

## Why this trace matters for future agents

The inverse of `feedback_remove_kay_from_loop`. That memory says: automate Kay out of manual steps. This trace says: automate **Claude** out of ad-hoc execution once the work has shape. A Chief of Staff doing the same operation by hand for the third time is itself a Kay-decision-fatigue tax — every invocation requires Claude to re-derive the right shape, re-check the guardrails, re-pick the file path.

A skill captures the decided shape once. Future agents reading this trace should look for the same signal in the next one-off (likely candidates: budget tracker scripts, dashboard refreshers, niche scoring exports) and graduate them when the same triggers fire.

## Key insight

**One-offs decay into ad-hoc patterns. Skills crystallize them.** The five-day window between the original build (2026-04-26) and graduation (2026-05-01) is a useful upper bound — any one-off that's still being touched daily after a week deserves a graduation review.

## How a future agent should apply

When detecting one of the four graduation signals above for any existing one-off file/process:

1. Surface to Kay: `RECOMMEND: Graduate {one-off-name} into a skill — {signal observed} → YES / NO / DISCUSS`
2. If YES, propose verbs (3-7 ideal), decision matrix, guardrails, schedule integration.
3. Build skill at `.claude/skills/{skill-name}/SKILL.md` + helper script at `scripts/{skill_name}.py`.
4. Update the project memory to reflect graduation (replace "one-off" language with "owned by {skill-name}").
5. Write a trace recording the graduation decision (this file is the canonical example).

Avoid graduating prematurely. A pure one-off touched once and never again does not need a skill — the file itself is the artifact. Graduation is for sustained-engagement systems.

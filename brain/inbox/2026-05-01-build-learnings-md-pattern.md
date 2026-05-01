---
schema_version: 1.2.0
date: 2026-05-01
title: Add learnings.md to every skill (Harrison pattern)
status: backlog
source: call
urgency: low
source_ref: "[[calls/2026-04-30-harrison-wells-coaching-session]]"
confidence: high
tags: [date/2026-05-01, inbox, source/call, person/harrison-wells, company/dodo-digital, topic/claude-infrastructure, topic/skills-development, topic/calibration, urgency/low, status/backlog]
---

# Add learnings.md to every skill (Harrison pattern)

## Description

Harrison's pattern from the 4/30 coaching session: every skill ships with a `learnings.md` file that Claude writes back to as it learns from each run. Skill checks `learnings.md` BEFORE running and updates AFTER. Per Harrison, **negative directives outperform positive** (e.g., "do NOT do X" beats "do Y") because the model is better at avoiding flagged anti-patterns than at remembering positive instructions.

## Action

- Add `learnings.md` to one pilot skill first (suggest `pipeline-manager` or `target-discovery` — both are mature and have multiple corrections logged).
- Wire the SKILL.md preamble to read `learnings.md` at start, append to it at end of each run.
- Bias entries toward negative directives ("do NOT do X because Y").
- Once pilot proves out, roll the pattern across all `.claude/skills/`.
- Consider whether the `feedback_*.md` files in `memory/` should partially fold in (some are skill-specific and would belong in that skill's `learnings.md` instead of global memory).

## Context

- Source: [[calls/2026-04-30-harrison-wells-coaching-session]] section A.3.
- Tied to broader calibration pipeline: decision-traces → calibration-workflow → memory/feedback files. `learnings.md` would be a third tier (skill-local, runtime-updated).
- Low urgency — current calibration loop works; this is an upgrade, not a fix.
- Related: [[entities/harrison-wells]], [[entities/dodo-digital]].

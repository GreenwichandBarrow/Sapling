---
schema_version: 1.2.0
date: 2026-05-01
title: Build /discuss or /think skill — strategic conversation before plan mode
status: done
source: call
urgency: medium
source_ref: "[[calls/2026-04-30-harrison-wells-coaching-session]]"
confidence: high
tags: [date/2026-05-01, inbox, source/call, person/harrison-wells, company/dodo-digital, topic/claude-infrastructure, topic/skills-development, urgency/medium, status/done]
---

# Build /discuss or /think skill — strategic conversation before plan mode

## Description

Harrison's recommendation from the 4/30 coaching session: build a `/discuss` (or `/think`) skill that runs a strategic conversation phase BEFORE plan mode. Kay's framing: *"plan mode is the final step, not thinking it through with you."* Today she jumps straight into plan mode without first interrogating goals/constraints/alternatives with Claude. Kay said *"I'm definitely going to do that."*

## Action

- Define skill scope: open-ended Socratic conversation that surfaces goals, constraints, alternatives, hidden assumptions, and tradeoffs BEFORE any plan-mode artifact is generated.
- Write SKILL.md with trigger conditions (Kay invokes `/discuss` or `/think` when she's not ready for a plan yet).
- Confirm output handoff: when the discussion converges on direction, skill suggests "ready for plan mode?" and Kay opts in.
- Add to `.claude/skills/` and register slash command.

## Context

- Source: [[calls/2026-04-30-harrison-wells-coaching-session]] section A.5.
- Sister concept to plan mode: discussion → plan → execute (three-phase pipeline).
- Recurring pattern: Kay forgets plan mode (per `feedback_recommend_plan_mode`). Adding an earlier-stage skill gives her a softer entry point that flows naturally into plan mode.
- Related: [[entities/harrison-wells]], [[entities/dodo-digital]].

## Resolution

Closed 2026-05-10. Built as `/socrates` skill, registered in active skills list. Triggers on `/socrates`, `/think`, or `/discuss`. Frames problem, surfaces assumptions, names alternatives, hands off to plan mode at convergence. Three-phase pipeline (`/socrates` → `/plan` → execute) is now codified in CLAUDE.md.

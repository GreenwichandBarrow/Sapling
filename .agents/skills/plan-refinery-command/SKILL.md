---
name: plan-refinery-command
description: Codex-native wrapper for Claude-era /ideate and /refine commands. Use when Kay invokes /ideate, /refine, asks to improve a plan, generate options, pressure-test a design, or refine a strategy before execution. Routes to the plan-refinery skill while preserving command intent.
---

# Plan Refinery Command

This skill preserves the Claude-era `/ideate` and `/refine` commands.

Use the existing `plan-refinery` skill as the execution engine.

## Ideate

Use when Kay wants options, creative alternatives, strategic branches, or "what should we consider?"

Expected behavior:
- generate a small set of high-quality options
- name tradeoffs
- recommend one path
- avoid generic brainstorming sprawl

## Refine

Use when Kay already has a plan, workflow, skill, dashboard idea, or process and wants it made sharper.

Expected behavior:
- identify weak points
- preserve what works
- recommend concrete edits
- separate quick fixes from deeper redesign

## Migration Rule

If the topic is a migrated Claude workflow, compare against the preserved original contract before recommending simplification. The goal is not a lighter version; it is a faithful version plus intentional improvement.

## Success Criteria

Kay gets the same collaborative design-tree refinement she expected from Claude Code, with clearer Codex-native execution handoff.

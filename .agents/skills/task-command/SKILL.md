---
name: task-command
description: Codex-native /task wrapper for Kay's operating system. Use when Kay invokes /task, asks to turn a request into an actionable task, or wants a structured plan/execution path with decision traces, beads when available, and commit stewardship.
---

# Task Command

Use this skill to preserve the Claude-era `/task` behavior in Codex.

## Flow

1. Restate the task in plain English.
2. Decide whether it is:
   - immediate execution
   - planning first
   - needs another skill
   - needs Kay decision
3. If the task is multi-step, create or update a visible plan.
4. Use existing repo patterns and relevant skills.
5. Record durable decisions in `brain/session-decisions/` when the operating model changes.
6. Use `commit-steward` for commits when changes are ready.

## Beads / Trackers

If a task tracker such as `bd` is available and the repo already uses it, create/update the appropriate task. If not available, do not block execution; record the task in the relevant operating artifact instead.

## Guardrails

- Never send emails.
- Do not invent missing credentials or access.
- Do not use destructive git commands.
- Do not overwrite unrelated user changes.
- Use header-based spreadsheet references where Sheets are involved.

## Output

For small tasks, act and report the result.

For larger tasks, keep the plan short and update it as work completes.

## Success Criteria

The request becomes a tracked, executable work item with clear owner, artifact, validation path, and commit/closeout path.

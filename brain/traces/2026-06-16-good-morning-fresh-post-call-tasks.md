---
schema_version: 1.1.0
date: 2026-06-16
type: trace
task: Scope Good Morning post-call task review
had_human_override: true
review_status: pending
importance: high
target: skill:pipeline-manager
tags: [date/2026-06-16, trace, domain/process, pattern/morning-briefing, status/pending]
---

# Good Morning Fresh Post-Call Tasks

## Context

Kay asked whether Good Morning can include tasks that came up from post-call analysis in the prior 24 hours. The existing behavior read every pending post-call task file, which mixed fresh task candidates with stale backlog and created morning-review noise.

## Decisions

### Fresh 24-hour post-call candidates over full pending backlog

**AI proposed:** Continue treating every pending post-call task file as morning-review material.

**Chosen:** Good Morning should surface only post-call-analysis task candidates from the prior 24 hours. Older pending files are backlog and should be routed to Task Manager review instead of expanded inside Daily Ops.

**Reasoning:** Fresh post-call tasks belong in morning approval because they are time-sensitive and context is still active. Older staged files need cleanup judgment and should not compete with daily operating decisions.

**Pattern:** #morning-briefing

## Learnings

- Good Morning should include fresh post-call task candidates for approval, but it should not become a historical post-call backlog review.
- Task Manager owns backlog cleanup before canonical To Do writes.

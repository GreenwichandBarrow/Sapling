---
schema_version: 1.1.0
date: 2026-06-10
type: trace
task: Update goodnight workflow for multi-thread Codex operating model
had_human_override: true
importance: high
target: command:goodnight
tags: [date/2026-06-10, trace, topic/goodnight, topic/codex-threads, status/done]
---

## Context

Kay asked whether separate Codex chat threads meant `/goodnight` needed to commit all threads. The issue was not literally committing chat transcripts; it was that separate operating threads can create repo artifacts and decisions outside the canonical daily rhythm chat.

## Decisions

### Make goodnight multi-thread-aware
**AI proposed:** Treat this as a calibration candidate for later.
**Chosen:** Kay asked to update the workflow now, and `/goodnight` was updated to require an active/recent thread inventory before writing session decisions.
**Reasoning:** Once work splits across Codex threads, a current-chat-only closeout loses decisions, leaves artifacts uncommitted, or stages unrelated dirty files without ownership. The closeout must include each thread as Included, No repo delta, or Excluded with reason.
**Pattern:** #multi-thread-closeout

## Learnings

Future goodnight runs should not trust the current conversation as the full source of truth. If thread tools are unavailable, use repo evidence: `git status`, continuation files, verb logs, and dated artifacts. Every remaining dirty file after a goodnight commit needs an explicit reason.

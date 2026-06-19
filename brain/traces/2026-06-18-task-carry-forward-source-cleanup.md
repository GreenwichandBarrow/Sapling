---
schema_version: 1.1.0
date: 2026-06-18
type: trace
tags: [date/2026-06-18, trace, pattern/task-carryover, status/pending]
task: Task tracker carry-forward cleanup
had_human_override: true
review_status: pending
importance: high
target: skill:task-tracker-manager
---

# Task Carry-Forward Source Cleanup

## Context

Kay observed that when Task Manager moves prior-day unchecked items into the current day during a Good Morning run, the prior day remains visually messy: moved rows leave blank or black-looking gaps, while completed checked rows stay scattered. She asked that the prior day be cleaned up so checked rows move to the top.

## Decisions

### Pack Checked Prior-Day Rows After Carry-Forward

**AI proposed:** Carry-forward moved unchecked tasks forward but left the source day layout mostly as-is.

**Chosen:** After `carry-forward-day`, clean the source day tab by packing checked/completed rows to the top, any remaining unchecked rows beneath them, and blanks below.

**Reasoning:** Kay uses day tabs as visual working surfaces. A prior day should be readable history after carry-forward, not a sparse grid with gaps. This is now part of the carry-forward contract for Good Morning and Good Night.

**Pattern:** #task-carryover

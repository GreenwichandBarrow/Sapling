---
schema_version: 1.1.0
date: 2026-06-17
type: trace
tags: [date/2026-06-17, trace, pattern/briefing-preflight, pattern/task-carryover, status/pending]
task: Good Morning / Good Night operating rhythm correction
had_human_override: true
review_status: pending
importance: high
target: skill:pipeline-manager
---

# Good Morning Brief Prep and Carryover Correction

## Context

During the 2026-06-17 Daily Operating Rhythm, Kay corrected two operating assumptions. First, Sam Hyde / Steuart Botchford briefs should already have been prepared for the day's meeting, and Luka Salamunic / Sara Rosenthal briefs should be prepared for the following day. Second, Task Manager should carry prior-day incomplete tasks forward so Wednesday contains both already-planned Wednesday work and unfinished earlier-day work.

## Decisions

### Generate Missing Required Briefs Instead of Asking

**AI proposed:** Surface the issue as a question in the morning briefing and then react after Kay answered.

**Chosen:** Prepare the missing Sam / Steuart brief immediately and prepare Luka / Sara briefs for the next day.

**Reasoning:** Kay's correction was that these briefs were expected operational prep, not optional briefing content. Future Good Morning runs should enumerate today and tomorrow external meetings, verify whether required briefs exist, and generate missing briefs or surface a clear failure if generation is blocked.

**Pattern:** #briefing-preflight

### Repair Carryover Directly Through Task Manager

**AI proposed:** Treat prior-day incomplete tasks as an item for Kay to review.

**Chosen:** Run task-tracker carry-forward commands immediately after Kay confirmed that incomplete prior-day tasks should carry into Wednesday.

**Reasoning:** Kay's expected behavior is that not-completed day-tab items roll forward. When that invariant fails, the system should repair through the Task Manager workflow, then report any capacity blockers. It should not leave the issue as a mental note or ask Kay to manually reconcile.

**Pattern:** #task-carryover

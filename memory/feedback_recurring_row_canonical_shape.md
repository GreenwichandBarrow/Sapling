---
name: feedback_recurring_row_canonical_shape
description: "A recurring To Do item = Status \"On-going\" + Horizon \"Weekly Recurring {Day}\" ONLY; never duplicate recurrence/day in Notes"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e928b23a-183e-488d-8287-8428f26d12c3
---

A recurring item in the personal task tracker `To Do` tab has exactly one canonical representation: **Status = `On-going`** and **Horizon = `Weekly Recurring {Day}`** (e.g. `Weekly Recurring Mon`). The recurrence cadence and target day live in the **Horizon column ONLY**. The Notes column holds genuine context (what the task entails) and must NOT restate "Recurring weekly", "(Mon)", or any day/cadence label.

**Why:** 2026-05-17 consolidation migration carried the old Recurring-tab note text ("Recurring weekly", "Recurring weekly (Mon)") into the new `To Do` Notes column. That duplicates what Horizon already encodes and is precisely the "encode the day in Notes/task name" pattern Kay and Claude explicitly rejected during the /socrates design conversation (the dropdown-Horizon approach was chosen specifically to avoid free-text day encoding). Kay corrected the rows manually and said: "you just mentioned it in the notes, which was not the decision we made." Putting the same fact in two places creates drift and contradicts the locked design.

**How to apply:** When creating/migrating/stamping a recurring row, set Status `On-going` + Horizon `Weekly Recurring {Day}` and leave Notes free of recurrence/day text. When reading recurring rows, trust Horizon as the single source of cadence+day, never parse Notes. If a migration/import source has a recurrence note, strip it — do not carry it into Notes. See [[project_personal_task_tracker]], [[feedback_weekly_plan_layers_on_carryover]].

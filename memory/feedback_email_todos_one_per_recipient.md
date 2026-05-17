---
name: feedback_email_todos_one_per_recipient
description: "Email to-dos must be captured as one row per recipient/email, never bundled into a single multi-name row"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e928b23a-183e-488d-8287-8428f26d12c3
---

When creating email-related to-dos in the personal task tracker (To Do tab, day tabs, Week tab), **break them out one row per recipient / per email**. Never bundle multiple people into a single row like "Email follow-ups: Carlos, Becky, Laura, ...".

**Why:** 2026-05-17 — Claude captured a Sunday slot as "Email follow-ups: Carlos, Hamptons Pest, Jay & Jason, Matt, Becky, Laura, Krupa, Deborah" (one row, 8 people). Kay can only check ONE box for that row, so partial progress is invisible and she can't track which sends are done. A row's checkbox/Status is binary — it must map 1:1 to a single actionable email so each completes independently.

**How to apply:** Any time multiple email/follow-up sends are surfaced (pipeline-manager action items, conference follow-ups, intro chains, ad hoc "email X, Y, Z"), append/promote them as separate rows — one per recipient — each with its own Status. Same logic for any task where Kay needs to track sub-items independently: if it has N independently-completable parts, it's N rows, not one. See [[project_personal_task_tracker]], [[feedback_recurring_row_canonical_shape]], [[feedback_weekly_plan_layers_on_carryover]].

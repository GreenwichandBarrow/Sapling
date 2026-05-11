---
schema_version: 1.2.0
date: 2026-05-11
title: Skill-build session — task-tracker-manager (5 gaps) + budget-manager (1 gap)
status: backlog
source: manual
urgency: medium
due_date: 2026-05-25
automated: false
tags:
  - date/2026-05-11
  - inbox
  - source/manual
  - skill/task-tracker-manager
  - skill/budget-manager
---

# Skill-build session: task-tracker-manager + budget-manager

Surfaced during 2026-05-11 Monday session while applying triage decisions to the personal task tracker. Multiple verb gaps required workarounds; one budget-manager projection bug surfaced via the Q1 health-anomaly correction.

## task-tracker-manager — 5 gaps

1. **`archive` verb HIDES tabs — must move-to-far-right instead.** Kay corrected explicitly 2026-05-11: "I dont want any hidden archive. I pulled it back out and put it all the way to the right." Update `scripts/task_tracker.py` archive verb to use openpyxl tab-reorder, not state=hidden.

2. **`archive` verb breaks on Monday-of-current-week edge case.** When run on a Monday, computes next-Monday=current+7 instead of current. 2026-05-11 apply-all subagent had to manually rename "May 18-24" → "May 11-17" after archive verb fired wrong. Add edge-case handler: if today is Monday, new live-tab name uses today, not today+7.

3. **New `archive-todo` verb + "Completed To Do" tab schema.** Sweep ✅ rows from To Do tab → new "Completed To Do" tab (mirror of To Do structure, with `completed_date` column). Running list of completions. Trigger: Sunday /goodmorning weekly ceremony, also on-demand.

4. **New `schedule-to-day-slot` verb (direct, not 2-step).** Currently requires append-then-promote. Add a single verb that takes (item, day, type) and lands it directly in the priority slot for that day.

5. **New `projects-add` verb.** Currently must use openpyxl directly (apply-all subagent did this for "Deal Aggregator Expansion" project row). Add a verb: takes (name, type, status, target-date) and appends row to Projects tab.

## budget-manager — 1 gap

6. **Distinguish recurring vs one-time line items when projecting runway.** Today the script projected Q1 actuals into a 7.5mo runway / Nov 2026 cash-zero / $7,393/mo savings target. Reality: $8,250 Q1 health was one-time, true runway is 9.46mo. Naive run-rate projection amplified the Q1 anomaly into a burn-cliff. Fix: add `--annotate-one-time` flag or a one-time line-items registry, strip those from forward projection.

## Acceptance

- All 5 task-tracker verbs ship + tested against the live xlsx (with VPS download/upload cycle)
- archive-todo verb tested on the new Completed To Do tab pattern
- budget-manager rerun on March P&L with one-time correction → produces 9.46mo runway natively (no manual reframe)
- All changes commit + push to main

## Related memory

- project_health_expense_one_time_q1_2026.md — the financial fact driving gap #6
- feedback_task_tracker_skill_executes_dont_make_kay_apply.md — the policy that motivated discovering gaps #4-5
- project_personal_task_tracker.md — current skill spec

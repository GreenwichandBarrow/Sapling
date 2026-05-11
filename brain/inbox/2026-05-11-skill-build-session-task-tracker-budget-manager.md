---
schema_version: 1.2.0
date: 2026-05-11
title: Skill-build session — task-tracker-manager (5 gaps, DONE) + budget-manager (1 gap, deferred to Friday)
status: partial-complete
source: manual
urgency: medium
due_date: 2026-05-15
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

**2026-05-11 update:** All 5 task-tracker gaps shipped in the same Monday session (Kay reopened the file later that day). The budget-manager gap (#6) was deferred to Friday per Kay's redirect: the budget script already ran today (Tue slot 2 marked ✅), and the Friday work is the *human assessment* of cuts, not a re-run with annotation. The skill-code fix lives on as a Friday task entry.

## task-tracker-manager — 5 gaps ✅ DONE

1. ✅ **`archive` verb HIDES tabs — must move-to-far-right instead.** Fixed in `scripts/task_tracker.py:cmd_archive`: `dst.sheet_state = "visible"` + `wb.move_sheet(..., offset=len(wb.sheetnames) - 1 - current_idx)` parks the archive tab at the far right.

2. ✅ **`archive` verb breaks on Monday-of-current-week edge case.** Fixed: when `today.weekday() == 0`, `new_monday = today` (not `today + timedelta(days=7)`).

3. ✅ **New `archive-todo` verb + "Completed To Do" tab schema.** Implemented. Creates the tab idempotently on first run; sweeps ✅ rows from To Do → Completed To Do with a `Completed` date column in H. Wired into `goodnight` AUTO-EXECUTE per updated SKILL.md.

4. ✅ **New `schedule-to-day-slot` verb (direct, not 2-step).** Implemented with optional `--slot` (auto-picks first empty when omitted) + `--force` to overwrite occupied slots.

5. ✅ **New `projects-create-gantt` verb.** Implemented. Clones the Myself Renewed Healthcare structure (title/subtitle/header row 5 with N weekly Monday-anchored columns), updates Projects index with HYPERLINK formula, supports both append-new-row and update-existing-row paths. Entity-color conditional formatting drives the Gantt bar.

## budget-manager — 1 gap (DEFERRED TO FRIDAY)

6. **Distinguish recurring vs one-time line items when projecting runway.** Deferred to Friday 2026-05-15. Friday's slot already has the human-assessment work scheduled ("Assess budget reduction areas — post-Q1 expense review; explore summer desk takeover"); the skill-code fix is a separate Friday task that can pair with Kay's review session. **Re-evaluate Friday whether to:** (a) bundle the fix into Friday's assessment session, (b) defer further if Friday-review already produces actionable cuts without script rerun, or (c) split into a quick `--annotate-one-time` patch + leave the broader recurring-vs-one-time registry to a later sprint.

## Acceptance

- ✅ All 5 task-tracker verbs shipped + tested against the live xlsx (VPS download/upload cycle worked clean)
- ✅ archive-todo verb tested on the new Completed To Do tab pattern (no ✅ rows present yet — tab created idempotently)
- ✅ `projects-create-gantt` tested by creating "Deal Aggregator Expansion" Gantt tab live
- ⏭️ budget-manager `--annotate-one-time` deferred to Friday 2026-05-15
- ✅ All task-tracker changes committed + pushed to main

## Related memory

- project_health_expense_one_time_q1_2026.md — the financial fact driving gap #6
- feedback_task_tracker_skill_executes_dont_make_kay_apply.md — the policy that motivated discovering gaps #4-5
- project_personal_task_tracker.md — current skill spec

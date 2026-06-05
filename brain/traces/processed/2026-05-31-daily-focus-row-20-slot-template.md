---
review_status: applied
schema_version: "1.1.0"
date: 2026-05-31
type: trace
title: "Task-tracker template gained a DAILY FOCUS row (13) + grew to 20 slots"
tags:
  - date/2026-05-31
  - trace
  - skill/task-tracker-manager
  - topic/daily-focus-template
  - topic/task-tracker-20-slot-grow
  - status/done
---

# Template change: DAILY FOCUS row + 20 priority slots

## Trigger
Setting this week's to-dos, Kay (a) added a `DAILY FOCUS` banner row to the Week tab + every day tab so each day states its theme, and (b) hit the 15-slot ceiling on Monday (22 tasks) and directed "grow the template to 20."

## Decision
Make both permanent structural changes on the live file: `DAILY FOCUS` at **row 13** (above the task-column header, which moved to row 14; slots start row 15), and grow priority capacity from **15 → 20 slots** (rows 15–34; Monday 22 → row 36). Applied to Week tab + all 7 day tabs.

## Alternatives Considered
- **Row 2 placement for the focus banner** (zero structural ripple). Rejected: Kay had already built it at row 13 framing the task list and said keep it there.
- **Force-fit Monday's overflow** (top-15 + backlog the rest, or spill into notes). Rejected: Kay explicitly wanted the capacity grown, not the work truncated.

## Reasoning
Grow the structure to fit real volume rather than forcing the work into a rigid ceiling. The focus row turns the abstract daily theme into a visible header on the surface Kay actually works.

## Why This Trace Matters
The code does NOT yet reflect this. `scripts/task_tracker.py` constants (`DAY_SLOT_FIRST_ROW/LAST_ROW`, `WK_SLOT_*`, `DAY_NOTES_*`, `DAY_COL_HEADER_ROW`) + `build_day_tabs.py` + `build_week_tab.py` still assume the old layout (no row-13 focus, 15 slots, header at 13/slots at 14). Any scripted write (`promote`, `distribute-week`, next `build-week`, `reformat`) will misalign by one row and could clobber the focus row. Code hardening is a required follow-up: add `DAY_FOCUS_ROW=13` (preserve in clear logic), shift header→14, slots→15–34 (20), notes down; mirror on the Week tab.

## Key Insight
A user-made structural change to a live sheet is now ahead of the code that maintains it. Until the layout constants + builders catch up, treat scripted day-tab/Week writes as unsafe on this file and do them directly (read back to verify) — never trust a verb that assumes the old geometry.

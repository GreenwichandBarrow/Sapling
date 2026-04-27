---
date: 2026-04-27
type: output
output_type: session-decisions
title: "Session Decisions — 2026-04-27 (Monday)"
tags: ["date/2026-04-27", "output", "output/session-decisions", "topic/personal-task-tracker", "topic/excel-build", "status/draft"]
---

# Session Decisions — 2026-04-27 (Monday)

Personal-tooling-only session. Built [[outputs/to-do-4-26-26-xlsx|TO DO 4.26.26.xlsx]] to replace Motion. Five-tab architecture (This Week / To Do / To Do Long Term / Projects index / first Gantt project tab). Session began evening 2026-04-26, crossed midnight, wrapped 2026-04-27.

## Decisions

### Replace Motion with Excel-based personal task tracker
- **APPROVE** — Motion creates too much noise (recurring auto-tasks, near-duplicates, principles-not-tasks). Kay wants Excel for the daily/weekly view + paper for journaling. Built [[outputs/to-do-4-26-26-xlsx|TO DO 4.26.26.xlsx]] in `/Users/kaycschneider/My Drive/STRATEGIC PLANNING/`. Two python scripts (`scripts/build_tasks_excel.py` + `scripts/populate_tasks_from_motion.py`) own structure + data refresh.

### Architecture: 5-tab layout
- **APPROVE** — (1) **This Week** with habit tracker + day grid + donuts + notes/journal area; (2) **To Do** = single capture point, tagged Type+Project; (3) **To Do Long Term** = intents/someday items; (4) **Projects** = index of activated time-bound projects with hyperlinks; (5) per-project Gantt tabs (only for activated projects). Kay's wording: "everything sits in backlog and then projects is an organized view by entity or project title."

### Promotion model for projects (not upfront structure)
- **APPROVE** — Items live as "Create project for X" intents on To Do Long Term. Only when ready to plan do they get promoted to a Projects-tab Gantt. Kay's wording: "they stay on To Do Long Term as 'create project for xxx' and then once its time to create that project, it goes to a gantt if its time bound." Avoids tab proliferation.

### Manual-tick Gantt (not auto-driven by Start/Target)
- **APPROVE** — Each timeline cell is a checkbox; ticking fills the cell entity-color. Building a contiguous run of ticks across weeks creates the Gantt bar. Kay rejected the auto-format approach. Start/Target columns stay as planning reference but no longer drive the bar.

### Healthcare Gantt as first seed project
- **APPROVE** — 10 milestones rolled up from Backlog nonprofit-launch tasks (501c3 verification, board resolution, donation processor, etc.) + placeholder for healthcare program design. 16-week timeline, rose entity color.

### Type tags stay Home/Work; entities expressed via Project column
- **APPROVE** — Briefly considered subdividing Type into 5 entity options (Home/G&B/Myself Renewed/Kai Grey/Panthera Grey). Kay pivoted: entity granularity belongs at the Project level, not the task tag. Backlog Type column reverted to binary Home/Work; Projects index has Entity dropdown.

### Slim Work list (18 items)
- **APPROVE** — From ~80 OCR'd Motion tasks across 12 screenshots, recommended ~50 keepers + ~25 drops. Kay further trimmed Work to 18 items, dropped: Sonja coffee, Denning Rodriguez follow-up, Eric Dreyer outreach, LinkedIn → Attio export, E&K SaaS CIM, UPS mailbox renewal, Britta Nelson follow-up, NY Dept of State confirm, G&B management report review, Krista Searching-with-Claude email, Rachel Tepper / Zoe intro, 1st/2nd/3rd LOI placeholders, Suzanne & Lily intro, Kinji Fundraising class.

### Habit list final: 7 items
- **APPROVE** — Water & hygiene / Meditation & stretches / ACV drink & probiotic protein shake / Exercise class / Bike to work / 10K steps / Omega 3 & magnesium. No sub-headers; single block. Earlier 9-item version felt "too much" — Kay slimmed.

### European Mon-Sun calendar week
- **APPROVE** — Day grid runs Monday → Sunday, not Sunday → Saturday. Date formulas use WEEKDAY(...,2) for Monday-anchored math.

### Donuts over each day, no bar charts
- **REJECT** (bar charts) — Kay: "I dont need the bar charts on anything... seem redundant." Kept the per-day donut over each day (anchored above the day's task area, fills sage as priorities tick to ✅).

### Priority checkboxes side-by-side, not stacked
- **REJECT** (vertical pair) — First implementation put status above task in stacked rows. Kay: "the drop down for the check mark is ok but it should be next to the item, not on top of." Restructured day grid into 2 sub-cols per day (small status + wide task). Status cell sits LEFT of task in same row.

### Save as project memory, not as skill
- **APPROVE** — Skills are for recurring logic-driven workflows (deal-evaluation, niche-intelligence). Personal task tracker is a one-off artifact; once built, Kay works in Excel directly. Memory at `memory/project_personal_task_tracker.md` captures architecture + script paths + rollover ceremony + pending items.

## Actions Taken

- **CREATED** — `scripts/build_tasks_excel.py` — full workbook structure: 5 tabs, donut charts, conditional formatting, manual-tick Gantt builder function
- **CREATED** — `scripts/populate_tasks_from_motion.py` — clears + writes To Do (33 items), To Do Long Term (5 intents), Projects index (1 active project)
- **CREATED** — `/Users/kaycschneider/My Drive/STRATEGIC PLANNING/TO DO 4.26.26.xlsx` — the actual file
- **CREATED** — `memory/project_personal_task_tracker.md` — project memory with file path, scripts, architecture, Sunday rollover ceremony, pending items
- **UPDATED** — `memory/MEMORY.md` — added project memory index entry

## Deferred

- **"Create brochure for LF" entity assignment** — Kay never specified which work entity (G&B / Kai Grey / Panthera Grey). Currently tagged just Work. Trigger: Kay's next session on the file.
- **Healthcare program design milestone** — placeholder; Kay needs to break down into plan tiers + delivery model. Trigger: Kay's design pass.
- **Suzanne & Lily intro + Kinji Fundraising class** — dropped from Work list. Trigger: if Kay surfaces them again.
- **Old `G&B TO DO 3.23.26.xlsx`** in Strategic Planning folder + old `~/Documents/Tasks.xlsx` backup — Kay to decide when to archive/delete. Trigger: confidence in new file.

## Open Loops

- First real-week use of the new tracker (testing planning + tick + Sunday rollover)
- Untested: Sunday rollover ceremony (right-click → copy → rename last week's dates → hide → clear live tab)
- Future Gantt projects to seed when Kay activates more from To Do Long Term (most likely candidates: French Passports, Wedding Album)

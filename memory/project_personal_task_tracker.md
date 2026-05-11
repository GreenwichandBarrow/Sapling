---
name: Personal Task Tracker (TO DO M.DD.YY.xlsx)
description: Kay's personal Excel-based task system replacing Motion. Owned by task-tracker-manager skill as of 2026-05-01. Architecture, file paths, scripts, verbs, conventions.
type: project
originSessionId: 29fe887a-b391-45f3-9e99-2be7e94b5ed5
---
# Personal Task Tracker

Built 2026-04-26 to replace Motion (which generated too much noise). **Graduated 2026-05-01** from one-off to skill-owned file. Skill: `task-tracker-manager` at `.claude/skills/task-tracker-manager/SKILL.md`. Helper: `scripts/task_tracker.py`.

## File location
- **Live working file:** `/Users/kaycschneider/My Drive/STRATEGIC PLANNING/TO DO M.DD.YY.xlsx` (currently `TO DO 4.26.26.xlsx`)
- **Clean template (empty):** `/Users/kaycschneider/My Drive/MANAGER DOCUMENTS/G&B MASTER TEMPLATES/TO DO TEMPLATE.xlsx`
- **Backups:** `~/My Drive/STRATEGIC PLANNING/TO DO 4.26.26.bak.{YYYYMMDD-HHMMSS}.xlsx` — auto-created by skill before every write, last 5 retained.

When Kay rebuilds for a new template version, follow her file naming convention: `TO DO M.DD.YY.xlsx` in the STRATEGIC PLANNING folder. Easiest path: duplicate the template, rename, then run `populate_tasks_from_motion.py` if she wants the prior To Do data carried in. Or just rebuild via `TASKS_XLSX_OUT={path} python3 scripts/build_tasks_excel.py`.

## Build scripts (in this repo)
- `scripts/build_tasks_excel.py` — full workbook structure (tabs, formulas, charts, conditional formatting, Healthcare Gantt seed). **Note: as of 2026-05-01 chart objects are stripped on every reformat run.** New rebuilds should drop the chart code; left in place pending next rebuild cleanup.
- `scripts/populate_tasks_from_motion.py` — clears data rows + writes the To Do, To Do Long Term, and Projects index data
- `scripts/maintain_tasks_excel.py` — bootstrap one-shot maintenance (donut delete + percent promotion + CF reapply + tab rename). Was used 2026-05-01 to migrate to the new layout. Skill's `reformat` verb is the long-term equivalent.
- `scripts/task_tracker.py` — skill helper. Six subcommands: `append`, `promote`, `archive`, `reformat`, `report`, `gantt-tick`.

**Run order to rebuild from scratch:** close Excel → run build → run populate → run reformat → open. The build wipes all data; populate restores it; reformat strips charts and applies the new layout.

## Architecture — 5 tabs

1. **Live week tab** — habit tracker (7 items, Mon-Sun grid) + day grid (Mon-Sun, **big % display per day** at rows 17-21 [migrated 2026-05-01 from openpyxl DoughnutCharts which render blank on Excel-Mac], **15 priority slots** per day, slim 8-row notes area). Each day spans 2 sub-columns: small status + wide task. Priority checkbox sits LEFT of task text in same row.
   - **Tab name = current Mon-Sun range** (e.g. `Apr 27-May 3`, `May 4-10`). Renamed each Sunday by `task_tracker.py archive`. Old name "This Week" deprecated 2026-05-01 — Kay wants the date visible at the bottom of Excel without opening the tab. Date formulas inside the tab reference TODAY(), not the tab name, so renaming is safe.
2. **To Do** — single capture point for all tasks. Columns: Status / Task / Type (Home or Work) / Project (optional tag, links to a project name) / Due / Notes. Items tagged "Myself Renewed Healthcare" connect to that Gantt tab.
3. **To Do Long Term** — intents/someday items without hard timelines. Status options: Idea / Active / On hold / Promoted / Done. When an item is ready to be worked on with milestones, it gets promoted to a Projects tab.
4. **Projects** — index of *active* time-bound projects with Entity / Status / Start / Target / Tab hyperlink / Notes. Currently holds: Myself Renewed Healthcare.
5. **Myself Renewed Healthcare** — first Gantt-project tab. 10 milestones × 16 weekly columns. Each timeline cell is a manual checkbox; ticking fills the cell rose-pink. Building a contiguous run of ticks across weeks visually creates a Gantt bar.

Plus hidden archive tabs `archive_{Mmm D-D}` accumulating from each Sunday rollover.

## Skill verbs (`task-tracker-manager`)

| Verb | Trigger | Auto vs surface |
|---|---|---|
| `append` | "Add to To Do" / mid-day capture / goodmorning capture pass | Surface as `RECOMMEND: Add to To Do — "X" / Type / Project / Due → YES/NO` for single items; surface for batch ≥3 |
| `promote` | "Move X to {day} slot {N}" | Always surface (affects day plan) |
| `archive` | `goodnight` Sunday | Auto |
| `reformat` | Detected broken CF / chart drift | Auto |
| `report` | Friday briefing / on-demand | Auto |
| `gantt-tick` | "Healthcare milestone N done" / "tick week K" | Auto |

## Key design decisions
- **European calendar week** (Mon-Sun, not Sun-Sat).
- **Big % display per day** instead of donut charts (2026-05-01 — see `brain/traces/2026-05-01-openpyxl-donut-mac-incompat.md`). Never re-add openpyxl chart objects.
- **Sage-green palette** from Instagram template Kay liked.
- **Manual-tick Gantt** (not auto-driven by Start/Target dates) — Kay wanted the tick-as-you-go feel, building the bar herself.
- **Type tags Work/Home only**, not subdivided into entities. Entities (G&B / Myself Renewed / Kai Grey / Panthera Grey) are expressed via the Project column instead.
- **Strikethrough + sage-light fill** on done items everywhere (priorities, habits, To Do, projects).
- **Habit tracker stays visible** when scrolling into day grid (freeze pane at A15).
- **Promotion via skill, not drag.** Excel inherits source-cell conditional-formatting rules on drag, breaking the destination grid. Always use `task_tracker.py promote`. Source row gets `→` status indicator.
- **lsof guardrail.** Skill verbs that mutate the file run `lsof` first; refuse if Excel has the file open. See `brain/traces/2026-05-01-xlsx-write-lsof-guardrail.md`.

## Sunday rollover ceremony (now skill-driven)

Triggered by `goodnight` on Sunday evening. Calls `task_tracker.py archive`, which:
1. Loads the live week tab.
2. Copies it via `wb.copy_worksheet(src)`, renames the copy to `archive_{old-label}` (e.g. `archive_Apr 27-May 3`), hides it.
3. Renames the original to next week's label (`May 4-10`).
4. Clears habit checkmarks (rows 7-13 → ☐), priority status cells (rows 23-37 col `sc` → ☐), priority task text (cols `tc` → empty), notes (rows 40-47).
5. Saves + writes a trace + posts a one-liner to Slack `#operations`.

If `goodnight` runs on a non-Sunday, `archive` is skipped.

## Open items
- **mid-day-save 2026-05-01:** Live `TO DO 4.26.26.xlsx` still has DoughnutChart objects + tab name `This Week` until first `reformat` run completes (was blocked on Excel close at session end).
- **build_tasks_excel.py chart code is dead** — drop it on next rebuild cleanup. Kept temporarily for reference.
- **Old G&B TO DO 3.23.26.xlsx still in the folder** — Kay can decide when to archive/delete.
- **Old `~/Documents/Tasks.xlsx`** is a backup from earlier iteration, can be deleted.

## How to add a new Gantt project later
1. Edit `build_tasks_excel.py`: add a new `{PROJECT_NAME}_MILESTONES` list and call `build_gantt_project_tab(wb, "Project Name", "Entity", MILESTONES, weeks_span=N)` after the Healthcare seed
2. Edit `populate_tasks_from_motion.py`: add a row to `PROJECTS_INDEX` with the project name + entity + dates + hyperlink formula
3. Rerun build → populate → reformat
4. The skill's `gantt-tick` verb works on any project tab by name — no per-project wiring needed.

## Iterating on the file mid-week
**Don't rerun the build script** — it wipes everything. Use the skill verbs. If Kay edits Excel directly and breaks the conditional formatting, run `task_tracker.py reformat` to restore.

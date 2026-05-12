---
name: Personal Task Tracker (TO DO 5.12.26 Sheet)
description: Kay's personal Google Sheets task system replacing Motion. Owned by task-tracker-manager skill. Architecture, sheet ID, scripts, verbs, conventions. Migrated 2026-05-12 from Excel.
type: project
originSessionId: 29fe887a-b391-45f3-9e99-2be7e94b5ed5
---
# Personal Task Tracker

Built 2026-04-26 to replace Motion (which generated too much noise). **Graduated 2026-05-01** from one-off to skill-owned. Skill: `task-tracker-manager` at `.claude/skills/task-tracker-manager/SKILL.md`. Helper: `scripts/task_tracker.py`. **Migrated 2026-05-12** from Excel (`.xlsx` on iMac Drive) to Google Sheets so Kay can access from any browser.

## File location

- **Live working sheet:** `TO DO 5.12.26` — Google Sheet
  - **ID:** `1ewqQshtN5pz8kmMTEvBZgAFy-0XB37-MVONkN_mdZmk`
  - **URL:** https://docs.google.com/spreadsheets/d/1ewqQshtN5pz8kmMTEvBZgAFy-0XB37-MVONkN_mdZmk/edit
  - **Drive folder:** `STRATEGIC PLANNING` (`12IpnsQ5V_M1fiTm0NZM9wKhlerauILMd`)
- **Legacy Excel:** `~/My Drive/STRATEGIC PLANNING/TO DO 4.26.26.xlsx` — preserved as historical artifact, READ-ONLY, not actively maintained
- **Snapshots:** `brain/context/rollback-snapshots/tasks-{verb}-{timestamp}.json` — last 5 per verb retained

When Kay wants a new tracker (yearly cycle, after a major schema rework, etc.), follow her naming convention `TO DO M.DD.YY` in the STRATEGIC PLANNING folder. To create one: re-run `/tmp/tracker-migration/build_sheet.py` with `NEW_SHEET_TITLE` updated.

## Migration (2026-05-12) — Excel → Sheets

**Donut-chart restoration (same day, evening pass).** Excel→Sheets migration originally inherited the no-chart constraint (openpyxl renders xlsx-only chart objects that broke on Sheets import) and kept big-% text only in rows 17–21. Kay flagged the text-only display as visually inferior to her original aesthetic intent (real donut shape with hole). Donut charts rebuilt via Sheets API native `pieChart` objects with `pieHole=0.5` — 7 charts, one per day, anchored at row 17 of each day-pair's left column. Math moved to hidden helper tab `_donut_data`. Build script: `scripts/build_donut_charts.py`.

**Excel → Google Sheets cutover.** Triggered because Kay wanted browser-native access from any device (the iMac-only Excel path blocked the Hetzner VPS server from writing). Full migration in one pass:
- Created new Sheet (`TO DO 5.12.26`) with the 5-tab architecture mirrored
- Migrated all data: 52 To Do rows, 5 To Do Long Term rows, 2 Projects rows, 10 Healthcare milestones (incl. dates), Live Week habits + priority slots + notes
- Native Sheets primitives replace Unicode glyphs: checkboxes (Data Validation), dropdowns (Data Validation), conditional formatting (native rules)
- Rewrote `scripts/task_tracker.py` to use Sheets API via `requests` + `gog` refresh-token export. CLI surface preserved — all callers (skill, briefings) still work without changes.
- Snapshot-to-JSON (`brain/context/rollback-snapshots/`) replaces .xlsx file-copy backups
- `lsof` file-lock guardrail dropped (no longer relevant)
- Build scripts marked DEPRECATED: `build_tasks_excel.py`, `populate_tasks_from_motion.py`, `maintain_tasks_excel.py`

**Old Excel left in place.** Kay decides when to archive/rename it; do not auto-delete.

## Architecture — 5 tabs

1. **Live week tab** — habit tracker (7 habits, Mon-Sun grid) + day grid (Mon-Sun, **native donut chart per day** at rows 17-21 (pie + pieHole=0.5, driven by hidden helper tab `_donut_data`), **15 priority slots** per day, slim 8-row notes area). Each day spans 2 sub-columns: small status + wide task. Priority checkbox sits LEFT of task text in same row.
   - **Tab name = current Mon-Sun range** (e.g. `May 11-17`). Renamed each Sunday by `task_tracker.py archive`.
2. **To Do** — single capture point for all tasks. Columns: Status (checkbox) / Task / Type (dropdown: Work or Home) / Project (dropdown: G&B, Kai Grey, Panthera Grey, Myself Renewed, Home — free text allowed) / Due (date) / Notes. Header row frozen.
3. **To Do Long Term** — intents/someday items without hard timelines. Status dropdown options: Idea / Active / On hold / Promoted / Done. When ready to plan, promote to a Projects tab.
4. **Projects** — index of *active* time-bound projects with Project / Entity (dropdown) / Status (dropdown: Plan Needed / Active / On hold / Done) / Start / Target / Tab hyperlink / Notes. Currently holds: Myself Renewed Healthcare, Deal Aggregator Expansion.
5. **Myself Renewed Healthcare** — first Gantt-project tab. 10 milestones × 16 weekly columns. Each timeline cell is a native checkbox; ticking fills the cell blush-pink (entity color). Building a contiguous run of ticks visually creates a Gantt bar.

Plus: **Deal Aggregator Expansion** (Gantt, 12 weeks from 2026-05-11, G&B sage). **Completed To Do** (created by `archive-todo` on first run, sweeps completed To Do rows). Archive tabs `archive_{Mmm D-D}` accumulate from each Sunday rollover, parked far-right.

## Build scripts (in this repo)

- `scripts/task_tracker.py` — skill helper. Eight subcommands: `append`, `promote`, `archive`, `archive-todo`, `schedule-to-day-slot`, `projects-create-gantt`, `reformat`, `report`, `gantt-tick`.
- **DEPRECATED:** `scripts/build_tasks_excel.py`, `scripts/populate_tasks_from_motion.py`, `scripts/maintain_tasks_excel.py` — Excel-era build path. Replaced by the one-shot `/tmp/tracker-migration/build_sheet.py` for any future rebuild. Kept in repo for reference; do not run.

## Skill verbs (`task-tracker-manager`)

| Verb | Trigger | Auto vs surface |
|---|---|---|
| `append` | "Add to To Do" / mid-day capture / goodmorning capture pass | Surface as `RECOMMEND: Add to To Do — "X" / Type / Project / Due → YES/NO` for single items; surface for batch ≥3 |
| `promote` | "Move X to {day} slot {N}" | Always surface (affects day plan) |
| `schedule-to-day-slot` | "Schedule X for {day}" | Always surface |
| `archive` | `goodnight` Sunday | Auto |
| `archive-todo` | `goodnight` Sunday (also safe on any day) | Auto |
| `projects-create-gantt` | "Start a project for X" | Always surface |
| `reformat` | Detected broken CF | Auto |
| `report` | Friday briefing / on-demand | Auto |
| `gantt-tick` | "Healthcare milestone N done" / "tick week K" | Auto |

## Key design decisions

- **European calendar week** (Mon-Sun, not Sun-Sat).
- **Native Google Sheets donut charts per day** in rows 17–21 (one chart per day, pie + pieHole=0.5). Reverted 2026-05-12 from the interim big-% text display. Math is driven by the hidden helper tab `_donut_data` (7 rows × 3 cols: Day / Done / Left) which holds `COUNTIF` + `COUNTA` formulas pointing back at the Live Week status + task ranges. Charts re-render live as checkboxes toggle. **Never re-add openpyxl chart objects** (Excel-only constraint that broke `.xlsx` file rendering). Google Sheets native pieChart objects are fine and are now the canonical visual for the Live Week %-done display per Kay's 2026-05-12 preference.
- **Sage-green palette** from Instagram template Kay liked. Sage-light `#e8efd8`, sage-dark `#7a8c4d`, sage-extra-light `#f3f7e8`. Entity tints: G&B sage, Kai Grey warm-grey, Panthera Grey cool-grey, Myself Renewed blush, Home warm-tan. *Donut slice colors are theme-driven in the Sheets API — `pieChart` has no per-slice color field. Default palette applied at build; manual recolor available via Chart Editor in the Sheet UI if Kay wants sage on the slices.*
- **Manual-tick Gantt** (not auto-driven by Start/Target dates) — Kay wanted the tick-as-you-go feel.
- **Type tags Work/Home only**, not subdivided into entities. Entities expressed via Project column.
- **Strikethrough + sage-light fill** on done items everywhere via native conditional formatting rules tied to checkbox state.
- **Native Sheets checkboxes** (Data Validation, not Unicode glyphs) — properly clickable from any browser, mobile-friendly.
- **Promotion via skill, not drag.** Always use `task_tracker.py promote`. Source row gets a "→ promoted to {day} slot {N}" marker appended to Notes.
- **No file-lock check.** Drive handles concurrency natively; no `lsof` equivalent needed.

## Sunday rollover ceremony

Triggered by `goodnight` on Sunday evening. Calls `task_tracker.py archive`, which:
1. Finds the live week tab via metadata.
2. Duplicates it via `duplicateSheet` API to `archive_{old-label}` and parks at far-right of tab strip.
3. Renames the original to next week's label (Monday edge case handled).
4. Clears habit checkboxes, priority statuses, priority task text, notes.
5. Writes a trace; (optionally) posts a one-liner to Slack `#operations`.

## Open items

- **Stale-projects detection in `report` not yet wired** — placeholder in code, requires per-Gantt-tab week-cell scan with date heuristic. Defer to next iteration.
- **`reformat` is additive only** — duplicate CF rules can stack if run repeatedly. Manual cleanup in UI if they accumulate. Future enhancement: read existing rules + delete them first.
- **Legacy Excel `TO DO 4.26.26.xlsx`** still in Drive folder — Kay decides when to archive/rename. Don't touch.

## How to add a new Gantt project later

Use the skill verb directly:
```bash
python3 scripts/task_tracker.py projects-create-gantt \
  --project "New Project Name" \
  --entity "G&B" \
  --status "Plan Needed" \
  --start "2026-05-15" \
  --target "2026-08-15" \
  --weeks 14
```
This creates the Gantt tab and updates the Projects index with a HYPERLINK in one shot. No rebuild needed.

## Iterating on the file mid-week

Use the skill verbs — never edit the Sheet structure programmatically outside the verbs. If Kay edits the Sheet directly and breaks a CF rule, run `task_tracker.py reformat`.

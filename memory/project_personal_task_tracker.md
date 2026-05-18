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

## 2026-05-17 — single-To Do-backend consolidation + BOTH-surfaces model (CURRENT ARCHITECTURE)

**2026-05-17 consolidation (locked):** retired the multi-tab To Do backend down to ONE `To Do` tab. `To Do Long Term`, `Recurring Weekly To Dos`, `Completed To Do`, and `_donut_data` were renamed `_retired_{name}_2026-05-17` + hidden by the migration (final deletion is a later follow-up). No more checkbox-sweep, no `Completed To Do` tab, no donut charts / %-display. Migration: `scripts/migrate_todo_consolidation.py`.

The tracker has ONE `To Do` backend tab + **BOTH** working surfaces:

1. **`To Do` tab** — the single capture point. Columns: **A=Status, B=Task, C=Type, D=Project, E=Due, F=Notes, G=Horizon**.
   - **`Status`** = 3-state native dropdown: `Not Completed` / `On-going` / `Completed`. Replaces the old native checkbox + the archive-todo sweep. **"Done" = `Status == "Completed"`**; done-row CF fires on that value. Completed rows stay in place (no relocation).
   - **`Horizon`** = native dropdown: `Short Term`, `Long Term`, `Weekly Recurring Mon`..`Weekly Recurring Sat` (extensible later to Quarterly/Yearly). `Long Term`/someday items live here (no separate tab). A **recurring item** = `Horizon` starts with "Weekly Recurring" + `Status == "On-going"`; `build-week` reads these rows directly from `To Do` (NO separate Recurring tab).
   - **Cleanliness = saved filter/sort views in the Sheet UI** (e.g. filter `Status != Completed`, sort by `Due`), NOT row relocation.
2. **`Week` planning tab** — the Sunday canvas, ALL 7 days visible Sun→Sat, one block per day side by side. **Leftmost in the strip (index 0, before `Sun`).** This is where `build-week` rebuilds/clears + stamps the recurring `To Do` rows, and where Kay lays out / finalizes the whole week. **KEEPS native checkboxes** (Kay's working surface, unchanged).
3. **7 permanent day tabs** (`Sun Mon Tue Wed Thu Fri Sat`, immediately after `Week`) — the calm, large-font daily *execution* surface. Kay works these Mon–Sat. **NOT auto-populated** until `distribute-week` fans the finalized Week plan out into them. **KEEP native checkboxes** (unchanged) — only the `To Do` backend changed to the Status dropdown.

Rationale: the original single "Live Week" 7-day-pair grid (small text, 7 days competing) drove Kay's overwhelm. The first rebuild over-corrected by deleting the weekly surface entirely; corrected same day to BOTH surfaces. The 2026-05-17 consolidation then collapsed the 4 backend tabs into one Status/Horizon-driven `To Do` tab. Converged via `/socrates` (`brain/outputs/2026-05-17-discussion-daily-tab-tracker-rebuild.md`).

**Week-tab layout** (modelled on the verbatim `archive_May 11-17` grid copy but RE-ORDERED Sun→Sat; the archive grid was Mon-first): col 0 = habit/notes label; for day i (0=Sun..6=Sat) status checkbox col = `1+2*i`, content/task col = `2+2*i`. Row 1 merged A1:O1 title `WEEK OF May 17-23` (16pt bold, sage-light) · row 5 `HABIT TRACKER` · row 6 Sun..Sat 2-col-merged sub-headers · rows 7–15 nine habit rows (label col 0, native checkbox per day; "Meditation"/"Exercises" + "Class" separated 2026-05-18, "ACV drink" + "Probiotic protein shake" split 2026-05-17) · row 16 SUNDAY..SATURDAY 2-col-merged day headers (11pt bold, white/sage-dark, carry the date) · rows 24–38 fifteen priority slots/day (status checkbox col + task col, wrap, done-row CF) · row 40 notes sub-headers · rows 41–48 merged free-notes block/day. Native checkboxes, sage palette. **No donut** (donuts removed entirely 2026-05-17).

**Per-day-tab layout:** row 1 merged title `SUNDAY · May 17` (20pt bold, sage-dark) · row 3 `HABITS` · rows 4–12 nine habit rows (A=checkbox, B:E merged label 14pt) · row 13 column headers (✓|Task|Type|Project|Notes, 12pt) · rows 14–28 fifteen priority slots (A=native checkbox · B=Task **17pt** · C=Type dropdown · D=Project dropdown · E=Notes; ~34px) · row 30 `NOTES` · rows 31–38 free-notes block. **No donut** (removed 2026-05-17).

**Week boundary = Sunday** (`today - timedelta(days=(today.weekday()+1)%7)` → Sun..Sat).

**Sunday ceremony** (in `/goodmorning`, NOT `goodnight`): `report` (per-day carryover across 7 day tabs) → Kay walks each carryover → `sync-done-status` across 7 tabs (set matching `To Do` rows to `Status=Completed` in place — **no sweep, `archive-todo` RETIRED**) → **`build-week`** (snapshot Week tab + To Do → combined far-right `archive_{Sun-date}` tab values-only of the prior Week tab → clear all 7 day-blocks on the **Week tab** → re-title Week row 1 + per-day header dates → stamp recurring `To Do` rows **onto the Week tab**; day tabs untouched) → Kay finalizes the full week on the Week tab (approved items via `promote`/`schedule-to-day-slot`/`move-day-item` or direct entry) → **`distribute-week`** (fan finalized Week plan → 7 day tabs; collision-aware, snapshot+trace) → `reformat` if needed. Carryover is **manual only** — no auto-carry.

**Scripts:** Week-tab builder `scripts/build_week_tab.py` (one-shot; `--dry-run`, `--no-populate`). Day-tab builder `scripts/build_day_tabs.py` (idempotent; `--dry-run`; structure/formatting only, never clears content; no donut step). Consolidation migration `scripts/migrate_todo_consolidation.py`. Donut scripts removed.

**Verb changes:** `build-week` targets the **Week planning tab** (archive prior Week verbatim + clear all 7 day-blocks + re-title + stamp recurring `To Do` rows onto the Week tab; `--skip-recurring`, `--dry-run`). **`distribute-week`** (`--dry-run`, `--force`, `--day {X}`) fans the finalized Week plan into the 7 day tabs, collision-aware, snapshot+trace. `archive` → DEPRECATED alias of `build-week`. **`archive-todo` → RETIRED no-op** (no sweep, no `Completed To Do`; "done" = `Status=Completed` in place). `recurring-add` / `recurring-remove` now write/clear `To Do` rows (Horizon = `Weekly Recurring {day}`, Status `On-going`), NOT a separate tab. `append` gained optional `--horizon` (default `Short Term`). `move-day-item` / `promote` / `schedule-to-day-slot` / `sync-done-status` / `report` / `reformat` operate on the 7 single-column day tabs (slots rows 14–28, habits rows 4–12) and the `To Do` tab; `sync-done-status` now sets `Status=Completed` (was: checkbox TRUE).

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

## Architecture — 5 tabs  (⚠️ SUPERSEDED 2026-05-17 — see "single-To Do-backend consolidation + BOTH-surfaces model" above. The single Live Week tab, `To Do Long Term`, `Recurring Weekly To Dos`, `Completed To Do`, and `_donut_data` are ALL retired/hidden. Section kept for historical context only.)

1. **Live week tab** [RETIRED 2026-05-17] — habit tracker (7 habits, Mon-Sun grid) + day grid (Mon-Sun, **native donut chart per day** at rows 17-21 (pie + pieHole=0.5, driven by hidden helper tab `_donut_data`), **15 priority slots** per day, slim 8-row notes area). Each day spans 2 sub-columns: small status + wide task. Priority checkbox sits LEFT of task text in same row.
   - **Tab name = current Mon-Sun range** (e.g. `May 11-17`). Renamed each Sunday by `task_tracker.py archive`.
2. **To Do** — single capture point for all tasks. Columns: Status (checkbox) / Task / Type (dropdown: Work or Home) / Project (dropdown: G&B, Kai Grey, Panthera Grey, Myself Renewed, Home — free text allowed) / Due (date) / Notes. Header row frozen.
3. **To Do Long Term** — intents/someday items without hard timelines. Status dropdown options: Idea / Active / On hold / Promoted / Done. When ready to plan, promote to a Projects tab.
4. **Projects** — index of *active* time-bound projects with Project / Entity (dropdown) / Status (dropdown: Plan Needed / Active / On hold / Done) / Start / Target / Tab hyperlink / Notes. Currently holds: Myself Renewed Healthcare, Deal Aggregator Expansion.
5. **Myself Renewed Healthcare** — first Gantt-project tab. 10 milestones × 16 weekly columns. Each timeline cell is a native checkbox; ticking fills the cell blush-pink (entity color). Building a contiguous run of ticks visually creates a Gantt bar.

Plus: **Deal Aggregator Expansion** (Gantt, 12 weeks from 2026-05-11, G&B sage). **Completed To Do** (created by `archive-todo` on first run, sweeps completed To Do rows). **Recurring Weekly To Dos** (added 2026-05-15, sheetId `1997242109` — see dedicated section below). Archive tabs `archive_{Mmm D-D}` accumulate from each Sunday rollover, parked far-right.

## Build scripts (in this repo)

- `scripts/task_tracker.py` — skill helper. Subcommands: `append` (`--horizon`), `promote`, `build-week` (`--skip-recurring` / `--dry-run`), `distribute-week`, `archive` (DEPRECATED alias of `build-week`), `archive-todo` (RETIRED no-op), `sync-done-status`, `schedule-to-day-slot`, `move-day-item`, `recurring-add`, `recurring-remove`, `projects-create-gantt`, `reformat`, `report`, `gantt-tick`.
- `scripts/migrate_todo_consolidation.py` — one-shot 2026-05-17 migration (retire 4 backend tabs → single Status/Horizon `To Do`).
- **DEPRECATED:** `scripts/build_tasks_excel.py`, `scripts/populate_tasks_from_motion.py`, `scripts/maintain_tasks_excel.py` — Excel-era build path. Replaced by the one-shot `/tmp/tracker-migration/build_sheet.py` for any future rebuild. Kept in repo for reference; do not run.

## Skill verbs (`task-tracker-manager`)

| Verb | Trigger | Auto vs surface |
|---|---|---|
| `append` | "Add to To Do" / mid-day capture / goodmorning capture pass | Surface as `RECOMMEND: Add to To Do — "X" / Type / Project / Due / Horizon → YES/NO` for single items; surface for batch ≥3 |
| `promote` | "Move X to {day} slot {N}" | Always surface (affects day plan) |
| `schedule-to-day-slot` | "Schedule X for {day}" | Always surface |
| `build-week` | `goodmorning` Sunday | Auto (`archive` is a DEPRECATED alias) |
| `distribute-week` | After Kay finalizes the Week tab (Sunday) | Auto on confirmation; `--dry-run` first |
| `archive-todo` | RETIRED 2026-05-17 — no-op (no sweep; done = `Status=Completed` in place) | n/a |
| `sync-done-status` | "sync done items" / "reconcile weekly to To Do" / Sunday step | Auto (sets matching `To Do` rows to `Status=Completed`) |
| `move-day-item` | Sunday carryover walkthrough | Auto on Kay's approval of a specific move |
| `projects-create-gantt` | "Start a project for X" | Always surface |
| `reformat` | Detected broken CF | Auto |
| `report` | Friday briefing / on-demand | Auto |
| `gantt-tick` | "Healthcare milestone N done" / "tick week K" | Auto |
| `recurring-add` | "Make X a weekly recurring task on Monday" (writes a `To Do` row, Horizon=`Weekly Recurring {day}`) | Auto when intent unambiguous; surface when exploring |
| `recurring-remove` | "Drop the recurring X" / "remove row N" (clears the `To Do` row) | Auto when row content was just confirmed in conversation |

## Key design decisions

- **European calendar week** (Mon-Sun, not Sun-Sat).
- **Donut charts + %-display REMOVED entirely (2026-05-17 consolidation).** `_donut_data` retired/hidden, donut scripts removed. No progress visual on any surface — progress is read directly from `Status` on `To Do` / native checkboxes on the day & Week tabs. (Historical: 2026-05-12 to 2026-05-17 there were native pieChart donuts per day driven by `_donut_data`; superseded.)
- **Sage-green palette** from Instagram template Kay liked. Sage-light `#e8efd8`, sage-dark `#7a8c4d`, sage-extra-light `#f3f7e8`. Entity tints: G&B sage, Kai Grey warm-grey, Panthera Grey cool-grey, Myself Renewed blush, Home warm-tan. *Donut slice colors are theme-driven in the Sheets API — `pieChart` has no per-slice color field. Default palette applied at build; manual recolor available via Chart Editor in the Sheet UI if Kay wants sage on the slices.*
- **Manual-tick Gantt** (not auto-driven by Start/Target dates) — Kay wanted the tick-as-you-go feel.
- **Type tags Work/Home only**, not subdivided into entities. Entities expressed via Project column.
- **Strikethrough + sage-light fill** on done items: on the day & Week tabs via CF tied to native checkbox state; on the `To Do` tab via CF tied to `Status == "Completed"`.
- **Native Sheets checkboxes** (Data Validation, not Unicode glyphs) — properly clickable from any browser, mobile-friendly.
- **Promotion via skill, not drag.** Always use `task_tracker.py promote`. Source row gets a "→ promoted to {day} slot {N}" marker appended to Notes.
- **No file-lock check.** Drive handles concurrency natively; no `lsof` equivalent needed.

## Sunday rollover ceremony

**See the CURRENT ARCHITECTURE "Sunday ceremony" line above.** Triggered by `/goodmorning` on Sunday (NOT `goodnight`). End-to-end: `report` → Kay walks carryover (manual, no auto-carry) → `sync-done-status` across 7 day tabs (set matching `To Do` rows to `Status=Completed` in place) → `build-week` (snapshot Week tab + To Do → far-right `archive_{Sun-date}` of prior Week tab → clear all 7 Week-tab day-blocks → re-title → stamp recurring `To Do` rows onto the Week tab) → Kay finalizes the Week tab → `distribute-week` (fan → 7 day tabs) → `reformat` if needed → git commit.

**`archive-todo` is RETIRED** (no sweep, no `Completed To Do` tab — "done" = `Status=Completed` in place; cleanliness = saved filter/sort views). The Sunday-evening `goodnight` `archive` trigger is RETIRED; `archive` survives only as a DEPRECATED alias of `build-week`.

## Recurring items (live in `To Do`, no separate tab — supersedes the 2026-05-15 "Recurring Weekly To Dos tab")

**SUPERSEDED 2026-05-17.** The dedicated `Recurring Weekly To Dos` tab (built 2026-05-15, option (b)) was retired (renamed `_retired_Recurring Weekly To Dos_2026-05-17` + hidden) in the consolidation. Recurrence is now a property of a normal `To Do` row:

- A **recurring item** = a `To Do` row with `Horizon` = `Weekly Recurring {day}` (e.g. `Weekly Recurring Mon`) and `Status = On-going`.
- `build-week` reads these rows directly from `To Do` every Sunday and stamps each onto its day (collision-refuse: explicit slot pins, blank auto-picks, conflicts log+skip). `--skip-recurring` bypasses; `--dry-run` previews.
- Edit path: `recurring-add --day Mon --task "..." --type Work --project "G&B" [--slot N] [--notes "..."]` (writes a `To Do` row, Status `On-going`, Horizon `Weekly Recurring Mon`) / `recurring-remove --row N` (clears the `To Do` row; refuses non-recurring rows). Or set the `Horizon` dropdown directly on any `To Do` row in the Sheet UI. Both verbs snapshot + trace (decision-content — compounds on every future Sunday).
- Known weekly recurring G&B items: Mon — Process payroll, Mon — Process conference registrations, Wed — Niche intel review, Fri — Weekly review (system health + M&A + budget).

## Open items

- **Stale-projects detection in `report` not yet wired** — placeholder in code, requires per-Gantt-tab week-cell scan with date heuristic. Defer to next iteration.
- **`reformat` is additive only** — duplicate CF rules can stack if run repeatedly. Manual cleanup in UI if they accumulate. Future enhancement: read existing rules + delete them first.
- **Legacy Excel `TO DO 4.26.26.xlsx`** still in Drive folder — Kay decides when to archive/rename. Don't touch.
- ~~**Weekly recurring items not codified**~~ — RESOLVED. Now `To Do` rows with `Horizon = Weekly Recurring {day}` + `Status = On-going`, read by `build-week`. (2026-05-15 separate-tab approach superseded by the 2026-05-17 consolidation — see "Recurring items" section above.)
- **Retired-tab final deletion** — `_retired_{To Do Long Term, Recurring Weekly To Dos, Completed To Do, _donut_data}_2026-05-17` tabs are hidden, not deleted. Deletion is a later follow-up once the new model is verified stable.

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

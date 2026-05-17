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

## 2026-05-17 — BOTH-surfaces model (CURRENT ARCHITECTURE — design-corrected)

The tracker has **BOTH surfaces**:

1. **`Week` planning tab** — the Sunday canvas, ALL 7 days visible Sun→Sat, one block per day side by side. **Leftmost in the strip (index 0, before `Sun`).** This is where `build-week` rebuilds/clears + stamps the Recurring Template, and where Kay lays out / finalizes the whole week.
2. **7 permanent day tabs** (`Sun Mon Tue Wed Thu Fri Sat`, immediately after `Week`) — the calm, large-font daily *execution* surface. Kay works these Mon–Sat. They are **NOT auto-populated** until `distribute-week` fans the finalized Week plan out into them.

Rationale: the original single "Live Week" 7-day-pair grid (small text, 7 days competing) drove Kay's overwhelm. The first rebuild over-corrected by deleting the weekly surface entirely (day-tabs-only), which removed her planning canvas. The corrected binding model keeps both: plan on the Week tab, execute on the day tabs. Converged via `/socrates` (`brain/outputs/2026-05-17-discussion-daily-tab-tracker-rebuild.md`); plan `synthetic-bubbling-snowglobe` (see its ⚠️ DESIGN CORRECTION block).

**Week-tab layout** (modelled on the verbatim `archive_May 11-17` grid copy but RE-ORDERED Sun→Sat; the archive grid was Mon-first): col 0 = habit/notes label; for day i (0=Sun..6=Sat) status checkbox col = `1+2*i`, content/task col = `2+2*i`. Row 1 merged A1:O1 title `WEEK OF May 17-23` (16pt bold, sage-light) · row 5 `HABIT TRACKER` · row 6 Sun..Sat 2-col-merged sub-headers · rows 7–14 eight habit rows (label col 0, native checkbox per day; "ACV drink" + "Probiotic protein shake" split from one combined row 2026-05-17) · row 15 SUNDAY..SATURDAY 2-col-merged day headers (11pt bold, white/sage-dark, carry the date) · rows 23–37 fifteen priority slots/day (status checkbox col + task col, wrap, done-row CF) · row 39 notes sub-headers · rows 40–47 merged free-notes block/day. Native checkboxes, sage palette. **No per-day donut on the Week tab** (it is a planning canvas — kept simple; the 7 day tabs retain their donut charts).

**Per-day-tab layout** (unchanged): row 1 merged title `SUNDAY · May 17` (20pt bold, sage-dark) · row 3 `HABITS` · rows 4–11 eight habit rows (A=checkbox, B:E merged label 14pt; spacer row consumed by the 2026-05-17 ACV/probiotic split — slots/donut row positions unchanged) · row 12 column headers (✓|Task|Type|Project|Notes, 12pt) · rows 13–27 fifteen priority slots (A=native checkbox · B=Task **17pt** · C=Type dropdown · D=Project dropdown · E=Notes; ~34px) · row 29 `NOTES` · rows 30–37 free-notes block · one per-day donut (pieHole=0.5, ~160px) anchored col G row 1.

**Week boundary = Sunday** (`today - timedelta(days=(today.weekday()+1)%7)` → Sun..Sat).

**Sunday ceremony** (in `/goodmorning`, NOT `goodnight`): `report` (per-day carryover across 7 day tabs) → Kay walks each carryover → `archive-todo` (auto `sync-done-status` across 7 tabs) → **`build-week`** (snapshot Week tab + `_donut_data` + To Do → combined far-right `archive_{Sun-date}` tab values-only of the prior Week tab → clear all 7 day-blocks on the **Week tab** → re-title Week row 1 + per-day header dates → stamp Recurring Template **onto the Week tab**; day tabs untouched) → Kay finalizes the full week on the Week tab (approved items via `promote`/`schedule-to-day-slot`/`move-day-item` or direct entry) → **`distribute-week`** (fan finalized Week plan → 7 day tabs; collision-aware, snapshot+trace) → `reformat` if needed. Carryover is **manual only** — no auto-carry.

**Scripts:** Week-tab builder `scripts/build_week_tab.py` (one-shot; `--dry-run`, `--no-populate`; creates the leftmost Week tab + reverse-populates from the day tabs). Day-tab builder `scripts/build_day_tabs.py` (idempotent; `--dry-run`, `--donuts-only`; only (re)writes structure/formatting, never clears content). One-shot cutover verb `task_tracker.py migrate` (dry-run default; never runs destructive teardown — human-supervised). `build_donut_charts.py` (single-grid) superseded. `_donut_data`: 7 rows, `=COUNTIF('Sun'!A13:A27,TRUE)` / `=COUNTA('Sun'!B13:B27)-COUNTIF(...)`.

**Verb changes:** `build-week` now targets the **Week planning tab** (archive prior Week verbatim + clear all 7 day-blocks + re-title + stamp Recurring onto the Week tab; `--skip-recurring`, `--dry-run`). New verb **`distribute-week`** (`--dry-run`, `--force`, `--day {X}`) fans the finalized Week plan into the 7 day tabs, collision-aware (refuses to overwrite a day-tab slot the Week plan changes unless `--force`), snapshot+trace. `archive` → DEPRECATED alias of `build-week` (delegates + stderr notice). `move-day-item` (`--state completed|incomplete|added|deleted`) + `promote`/`schedule-to-day-slot`/`sync-done-status`/`report`/`reformat` still operate on the 7 single-column day tabs (slots rows 13–27, habits rows 4–11, status col A, task col B) and are unchanged.

**2026-05-17 design correction (post-implementation):** the first day-tab rebuild WRONGLY deleted the weekly surface. Corrected same day to BOTH surfaces. The `Week` tab was created leftmost (sheetId 1062871087) and reverse-populated from the then-current 7 day tabs (13 slots) so Kay had the week at a glance immediately. `cmd_build_week` reworked Week-targeting; `cmd_distribute_week` added; SKILL.md / this memory / `goodmorning.md` Sunday block updated.

**Migration cutover (Sun 2026-05-17, human-supervised):** snapshot all tabs → legacy `sync-done-status` against OLD `May 11-17` grid → `archive-todo` → `build_day_tabs.py` → duplicate `May 11-17` → `archive_May 11-17` far-right → delete/hide retired `Today` (sheetId 433823170) + old grid AFTER archive exists → `report` → Kay walks carryover. The old single-grid `LIVE_*` constants + `find_live_week_tab()`/`current_week_label()` are retained ONLY for the migration's pre-teardown read; remove post-cutover.

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

## Architecture — 5 tabs  (⚠️ SUPERSEDED 2026-05-17 — see "Day-tab rebuild" above; the single Live Week tab no longer exists. Section kept for historical context only.)

1. **Live week tab** [RETIRED 2026-05-17] — habit tracker (7 habits, Mon-Sun grid) + day grid (Mon-Sun, **native donut chart per day** at rows 17-21 (pie + pieHole=0.5, driven by hidden helper tab `_donut_data`), **15 priority slots** per day, slim 8-row notes area). Each day spans 2 sub-columns: small status + wide task. Priority checkbox sits LEFT of task text in same row.
   - **Tab name = current Mon-Sun range** (e.g. `May 11-17`). Renamed each Sunday by `task_tracker.py archive`.
2. **To Do** — single capture point for all tasks. Columns: Status (checkbox) / Task / Type (dropdown: Work or Home) / Project (dropdown: G&B, Kai Grey, Panthera Grey, Myself Renewed, Home — free text allowed) / Due (date) / Notes. Header row frozen.
3. **To Do Long Term** — intents/someday items without hard timelines. Status dropdown options: Idea / Active / On hold / Promoted / Done. When ready to plan, promote to a Projects tab.
4. **Projects** — index of *active* time-bound projects with Project / Entity (dropdown) / Status (dropdown: Plan Needed / Active / On hold / Done) / Start / Target / Tab hyperlink / Notes. Currently holds: Myself Renewed Healthcare, Deal Aggregator Expansion.
5. **Myself Renewed Healthcare** — first Gantt-project tab. 10 milestones × 16 weekly columns. Each timeline cell is a native checkbox; ticking fills the cell blush-pink (entity color). Building a contiguous run of ticks visually creates a Gantt bar.

Plus: **Deal Aggregator Expansion** (Gantt, 12 weeks from 2026-05-11, G&B sage). **Completed To Do** (created by `archive-todo` on first run, sweeps completed To Do rows). **Recurring Template** (added 2026-05-15, sheetId `1997242109` — see dedicated section below). Archive tabs `archive_{Mmm D-D}` accumulate from each Sunday rollover, parked far-right.

## Build scripts (in this repo)

- `scripts/task_tracker.py` — skill helper. Subcommands: `append`, `promote`, `archive` (`--skip-recurring` / `--dry-run`), `archive-todo`, `sync-done-status`, `schedule-to-day-slot`, `recurring-add`, `recurring-remove`, `projects-create-gantt`, `reformat`, `report`, `gantt-tick`.
- **DEPRECATED:** `scripts/build_tasks_excel.py`, `scripts/populate_tasks_from_motion.py`, `scripts/maintain_tasks_excel.py` — Excel-era build path. Replaced by the one-shot `/tmp/tracker-migration/build_sheet.py` for any future rebuild. Kept in repo for reference; do not run.

## Skill verbs (`task-tracker-manager`)

| Verb | Trigger | Auto vs surface |
|---|---|---|
| `append` | "Add to To Do" / mid-day capture / goodmorning capture pass | Surface as `RECOMMEND: Add to To Do — "X" / Type / Project / Due → YES/NO` for single items; surface for batch ≥3 |
| `promote` | "Move X to {day} slot {N}" | Always surface (affects day plan) |
| `schedule-to-day-slot` | "Schedule X for {day}" | Always surface |
| `archive` | `goodnight` Sunday | Auto |
| `archive-todo` | `goodnight` Sunday (also safe on any day) | Auto. Auto-calls `sync-done-status` as pre-step (skip with `--skip-sync`). |
| `sync-done-status` | "sync done items" / "reconcile weekly to To Do" / auto pre-step inside `archive-todo` | Auto |
| `projects-create-gantt` | "Start a project for X" | Always surface |
| `reformat` | Detected broken CF | Auto |
| `report` | Friday briefing / on-demand | Auto |
| `gantt-tick` | "Healthcare milestone N done" / "tick week K" | Auto |
| `recurring-add` | "Make X a weekly recurring task on Monday" | Auto when intent unambiguous; surface when exploring |
| `recurring-remove` | "Drop the recurring X" / "remove row N from the recurring template" | Auto when row content was just confirmed in conversation |

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

End-to-end weekly flow:
`report` (Sunday morning) → walk-through with Kay → `promote` decisions → ... week's work ... → `archive-todo` (Sunday evening, auto-calls `sync-done-status` first to flip matching To Do rows for any checked priority slots) → Completed To Do tab populated → `archive` (renames live tab to next week, clears slots) → git commit.

Triggered by `goodnight` on Sunday evening. The `archive-todo` call MUST precede `archive` — the sync pre-step inside `archive-todo` needs the still-live week tab to reconcile slots against. The `archive` verb then:
1. Finds the live week tab via metadata.
2. Duplicates it via `duplicateSheet` API to `archive_{old-label}` and parks at far-right of tab strip.
3. Renames the original to next week's label (Monday edge case handled).
4. Clears habit checkboxes, priority statuses, priority task text, notes.
5. **Stamps the Recurring Template tab onto the new week's day-slots** (added 2026-05-15). Reads every row of `Recurring Template`, calls `_stamp_recurring_template(client, meta, new_label)` which mirrors `schedule-to-day-slot` semantics with `force=False`. Explicit-slot rows pin; blank-slot rows auto-pick. Slot conflicts log + skip (Kay resolves manually). Bypass with `--skip-recurring`. Preview the whole ceremony (no writes) with `--dry-run`.
6. Writes a trace (including recurring-stamp summary); (optionally) posts a one-liner to Slack `#operations`.

## Recurring Template tab (built 2026-05-15 — option (b))

The tracker has no native recurrence primitive in Google Sheets, so recurrence is layered in via a dedicated tab + an extension to the Sunday `archive` ceremony. Option (b) chosen over (a) hardcoding and (c) per-row flagging — keeps recurrence config out of code and lets Kay edit through the Sheet UI like any other tab.

**Tab:** `Recurring Template` (sheetId `1997242109`), positioned at index 3 (after `To Do Long Term`, before `Projects` and archives).

**Schema:**

| Col | Header | Type | Notes |
|---|---|---|---|
| A | Day | Native dropdown Mon..Sun | Required |
| B | Slot | Numeric 1..15 OR blank | Blank = auto-pick first empty slot at stamp time |
| C | Task | Free text | Required |
| D | Type | Native dropdown Work/Home | Required |
| E | Project | Free text | Optional (G&B, Kai Grey, Panthera Grey, Myself Renewed, Home, or anything) |
| F | Notes | Free text | Optional |

Header row formatted sage-dark + white bold. Day, Slot, Type columns have data validation rules; column widths tuned for readability.

**Seed rows (locked 2026-05-15 from Kay's 4 known weekly recurring items):**

| Day | Task | Type | Project |
|---|---|---|---|
| Mon | Process payroll | Work | G&B |
| Mon | Process conference registrations | Work | G&B |
| Wed | Niche intel review | Work | G&B |
| Fri | Weekly review — system health, M&A activities, budget | Work | G&B |

**Editing the template:**
- **Kay direct:** edit cells in the Sheet UI — add rows, change day, edit task text.
- **Claude via skill:**
  - `python3 scripts/task_tracker.py recurring-add --day Mon --task "..." --type Work --project "G&B" [--slot N] [--notes "..."]`
  - `python3 scripts/task_tracker.py recurring-remove --row N`
  - Both verbs snapshot + trace (decision-content — each edit compounds on every future Sunday rollover).

**Sunday rollover integration:** `cmd_archive` in `scripts/task_tracker.py` was extended to read this tab after clearing the new week's slots. For each row, the helper `_stamp_recurring_template` calls the same `schedule-to-day-slot` semantics (`force=False`) — explicit-slot rows pin to that slot, blank-slot rows auto-pick the first empty slot for their day. Slot conflicts (already-populated slot) log a warning to stderr and skip; Kay resolves manually. In-memory grid is tracked so back-to-back template rows for the same day auto-pick distinct slots.

**Escape hatches:**
- `python3 scripts/task_tracker.py archive --skip-recurring` — bypass the stamp step entirely (rare).
- `python3 scripts/task_tracker.py archive --dry-run` — preview the full ceremony (rename + clear + stamp) without any writes. Reports each row that would land on which day/slot. Useful pre-Sunday sanity check.

**Recurring rows for the CURRENT week (May 11-17, before this build):** still placed as one-off To Do rows 75/76/77 + a Fri slot scheduled today. Those handle this cycle; the recurring tab takes over starting May 18-24.

## Open items

- **Stale-projects detection in `report` not yet wired** — placeholder in code, requires per-Gantt-tab week-cell scan with date heuristic. Defer to next iteration.
- **`reformat` is additive only** — duplicate CF rules can stack if run repeatedly. Manual cleanup in UI if they accumulate. Future enhancement: read existing rules + delete them first.
- **Legacy Excel `TO DO 4.26.26.xlsx`** still in Drive folder — Kay decides when to archive/rename. Don't touch.
- ~~**Weekly recurring items not codified**~~ — RESOLVED 2026-05-15 by Recurring Template tab + `archive` extension (option b). See "Recurring Template tab" section above.

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

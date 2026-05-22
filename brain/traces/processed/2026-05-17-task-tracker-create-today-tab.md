---
schema_version: 1.2.0
name: task-tracker create-today-tab
date: 2026-05-17
review_status: applied
type: trace
tags:
  - date/2026-05-17
  - trace
  - skill/task-tracker-manager
  - verb/create-today-tab
  - topic/task-tracker
---
# task-tracker create-today-tab

New structural tab on the `TO DO 5.12.26` Google Sheet (architecture: `memory/project_personal_task_tracker.md`, owner skill [[traces/2026-05-15-task-tracker-recurring-remove-row6|task-tracker-manager]]). Kay-sanctioned build (design confirmed: auto-mirror the Live Week current-day block, ~1.5× font).

## Decision

Build a `Today` tab as a **read-only single-day mirror** of whichever Live Week day-block matches the current weekday, so the day's plan opens first without Kay scrolling the 7-day grid. One source of truth stays Live Week; Today never stores data.

## What was built

- **Tab:** `Today`, sheetId `433823170`, positioned at **index 0** (leftmost — opens before `May 11-17`). Sage-dark tab color, gridlines off.
- **Layout (cols A–F):** A1 title `TODAY` (merged A1:F1, 26pt). A2 subtitle `=CONCATENATE("Mirrors Live Week  ·  ",TEXT(TODAY(),"dddd, mmmm d"))`. Row 4 `HABIT TRACKER` band. Rows 5–11 the 7 habits (label literal in A, mirrored boolean in B). Row 13 `TODAY'S PRIORITIES` band. Row 14 column headers (Done / Task / Type / Project / Notes). Rows 15–29 the 15 priority slots. Row 31 `COMPLETION` band + donut chart.
- **Hidden helper col H:** `H1 =TEXT(TODAY(),"ddd")` (weekday). `H2` = status column index in Live Week `A:O`, `H3` = task column index, both `=CHOOSE(MATCH($H$1,{"Mon";...;"Sun"},0), …)` mapping Mon→B/C(2/3) … Sun→N/O(14/15). Column H hidden.
- **Auto-mirror formulas:** every habit and priority cell is `=INDEX('May 11-17'!$A:$O, <LiveWeekRow>, $H$2 or $H$3)`. Habits pull Live Week rows 7–13; priorities pull rows 23–37. Column resolves daily from `$H$1`, so the tab tracks the current day with zero maintenance.
- **Native checkboxes:** BOOLEAN data-validation on the mirrored status cells (B5:B11 habits, A15:A29 priorities) so TRUE/FALSE renders as a real Sheets checkbox, not a glyph (guardrail #6).
- **Donut chart:** added a dynamic block at `_donut_data!A10:C10` (`=TEXT(TODAY(),"ddd")` + two `VLOOKUP`s into the existing per-day Done/Left rows A2:C8). New pieChart (pieHole 0.55, chartId `2021912981`) anchored on Today at row 32, col B, sourcing that dynamic row — re-renders for whatever day it is.
- **Font:** Live Week body 10pt → Today body **15pt** (1.5×). Title 16→26pt, section bands 10→15pt bold, column headers 13pt bold. Row heights / column widths widened to suit.

## Auto-mirror approach

Weekday string from `TEXT(TODAY(),"ddd")` → `CHOOSE/MATCH` to a Live Week column index → `INDEX` into Live Week's fixed row ranges. No script re-run needed day to day; Google recalculates `TODAY()` automatically.

## Limitation (documented)

**Today is a one-way, read-only mirror — not a two-way checkbox sync.** The status cells hold `=INDEX(...)` formulas; a real two-way checkbox would require the cell to be writable, which would destroy the formula on first click. Kay must toggle done-status on the **Live Week tab** (the single source of truth). Today reflects that state on next recalculation. The checkbox UI on Today is display-only — clicking it there would overwrite the mirror formula for that cell (a manual error, recoverable by re-running this build / restoring the formula). The `Type / Project / Notes` columns are placeholders: Live Week day-blocks carry only Status + Task, so those columns are intentionally blank on Today.

## Verification (2026-05-17, Sunday)

- Tab order: `Today` idx 0, `May 11-17` idx 1 ✓
- `H1` resolved `Sun`; `H2`=14, `H3`=15 (Sun = Live Week cols N/O) ✓
- A2 → "Mirrors Live Week  ·  Sunday, May 17"; priorities B15–B18 = Sunday's 4 tasks, matching Live Week O23–O26 ✓
- `_donut_data!A10:C10` → `['Sun', 0, 4]` ✓
- No `#REF`/`#ERROR` cells ✓
- Native BOOLEAN validation on B5 + A15 confirmed ✓
- Fonts: title 26pt, body 15pt (=1.5× LW 10pt) ✓
- Chart 2021912981 anchored on Today sheet ✓

## Paths

- Snapshot (pre-build sheet list + `_donut_data` + Live Week values): `/home/ubuntu/projects/Sapling/brain/context/rollback-snapshots/tasks-create-today-tab-20260517-085151.json`
- Rollback: delete sheetId `433823170` + chart `2021912981`, clear `_donut_data!A10:C10`. No prior data was overwritten (new tab; `_donut_data` row 10 was empty).

## Follow-up for skill memory

Architecture change — `memory/project_personal_task_tracker.md` should gain a "Today tab" note: the Sunday `archive` ceremony renames the Live Week tab but the Today tab references it by the literal name `'May 11-17'`. **When `archive` renames the live tab, the Today formulas will break (stale tab name) unless `archive` is extended to rewrite Today's `INDEX` references to the new week label.** Flagged as an open item; not in scope for this build.

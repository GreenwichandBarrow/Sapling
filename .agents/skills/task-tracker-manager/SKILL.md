---
name: task-tracker-manager
description: Owns Kay's personal task tracker — weekly Google Sheets files with the current week in `STRATEGIC PLANNING` and prior weeks in the `To Do Archive` Drive folder (current week resolved via `scripts/tracker_sheet_resolver.py`; e.g., `TO DO 5.31.26`). Single capture point + Week planning tab + 7 permanent day tabs (Sun..Sat) + Gantt project tabs. Append items, promote items into a day tab's priority slots, run the Sunday build-week rebuild ceremony (creates next week's file, pulls carryover cross-file), move/carry items between day tabs, re-apply conditional formatting, surface a To Do health report. Reports to Chief of Staff. NOT operational sheets — that's tracker-manager.
archetype: router
context_budget:
  skill_md: 200
  max_references: 12
  learnings_md: 40
  sub_agent_limit: 500
---

# Task Tracker Manager

Standing owner of Kay's personal task system. The tracker lives as weekly Google Sheets files with the current week in `STRATEGIC PLANNING` and prior weeks in the `To Do Archive` Drive folder. Each Sunday's `build-week` Drive-copies the prior week's file into a new `TO DO M.D.YY` file in `STRATEGIC PLANNING` (e.g., `TO DO 5.31.26`), then moves the prior file into `To Do Archive` as immutable history. The **current week's sheet ID is resolved dynamically** via `scripts/tracker_sheet_resolver.py` (hybrid pointer + Drive-search fallback; canonical pointer at `~/.config/sapling/current-tracker-sheet.json`; legacy `~/.claude/config/current-tracker-sheet.json` is read fallback only). Use `python3 scripts/tracker_sheet_resolver.py --print-id` to print the current ID for shell consumers; the resolver auto-rebuilds the pointer if missing/stale. Built 2026-04-26 on Excel; migrated to Google Sheets 2026-05-12; weekly-files architecture shipped 2026-05-26. This skill is the operational layer — Chief of Staff calls into it, this skill executes.

**Credential prerequisite:** before any manual `gog` / Google-backed task-tracker command, use the 1Password-backed helper:

```bash
source /home/ubuntu/projects/Sapling/scripts/op-env.sh
```

`scripts/task_tracker.py` and `scripts/tracker_sheet_resolver.py` also source this helper for their internal `gog` subprocesses. If Google access appears missing, check this path before diagnosing OAuth, rotating credentials, or reporting an outage.

Architecture lives in `memory/project_personal_task_tracker.md`. Update that memory whenever the architecture changes.

**Sheet ID env override:** Scripts read `TRACKER_SHEET_ID` from env if set, otherwise default to the constant above. Future rebuilds: update the constant + set `TRACKER_SHEET_ID` to the new id.

**Architecture (2026-05-17 — single-To Do-backend + BOTH-surfaces model):** The tracker has ONE `To Do` backend tab plus a `Week` planning tab AND 7 day tabs. The retired tabs (`To Do Long Term`, `Recurring Weekly To Dos`, `Completed To Do`, `_donut_data`) were renamed `_retired_{name}_2026-05-17` + hidden by the migration (final deletion is a later follow-up).
- **`To Do` tab** — the single capture point for all tasks. Columns: **A=Status, B=Task, C=Type, D=Project, E=Due, F=Notes, G=Horizon**.
  - **`Status`** = 3-state native dropdown: `Not Completed` / `On-going` / `Completed`. Replaces the old native checkbox + the archive-todo sweep. **"Done" = `Status == "Completed"`.** Done-row conditional formatting fires on `Status == "Completed"`.
  - **`Horizon`** = native dropdown: `Short Term`, `Long Term`, `Weekly Recurring Mon`..`Weekly Recurring Sat` (extensible later to Quarterly/Yearly). A **recurring item** = `Horizon` starts with "Weekly Recurring" + `Status == "On-going"`; `build-week` reads these rows directly from `To Do` (NOT a separate tab) and stamps each onto its day. `Long Term`/someday items now live here with `Horizon=Long Term` (no separate tab).
  - Day tabs and the Week tab **KEEP native checkboxes** (Kay's working surfaces, unchanged) — only the `To Do` backend changed to the Status dropdown.
- **`Week` tab** — the Sunday planning canvas, ALL 7 days visible Sun→Sat, one block per day side by side, **leftmost in the strip (index 0, before `Sun`)**. `build-week` rebuilds/clears it + stamps the recurring `To Do` rows onto it; Kay lays out / finalizes the whole week here. Layout: col 0 = habit/notes label; for day i (0=Sun..6=Sat) status checkbox col `1+2*i`, task col `2+2*i`. Row 1 merged title `WEEK OF May 17-23`, row 5 `HABIT TRACKER`, row 6 Sun..Sat sub-headers, rows 7–15 nine habit rows, row 16 SUNDAY..SATURDAY day headers (carry dates), rows 24–48 twenty-five priority slots/day, with each day block's first three slots shaded sage, rows 51–58 notes block. Builder: `scripts/build_week_tab.py` (one-shot; `--dry-run`, `--no-populate`).
- **7 day tabs** (`Sun Mon Tue Wed Thu Fri Sat`, immediately after `Week`) — the calm, large-font daily *execution* surface. Kay works these Mon–Sat. **NOT auto-populated until `distribute-week` fans the finalized Week plan out into them.** Per-day layout: row 1 merged title `SUNDAY · May 17` (20pt), rows 5–13 habit tracker (9 habits, A=checkbox), row 15 column headers, rows 16–40 twenty-five priority slots (A=native checkbox · B=Task 17pt · C=Type dropdown · D=Project dropdown · E=Notes), with rows 16–18 shaded sage as the top-three priority band, rows 43–50 free-notes block. Builder: `scripts/build_day_tabs.py` (idempotent; `--dry-run`).

**Sunday flow (weekly-files architecture, shipped 2026-05-26):**

Single autonomous command via `/goodmorning` Sunday step:
```bash
python3 /home/ubuntu/projects/Sapling/scripts/task_tracker.py build-week
```

Before a live build, `build-week` trusts the canonical pointer by default and checks for an existing `TO DO {Sunday}.YY` file. If one already exists, routine runs refuse to create a duplicate. Use `--refresh-pointer` only for recovery and `--force-new-file` only for explicit sandbox/testing copies.

`cmd_build_week` dispatches to `cmd_build_week_v2` which executes end-to-end:
1. Resolve PRIOR file via `tracker_sheet_resolver.py` (pointer fast-path, Drive-search fallback)
2. Snapshot prior file (Week + 7 day tabs + To Do) to rollback JSON
3. `gog drive copy` prior → NEW file `TO DO {next-Sun-date}.YY` in `STRATEGIC PLANNING`; after the new file is built successfully, move the PRIOR file to `To Do Archive`
4. Clear all 7 day tabs on new file (structure/CF/dropdowns/checkbox-validation preserved)
5. Stamp recurring `To Do` rows (Horizon `Weekly Recurring {day}`) onto new file's day tabs
6. Cross-file carryover: read PRIOR day-tab incompletes → write to NEW day-tab next-empty-slot (dedup vs recurring)
7. Wire Week tab cells as in-file formulas (`=Tue!B14` etc.) — live read-only mirror of day tabs
8. Re-title Week tab + per-day header dates + each day tab's `A1`
9. Update pointer atomically (LAST step — mid-rollover failures leave prior file canonical)
10. Trace

**After build-week completes:** Kay reviews the new file's Week tab (auto-mirror of day tabs via formulas), adjusts items DIRECTLY on day tabs. Week tab auto-updates. No `distribute-week` step needed.

**Alignment doctrine:** Week tab cells are FORMULAS pointing at same-file day tabs. Day tabs = the SINGLE edit surface. Week tab = live read-only view. No drift possible — they're the same data through formula refs.

**Carryover doctrine (weekly-files):** carryover is AUTO-PULLED CROSS-FILE from prior file's day tabs into the new file's day tabs during `build-week` step 6. Read happens BEFORE the new file's day tabs are touched in any other way (only recurring stamps land first, and dedup catches collisions). Prior file is immutable history once rollover completes.

**Order-of-operations (critical):**
```
cmd_build_week_v2:
  1. resolve prior → snapshot → drive copy new file into STRATEGIC PLANNING → build new file → archive prior file
  2. clear new file day tabs → stamp recurring → cross-file carryover from prior
  3. wire formulas → retitle → update pointer atomically (LAST)
```
Steps are atomic within a single `build-week` invocation. No separate human gate between sub-steps. The new file is the live working surface; the prior file is frozen history.

**Legacy mode:** `--legacy` flag invokes the pre-2026-05-26 in-place rebuild (archive tab inside same sheet, no new file, requires separate `distribute-week` for day-tab fan-out). Kept callable per `feedback_explicit_review_before_retiring_verbs` — recovery only.

**Forbidden pattern (clarified 2026-05-26 after Kay's correction):** do NOT mirror mid-week day-tab edits back to the Week tab via writes. Under the formula architecture this isn't possible (cells are formulas) but the rule remains for legacy mode + any future arch changes. The "rebuild Week tab from current day tabs" anti-pattern is forbidden.

**Cleanliness model:** No row relocation, no checkbox-sweep, no donut/%-display. `To Do` cleanliness is achieved via **saved filter/sort views in the Sheet UI** (e.g. filter `Status != Completed`, sort by `Due`), NOT by moving completed rows to another tab. Completed rows stay in place with `Status=Completed` and render via done-row CF. **Distinction:** *completed* rows are never relocated (filter views handle them); *empty/gap* rows ARE physically removed — see compaction doctrine below.

**Empty-row compaction doctrine (codified 2026-05-31 per Kay):** the `To Do` backend tab accumulates GAP rows — leftover `FALSE` checkbox cells from the pre-2026-05-17 checkbox architecture, blank rows, stray empty-checkbox rows. Two mechanisms feed the pile: `append` only ever fills the first empty row (it never removes), and `build-week`'s Drive-copy carries the whole cluttered tab forward every Sunday. Left alone it bloats to hundreds of rows (observed 2026-05-31: 412 rows, only 125 real, 286 gaps). The **`compact-todo`** verb strips every gap row, packs the real rows contiguously from row 2, physically deletes the surplus rows (retaining a ~40-row validated append buffer), and re-applies Status/Type/Project/Horizon dropdown validation (the relative done-row CF survives untouched). It runs automatically inside `build-week` (step 4b, on the freshly-copied new file, before the recurring stamp) so every week starts clean, and is callable on demand. This is NOT completed-row relocation — gap rows hold no data and are pure clutter.

**Pack-to-top doctrine (codified 2026-05-26):** every verb that writes to day-tab or Week-tab priority slots MUST keep items packed at the TOP of the 25-slot range. No leading empty rows, no gaps between items. The 25 slots are a CAPACITY CEILING, not a fixed seating chart. `promote`, `schedule-to-day-slot`, `move-day-item`, `distribute-week`, `sync-done-status`, recurring-stamp, carryover-pull — all use next-empty-slot logic. `--slot N` override allowed but warns if it leaves earlier slots empty. See `memory/feedback_task_tracker_pack_to_top.md`.

**Recurring items (live in `To Do`, no separate tab):** A recurring item is a normal `To Do` row with `Horizon` = `Weekly Recurring {day}` (e.g. `Weekly Recurring Mon`) and `Status = On-going`. The Sunday `build-week` ceremony reads these rows directly from `To Do` and stamps each onto its day's slots after the day-blocks are cleared. Occupied-slot conflicts log + skip (Kay resolves manually). Primary edit path is the `recurring-add` / `recurring-remove` verbs (which write/clear `To Do` rows with the right Horizon); Kay can also set the `Horizon` dropdown directly on any `To Do` row. Known weekly recurring G&B items: Mon — Process payroll, Mon — Process conference registrations, Wed — Niche intel review, Fri — Weekly review (system health + M&A + budget).

## When to invoke

- Kay says "add to To Do" / "put X on the list" / "save this for later" → **append**
- Kay says "move {todo-row} to {day} slot {N}" (To Do → week tab) → **promote**
- Kay says "schedule X for Wed" / "X goes on Friday" / direct day-slot drop with no To Do source row → **schedule-to-day-slot**
- Kay says "sync done items" / "reconcile weekly to To Do" / "the weekly slots aren't matching To Do" → **sync-done-status**
- Sunday morning as part of `goodmorning` → **build-week** (weekly rebuild ceremony — targets the **Week planning tab**: writes a combined far-right `archive_{Sun-date}` tab of the prior Week tab, clears all 7 day-blocks on the Week tab + re-titles it, stamps the recurring `To Do` rows **onto the Week tab**; day tabs untouched; `--skip-recurring` to bypass; `--dry-run` to preview). `archive` is a DEPRECATED alias that delegates here.
- After Kay finalizes the week on the Week tab (Sunday) → **distribute-week** (fans the finalized Week plan OUT into the 7 day tabs; collision-aware, `--dry-run` / `--force` / `--day {X}`)
- Kay says "move {day} slot N to {day}" / approves a carryover during the Sunday walkthrough → **move-day-item** (`--state completed|incomplete|added|deleted`)
- `/goodnight` daily closeout calls this skill ONLY for **carry-forward-day** (moves all unchecked/non-empty priority slots from today's day tab to tomorrow's next empty slots; no item-by-item approval needed; `--dry-run` available). Repo closeout, commits, pushes, durable learnings, hooks, and decision traces belong to `goodnight-closeout`.
- Kay says "make X a weekly recurring task on {day}" / "always put Y on Mondays" → **recurring-add**
- Kay says "stop the recurring task in row N" / "drop the recurring X" → **recurring-remove**
- Kay says "start a project for X" / "create a Gantt for {project}" → **projects-create-gantt**
- Kay reports a chart broke / strikethrough not firing / formatting drifted → **reformat**
- Kay says "clean up the To Do tab" / "look at all the empty rows" / "eliminate the gap rows" → **compact-todo** (also runs automatically inside `build-week`)
- Friday morning weekly review → **report** (carry-forward from prior week + slot capacity)
- `goodmorning` capture pass → batch **append** for items surfaced in email-intelligence + open loops from yesterday's session-decisions
- Kay says "Healthcare milestone N done" / "tick week K on {project}" → **gantt-tick**

## File scope — owns ONE sheet

| File | Location | Owned? |
|---|---|---|
| Personal task tracker | Current weekly Google Sheet in `STRATEGIC PLANNING`; prior weekly files in `To Do Archive`. Current sheet ID resolved via `scripts/tracker_sheet_resolver.py --print-id` (env var `TRACKER_SHEET_ID` overrides) | YES |
| Legacy Excel (read-only) | `~/My Drive/STRATEGIC PLANNING/TO DO 4.26.26.xlsx` — preserved as historical artifact; do not write | Read-only reference |

Out of scope: Industry Research Tracker, DealsX, target lists, vault, briefs. Those belong to other skills.

## Verbs

All verbs are exposed via `scripts/task_tracker.py` with subcommands. Chief of Staff calls them; this skill is the contract.

### 1. append

Add a single row to the To Do tab.

```bash
python3 scripts/task_tracker.py append \
  --task "Draft brochure for LF" \
  --type Work \
  --project "Kai Grey" \
  --due "2026-05-08" \
  --notes "Reference Vivienne deck" \
  --horizon "Short Term"
```

- Type: `Work` or `Home` (only). Required.
- Project: free text, optional. Use entity-name conventions: `G&B`, `Kai Grey`, `Panthera Grey`, `Myself Renewed`, or a project name like `Healthcare`.
- Due: ISO date `YYYY-MM-DD`, optional.
- Notes: free text, optional.
- Horizon: optional dropdown value — `Short Term` (default), `Long Term`, or `Weekly Recurring {day}`. Someday/intent items use `Long Term`.
- Status auto-fills `Not Completed`. Inserts at the first empty row >=6. Returns the row number on stdout.

### 2. promote

Move an item from To Do into a specific day's priority slot on the live week tab.

```bash
python3 scripts/task_tracker.py promote \
  --todo-row 12 \
  --day Wed \
  --slot 3
```

- `--day` accepts Sun..Sat / Mon..Sun (resolves to the matching day TAB)
- `--slot` is 1-25 (rows 16-40 on the target day tab)
- Copies Task (+ Type/Project) from the To Do row into the day tab's slot (A:E), leaves the To Do row in place but prepends a `→ promoted to {day} slot {N} on {date}` marker to its Notes field so it's visually de-prioritized but still readable.
- Refuses to overwrite a non-empty priority slot (shows current contents, errors out).

### 3. build-week (Sunday weekly rebuild ceremony — targets the Week planning tab)

Run from `goodmorning` on Sunday (the Sunday-evening `archive` trigger is RETIRED).

```bash
python3 scripts/task_tracker.py build-week [--skip-recurring] [--skip-carryover] [--dry-run]
```

1. Computes the Sunday-boundary week (`today - (weekday+1)%7` → Sun..Sat).
2. Snapshots the **Week tab** + `To Do` + all 7 day tabs to one rollback JSON.
3. Writes ONE combined far-right `archive_{Sun-date}` tab capturing the prior week's **Week tab** verbatim (values-only flat archive). The Week tab is NOT destroyed — it is cleared + re-titled in place; title/headers/labels/dropdowns/CF/checkbox-validation formatting is preserved.
4. Clears all 7 day-blocks on the Week tab: habit checkboxes, 25 priority slots/day, notes block.
5. Re-titles the Week tab's row-1 title to `WEEK OF {Sun-Sat}` + re-stamps the per-day header-row dates.
6. **Reads the recurring `To Do` rows** (Horizon starts with "Weekly Recurring" + Status `On-going`) and **stamps each onto the Week tab** for its day (collision-refuse logic — explicit slot pins, blank slots auto-pick first empty, conflicts warn+skip). `--skip-recurring` bypasses.
6a. **AUTO-PULL incomplete carryover from prior week's day tabs onto the new Week tab (NEW — 2026-05-26 per Kay):**
    - For each of the 7 day tabs, read every priority slot (rows 16–40, status col A + task col B).
    - An item is "incomplete" if `Task` is non-empty AND `Status` checkbox is FALSE.
    - For each incomplete item: write the Task text into the same day's day-block on the new Week tab (collision-refuse vs recurring stamps; auto-pick next empty slot if its prior slot is occupied by a recurring item).
    - Items whose source slot has Status TRUE are SKIPPED (they were completed last week; no need to carry).
    - Items whose source slot is empty are SKIPPED.
    - Trace each pulled item: `- carryover-pull: {Day} slot N "{Task}"`.
    - `--skip-carryover` flag bypasses this step (useful for first-ever build or recovery scenarios).
    - **Why:** closes the loop. Kay reviews carryover items ON THE WEEK TAB during the Sunday walkthrough; no separate `report` → `move-day-item` per-item dance. Carryover doctrine corrected 2026-05-26.
7. **The 7 day tabs are NOT touched by build-week itself** (only READ for carryover-pull). Day tabs get OVERWRITTEN downstream by `distribute-week`. Kay finalizes the week on the Week tab between `build-week` and `distribute-week`.

`archive` is a DEPRECATED alias → `build-week` (prints a deprecation notice on stderr, then delegates).

**Implementation status (2026-05-26):** Step 6a auto-pull is SPEC'd here but NOT YET IMPLEMENTED in `scripts/task_tracker.py::cmd_build_week`. Until shipped, the Sunday workflow temporarily continues with the old manual `report` → `move-day-item` pattern. Follow-up bead required to land the implementation. Once shipped, the `report` verb's "Carryover" section becomes ad-hoc/diagnostic only.

### 3a-bis. distribute-week (fan the finalized Week plan into the 7 day tabs)

```bash
python3 scripts/task_tracker.py distribute-week [--dry-run] [--force] [--day Wed]
```

Run AFTER Kay finalizes the week on the Week tab. Reads each Week-grid day-block's 25 priority slots (status + task) + habit checkboxes and writes them into the corresponding day tab's slots (rows 16–40) + habits (rows 5–13).

- **Collision-aware:** refuses to overwrite a non-empty day-tab slot the Week plan changes (or that the Week plan leaves empty) unless `--force` — so re-running after a manual day-tab edit is safe by default. `--dry-run` reports planned writes + collisions; `--day {Sun..Sat}` limits to one day.
- Task text only is carried onto/off the Week canvas (compact); day-tab Type/Project/Notes are reset to blank on distribute (Kay enriches on the day tab, or the metadata was set on the recurring `To Do` row). Snapshots every target day tab + the Week tab; always traces.

### 3a. move-day-item (manual carryover between day tabs)

```bash
python3 scripts/task_tracker.py move-day-item \
  --from Thu --slot 4 --to Sun [--to-slot 2] \
  --state completed|incomplete|added|deleted [--force]
```

- `completed`: copy src→dst, dst status TRUE, clear src (a move).
- `incomplete`: copy src→dst, dst status FALSE, clear src (carry forward).
- `added`: write dst only (`--task` required; src ignored — brand-new item).
- `deleted`: clear src only, no dst write.
- Copies Task/Type/Project/Notes. `--to-slot` optional (auto-picks first empty on dst). Collision-refuse on an occupied dst unless `--force`. Snapshots src+dst, always traces.

### 3b. archive-todo (RETIRED 2026-05-17 — no-op)

`archive-todo` is **RETIRED**. There is no sweep and no `Completed To Do` tab. "Done" is now `Status == "Completed"` set in place on the `To Do` row; the row stays where it is and renders via done-row CF. The verb remains as a **no-op** (prints a deprecation notice on stderr and exits 0) so any stale caller does not error. Cleanliness = saved filter/sort views in the Sheet UI, not row relocation. The Sunday ceremony no longer runs it.

### 3c. sync-done-status (reconcile weekly slots → To Do)

```bash
python3 scripts/task_tracker.py sync-done-status [--dry-run]
```

When Kay checks a priority-slot status box during the week, this verb walks all 7 day TABS × 25 priority slots (cols A=status checkbox, B=task; rows 16-40) and finds every checked slot, then matches each slot's Task field against the To Do tab's Task field (exact case, leading/trailing whitespace stripped). For each unambiguous match where the To Do `Status` is not yet `Completed`, the verb sets `Status` to `Completed` so the existing conditional formatting paints strikethrough + sage-light fill.

- **Match found, To Do Status != Completed** → set to `Completed`.
- **Match found, To Do Status already `Completed`** → no-op.
- **Match NOT found** → skipped silently (likely a `schedule-to-day-slot` item that never lived on To Do).
- **Match found, but multiple To Do rows share the same task text** → ambiguous. Verb prints `AMBIGUITY: "<task>" matches To Do rows [N, M]` and skips the write. Resolve manually.
- Snapshots the To Do Status column before any write; trace emitted ONLY if rows changed.
- `--dry-run` reports what would change without writing.

Direct invocation when Kay wants to refresh strikethrough/fill on To Do mid-week to reflect day-tab progress.

### 4. schedule-to-day-slot (direct write, no To Do source)

```bash
python3 scripts/task_tracker.py schedule-to-day-slot \
  --task "Assess budget reduction areas (post-Q1 expense review)" \
  --day Fri \
  --slot 5
```

- `--day` accepts Sun..Sat / Mon..Sun (resolves to the matching day TAB)
- `--slot` is 1..25 (rows 16-40) — **optional**; if omitted, auto-picks the first empty slot for that day tab. (Single-step alternative to `append` → `promote`.)
- Optional `--type` / `--project` / `--notes` write into C/D/E of the slot.
- Refuses to overwrite an occupied slot unless `--force` is passed.
- Status cell auto-fills as an unchecked native Sheets checkbox.

### 5. projects-create-gantt

```bash
python3 scripts/task_tracker.py projects-create-gantt \
  --project "Deal Aggregator Expansion" \
  --entity "G&B" \
  --status "Plan Needed" \
  --start "2026-05-11" \
  --target "2026-06-15" \
  --weeks 12 \
  --notes "Re-plan dedicated session Tue 5/12"
```

- Creates a new Gantt project tab cloning the **Myself Renewed Healthcare** structure: title (row 2), subtitle (row 3), header row 5 with Status/Milestone/Start/Target/Notes + N weekly Monday-anchored columns starting from the Monday of `--start`.
- 10 blank milestone rows scaffolded with native Sheets checkboxes in the Status column ready for fill-in.
- Conditional formatting: week-cell checked → entity-color fill (builds the Gantt bar); milestone-row checked → muted/strikethrough.
- Entity colors: Home / G&B / Myself Renewed / Kai Grey / Panthera Grey (defaults to G&B sage if unknown).
- Updates the Projects index: appends a new row if the project isn't there, or updates the existing row's `Tab` HYPERLINK if it already exists (preserves notes from the prior row).
- Tab name validation: no `:\/?*[]` characters.

### 7. recurring-add

Append a `To Do` row with `Horizon = Weekly Recurring {day}` and `Status = On-going`. `build-week` reads these rows every Sunday and stamps them onto the new week. Decision-content (changes future weeks) — emits a trace.

```bash
python3 scripts/task_tracker.py recurring-add \
  --day Mon \
  --task "Process payroll" \
  --type Work \
  --project "G&B" \
  [--slot 3] \
  [--notes "..."]
```

- `--day` accepts Mon..Sun (case-insensitive, canonicalizes to 3-letter form) — sets `Horizon = Weekly Recurring {day}`.
- `--type` is `Work` or `Home` (required).
- `--slot` is optional; omit for auto-pick at stamp time. Numeric 1..25. (Stored in Notes as a slot pin if given.)
- `--project` and `--notes` are free text, optional.
- Writes a normal `To Do` row (Status `On-going`) at the first empty row >=6.

### 8. recurring-remove

Stop a recurring item by clearing its `To Do` row (preserves row numbering for snapshot rollback).

```bash
python3 scripts/task_tracker.py recurring-remove --row 12
```

- `--row` is the 1-based row number on the `To Do` tab (row 1 is the header — refuse).
- Refuses if the row is already empty or is not a `Weekly Recurring` row.
- Snapshots the row first, traces the removal.

### 4. reformat

Re-apply conditional formatting (strikethrough/sage-light done-row fill across Week priorities, day-tab priorities, habits, and the `To Do` tab — done-row CF fires on `Status == "Completed"`) after a manual edit broke a rule.

```bash
python3 scripts/task_tracker.py reformat
```

Idempotent — safe to run more than once. Adds the canonical rules; does not delete pre-existing ones.

### 4b. compact-todo

Strip empty/leftover gap rows from the `To Do` tab and pack real rows to the top. See "Empty-row compaction doctrine" above for the why.

```bash
python3 scripts/task_tracker.py compact-todo [--dry-run] [--buffer N]
```

- A *real* row = Task (col B) non-empty. Everything else (leftover `FALSE` checkbox cells, blank rows) is a gap and gets removed.
- Rewrites header + real rows contiguously from row 2, physically **deletes** the surplus rows so the sheet shrinks (not just clears them), and re-applies Status/Type/Project/Horizon dropdown validation across the retained range.
- `--buffer N` (default 40) = blank validated rows kept below the content for future `append` writes. `--dry-run` reports real/gap counts without writing.
- Snapshots the full tab first; traces only when ≥1 gap row is removed (no-op runs leave no trace).
- **Runs automatically inside `build-week`** (step 4b, on the freshly-copied new file) so every week starts clean. Decision-content (changes sheet structure) → emits a trace.

### 5. report

Surface a To Do health summary. Returns markdown. Used by Friday briefing + on-demand.

Output shape:
```
## Tracker health (as of {date})
- {N} overdue (Due before today, Status != Completed)
- {N} unscheduled (To Do tab, no Due, sitting > 7 days)
- {N} priority slots empty for tomorrow
- Carryover from last week: {list of items not done in last week, by day}
- Stale projects (no tick on Gantt in 14+ days): {project list}
- Sheet: <url>
```

### 6. gantt-tick

Tick a week-cell on a Gantt project tab.

```bash
python3 scripts/task_tracker.py gantt-tick \
  --project "Myself Renewed Healthcare" \
  --milestone-row 6 \
  --week-col K
```

Sets the cell to a checked native Sheets checkbox; conditional-format fills it with the entity color, building the Gantt bar.

## Decision matrix — auto-execute vs surface-for-approval

**AUTO-EXECUTE** (proceed without YES/NO):
- `gantt-tick` on a milestone Kay just told me she completed
- `reformat` when broken formatting is detected during another verb's execution
- `compact-todo` when Kay asks to clean up gap rows, or any time the To Do tab has accumulated gaps (snapshot-protected, run `--dry-run` first if unsure of the count)
- `build-week` on Sunday morning as part of `goodmorning` (`archive` alias delegates here) — targets the Week tab; day tabs untouched
- `distribute-week` on Sunday once Kay confirms the Week tab is finalized (run `--dry-run` first; surface collisions before a `--force`)
- `move-day-item` when Kay approves a specific carryover during the Sunday walkthrough
- `sync-done-status` on demand (reflect day-tab progress onto `To Do` Status)
- `append` when Kay explicitly says "add to To Do" with the task content already specified
- `recurring-add` when Kay's intent is unambiguous (specific day + task content given, e.g. "make 'process payroll' a recurring Monday task")
- `recurring-remove` when Kay names a specific row to drop and the row content was just confirmed in conversation

**SURFACE FOR APPROVAL** (RECOMMEND + YES/NO/DISCUSS, write only on YES):
- Bulk `append` (>=3 items at once from email-intelligence scan or open loops)
- `promote` — always confirm the day + slot before writing, since this affects Kay's day plan
- `schedule-to-day-slot` — always confirm the day + (auto-picked or explicit) slot before writing; same reason as `promote`
- `projects-create-gantt` — always confirm project name + entity + start/target before writing; this creates a new visible tab that's hard to undo without leaving stub rows in Projects
- Any operation when the tracker file size has changed unexpectedly (>5KB delta from last known good state — possible corruption or external edit)
- Renaming the live tab to a non-current-week label
- `recurring-add` / `recurring-remove` when Kay is exploring ("should we make this recurring?") rather than directing — surface with RECOMMEND and only write on YES. These compound across every future week.

## Hard guardrails — always

1. **Snapshot affected ranges before any write.** Each mutating verb saves the pre-write state of the ranges it touches to `brain/context/rollback-snapshots/tasks-{verb}-{timestamp}.json`. Keep last 5 snapshots per verb, prune older. Rollback path is: read snapshot JSON, replay each range via `values.update`.
2. **API quota backoff.** Every Sheets API call is wrapped with exponential backoff (5 attempts, 1s..16s) on 429 / 5xx responses. Drop the failure cleanly with a `task-tracker-manager: API error <code>` message if it still fails.
3. **Never wipe data on a populated tab.** No bulk-delete or bulk-clear without a snapshot. `build-week` is the only verb that clears the **Week tab's** data, and it writes the combined far-right `archive_{Sun-date}` tab (verbatim values capture of the prior Week tab) before clearing. `distribute-week` overwrites day-tab slots but is collision-refuse by default (`--force` required to clobber) and snapshots every target day tab + the Week tab first. `build_week_tab.py` / `build_day_tabs.py` only (re)write structure/formatting — they do NOT clear existing slot/habit/notes content (build_week_tab.py reverse-populates from the day tabs on first creation).
4. **Trace decision-content writes** to `brain/traces/{date}-task-tracker-{verb}-{slug}.md` with what changed + snapshot path. Trace emission applies ONLY to `build-week` (and its `archive` alias), `move-day-item`, `promote`, `schedule-to-day-slot`, `projects-create-gantt`, `reformat`, `sync-done-status`, `recurring-add`, and `recurring-remove` verbs — those carry decision content. The `append` verb does NOT emit a trace; its rollback line is routed to `logs/scheduled/task-tracker-{date}.log` instead. Rationale: `append` traces are rollback receipts (task + row + snapshot path), not decisions, and they pollute calibration input. Source: 2026-05-08 calibration — 6 of 35 traces (17%) in the prior batch were `append` receipts. **`sync-done-status` is no-op-aware:** it writes a trace ONLY when ≥1 To Do row actually flipped — no-op runs leave no trace (same calibration-pollution rationale). **`compact-todo` is likewise no-op-aware:** traces ONLY when ≥1 gap row is removed. **`recurring-add` / `recurring-remove` always trace** because each edit compounds across every future Sunday rollover.
5. **Tab-name validation.** No `:\/?*[]` characters in tab names. (Google Sheets is more permissive than Excel — no 31-char cap — but keep the character ban for readability.)
6. **Use native Sheets primitives, never Unicode glyphs.** Checkboxes are native (Data Validation → Checkbox). Dropdowns are native (Data Validation → Dropdown). Conditional formatting is native rules, not formulas-as-text. Done items render via CF rules tied to the checkbox state, not via inserted ✅ characters.

## Output expectations

- Every successful write ends with a single-line confirmation echoed to the Chief of Staff: `task-tracker-manager: appended row 12 ("Draft brochure for LF" / Work / Kai Grey / 2026-05-08)`.
- Every refused write ends with a single-line reason: `task-tracker-manager: refused promote — Wed slot 3 already contains "Vivienne board prep"`.
- Trace files are mandatory for `archive`, `promote`, `schedule-to-day-slot`, `projects-create-gantt`, `reformat`, `recurring-add`, and `recurring-remove` (decision-content verbs). `sync-done-status` writes a trace conditionally (only when ≥1 row was actually flipped). The `append` verb writes its rollback line to `logs/scheduled/task-tracker-{date}.log`, NOT to `brain/traces/` — append receipts are not decisions and pollute calibration input (2026-05-08 calibration). `gantt-tick` and `report` traces remain optional.

## Standard workflow — append example

When Kay says "add 'draft Calder follow-up' to To Do":

1. Chief of Staff parses: task=`Draft Calder follow-up`, type=`Work` (inferred from G&B context), project=`G&B`, due=none, notes=none.
2. Chief of Staff RECOMMENDs: `Add to To Do — "Draft Calder follow-up" / Work / G&B / no due → YES / NO`.
3. Kay says YES.
4. Skill runs `python3 scripts/task_tracker.py append --task "Draft Calder follow-up" --type Work --project "G&B"`.
5. Skill snapshots the target row range, writes the new row via `values.update`, writes the rollback receipt to `logs/scheduled/task-tracker-{date}.log`, echoes confirmation with row number.

## Schedule integration

| Trigger | Verb | Where |
|---|---|---|
| `goodmorning` (weekday) | `report` (overdue + today's empty slots) + batch `append` if open loops | Capture pass at end of morning workflow |
| `goodmorning` **Sunday** | `report` (full week-planning health: carryover, empty slots, stale items, stale Gantt) → walk-through with Kay → `promote`/`append` for each decision | **Canonical Sunday weekly-planning ceremony.** Drives the new-week tab setup. See `goodmorning.md` Step 6 Sunday overlay. |
| Mid-day conversation | `append` / `promote` / `gantt-tick` / `sync-done-status` | On Kay's request |
| `goodmorning` **Sunday** ceremony | `report` (carryover) → Kay walks each carryover (`move-day-item`) → `sync-done-status` across 7 day tabs (reflect last week's progress onto `To Do` Status) → `build-week` (Week tab: archive + clear + re-title + stamp recurring) → Kay finalizes the week on the Week tab (approved promotions / direct entry) → `distribute-week` (fan Week → 7 day tabs) → `reformat` if needed | The single Sunday-evening `goodnight` `archive` trigger is RETIRED. `archive-todo` is RETIRED (no sweep, no `Completed To Do` tab — done = `Status=Completed` in place). `distribute-week` runs AFTER Kay finalizes the Week tab. **Recurring items come from `To Do` rows with `Horizon = Weekly Recurring {day}`** — Kay sets the Horizon dropdown directly or uses `recurring-add` / `recurring-remove`, NOT a separate tab or hardcoded code. |
| Friday briefing | `report` (full health, including carryover) | Part of weekly-tracker context |

## Failure modes to watch

- Sheets API quota exhaustion: retried 5x with exponential backoff. If still failing, surface to Kay as `task-tracker-manager: API error <code>` — don't half-finish a verb.
- Auth failure (gog refresh token revoked): script exits with `task-tracker-manager: gog token export failed`. Fix via `gog auth login` for the kay.s account.
- Tab name collision on archive: if `archive_{week-label}` already exists from a prior failed rollover, append `_v2`, `_v3`, etc. (already handled in code).
- Conditional formatting drift: if a manual edit removed a CF rule, run `reformat` — it re-adds the canonical rules. Note that `reformat` is additive only — duplicate rules may stack. Manually delete duplicates in the Sheet UI if they accumulate.

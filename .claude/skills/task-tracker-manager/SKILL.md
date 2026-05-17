---
name: task-tracker-manager
description: Owns Kay's personal task tracker — Google Sheet (TO DO 5.12.26) — single capture point + 7 permanent day tabs (Sun..Sat) + Gantt project tabs. Append items, promote items into a day tab's priority slots, run the Sunday build-week rebuild ceremony, move/carry items between day tabs, re-apply conditional formatting after manual edits, and surface a To Do health report (overdue / empty slots / per-day carryover). Reports to Chief of Staff. NOT operational sheets — that's tracker-manager.
archetype: router
context_budget:
  skill_md: 200
  max_references: 12
  learnings_md: 40
  sub_agent_limit: 500
---

# Task Tracker Manager

Standing owner of Kay's personal task system. The tracker lives in Google Sheets — title `TO DO 5.12.26`, id `1ewqQshtN5pz8kmMTEvBZgAFy-0XB37-MVONkN_mdZmk`, in the `STRATEGIC PLANNING` Drive folder. Built 2026-04-26 on Excel, **migrated to Google Sheets 2026-05-12** for browser-native access from any device. This skill is the operational layer — Chief of Staff calls into it, this skill executes.

Architecture lives in `memory/project_personal_task_tracker.md`. Update that memory whenever the architecture changes.

**Sheet ID env override:** Scripts read `TRACKER_SHEET_ID` from env if set, otherwise default to the constant above. Future rebuilds: update the constant + set `TRACKER_SHEET_ID` to the new id.

**Architecture (2026-05-17 day-tab rebuild):** The single "Live Week" 7-day-pair grid is RETIRED. The tracker now uses **7 permanent, writable, large-font day tabs** (`Sun Mon Tue Wed Thu Fri Sat`, leftmost in the strip, structurally identical, only the title row differs). Kay plans the week Sunday morning via `/goodmorning` (`build-week` builds/clears + stamps recurring), then lives only in the current day's tab all week. No week-grid mirror, no back-sync. Per-day layout: row 1 merged title `SUNDAY · May 17` (20pt), rows 4–10 habit tracker (7 habits, A=checkbox), row 12 column headers, rows 13–27 fifteen priority slots (A=native checkbox · B=Task 17pt · C=Type dropdown · D=Project dropdown · E=Notes), rows 30–37 free-notes block, one per-day donut chart anchored col G row 1. Builder: `scripts/build_day_tabs.py` (idempotent; `--dry-run`, `--donuts-only`).

**Per-day %-done display:** One native donut chart (pie + `pieHole=0.5`, ~160px, anchored col G row 1) per day tab. Math lives on the hidden helper tab `_donut_data` (header `Day | Done | Left`, 7 rows, `=COUNTIF('Sun'!A13:A27,TRUE)` / `=COUNTA('Sun'!B13:B27)-COUNTIF(...)`). Formulas/charts reference fixed ranges on the permanent day tabs, so `build-week`'s value-clear does not break them. Legacy `scripts/build_donut_charts.py` (single-grid) is superseded by `build_day_tabs.py`.

**Recurring Template tab (added 2026-05-15):** A dedicated tab `Recurring Template` (sheetId `1997242109`, positioned after `To Do Long Term`, before `Projects` and archives) holds rows the Sunday `build-week` ceremony stamps onto every new week. Schema:

| Day | Slot | Task | Type | Project | Notes |
|---|---|---|---|---|---|
| Mon..Sun (dropdown) | 1..15 OR blank (blank = auto-pick first empty slot) | free text | Work / Home (dropdown) | free text (G&B, Kai Grey, etc.) | free text |

Edit the tab from the Sheet UI directly (Kay) or via `recurring-add` / `recurring-remove` verbs (Claude). The `build-week` verb reads this tab and stamps each row onto the 7 clean day tabs after the slots are cleared. Occupied-slot conflicts log + skip (Kay resolves manually). Seeded 2026-05-15 with 4 weekly recurring G&B items: Mon — Process payroll, Mon — Process conference registrations, Wed — Niche intel review, Fri — Weekly review (system health + M&A + budget).

## When to invoke

- Kay says "add to To Do" / "put X on the list" / "save this for later" → **append**
- Kay says "move {todo-row} to {day} slot {N}" (To Do → week tab) → **promote**
- Kay says "schedule X for Wed" / "X goes on Friday" / direct day-slot drop with no To Do source row → **schedule-to-day-slot**
- Kay says "sync done items" / "reconcile weekly to To Do" / "the weekly slots aren't matching To Do" → **sync-done-status**
- Sunday morning as part of `goodmorning` → **build-week** (weekly rebuild ceremony — writes a combined far-right `archive_{Sun-date}` tab, clears + re-titles all 7 day tabs, stamps the Recurring Template; `--skip-recurring` to bypass; `--dry-run` to preview). `archive` is a DEPRECATED alias that delegates here.
- Kay says "move {day} slot N to {day}" / approves a carryover during the Sunday walkthrough → **move-day-item** (`--state completed|incomplete|added|deleted`)
- Sunday morning as part of `goodmorning` → **archive-todo** (auto-runs `sync-done-status` across the 7 day tabs first, then sweeps ✅ rows out of To Do into the Completed To Do running list; safe to run any day; skip the auto-sync with `--skip-sync`). Runs BEFORE `build-week` so the slot→To Do reconciliation sees the still-populated day tabs.
- Kay says "make X a weekly recurring task on {day}" / "always put Y on Mondays" → **recurring-add**
- Kay says "stop the recurring task in row N" / "drop the recurring X from the template" → **recurring-remove**
- Kay says "start a project for X" / "create a Gantt for {project}" → **projects-create-gantt**
- Kay reports a chart broke / strikethrough not firing / formatting drifted → **reformat**
- Friday morning weekly review → **report** (carry-forward from prior week + slot capacity)
- `goodmorning` capture pass → batch **append** for items surfaced in email-intelligence + open loops from yesterday's session-decisions
- Kay says "Healthcare milestone N done" / "tick week K on {project}" → **gantt-tick**

## File scope — owns ONE sheet

| File | Location | Owned? |
|---|---|---|
| Personal task tracker | Google Sheet `TO DO 5.12.26` (id `1ewqQshtN5pz8kmMTEvBZgAFy-0XB37-MVONkN_mdZmk`) in `STRATEGIC PLANNING` Drive folder | YES |
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
  --notes "Reference Vivienne deck"
```

- Type: `Work` or `Home` (only). Required.
- Project: free text, optional. Use entity-name conventions: `G&B`, `Kai Grey`, `Panthera Grey`, `Myself Renewed`, or a project name like `Healthcare`.
- Due: ISO date `YYYY-MM-DD`, optional.
- Notes: free text, optional.
- Inserts at the first empty row >=6. Returns the row number on stdout.

### 2. promote

Move an item from To Do into a specific day's priority slot on the live week tab.

```bash
python3 scripts/task_tracker.py promote \
  --todo-row 12 \
  --day Wed \
  --slot 3
```

- `--day` accepts Sun..Sat / Mon..Sun (resolves to the matching day TAB)
- `--slot` is 1-15 (rows 13-27 on the target day tab)
- Copies Task (+ Type/Project) from the To Do row into the day tab's slot (A:E), leaves the To Do row in place but prepends a `→ promoted to {day} slot {N} on {date}` marker to its Notes field so it's visually de-prioritized but still readable.
- Refuses to overwrite a non-empty priority slot (shows current contents, errors out).

### 3. build-week (Sunday weekly rebuild ceremony)

Run from `goodmorning` on Sunday (the Sunday-evening `archive` trigger is RETIRED).

```bash
python3 scripts/task_tracker.py build-week [--skip-recurring] [--dry-run]
```

1. Computes the Sunday-boundary week (`today - (weekday+1)%7` → Sun..Sat) for the 7 day tabs.
2. Snapshots the 7 day tabs + `_donut_data` + `To Do` to one rollback JSON.
3. Writes ONE combined far-right `archive_{Sun-date}` tab capturing the prior week's 7 day tabs verbatim (values-only flat archive). The live day tabs are NOT duplicated/destroyed — they are cleared + re-titled in place; title/header/dropdown/CF/checkbox-validation formatting is preserved.
4. Clears each present day tab: habit checkboxes, 15 priority slots (A:E), free-notes block.
5. Re-titles each day tab's row-1 title to this week's Sun..Sat date.
6. **Stamps the Recurring Template** onto the 7 clean day tabs (same collision-refuse logic — explicit slot pins, blank slots auto-pick first empty, conflicts warn+skip). `--skip-recurring` bypasses. `--dry-run` previews end-to-end with no writes.
7. Carryover is **NOT auto-copied** — `report` surfaces incompletes; Kay approves each move via `move-day-item`/`promote`.

`archive` is a DEPRECATED alias → `build-week` (prints a deprecation notice on stderr, then delegates).

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

### 3b. archive-todo (sweep ✅ rows out of To Do)

```bash
python3 scripts/task_tracker.py archive-todo
```

Idempotent. **Auto-runs `sync-done-status` as a pre-step** so any priority-slot checkbox Kay flipped during the week propagates to its matching To Do row before the sweep. Pass `--skip-sync` to bypass the pre-step (rare — sweep-only behavior).

Then creates the **Completed To Do** tab on first run (mirror of To Do schema + a trailing `Completed` date column), sweeps every checked row out of the To Do tab and appends it to Completed To Do, stamping today's date. Cleared rows on the To Do side keep their numbered position (Status/Task/Type/Project/Due/Notes all wiped). Safe to run on any day, but the canonical trigger is **Sunday morning as part of the `goodmorning` ceremony**, alongside `build-week`.

### 3c. sync-done-status (reconcile weekly slots → To Do)

```bash
python3 scripts/task_tracker.py sync-done-status [--dry-run]
```

When Kay checks a priority-slot status box during the week, this verb walks all 7 day TABS × 15 priority slots (cols A=status, B=task; rows 13-27) and finds every checked slot, then matches each slot's Task field against the To Do tab's Task field (exact case, leading/trailing whitespace stripped). For each unambiguous match where the To Do Status is FALSE, the verb flips Status to TRUE so the existing conditional formatting paints strikethrough + sage-light fill — and the next `archive-todo` sweep picks the row up cleanly.

- **Match found, To Do Status FALSE** → flip to TRUE.
- **Match found, To Do Status already TRUE** → no-op.
- **Match NOT found** → skipped silently (likely a `schedule-to-day-slot` item that never lived on To Do).
- **Match found, but multiple To Do rows share the same task text** → ambiguous. Verb prints `AMBIGUITY: "<task>" matches To Do rows [N, M]` and skips the write. Resolve manually.
- Snapshots the To Do Status column before any write; trace emitted ONLY if rows changed.
- `--dry-run` reports what would change without writing.

Auto-fires as the pre-step inside `archive-todo` so Sunday cleanup sees the synced state. Direct invocation is rare — useful when Kay wants to refresh strikethrough/fill on To Do mid-week without sweeping.

### 4. schedule-to-day-slot (direct write, no To Do source)

```bash
python3 scripts/task_tracker.py schedule-to-day-slot \
  --task "Assess budget reduction areas (post-Q1 expense review)" \
  --day Fri \
  --slot 5
```

- `--day` accepts Sun..Sat / Mon..Sun (resolves to the matching day TAB)
- `--slot` is 1..15 (rows 13-27) — **optional**; if omitted, auto-picks the first empty slot for that day tab. (Single-step alternative to `append` → `promote`.)
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

Append a row to the `Recurring Template` tab. The row is stamped onto every future Sunday `build-week` ceremony. Decision-content (changes future weeks) — emits a trace.

```bash
python3 scripts/task_tracker.py recurring-add \
  --day Mon \
  --task "Process payroll" \
  --type Work \
  --project "G&B" \
  [--slot 3] \
  [--notes "..."]
```

- `--day` accepts Mon..Sun (case-insensitive, canonicalizes to 3-letter form).
- `--type` is `Work` or `Home` (required).
- `--slot` is optional; omit for auto-pick (blank in the Sheet = first empty slot at stamp time). Numeric 1..15.
- `--project` and `--notes` are free text, optional.
- Appends to the first empty row >=2 (preserves explicit row gaps).

### 8. recurring-remove

Clear a row on the `Recurring Template` tab (preserves row numbering for snapshot rollback).

```bash
python3 scripts/task_tracker.py recurring-remove --row 5
```

- `--row` is the 1-based row number on the Recurring Template tab (row 1 is the header — refuse).
- Refuses if the row is already empty.
- Snapshots the row first, traces the removal.

### 4. reformat

Re-apply conditional formatting (strikethrough/sage-light done-row fill across Live Week priorities, habits, To Do, To Do Long Term) after a manual edit broke a rule.

```bash
python3 scripts/task_tracker.py reformat
```

Idempotent — safe to run more than once. Adds the canonical rules; does not delete pre-existing ones.

### 5. report

Surface a To Do health summary. Returns markdown. Used by Friday briefing + on-demand.

Output shape:
```
## Tracker health (as of {date})
- {N} overdue (Due before today, Status unchecked)
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
- `build-week` on Sunday morning as part of `goodmorning` (`archive` alias delegates here)
- `move-day-item` when Kay approves a specific carryover during the Sunday walkthrough
- `archive-todo` on Sunday as part of the ceremony (auto-calls `sync-done-status` first)
- `sync-done-status` on demand and as the auto pre-step inside `archive-todo`
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
3. **Never wipe data on a populated tab.** No bulk-delete or bulk-clear without a snapshot. `build-week` is the only verb that clears the day tabs' data, and it writes the combined far-right `archive_{Sun-date}` tab (verbatim values capture) before clearing. `build_day_tabs.py` only (re)writes structure/formatting — it does NOT clear existing slot/habit/notes content.
4. **Trace decision-content writes** to `brain/traces/{date}-task-tracker-{verb}-{slug}.md` with what changed + snapshot path. Trace emission applies ONLY to `build-week` (and its `archive` alias), `move-day-item`, `archive-todo`, `promote`, `schedule-to-day-slot`, `projects-create-gantt`, `reformat`, `sync-done-status`, `recurring-add`, and `recurring-remove` verbs — those carry decision content. The `append` verb does NOT emit a trace; its rollback line is routed to `logs/scheduled/task-tracker-{date}.log` instead. Rationale: `append` traces are rollback receipts (task + row + snapshot path), not decisions, and they pollute calibration input. Source: 2026-05-08 calibration — 6 of 35 traces (17%) in the prior batch were `append` receipts. **`sync-done-status` is no-op-aware:** it writes a trace ONLY when ≥1 To Do row actually flipped — no-op runs leave no trace (same calibration-pollution rationale). **`recurring-add` / `recurring-remove` always trace** because each edit compounds across every future Sunday rollover.
5. **Tab-name validation.** No `:\/?*[]` characters in tab names. (Google Sheets is more permissive than Excel — no 31-char cap — but keep the character ban for readability.)
6. **Use native Sheets primitives, never Unicode glyphs.** Checkboxes are native (Data Validation → Checkbox). Dropdowns are native (Data Validation → Dropdown). Conditional formatting is native rules, not formulas-as-text. Done items render via CF rules tied to the checkbox state, not via inserted ✅ characters.

## Output expectations

- Every successful write ends with a single-line confirmation echoed to the Chief of Staff: `task-tracker-manager: appended row 12 ("Draft brochure for LF" / Work / Kai Grey / 2026-05-08)`.
- Every refused write ends with a single-line reason: `task-tracker-manager: refused promote — Wed slot 3 already contains "Vivienne board prep"`.
- Trace files are mandatory for `archive`, `archive-todo`, `promote`, `schedule-to-day-slot`, `projects-create-gantt`, `reformat`, `recurring-add`, and `recurring-remove` (decision-content verbs). `sync-done-status` writes a trace conditionally (only when ≥1 row was actually flipped). The `append` verb writes its rollback line to `logs/scheduled/task-tracker-{date}.log`, NOT to `brain/traces/` — append receipts are not decisions and pollute calibration input (2026-05-08 calibration). `gantt-tick` and `report` traces remain optional.

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
| `goodmorning` **Sunday** ceremony | `report` (carryover) → Kay walks each carryover (`move-day-item`) → `archive-todo` (auto `sync-done-status` across 7 day tabs) → `build-week` (combined archive + clear + re-title + stamp recurring) → approved promotions → `reformat` if needed | The single Sunday-evening `goodnight` `archive` trigger is RETIRED. Order matters: `archive-todo` (and its `sync-done-status` pre-step) must run BEFORE `build-week` so the slot→To Do reconciliation sees the still-populated day tabs. **Recurring items come from the `Recurring Template` tab** — Kay edits it in the Sheet UI or via `recurring-add` / `recurring-remove`, NOT hardcoded in code. |
| Friday briefing | `report` (full health, including carryover) | Part of weekly-tracker context |

## Failure modes to watch

- Sheets API quota exhaustion: retried 5x with exponential backoff. If still failing, surface to Kay as `task-tracker-manager: API error <code>` — don't half-finish a verb.
- Auth failure (gog refresh token revoked): script exits with `task-tracker-manager: gog token export failed`. Fix via `gog auth login` for the kay.s account.
- Tab name collision on archive: if `archive_{week-label}` already exists from a prior failed rollover, append `_v2`, `_v3`, etc. (already handled in code).
- Conditional formatting drift: if a manual edit removed a CF rule, run `reformat` — it re-adds the canonical rules. Note that `reformat` is additive only — duplicate rules may stack. Manually delete duplicates in the Sheet UI if they accumulate.

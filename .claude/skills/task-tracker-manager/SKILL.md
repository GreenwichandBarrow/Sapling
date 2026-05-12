---
name: task-tracker-manager
description: Owns Kay's personal task tracker — Google Sheet (TO DO 5.12.26) — single capture point + per-day priority slots + Gantt project tabs. Append items, promote items into specific day-of-week slots, run the Sunday archive/rollover ceremony, re-apply conditional formatting after manual edits, and surface a To Do health report (overdue / empty slots / weekly carryover). Reports to Chief of Staff. NOT operational sheets — that's tracker-manager.
---

# Task Tracker Manager

Standing owner of Kay's personal task system. The tracker lives in Google Sheets — title `TO DO 5.12.26`, id `1ewqQshtN5pz8kmMTEvBZgAFy-0XB37-MVONkN_mdZmk`, in the `STRATEGIC PLANNING` Drive folder. Built 2026-04-26 on Excel, **migrated to Google Sheets 2026-05-12** for browser-native access from any device. This skill is the operational layer — Chief of Staff calls into it, this skill executes.

Architecture lives in `memory/project_personal_task_tracker.md`. Update that memory whenever the architecture changes.

**Sheet ID env override:** Scripts read `TRACKER_SHEET_ID` from env if set, otherwise default to the constant above. Future rebuilds: update the constant + set `TRACKER_SHEET_ID` to the new id.

## When to invoke

- Kay says "add to To Do" / "put X on the list" / "save this for later" → **append**
- Kay says "move {todo-row} to {day} slot {N}" (To Do → week tab) → **promote**
- Kay says "schedule X for Wed" / "X goes on Friday" / direct day-slot drop with no To Do source row → **schedule-to-day-slot**
- Sunday evening as part of `goodnight` → **archive** (rollover ceremony)
- Sunday evening as part of `goodnight` → **archive-todo** (sweep ✅ rows out of To Do tab into the Completed To Do running list; safe to run any day)
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

- `--day` accepts Mon/Tue/Wed/Thu/Fri/Sat/Sun
- `--slot` is 1-15 (rows 23-37 on the week tab)
- Copies the task text from To Do col C into the day's priority task cell, leaves the To Do row in place but flips its status to `→` (moved indicator) so it's visually de-prioritized but still readable.
- Refuses to overwrite a non-empty priority slot (shows current contents, errors out).

### 3. archive (Sunday rollover ceremony)

Run from `goodnight` on Sunday evening.

1. Reads the live week tab name (e.g., `Apr 27-May 3`).
2. Duplicates the live tab to an archive sheet `archive_{week-label}` via the Sheets API `duplicateSheet` request — all values, formats, conditional formatting, and merges carry over.
3. **Leaves the archive sheet VISIBLE and parks it at the far right** of the tab strip so the live tab + reference tabs stay easy to find. (Hidden archives were rejected by Kay 2026-05-11 — she wants to scroll right to see past weeks.)
4. Renames the live tab to the upcoming week's label. **Monday edge case handled**: if `archive` runs on a Monday, the new live tab uses today (the current Monday), not today+7 (next Monday).
5. Clears: habit checkboxes, priority status checkboxes, priority task text, notes block (all back to empty / unchecked).
6. Posts a one-liner to Slack `#operations` confirming the rollover with the new week label.

### 3b. archive-todo (sweep ✅ rows out of To Do)

```bash
python3 scripts/task_tracker.py archive-todo
```

Idempotent. Creates the **Completed To Do** tab on first run (mirror of To Do schema + a trailing `Completed` date column), then sweeps every checked row out of the To Do tab and appends it to Completed To Do, stamping today's date. Cleared rows on the To Do side keep their numbered position (Status/Task/Type/Project/Due/Notes all wiped). Safe to run on any day, but the canonical trigger is **Sunday evening as part of `goodnight`**, alongside the `archive` ceremony.

### 4. schedule-to-day-slot (direct write, no To Do source)

```bash
python3 scripts/task_tracker.py schedule-to-day-slot \
  --task "Assess budget reduction areas (post-Q1 expense review)" \
  --day Fri \
  --slot 5
```

- `--day` accepts Mon..Sun
- `--slot` is 1..15 — **optional**; if omitted, the verb auto-picks the first empty slot for that day. (This is the single-step alternative to `append` → `promote`.)
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
- `archive` on Sunday evening as part of `goodnight`
- `archive-todo` on Sunday evening as part of `goodnight`
- `append` when Kay explicitly says "add to To Do" with the task content already specified

**SURFACE FOR APPROVAL** (RECOMMEND + YES/NO/DISCUSS, write only on YES):
- Bulk `append` (>=3 items at once from email-intelligence scan or open loops)
- `promote` — always confirm the day + slot before writing, since this affects Kay's day plan
- `schedule-to-day-slot` — always confirm the day + (auto-picked or explicit) slot before writing; same reason as `promote`
- `projects-create-gantt` — always confirm project name + entity + start/target before writing; this creates a new visible tab that's hard to undo without leaving stub rows in Projects
- Any operation when the tracker file size has changed unexpectedly (>5KB delta from last known good state — possible corruption or external edit)
- Renaming the live tab to a non-current-week label

## Hard guardrails — always

1. **Snapshot affected ranges before any write.** Each mutating verb saves the pre-write state of the ranges it touches to `brain/context/rollback-snapshots/tasks-{verb}-{timestamp}.json`. Keep last 5 snapshots per verb, prune older. Rollback path is: read snapshot JSON, replay each range via `values.update`.
2. **API quota backoff.** Every Sheets API call is wrapped with exponential backoff (5 attempts, 1s..16s) on 429 / 5xx responses. Drop the failure cleanly with a `task-tracker-manager: API error <code>` message if it still fails.
3. **Never wipe data on a populated tab.** No bulk-delete or bulk-clear without a snapshot. The `archive` verb is the only verb that clears the live week's data, and it duplicates the tab first.
4. **Trace decision-content writes** to `brain/traces/{date}-task-tracker-{verb}-{slug}.md` with what changed + snapshot path. Trace emission applies ONLY to `archive`, `archive-todo`, `promote`, `schedule-to-day-slot`, `projects-create-gantt`, and `reformat` verbs — those carry decision content. The `append` verb does NOT emit a trace; its rollback line is routed to `logs/scheduled/task-tracker-{date}.log` instead. Rationale: `append` traces are rollback receipts (task + row + snapshot path), not decisions, and they pollute calibration input. Source: 2026-05-08 calibration — 6 of 35 traces (17%) in the prior batch were `append` receipts.
5. **Tab-name validation.** No `:\/?*[]` characters in tab names. (Google Sheets is more permissive than Excel — no 31-char cap — but keep the character ban for readability.)
6. **Use native Sheets primitives, never Unicode glyphs.** Checkboxes are native (Data Validation → Checkbox). Dropdowns are native (Data Validation → Dropdown). Conditional formatting is native rules, not formulas-as-text. Done items render via CF rules tied to the checkbox state, not via inserted ✅ characters.

## Output expectations

- Every successful write ends with a single-line confirmation echoed to the Chief of Staff: `task-tracker-manager: appended row 12 ("Draft brochure for LF" / Work / Kai Grey / 2026-05-08)`.
- Every refused write ends with a single-line reason: `task-tracker-manager: refused promote — Wed slot 3 already contains "Vivienne board prep"`.
- Trace files are mandatory for `archive`, `archive-todo`, `promote`, `schedule-to-day-slot`, `projects-create-gantt`, and `reformat` (decision-content verbs). The `append` verb writes its rollback line to `logs/scheduled/task-tracker-{date}.log`, NOT to `brain/traces/` — append receipts are not decisions and pollute calibration input (2026-05-08 calibration). `gantt-tick` and `report` traces remain optional.

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
| Mid-day conversation | `append` / `promote` / `gantt-tick` | On Kay's request |
| `goodnight` Sunday | `archive` | Step before git commit. Rolls the live tab into next-week's name + clears slots. Pairs with Sunday-morning `report` to bracket the week. |
| Friday briefing | `report` (full health, including carryover) | Part of weekly-tracker context |

## Failure modes to watch

- Sheets API quota exhaustion: retried 5x with exponential backoff. If still failing, surface to Kay as `task-tracker-manager: API error <code>` — don't half-finish a verb.
- Auth failure (gog refresh token revoked): script exits with `task-tracker-manager: gog token export failed`. Fix via `gog auth login` for the kay.s account.
- Tab name collision on archive: if `archive_{week-label}` already exists from a prior failed rollover, append `_v2`, `_v3`, etc. (already handled in code).
- Conditional formatting drift: if a manual edit removed a CF rule, run `reformat` — it re-adds the canonical rules. Note that `reformat` is additive only — duplicate rules may stack. Manually delete duplicates in the Sheet UI if they accumulate.

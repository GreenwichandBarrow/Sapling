---
name: task-tracker-manager
description: Owns Kay's personal Excel task tracker (TO DO M.DD.YY.xlsx) — single capture point + per-day priority slots + Gantt project tabs. Append items, promote items into specific day-of-week slots, run the Sunday archive/rollover ceremony, re-apply conditional formatting after manual edits, and surface a To Do health report (overdue / empty slots / weekly carryover). Reports to Chief of Staff. NOT operational sheets — that's tracker-manager.
---

# Task Tracker Manager

Standing owner of Kay's personal task system. The file lives in Drive (`/Users/kaycschneider/My Drive/STRATEGIC PLANNING/TO DO M.DD.YY.xlsx`). Built 2026-04-26 to replace Motion. This skill is the operational layer — Chief of Staff calls into it, this skill executes.

Architecture lives in `memory/project_personal_task_tracker.md`. Update that memory whenever the architecture changes.

## When to invoke

- Kay says "add to To Do" / "put X on the list" / "save this for later" → **append**
- Kay says "move X to {day} slot {N}" / "schedule X for Wed" / "X goes on Friday" → **promote**
- Sunday evening as part of `goodnight` → **archive** (rollover ceremony)
- Kay reports a chart broke / strikethrough not firing / formatting drifted → **reformat**
- Friday morning weekly review → **report** (carry-forward from prior week + slot capacity)
- `goodmorning` capture pass → batch **append** for items surfaced in email-intelligence + open loops from yesterday's session-decisions
- Kay says "Healthcare milestone N done" / "tick week K on {project}" → **gantt-tick**

## File scope — owns ONE file

| File | Path | Owned? |
|---|---|---|
| Personal task tracker | `~/My Drive/STRATEGIC PLANNING/TO DO M.DD.YY.xlsx` | YES |
| Backup template | `~/My Drive/MANAGER DOCUMENTS/G&B MASTER TEMPLATES/TO DO TEMPLATE.xlsx` | Read-only reference |

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
2. Creates a hidden archive sheet `archive_{week-label}` with a deep-copy of all current cell values, styles, and merged ranges. (openpyxl can't `Move/Copy` like Excel UI — we serialize cell-by-cell.)
3. Hides the archive sheet.
4. Renames the live tab to next week's label (`May 4-10`).
5. Clears: habit checkmarks (rows 7-13 → ☐), priority status cells (rows 23-37 col `sc` → ☐), priority task text (cols `tc` → empty), notes block (rows 40-47).
6. Posts a one-liner to Slack `#operations` confirming the rollover with the new week label.

### 4. reformat

Re-apply conditional formatting + fix donuts when manual Excel edits broke them. Also runs on the first invocation after the legacy donut-chart layout (replaces donuts with big % display in the merged anchor cells rows 17-21).

```bash
python3 scripts/task_tracker.py reformat
```

Idempotent — safe to run more than once. Calls into `scripts/maintain_tasks_excel.py` core logic.

### 5. report

Surface a To Do health summary. Returns markdown. Used by Friday briefing + on-demand.

Output shape:
```
## Tracker health (as of {date})
- {N} overdue (Due before today, Status not ✅)
- {N} unscheduled (To Do tab, no Due, sitting > 7 days)
- {N} priority slots empty for tomorrow
- Carryover from last week: {list of items not done in last 5 priority slots, by day}
- Stale projects (no tick on Gantt in 14+ days): {project list}
```

### 6. gantt-tick

Fill a week-cell on a Gantt project tab.

```bash
python3 scripts/task_tracker.py gantt-tick \
  --project "Myself Renewed Healthcare" \
  --milestone-row 6 \
  --week-col K
```

Sets the cell to `✅` so the conditional-format fills it with the entity color, building the Gantt bar.

## Decision matrix — auto-execute vs surface-for-approval

**AUTO-EXECUTE** (proceed without YES/NO):
- `gantt-tick` on a milestone Kay just told me she completed
- `reformat` when broken formatting is detected during another verb's execution
- `archive` on Sunday evening as part of `goodnight`
- `append` when Kay explicitly says "add to To Do" with the task content already specified

**SURFACE FOR APPROVAL** (RECOMMEND + YES/NO/DISCUSS, write only on YES):
- Bulk `append` (>=3 items at once from email-intelligence scan or open loops)
- `promote` — always confirm the day + slot before writing, since this affects Kay's day plan
- Any operation when the tracker file size has changed unexpectedly (>5KB delta from last known good state — possible corruption or external edit)
- Renaming the live tab to a non-current-week label

## Hard guardrails — always

1. **Backup before any write.** Copy the live xlsx to `~/My Drive/STRATEGIC PLANNING/TO DO M.DD.YY.bak.{timestamp}.xlsx` before opening for write. Keep last 5 backups, prune older.
2. **File-lock check.** Before opening for write, `lsof` the file. If Excel has a handle on it, error out with "Excel has the file open — close it first" and surface to Kay. Never blind-overwrite a file Excel is editing (Excel's autosave will clobber our write or vice versa).
3. **Never rerun build_tasks_excel.py on a populated file.** That script wipes data. Only the rebuild path uses it — and only after a backup.
4. **Trace every write** to `brain/traces/{date}-task-tracker-{verb}-{slug}.md` with what changed + rollback path (`cp` from the backup).
5. **Tab-name validation.** Excel forbids `:\/?*[]` in tab names and caps at 31 chars. Any rename calls `validate_tab_name(name)` before applying.
6. **No openpyxl chart objects on the week tab.** They render blank on Excel-Mac. Use cell-based % display instead (path C decision, 2026-05-01).

## Output expectations

- Every successful write ends with a single-line confirmation echoed to the Chief of Staff: `task-tracker-manager: appended row 12 ("Draft brochure for LF" / Work / Kai Grey / 2026-05-08)`.
- Every refused write ends with a single-line reason: `task-tracker-manager: refused promote — Wed slot 3 already contains "Vivienne board prep"`.
- Trace files are mandatory for `append`, `promote`, `archive`. Optional for `reformat`, `gantt-tick`, `report`.

## Standard workflow — append example

When Kay says "add 'draft Calder follow-up' to To Do":

1. Chief of Staff parses: task=`Draft Calder follow-up`, type=`Work` (inferred from G&B context), project=`G&B`, due=none, notes=none.
2. Chief of Staff RECOMMENDs: `Add to To Do — "Draft Calder follow-up" / Work / G&B / no due → YES / NO`.
3. Kay says YES.
4. Skill runs `python3 scripts/task_tracker.py append --task "Draft Calder follow-up" --type Work --project "G&B"`.
5. Skill backs up file, validates Excel is closed, writes the row, verifies via read-back, writes a trace, echoes confirmation.

## Schedule integration

| Trigger | Verb | Where |
|---|---|---|
| `goodmorning` | `report` (overdue + today's empty slots) + batch `append` if open loops | Capture pass at end of morning workflow |
| Mid-day conversation | `append` / `promote` / `gantt-tick` | On Kay's request |
| `goodnight` Sunday | `archive` | Step before git commit |
| Friday briefing | `report` (full health, including carryover) | Part of weekly-tracker context |

## Failure modes to watch

- Drive sync conflict: if Drive shows `(1)` or `(conflict)` suffix on the file, stop and surface — never write to a conflict copy.
- Tab name collision on archive: if `archive_{week-label}` already exists from a prior failed rollover, append `_v2`, `_v3`, etc.
- Conditional formatting drift: if `reformat` reports >2 sheets had missing rules, that's a sign manual editing broke things — note in the trace and consider scheduling a `reformat` on the next briefing.

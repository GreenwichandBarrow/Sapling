---
name: compact-slots-after-move-or-clear
description: When clearing or moving items in the personal task tracker's weekly tab, immediately compact the remaining items so there are no blank rows above filled ones. Day's slots should always be flush-top, no gaps.
metadata:
  type: feedback
---

## Rule

When a verb clears a slot or moves an item between days, **immediately pull remaining items up** so each day's priority list is flush-top with no blank rows between filled ones.

- ✅ A day's filled slots occupy slots 1..N contiguously (1, 2, 3 — no gap)
- ❌ A day's filled slots scattered with empties between (1, then blank, then 3 — gap at slot 2)

## Why

Visual scan cost: when a day's column has filled-blank-filled-blank-filled, Kay can't tell at a glance "what am I working on today?" — she has to skip over empty rows to read the next task. Flush-top is the natural reading pattern (top-down, no breaks). Also matters for the donut chart math: the `_donut_data` formulas use `COUNTA(task_range)` which counts non-empty cells anywhere in rows 23-37; gaps don't break the math but DO make the layout messy.

Precipitating trace: 2026-05-12 — after Thursday-clear and Friday→Sunday batch moves, Tuesday had slots 1, 2, 6, 8 filled with 3, 4, 5, 7 blank; Friday had slots 5, 6 filled with 1-4 blank. Kay flagged: "please make sure once you move items, you pull up the remaining so there are no blank rows or cells above a to do item on a days list."

## How to apply

For **every** verb that mutates slots (`promote`, `schedule-to-day-slot`, `--force` overwrites, manual `move` operations, slot clears, status sweeps), the implementation MUST:

1. After the primary write, read the affected day's full slot column (rows 23-37 of the task-text column for that day).
2. Identify any blank rows BELOW filled rows.
3. Pull filled rows up to fill the gap. Preserve each row's status checkbox alongside the task text — both `status_col` and `task_col` cells move together as a pair.
4. Clear the now-vacated tail rows.

For the existing verbs, this means:
- `schedule-to-day-slot`: when it auto-picks a slot N, but there's a gap at any slot < N, place the item at the gap instead, and don't leave gaps behind when items are moved out.
- `promote`: same — the destination slot's day must compact after the write if there are gaps.
- Manual Sheets-API moves (e.g., a "move from day X to day Y" pattern): after writing the destination and clearing the source, compact BOTH the source day and the destination day.

For ad-hoc / one-off scripts that move slots, ALWAYS include the compaction pass before reporting "done."

## Edge cases

- Done (✅) items still occupy a slot until Sunday's `archive-todo` sweep. Don't drop them prematurely. Compaction just pulls them up alongside open items — the strikethrough fill stays.
- Cross-day moves (e.g., Friday→Sunday for 4 items): compact the SOURCE day AND the DESTINATION day. Destination already gets compacted by writing items into slots 1, 2, 3, 4 sequentially. Source needs compaction if there were filled rows BELOW the cleared rows.

## Follow-up: graduate to skill verb

This rule should eventually be enforced via a `compact-day` verb on `scripts/task_tracker.py` that any other verb calls as a post-step. Until that exists, every mutation script (gog calls, direct API batchUpdates) does the compaction inline.

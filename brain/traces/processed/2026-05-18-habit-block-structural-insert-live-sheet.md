---
schema_version: 1.1.0
date: 2026-05-18
review_status: applied
type: trace
title: "Structural insert into live task-tracker habit block: proceed on explicit Kay direction + snapshot, even with pre-existing constant drift"
trace_type: judgment-call
tags: ["date/2026-05-18", "trace", "topic/task-tracker", "topic/habit-tracker", "topic/structural-change", "status/closed"]
---

# Structural insert into live task-tracker habit block: proceed on explicit Kay direction + snapshot, even with pre-existing constant drift

## Trigger

Kay directed splitting the habit tracker: relabel "Meditation & stretches"→Meditation, "Exercise class"→Class, AND add a new "Exercises" row under Meditation. The habit block was exactly full (8 rows, no spare); priority-slot/notes rows are hardcoded immediately after it across `task_tracker.py` + `build_day_tabs.py`. Adding a 9th row = physical row-insert on the Week tab + all 7 day tabs mid-Monday (Kay actively using the board) + ~16 code-constant bumps. Inspection also found the Week-tab constants (`WK_SLOT_FIRST_ROW=23`) did NOT match the live sheet (slots at row 16) — pre-existing drift.

## Decision

Proceed with the structural insert. Did the 2 zero-risk relabels immediately; for the new row: full 8-tab snapshot → `insertDimension` (inheritFromBefore) → set label + reset inherited checkbox → bump every constant ≥ insert row by +1 in both scripts → `sync-done-status --dry-run` to prove verbs read the new layout → update SKILL.md + architecture memory.

## Alternatives Considered

- **Defer / ask again** — rejected: Kay had directed it twice with clarification (action mandate = HOW not WHETHER). Re-asking = decision-fatigue violation.
- **Relabel only, drop the new row** — rejected: that silently ignores half her explicit instruction.
- **Repurpose an existing habit row instead of inserting** — rejected: would delete one of her habits on Claude's judgment.
- **Block on the Week-tab constant drift first** — rejected: the +1 *relative* shift is sound regardless of absolute baseline (insertDimension shifts every row below by exactly 1, so constant+1 preserves whatever mapping existed). Fixing the unrelated pre-existing drift mid-task would widen scope.

## Reasoning

Confirm-before-irreversible applies to live outward-facing systems — but Kay's explicit twice-given direction resolves WHETHER; my job was a correct, reversible HOW. Snapshot + verb dry-run made it reversible and verified. The pre-existing Week constant mismatch was a landmine to *not* step on (don't "fix" unrelated drift inside a directed change), not a blocker, because relative shift math holds independent of it.

## Why This Trace Matters

A future agent facing "structural change to Kay's live tracker mid-workday" might either refuse (over-cautious, ignores her directive) or charge in without snapshot/verb-verification (corrupts the board). The middle path: explicit direction resolves WHETHER; snapshot + post-change verb dry-run is the mandatory HOW safety net; and pre-existing drift in adjacent constants is left alone unless it actually breaks the relative shift.

## Key Insight

A row insert is a relative +1 to everything below it — that math is correct even when the absolute baseline constants are already wrong. Verify the change with the consuming code (a verb dry-run), not just by eyeballing the sheet.

---
name: check-status-before-surfacing-carryover
description: When the task tracker shows a non-empty slot, check the status checkbox before surfacing as carryover or open decision. Checked = TRUE = done; don't re-surface completed work as if it were pending.
metadata:
  type: feedback
---

## Rule

Before flagging any task-tracker slot item as "carryover" / "still open" / "decision needed," **read the status checkbox state of that slot, not just the task text**. A slot with a non-empty task description AND a checked status box (`TRUE`) is **completed work** — it should NOT be surfaced as an open decision in a briefing or summary.

## Why

The `promote` verb's "refused — slot already contains X" error message only tells you the task TEXT is non-empty. It says nothing about whether the work has been done. If you surface that text as a carryover/open item without checking the status, you'll re-raise completed items and waste Kay's decision attention.

## Precipitating trace

2026-05-12 — During the new-Sheet today-slot update, the `promote` verb refused to write to Tuesday slot 2 ("already contains 'Run budget-manager monthly mode for March P&L'"). I surfaced this to Kay as an open carryover decision (run / drop / defer). Kay replied: "you already ran the budget manager for march yesterday." The slot's status checkbox was in fact `TRUE` — work was DONE, not pending. The Sheets migration ported the checked state correctly; I just didn't check it. Pure tracking-hygiene miss.

## How to apply

- When `promote` / `schedule-to-day-slot` errors with "already contains 'X'": don't surface X as an open item. First read the status cell. If `TRUE` → completed, do not surface; instead, either auto-pick another slot or report "slot occupied by completed item; auto-routing to slot N."
- When generating any briefing or summary that pulls live slot contents: include the checkbox state. Render checked items with ✅ prefix or strikethrough. Surface only unchecked items in "open" lists.
- When in doubt: read both the task text AND the status cell (`Live!{status_col}{row}`) before describing the slot. The cost of one extra Sheets read is trivial; the cost of re-surfacing completed work is Kay's decision fatigue.

## Cross-references

- `feedback_decision_fatigue_minimization` — every decision-bucket item should be a real open question, not a closed loop
- `feedback_briefing_no_done_items` — briefings surface open items only; this rule extends the same logic to mid-conversation summaries
- `feedback_no_resurface_yesterday_approved_today_trigger` — same family; don't re-surface things Kay's already resolved

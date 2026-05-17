---
name: feedback_ongoing_todo_capture_ask_placement
description: "Kay drops to-do items ad hoc in conversation anytime — capture each via task-tracker-manager; if she didn't say where, ask placement with a recommended default"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8f278aa1-0390-4c59-a1e0-363cfa6127a3
---

Kay wants to hand off to-do items conversationally on an ongoing basis (not only during structured planning). Any time she says something like "add X", "remind me to X", "I need to X", "todo: X", or otherwise states an actionable item in passing, treat it as a capture event: route it to the personal task tracker via [[project_personal_task_tracker]] (`task-tracker-manager` `append` / `promote` / `schedule-to-day-slot`).

**Why:** She will not always remember to state where it goes, and unrecorded items get lost. She explicitly asked to be asked when placement is unspecified.

**How to apply:**
- If she stated placement (a specific day, the backlog, a project, Long Term) → place it there, confirm in one line, no question.
- If placement is NOT stated → ask ONE question (per [[feedback_questions_one_at_a_time]]) framed as a RECOMMEND with quick alternatives so it resolves in one keystroke (per [[feedback_decision_fatigue_minimization]]). Options after the day-tab rebuild: **To Do backlog** (default for undated/unscheduled — the single capture point), a **specific day tab this week** (Sun..Sat) if it's clearly day-bound, **To Do Long Term** (someday), or a **Project**.
- Default recommendation when genuinely ambiguous: To Do backlog (its design purpose is the catch-all single capture point).
- Never silently drop or defer a stated to-do. Capture immediately; don't batch them away.

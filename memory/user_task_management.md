---
name: task-management-preferences
description: "Kay's productivity tool stack. Google Sheets is primary (migrated 2026-05-12 from Motion). Motion is being lapsed."
metadata: 
  node_type: memory
  type: user
  originSessionId: 03560fda-4372-4242-bb27-ca05145be53d
---

Kay's productivity tool stack (as of May 2026):
- **Weekly Google Sheets `TO DO M.D.YY`** (e.g., `TO DO 5.31.26`) in `To Do Archive` Drive folder — primary personal task tracker. Owned by the `task-tracker-manager` skill. Current week's sheet ID resolved dynamically via `scripts/tracker_sheet_resolver.py` (pointer + Drive-search fallback). See `project_personal_task_tracker.md` for full architecture and Sunday rollover ceremony.
- **Google Calendar** — recurring/scheduled items, external meetings.
- **OneNote** — repository-style lists and reference material.
- **Obsidian (brain/)** — knowledge graph, entities, call notes, decision traces.
- **Beads (`bd`)** — multi-step / multi-session engineering work, dependencies, agent task queue.

## Motion — lapsing, not active

Kay migrated off Motion 2026-05-12 (Excel-tracker era) → Google Sheets. Motion is no longer the primary task manager.

- **Status:** auto-renewal disabled (or to be disabled) in-app per `project_motion_cancellation_status.md`.
- **Paid term runs through 2027-03-10**, then lapses naturally.
- **Don't propose Motion task creation** — route every task action through the `task-tracker-manager` skill, which writes to the Sheet.
- **Don't cite the 30-day refund window** in any Motion correspondence (closed 2026-04-09).

## How to apply

- "Add a task" / "remind me to" / "put X on my list" → invoke `task-tracker-manager` `append` verb (auto-resolves current week's file via resolver). Never propose Motion.
- "Move X to {day}" / "schedule X for {day}" → `task-tracker-manager` `promote` or `schedule-to-day-slot` verb.
- Friday briefing task-tracker section → `task-tracker-manager` `report` verb.
- Sunday `goodnight` triggers the rollover (`archive-todo` → `archive`).
- If Kay references Motion as still-active in conversation, gently flag that the Sheet is the primary surface now; don't silently dual-write.

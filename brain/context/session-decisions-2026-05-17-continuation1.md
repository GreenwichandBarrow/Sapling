---
date: 2026-05-17
type: context
title: "Session Decisions — 2026-05-17 (continuation #1 — CONFLICTS with main 5/17 file)"
tags: ["date/2026-05-17", "context", "topic/session-decisions", "topic/task-tracker-rebuild", "topic/parallel-session-conflict", "status/conflict"]
---

# Session Decisions — 2026-05-17 (continuation #1)

> ⚠️ **PARALLEL-SESSION CONFLICT.** This session (continuation-1) and the
> session recorded in `session-decisions-2026-05-17.md` (continuation-2,
> commits `d8613e1`/`5e01423`/`1cce64e`) made **directly contradictory**
> architectural changes to the same live task tracker on the same day.
> The live sheet now contains BOTH outputs. Neither file overwrites the
> other; Kay must choose the winning model. See the conflict trace.

## Decisions (this session)

### Task tracker architecture (Socrates-driven, Kay-directed)
- **APPROVE** — Replace single Live Week grid with **Week planning tab + 7 permanent day tabs (Sun–Sat)**. Reached via `/socrates` convergence: week-at-a-glance overwhelm → calm single-day surfaces; Sunday plans in the Week tab; `distribute-week` fans into day tabs; no back-sync. Kay drove this explicitly and corrected the week-tab deletion herself mid-session.
- **APPROVE** — SSH fix: relaxed sshd `ClientAliveCountMax` 2→10 + VPS-side auto-tmux login hook (device-independent; cmux ≠ tmux).
- **APPROVE** — Surgical trim of `/goodnight` skills step (redundant with `evolve`; new-formalization scan kept).
- **APPROVE** — Whispr removed from tech stack (native macOS dictation; account cancelled).
- **APPROVE** — Ongoing ad-hoc to-do capture behavior codified.

### CONFLICT with continuation-2
- continuation-2 **APPROVED the opposite**: single `To Do` tab + Status/Horizon dropdowns, day tabs retired as `_retired_*`, "collapse thin boundaries." That session's commits are already on `origin/main`.

## Actions Taken (this session — all already in repo via 5/18 bookends; git clean)
- CREATED Week tab (sheetId 1062871087) + 7 day tabs; `build-week` reworked, `distribute-week` added; `build_day_tabs.py`, `build_week_tab.py`.
- CREATED `archive_May 11-17` (verbatim old grid), `archive_May 17`.
- UPDATED task-tracker SKILL.md, goodmorning.md, goodnight.md, project_personal_task_tracker.md to BOTH-surfaces model.
- CREATED memory: `reference_gog_interactive_unlock_recipe`, `feedback_ongoing_todo_capture_ask_placement` (latter also created by continuation-2 — overlap).
- SSH: sshd reaper relaxed, `~/.bashrc` auto-tmux hook added.
- Whispr removed from `dashboard/data/tech_stack.yaml` + infra mockup.

## Open Loops (BLOCKING — needs Kay)
- **Architectural conflict unresolved.** Live sheet has BOTH the Week+7-day-tab model AND the consolidated-To-Do model with `_retired_*` tabs. Kay must pick ONE. Whichever loses, its tabs need cleanup and the corresponding code/docs/memory reverted.
- Ask Harrison MCP still not installed (needs Kay's browser OAuth: `curl -fsSL https://client.dododigital.ai/install.sh | bash -s -- --targets claude-code`).

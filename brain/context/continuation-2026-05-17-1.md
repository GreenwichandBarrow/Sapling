---
date: 2026-05-17
type: context
title: "Continuation — 2026-05-17 #1"
saved_at: 2026-05-17T11:42:00-04:00
session_number: 1
tags: ["date/2026-05-17", "context", "topic/continuation"]
---

## Active Threads
- **Task tracker rebuild — COMPLETE & validated.** Single Live Week grid replaced by 7 permanent writable large-font day tabs (Sun..Sat). Migration ran, old grid + Today tab archived/deleted, recurring stamped, 9 G&B carryover items placed into this week's day slots. Ceremony tested end-to-end.
- **Ask Harrison MCP — NOT installed.** Installer needs interactive browser OAuth (Kay's whitelisted email). Command ready: `!curl -fsSL https://client.dododigital.ai/install.sh | bash -s -- --targets claude-code` then `/mcp`.
- **goodmorning briefing — deferred to fresh session** (this context too deep for the signal swarm).

## Decisions Made This Session
- SSH: relaxed sshd reaper + added VPS-side auto-tmux login hook (device-independent).
- Goodnight skills-update step trimmed (redundant with `evolve`; Harrison updated it on backend).
- Whispr removed from tech_stack.yaml + infra mockup (account cancelled, native Mac dictation set up).
- Ongoing ad-hoc to-do capture behavior codified to memory.
- Daily-tab tracker: Socrates → plan → built → migrated → tested.

## Next Steps
1. **TOP PRIORITY — fix design miss: restore the WEEK tab.** The rebuild wrongly DELETED the weekly planning tab. Corrected model is BOTH: a **Week tab = Sunday planning canvas (all 7 days visible)** → Kay lays out the full week there → a NEW **distribute step/verb pushes the completed week plan into the 7 day tabs** → Kay then works the daily tabs Mon–Sat. `build-week` must be reworked: instead of stamping recurring straight into day tabs, it (re)builds the Week planning tab + stamps recurring there; a new `distribute-week` verb fans the finalized week plan out to the 7 day tabs. Old week data is SAFE in `archive_May 11-17` (verbatim copy) — rebuild the Week tab structure from it. Do this FIRST in the fresh session, before /goodmorning.
2. Kay runs `/goodmorning` (after #1) → full briefing + week planning in Week tab → distribute → live in **Sun** day tab.
3. Optional: delete empty first-run `archive_May 17` artifact.
4. Kay runs the Ask Harrison MCP installer (browser step is hers).
5. Tonight `/goodnight` commits all uncommitted code/doc/memory changes.

## Open Questions
- ⚠️ `memory/project_personal_task_tracker.md` + `task-tracker-manager/SKILL.md` were updated to the WRONG day-tab-only model (no week tab). Fresh session must correct both to the Week-tab + day-tabs model before trusting them.
- Personal carryover (PSLF, GLP1, gift for Lois, bday cards, SLD video, modeling agencies) left in To Do backlog — Kay places into days as desired when living in day tabs.
- Confirm the 9 recommended G&B day placements suit her week (adjust via `move-day-item`).

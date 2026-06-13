---
name: session-checkpoint
description: Save and resume long-running Kay/DaVinci work sessions. Use for /savestate, /pickingback, "save state", "pick back up", "continue from where we left off", or when a long session needs a clean handoff. Preserves Claude-era continuation files without automatically committing or pushing unless explicitly requested.
---

# Session Checkpoint

This skill preserves the Claude-era `/savestate` and `/pickingback` contracts for Codex.

## Save State

Use when Kay asks to save state, pause, change computers, change chats, or keep a long workstream recoverable.

Create a continuation file:

`brain/context/continuation-YYYY-MM-DD-N.md`

Include:
- active threads / workstreams
- decisions made
- files changed or likely relevant
- next steps
- open questions
- blockers
- what not to redo
- any user preferences learned

Rules:
- Do not commit by default.
- If Kay explicitly says `--commit` or asks to commit, use `commit-steward`.
- Never push unless Kay explicitly approves pushing.
- Do not overwrite older continuation files.
- Keep the artifact concise enough to be useful on pickup.

## Picking Back Up

Use when Kay asks to resume, pick back up, or continue from saved state.

Steps:
1. Find the latest continuation file from the last 48 hours.
2. Read it with any current thread context.
3. Summarize:
   - where we left off
   - next recommended move
   - blockers
   - any decisions needed
4. Stop and wait if the next step changes scope or requires Kay's decision.

Rules:
- Do not re-run Good Morning.
- Do not mutate files just because a continuation file exists.
- Do not treat old continuation notes as more authoritative than newer user instructions.

## Success Criteria

The next Codex session can resume without Kay reconstructing the work from memory, and without accidental commits, pushes, or duplicated morning/evening routines.

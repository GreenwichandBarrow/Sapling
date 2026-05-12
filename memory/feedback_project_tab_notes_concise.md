---
name: project-tab-notes-concise
description: Project-tab Notes columns (Gantt tabs and project checklists) must be 1-line concise. NO memory file references, NO sheet IDs, NO doctrine attributions. The internal lens stays in Claude's head, not on Kay's UI.
metadata:
  type: feedback
---

## Rule

Notes on project tabs (`Deal Aggregator Expansion`, future Gantt or project-checklist tabs) are 1-line, plain-English descriptions of what the task is. They are NOT extensions of the personal task tracker's free-form Notes column.

**FORBIDDEN in project-tab Notes:**
- Memory file references (`per feedback_X`, `per project_Y`, `per user_Z`)
- Sheet IDs (`Sheet 18zzE1y-...`, `Doc 1gTQoC...`)
- Doctrine attributions (`per the Megan Lawlor pattern`, `per X memory`)
- Multi-sentence explanations
- Reasoning / rationale (belongs in Claude's head when populating, not in the cell)

**ALLOWED:**
- One-line task description in plain English
- Concrete action verbs (Confirm / Pull / Send / Verify / Decide / Build / Ask)
- The minimum information Kay needs to recognize what the row is asking for

## Why

Kay's project tabs are working surfaces. Verbose notes with memory-file names and sheet IDs:
1. Make scan-and-act expensive (Kay has to filter signal from internal-attribution noise)
2. Treat the project surface like Claude's working memory rather than Kay's
3. Confuse the personal task tracker conventions (where Notes can be richer) with the project surface (which is focused)

Precipitating trace: 2026-05-12 — when I populated the Deal Aggregator Expansion Gantt, Notes carried full memory-reference chains like "Per `feedback_marketplace_vs_broker_distinction`. Marketplaces (platforms): Axial (filter state in `project_axial_buyside_filter_state`)..." Kay flagged: "i dont want notes like this in here ... way too verbose, needs to be concise and to the point. this project list is not the tracker."

## How to apply

- Before writing any Notes cell on a project tab: ask "would Kay scan this and immediately know what to do?" If the cell needs decoding (memory file lookups, sheet ID resolution, doctrine cross-references), rewrite.
- Aim for 8-15 words per Notes cell. Truncate aggressively. Strip "per X" attributions entirely.
- If a Notes cell adds nothing beyond the milestone/task name, **leave it empty**. Empty is better than noise.
- For Claude's own working context (which memories/IDs apply), keep that mental note internal — it informs what I write, but doesn't appear in the cell.

## Distinct from tracker conventions

Personal task tracker (`TO DO M.DD.YY` Sheet, To Do tab) Notes column can be richer — references to inbox items, links to email, multi-line context. That's the tracker's Notes.

Project-tab Notes are TIGHTER. The project tab is a focused project plan, not a catch-all capture surface.

## Related

- `feedback_strip_user_context_from_public_copy` — internal lens-phrases (memory names, doctrine refs) don't go in surfaces Kay sees
- `feedback_no_state_paste_when_live_surface_open` — same family: don't add noise to surfaces Kay's actively using
- `feedback_decision_fatigue_minimization` — every word should reduce Kay's mental load

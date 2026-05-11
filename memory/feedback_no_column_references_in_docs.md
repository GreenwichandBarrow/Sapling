---
name: Never reference specific sheet columns in docs or guides OR conversation
description: All Kay-facing output (docs, guides, SOPs, AND conversation prose) must reference sheet fields by name/concept, not "Col K" or "Col V". Enforced by Stop-router handler no_column_letters.
type: feedback
originSessionId: c9463652-c8f2-4d3d-b096-737d00fef818
---
## Rule

Any output intended for Kay — Google Docs, call guides, SOPs, Slack messages to JJ/Sam, onboarding docs, **and the conversation itself** — must reference fields by their **name or concept**, not by column letter. Triangulate using the column **header name** plus a **row identifier** (row number or the row's primary entity).

- ✅ "the 1st Call Date field on row 4" / "the owner's name for Acme Pest"
- ❌ "Col K (Owner Name)" / "write it in Col V" / "Col T is empty this week"

**Escalation history:** 4/24 — graduated from memory-only to an enforced Stop-hook (`.claude/hooks/router/handlers/no_column_letters.py`, registered in `.claude/hooks/router/stop.py`). Kay flagged this as a repeat violation after 3+ sessions of Claude surfacing "Col T / Col V" in briefing output. The hook reads the last assistant message, strips code fences, and blocks the stop if a `[Cc]ol(umn)?s?\s*\.?\s*[A-Z]{1,2}\b` pattern survives.

**Why:** Columns can be reordered, inserted, or renamed as sheet schemas evolve. A guide that says "Col K" becomes actively wrong the moment we add a column in front of it — and the human reading the guide won't know. The concept ("owner's name") stays stable across schema changes.

**Scope:**
- ✅ **Concept-named in:** Google Docs, Call Guide, JJ/Sam Slack messages, onboarding docs, SOPs, deliverables
- ⚠️ **Column references OK in:** skill SKILL.md files, Python scripts, API integration code, stop hooks, anything machine-parsed — those need the exact column so they don't break. But even there, prefer a named constant (`OWNER_NAME_COL = "K"`) at the top so future renames are one edit.

**How to apply:** when drafting anything for human consumption, read it back and replace every "Col X" with the field's meaning. When drafting code, use a named constant so a future column move is a single-line change.

---
name: Subagent trigger is tool-call volume, not conceptual complexity
description: Delegate to subagent whenever a task requires 5+ tool calls of grunt work (download → parse → edit → verify → upload → confirm), regardless of how "small" it feels conceptually.
type: feedback
originSessionId: c9463652-c8f2-4d3d-b096-737d00fef818
---
## Rule

Spawn a subagent whenever a task requires **5+ tool calls of mechanical work** (file downloads, format conversions, write-and-verify loops, API loops). The trigger is **volume of grunt-work tool calls**, not the conceptual size of the change.

## Why

On 2026-04-20 Kay greenlit a one-pager update with 3 specific text edits to a PPTX. It felt small — "just 3 fields" — so I started doing it in the main context. Kay correctly called it out: PPTX editing requires download → parse with python-pptx → edit runs → save → upload → verify → locate Drive folder. That's 6-10 tool calls of grunt work that:

1. Bloats main context with format-conversion output
2. Distracts me from orchestration / judgment work she actually needs the main context for
3. Could have been run in parallel while I answer her other questions
4. Directly violates CLAUDE.md's "You do NOT do the grunt work" rule

## How to apply

Before starting mechanical work, count the tool calls you'd need:

- File download → 1
- Parse / extract text → 1
- Edit with library (python-pptx, openpyxl, etc.) → 2-3 (load, manipulate, save)
- Verify → 1
- Re-upload → 1
- Post-upload metadata check → 1

**6+ calls → spawn a subagent.** Single sheet read + single cell update (2 calls) → do it yourself. PPTX/XLSX/DOCX edits → subagent, always.

Other grunt-work patterns that should auto-trigger subagent:
- API loops (more than ~5 iterations)
- Sheet mass writes (more than 10 rows)
- Binary format manipulation (PPTX, XLSX, DOCX, PDF)
- Enrichment tasks (Apollo/Linkt/web-research chains)
- Snapshot-then-modify workflows (by definition multi-step)

## Counter-examples (where direct is fine)

- Single Google Doc find-replace (1-2 calls) — direct
- Single Slack send (1 call) — direct
- Single sheet row read + 1 cell update (2-3 calls) — direct
- Quick git commit (2 calls) — direct

## Related rules

- `feedback_chief_of_staff_role.md` — high-level framing
- CLAUDE.md "Role: Chief of Staff" section — the canonical source
- `feedback_subagent_sheet_write_safety.md` — what to brief subagents on

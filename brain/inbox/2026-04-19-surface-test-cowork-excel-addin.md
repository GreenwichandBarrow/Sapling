---
schema_version: 1.0.0
date: 2026-04-19
title: "Surface test plan — Cowork vs Claude Code; Excel add-in vs openpyxl"
status: backlog
source: manual
urgency: normal
automated: false
tags: [date/2026-04-19, inbox, source/manual, urgency/normal, topic/surface-test, topic/cowork, topic/excel-addin, topic/system-improvement]
---

## Description

**Source:** 2026-04-19 Anacapa deck analysis (Harry Liu, Going Deeper with Claude, Apr 17 2026), Lesson 6. We do all G&B work in Claude Code today. Different tasks map to different Claude surfaces (Chat/Cowork/Code). Worth empirically testing whether Cowork or Excel add-in produce better outputs for specific tasks before migrating any skill.

### Hypothesis

1. **File deliverables** (investor updates, meeting briefs, board-style decks) → Cowork may produce cleaner files because it's designed to write deliverables.
2. **Spreadsheet ops** (budget reconciliation, scorecard generation, financial modeling) → Excel add-in (beta as of April 2026) may replace openpyxl with native .xlsx editing.

### Test 1 — Meeting brief: Code vs Cowork

Next meeting brief Kay has scheduled: generate TWICE, once in Claude Code (current workflow) and once in Cowork. Same skill, same inputs.

**Measured:**
- Time to generate (wall clock)
- Format consistency with G&B brand (Avenir, black text, centered logo per feedback_doc_formatting)
- How many formatting fixes Kay makes before shipping
- Kay's preference rating 1-10

**Decision criterion:** If Cowork wins on ≥2 of {time, format fidelity, fewer edits}, migrate meeting-brief to Cowork as primary surface.

### Test 2 — Budget reconciliation: openpyxl vs Excel add-in

Next monthly budget reconciliation (first Friday after Anthony delivers P&L): run existing budget-manager Python workflow, then redo using Claude Excel add-in. Same inputs.

**Measured:**
- Native Excel formulas vs broken formulas
- Ability to produce charts/pivots
- Whether Kay can edit output live without breaking it

**Decision criterion:** If Excel add-in produces working native formulas, cleaner formatting, and survives Kay's direct edits, migrate budget-manager to Excel add-in as primary engine.

### Prerequisites

- Cowork: already installed on Kay's Mac (part of Claude Desktop)
- Excel add-in: verify beta access in Kay's Anthropic org settings. If not, request via Anacapa contact.

### Timeline

- Test 1 trigger: next meeting brief needed
- Test 2 trigger: first Friday after Anthony's next P&L delivery
- Report back: append findings to this file, decision logged in next session-decisions

### Notes

Both surfaces use the SAME underlying `.claude/skills/{skill}/` folder per Harry ("One folder → works in Cowork and Claude Code"). Testing the surface, not the skill logic. Don't invent work to trigger tests — use real upcoming tasks.

## Notes

*Not started*

## Outcome

*Pending*

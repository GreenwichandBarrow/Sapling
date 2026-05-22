---
schema_version: 1.1.0
date: 2026-05-18
review_status: applied
type: trace
title: "Conference auto-archival: passed Evaluating rows = assume Skip; Pipeline→Skipped needs schema projection"
trace_type: workflow-rule
tags: ["date/2026-05-18", "trace", "topic/conference-discovery", "topic/conference-pipeline", "topic/schema-projection", "status/closed"]
---

# Conference auto-archival: passed Evaluating rows = assume Skip; Pipeline→Skipped needs schema projection

## Trigger

[[Conference Pipeline]] Skipped tab had 10 rows (39–48) visibly column-shifted — "Skip" under *Location*, dates under *Event Name*. Root cause: rows were appended verbatim from the Pipeline tab (16-col schema, leading `Week Of` + `Decision` in C) into the Skipped tab (14-col schema, no `Week Of`, `Decision` in M). Separately, the 5/11–5/15 week had passed (today 5/18) with all 11 rows still `Decision = Evaluating` (no final call).

## Decision

1. **Pipeline ≠ Skipped/Attended schema — projection is mandatory.** Auto-archival must map Pipeline cols → destination 14-col schema (B→A date, D→B event, C→M decision, drop `Week Of`/`Registration Paid`), never append the raw row. Codified as a MANDATORY Column-Mapping table + forbidden-pattern + post-move assertion in both `conference-discovery/SKILL.md` and `headless-sunday-prompt.md`.
2. **Passed + `Evaluating` + no Decision = assume Skip** (Kay's explicit rule). Archive to Skipped with `Decision=Skip`; do NOT leave in Pipeline waiting, do NOT treat as Attended.

## Alternatives Considered

- **Leave passed Evaluating rows in Pipeline** — rejected by Kay; a passed conference with no decision is a de-facto skip, Pipeline should hold only future/actionable rows.
- **Mark passed Evaluating as a new "Lapsed" status** — rejected: agent-invented statuses are forbidden; `Skip` is the existing terminal that fits.
- **Fix only the live rows, not the skill** — rejected: the scheduled Sunday run would recreate the shift every week (it appends via the same path).

## Reasoning

The column-shift was invisible to the row-count validator (row count was within tolerance) — only schema-aware projection prevents it. The headless prompt is what the scheduled job actually executes, so the rule had to live there too, not just in SKILL.md. "Assume Skip for passed-undecided" keeps the Pipeline tab a clean future-only queue without forcing Kay to retro-decide dead conferences.

## Why This Trace Matters

A future agent doing conference auto-archival will, by default, copy whole Pipeline rows (the obvious move) and silently corrupt the Skipped/Attended tabs. And without the explicit rule it would either leave passed-undecided rows cluttering Pipeline or wrongly infer attendance.

## Key Insight

Cross-tab moves are schema projections, not row copies, whenever source and destination schemas differ. And "no decision before the date passed" is itself a decision: Skip.

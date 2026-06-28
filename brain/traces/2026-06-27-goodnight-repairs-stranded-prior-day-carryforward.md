---
schema_version: 1.2.0
date: 2026-06-27
type: trace
tags: [date/2026-06-27, trace, pattern/task-carry-forward, status/pending]
importance: high
target: skill:goodnight-closeout
---

## Context
Kay skipped Friday goodnight and Saturday good morning, then started Saturday night goodnight. The default closeout path initially checked only Saturday -> Sunday, which missed 49 incomplete Friday tasks still stranded on the Friday tab.

## Decisions
### Goodnight repairs stranded prior-day carry-forward after missed bookends
**AI proposed:** Treat Saturday night as ordinary Sat -> Sun carry-forward because Saturday had no incomplete items.
**Chosen:** Sweep the stranded Friday tab into Sunday because both the Friday goodnight and Saturday good morning were missed.
**Reasoning:** The operating need is next-day readiness, not literal current-date movement. When both bookends are missed, goodnight must detect and repair earlier live-day carry-forward gaps before closing the day.
**Pattern:** #pattern/task-carry-forward

---
schema_version: 1.1.0
date: 2026-06-19
type: trace
task: Restructure Good Morning brief format
had_human_override: true
review_status: pending
importance: high
target: skill:pipeline-manager
tags: [date/2026-06-19, trace, status/pending, topic/good-morning, source/pipeline-manager]
---

# Good Morning Brief Restructure

## Context
Kay revised the Good Morning brief format so it becomes the daily operating edit surface, while the dashboard remains the reference point after morning decisions are handled.

## Decisions

### Collapse subsection labels into numbered action lines by default
**AI proposed:** Use separate indented subsection rows under each dashboard section.
**Chosen:** Use `N. **Subsection:** item` when there is only one item in that subsection; expand subsections only when there are 2+ separate decisions.
**Reasoning:** Separate subsection rows made the brief look longer without adding decision value. Kay needs fast reference numbers and a compact review surface.
**Pattern:** #morning-brief-edit-surface

### Keep content scope, change routing
**AI proposed:** Removing sections could have implied dropping old Good Morning content.
**Chosen:** Treat the change as restructuring, not reduction: email, pipeline, deal aggregator, brief prep, health failures, and task-manager/M&A work all remain, but route to the new sections.
**Reasoning:** The failure mode to avoid is losing useful signals because the presentation changed. The new layout should reduce friction while preserving coverage.
**Pattern:** #preserve-signal-while-restructuring

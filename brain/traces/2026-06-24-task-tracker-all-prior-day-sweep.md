---
schema_version: "1.1.0"
date: 2026-06-24
type: trace
tags: [date/2026-06-24, trace, client/greenwich-and-barrow, topic/task-tracker, topic/goodmorning, status/applied]
had_human_override: true
importance: high
target: skill:goodmorning
applied_to: [".agents/skills/goodmorning/SKILL.md", ".agents/skills/task-tracker-manager/SKILL.md", "scripts/task_tracker.py"]
---

## Context

During Good Morning repair, only Tuesday-to-Wednesday carry-forward ran. Kay then noticed Monday tasks were still stranded on the live tracker.

## Decisions

### Sweep all prior live day tabs, not just yesterday
**AI proposed:** Treat the missed carry-forward as a prior-day repair problem.
**Chosen:** Good Morning must sweep every earlier live day tab in the current week into the current day, earliest first, and report must include overflow rows above `NOTES`.
**Reasoning:** Missed Good Night runs and prior repair gaps can leave older day tabs active. A yesterday-only check falsely clears the system while Monday/Sunday rows remain operationally live.
**Pattern:** #pattern/carry-forward-all-prior-days

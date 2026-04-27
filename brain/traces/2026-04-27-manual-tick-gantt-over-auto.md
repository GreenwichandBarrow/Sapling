---
schema_version: 1.1.0
date: 2026-04-27
type: trace
today: "[[notes/daily/2026-04-27]]"
task: Chose manual-tick Gantt over auto-formatting Gantt for personal Excel task tracker
had_human_override: true
importance: medium
target: scripts/build_tasks_excel.py — build_gantt_project_tab function, future per-project tab seeds
tags: [date/2026-04-27, trace, topic/personal-task-tracker, topic/design-philosophy, pattern/manual-over-auto-in-personal-tools, domain/tooling]
---

# Decision Trace: Manual-tick Gantt over auto-formatting Gantt

## Context

Building [[outputs/to-do-4-26-26-xlsx|TO DO 4.26.26.xlsx]] for Kay, the per-project Gantt tabs needed a timeline visualization. My first instinct: have Kay enter Start + Target dates per milestone, then conditional-formatting auto-fills the timeline cells between those dates with the entity color. This is the standard Excel-Gantt pattern.

Kay's redirect: *"maybe for the gannt chart, the boxes under the dates have check mark boxes, so that if you check the cell becomes highlighted that mid level green so wheneverything is checked it will show like a gantt chart."*

Each timeline cell becomes a manual checkbox. Tick a contiguous run of weeks, the row builds into a bar visually. No date math driving the bar.

## Decision

Replaced auto-format with manual checkboxes. Each week-cell defaults to ☐ with status dropdown. Conditional format: if cell = ✅, fill entity color. Start/Target columns kept as planning reference but no longer drive the bar.

## Alternatives Considered

1. **Auto-format from Start/Target dates (original plan)** — entry once per milestone, bars draw themselves. Rejected by Kay.

2. **Hybrid: auto-fill from dates AND allow manual override** — gives the best of both. Rejected: complexity nobody asked for; Kay's gesture was clear.

3. **Manual checkboxes, no Start/Target columns at all** — simpler. Rejected: the date columns are still useful as planning reference even when not driving the bar.

4. **Manual checkboxes, kept Start/Target as reference (chosen)** — minimal code, preserves Kay's mental model, lets her drive the visual herself.

## Reasoning

- Personal tooling is about *gesture* — Kay wants to feel her progress, not have it computed for her. Auto-formatting pushes the user into a passive role.
- The same pattern showed up earlier in the session: she wanted the priority checkbox NEXT TO the task (not above), wanted to manually tick habits each day (not pre-computed adherence). Consistent preference for manual interaction.
- Instagram-template aesthetic she liked (the donuts, the per-day tracker) is also manual-tick. The template's appeal IS the act of checking, not the computed output.
- Auto-formatting also hides the underlying state — when it doesn't behave as expected, the user can't easily see why. Manual ticking is transparent.

## Why This Trace Matters

Future agent building any per-Kay personal tool (planner, habit tracker, journal template, dashboard) will instinctively reach for auto-computed displays. They look impressive and require less user effort. Don't. For Kay's personal artifacts, **default to manual gesture over auto-computation**. Save the auto-magic for operational systems (deal pipeline, briefings, snapshots) where Kay is the *consumer* not the *operator*.

## Key Insight

The pattern: in Kay's *personal tools* (where she is the operator), prefer manual interaction so she owns the gesture. In Kay's *operational systems* (where she is the consumer), prefer automation so she doesn't carry the load. Same person, opposite default depending on her role at the surface.

---
schema_version: 1.1.0
date: 2026-05-01
type: trace
title: "openpyxl DoughnutChart objects render blank on Excel-Mac — use cell-based % display"
tags: ["date/2026-05-01", "trace", "topic/excel-tooling", "topic/personal-task-tracker", "domain/technical", "had_human_override"]
importance: medium
target: skill:task-tracker-manager
---

# openpyxl DoughnutChart on Excel-Mac

## Context

Kay's TO DO 4.26.26.xlsx was built 2026-04-26 with seven `openpyxl.chart.DoughnutChart` objects on the This Week tab, one per day. They were intended as visual progress rings with `holeSize=65` and per-DataPoint solid fills (sage-dark for done, light-grey for open). The donuts referenced helper data in hidden rows Q99:S107.

Kay reported 2026-05-01 that "the graphs are not working" — the donuts render blank or as empty boxes when she opens the file in Excel-Mac.

## Decisions

### Donut visualization fix path

**AI proposed:** Three options — (A) cell-based "donuts" using 8-cell circle of conditional-formatted blocks driven by % done, (B) generate chart natively in Excel, save as template, script `xltx` injection, (C) replace donuts with single big % per day, no chart engine.

**Chosen:** **Path C** — delete all DoughnutChart objects from worksheet (set `ws._charts = []`), promote the per-day % formula into the now-freed merged anchor cells at rows 17-21, render at 36pt bold sage-dark font.

**Reasoning:** The per-day % already existed at row 22 of the file as a text formula. Path C is structurally simplest, fully Excel-Mac compatible (no chart objects = no compatibility surface), still informative, and reclaims visual real estate by putting the big number where the donut anchor was. Path A requires per-cell conditional-formatting choreography that's brittle. Path B requires manual Excel intervention which breaks the rebuild-from-script principle. Charts produce no value here — the % alone tells Kay what she needs.

**Pattern:** When openpyxl-generated chart objects misbehave in Excel-Mac, default to cell-based rendering, not deeper chart-spec debugging. The OOXML chart serialization gap between openpyxl and Excel-Mac is a known, durable problem; not worth fighting.

## Why this trace matters for future agents

A future agent looking at the file might see "this had donuts originally" and try to re-add them via openpyxl. **Don't.** They will render blank again. The decision is permanent: cell-based percentages only.

This generalizes beyond this file: any Claude-built xlsx that targets Kay's Excel-Mac workflow should avoid openpyxl chart objects entirely. Bar charts, line charts, pie charts — all have the same OOXML serialization gap. If a chart is genuinely needed, generate the file with formula-driven cell visualizations (sparklines via REPT(), heatmaps via conditional formatting, gauges via merged-cell calculations) instead.

## Key insight

**openpyxl's chart engine is a one-way trip into incompatibility.** It writes spec-compliant OOXML, but Excel-Mac's renderer rejects subtle attribute combinations (`holeSize`, per-point graphical properties, transparent backgrounds). The gap is not Claude's to close. Architect xlsx outputs around it.

## How a future agent should apply

- When building or maintaining xlsx for Kay's workflow: never instantiate `openpyxl.chart.*` objects.
- Use formula-driven cells, conditional formatting, and font sizing to convey state.
- If Kay specifically requests a chart, surface this trace and ask whether cell-based equivalent is acceptable before falling back to openpyxl chart objects.
- The `task-tracker-manager` skill's `reformat` verb permanently strips chart objects on every run — this is a feature, not a bug.

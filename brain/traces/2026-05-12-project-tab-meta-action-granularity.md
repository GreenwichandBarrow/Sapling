---
date: 2026-05-12
type: trace
title: "Project tab items describe meta action, not per-instance enumeration"
tags:
  - date/2026-05-12
  - trace
  - topic/project-tab-design
  - topic/task-granularity
  - topic/task-tracker
  - topic/checklist-format
schema_version: 1.1.0
---

# Project tab items describe meta action, not per-instance enumeration

## Trigger

When scoping the Deal Aggregator Expansion project, Claude initially proposed ~80 granular items split across 15 sections — including 21+ items for "Marketplace Audit" (one row per platform: Confirm Axial, Confirm Flippa, Confirm BizBuySell, etc.).

Kay corrected: "ALL OF THOSE MARKETPLACES SHOULD BE LISTED IN THIS SOURCING LIST IN THE STRUCTURE WE ALIGNED ON, THEN WE SHOULD START INDICATING THEIR STATUS BUT THE LIST BY MARKETPLACE DOES NOT GO INTO THE PROJECT TAB. THE PROJECT SHOULD BE - DO FULL INVENTORY ASSESSMENT OF MARKETPLACE LIST IN SOURCING LIST"

Generalizing the principle (after subsequent "DONT LIST OUT EVERY COLUMN THAT NEEDS TO CHANGE"): project items describe META action, not per-step or per-instance implementation.

## Decision

Project-tab task names describe the META action only.

- ✅ "Full inventory assessment of marketplace list in Sourcing List" (one item)
- ❌ 21 items, one per platform (Confirm Axial, Confirm Flippa, ...)

- ✅ "Update Sourcing List structure as newly aligned" (one item)
- ❌ "Add Listings Scanned column / Add Near-Misses column / Add Funnel Entries column / Add Entry Rate column / Add Last Reviewed column" (5 items)

- ✅ "Build broker-channel dashboard tile" (one item)
- ❌ "Build broker-channel dashboard tile (# sent / # replies / # CIMs / # active deals)" (parenthetical detail)

Per-row work belongs in the source list/sheet where each row has its own status columns. Per-column or per-step implementation belongs in the work itself, not the project tracker.

## Alternatives Considered

1. **Granular (~80 items)** — every concrete step / per-platform check listed. (My initial proposal; rejected.)
2. **Meta-action only (~17 items)** — one item per coherent unit of work; per-instance work pushed to source surfaces. (Adopted.)
3. **Hybrid with section-header rows + indented sub-tasks** — preserves both layers. (Considered; rejected as visual clutter and against Kay's "I don't want big milestones" pushback.)

## Reasoning

The project tab is for tracking META PROGRESS on coherent units of work. The Sourcing List (or any source list) has its own status columns for per-row tracking. Replicating per-row work as per-row items on the project tab:
- Duplicates the surface (Sourcing List sheet is already the canonical list of marketplaces)
- Defeats compaction (the project tab balloons; Kay can't scan it)
- Locks specific implementation steps into the project plan, making it brittle when the work approach changes

Kay's mental model: project tab = "what coherent units of work do we need to do?"; source list = "what's the per-instance status of each thing?". Mixing the two layers is the failure mode.

Subsidiary rule (from same session): no parenthetical column lists or implementation-detail enumerations in the task description. If detail is needed for context, it goes in the Notes column — and even there, stays concise.

## Why This Trace Matters

A future agent scoping a project plan will default to granular task enumeration because it pattern-matches "be specific, capture every step." That default fails Kay's project tab because the per-step granularity is duplicated by the source list's per-row tracking.

Decision rule for future use:
- If work is per-row in another sheet/list → project tab item is the META action ("Full hygiene pass on Intermediary Target List", "Update latest status of marketplaces in Sourcing List").
- If work is a coherent unit not naturally tracked elsewhere → project tab item is the unit ("Build dashboard tile", "Send 50 broker email batch").
- NO parenthetical enumeration of implementation steps in the task description. Notes column gets one-line concise context only (per `feedback_project_tab_notes_concise`).

## Key Insight

Two layers of tracking: project tab (meta progress on units of work) and source lists (per-instance status). Pushing per-instance work UP to the project tab confuses the layers and overwhelms the tracker. The fix is structural, not stylistic — keep the layers separate, let each surface own its own granularity.

---
date: 2026-05-12
type: trace
title: "Channel-based Drive sub-organization (not function-based) inside OPERATIONS"
tags:
  - date/2026-05-12
  - trace
  - topic/drive-organization
  - topic/folder-architecture
  - topic/buy-box
  - topic/sourcing-channels
schema_version: 1.1.0
---

# Channel-based Drive sub-organization (not function-based) inside OPERATIONS

## Trigger

Kay flagged "I'm getting a list lost in the organization of documents related to this" — buy boxes in one folder, sourcing list in another, target lists in a third, intermediary lists scattered across two duplicate folders. Asked: how to better organize?

## Decision

Reorganize `OPERATIONS/` by **channel** (PROPRIETARY SOURCING vs INTERMEDIARY SOURCING) rather than by **function** (single BUY BOX folder, single OUTREACH folder, single SOURCING LIST folder).

Final structure inside OPERATIONS:
- `PROPRIETARY SOURCING/` — BUY BOX (proprietary), TARGET LISTS, COLD CALLING (was JJ), EMAIL & LINKEDIN/DEALSX
- `INTERMEDIARY SOURCING/` — BUY BOX (broker), SOURCING LIST, INTERMEDIARY TARGET LIST, PREP DOCS
- `CONFERENCES/` lives in Kay's view-only RESEARCH (cross-channel)

## Alternatives Considered

1. **Function-based** — single BUY BOX folder containing both broker + proprietary; single OUTREACH folder containing both target lists + intermediary; single SOURCING LIST folder. (My initial proposal.)
2. **Hybrid with shortcuts** — channel folders cross-reference function folders via Drive shortcuts. (Considered, dismissed as confusing.)
3. **Audience-only (current state pre-restructure)** — leave it scattered, just clean up duplicates. (Rejected — addresses symptoms, not the underlying friction.)

## Reasoning

The function-based proposal seemed cleaner on paper (one BUY BOX, one OUTREACH) but Kay's correction surfaced the deeper truth: **the two buy boxes are genuinely different documents.**

- Proprietary buy box: niche-specific (per active niche), tristate region, $2-10M EBITDA, services-focused
- Broker buy box: industry-agnostic, geography internal-only, $2M EBITDA floor, opportunistic

When the broker channel email batch is being executed, the operator needs the broker buy box. When the proprietary cold-calling is being executed, the operator needs the proprietary buy box. Co-locating both in one folder means EVERY workflow step requires "which one applies to me right now?" filtering — friction at the wrong layer.

Same logic propagates: proprietary target lists co-locate with proprietary buy box; intermediary target list co-locates with broker buy box; sourcing list (which tracks ALL marketplaces + broker channels — all intermediary in nature) co-locates with intermediary.

The function-based grouping treats all "buy boxes" as one CATEGORY of asset; the channel-based grouping treats each channel's full toolkit as one COHESIVE WORKFLOW SURFACE. Workflow cohesion wins over asset-category cleanliness.

## Why This Trace Matters

A future agent reorganizing files for any multi-channel operation (sourcing, outreach, etc.) will default to function-based grouping because it pattern-matches "one canonical home per asset type." That default is wrong when the same asset TYPE has materially different INSTANCES per channel. Channel-based grouping is the right pattern when (a) instances genuinely differ per channel AND (b) workflows execute within a single channel at a time.

Decision rule for future use:
- If asset type has ONE canonical instance shared across channels → function-based grouping (one folder).
- If asset type has materially different per-channel instances → channel-based grouping (one folder per channel containing that channel's instance).

## Key Insight

"The buy boxes are now different" was the unlocking observation. The structural decision flows from the document-content reality, not from architectural taste. If the two buy boxes had been the same document with channel-tagged sections, function-based would have been correct.

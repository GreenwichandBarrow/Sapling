---
schema_version: 1.1.0
date: 2026-04-24
type: trace
title: "Merged Tech Stack page into Infrastructure"
tags: [date/2026-04-24, trace, topic/dashboard, topic/architecture, topic/redundancy]
people: []
companies: []
---

# Merged Tech Stack page into Infrastructure

## Decision

Collapsed the planned 7-section Command Center IA into 6 sections by merging the Tech Stack page into Infrastructure. Tech Stack's three sub-sections (Connectivity Canary, Credits & Trends, Reference List) became Zones 2, 3, and 5 of Infrastructure.

## Why this is a non-obvious choice

The original scope doc (committed 2026-04-24 AM) had Tech Stack as a separate sidebar entry with the explicit rationale: "External-dependency connectivity canary + credit balances + subscription cost variance." That looked clean on paper. The boundary felt distinct: Infrastructure = local/system, Tech Stack = external services.

In practice the boundary collapsed because:
- The Infrastructure "Tooling Operational Status" zone (which we'd just added in this session for the 11 shared tools that previously lived under C-Suite & Skills) was checking auth, API keys, and rate limits — exactly what Tech Stack's "Connectivity Canary" was specced to do.
- Several entries appear in both surfaces: gogcli=gog, github=gh CLI, motion=API. Having two pages with overlapping data forced a "where do I look?" question every time.
- A future agent looking at the scope doc would see the original Tech Stack page intent and might rebuild the split — even though the two pages answer the same operational question with different vocabulary.

## What a future agent might do differently without this trace

Build separate pages because the scope doc's original IA looked authoritative. Result: split mental model, duplicate data, sidebar bloat.

## Litmus

Kay's exact reaction after the merge: "wow I love infrastructure now." Validated. Memory captured at `memory/feedback_collapse_thin_boundaries.md` so the heuristic — "if two pages share thin boundaries, recommend merge before coding" — is reusable on the next dashboard or internal-tool design.

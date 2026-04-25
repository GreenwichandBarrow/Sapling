---
schema_version: 1.1.0
date: 2026-04-24
type: trace
title: "Active Deal Pipeline rescoped to NDA-forward only"
tags: [date/2026-04-24, trace, topic/dashboard, topic/pipeline, topic/dealsx]
people: []
companies: []
---

# Active Deal Pipeline rescoped to NDA-forward only

## Decision

Renamed "Deal Pipeline" → "Active Deal Pipeline" and dropped the Identified + Contacted columns. New page is a 4-column Kanban (NDA → Financials Received → Submitted LOI → Signed LOI) plus a closed strip filtered to post-NDA failures only. Outbound funnel data (Identified + Contacted counts, channel split, reply rates, conversion to NDA) moves to M&A Analytics.

## Why this is a non-obvious choice

The original scope (and the Streamlit page shipped Session 3) had a 6-column Kanban mirroring Attio's full pipeline. That made sense when the Identified+Contacted columns held tens of warm targets. With DealsX scaling cold outreach to thousands per week, those columns were on track to become 2,000-card visual noise — a mental model that conflates "we sent emails to a list" with "we are in active conversation."

Kay caught this forward-looking: "now dealsx is doing our list building and there will be thousands identified & contacted I wonder if this is really 'active deal pipeline' and it starts with NDA."

The rescoping is anchored on a sharper definition of "active": mutual engagement (NDA signed forward = real conversation, financials, LOIs). Identified + Contacted are inventory and outreach attempts, not pipeline.

This is a forward-looking architectural call. Today there are 0 deals NDA-forward and 18 in pre-NDA (the page would render mostly empty). But the design choice is for the page Kay needs in 8 weeks when DealsX is at full scale, not the page that demos best today.

## What a future agent might do differently without this trace

Re-add the Identified + Contacted columns because they're in the Attio data and "Pipeline" sounds inclusive of all stages. Result: Kanban becomes a useless wall of cold outreach cards, defeating the purpose of having a pipeline tracker.

## Side-effect

The closed-lifetime number drops from 131 (all Attio closures, mostly cold-outreach attrition) to ~12 (post-NDA failures only) — the meaningful "deals we lost after real engagement" number. Far more useful for retrospective.

## Litmus

Trigger to revisit: if Kay or a future stakeholder asks "where do I see the cold outreach numbers?" the answer is *M&A Analytics outbound funnel*, NOT the Pipeline page. If that referral consistently feels wrong, the merge would need to be re-litigated. Until then, hold scope.

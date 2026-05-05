---
schema_version: 1.1.0
date: 2026-05-04
type: trace
title: "Cold-list engagement = two-way correspondence; outbound-only with no reply doesn't count"
trace_type: doctrine-refinement
tags: ["date/2026-05-04", "trace", "topic/cold-list-engagement-rule", "topic/intermediary-pipeline", "topic/calibration-refinement"]
---

# Cold-list engagement = two-way correspondence; outbound-only with no reply doesn't count

## Trigger

After the engagement-classification subagent removed 16 firms from the Intermediary Target List (rows where Attio interactions data showed prior emails or calls), Kay flagged Transworld of NY (Sam Curcio): the row had been kept by the subagent, but the validation artifact noted G&B emailed nyc@gdt.tworld.com on 2026-04-30. Per the original engagement rule (`feedback_cold_list_attio_engagement_rule` — initial form: "Attio Company record exists, prior email or call → REMOVE"), that 4/30 outbound should have triggered REMOVE. Kay's response: "keep transworld, they never wrote me back."

This contradicted Kay's earlier in-session decision on Choate Hall & Stewart (which had a 14-month-stale email thread but was REMOVED per strict rule). The contradiction surfaced a hidden distinction the rule hadn't captured: outbound-only vs. two-way.

## Decision

Refined the cold-list engagement rule: **engagement = two-way correspondence** (received reply / call logged / meeting held). One-way outbound emails with no response do NOT count as engagement; the row stays on the cold list as still-cold.

Concrete calibration examples captured in the refined memory:
- **Choate Hall & Stewart** — strong two-way email thread that went stale 14 months ago → REMOVE (engagement existed, just dormant)
- **BDG-CPAs** — single Nov 2025 outbound, no reply → KEEP (one-way ping, no engagement)
- **Transworld of NY (Sam Curcio)** — single 4/30 outbound, no reply → KEEP (one-way ping, no engagement)
- **Live Oak / Goodwin / Plexus / Heritage / Bellizio** — active two-way threads with logged meetings → REMOVE

Updated `feedback_cold_list_attio_engagement_rule.md` to lead with the two-way nuance in the rule statement, with the four canonical examples in the body.

## Alternatives Considered

1. **Keep the strict rule (any prior email = REMOVE)** — what the engagement-classification subagent applied. Rejected because it strips legitimate cold-re-engageable contacts where the first attempt didn't land.
2. **Add a staleness carve-out (any email older than N months = treat as cold again)** — what I floated for Choate. Kay rejected by REMOVING Choate (because Choate had real two-way history, just dormant) — staleness alone isn't the right boundary; bidirectionality is.
3. **Per-firm judgment** — what I'd been doing on the 3 ambiguous cases (NYBB / Choate / BDG). Doesn't scale; future runs re-litigate.

## Reasoning

The point of a cold list is to track contacts G&B hasn't formed a relationship with yet. A one-way outbound email is an attempt that didn't land — no relationship was formed, the contact remains cold. Removing it from the list would lose the re-engagement candidate (and Apollo wouldn't re-enrich it because it'd no longer be on the list).

Two-way correspondence (or a logged call/meeting) means a relationship exists in some form, even if dormant. Those belong in Attio's relationship-management surface, not on the cold-outreach list.

The Apollo enrichment pipeline benefits from the refined rule: it focuses credits on actually-cold contacts (no reply yet) instead of wasting credits re-enriching firms where a relationship already started.

## Why This Trace Matters

Without this refinement, the engagement-classification subagent would over-strip cold lists every time it runs. The 16 firms removed today were largely correct — they had documented two-way engagement (logged meetings, multi-email threads, "Very Strong" strength scores). But borderline cases (firms with weak Attio records and only outbound history) were over-removed. The Transworld correction caught one such case after-the-fact; the refined rule prevents the next pass from making the same error.

A future `relationship-manager` or `outreach-manager` skill update should reference this rule when designing automation that touches cold-list rows.

## Key Insight

**The boundary between "cold contact" and "active relationship" isn't "any past contact attempt" — it's "any past two-way exchange."** This distinction matters because:
- Outbound-only attempts that didn't land are still legitimate re-engagement targets (different angle, different sender, different timing might work)
- Two-way exchanges create a relationship surface that belongs in CRM (Attio), even if dormant
- Apollo enrichment economics depend on this — re-enriching firms with established relationships wastes credits

Same logic likely applies to other "have we engaged with X" questions across the system (warm-intro detection, nurture cadences, dropped-ball scans). Anywhere "prior contact" is a gating signal, refine to "prior two-way contact."

---
schema_version: 1.1.0
date: 2026-05-01
type: trace
title: "Free VRA / pre-sale audit / valuation gesture from M&A advisor = sell-side prospecting, NOT warm-intermediary signal"
tags: ["date/2026-05-01", "trace", "topic/intermediary-classification", "topic/buy-side-discipline", "domain/sales", "had_human_override"]
importance: high
target: skill:relationship-manager
---

# Sell-side advisor "free tool" pattern

## Context

Bob Williamson, Pest & Lawn director at Cetane Associates (M&A advisory firm), met Kay in person at NJPMA workshop 2026-04-29. Sent Kay a VRA (Value Range Analysis) sample on 4/30 with offer of a free Value Range Analysis. Email-intelligence skill 2026-05-01 surfaced as an actionable "warm intermediary follow-up" (Inbox item, recommended a 20-min intro-call ask).

## Decisions

### Classify the VRA gesture

**AI proposed (initial):** Treat as warm-intermediary signal. Bob is a pest-specialist M&A advisor; Kay's active niche is pest management; he sent a sample after meeting in person. Recommend warm reply proposing a 20-min intro call.

**Kay overrode:** Cetane is **sell-side** advisory. The free VRA is a sell-side prospecting tool — the advisor offers a free valuation to OWNERS thinking about selling, hoping to capture the engagement when they decide to sell. Williamson's gesture is prospecting Kay as if she were a future seller, not extending an intermediary relationship to her as a buyer. **Wrong layer for buy-side intent.** Maintain the warm NJPMA intro at the human level but don't pursue the VRA thread or escalate to working-relationship.

**Reasoning:** Kay's read of the M&A landscape: when an advisor's first move is to offer a free pre-sale audit / valuation tool, they are by definition working the seller side of the table. A buy-side intermediary's first move looks different — they share a deal pipeline, offer to walk through their NDA process, or ask what your buy-box looks like. Williamson's NJPMA presence may have looked like buy-side networking, but the VRA follow-up resolves the ambiguity: he's a sell-side specialist trolling for engagements.

This is the second sell-side advisor encountered in two weeks (Calder Capital was the first — engagement-fee structure flagged for buy-side use, see `feedback_buyside_advisor_success_fee_only` 2026-04-30). Pattern emerging.

**Pattern:** Free pre-sale audits / VRAs / valuation tools / "what's your business worth" calculators are sell-side prospecting moves. The advisor wants to be the seller's advisor when they decide to sell. None of that helps a buyer.

## Why this trace matters for future agents

The default email-intelligence classification sees: M&A advisor + warm in-person intro + sample document + free service offer = warm intermediary worth nurturing. **The free-service-offer is the signal in the wrong direction.** A buy-side intermediary doesn't lead with "let me give you a free thing" — they lead with deal-flow access or pipeline introductions.

Future agents triaging M&A advisor emails should flag "free VRA," "free valuation," "free pre-sale audit," "what's your business worth" language as sell-side markers and downgrade the warmth signal accordingly.

## Key insight

**Direction of the free thing reveals which side of the table the advisor sits on.** Buy-side advisors don't give buyers free deliverables — they earn on closing fees. Sell-side advisors give sellers free deliverables (pre-sale audits, VRAs) as engagement bait. When a buy-side person receives a free deliverable from an M&A advisor, the advisor is treating them as a future seller, not a current buyer.

## How a future agent should apply

For any inbound from an "M&A advisor" / "M&A specialist" / "investment banker" with one of these hooks:
- "Free Value Range Analysis"
- "Complimentary pre-sale audit"
- "What's your business worth — free assessment"
- "Sample valuation"
- "Quick pre-listing review"

→ Classify as **sell-side prospecting**. Maintain the personal-relationship layer (warm NJPMA-style intro stays warm) but do NOT escalate to working-relationship. Do NOT propose a 20-min intro call as if they're a buy-side intermediary. Suppress from "warm intermediary" surfaces in briefings.

Inverse signal — actual buy-side intermediary:
- "Happy to share what's currently on my desk under NDA"
- "Tell me your buy-box and I'll flag matches as they come"
- "Here's how I work with my buyer side"
- Active deal-flow as the lead, not a free deliverable.

Watch for third instance after Calder Capital (4/30) and Cetane (5/1) to graduate this from a trace into a `feedback_*.md` durable rule.

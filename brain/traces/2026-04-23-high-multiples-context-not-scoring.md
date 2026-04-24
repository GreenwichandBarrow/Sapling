---
schema_version: 1.1.0
date: 2026-04-23
type: trace
title: "High-Multiples / Sellers' Markets = Context Awareness, Not Scorecard Adjustment"
tags: ["date/2026-04-23", "trace", "topic/niche-intelligence", "topic/scorecard-doctrine", "topic/buy-side-economics", "topic/xpx-panel"]
had_human_override: true
importance: medium
target: skill
people: ["[[entities/kay-schneider]]"]
companies: []
---

# Trace: High-Multiples Are Context, Not Scoring

## Context

XPX Lower Middle Market panel 2026-04-23 surfaced industry-performance data: Transportation +20% YoY, Business Services (MSPs / Atlassian / ServiceNow partners) "double-digit resurgence at high multiples," Healthcare supply-demand imbalance (seller's market for quality assets). All three sectors are absent from G&B's current 8 active niches.

AI proposed: cross-check tracker, see if these were dismissed in prior niche-intelligence runs. If not dismissed, evaluate as candidate niches.

Kay's correction: "46 is about double digit multiples, it's a sellers market. We don't want that."

Then on the broader scoring question: "I don't want any scorecard changes, just context awareness."

## Decisions

### High multiples = a buyer's-economics flag, NOT a niche-quality flag
**AI implicit framing:** Hot sectors with growth + high multiples might be evaluable as new niches.
**Chosen:** Hot sectors with double-digit multiples are explicitly avoided because G&B-as-buyer cannot win on terms — buyers paying premium prices means we'd either overpay or get out-bid. The underlying business may be great, but the entry economics are wrong for an acquirer.
**Reasoning:** Niche scoring measures business quality (margins, recurring revenue, growth, TAM). Sector multiples measure buyer-side competition. These are independent dimensions. A great business in a hot sector is not a great acquisition for G&B at current prices.
**Pattern:** #pattern/separate-business-quality-from-buy-side-economics

### Context awareness, NOT a scoring rule
**AI proposed:** Codify high-multiple sectors as a -X scoring deduction or "buyer competitiveness" line item.
**Kay rejected:** "I don't want any scorecard changes, just context awareness."
**Chosen:** Save as memory `feedback_high_multiples_avoid_context.md`. When summarizing M&A intel, *mention* if a sector is running hot. Do NOT then propose downgrading/deprioritizing the related niche on the scorecard.
**Reasoning:** Mixing market-pricing context into the business-quality score muddies both signals. The scorecard is a stable measurement of niche quality; market conditions change quarter-to-quarter. If Kay decides to deprioritize based on multiples, that's a Kay decision recorded in session-decisions, not a scoring rule that auto-fires every time the multiple data refreshes.
**Pattern:** #pattern/keep-stable-measures-stable-flag-volatile-context-separately

### $3-5M EBITDA = open lane (companion observation, also context-only)
**Data point from XPX:** 95% of committed-capital funds have $1-3M EBITDA mandates. Above $3M, fund competition thins.
**AI proposed:** Tilt G&B buy-box framing toward $3-5M EBITDA where competition is thinner.
**Kay chose:** Don't narrow the buy box. Keep $1.5-5M inclusive. **Note** the open-lane observation but don't act on it as a buy-box change. "More opportunity for us 3-5M etc."
**Reasoning:** Buy-box edits are durable structural commitments; an observation about current fund-mandate distribution is current-cycle context. Narrowing now would lock G&B out of the $1.5-3M band when fund mandates inevitably move again. Awareness lets Kay weight prioritization within the band; narrowing eliminates options.
**Pattern:** #pattern/observation-now-not-policy-change

## Why This Trace Matters

A future agent ingesting M&A intel would, by default, want to "do something" with hot-sector data — propose adding the niche, adjust scoring, downgrade/upgrade something. The doctrine here is that market data informs Kay's read but doesn't auto-fire system changes.

This trace also shields the scorecard from drift. If every panel report or industry intel piece could nudge scoring, the scorecard becomes a moving average of M&A news instead of a stable measure of niche fundamentals.

## Key Insight

Two distinct categories:
- **Niche quality** = stable measures of business fundamentals (margins, recurring revenue, growth, TAM). Codified in scorecard. Slow to change.
- **Market context** = current-cycle conditions (multiples, fund mandates, buyer composition). Mentioned as flags. Fast to change.

Don't fold one into the other. If you do, you lose the ability to ask "is this a great business" without contaminating the answer with "what is the buy-side market doing this quarter."

## Closure Mechanism

- New memory `feedback_high_multiples_avoid_context.md` codifying the rule.
- Companion observation about $3-5M EBITDA "open lane" folded into the same memory (also context-only, not a buy-box edit).
- MEMORY.md index updated.
- No scorecard changes made. No buy-box edits made.

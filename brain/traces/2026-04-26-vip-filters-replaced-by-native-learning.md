---
schema_version: 1.1.0
date: 2026-04-26
type: trace
today: "[[notes/daily/2026-04-26]]"
task: Deleted 12 hardcoded VIP IMPORTANT,CATEGORY_PERSONAL Gmail filters in favor of Gmail's native Important learning
had_human_override: true
importance: medium
target: process
tags: [date/2026-04-26, trace, topic/email-filters, topic/native-vs-rules, pattern/native-ml-beats-hardcoded-rules, domain/technical]
---

# Decision Trace: Native ML beats hardcoded rules for behavioral classification

## Context

Kay's Gmail had 12 filters routing specific senders (Anacapa Partners, ML Capital, Sam@DealsX, Amanda Loiacono, Fred@Fireflies, Jet Aviation contact, Benchmark International acquisitions, etc.) to `IMPORTANT,CATEGORY_PERSONAL`. Each filter hardcoded one sender as VIP-tier.

When I surfaced the 12 for review, I expected Kay to keep some (Anacapa = real investor, ML Capital = peer searcher, etc.). Instead she said: *"none of these are VIP to me. The only VIPs are my investors (which already have the autolabel) and my family (which are not sending me email on this account)."* Then: *"I think having the important vs other separations in my inbox do the work of a vip labeling..."*

## Decision

Deleted all 12 VIP filters. Gmail's native Important classifier (Priority Inbox + the yellow arrow) takes over VIP recognition based on Kay's actual engagement patterns — who she opens, replies to, archives quickly, etc.

## Alternatives Considered

1. **Keep filters for the 4 I judged "real VIPs"** (Anacapa, ML Capital, DealsX, Amanda) — rejected. Kay's own categorization disagreed; she said none rise to VIP. Respecting her call avoids forcing my model of importance onto her.
2. **Migrate the senders to a new `auto/vip` label without IMPORTANT flag** — rejected. The semantic ask isn't "categorize VIPs"; it's "boost their visibility in the inbox." Native Important learning does this; a new label doesn't.
3. **Audit the 12 senders against Attio for actual relationship signals before deciding** — overkill. Kay's stated preference is the source of truth; data-mining her relationships to override her would be both slow and disrespectful.

## Reasoning

Gmail's Important classifier learns from behavior — opens, replies, response time, who's in your sent mail. This adapts as relationships evolve. A hardcoded `from:beacon@anacapapartners.com → IMPORTANT` filter doesn't adapt: if Kay stops engaging with that sender for any reason, the filter still boosts them.

For binary categorization (newsletters vs personal vs financial), rules are appropriate — the categories are stable and well-defined. For *behavioral importance* (who I should attend to first), native learning is strictly better because the signal is dynamic.

## Why This Trace Matters

Future agents recommending email categorization should distinguish between:
- **Categorical rules** (good fit for filters) — sender domain, subject keyword, list-id. Stable, well-defined.
- **Behavioral signals** (good fit for native ML) — who's important right now, who I respond to, who needs my attention. Dynamic, learned.

Don't propose hardcoded VIP/Important filters. Let Gmail learn. If the user wants categorical routing (deal flow, investors, team), that's a different question with a different answer.

## Key Insight

The right SaaS feature to use depends on whether the classification is *categorical* (stable, rule-shaped) or *behavioral* (dynamic, learned). Defaulting to filters for everything misuses the rule layer for problems the ML layer solves better.

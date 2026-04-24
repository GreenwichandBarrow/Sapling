---
schema_version: 1.1.0
date: 2026-04-23
type: trace
title: "Audience Taxonomy — Advisor Collapses Into Intermediary (3 Buckets, Not 4)"
tags: ["date/2026-04-23", "trace", "topic/audience-taxonomy", "topic/conference-engagement-skill", "topic/outreach-classification", "topic/post-conference-followup"]
had_human_override: true
importance: medium
target: process
people: ["[[entities/kay-schneider]]"]
companies: []
---

# Trace: Advisor Collapses Into Intermediary — 3 Buckets Only

## Context

While designing the post-conference email template variations for `conference-engagement`, Claude initially proposed a 4-audience taxonomy: Intermediary, Owner, Advisor/Industry Expert, Peer/Ecosystem. Kay flagged this immediately: "for audience please dont list 'advisor' twice, that is confusing. It should just be under intermediary because they advise businesses and therefore have direct connections."

## Decisions

### Collapse Advisor into Intermediary. 3 audience buckets only.
**APPROVE (Kay override):**
1. Intermediary — advisors, wealth managers, M&A, brokers, exit planners, CPAs, attorneys, bankers. Anyone who advises business owners and can refer deal flow. Gets the buy-box reference paragraph.
2. Owner — potential sellers. No buy-box, no ask, curiosity only.
3. Peer / Ecosystem — other searchers, service providers, fellow LPs, family offices. Simple stay-in-touch.

Saved as `feedback_audience_taxonomy_conferences`.

## Alternatives Considered

- **4 buckets (Intermediary, Advisor, Owner, Peer).** Claude's initial proposal. Rejected.
- **5 buckets (separate M&A advisor from wealth manager from broker from attorney).** Not proposed, but the logical extension of the "split by role" reasoning. Also wrong.
- **2 buckets (Potential-referrer and Not).** Simpler but loses the Owner vs Peer distinction (owners get curiosity-only messaging; peers get stay-in-touch).

## Reasoning

**The split between "intermediary" and "advisor" was a conceptual error.** Both categories have identical outreach patterns: the email body is the same. Creating two buckets with identical bodies is duplicate logic dressed up as taxonomy.

**The functional question is: can this person refer deal flow?** If yes → they need the buy-box paragraph. If they're a potential seller themselves → they need curiosity-only messaging. Everyone else is a peer. That's the real three-way split.

**Advisors by definition have direct owner access.** A wealth manager advising an HNW family has direct access to that family's business. An M&A advisor has direct access to sell-side clients. A CPA has direct access to every owner they serve. The "advise" verb IS the referral mechanism.

**Bucket count inflation is a readability tax for Kay.** Every additional bucket is another decision she has to make per card. 3 buckets = fast classification. 4 buckets with overlapping criteria = slow, and the wrong split produces wrong outreach (an advisor classified as non-intermediary would get stay-in-touch messaging instead of the buy-box paragraph — a worse outcome than a peer getting the buy-box, because the advisor was the actual referral source).

## Why This Trace Matters

Future agents designing audience taxonomies for outreach skills will naturally want to proliferate buckets ("but what about *industry experts* who aren't exactly *intermediaries*?"). The answer is always: collapse to the functional outreach pattern. If the email body is the same, the bucket is the same.

This also applies beyond conference-engagement — any skill that classifies by audience (relationship-manager, outreach-manager conference-outreach subagent) should use the same 3-bucket taxonomy.

## Key Insight

**Taxonomy follows function, not title.** The question is "what email body does this person get?" not "what's their LinkedIn headline?" Advisors → buy-box. Owners → curiosity. Everyone else → stay-in-touch. If two titles resolve to the same body, they're one bucket.

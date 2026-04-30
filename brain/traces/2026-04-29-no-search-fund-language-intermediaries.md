---
schema_version: 1.1.0
date: 2026-04-29
type: trace
had_human_override: true
importance: high
target: intermediary outreach voice across all email-template variations and any future direct broker/IB/lender outreach
tags: [date/2026-04-29, trace, topic/intermediary-outreach, topic/voice, topic/heritage-holding-model, pattern/avoid-stigmatized-label, domain/communications]
---

# Decision Trace: Drop "search fund" / "search vehicle" language for intermediaries

## Context

Drafting the G&B Intermediary Outreach Templates Doc. My v1 used "search vehicle" repeatedly throughout the 8 audience variations — assumed it was the accurate self-description matching G&B's actual structure (which it is, technically: 12-investor commitments, 24-month window, single-acquisition mandate).

Kay flagged this directly: *"There is no such thing as committed equity. Remove that. At this point everyone knows search funds, and they are not looked at very fondly. Can you please look at the newsletter that I get from heritage holdings."*

I read the Heritage Holding monthly newsletter (Sam Kramer / s.kramer@heritage-holding.com). Their framing self-describes as "Heritage Holding" — explicitly a "holding company" — and only commercially mentions their fund structure when needed ("investing out of $220m fund"). The buy-box is Heritage-Holding-style scannable: "What we look for / focus / what we don't do."

## Decision

Rewrite the entire template to drop "search vehicle" / "search fund" / "ETA" terminology. Replace with **"holding company in formation"**:

- Accurate (G&B becomes a HoldCo once a deal closes per `project_gb_charter.md`)
- Matches the Heritage Holding positioning Kay endorsed
- Avoids the search-fund stigma in the broker / IB / lender community

Also remove all "$2.8M committed equity" claims (false framing — search-fund equity is committed-on-deal, not held in escrow). Remove "24-month acquisition window" (sounds urgent / pressure-driven).

Saved as durable memory: `feedback_no_search_fund_language_intermediaries.md`.

## Why this matters for future agents

- **Owner outreach is different.** `feedback_outreach_about_them` and related rules apply only to OWNER outreach. Owners don't have search-fund baggage. Intermediaries do.
- **The stigma is real and asymmetric.** Search-fund-versed intermediaries (brokers, IBs, lenders, family offices) have been pitched repeatedly by underqualified searchers. The label triggers junior / inexperienced / transient associations. Holding-company framing avoids this without being dishonest.
- **Heritage Holding is the calibration source.** When in doubt about voice for intermediary content, read their latest newsletter (Sam Kramer sends monthly).
- **One-and-done cadence** is paired with this decision. No follow-up sequences for intermediaries — patience > volume. Different from owner outreach which has Day 0/3/14 cadence.

## Litmus for future agents

If an agent is drafting outreach to a broker, IB, lender, lawyer, CPA, family office, corporate advisor, or association head — DO NOT use "search vehicle," "search fund," or "ETA." Use "holding company in formation," "long-term investment firm," "acquisition firm." If unsure, default to "New York-based holding company in formation."

Owner-facing outreach is unaffected by this trace. The owner-outreach playbook (DealsX templates, etc.) keeps its existing voice rules.

## Source

Kay 2026-04-29 conversation. Memory: `feedback_no_search_fund_language_intermediaries.md`. Authoritative template: G&B Intermediary Outreach Templates Doc (`1_cNsAPCopDAfReoDXbB4d3hZW8TcYUqJ3XKYY_er7i4`).

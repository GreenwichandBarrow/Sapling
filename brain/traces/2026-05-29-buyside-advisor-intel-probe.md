---
schema_version: 1.1.0
date: 2026-05-29
type: trace
task: "Respond to E&K (Joe Vanore) buy-side engagement proposal that violates success-fee-only doctrine"
had_human_override: true
importance: high
target: "memory:feedback_probe_advisor_track_record_before_declining"
tags: [date/2026-05-29, trace, person/joe-vanore, company/ever-kerr, topic/buy-side-advisor, topic/intermediary, status/active]
---

# Decision Trace: Probe Buy-Side Advisor Track Record Before Declining

## Context
[[entities/joe-vanore|Joe Vanore]] of [[entities/ever-kerr|E&K]] pitched a buy-side engagement with a **$3K/mo retainer** ($9K upfront for the first three-month term) + success fee (lesser of $100K+3% of Total Consideration or 10%, $50K floor; monthly payments credit toward the success fee). The retainer violates G&B's standing success-fee-only doctrine for buy-side advisors ([[../../memory/feedback_buyside_advisor_success_fee_only]]). CFO: affordable but tight (7.1mo runway, already ~2mo short of the Feb-2027 deadline; $3K/mo eats 69% of the monthly savings target). A 12-month scan of 347 E&K emails surfaced **zero pest-control listings** — only landscaping/turf + B2C — so his "we'd have a lot of success here" claim on pest is unsupported by his own deal flow.

## Decisions

### Decline-as-structured vs. probe-first
**AI proposed:** Clean decline (or counter success-fee-only) — the offer breaks doctrine and the flow is off-thesis.
**Chosen:** Do NOT clean-decline yet. First send a chat-only reply (Kay sends in-thread) probing E&K's recent pest transactions and the multiples playing out in the $1–3M EBITDA band, framed around "what the engagement could look like." Defer the engage/decline call until Joe answers.
**Reasoning:** The advisor's claim and his actual track record conflict, and the decision-relevant data (real pest multiples in G&B's band) is something he'll hand over for free while trying to win the engagement. Declining first closes that channel. The probe costs nothing, sharpens the eventual decline/counter, and yields pest-thesis intel regardless of whether E&K is ever engaged ("even if we don't use their services it could be a helpful data point" — Kay). Framing must point at the engagement, not "where the market sits," so the ask stays tied to the live negotiation.
**Pattern:** #pattern/intel-probe-before-decline

## Learnings
- A buy-side advisor's pitch is a free intel channel. Before declining one whose offer breaks success-fee-only doctrine, probe their transaction track record + multiples in the target niche — you extract comps and test their claim whether or not you ever engage.
- Codified as [[../../memory/feedback_probe_advisor_track_record_before_declining]]. Grounding case: E&K / Joe Vanore, 2026-05-29.

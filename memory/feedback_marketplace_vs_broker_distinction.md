---
name: Marketplace listings are NOT broker-mediated deals — distinguish before flagging into broker channel
description: Flippa, BizBuySell-self-listed, and other owner-listed marketplace blasts are not broker channel deal flow. They go through the broker channel only if a verified human broker is named and has a real track record. Marketplace cattle-call listings (3000+ buyers per `feedback_broker_competition`) belong in the deal-aggregator OUT bucket regardless of financials.
type: feedback
originSessionId: c0375c4c-6be2-4191-9f4b-0e97e59a3de4
---
**Rule:** Before flagging an inbound deal listing as broker-channel-eligible, verify that there is (a) a real human broker named in the body, (b) a verified firm with a deal track record in our LMM range, and (c) a US tristate operating presence (or national footprint). Listings that fail any of these go to OUT, not OPPORTUNISTIC FLAG.

**Why:** 2026-05-04 broker-channel build rerun flagged "Tory @ Flippa $16M B2B Trade Fair Exhibitor Recruitment Service" as the cleanest FLAG candidate from 30 days of broker BLAST emails. Subagent enrichment revealed: "Tory" is `marketing@flippa.com` (newsletter sender, not a broker). The actual broker named in the body was Amber Burke, Baltimore MD (out of geo). The business itself is a B2B online marketplace middleman for global trade fairs, not operationally-critical services. The listing had likely already delisted in the 11-day window. Per `feedback_broker_competition` (Broker deals go to 3000+ buyers, G&B rarely wins), Flippa is exactly that cattle-call layer. Even if a Flippa listing meets buy-box criteria on financials, the broker isn't the right counterparty.

**How to apply:**
- deal-aggregator dual-filter (Tue work): owner-listed marketplace sources (Flippa, BizBuySell, BizQuest if owner-listed) flag as `marketplace-cattle-call` and route to OUT regardless of financial fit. Broker-mediated sources (firm-named brokers, IBs, Axial members) route to STRICT or OPPORTUNISTIC normally.
- email-intelligence: a BLAST email from `marketing@flippa.com` or similar marketplace-newsletter sender does NOT trigger the broker-inbound reputation rule, even if a deal headline inside passes financial gates. Marketplace newsletters are NEWSLETTER classification, not BROKER.
- Source-list maintenance: tag each Sourcing Sheet row as `BROKER-MEDIATED` or `MARKETPLACE-OWNER-LISTED`. Filter the dual-filter routing accordingly.
- For verified-broker pipeline ingestion: the listing must name a human broker (not just a marketplace platform staff name) AND the firm must have a track record (firm website with deal advisory page + recent closings + named professionals on LinkedIn).

**Caught:** 2026-05-04 broker-channel rerun. Audit subagent flagged "Tory @ Flippa" as cleanest FLAG. Tory enrichment subagent revealed Flippa newsletter pattern + Amber Burke geographic mismatch + marketplace-not-broker classification. G&B operator confirmed kill. The audit's earlier 22-FLAG count was inflated by similar marketplace-newsletter blasts — true broker-channel pipeline is smaller than the headline number.

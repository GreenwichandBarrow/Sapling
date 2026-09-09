---
schema_version: 1.1.0
date: 2026-09-09
deals_found: 0
sources_scanned: 16
sources_blocked_verified: 0
sources_blocked_single_attempt: 1
email_deals: 6
dealsx_replies: 0
broker_opportunistic: 1
email_scan_status: live
tags: [date/2026-09-09, output/deal-aggregator-scan, topic/deal-aggregator, status/done]
---
# Deal Aggregator Scan — 2026-09-09

Morning run. Buy boxes were freshly read from Drive. Active niches and DEALSX corpus were freshly read from the Industry Research Tracker. The 2026-09-07 niche-intelligence sidecar was loaded; its three new niches were treated as watchlist-only and were not PASS/Slack eligible. SMB Deal Hunter / Helen Guo and Quiet Light rows were hard-excluded from this run per the paywall/paused-source rules.

Corpus paths: active niches with populated DEALSX references used DEALSX Keywords + Quick notes plus WEEKLY REVIEW Quick notes; the blank-reference active rows used WEEKLY REVIEW row enrichment. New-niche watchlist: Outsourced Billing, Outsourced Diagnostic Medical Physics QA, and Independent Electrical Power-System Testing and Preventive Reliability Services.

## Deals Surfaced (sent to Slack individually)

None today. No PASS rows; no Slack post was sent.

## Email Inbound Deals

Six non-excluded listing rows were parsed from the live email artifact: two BizBuySell franchise listings, two Transworld listings, one Baton Marketplace listing, and one Calder Capital listing. None cleared an active-thesis PASS gate. SMB Deal Hunter / Helen Guo and Quiet Light listings were ignored entirely and do not count here.

## DealsX Proprietary Outreach Replies

No DealsX reply records were present in today's email artifact. No dashboard snapshot was available beyond the email artifact, so DealsX coverage is incomplete for this run.

None today.

## Broker Opportunistic Review

1. **Premium home automation design and installation business** — Baton Marketplace | Revenue $5,264,273 | EBITDA $2,239,169 | Home services | Key signals: not disclosed | clears disclosed services financial bands but does not match an active thesis corpus; source link: Baton Marketplace email alert.

## Near Misses

None today. Email leg was live; no listing met the near-miss threshold after disclosed hard-excludes and financial screening.

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Key Signals | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|-------------|---------|---------------|
| Baton Marketplace | Premium home automation design and installation business | New York | $5,264,273 | $2,239,169 | 42.5% | Home services | not disclosed | BROKER-OPPORTUNISTIC | Clears disclosed Services financial bands but no active-thesis corpus match; artifact-only. |
| BizBuySell | School of Rock franchise | undisclosed | undisclosed | undisclosed | undisclosed | Franchise / education | not disclosed | HARD-REJECT | Franchise hard-exclude. |
| BizBuySell | Mr. Electric franchise | undisclosed | undisclosed | undisclosed | undisclosed | Franchise / electrical services | not disclosed | HARD-REJECT | Franchise hard-exclude. |
| Transworld Business Advisors | Pair of Edible Arrangements Stores | New York (Nassau County) | $1.18M | $173,167 | undisclosed | Franchise / food retail | not disclosed | HARD-REJECT | Franchise and consumer retail/food hard-excludes. |
| Transworld Business Advisors | Carpet & Tile Business | New York (Nassau County) | undisclosed | $131,815 | undisclosed | Flooring services | not disclosed | HARD-REJECT | Disclosed EBITDA below Services lower band; labor-heavy service risk. |
| Calder Capital | Event Planning and Entertainment Company | Mid-Atlantic | $432,721 | $256,088 | 59.2% | Event services | not disclosed | HARD-REJECT | Disclosed revenue and EBITDA below Services lower bands. |

## Source Scorecard

All active rows in the live Sourcing Sheet are represented, plus Transworld Business Advisors because it appeared as an active parsed email source. Email-only sources were covered through the live email artifact; marketplace pages were fetched directly. `blocked (single-attempt)` means a web fetch failed and no browser fallback was available; it is not a verified dead-source conclusion.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| BizBuySell | Newsletter | active email/newsletter | — | 2 | 0 | — |
| Business Exits | Marketplace | active; fetched, no listing cards parsed | 200 | 0 | 0 | — |
| DealForce | Marketplace | active; fetched, no listing cards parsed | 200 | 0 | 0 | — |
| Empire Flippers | Marketplace | active; fetched, no in-scope cards parsed | 200 | 0 | 0 | — |
| Everingham & Kerr | Newsletter | active email-only; no today's rows | — | 0 | 0 | — |
| IAG M&A Advisors | Direct email | active relationship; no today's rows | 200 | 0 | 0 | — |
| Rejigg | Marketplace | active; public landing page, no listing cards parsed | 200 | 0 | 0 | — |
| Viking Mergers (email-only row) | Newsletter | active email-only; no today's rows | — | 0 | 0 | — |
| Viking Mergers (newsletter row) | Newsletter | active newsletter; no today's rows | — | 0 | 0 | — |
| Baton Market | Marketplace | active email alert; web page fetched | 200 | 1 | 0 | — |
| Calder Capital | Newsletter | active email source; web fallback single-attempt blocked | 406 | 1 | 0 | — |
| GP Bullhound | Direct email | active relationship; no today's rows | 200 | 0 | 0 | — |
| PCO Bookkeepers | Newsletter | active; no actionable listing parsed | 200 | 0 | 0 | — |
| Sica Fletcher | Direct email | active; announcements page fetched, no actionable listing parsed | 200 | 0 | 0 | — |
| Synergy Business Brokers Real Estate | Marketplace | active; page fetched, no listing cards parsed | 200 | 0 | 0 | — |
| Transworld Business Advisors | Newsletter | observed active email source | — | 2 | 0 | — |

Automated run coverage: 7 marketplace/relationship web surfaces fetched successfully, one web surface had a single-attempt 406 response, and email coverage was read from the live email-intelligence artifact. Manual deal-source queue: Calder Capital web follow-up; no direct-email source requires manual marketplace work.

## Volume Check

- Deals surfaced today: 0
- Broker-opportunistic review items: 1
- 7-day rolling average: 0.0 PASS deals/day (2026-09-02 through 2026-09-09 weekday artifacts)
- Target: 1-3/day — CRITICAL
- Email leg: live
- Funnel bottleneck: source coverage / DealsX coverage incomplete

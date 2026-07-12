---
schema_version: 1.2.0
date: 2026-07-12
type: email-scan-results
status: review
skill_origin: email-intelligence
kay_approved: null
people:
  - "[[entities/anthony-bacagan]]"
  - "[[entities/beth-odonnell]]"
  - "[[entities/jackie-hirsch]]"
companies:
  - "[[entities/greenwich-and-barrow]]"
  - "[[entities/startvirtual]]"
tags:
  - date/2026-07-12
  - output
  - output/email-scan-results
  - status/review
  - person/anthony-bacagan
  - person/beth-odonnell
  - person/jackie-hirsch
  - company/greenwich-and-barrow
  - company/startvirtual
  - topic/budget
  - topic/bookkeeper
  - topic/deal-flow
  - topic/intro
---

# Email Intelligence Scan Results

## Actionable Items Created
- None. The Beth-to-Jackie intro is already tracked in [[brain/inbox/2026-07-07-review-beth-introduction-to-jackie-hirsch]], and the June 2026 bookkeeper report already produced [[brain/outputs/2026-07-11-budget-report-june-2026]] from the same Gmail thread.

## Deal Flow Classified
- DIRECT: 4
- BLAST: 14
- NEWSLETTER: 1
- The 15 surfaced deal-related candidates were dominated by broker/newsletter blasts; the rest of the inbox window was ordinary noise.

## Draft Status
- 1 unsent draft, 0 sent drafts in the compact Gmail payload.
- `r766635097214011401` is still pending, has blank subject/to, and is older than 48 hours.
- No prior-workday `session-decisions` file was available in this workspace to confirm a send or delete decision.

## Introductions Detected
- No new intro item needed. [[entities/beth-odonnell|Beth O'Donnell]] introduced [[entities/jackie-hirsch|Jackie Hirsch]] in thread `19f37ffc556e3e32`, and that connection is already tracked in [[brain/inbox/2026-07-07-review-beth-introduction-to-jackie-hirsch]] and [[entities/jackie-hirsch]].
- Kay already replied in-thread and the follow-up call is on the calendar for July 13, 2026.

## Niche Signals
- [[entities/startvirtual|StartVirtual]] sent a routine EOW financial update, but the monthly Management Report had already been processed into [[brain/outputs/2026-07-11-budget-report-june-2026]].
- [[entities/beth-odonnell|Beth O'Donnell]] / Search Fund Coalition remains a useful warm-intro channel for brokers and peers.
- [[entities/jackie-hirsch|Jackie Hirsch]] surfaced strong, explicit feedback about searcher positioning, especially around buyer fit and translating prior brand experience into acquisition thesis language.
- Deal-newsletter content stayed concentrated in SMB acquisitions, SaaS, creator/media assets, and consumer brands. [[entities/peter-lang|Peter Lang]]'s SBA training email also surfaced personal-guarantee insurance as a live acquisition-financing topic.
- Granola returned no new notes in the lookup window.

## In-Person Meetings Today
- None in the compact context. The intro thread references a future call with [[entities/jackie-hirsch|Jackie Hirsch]] on July 13, 2026, not a same-day in-person meeting.

## Broker BLAST Listings (per-deal extraction)
Rows below capture the visible listings in the compact Gmail excerpts. A few long digests were truncated in the bounded context, so some multi-listing emails are represented as a listing bundle where the underlying body details were not fully visible in the excerpt.

| source | headline | geo | revenue | ebitda | margin | industry | flag_reason | gmail_msg_id | listing_ordinal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Helen Guo, SMB Deal Hunter | Three-Location Pet Supply Retail Business | Texas | $5,000,000 | $2,000,000 |  | pet retail | deal-newsletter-known-sender | 19f42ccdbf4f5567 | 1 |
| Helen Guo, SMB Deal Hunter | Home Healthcare Services Company | New Jersey |  | $300,000 |  | home healthcare | deal-newsletter-known-sender | 19f42ccdbf4f5567 | 2 |
| Helen Guo, SMB Deal Hunter | PVC Pipe Distribution Company | Nevada |  | $250,000 |  | distribution | deal-newsletter-known-sender | 19f42ccdbf4f5567 | 3 |
| Helen Guo, SMB Deal Hunter | Non-Emergency Medical Transportation Company | New Jersey |  | $1,100,000 |  | transportation | deal-newsletter-known-sender | 19f42ccdbf4f5567 | 4 |
| Helen Guo, SMB Deal Hunter | Electrical Contractor Company | North Carolina |  | $700,000 |  | electrical contracting | deal-newsletter-known-sender | 19f42ccdbf4f5567 | 5 |
| Helen Guo, SMB Deal Hunter | Auto Repair Shop | North Carolina | $1,000,000 | $500,000 |  | auto repair | deal-newsletter-known-sender | 19f5204a1b800ba2 | 1 |
| Helen Guo, SMB Deal Hunter | Remote Architectural Photography and Videography Company | undisclosed |  | $500,000 |  | services / media | deal-newsletter-known-sender | 19f5204a1b800ba2 | 2 |
| Helen Guo, SMB Deal Hunter | Wholesale Fruit and Vegetable Business | New York City |  | $900,000 |  | wholesale distribution | deal-newsletter-known-sender | 19f5204a1b800ba2 | 3 |
| Helen Guo, SMB Deal Hunter | Outdoor Living and Hardscaping Company | South Carolina |  | $1,000,000 |  | outdoor services | deal-newsletter-known-sender | 19f5204a1b800ba2 | 4 |
| Helen Guo, SMB Deal Hunter | Vertically Integrated Manufacturing and eCommerce Businesses | Wisconsin |  | $500,000 |  | manufacturing / ecommerce | deal-newsletter-known-sender | 19f5204a1b800ba2 | 5 |
| Tory @ Flippa | Men's wellness brand | undisclosed | $8.9M annual revenue |  | 20% repeat customer rate | ecommerce / wellness | deal-newsletter-known-sender | 19f33ab10dda52d7 | 1 |
| Tory @ Flippa | Legal Client Prospecting Service | undisclosed | $433K annual revenue |  | 0 CAC | legal services / lead gen | deal-newsletter-known-sender | 19f33ab10dda52d7 | 2 |
| Tory @ Flippa | Finance app | undisclosed |  |  |  | fintech app | deal-newsletter-known-sender | 19f33ab10dda52d7 | 3 |
| searchagent@bizquest.com | New York businesses for sale bundle | New York | 16 new listings |  |  | multi-listing bundle | multi-listing | 19f368d8f59554ad | 1 |
| NewBizOpps@bizbuysell.com | 3-Location Car Wash Portfolio bundle | New York / Kings County / Westchester County | 5 listings |  | ~14% cap | car wash / auto services | multi-listing | 19f374ec15e4568a | 1 |
| Lisa @ Generational Group | July Deal Books bundle | undisclosed |  |  |  | multi-book deal digest | multi-listing | 19f37c560414ecd2 | 1 |
| Brad Wayland | Premium Self-Help Book and System | undisclosed | 40,000 copies sold |  | 35% net margins | media / publishing | deal-newsletter-known-sender | 19f37c4959bfac39 | 1 |
| Chris Guthrie | 11-Year-Old Matcha Tea Powder Business | undisclosed | $1,959,141 | $806,714 earnings |  | ecommerce / consumables | deal-newsletter-known-sender | 19f38a03728376ee | 1 |
| Tory @ Flippa | Hardware Brand | undisclosed | $2.1M annual revenue |  |  | ecommerce / hardware | deal-newsletter-known-sender | 19f38d204ffc6b6d | 1 |
| Tory @ Flippa | Video Chat Site | undisclosed | 3M monthly views |  |  | media / consumer internet | deal-newsletter-known-sender | 19f38d204ffc6b6d | 2 |
| Tory @ Flippa | Trading SaaS | undisclosed |  |  | 64% margin | SaaS | deal-newsletter-known-sender | 19f38d204ffc6b6d | 3 |
| Brad Wayland | Affiliate & Direct-Response Business | undisclosed |  |  | low multiple | marketing / direct response | deal-newsletter-known-sender | 19f3cebbb19fff67 | 1 |
| Tory @ Flippa | Ergonomic Chair Brand | undisclosed | $5.1M annual revenue |  |  | ecommerce / furniture | deal-newsletter-known-sender | 19f3df9e7e6d6edf | 1 |
| Tory @ Flippa | Media Portfolio | undisclosed | 40M sessions |  |  | media / portfolio | deal-newsletter-known-sender | 19f3df9e7e6d6edf | 2 |
| Tory @ Flippa | The Exit | undisclosed |  |  |  | media / content | deal-newsletter-known-sender | 19f3df9e7e6d6edf | 3 |
| Drew Ermenc | Amazon FBA Wholesale Business | undisclosed | $1M+ revenue |  | zero ad spend | ecommerce / Amazon FBA | deal-newsletter-known-sender | 19f4213f5fb176ff | 1 |
| Tory @ Flippa | Polewear Brand | undisclosed | $1.3M annual revenue |  |  | ecommerce / apparel | deal-newsletter-known-sender | 19f431ae1194de53 | 1 |
| Tory @ Flippa | Blog Site | undisclosed | 186K monthly views |  |  | media / blog | deal-newsletter-known-sender | 19f431ae1194de53 | 2 |
| Tory @ Flippa | Navigate the Noise | undisclosed |  |  |  | media / content | deal-newsletter-known-sender | 19f431ae1194de53 | 3 |
| Chris Wozniak | Craft Brewing Media Brand | undisclosed | $1.2M ARR |  |  | media / podcast | deal-newsletter-known-sender | 19f473788cdc9a1c | 1 |

## Auto-Drafts Created
None

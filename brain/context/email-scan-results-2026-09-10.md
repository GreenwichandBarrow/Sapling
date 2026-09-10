---
schema_version: 1.1.0
date: 2026-09-10
type: email-scan-results
skill_origin: email-intelligence
tags: [date/2026-09-10, output/email-scan-results, status/draft, source/gmail]
---

# Email Scan Results

## 1. Actionable Items Created

- None. No new CIM, active-deal fast-path, introduction, or bookkeeper trigger inbox item was created.
- Bookkeeper Management Report for period 2026-07 was detected in message `1a04434972f8b44a` but already processed. Existing outputs: `brain/outputs/2026-08-28-budget-report-july-2026.md` and `brain/outputs/2026-09-01-budget-report-july-2026.md`. Duplicate trigger and budget-manager invocation were skipped per period idempotency.

## 2. Deal Flow Classified

- DIRECT: 17
- BLAST: 20
- NEWSLETTER: 20
- Scan scope: 62 inbound-query records, including 5 records carrying SENT labels; deal-flow-label messages were deduplicated through the compact context.
- Deal-newsletter/listing sources detected: SMB Deal Hunter, Quiet Light, Calder Capital, Transworld, BizBuySell, Baton, and Everingham & Kerr.

## 3. Draft Status

- 2 Gmail drafts were returned by the draft scan; 1 draft detail was available. The available draft is unsent and dated 2026-08-20, therefore older than 48 hours. No prior-workday session-decision file existed to suppress the stale flag.
- No auto-acknowledgment draft was required: no inbound NDA/CIM attachment trigger was present in the compact source artifact.

## 4. Introductions Detected

- None.

## 5. Niche Signals

- Deal-flow emails surfaced recurring SMB opportunities in home automation, pest control, HVAC/sheet-metal fabrication, plumbing, metrology, restaurants, distribution, career services, video editing, SaaS/FinTech, and Amazon/FBA brands.
- The Helen Guo SMB Deal Hunter newsletter contained five explicit listings: Pennsylvania beer distributor, Minnesota graphics/sign company, New Mexico electrical/solar contractor, New Jersey jewelry-tools distributor, and Florida charter-bus company.
- Acquisition Lab newsletter reported diligence/QoE risk as a recurring deal-screening theme. This is a passive signal, not a validated thesis conclusion.

## 6. In-Person Meetings Today

- No calendar-confirmed in-person meeting was available in the compact source artifact. An email invitation advertised the NYC ETA & SMB Breakfast for September 10, 2026; invitation status was not inferred as attendance.

## 7. Broker BLAST Listings (per-deal extraction)

| source | headline | geo | revenue | ebitda | margin | industry | flag_reason | gmail_msg_id | listing_ordinal |
|---|---|---|---|---|---|---|---|---|---:|
| Helen Guo, SMB Deal Hunter | Drive-Through Beer Distributor | PA | $1.5M | $250K | undisclosed | Beverage distribution | deal-newsletter-known-sender | 1a08812b3ff479ab | 1 |
| Helen Guo, SMB Deal Hunter | Custom Graphics and Sign Company | MN | undisclosed | $900K | undisclosed | Signs/graphics | deal-newsletter-known-sender | 1a08812b3ff479ab | 2 |
| Helen Guo, SMB Deal Hunter | High-Voltage Electrical and Solar Site Contractor | NM | undisclosed | $746K | undisclosed | Electrical/solar contracting | deal-newsletter-known-sender | 1a08812b3ff479ab | 3 |
| Helen Guo, SMB Deal Hunter | Jewelry Tools and Supplies Distributor | NJ | undisclosed | $700K | undisclosed | Distribution | deal-newsletter-known-sender | 1a08812b3ff479ab | 4 |
| Helen Guo, SMB Deal Hunter | Charter Bus Company | FL | undisclosed | $300K | undisclosed | Transportation | deal-newsletter-known-sender | 1a08812b3ff479ab | 5 |
| Drew Ermenc, Quiet Light | Amazon FBA Baby Brand | undisclosed | undisclosed | undisclosed | undisclosed | E-commerce/FBA | single-listing-blast | 1a067983aa860713 | 1 |
| Calder Capital M&A | Event Planning and Entertainment Company | undisclosed | $432,721 | undisclosed | undisclosed | Events/entertainment | single-listing-blast | 1a0684c5f5ec5650 | 1 |
| Brad Wayland, Quiet Light | Clip Art Subscription Business | undisclosed | undisclosed | undisclosed | undisclosed | Digital subscription | single-listing-blast | 1a06879bc86056b4 | 1 |
| Samuel Curcio, Transworld | Absentee Pair of Edible Arrangements Stores | Nassau County, NY | $1.18M | $173,167 SDE | undisclosed | Food/franchise | multi-listing | 1a06c0e7e40d2157 | 1 |
| Samuel Curcio, Transworld | Carpet & Tile Business | Nassau County, NY | undisclosed | $131,815 SDE | undisclosed | Flooring | multi-listing | 1a06c0e7e40d2157 | 2 |
| Samuel Curcio, Transworld | Kitchen and Bath Cabinet Manufacturer | CT | undisclosed | $0 SDE | undisclosed | Manufacturing | multi-listing | 1a06c0e7e40d2157 | 3 |
| Samuel Curcio, Transworld | Absentee Run Recording Studio | Brooklyn, NY | undisclosed | $134,988 SDE | undisclosed | Media/entertainment | multi-listing | 1a06c0e7e40d2157 | 4 |
| Samuel Curcio, Transworld | High-Growth Distribution Co. | Suffolk County, NY | undisclosed | $1,446,050 SDE | undisclosed | Distribution | multi-listing | 1a06c0e7e40d2157 | 5 |
| Samuel Curcio, Transworld | SBA Pre-Qual Multi-Restaurant Portfolio | MA | $4.0M projected 2026 | $459,435 SDE | undisclosed | Restaurants | multi-listing | 1a06c0e7e40d2157 | 6 |
| Samuel Curcio, Transworld | Commercial Restroom Partitions Business | Suffolk County, NY | $2.3M | negative SDE | undisclosed | Manufacturing/distribution | multi-listing | 1a06c0e7e40d2157 | 7 |
| Ryan Condie, Quiet Light | FinTech SaaS | undisclosed | undisclosed | $33K SDE | undisclosed | SaaS/FinTech | single-listing-blast | 1a06cc1f6924bc30 | 1 |
| BizBuySell | Hot Franchise Listings | undisclosed | undisclosed | undisclosed | undisclosed | Franchises | deal-newsletter-known-sender | 1a082047766a5661 | 1 |
| Baton Marketplace | Premium Home Automation Design and Installation Business | NY | $5.264M | $2.239M adjusted cash flow | undisclosed | Home services | single-listing-blast | 1a0811b86e67f991 | 1 |
| Jon Hainstock, Quiet Light | Subscription Video-Editing Service | undisclosed | undisclosed | undisclosed | undisclosed | Business services | single-listing-blast | 1a0815c263569620 | 1 |
| Chris Wozniak, Quiet Light | UV-Protection Umbrella Brand | undisclosed | undisclosed | undisclosed | undisclosed | E-commerce/FBA | single-listing-blast | 1a08236a262aae39 | 1 |
| Chris Wozniak, Quiet Light | DTC Pest Control Brand | undisclosed | $10.7M TTM | undisclosed | undisclosed | E-commerce/pest control | single-listing-blast | 1a08682be0f5b1b5 | 1 |
| Max Friar, Calder Capital | Integrated Metrology Solutions Provider | undisclosed | $2.288M | undisclosed | undisclosed | Metrology/manufacturing | single-listing-blast | 1a08729e03bcfb82 | 1 |
| Brad Wayland, Quiet Light | Thumbtack-Dominant Career Services Business | undisclosed | undisclosed | undisclosed | 33%+ net margin | Career services | single-listing-blast | 1a0875cf723c21ba | 1 |

## 8. Auto-Drafts Created

None.

### System Status / Actionable Items

- Granola REST query completed successfully and returned no new notes since 2026-09-09T00:00:00Z; no call notes were created.
- Bookkeeper P&L chain: July 2026 already processed; emitted `BOOKKEEPER-PL-CHAIN: skipped existing budget-manager monthly for period 2026-07 existing_output=brain/outputs/2026-09-01-budget-report-july-2026.md`.
- No CIM or Active Deal Fast-Path match was identified in the compact source artifact; no Drive, Attio, deal-evaluation, or Slack side effect was required.

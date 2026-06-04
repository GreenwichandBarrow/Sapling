---
date: 2026-06-04
deals_found: 0
sources_scanned: 3
sources_blocked_verified: 0
sources_blocked_single_attempt: 1
email_deals: 0
dealsx_replies: 0
buy_box_source: live
morning_artifact_present: true
run_type: afternoon
---
# Deal Aggregator Scan — 2026-06-04 (Afternoon Top-Up)

Afternoon run (`--afternoon` flag). Buy-box docs re-read live from Drive. Active niches re-confirmed from WEEKLY REVIEW tab (8 active: Premium Pest, Private Art Advisory, Estate Management, Specialty Coffee Equipment, High-End Commercial Cleaning, Vertical SaaS Luxury, Specialty Insurance Brokerage, Storage & Related Services for High-Value Assets). Email-scan-results artifact for today confirmed present.

Time-sensitive platforms scanned: Rejigg, Flippa, Everingham & Kerr (email channel). Full Channel 1 + 3 sweep skipped — morning run covered those.

**Note on E&K morning fingerprint gap:** The E&K Metal Manufacturing deal (Kay signed NDA Jun 3) was flagged in today's morning artifact under `email_deals: 1` but has no corresponding fingerprint entry in `deal-aggregator-fingerprints.jsonl`. Morning run appears to have not called the fingerprint `add` step for that match. Afternoon run cannot retroactively add it (no financials/geography to construct the hash against the correct scheme). Flagged for morning run calibration.

---

## Deals Surfaced (sent to Slack individually)

None today.

---

## Email Inbound Deals

None new since morning scan. Two E&K emails received this afternoon:

1. **E&K Machining Services re-blast** (thread 19e9360e06fc1fd7, arrived 12:02 ET) — Same listing as morning email-scan-results capture (msg 19e8a094b1a214f4, "Machining Services, Engineering & Waterjet Cutting Company", Southeastern US, $2.3M rev, $500K normalized EBITDA). Buy-box fail: revenue $2.3M < $10M Services floor. Duplicate of morning scan listing; no Slack.

2. **E&K Project Widgets, Inc. tombstone** (thread 19e93a2ace67a48a, arrived 13:15 ET) — Acquisition announcement / press release. PWI (enterprise project management software, DE, Microsoft Partner) acquired by private investor. Not a for-sale listing. Intel only: E&K closed a deal on a project-management SaaS-adjacent product company.

---

## DealsX Proprietary Outreach Replies

None in today's email-scan-results.

---

## Near Misses (not Slacked)

- Rejigg Luxury Handmade Rug Company ($27.5M rev, $5.1M EBITDA, ~18.5% margin) — Revenue and margin both technically in range, but consumer retail / DTC hard exclude applies. Geography spans NY/So. California (CA soft-exclude also applicable). Not a services-thesis match.
- Rejigg Mobile Phone Distributor ($28.3M rev, $166.2K SDE) — Revenue in range but SDE margin 0.6% is far below 10% floor (disclosed-and-failed criterion). No niche corpus match.
- Rejigg Golf Event Production Company ($14.4M rev, $6.5M SDE) — Revenue in range, but hospitality/nightlife hard exclude applies; EBITDA also above $5M ceiling.

---

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Rejigg | Luxury Handmade Rug Company | NY / So. California | $27.5M | $5.1M | ~18.5% | Luxury Retail (rugs) | HARD-REJECT | Consumer retail/DTC hard exclude; CA soft-exclude also present |
| Rejigg | Golf Event Production Company | New York | $14.4M | $6.5M (SDE) | ~45% | Events / Hospitality | HARD-REJECT | Hospitality/events hard exclude; EBITDA above $5M ceiling |
| Rejigg | Mobile Phone Distributor | New York | $28.3M | $166.2K (SDE) | 0.6% | Distribution | HARD-REJECT | Margin 0.6% disclosed-and-failed (10% floor) |
| Rejigg | Plumbing, Electrical & Hardware Wholesale Supplier | New York | $5.3M | $938K (SDE) | ~17.7% | Distribution / Wholesale | HARD-REJECT | Revenue below $10M floor; construction-adjacent |
| Rejigg | Custom Shading Business | New York | $11.1M | $1.2M (SDE) | ~10.8% | Manufacturing / Home Services | HARD-REJECT | EBITDA $1.2M below $1.5M floor (disclosed-and-failed) |
| Rejigg | Educational Consulting Business | NYC metro | $6.2M | $2.7M (SDE) | ~43.5% | Professional Services | HARD-REJECT | Revenue below $10M floor |
| Rejigg | Construction Business | New Jersey | $25M | $5M | ~20% | Construction | HARD-REJECT | Construction hard exclude |
| Rejigg | High-End Kitchen Millwork / Cabinetry | New York | $4.5M | $1M | ~22.2% | Manufacturing | HARD-REJECT | Revenue below $10M floor; capital-intensive manufacturing |
| Rejigg | Precision Milling & Machining Shop | New York | $5.1M | $222K | ~4.3% | Manufacturing | HARD-REJECT | Revenue below $10M floor; margin 4.3% below 10% floor |
| Rejigg | HVAC and Plumbing Services Business | Adirondack / upstate NY | $3.5M | $440.1K (SDE) | ~12.6% | HVAC / Trades | HARD-REJECT | Revenue below $10M floor; construction-adjacent trades |
| Rejigg | Pool Construction / Maintenance Company | New Jersey | $5M | $1.8M | ~36% | Construction | HARD-REJECT | Construction hard exclude; revenue below $10M floor |
| Rejigg | Engineering / Environmental Consulting Firm | New Jersey | $4.6M | $484K | ~10.5% | Professional Services | HARD-REJECT | Revenue below $10M floor |
| Rejigg | Packaging Company | New York | $5.8M | $984.4K | ~17% | Manufacturing | HARD-REJECT | Revenue below $10M floor; capital-intensive manufacturing |
| Rejigg | Boutique Branding & Marketing Strategy Agency | New York | $1.3M | $584.5K | ~45% | Marketing | HARD-REJECT | Revenue below $10M floor |
| Rejigg | NYC Metro Area Furniture Business | NYC metro | $1.4M | $529.4K (SDE) | ~37.8% | Retail | HARD-REJECT | Revenue below $10M floor; retail |
| Rejigg | Technology Infrastructure & Solutions Provider | Connecticut | $6M | $772K (SDE) | ~12.9% | IT Services | HARD-REJECT | Revenue below $10M floor; not vertical SaaS |
| Rejigg | Debt Collection & AR Management Firm | New York | $2.3M | $1.3M | ~56.5% | Professional Services | HARD-REJECT | Revenue below $10M floor; potential lending/credit exclude |
| Rejigg | Industrial Fluid Handling Equipment Supplier | New Jersey | $4.1M | $655.9K (SDE) | ~16% | Manufacturing / Distribution | HARD-REJECT | Revenue below $10M floor |
| Rejigg | Equine Veterinary Service | New Jersey | $2.5M | $500K (SDE) | ~20% | Healthcare / Veterinary | HARD-REJECT | Revenue below $10M floor |
| Rejigg | Commercial Real Estate Company | New York City | $2.7M | $1.1M | ~40.7% | Real Estate Services | HARD-REJECT | Revenue below $10M floor |
| Rejigg | Advertising Management Software Company | Connecticut | $1.3M | $450K (SDE) | ~34.6% | Software / Publishing | HARD-REJECT | ARR below $3M SaaS floor; horizontal/publishing software (not vertical SaaS) |
| Rejigg | Snow Removal Business | NYC metropolitan area | $1.3M | $780K (SDE) | ~60% | Facility Services | HARD-REJECT | Revenue below $10M floor; seasonal hard exclude |
| Rejigg | Medical Rehabilitation Equipment Dealer | Tri-state area | $1.3M | $389.9K (SDE) | ~30% | Healthcare Equipment | HARD-REJECT | Revenue below $10M floor |
| Rejigg | Electrical Supply Distributor | NYC area | $2.3M | $612.8K (SDE) | ~26.6% | Distribution | HARD-REJECT | Revenue below $10M floor |
| Rejigg | Professional Dog Boarding Business | New York | $68.8K | $64.3K (SDE) | ~93.5% | Consumer Services | HARD-REJECT | Consumer B2C; revenue far below floor |
| Rejigg | Food Distributor | NJ / Hudson Valley NY | $540K | $260K (SDE) | ~48.1% | Food / Distribution | HARD-REJECT | Revenue far below floor |
| Rejigg | Marketing Consulting Firm | New York | $500K | $400K | ~80% | Professional Services | HARD-REJECT | Revenue below $10M floor |
| Rejigg | Full Service Marketing Agency | New York | $653.8K | $175.2K | ~26.8% | Marketing | HARD-REJECT | Revenue below $10M floor |
| Rejigg | Branding Agency | New York | $249.7K | $135.1K (SDE) | ~54.1% | Marketing | HARD-REJECT | Revenue far below floor |
| Rejigg | Restoration & Mitigation Business | Connecticut | $1.5M | $350K (SDE) | ~23.3% | Restoration Services | HARD-REJECT | Revenue below $10M floor |
| Everingham & Kerr | Machining Services, Engineering & Waterjet Cutting Company (re-blast) | Southeastern US | $2.3M | $500K | ~21.7% | Machining / Engineering Services | HARD-REJECT | Revenue $2.3M below $10M floor; duplicate of morning scan listing |
| Everingham & Kerr | Project Widgets, Inc. — acquisition tombstone | Delaware | undisclosed | undisclosed | undisclosed | Enterprise Project Management Software | HARD-REJECT | Acquisition announcement (tombstone), not a for-sale listing |

---

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Rejigg | General | active | 200 | 30 | 0 | — |
| Flippa | General | blocked (single-attempt) | JS-shell | 0 | — | — |
| Everingham & Kerr | Email-only broker | active | email | 2 | 0 | — |

**Flippa note:** WebFetch returns only Angular template placeholders (`{{ listing.basic_info.name }}`). No server-rendered listing content. Agent-browser (`agent-browser install`) required for live data. Single-attempt block — not verified via second method. Next run should route through agent-browser.

---

## Volume Check

- Deals surfaced this afternoon: 0
- Deals surfaced this morning (full run): 0
- Combined today: 0
- 7-day rolling average: 0.17 deals/day (per morning artifact; no new matches to shift this)
- Target: 1–3/day — **BELOW TARGET**

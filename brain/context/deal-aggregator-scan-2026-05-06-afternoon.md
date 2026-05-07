---
date: 2026-05-06
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 2
sources_blocked_single_attempt: 1
email_deals: 6
buy_box_source: live
notes: "Afternoon top-up. 1 new Everingham & Kerr listing (B2B Trade Magazine Publisher, $2.2M rev / $1M EBITDA — both below Services buy-box floors, HARD-REJECT) + 5 new SMB Deal Hunter listings (auto parts retail, landscaping/snow, equipment attachments, asphalt/trail paving, septic/drain — all below $10M rev floor, $1.5M EBITDA floor, plus construction/manufacturing/retail hard-excludes). Zero PASS, zero NEAR-MISS clears, zero Slack posts. Rejigg homepage Next.js JS-shell (no listings in static markup, login-gated) — verified blocked. Flippa listing page redirects (302) to JS shell — verified blocked. E&K /listings/ web path returns 404 — verified blocked (E&K is email-only by design, web-side dead is expected). Morning artifact at brain/context/deal-aggregator-scan-2026-05-06.md is intact and untouched. Fingerprint store: 0 records (still empty since no PASS landed today)."
tags: [date/2026-05-06, deal-aggregator, scan-artifact, afternoon-top-up]
---
# Deal Aggregator Scan — 2026-05-06 (Afternoon Top-Up)

## Deals Surfaced (sent to Slack individually)

None today. 0 listings cleared the buy-box gate AND matched an active-niche corpus across afternoon email channel (Everingham & Kerr 12:32 ET blast, SMB Deal Hunter 12:21 ET blast) and rescanned time-sensitive web sources (Rejigg, Flippa, E&K web). All 6 new email-channel listings are disclosed-and-failed on the financial floor (Services buy-box: $10M revenue floor, $1.5M EBITDA floor) plus several hit industry hard-excludes (construction/labor-heavy, capital-intensive manufacturing, consumer retail). No Slack post sent. No fingerprint records added.

## Email Inbound Deals

1. **Everingham & Kerr — B2B Trade Magazine Publisher** (admin1@everkerr.com, msg `19dfe220a6dce1b5`, 2026-05-06 12:32 ET) | $2.2M revenue / $1M normalized EBITDA / ~45% margin / undisclosed geography | Industry: B2B trade publishing for the meetings industry | Verdict: HARD-REJECT — disclosed-and-failed on revenue floor ($10M) AND EBITDA floor ($1.5M); industry not in active-niche corpus.
2. **SMB Deal Hunter (Helen Guo) — Off The Grid issue, 5 listings** (helen@mail.smbdealhunter.xyz, msg `19dfe17be2d9014e`, 2026-05-06 12:21 ET / 16:21 UTC) | All 5 listings below G&B financial floors AND in hard-excluded industries — see Listings Reviewed log for per-listing detail.

## Near Misses (not Slacked)

- All 6 afternoon email-channel listings are HARD-REJECT (multiple disclosed-and-failed criteria plus industry hard-excludes); none clear the financial gate as a "near miss" candidate.
- No new web-source near misses surfaced — the 6 morning Business Exits + Synergy BB near misses (Telecom Caller Trust SaaS, CA Property Tax Consultants, GovCon IT, B2B Experiential Marketing, GovCon ERP, FL LED Display) remain on market per morning artifact and are not re-flagged here (intra-day dedup).
- Rejigg, Flippa, E&K web all dark this fire (Next.js JS-shell / 302 redirect / 404 respectively) — afternoon top-up depended on email channel for new flow, which delivered 6 listings (all rejected).

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Everingham & Kerr (email) | B2B Trade Magazine Publisher — Meetings Industry (3 print/online titles, ~30K paid+digital subs) | undisclosed | $2.2M | $1M | ~45% | B2B trade publishing / industry media | HARD-REJECT | Revenue $2.2M < $10M Services floor (disclosed); EBITDA $1M < $1.5M floor (disclosed); industry not in active-niche corpus |
| SMB Deal Hunter (email) | Automotive Parts E-Commerce + Retail Business (15-yr brand, Shopify + physical store, 8 employees, zero paid ads) | Southern California | $2.0M | $0.5M | ~25% | Auto parts e-comm + retail (DTC) | HARD-REJECT | Revenue < $10M floor (disclosed); EBITDA < $1.5M floor (disclosed); consumer retail/DTC hard-exclude; CA soft-flag |
| SMB Deal Hunter (email) | Landscaping & Snow Removal Co (40-yr operator, GM in place, 25 direct + 20-25 sub crews, lawn-maint contracts + per-push snow) | Southern Minnesota | $4.3M | $0.5M | ~12% | Commercial landscaping + snow removal | HARD-REJECT | Revenue < $10M floor (disclosed); EBITDA < $1.5M floor (disclosed); construction/labor-heavy field-services hard-exclude |
| SMB Deal Hunter (email) | Equipment Attachment Co (heavy-machinery add-ons for excavators/skid steers/tractors, 6-person team, contracts, $4.2M projected 2026 / 30%+ growth) | Connecticut | $3.2M | $0.65M | ~20% | Heavy-equipment attachment manufacturing | HARD-REJECT | Revenue < $10M floor (disclosed); EBITDA < $1.5M floor (disclosed); capital-intensive manufacturing hard-exclude |
| SMB Deal Hunter (email) | Asphalt & Trail Paving Contractor (gov't-bid trail builds for public lands/national parks, 4-person core scaling to 14 in season, IIJA-funded pipeline) | Utah | $1.3M | $0.45M | ~35% | Trail paving / asphalt contracting | HARD-REJECT | Revenue < $10M floor (disclosed); EBITDA < $1.5M floor (disclosed); construction hard-exclude |
| SMB Deal Hunter (email) | Septic & Drain Service Co (2024 launch, 40-yr operator, capturing only 35-40% of inbound calls, 4 trucks, lift-station line scaling, 2nd TX city license secured) | Texas | $1.0M | $0.4M | ~40% | Septic/drain field services | HARD-REJECT | Revenue < $10M floor (disclosed); EBITDA < $1.5M floor (disclosed); construction/labor-heavy field-services hard-exclude |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Everingham & Kerr (email channel) | General — Email-only broker | active | n/a (Gmail) | 1 | 0 | — |
| SMB Deal Hunter (email channel) | General — Newsletter blast | active | n/a (Gmail) | 5 | 0 | — |
| Rejigg (web) | General — Marketplace | blocked (verified) | 200 (JS shell, login-gated, 0 server-rendered listings) | 0 | 0 | — |
| Flippa (web) | General — Marketplace | blocked (verified) | 302 redirect → JS shell | 0 | 0 | — |
| Everingham & Kerr (web /listings/) | General — Email-only broker | blocked (single-attempt) | 404 | 0 | 0 | — |

**Notes:**
- Afternoon top-up scope per SKILL.md: lightweight rescan of email channel + time-sensitive platforms only. Skips full Channel 1 + 3 (covered in 6am morning run, see `brain/context/deal-aggregator-scan-2026-05-06.md`).
- Email channel rescan window: `newer_than:8h` against deal-flow senders (rejigg.com, everkerr.com, flippa.com) + broader broker-signal subject keywords ("for sale", "acquisition opportunity", "new listing", "now available", "retained to arrange", "CIM available"). Two new threads landed since morning run: E&K B2B Trade Magazine (12:32 ET) + SMB Deal Hunter Off The Grid blast (12:21 ET).
- E&K /listings/ 404 is consistent with E&K's email-only operating model (no public web listings page). Marking single-attempt rather than verified — E&K listings are delivered via email blast, web-dark is by design, not a fetch failure.
- **Fingerprint store status:** `brain/context/deal-aggregator-fingerprints.jsonl` is empty (0 records). All Last Match Date values therefore "—". Six afternoon listings hard-rejected on disclosed criteria → no fingerprints added.

## Volume Check
- Deals surfaced today (afternoon top-up): 0
- Deals surfaced today (cumulative across morning + afternoon): 0
- 7-day rolling average: 0/day
- Target: 1-3/day — **BELOW TARGET**. 5 consecutive zero-PASS days on web-scrapable channels; today's afternoon email channel surfaced 6 listings, all hard-rejected on financial floor. Friday 5/8 digest should include: (a) retire GP Bullhound /transactions/ (verified-dead 2 days running), (b) review Inside Self-Storage productivity (15 logged 5/6, 0 specialty wine/art/jewelry hits across 30+ days), (c) note SMB Deal Hunter pattern — newsletter consistently surfaces sub-$1M EBITDA deals which are below G&B floor; assess whether SMBDH is earning its slot or if it should be deprecated to intel-only.

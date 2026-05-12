---
date: 2026-05-12
run_mode: afternoon-top-up
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 1
sources_blocked_single_attempt: 0
email_deals: 0
buy_box_source: live (Services + Insurance + SaaS docs re-read from Drive this run)
morning_artifact_present: true
---
# Deal Aggregator Scan — 2026-05-12 (Afternoon)

Afternoon top-up run (`--afternoon`, 14:00 ET). Re-read buy-boxes + active niches from Drive. Lightweight rescan of email-driven channel + time-sensitive platforms (Rejigg, Flippa, Everingham & Kerr). Channel 1 + 3 full sweep already covered by morning run (`brain/context/deal-aggregator-scan-2026-05-12.md`, 0 deals, 4 NEAR-MISS, 5 FLAG, 8+ HARD-REJECT). Today's `email-scan-results-2026-05-12.md` now exists and is read this run; the morning artifact's "email channel gap (timing)" note is closed.

## Deals Surfaced (sent to Slack individually)

None today. 0 listings cleared the buy-box gate AND matched an active niche corpus. 0 Slack posts to `#active-deals` this run.

## Email Inbound Deals

None today. `email-scan-results-2026-05-12.md` was scanned: 0 CIMs, 0 broker blasts with for-sale signal, 0 broker-signal keywords matched in any inbound body (per email-intelligence Section 2 + Section 7 negative result). Only DIRECT inbound was Janet Crockett @ saltouncapital.com (investor admin, not deal flow). One BLAST classified — Tory @ Flippa marketplace promo — surfaced per `feedback_marketplace_vs_broker_distinction` as marketplace cattle-call, NOT broker channel; promoted assets (Test Prep App, SocMed SaaS, Connected Lifestyle Brand, card game store, family gift brand, education app) are all out of every G&B buy-box.

## Near Misses (not Slacked)

- **Flippa marketplace promo (Tory)** — already classified BLAST by email-intelligence at 07:00 ET. Promoted assets land outside Services / Insurance / SaaS buy-boxes (consumer / digital / education). No-action; logged for cross-day dedup awareness only.
- **BROWSER_AUTOMATION_UNAVAILABLE** — `agent-browser` is not installed on this host (`which agent-browser` = command not found). Flippa scrape blocked at platform layer; verified blocked. Infra ask unchanged from morning artifact: `npm i -g agent-browser && agent-browser install`.
- **Everingham & Kerr** — homepage 200 OK (everkerr.com, 85KB). Per SKILL.md classification, E&K is email-only with no public listings page (homepage carries no `/listings`, `/for-sale`, or `/businesses` route). E&K coverage for today flows through the email channel, which produced 0 broker-signal matches in `email-scan-results-2026-05-12.md`.

## Listings Reviewed (full log)

10 listings parsed from Rejigg `/businesses` this run. All sit on the wrong side of the Services Buy-Box financial floor ($10M revenue / $1.5M EBITDA / 10% margin) OR hit an industry hard-exclude. Zero clear the gate. Sort order: PASS → NEAR-MISS → FLAG → HARD-REJECT.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Rejigg | Indiana Limestone Company | IN | $17,000,000 | $3,000,000 | 17.6% | Quarry / Stone Extraction | HARD-REJECT | Services BB hard-exclude: capital-intensive manufacturing |
| Rejigg | Bar & Restaurant | CA | $520,000 | $101,378 | 19.5% | Hospitality / F&B | HARD-REJECT | Services BB hard-exclude: restaurants/hospitality/nightlife; rev $520K below $10M floor; CA soft-flag |
| Rejigg | Asphalt Paving and Maintenance Business | WI | $1,119,371 | $304,941 | 27.2% | Construction Services | HARD-REJECT | Services BB hard-exclude: construction/labor-heavy field services; rev below floor |
| Rejigg | Oxidizing Cleaning Solution Company | NC | $700,000 | $100,000 | 14.3% | Consumer Cleaning Products | HARD-REJECT | Services BB hard-exclude: consumer retail/DTC (sells to individual consumers per blurb); rev below $10M floor |
| Rejigg | Hair and Beauty Care Retailer | VA | $657,737 | $84,684 | 12.9% | Consumer Retail | HARD-REJECT | Services BB hard-exclude: consumer retail/DTC; rev below $10M floor |
| Rejigg | Broadcast Equipment Supplier | FL | $1,900,000 | -$31,000 | -1.6% | Broadcast Equipment Dealer | HARD-REJECT | Negative EBITDA (disclosed-and-failed); rev below $10M floor |
| Rejigg | Enterprise Risk Management Software | NV | $525,000 | $57,700 | 11.0% | Horizontal SaaS (ERM) | HARD-REJECT | SaaS BB hard-exclude: ARR below $3M floor; horizontal/risk-mgmt SaaS, not vertical-luxury |
| Rejigg | Hauling / Junk Removal Company | PA | $208,107 | $112,857 | 54.2% | Hauling / Junk Removal | HARD-REJECT | Rev $208K below $10M floor; labor-heavy field services |
| Rejigg | B2B Fire Safety Equipment Dealer | TX | $2,426,491 | $164,993 | 6.8% | Fire Safety Equipment | HARD-REJECT | Rev below floor; margin 6.8% below 10% Services BB floor (disclosed-and-failed) |
| Rejigg | Home Lease & Furnishings Business | AL | $2,727,464 | $310,725 | 11.4% | Consumer Furnishings / Rentals | HARD-REJECT | Services BB hard-exclude: consumer retail-adjacent; rev below floor |

## Source Scorecard

Time-sensitive sources scanned this afternoon run only. Channel 1 + 3 full sweep is the morning run's responsibility (see morning artifact's Source Scorecard for the 17-source row set).

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Rejigg | General | active | 200 | 10 | 0 | — |
| Everingham & Kerr | General | active | 200 (homepage; email-only for listings) | 0 | 0 | — |
| Flippa | General | blocked (verified) | — (agent-browser unavailable) | 0 | 0 | — |
| Email channel (email-scan-results-2026-05-12.md) | General | active | N/A (artifact-read) | 0 | 0 | — |

**Notes:**
- **Rejigg** — `/businesses` page returned full embedded listing JSON for 10 active listings. None cleared the buy-box; all HARD-REJECT (financial floor or industry hard-exclude). Morning artifact correctly flagged Rejigg as email-channel pending; afternoon top-up confirms zero PASS via direct platform scrape as well.
- **Everingham & Kerr** — homepage healthy, no listings route, email-only per SKILL.md. Email channel coverage for the 2-day window is captured in `email-scan-results-2026-05-12.md` (0 broker-signal matches). No new for-sale-keyword inbound.
- **Flippa** — JS-shell / agent-browser required. Host has no `agent-browser` install (verified `which agent-browser` = not found). Per SKILL.md stop hook, surfaced explicitly. Tory @ Flippa marketplace promo classified BLAST by email-intelligence and dispositioned per `feedback_marketplace_vs_broker_distinction`.
- **Email channel** — `email-scan-results-2026-05-12.md` exists this run (was missing at 06:03 ET morning fire). Scanned for: CIMs, broker blasts with deal teasers, intro forwards, NDA follow-ups. Result: 0 deal-classified items, 0 broker-signal keywords matched in inbound body, 0 introduction signals.

## Volume Check

- Deals surfaced this afternoon run: **0**
- Day total (morning + afternoon): **0**
- 7-day rolling average: **0** (fingerprint store remains empty — 0 entries in `brain/context/deal-aggregator-fingerprints.jsonl`)
- Target: 1–3/day — **BELOW TARGET**

**Diagnostic:** Combined day produced 4 financial-gate-clearing NEAR-MISS listings (govcon IT, experiential marketing, govcon ERP, LED display — all from morning) plus 0 from afternoon. Pattern: listings clear $10M / $1.5M EBITDA / 10% margin floors but sit in industries outside the eight active-niche corpora (Pest, Art Advisory, Estate Mgmt, Coffee Equipment, Cleaning, Luxury SaaS, Specialty Insurance, HV Storage). Afternoon Rejigg sweep added 10 sub-floor / hard-exclude listings (consumer retail, hospitality, construction, quarry, horizontal SaaS) — none in the financial band, so no NEAR-MISS additions. Email channel produced no inbound deal signal today. Infra ask outstanding: agent-browser install would unblock Flippa + BizBuySell, the two largest scraper-403 sources by likely volume.

**Corpus path log (re-resolved this run):** Active niche list unchanged from morning fire — 8 active niches, same DealsX↔WR foreign-key resolution, same corpus build. Private Art Advisory remains the only WR-row-built corpus (DealsX Niche field blank); other 7 use DealsX keywords primary + WR Quick notes supplementary.

---
date: 2026-04-29
run: afternoon
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 0
sources_blocked_single_attempt: 0
email_deals: 4
buy_box_source: live
morning_artifact_present: true
---
# Deal Aggregator Scan — 2026-04-29 (Afternoon Top-Up)

Lightweight afternoon rescan of email channel + time-sensitive platforms (Rejigg, Flippa, Everingham & Kerr). 4 deal-bearing inbounds since the 7 AM email-intelligence run plus 25 Flippa SaaS listings reviewed via agent-browser. Zero cleared the buy-box gate against an active niche. No Slack posts.

## Deals Surfaced (sent to Slack individually)

None today.

## Email Inbound Deals

None today (afternoon window). 4 deal-bearing emails landed between morning artifact write and 2 PM ET, but all four are near-miss / hard-exclude — see Near Misses below.

## Near Misses (not Slacked)

- **Everingham & Kerr — Machining Services, Engineering & Waterjet Cutting Company** (Southeastern US, $2.3M revenue, $500K normalized EBITDA, sent 12:46 PM ET 4/29). Three disclosed-and-fails: revenue floor ($2.3M < $10M Services BB), EBITDA floor ($500K < $1.5M Services BB), industry hard-exclude (capital-intensive manufacturing per Services BB). Clean auto-reject.
- **Quiet Light — "Passion-Driven DTC Brand, 187% YoY Growth, 367K Email Subscribers"** (custom collectible/hobbyist DTC ecommerce, sent 2:00 PM ET 4/29). Industry hard-exclude (consumer retail / DTC per Services BB). Not relevant to any active thesis.
- **Quiet Light — "Distressed Dual-Portfolio Baby Brand, 25-Year Legacy"** (DTC consumer brand, distressed asset, 7-10 day close, sent 10:00 AM ET 4/29). Industry hard-exclude (consumer retail / DTC). Distressed-asset framing also off-thesis.
- **Helen Guo SMB Deal Hunter — "New Off-Market Businesses For Sale"** (HVAC company + vehicle wrap shop blast, sent ~12:52 PM ET 4/29). HVAC = construction/labor-heavy field services hard-exclude; vehicle wrap = consumer retail hard-exclude. Newsletter-style blast, not personalized.
- **Flippa — 25 SaaS listings (page 1, $250K revenue / $1M price filters)** scanned via agent-browser. Sample: India education SaaS $63K ARR (below floor); Israel AI commerce platform negative EBITDA (auto-reject); UAE spyderads.app age 1 yr (below 5+); Hong Kong astrology B2C (hard-exclude); UAE video hosting horizontal infrastructure; DE "Augmented Agentic Infrastructure" $4.28M revenue + $2.86M annual EBITDA disclosed-and-passes financials but reads as horizontal infrastructure / contract-financing structure (not vertical SaaS — fails SaaS BB structural filter). Closest financial near-miss is the DE listing; flag for re-scan if next iteration discloses a clearer vertical/customer-base.

## Source Scorecard

Afternoon top-up only — full source coverage was logged in the morning artifact. Rows below = sources actually scanned this afternoon run.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Email channel (Superhuman, since 7 AM ET) | General (Email) | active | n/a | 4 | 0 | — |
| Rejigg | General (Email) | active | n/a | 0 | 0 | — |
| Everingham & Kerr | General (Email) | active | n/a | 1 | 0 | — |
| Flippa | General (Web) | active | 200 | 25 | 0 | — |

**Status notes:**
- Flippa: WebFetch returned `JS_SHELL_NO_LISTINGS` on first attempt (template placeholders, JS-rendered). Per SKILL.md routing rule, second attempt via `agent-browser open` + `agent-browser snapshot -i` succeeded — 25 SaaS listings parsed cleanly. Source is alive and scrapable through agent-browser; promote off the Cloudflare-blocked watchlist for next Friday's source-stewardship digest.
- Email channel: 4 deal-bearing inbounds since morning artifact (1 E&K + 2 Quiet Light + 1 Helen Guo). All near-miss / hard-exclude — none Slack-worthy.
- Rejigg: zero new afternoon blasts (`from:rejigg.com newer_than:6h` → 0 results).
- Everingham & Kerr: one new acquisition email (Machining/Waterjet, near-miss).

## Volume Check

- Deals surfaced today (afternoon top-up): 0
- Deals surfaced today (full day, morning + afternoon): 0
- 7-day rolling average: ~0/day (fingerprint store empty since launch; no Slack matches recorded)
- Target: 1-3/day — **BELOW TARGET**

Afternoon flow consistent with morning read: web-scrape and email channels are healthy (94 morning + 25 afternoon listings parsed; 4 afternoon deal emails received), but listing populations skew DTC ecommerce / horizontal SaaS / capital-intensive manufacturing — orthogonal to G&B's luxury-services / vertical-SaaS-for-luxury / specialty-insurance theses. Funnel gap is structural to the channels, not a fetch problem. One actionable signal for Friday digest: Flippa via agent-browser is scrapable — the SaaS facet returned 5,342 total open listings with parseable facets (Industry, Monthly Profit, Site Age, Sale Type, Asset Type), so deeper-page sweeps with vertical-luxury keyword filters (jewelry, art, wine, yacht, equestrian, hospitality) could plausibly surface a thesis match the pagination-1 default sort missed.

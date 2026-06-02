---
date: 2026-06-02
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 0
sources_blocked_single_attempt: 3
email_deals: 0
buy_box_source: live
morning_artifact_present: true
niche_corpus_note: "Active niches re-confirmed from WEEKLY REVIEW tab. 8 active niches (Active-Outreach + Active-Long Term). Buy-box docs re-read live from Drive."
---
# Deal Aggregator Scan — 2026-06-02 (Afternoon Top-Up)

**Run:** 2026-06-02 · Headless afternoon mode (`--afternoon`) · 2:00 PM ET
**Scope:** Time-sensitive platforms (Rejigg, Flippa, Everingham & Kerr) + email channel re-check only. Full Channel 1 + 3 sweep covered by morning run.

---

## Deals Surfaced (sent to Slack individually)

None today.

---

## Email Inbound Deals

None. `email-scan-results-2026-06-02.md` (morning intelligence run) processed 10 email-blast listings — all HARD-REJECT, zero buy-box matches, zero CIMs. No afternoon email-intelligence artifact (email-intelligence runs once at 7am). No new inbound deal emails detected beyond morning run coverage.

---

## Near Misses (not Slacked)

None. All time-sensitive platforms blocked via direct fetch this run (see Source Scorecard). Email channel fully covered by morning artifact — 10 listings processed, all HARD-REJECT.

---

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Flippa (email digest) | Business Acquisition Platform (3-yr-old) | undisclosed | $2.4M | undisclosed | 69% | Business Education / Training SaaS | HARD-REJECT | Already processed in morning run; fingerprint check confirms morning coverage. Revenue below SaaS ARR floor ($3M min); no active-niche match |
| Flippa (email digest) | Spiritual Guidance Shopify Brand | undisclosed | $1.5M | undisclosed | undisclosed | Ecommerce / Spiritual Wellness | HARD-REJECT | Already processed in morning run; DTC/consumer hard-excluded |
| Flippa (email digest) | Pet Portrait Shopify Brand | undisclosed | $141K | undisclosed | undisclosed | Ecommerce / Pet Products | HARD-REJECT | Already processed in morning run; DTC/consumer hard-excluded; revenue far below floor |
| Flippa (email digest) | Cornwall Travel Platform / Facebook Page | Cornwall, UK | $44K | undisclosed | undisclosed | Digital Media / Travel | HARD-REJECT | Already processed in morning run; non-US; travel; revenue far below floor |
| Flippa (email digest) | Mobile App (2 years old, 5500% growth) | undisclosed | $166K TTM | $83K TTM | undisclosed | Mobile App | HARD-REJECT | Already processed in morning run; operating history under 5 years; revenue far below floor |
| Flippa (email digest) | Mixology WooCommerce Store | undisclosed | $149K | undisclosed | undisclosed | Ecommerce / Food & Beverage | HARD-REJECT | Already processed in morning run; DTC/consumer hard-excluded; revenue far below floor |
| Flippa (email digest) | AI Middleware SaaS (66% share) | undisclosed | $481K | undisclosed | 59% | SaaS / AI Infrastructure | HARD-REJECT | Already processed in morning run; ARR far below $3M SaaS floor; horizontal not vertical SaaS |
| Everingham & Kerr (email) | Monthly Client Report (PDF link only — no listing body data) | undisclosed | undisclosed | undisclosed | undisclosed | Various | FLAG | Email body contained only a link to external PDF; no listing-level data extractable from email |
| Rejigg (email) | Re-engagement email (no listings section) | undisclosed | undisclosed | undisclosed | undisclosed | N/A | FLAG | Re-engagement email only; no deal listings included |

---

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Rejigg | General | blocked (single-attempt) | 404 (JS shell — `/listings` and `/businesses-for-sale` both 404 after redirect) | 0 new (re-engagement email only, no listings; already captured morning) | 0 | — |
| Flippa | General | blocked (single-attempt) | 404 (`/businesses` path; JS-rendered, agent-browser required) | 7 (already processed in morning run via email digest) | 0 | — |
| Everingham & Kerr | General | blocked (single-attempt) | 404 (`/current-listings`, `/listings`, `/businesses-for-sale` all 404) | 0 new (monthly report email had PDF link only; no listing body data; already captured morning) | 0 | — |
| Email channel | General | active (morning artifact read) | N/A | 9 (7 Flippa + 1 E&K email + 1 Rejigg email — all already reviewed morning) | 0 | — |

**Note on platform blocks:** All three time-sensitive platforms (Rejigg, Flippa, Everkerr) are JS-rendered or have non-standard listing paths. Direct curl scraping returns 404 or renders an empty JS shell. Per SKILL.md, these require agent-browser for live scraping. Marking as `blocked (single-attempt)` — only one fetch attempt made per platform. Email coverage (morning run) remains the primary access channel for all three; no afternoon-specific email blasts detected. Agent-browser is not installed (`BROWSER_AUTOMATION_UNAVAILABLE`).

---

## Volume Check
- Deals surfaced today (morning + afternoon combined): 0
- 7-day rolling average: 0.0/day
- Target: 1–3/day — **BELOW TARGET**

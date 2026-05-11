---
date: 2026-05-11
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 0
sources_blocked_single_attempt: 1
email_deals: 0
buy_box_source: live
morning_artifact_missing: false
run_mode: afternoon
---
# Deal Aggregator Scan — 2026-05-11 (Afternoon Top-Up)

Lightweight afternoon rescan per SKILL.md `--afternoon` path. Re-read buy-boxes (Services / Insurance / SaaS, all live from Drive). Re-read WEEKLY REVIEW active niches (8 Active rows: Premium Pest, Private Art Advisory, Estate Mgmt, Specialty Coffee Equipment, High-End Commercial Cleaning, Vertical SaaS, Specialty Insurance Brokerage, Specialty Storage). Rescanned time-sensitive sources only — Rejigg, Flippa, Everingham & Kerr — plus a re-read of the email channel via `email-scan-results-2026-05-11.md`. Channels 1 (full broker sweep) and 3 (niche-specific) skipped per afternoon run spec — morning run covered.

## Deals Surfaced (sent to Slack individually)

None today.

## Email Inbound Deals

None today. `email-scan-results-2026-05-11.md` (Monday 7am email-intelligence artifact) confirms 0 DIRECT, 0 broker BLASTs, 0 CIMs, 0 NDAs, 0 introductions. The only BLAST-classified emails today were automated (Google DMARC aggregate report + Uber receipt) — not broker deal flow. No new email-inbound deals landed between morning run and afternoon run.

## Near Misses (not Slacked)

- **Flippa (`flippa.com`) blocked — JS shell, agent-browser unavailable.** Homepage returns 200 but listing content is rendered client-side (Turbo/Stimulus app). Per SKILL.md routing, Flippa requires `agent-browser`, which is not installed on this server. Logged as `blocked (single-attempt)`. Surface for next-run retry / install resolution.
- **Everingham & Kerr (`everkerr.com`) — no afternoon blast email.** Email-channel scan shows no Everingham & Kerr inbound today. `/recent-transactions/` page contains closed deals only (not active flow). Email-only channel confirmed dark for the afternoon window.

## Listings Reviewed (full log)

Sorted: PASS first, then NEAR-MISS, then FLAG, then HARD-REJECT. Zero PASS / NEAR-MISS / FLAG today; all 10 reviewed Rejigg listings hard-reject on disclosed industry hard-excludes or disclosed-and-failed financial floors.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Rejigg | Oxidizing Cleaning Solution Company | undisclosed | $700K | $100K | 14% | Consumer DTC chemical/cleaning | HARD-REJECT | Consumer DTC hard-exclude + revenue below $10M Services floor |
| Rejigg | Hair and Beauty Care Retailer | undisclosed | $658K | $85K | 13% | Consumer retail (haircare/skincare) | HARD-REJECT | Consumer retail/DTC hard-exclude + revenue below floor |
| Rejigg | Broadcast Equipment Supplier | undisclosed | $1.9M | -$31K | negative | Broadcast equipment distribution | HARD-REJECT | Negative EBITDA (disclosed) + off-thesis distribution + revenue below floor |
| Rejigg | Indiana Limestone Company | IN | $17M | $3M | 18% | Limestone fabrication/manufacturing | HARD-REJECT | Capital-intensive manufacturing hard-exclude |
| Rejigg | Bar & Restaurant | CA | $520K | $101K | 19% | Restaurant + venue rental | HARD-REJECT | Restaurants/hospitality hard-exclude + below revenue floor (CA soft-flag also fires) |
| Rejigg | Enterprise Risk Management Software | undisclosed | $525K | $58K | 11% | Horizontal enterprise SaaS | HARD-REJECT | Horizontal SaaS hard-exclude + ARR below $3M SaaS floor |
| Rejigg | Hauling / Junk Removal Company | PA | $208K | $113K | 54% | Labor-heavy field service (junk removal/demolition) | HARD-REJECT | Construction/labor-heavy field-services hard-exclude + revenue below floor |
| Rejigg | Asphalt Paving and Maintenance Business | WI | $1.12M | $305K | 27% | Construction trades (paving) | HARD-REJECT | Construction hard-exclude + revenue below floor |
| Rejigg | B2B Fire Safety Equipment Dealer | undisclosed | $2.43M | $165K | 6.8% | Equipment distribution + inspection services | HARD-REJECT | EBITDA margin below 10% floor (disclosed-and-failed) + revenue below floor |
| Rejigg | Home Lease & Furnishings Business | undisclosed | $2.73M | $311K | 11% | Rent-to-own consumer leasing | HARD-REJECT | Lending / credit extension hard-exclude + consumer model + revenue below floor |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Rejigg | General (time-sensitive) | active | 200 | 10 | 0 | — |
| Flippa | General (time-sensitive) | blocked (single-attempt) | 200 (JS shell) | 0 | — | — |
| Everingham & Kerr | Email-only broker (time-sensitive) | active | 200 | 0 | 0 | — |
| Email channel | Inbound | active | n/a | 0 | 0 | — |

**Notes:**
- Rejigg: scraped via `__NEXT_DATA__` JSON payload at `/businesses` (server-side hydration). All 10 listings parsed, 0 buy-box matches.
- Flippa: homepage returns 200 but listings render via Turbo/Stimulus client-side bundle. Per SKILL.md, requires `agent-browser`. `which agent-browser` → not installed on this server. Marked `blocked (single-attempt)` not `blocked (verified)` — install path is a separate task; not a dead source.
- Everingham & Kerr: confirmed email-only for active flow. `/recent-transactions/` page enumerates closed deals (descriptors like "has been acquired by"), no active listings. Email channel today = 0 Everkerr blasts.
- Email channel: `email-scan-results-2026-05-11.md` reports 0 DIRECT inbound, 0 broker BLASTs, 0 CIMs/NDAs/intros today. Both detected BLAST emails (Google DMARC, Uber receipt) are automated transactional, not broker deal flow.

## Volume Check

- Deals surfaced today (combined morning + afternoon): 0
- Morning run: 0 deals (per `brain/context/deal-aggregator-scan-2026-05-11.md`)
- Afternoon run: 0 deals (this artifact)
- 7-day rolling average: ~0.3/day (estimated; full count would query fingerprint store + prior-week scan artifacts — fingerprint store is empty for the last 30 days)
- Target: 1-3/day — **BELOW TARGET**

Afternoon top-up added no new flow; Friday digest (`--digest-mode` 6am ET) will surface source-productivity context for the week.

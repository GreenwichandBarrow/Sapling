---
date: 2026-04-02
matches_found: 0
near_misses: 4
platforms_scanned: 8
platforms_accessible: 5
platforms_blocked: 3
---
# Intermediary Scan — 2026-04-02

## Matches (sent to Slack individually)
None. No actionable matches today.

Business Exits had 3 listings that financially fit the buy box, but all are Sale Pending and B2G (government contracts), not B2B:
- GovCon IT Firm (Judiciary & VA) — $19.7M rev / $3.4M EBITDA — Sale Pending
- B2B Experiential Marketing Vendor — $14.3M rev / $3.3M EBITDA — Sale Pending
- Government Contract ERP Service — $14M rev / $2.6M EBITDA — Sale Pending

Not Slacked: Sale Pending = not actionable. B2G = outside buy box (B2B/B2B2C required).

## Near Misses (not Slacked)

1. **California Property Tax Consultants** — Business Exits | $6.7M rev | $4.7M EBITDA | 70% margins | Compliance-adjacent (tax consulting for businesses) | California soft filter applies | Active listing (not pending) | URL: businessexits.com
   - Strongest active near miss. Exceptional margins. Compliance infrastructure thesis-adjacent. California is the only filter it fails.

2. **Insurance Agency SaaS Marketing Platform** — Website Closers | $3.7M ARR | $804K SDE | 98% gross margins | 850+ clients, 3% churn, 10+ years | Ask: $6M | URL: https://www.websiteclosers.com/businesses/saas-marketing-automation-platform-3-7m-arr-10-year-business-3-churn-rate-850-active-clients-proprietary-tech-stack-6-000-ltv/113889/
   - Thesis-adjacent (insurance agencies). But SDE $804K is well below $2M EBITDA floor. ARR $3.7M below $5M software floor. Too small.

3. **Diversified Environmental Services Provider** — Woodbridge/Mariner | $10.2M rev | $2.0M EBITDA | ~20% margins | Day 2, still listed | Teaser: https://marinerholdingsllc.app.box.com/s/i3n9f45vq4ah5exum5blqeioegf9sq58
   - EBITDA at floor. Not within active thesis. Competitive process (Woodbridge has 3000+ buyers). Carried from yesterday.

4. **MedTech Market Intelligence Provider** — Woodbridge/Mariner | $5.9M rev CAD | $2.1M EBITDA CAD | 35% margins | B2B market research for medical device/pharma
   - Revenue below $10M services floor (and in CAD). Regulated-industry data, compliance-adjacent. Worth monitoring.

## Niche Signals
- **Environmental remediation/compliance** — Woodbridge listing (Day 2). Still only 1 listing at scale. Below signal threshold (need 2+ across platforms or 3+ from same platform).
- **Insurance agency SaaS** — 1 listing (Website Closers, sub-scale at $804K SDE). Confirms insurance agencies buy marketing automation but this specific deal is too small.
- **Property tax consulting** — 1 listing (Business Exits, $4.7M EBITDA, 70% margins). Compliance infrastructure thesis-adjacent. First sighting. Monitor.
- **Government IT services/ERP** — 3 pending listings on Business Exits. B2G market active but outside buy box (not B2B).
- No signals meet the 2+ platform threshold for forwarding to niche-intelligence.

## Platform Status

### Accessible (5)
- **Rejigg:** Accessible. ~1,052 listings but only 10 visible without auth. Skews small ($500K-$5M). 0 matches.
- **Woodbridge/Mariner:** Accessible at new URL `/current-engagements/` (old URLs 404). 17 listings. 0 new matches. Environmental Services still listed.
- **Paine Pacific:** Accessible. 4 active + 4 upcoming (unchanged). 0 matches. HR Software + Cyber Security still upcoming — monitor.
- **Website Closers:** Partially accessible. Archive loads but no bulk financials. Individual listings accessible. ~1,500+ listings, heavily eCommerce. 0 matches.
- **Business Exits:** Fully accessible. 27 listings. 3 Sale Pending B2G matches (not actionable). 1 strong near miss (CA Property Tax).

### Blocked/Down (3)
- **ProNova Partners:** BLOCKED (403 on all pages). Was accessible yesterday. Bot-blocking tightened. Needs headless browser or email registration.
- **Gottesman Company:** DOWN (503 on all listing pages). Temporary — retry tomorrow.
- **Quiet Light:** BLOCKED (Cloudflare challenge). Requires real browser session. Same as yesterday.

### Not scanned today (skipped per rotation)
- Benchmark International — login-gated (Nexus portal)
- Flippa — not accessible
- DealForce — not accessible
- BizBuySell — login required
- FE International — login required
- Graphic Arts Advisors — recommend removal (print-only, wrong sector)
- Viking Mergers — email-only
- Everingham & Kerr — NDA-gated, no public listings

## Introduction Signals
- No new broker introductions detected in email-scan-results-2026-04-01.
- No email-scan-results for 2026-04-02 yet (email-intelligence hasn't run today).

## Recommendations
1. **Woodbridge URL update:** Change scan URL from `/current-projects/` to `/current-engagements/` in skill
2. **ProNova workaround:** Register for email deal flow directly, or implement headless browser scanning
3. **California Property Tax Consultants:** Kay's call — exceptional margins (70%), compliance-adjacent, but California soft filter. Worth pulling the CIM?
4. **Remove Graphic Arts Advisors** from rotation (print-only, wrong sector) — carried from yesterday
5. **Paine Pacific watch:** HR Software + Cyber Security listings still upcoming — check daily

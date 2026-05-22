---
schema_version: "1.0.0"
date: 2026-05-22
type: tracker
title: "Deal Aggregator Weekly Digest — 2026-05-22"
window_start: 2026-05-15
window_end: 2026-05-22
volume_7d_avg: 0.29
volume_prior_week_avg: 0.0
volume_status: "🔴 Critical"
proposed_additions: 2
proposed_retirements: 0
opportunistic_count: 0
sourcing_sheet_source: live
fingerprint_store_status: sparse
tags:
  - date/2026-05-22
  - tracker
  - topic/deal-aggregator
  - topic/weekly-digest
  - status/draft
---

# Deal Aggregator Weekly Digest — 2026-05-22

Window: **2026-05-15 → 2026-05-22** (5 weekday scans: Thu 05-15, Mon 05-18, Tue 05-19, Wed 05-20, Thu 05-21; Fri 05-22 morning daily-scan fires on a separate plist and isn't read by this digest. Weekend gaps 05-16/05-17 are expected — no scheduled scan.)

## 1. Source Productivity (Last 7 Days)

| Source | Category | 7d Matches | 7d Listings Reviewed | Last Match | Trend |
|---|---|---:|---:|---|:---:|
| Business Exits | General | 0 | 150 | — | → |
| Synergy Business Brokers | General | 0 | 100 | — | → |
| Empire Flippers | General | 0 | 76 | — | → |
| Website Closers | General | 0 | 51 | — | → |
| Synergy BB Real Estate | Niche / Estate Mgmt | 0 | 33 | — | → |
| Sica Fletcher | Niche / Specialty Insurance | 0 | 27 | — | ↑ |
| GP Bullhound | Niche / Vertical SaaS | 0 | 6 | — | → |
| Quiet Light | General | 0 | 1 | — | → |
| BizBuySell | General | 0 | 0 | — | → |
| DealForce | General | 0 | 0 | — | → |
| Everingham & Kerr | General | 0 | 0 | — | → |
| Flippa | General | 0 | 0 | — | ↓ |
| IAG M&A Advisors | General | 0 | 0 | — | → |
| PCO Bookkeepers | Niche / Premium Pest | 0 | 0 | — | → |
| Rejigg | General | 0 | 0 | — | → |
| SMB Deal Hunter (Helen Guo) | General | 0 | 0 | — | → |
| Viking Mergers | General | 0 | 0 | — | → |

- Sources rows = 17 (all sheet-Active sources on General + Niche-Specific tabs).
- Total listings reviewed across the week: **444** — concentrated on Business Exits / Synergy / Empire Flippers / Website Closers (general-platform horsepower); Sica Fletcher up sharply (7 → 27) on a denser tombstone window.
- Total buy-box matches across the week: **0** from scanned sources. (DealsX-channel inbound = 2; reported in Section 2 volume, doesn't appear in the platform-source table by spec.)
- Trend column compares to prior digest 2026-05-15 (window 05-08 → 05-15). Sica Fletcher ↑ on listings reviewed (still 0 matches). Flippa ↓ (6 → 0 listings reviewed; web path Cloudflare-gated, email-routed broker-blasts were silent this window). All others → (within ±50% of prior week's listings reviewed).
- **`fingerprint_store_status: sparse`** — `brain/context/deal-aggregator-fingerprints.jsonl` has 2 records (both DealsX-channel leads from 05-18 / 05-19). Zero platform-source matches have ever been written. "Last Match" column reads `—` for every platform source: instrument exists, scanned channels have not produced a PASS to write.

## 2. Volume Check

- 7-day rolling average: **0.29/day** (2 DealsX-channel inbound leads ÷ 7 days)
- Target: 1–3/day
- Status: **🔴 Critical**
- Prior-week average (05-08 → 05-15): 0.0/day → +0.29 week-over-week (DealsX-channel started producing inbound). Platform-source contribution still 0.
- Read: 444 listings reviewed across 5 weekday scans is healthy scan throughput; the gap is at the buy-box gate, not at scan coverage. Three consecutive 🔴 weeks (04-25→05-02, 05-08→05-15, 05-15→05-22) on platform-source volume. Either (a) the active niche corpora are too narrow to convert general-platform scan volume, or (b) the disclosed-field discipline is auto-flagging every candidate to FLAG/NEAR-MISS rather than PASS. Worth a deliberate calibration pass — see Section 5.

## 3. Proposed Additions

1. **Digital Capital Advisors (DCA)** — General Sources | https://www.digitalcapitaladvisors.com/
   - Why: Carlos Nieto (`carlos@digitalcapitaladvisors.com`) delivered an unsolicited sell-side teaser on 2026-05-19 ("Project Drone", precision-agriculture / agtech) with attached `Drone teaser T2.pdf` (5.3 MB). Active sell-side broker behavior. DCA is a lower-middle-market M&A advisory; the Carlos relationship was warm via in3o, but DCA the firm appears to push proactive deal flow to qualified buyers, so it earns a recurring slot rather than one-off email handling.
   - Recommended tab: **General Sources** (cross-industry M&A advisory)
   - Access: **Email + relationship** — live-check `https://www.digitalcapitaladvisors.com` returns HTTP 200 (browser UA; scraper UA gets 403, consistent with marketing site Cloudflare profile). Listings not publicly browsable — flow is broker-direct email teasers like Project Drone.
   - Type: `email-only broker` (advisory + deal platform sub-classification)
   - **RECOMMEND: Add to General Sources — status `Active - email-only`** → YES / NO / DISCUSS

2. **Transworld Business Advisors (NY)** — General Sources | https://www.tworld.com/
   - Why: Sam Curcio (`scurcio@tworld.com`) confirmed a Zoom call this window after a warm intro from Becky Wuest Creavin (Peapack Private). Transworld is a national LMM broker franchise with a public marketplace at tworld.com and active branch-level deal flow. Per `feedback_franchise_firm_one_entry_only`, ONE row per firm — the NY branch (Sam) is Kay's engagement point; the firm-level marketplace URL covers the broader listings surface.
   - Recommended tab: **General Sources**
   - Access: **Public marketplace + relationship** — live-check `https://www.tworld.com` returns HTTP 200 (browser UA). Marketplace listings publicly browsable; relationship channel through Sam (NY branch).
   - Type: `marketplace` (with email-only relationship overlay)
   - **RECOMMEND: Add to General Sources — status `Active - relationship + marketplace`** → YES / NO / DISCUSS

(All other unknown sender domains in the inbox window were classified out: villagesearchpartners.com / pozacp.com = searcher peers, not deal sources; bkgrowth.com = independent-sponsor peer; dododigital.ai / startvirtual.com = internal advisor/VA infra; oberle-risk.com = insurance-DD provider for searchers, intel-only; peapackprivate.com = warm-intro source [Becky], not a deal source itself; in3o.com = warm-intro source [Carlos's other firm], the deal-source classification lands on Digital Capital Advisors above; tristate-stl.com / emiliomiti.com = DealsX-lead landing domains, not sources. None merit a separate Sourcing Sheet row.)

## 4. Proposed Retirements

None this week.

- Per SKILL.md `<weekly_digest>` retirement-side spec, a proposed retirement requires (a) 30+ days no fingerprint-attributed match AND (b) 3 live-checks performed (URL resolves, domain registered, email-channel status). The fingerprint store now has 2 records (both DealsX-channel, since 2026-05-18), but zero platform-source matches have ever been written — so signal (a) remains undefined for every scanned source. Per `feedback_test_before_concluding_channel_dead`, never retire on absent data — silence from an instrument that has never recorded a hit for any platform source is not silence from any individual source.
- The fingerprint instrumentation gap remains a Section 5 calibration item (third consecutive week).

## 5. Recommended Actions (Kay's Review Bucket)

1. **Digital Capital Advisors → add to General Sources (`Active - email-only`)** — RECOMMEND: ADD → YES / NO / DISCUSS
2. **Transworld Business Advisors (NY) → add to General Sources (`Active - relationship + marketplace`)** — RECOMMEND: ADD → YES / NO / DISCUSS
3. **Volume = 🔴 third consecutive week** (0 platform-source deals/day, 0.29/day total with DealsX channel). 444 listings reviewed → 0 PASS. RECOMMEND: schedule a corpus-tuning pass on the active niches' DEALSX keyword sets + WR-row enrichment terms alongside next Tuesday's niche-intelligence (the same recommendation carried over from 05-15 digest — not yet executed) → YES / NO / DISCUSS
4. **Fingerprint store still empty for platform sources** (2 records total, both DealsX-channel since 05-18). The helper `scripts/deal-aggregator-fingerprint.sh add` has never been called from the scanned-source PASS path in 9+ weekday scans. Consistent with 0 platform PASS verdicts above, so likely "no matches" not "silent helper failure" — but the morning-run exit-code instrumentation request from 05-15 digest has not been implemented. RECOMMEND: have the next morning scan log the fingerprint-helper exit code for any PASS attempt (or explicit "no PASS to fingerprint" line if 0) → YES / NO / DISCUSS

---

### Sources read

- Daily scans (5): `brain/context/deal-aggregator-scan-{2026-05-15,18,19,20,21}.md`
- Email-scan results (8): `brain/context/email-scan-results-{2026-05-15,16,17,18,19,20,21,22}.md`
- Fingerprint store: `brain/context/deal-aggregator-fingerprints.jsonl` (2 records, both DealsX-channel)
- Sourcing Sheet: `1z8o2obq2mOG9drQ0umCmBk31K3OS2afMNGpVAlbLljw` — General Sources (22 rows) + Niche-Specific Sources (24 rows), live-read this run
- Prior digest for trend comparison: `brain/trackers/weekly/2026-05-15-deal-aggregator-digest.md`

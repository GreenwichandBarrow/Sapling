---
schema_version: "1.0.0"
date: 2026-05-02
type: tracker
title: "Deal Aggregator Weekly Digest — 2026-05-02"
window_start: 2026-04-25
window_end: 2026-05-02
volume_7d_avg: 0.0
volume_prior_week_avg: 0.0
volume_status: "🔴 Critical"
proposed_additions: 0
proposed_retirements: 0
opportunistic_count: 0
sourcing_sheet_source: live
fingerprint_store_status: empty
tags:
  - date/2026-05-02
  - tracker
  - topic/deal-aggregator
  - topic/weekly-digest
  - status/draft
---

# Deal Aggregator Weekly Digest — 2026-05-02

**Window:** 2026-04-25 → 2026-05-02 (Sat–Sat). Sat/Sun no-scan by design. Scan days with artifacts in window: Tue 4/28, Wed 4/29, Fri 5/1. Missing: Mon 4/27 + Thu 4/30 (morning artifacts not produced — both flagged in 5/1 digest as silent-failure pattern), and Sat 5/2 (today, this digest fires before any morning scan). **Effective scan days: 3.**

**Executive summary:** Third consecutive zero-matches week. 7-day rolling average remains 0/day — 🔴 Critical. The 5/1 digest's three carry-over proposals are partially actioned: **Helen Guo / SMB Deal Hunter** is now on the General Sources tab as `Active - email-only` (addition applied), **GP Bullhound** is now `Active` on the Niche-Specific tab under Vertical SaaS (status flip applied), and **Axial activation is in motion** — Andrew Lowis (XPX, 4/30) sent the Axial member-firm form link, Kay replied "Great will do, thank you!", and the form completion is the remaining step before the Axial-colleague intro can flow. No net-new source candidates emerged this week (inbox = peer relationships, vendor pitches, newsletters) and no net-new retirement candidates surfaced (no Active source crossed 30-day silent threshold with 3-live-check pass). Section 3 (Broker-channel opportunistic) is empty this week — Helen Guo's two blasts (generic $700K/yr SMB on 4/28, HVAC + vehicle wrap on 4/29) fell below opportunistic floor / hit Services hard-excludes; all marketplace near-misses were on STRICT-mode sources (Business Exits, Empire Flippers, Synergy, Website Closers, Flippa). The structural diagnosis from 4/24 + 5/1 holds unchanged: web-scrape channels are flowing inventory but skew DTC / construction / GovCon / horizontal-SaaS — orthogonal to G&B's luxury-services / vertical-SaaS-for-luxury / specialty-insurance theses. The single highest-value remaining unblock is **Axial form completion → first member-firm intro** (already in Kay's hand from Andrew Lowis 4/30).

---

## 1. Source Productivity (Last 7 Days)

**Caveat — fingerprint store is still 0 bytes** (carried unchanged across four consecutive digests since 4/22). Per `feedback_test_before_concluding_channel_dead`, "Last Match" cannot be sourced from the JSONL store; values below come from cross-referencing the 3 in-window scan artifacts (4/28, 4/29, 5/1) plus prior-digest "Last Known Match" attributions. The fingerprint-write gap is unchanged from prior week — see §6 Recommended Actions item 1.

| Source | Category | 7d Matches | 7d Listings Reviewed | Last Known Match | Trend |
|--------|----------|-----------:|---------------------:|------------------|:-----:|
| Business Exits | General (Marketplace) | 0 | ~90 (3 morning fetches × ~30) | Apr 16 (pre-digest series) | → |
| Empire Flippers | General (Marketplace) | 0 | ~72 (4/28 + 4/29 + 5/1 mornings) | None recorded | → |
| Synergy Business Brokers | General (Marketplace) | 0 | ~20 (4/29 morning) | None recorded | → |
| Website Closers | General (Marketplace) | 0 | ~39 (4/28 + 4/29 + 5/1 mornings) | None recorded | → |
| Flippa | General (Marketplace) | 0 | ~22 (web via agent-browser, 5/1 morning) | None recorded | → |
| BizBuySell | General (Marketplace) | 0 | 0 (verified blocked all 3 days — WebFetch + agent-browser both 403) | None recorded | → |
| SMB Deal Hunter (Helen Guo) | General (Newsletter blast) | 0 | 2 blasts (4/28 generic SMB; 4/29 HVAC + vehicle wrap) | None recorded | N/A (1st full week active) |
| Quiet Light | General (Email-only) | 0 | 0 (web Cloudflare 403; email channel 0 in-thesis blasts) | None recorded | → |
| Everingham & Kerr | General (Email-only) | 0 | 0 (no in-thesis broker blasts in window) | None recorded | → |
| Viking Mergers | General (Email-only) | 0 | 0 | None recorded | → |
| Rejigg | General (Email + login-gated web) | 0 | 0 | Platform match 4/20 (off-thesis) | → |
| DealForce | General (Email alerts) | 0 | 0 | None recorded | → |
| IAG M&A Advisors | General (Email + Advisory) | 0 | 0 (Flavia Milano thread dormant since 4/16) | None recorded | → |
| Synergy BB Real Estate | Niche (Estate Mgmt) | 0 | ~13 (4/28 + 4/29 + 5/1 mornings; 6 of 8 marked SOLD on 5/1) | None recorded | → |
| Sica Fletcher | Niche (Insurance, Advisory) | 0 | ~20 (intel-only — all consolidator-side announcements) | Feb 27 tombstone (Safe Harbour → ALKEME) | → |
| PCO Bookkeepers | Niche (Pest, Advisory) | 0 | 0 (tombstones image-only, unparseable) | None recorded | → |
| GP Bullhound | Niche (Vertical SaaS, Advisory) | 0 | 0 (newly Active this week — 1st scan rotation upcoming) | None recorded | N/A (newly active) |
| Acquire.com | General (Pending registration) | 0 | 0 | Not registered | → |
| Axial | General (Pending registration) | 0 | 0 | Not registered (member form sent 4/30 by Andrew Lowis; Kay form-fill pending) | → (in-motion) |
| BizScout | General (Pending registration) | 0 | 0 | Not registered | → |
| FE International | General (Pending registration) | 0 | 0 | Not registered | → |
| Kumo | General (Pending registration) | 0 | 0 | Not registered | → |
| Searchfunder | General (Pending alerts) | 0 | 0 | Alerts not yet enabled | → |
| Benchmark International | General (Registered - dormant) | 0 | 0 | Jun 30, 2025 (>10 months silent; retired 4/24) | → (dormant per applied retirement) |
| Paine Pacific | General (Relationship-only) | 0 | 0 | Relationship-only, no public inventory | → |
| Woodbridge (Mariner) | General (Relationship-only) | 0 | 0 | Relationship-only, rebranded | → |
| ProNova Partners | General (Blocked, relationship-only) | 0 | 0 | 403, relationship-only | → |
| Keystone Business Advisors | Niche (Pest, Pending decision) | 0 | 0 | Login-gated, decision carried | → |
| Anticimex US | Niche (Pest, Intel-only) | 0 | 0 | Strategic acquirer (intel only) | → |
| MarshBerry | Niche (Insurance, Intel-only) | 0 | 0 | URL fix needed (/recent-transactions/ 404) | → |
| Reagan Consulting | Niche (Insurance, Intel-only) | 0 | 0 | Member-gated | → |
| Agency Checklists | Niche (Insurance, Intel-only) | 0 | 0 | Industry news pub, Jan 26 last MA tombstone | → |
| IA Magazine | Niche (Insurance, Intel-only) | 0 | 0 | Trade publication | → |
| CMM Online | Niche (Cleaning, Intel-only) | 0 | 0 | Industry publication | → |
| Inside Self-Storage | Niche (Art Storage, Intel-only) | 0 | 0 | Self-storage REITs only | → |
| MidCap Advisors | Niche (Art Storage, Intel-only) | 0 | 0 | 2023 Artemis → Cadogan Tate | → |
| Calder Capital | Niche (Cleaning, Not yet scanning) | 0 | 0 | Tombstones at base URL | → |
| Green Bridge Advisors | Niche (Cleaning, Not yet scanning) | 0 | 0 | URL routes to non-cleaning content | → |
| Union Square Advisors | Niche (SaaS, Not yet scanning) | 0 | 0 | 403 bot-blocked | → |
| Exit Strategies Group | Niche (Estate Mgmt, Weak) | 0 | 0 | Marketing-only page, CA-flagged | → |
| Cetane | Niche (Pest, Weak) | 0 | 0 | All listings sub-$1M EBITDA; below floor + sell-side prospector confirmed 4/30 | → |
| Software Equity Group | Niche (SaaS, Weak) | 0 | 0 | Public news; SaaS-specialty | → |
| Tyton Partners | Niche (SaaS, Weak) | 0 | 0 | EdTech-specialty (off-thesis) | → |

**Trend arrow logic:** ↑/↓ = ±50% week-over-week match count; → = within ±50%. This week (0 across all sources) and prior week (per 5/1 digest, 0 across all sources) both sit at zero, so → is correct everywhere except: **(a) SMB Deal Hunter** marked N/A — 1st full week of active scanning since addition (newsletter cadence is ~weekly, 2 blasts captured this window, neither cleared opportunistic floor); **(b) GP Bullhound** marked N/A — newly Active this week, no prior-week comparison baseline; **(c) Axial** marked → (in-motion) — registration still pending but member-form path now in Kay's hand from Andrew Lowis 4/30, materially different from prior week's "single most-cited unblock."

## 2. Volume Check

- **7-day rolling average:** 0.0/day (0 matches ÷ 3 effective scan days)
- **Prior-week rolling average:** 0.0/day (per 5/1 digest)
- **Two-weeks-prior baseline (Apr 11–17):** 1.6/day
- **Status:** 🔴 **Critical** (third consecutive critical week)
- **Strict-floor matches:** 0 (would have Slack-pinged in `#active-deals`)
- **Opportunistic matches:** 0 (would have surfaced in §3 below)

**Diagnosis (unchanged from 5/1 — surfacing for compounding visibility):** The structural read holds. Across 3 scan days the filter reviewed approximately 256 listings (~90 Business Exits + ~72 Empire Flippers + ~39 Website Closers + ~22 Flippa + ~20 Synergy + ~13 Synergy Real Estate) and found zero buy-box-and-thesis intersection. Filter is functioning correctly (Data Availability Rule holding, hard-excludes catching DTC/GovCon/construction, near-miss list dense with disclosed-and-failed financials) — the gap remains upstream channel-mix, not screen calibration. The same listing populations recurred across this week's scans as prior week's (Empire Flippers all DTC, Website Closers all eCommerce/digital, Synergy Real Estate dominated by sub-floor + STR ops, Sica Fletcher 100% consolidator-side). The single most-cited structural unblock — Axial registration — moved from "single most-cited unblock" (5/1) to "in motion, awaiting Kay's form completion" (5/2) thanks to Andrew Lowis's 4/30 form-link send.

**Notable near-miss this week:** None new. The 4/29 NetSuite-native POS Software near-miss noted in 5/1 digest (Synergy, $1.6M ARR / $1.17M EBITDA, disclosed-and-failed on SaaS ARR floor) remains the closest structural shape to the Vertical SaaS thesis the channel has surfaced. No 5/1 morning scan near-miss cleared a tighter bar than that one.

## 3. Broker-channel opportunistic deals (this week)

**None this week.**

Re-screened the window's broker / intermediary / newsletter-blast inventory against the OPPORTUNISTIC floor ($1M EBITDA, 12% margin, broad services / SaaS / insurance pool, broker/intermediary-curated source per `feedback_broker_channel_opportunistic_floor`). Opportunistic-source classification per the SKILL.md channel-routing table = `Email-only broker`, `Newsletter blast`, `Advisory + Deal Platform`, `Marketplace + Email`, `Email-only broker + Buyer Portal`. Active sources matching that classification this week: Helen Guo / SMB Deal Hunter (Newsletter blast), Everingham & Kerr (Email-only broker), Quiet Light email channel (Marketplace + Email), Flippa email channel (Marketplace + Email), Viking Mergers (Email-only broker), Rejigg (Marketplace + Email), DealForce (Marketplace), IAG M&A Advisors (Advisory + Deal Platform).

- **Helen Guo blasts (2 in window):** 4/28 generic $700K/yr SMB blast — below opportunistic $1M EBITDA floor. 4/29 HVAC + vehicle wrap blast — HVAC fails Services hard-exclude (labor-heavy field service / construction-adjacent); vehicle wrap below floor + outside thesis. **Both rejected.**
- **Everingham & Kerr / Viking Mergers / DealForce / IAG / Rejigg / Quiet Light / Flippa email channels:** 0 in-thesis broker blasts captured by email-intelligence in window per scan artifacts 4/28 + 4/29 + 5/1.
- **Sica Fletcher** (Advisory, Intel-only — not an opportunistic source): 5–10 announcements per scan, all consolidator-acquired (PE-consolidator hard-exclude). Continues to feed niche-intelligence as market-structure signal.

Channel-mix note for Kay's awareness: SMB Deal Hunter completed its first full week active. Per the 30-day monitor clause in the addition Notes ("retire if 0 in-thesis hits"), the 30-day clock started 5/1. Will re-evaluate week of 5/29 against the retire-or-keep gate.

## 4. Proposed Additions

**Zero net-new this week.**

The 5/1 digest's three carry-over proposals (Helen Guo / Axial / GP Bullhound) are now resolved or in-motion:

- **Helen Guo / SMB Deal Hunter** ✅ APPLIED — appears on General Sources tab as `Active - email-only`, sender `helen@mail.smbdealhunter.xyz`, with the 30-day-monitor language captured in Notes.
- **GP Bullhound** ✅ APPLIED — Niche-Specific tab Vertical SaaS row now reads `Active`. First scan rotation upcoming.
- **Axial activation** 🟡 IN MOTION — Andrew Lowis (XPX, 4/30 17:30) sent the member-firm form link (`https://www.axial.net/request-information?utm_campaign=navbar-join`). Kay replied "Great will do, thank you!" Form completion + Axial-colleague intro is the live path; Sourcing Sheet status remains `Pending G&B registration` correctly until form is submitted. Surfaced as a Recommended Action below (item 4) — this is a Kay-action ask, not a sheet-structural change.

**New sources scouted and rejected as additions this week:**

- **Cetane Associates / Bob Williamson** (Pest & Lawn M&A Director, NJPMA workshop intro 4/29 → 4/30 follow-up email with sample VRA `Bugo Pest Remover_v2.pdf`) — Cetane is **already on Sourcing Sheet** (Niche-Specific Pest tab, `Weak` status). Bob's 4/30 outreach is **sell-side prospecting** per `feedback_free_valuation_equals_sell_side` — free Value Range Analysis is a lead-magnet for sell-side engagement, wrong layer for buy-side intent. Cetane's existing `Weak` row is correctly classified; no action needed. Network-wise, Bob is useful for pest ecosystem mapping (relationship-manager / river-guide-builder), not as a deal source.
- **Hollywell Q of E vendor** (Anacapa webinar referral, $20K search-fund Q of E with broken-deal-fee covered) — Q of E provider, not a deal source. Routes to deal-evaluation skill's vendor list, not deal-aggregator.
- **Inzo Technologies** (Rebekah Stender BDR pitch, IT/cybersecurity DD vendor) — service provider, not deal source. Skip (already noted in 5/1 digest).
- **Methodnode** (Natalie Evans, pay-per-booked-call outbound vendor, second touch 4/30 with sample-list offer) — outbound-as-a-service competitor to internal Apollo+JJ stack. Not deal source. Skip.
- **Heritage Holding Newsletter / Grant Hensel "This Week in ETA" / Mitchell Baldridge / Frank Sondors / Frieze VIP / NPMA Events / XPX** — search-fund peer / industry / promotional newsletters without specific deals. None are deal-flow channels.
- **NJPMA / NPMA / XPX NYC / ACG NY / Pest Mgmt Conference Charlotte / CWAN** — conference / event invites. Belong in `conference-discovery` queue, not deal-aggregator sources.
- **Aerospace & Defense woman-owned referral** (XPX corporate-advisor contact via Camilla Lin call 4/30 — owner inherited 10 yrs ago, would like to sell) — single-deal warm intro, not a recurring source. If it converts to a CIM / NDA, pipeline-manager handles. Not a Sourcing Sheet addition.

## 5. Proposed Retirements

**Zero net-new this week.**

No Active source crossed the 30-day silent threshold AND passed three live-checks AND was not already evaluated in a prior digest. Retirement candidates considered and rejected this week:

- **Cetane** (Niche-Pest, Weak) — Cloudflare-bot-blocked to scraper; sub-$1M EBITDA listings only. Bob Williamson 4/30 outreach **confirms domain is live + firm is active** (sell-side prospecting in pest niche is their working business). Per `feedback_test_before_concluding_channel_dead`: not "channel dead" — channel publishes content; content fails buy-box. **Keep at `Weak`.** Possible reclassification to `Intel-only` next cycle if pest-market data continues to be useful but actionable deal flow remains zero — defer to next digest.
- **PCO Bookkeepers** (Niche-Pest, Active) — page renders HTTP 200 but tombstones are image-only, unparseable. Domain alive, content present, parser limitation. **Keep on Active**, do not retire. Possible action: research whether PCO's PMP-newsletter feed (text-extractable) substitutes for the tombstone page — defer.
- **MarshBerry** (Niche-Insurance, Intel-only) — `/recent-transactions/` URL still 404 per 5/1 noted issue. Channel intel-only, low effort to fix URL. **Keep.** URL-fix surfaced in §6 below as Item 5.
- **Empire Flippers** (General, Active) — flowing inventory (~72 listings reviewed in window) but 100% DTC/digital/FBA — orthogonal to thesis. Pattern is "active but no thesis intersection," not "channel dead." Three consecutive weeks at this pattern. **Keep on Active** but note for Kay's attention: if 5th consecutive week of active scan + zero-thesis-intersection, consider `Weak` reclassification (would reduce scan-time cost without hard retirement).
- **Synergy Business Brokers Real Estate** (Niche-Estate-Mgmt, Active) — flowing inventory (~13 listings in window) but 6 of 8 marked SOLD on 5/1 alone, remaining 2 below revenue floor + outside HNW Estate Management thesis. Pattern matches Empire Flippers — "active but wrong thesis fit." **Keep**, monitor.
- **Searchfunder, Benchmark International (Dormant), Paine Pacific, Woodbridge (Mariner), ProNova Partners** — pre-active / dormant / relationship-only. Not eligible for retirement evaluation.

**Carry-over status from prior digests:** The 4/24 retirements (Benchmark International → Dormant; DealFlow Agent → removed) remain applied per 5/1 verification. No zombie status drift.

## 6. Recommended Actions (Kay's Review Bucket)

All proposals are approval-gated. On YES, I'll execute the sheet write (with pre-write snapshot per `feedback_subagent_sheet_write_safety`) and write a trace to `brain/traces/`. NO/DISCUSS = no write.

**Additions:** None this week. Three 5/1 carry-over proposals resolved (2 applied, 1 in-motion).

**Retirements:** None this week. Prior 4/24 retirements remain applied.

**Infrastructure (carry-overs from 5/1 + new this week):**

1. **RECOMMEND: Backfill/repair fingerprint store** — `brain/context/deal-aggregator-fingerprints.jsonl` still 0 bytes since 4/22 launch. Four consecutive digests have flagged this. Trend column will continue to fail Phase-2 stop hook + "Last Match" attribution will continue requiring scan-artifact archaeology until the store is wired into the active scan path AND a backfill from artifact history is applied. **Owner: CFO** (infrastructure spend / reliability hygiene). → YES / NO / DISCUSS

2. **RECOMMEND: Debug morning-run silent failures** — Mornings 4/27 + 4/30 produced no scan artifacts (per 5/1 digest); pattern persists into this digest's window (no 4/30 morning scan was written before today's digest fire). Pattern surfaces every week now. Investigate `scripts/run-skill.sh` lockfile + `.claude/skills/deal-aggregator/headless-morning-prompt.md` (the operator-question failure mode that this Friday digest wrapper specifically guards against). **Owner: CFO** (reliability). → YES / NO / DISCUSS

3. **RECOMMEND: Install BizBuySell persistent-session profile** — Two-attempt verification confirmed BizBuySell genuinely 403-blocked to both WebFetch and unauthenticated agent-browser this week (4/29 + 5/1). Per SKILL.md, `--profile ~/.deal-aggregator` with first-login should unblock the largest LMM platform. Kay's BizBuySell account confirmed registered (welcome email 3/22/2026). **Owner: CFO** (tooling). → YES / NO / DISCUSS

4. **RECOMMEND: Complete Axial member form (carry from Andrew Lowis 4/30)** — Andrew sent the form link `https://www.axial.net/request-information?utm_campaign=navbar-join` 4/30 17:30; form completion gates the Axial-colleague intro Andrew is brokering (his colleague specifically works with search funds). This is the single highest-yield activation Kay can take this week given three consecutive zero-match weeks on existing channels. **Owner: CIO** (source activation tied to thesis coverage). → YES / NO / DISCUSS

5. **RECOMMEND: Fix MarshBerry transactions URL** — Sourcing Sheet still notes `/recent-transactions/` 404; should test `/news/` or contact MarshBerry for canonical transactions feed URL. Carry-over from 5/1 (item 8). Low effort, intel-only impact. **Owner: GC** (sheet hygiene). → YES / NO / DISCUSS

6. **RECOMMEND: Reclassify Empire Flippers + Synergy Real Estate to "Weak" if 5th consecutive zero-thesis-intersection week persists (monitor, do not act this week)** — Empire Flippers now 4 weeks of "active scan, zero thesis intersection." Synergy Real Estate similar pattern. Reclassifying to `Weak` reduces daily scan-time cost without hard retirement (sources remain in rotation, just at lower scan priority). Surface as a watch item for next week's digest, not an action this week — `feedback_test_before_concluding_channel_dead` requires sustained pattern not single-week dip. **Owner: CIO** (source-tier classification). → MONITOR (no action this week)

---

**C-suite ownership summary:**
- **CFO**: 1, 2, 3 (infrastructure / tooling / reliability hygiene)
- **CIO**: 4, 6 (source activation tied to thesis coverage; tier classification)
- **GC**: 5 (sheet hygiene / source-row corrections)
- **CMO**: none this week (no addition involving voice-of-source / content channel)

## Slack Notification Status

Per spec: send to `SLACK_WEBHOOK_OPERATIONS` when ≥1 proposed change OR volume = 🔴. **Volume condition met (🔴 Critical, third consecutive zero-match week).** Proposals total = 0 net-new (3 carry-overs resolved or in-motion + 5 infrastructure carry-overs / fresh items). Slack will fire.

Draft posted below — wrapper will fire at digest-write completion.

> 🔴 Deal Aggregator — Weekly Digest 2026-05-02
>
> Volume: 0/day (critical, 3rd consecutive zero-match week)
> Proposals: 0 net-new this week. 5/1 carry-overs resolved — Helen Guo + GP Bullhound applied; Axial form-fill in motion via Andrew Lowis intro
> Infrastructure flags: fingerprint store still empty, morning-run silent failures persist, BizBuySell still 403-blocked
> Highest-yield action: Kay completes Axial member form → triggers Andrew Lowis colleague intro
> Full digest: `brain/trackers/weekly/2026-05-02-deal-aggregator-digest.md`

---

## Validation

- [x] Digest file exists at `brain/trackers/weekly/2026-05-02-deal-aggregator-digest.md`
- [x] All 6 required sections present (Source Productivity / Volume Check / Broker-channel opportunistic deals / Proposed Additions / Proposed Retirements / Recommended Actions)
- [x] Each proposed addition includes rationale + recommended tab + access method (zero net-new this week — carry-overs status-tracked instead)
- [x] Each proposed retirement includes rationale + retire-test logic (zero net-new this week — candidates evaluated and rejected with reasoning)
- [x] Trend column populated via prior-week (5/1 digest) comparison (not fabricated); Helen Guo + GP Bullhound + Axial marked N/A or → (in-motion) with explicit baseline-rationale paragraph
- [x] Fingerprint data gap surfaced honestly (carried over from 4/22 — fourth consecutive digest)
- [x] No auto-writes to the Sourcing Sheet — all 6 recommended actions await Kay's approval
- [x] Slack notification will fire (🔴 volume condition met independent of proposal count)
- [x] No operator-question framing emitted to harness (idempotency gate cleared cleanly; YES/NO/DISCUSS lines exist only inside §6 of the digest body for Kay's async review)

## Data Sources (this digest)

- `brain/context/deal-aggregator-scan-2026-04-28.md`
- `brain/context/deal-aggregator-scan-2026-04-29.md`
- `brain/context/deal-aggregator-scan-2026-05-01.md`
- (gap noted: 2026-04-25/26 weekend no-scan; 2026-04-27 + 2026-04-30 morning artifacts missing — silent-failure pattern surfaced as Recommended Action 2; 2026-05-02 morning scan not yet fired at digest time)
- `brain/context/email-scan-results-2026-04-{25,26,27,28,29,30}.md` + `email-scan-results-2026-05-{01,02}.md` (Source Scout sender-domain enumeration)
- `brain/context/deal-aggregator-fingerprints.jsonl` (0 bytes — gap flagged)
- `brain/trackers/weekly/2026-05-01-deal-aggregator-digest.md` (prior-week trend baseline + carry-over proposal status verification)
- `brain/trackers/weekly/2026-04-24-deal-aggregator-digest.md` (two-week trend reference)
- `G&B Deal Aggregator - Sourcing List` sheet ID `1z8o2obq2mOG9drQ0umCmBk31K3OS2afMNGpVAlbLljw` (General Sources + Niche-Specific Sources tabs, live-read; `sourcing_sheet_source: live`)

---
schema_version: "1.0.0"
date: 2026-05-01
type: tracker
title: "Deal Aggregator Weekly Digest — 2026-05-01"
window_start: 2026-04-24
window_end: 2026-05-01
volume_7d_avg: 0.0
volume_prior_week_avg: 0.0
volume_status: "🔴 Critical"
proposed_additions: 3
proposed_retirements: 0
sourcing_sheet_source: live
fingerprint_store_status: empty
tags:
  - date/2026-05-01
  - tracker
  - topic/deal-aggregator
  - topic/weekly-digest
  - status/draft
---

# Deal Aggregator Weekly Digest — 2026-05-01

**Window:** 2026-04-24 → 2026-05-01 (Fri-Fri). Sat/Sun no-scan by design. Scan days with artifacts in window: Mon 4/27 (afternoon only — morning silent failure), Tue 4/28 (+ afternoon), Wed 4/29 (+ afternoon), Thu 4/30 (afternoon only — morning artifact missing), Fri 5/1 (this digest, ahead of 6 AM morning scan). Effective scan days: 4.

**Executive summary:** Second consecutive zero-matches week. 7-day rolling average remains 0/day — 🔴 Critical. The 4/24 digest's five proposals are partially actioned: Benchmark International is now "Registered - dormant" on the sheet (retirement applied) and DealFlow Agent is no longer present (retirement applied). The three additions/activations (Helen Guo SMB Deal Hunter, Axial registration push, GP Bullhound flip) remain unactioned and are re-surfaced below as **carry-over proposals**, not net-new. Zero net-new source candidates emerged this week — inbound was clean (peer relationship, vendor pitches, newsletters). The structural diagnosis from 4/24 holds: web-scrape channels are flowing inventory (~280 listings parsed across the window) but skew DTC/construction/manufacturing/GovCon — orthogonal to G&B's luxury-services / vertical-SaaS-for-luxury / specialty-insurance theses. Two infrastructure deltas changed this week: (a) `agent-browser` is now functional and successfully scraped Flippa (25 SaaS listings on 4/29 afternoon — promote off the blocked watchlist), and (b) two morning runs (4/27 + 4/30) failed to produce artifacts, an emerging reliability issue.

---

## 1. Source Productivity (Last 7 Days)

**Caveat — fingerprint store is still 0 bytes** (carried over from 4/22). Per `feedback_test_before_concluding_channel_dead`, "Last Match" cannot be sourced from the JSONL store; values below come from cross-referencing the in-window scan artifacts (4/27, 4/28, 4/29, 4/30) plus the 4/24 prior-digest "Last Known Match" attributions. The fingerprint-write gap is unchanged from prior week — see §5 Recommended Actions item 6.

| Source | Category | 7d Matches | 7d Listings Reviewed | Last Known Match | Trend |
|--------|----------|-----------:|---------------------:|------------------|:-----:|
| Business Exits | General | 0 | ~90 (3 morning fetches × ~30) | Apr 16 (prior to digest series) | → |
| Empire Flippers | General | 0 | ~50 (4/28 + 4/29 mornings) | None recorded | → |
| Synergy Business Brokers | General | 0 | ~20 (4/29 morning) | None recorded | → |
| Website Closers | General | 0 | ~26 (4/28 + 4/29 mornings) | None recorded | → |
| Synergy BB Real Estate | Niche (Estate Mgmt) | 0 | ~7 (4/28 + 4/29 mornings) | None recorded | → |
| Flippa | General | 0 | ~65 (web via agent-browser, 4/28+4/29+4/30 afternoons) | None recorded | ↑ (now scrapable) |
| Sica Fletcher | Niche (Insurance) | 0 | ~20 (intel-only, all consolidator-side announcements) | Feb 27 tombstone (Safe Harbour → ALKEME) | → |
| Agency Checklists | Niche (Insurance) | 0 | ~2 | Intel-only; Jan 26 last MA tombstone | → |
| PCO Bookkeepers | Niche (Pest) | 0 | 0 (tombstones image-only, unparseable) | None | → |
| BizBuySell | General | 0 | 0 (verified blocked all 4 days — WebFetch + agent-browser both 403) | None recorded | → |
| Quiet Light | General | 0 | 0 (web 403; email channel active, 0 in-thesis blasts) | None recorded | → |
| Everingham & Kerr | General (email-only) | 0 | ~1 (Machining/Waterjet near-miss 4/29) | None recorded | → |
| Viking Mergers | General (email-only) | 0 | 0 | None recorded | → |
| Rejigg | General (email + login-gated web) | 0 | 0 | Platform match 4/20 (off-thesis) | → |
| DealForce | General (email) | 0 | 0 | None | → |
| IAG M&A Advisors | General (email) | 0 | 0 | Flavia Milano active thread 4/16 (intermediary) | → |
| Acquire.com | General (Pending registration) | 0 | 0 | Not registered | → |
| Axial | General (Pending registration) | 0 | 0 | Not registered — single most-cited unblock | → |
| BizScout | General (Pending registration) | 0 | 0 | Not registered | → |
| FE International | General (Pending registration) | 0 | 0 | Not registered | → |
| Kumo | General (Pending registration) | 0 | 0 | Not registered | → |
| Searchfunder | General (Pending alerts) | 0 | 0 | Alerts not yet enabled | → |
| Benchmark International | General (Registered - dormant) | 0 | 0 | Jun 30, 2025 (>10 months silent) | → (now Dormant per 4/24 retirement) |
| Paine Pacific | General (Relationship-only) | 0 | 0 | Relationship-only, no public inventory | → |
| Woodbridge (Mariner) | General (Relationship-only) | 0 | 0 | Relationship-only, rebranded | → |
| ProNova Partners | General (Blocked) | 0 | 0 | 403, relationship-only | → |
| Keystone Business Advisors | Niche (Pest, Pending decision) | 0 | 0 | Login-gated, decision carried | → |
| Anticimex US | Niche (Pest, Intel-only) | 0 | 0 | Strategic acquirer (intel only) | → |
| MarshBerry | Niche (Insurance, Intel-only) | 0 | 0 | URL fix needed (/recent-transactions/ 404) | → |
| Reagan Consulting | Niche (Insurance, Intel-only) | 0 | 0 | Member-gated | → |
| IA Magazine | Niche (Insurance, Intel-only) | 0 | 0 | Trade publication | → |
| CMM Online | Niche (Cleaning, Intel-only) | 0 | 0 | Industry publication | → |
| Inside Self-Storage | Niche (Art Storage, Intel-only) | 0 | 0 | Self-storage REITs only | → |
| MidCap Advisors | Niche (Art Storage, Intel-only) | 0 | 0 | 2023 Artemis → Cadogan Tate (only US fine-art-logistics deal in 3 years) | → |
| Exit Strategies Group | Niche (Estate Mgmt, Weak) | 0 | 0 | Marketing-only page, CA-flagged | → |
| Calder Capital | Niche (Cleaning, Not yet scanning) | 0 | 0 | Tombstones at base URL (no active-listings path) | → |
| Green Bridge Advisors | Niche (Cleaning, Not yet scanning) | 0 | 0 | URL routes to non-cleaning content (parent co.) | → |
| GP Bullhound | Niche (SaaS, Not yet scanning) | 0 | 0 | Not yet activated | → |
| Union Square Advisors | Niche (SaaS, Not yet scanning) | 0 | 0 | 403 bot-blocked | → |
| Cetane | Niche (Pest, Weak) | 0 | 0 | All listings sub-$1M EBITDA; below floor | → |
| Software Equity Group | Niche (SaaS, Weak) | 0 | 0 | Public news; SaaS-specialty | → |
| Tyton Partners | Niche (SaaS, Weak) | 0 | 0 | EdTech-specialty (off-thesis) | → |

**Trend arrow logic:** ↑/↓ = ±50% week-over-week match count; → = within ±50%. Both this week (0 matches across all sources) and prior week (per 4/24 digest, 0 matches) sit at zero, so → is correct everywhere except Flippa, marked ↑ — `agent-browser` successfully snapshotted Flippa on 4/29 afternoon (25 SaaS listings parsed cleanly), promoting it from "JS-shell blocked" to "active web". Listing inventory contained no thesis matches, but the channel itself unblocked materially. **Status update for the Sourcing Sheet:** Flippa's General Sources row currently reads "Active - email-only / Web broken (JS shell)" — that should be updated to "Active - email + web (agent-browser)". Surfacing as a recommended action below (item 7).

## 2. Volume Check

- **7-day rolling average:** 0.0/day (0 matches ÷ 4 effective scan days)
- **Prior-week rolling average:** 0.0/day (per 4/24 digest)
- **Two-weeks-prior baseline (Apr 11–17):** 1.6/day
- **Status:** 🔴 **Critical** (second consecutive critical week)

**Diagnosis:** The structural read from the 4/24 digest holds — channels are flowing inventory but listing populations skew DTC ecommerce / horizontal SaaS / capital-intensive manufacturing / GovCon services / construction-adjacent field services. Across 4 scan days the filter reviewed approximately 280 listings (90 Business Exits + 50 Empire Flippers + 65 Flippa + 26 Website Closers + 20 Synergy + ~30 niche-specific) and found zero buy-box-and-thesis intersection. Filter is functioning (Data Availability Rule holding, hard-excludes catching DTC and construction, near-miss list is dense with disclosed-and-failed financials) — the gap is upstream channel-mix, not screen calibration. Three open structural unblocks remain unchanged from 4/24: (a) Axial registration, (b) Helen Guo SMB Deal Hunter onboarding to feed lower-mid-market signal, (c) GP Bullhound activation for Vertical SaaS coverage.

**Notable near-miss this week:** NetSuite-native POS Software (Synergy Business Brokers, 4/29 — $1.6M ARR / $1.17M EBITDA / global) was the closest structural shape to the Vertical SaaS thesis the channel surfaced — disclosed-and-fails on ARR floor. Worth re-scanning in 12-18 months if they relist at higher ARR.

## 3. Proposed Additions

All three are **carry-overs from the 2026-04-24 digest** that have not yet been actioned. Re-surfacing because the 4/24 RECOMMEND→YES/NO/DISCUSS lines never received a YES (or a NO/DISCUSS that closed them out). No net-new source candidates emerged this week from the email-scan window — inbound classified as peer relationship (Ali Doswell), vendor BDR pitches (Inzo, Methodnode), event invites, newsletters, and one already-declined sourcing-platform vendor (Athena Simpson Acquimatch).

### 3.1 Helen Guo — SMB Deal Hunter (newsletter, off-market blasts) — CARRY-OVER from 4/24

- **Why (updated):** Reappeared in inbox 4/28 ($700K/yr generic SMB blast) and 4/29 (HVAC + vehicle wrap blast). Format is consistent — weekly cadence, specific-deal blasts (not marketing). Off-thesis on every blast this week, but the channel adds at ~5 deals/week of lower-mid-market signal which expands surface area for niches sitting below the $10M revenue threshold.
- **Recommended tab:** General Sources
- **Row values:** Status = "Active - email-only" · Source = "SMB Deal Hunter (Helen Guo)" · Type = "Newsletter blast" · Access = "Public (subscribed)" · URL = `https://smbdealhunter.com` (verify Kay's inbox sender header) · Notes = "Weekly ~5-listing blast; off-thesis 4/20–4/29 inventory but legitimate BLAST source. Monitor 30 days from add date — retire if 0 in-thesis hits."
- **Access:** Free (already subscribed)
- **RECOMMEND: Add to General Sources** → YES / NO / DISCUSS

### 3.2 Activate Axial (elevate from "Pending registration" to active priority) — CARRY-OVER from 4/24

- **Why (updated):** Now flagged across 11 consecutive scan artifacts (4/20 → 4/30) as the single most-cited unblock. Two consecutive zero-match weeks compound the opportunity cost. Major LMM M&A deal network; brokers post into vetted-buyer network. Already on the Sourcing Sheet as "Pending G&B registration" — elevation is a Kay-action (membership request), not a sheet structural change.
- **Recommended tab:** General Sources (status change only, no new row)
- **Access:** Membership by invite/request
- **RECOMMEND: Priority-flag Axial registration this week** → YES / NO / DISCUSS

### 3.3 Activate GP Bullhound (flip from "Not yet scanning" to Active) — CARRY-OVER from 4/24

- **Why (updated):** Already on the Niche-Specific Sources sheet under Vertical SaaS as "Not yet scanning." Global tech M&A advisor, $58B+ deal value since 1999, 183 M&A deals. Public news-release page. Flipping status to Active is a one-line sheet edit plus adding the URL to the weekly scan rotation.
- **Recommended tab:** Niche-Specific Sources (status change only)
- **Access:** Public (tombstones / news releases)
- **Caveat (unchanged from 4/24):** Vertical SaaS is the only niche on the active 8-niche list where GP Bullhound is relevant. If Vertical SaaS gets deprioritized (currently rank 6 per 4/20 ranking), this activation becomes lower-value.
- **RECOMMEND: Flip GP Bullhound to Active** → YES / NO / DISCUSS

---

**New sources scouted and rejected as additions this week:**

- **Inzo Technologies** (Rebekah Stender, 4/29 BDR pitch) — Cybersecurity DD vendor. Service provider, not a deal source. Skip.
- **Methodnode** (Natalie Evans, 4/29 vendor pitch) — Pay-per-booked-call outbound-as-a-service competitor to internal Apollo+JJ stack. Service provider, not a deal source. Skip.
- **Beacon / Anacapa** (4/30 webinar invite reminder) — Search-fund peer / accelerator content. Not a deal source. Already noted in `reference_outbound_vendors.md` if relevant.
- **Athena Simpson Acquimatch** (4/29 fireside follow-up) — Sourcing-platform vendor pitch; already declined per `project_athena_simpson_sourcing_review.md`.
- **NJPMA / NPMA / XPX NYC / CWAN** — Conference / event invites. Belong in conference-discovery queue, not deal-aggregator sources.
- **Heritage Holding Newsletter #11, Cornellians, Wealth Management** — Search-fund peer / industry newsletters without specific deals.

## 4. Proposed Retirements

**Zero net-new retirement candidates this week.** The 4/24 digest's two retirement proposals appear to be applied:

- **DealFlow Agent** — No longer present on the Niche-Specific Sources tab. Retirement appears executed. ✅
- **Benchmark International** — Sourcing Sheet status now reads "Registered - dormant" (the canonical dormant form). Retirement appears executed. ✅

If either of those was *not* yet formally moved to "Dormant" status (the prior digest used the verb "Dormant" specifically), Kay should confirm — a label-equivalence check, not a re-proposal.

**Retirement candidates considered and rejected this week:**

- **PCO Bookkeepers** — Active page (HTTP 200) but tombstones rendered as images, unparseable. Per `feedback_test_before_concluding_channel_dead`, this is not a "channel dead" signal — the channel publishes content; the parser can't extract it. Possible action: research whether the deals are listed in Dan Gordon's PMP newsletter feed (text-extractable) instead. **Keep on Active**, do not retire.
- **Cetane** — Listed sub-$1M EBITDA only, below buy-box floor. Cloudflare-blocked to scraper. Was already labeled "Weak" on 4/24. Pattern continues. **Keep**, hold at "Weak" status.
- **MarshBerry** — `/recent-transactions/` URL still 404 per 4/24 noted issue. Channel intel-only. URL fix needed (see §5 item 8). **Keep**, intel-only.
- **Empire Flippers** — Active and flowing inventory (~50 listings reviewed) but 100% DTC/digital/FBA — orthogonal to G&B thesis. Not silent — actively reviewed and rejecting. Pattern is "active but no thesis intersection," not "channel dead." **Keep on Active** but note it as a low-yield-for-thesis channel; revisit at 30-day mark if pattern holds.

## 5. Recommended Actions (Kay's Review Bucket)

All proposals are approval-gated. On YES, I'll execute the sheet write (with pre-write snapshot per `feedback_subagent_sheet_write_safety`) and write a trace to `brain/traces/`. NO/DISCUSS = no write.

**Additions (3 carry-overs from 4/24, no net-new this week):**
1. **RECOMMEND: Add Helen Guo / SMB Deal Hunter to General Sources** — consistent weekly BLAST source, expanding LMM signal surface area → YES / NO / DISCUSS
2. **RECOMMEND: Priority-flag Axial registration this week** — single most-cited unblock across two consecutive zero-match weeks → YES / NO / DISCUSS
3. **RECOMMEND: Flip GP Bullhound from "Not yet scanning" to Active** — closes Vertical SaaS coverage gap → YES / NO / DISCUSS

**Retirements:** None this week. Prior 4/24 retirements (DealFlow Agent, Benchmark International) appear applied — confirm if formal "Dormant" status label needed.

**Infrastructure (still blocking volume; carry-overs from 4/24 + new this week):**
4. **RECOMMEND: Debug morning-run silent failures** — Mornings 4/27 and 4/30 produced no scan artifacts. 4/27 morning showed Claude hallucinating a parallel scan and exiting 0 (per 4/27 afternoon diagnostic note). Pattern is new this week and needs investigation in `scripts/run-skill.sh` lockfile + `.claude/skills/deal-aggregator/headless-morning-prompt.md`. → YES / NO / DISCUSS
5. **RECOMMEND: Backfill/repair fingerprint store** — `brain/context/deal-aggregator-fingerprints.jsonl` still 0 bytes since 4/22. Two consecutive digests have flagged this. Trend column will continue to fail Phase-2 stop hook until the store is wired into the active scan path AND a backfill from artifact history is applied. → YES / NO / DISCUSS
6. **RECOMMEND: Update Flippa Sourcing Sheet row** — `agent-browser` proven functional 4/29 afternoon (25 SaaS listings parsed). Sheet currently labels Flippa "Active - email-only / Web broken (JS shell)" — update to "Active - email + web (agent-browser)." This is a hygiene update, not a status change — but it removes an outdated infrastructure block from the sheet. → YES / NO / DISCUSS
7. **RECOMMEND: Install BizBuySell persistent-session profile** — Two-attempt verification confirms BizBuySell is genuinely 403-blocked to both WebFetch and unauthenticated agent-browser. Per SKILL.md, `--profile ~/.deal-aggregator` with first-login should unblock the largest LMM platform. → YES / NO / DISCUSS
8. **RECOMMEND: Fix MarshBerry transactions URL** — Sourcing Sheet still notes `/recent-transactions/` 404; should test `/news/` or contact MarshBerry for canonical transactions feed URL. Low effort, intel-only impact. → YES / NO / DISCUSS

---

**CFO ownership:** 4, 5, 7 (infrastructure / tooling spend + reliability hygiene)
**CIO ownership:** 2, 3 (source activation decisions tied to thesis coverage)
**CMO ownership:** 1 (content-channel / voice-of-source addition)
**GC ownership:** 6, 8 (sheet hygiene / source-row corrections)

## Slack Notification Status

Per spec: send to `SLACK_WEBHOOK_OPERATIONS` when ≥1 proposed change OR volume = 🔴. Both conditions are met (3 carry-over proposals + critical volume).

Draft posted below — wrapper will fire at digest-write completion.

> 🔴 Deal Aggregator — Weekly Digest 2026-05-01
>
> Volume: 0/day (critical, second consecutive zero-match week)
> Proposals: 3 carry-overs from 4/24 still pending (Helen Guo / Axial / GP Bullhound), 0 net-new this week
> Infrastructure flags: morning-run silent failures (4/27, 4/30), fingerprint store still empty, Flippa unblocked via agent-browser
> Full digest: `brain/trackers/weekly/2026-05-01-deal-aggregator-digest.md`

---

## Validation

- [x] Digest file exists at `brain/trackers/weekly/2026-05-01-deal-aggregator-digest.md`
- [x] All 5 required sections present (Source Productivity, Volume Check, Proposed Additions, Proposed Retirements, Recommended Actions)
- [x] Each proposed addition includes rationale + recommended tab + access method
- [x] Each carry-over retirement was verified against current Sheet state (no zombies; both 4/24 retirements appear applied)
- [x] Trend column populated via prior-week (4/24 digest) comparison (not fabricated); Flippa's ↑ is justified by 4/29-afternoon scan-artifact evidence
- [x] Fingerprint data gap surfaced honestly (carried over from 4/24)
- [x] No auto-writes to the Sourcing Sheet — all 8 recommended actions await Kay's approval
- [x] Slack notification will fire (≥1 proposal AND 🔴 volume both met)

## Data Sources (this digest)

- `brain/context/deal-aggregator-scan-2026-04-27-afternoon.md` (morning failed silently)
- `brain/context/deal-aggregator-scan-2026-04-28.md` + `-afternoon.md`
- `brain/context/deal-aggregator-scan-2026-04-29.md` + `-afternoon.md`
- `brain/context/deal-aggregator-scan-2026-04-30-afternoon.md` (morning artifact missing)
- `brain/context/email-scan-results-2026-04-{24,25,26,27,28,29,30}.md` (sender-domain enumeration for Source Scout)
- `brain/context/deal-aggregator-fingerprints.jsonl` (0 bytes — gap flagged)
- `brain/trackers/weekly/2026-04-24-deal-aggregator-digest.md` (prior-week trend baseline + carry-over proposal status)
- `G&B Deal Aggregator - Sourcing List` sheet ID `1z8o2obq2mOG9drQ0umCmBk31K3OS2afMNGpVAlbLljw` (General Sources + Niche-Specific Sources tabs, live-read)

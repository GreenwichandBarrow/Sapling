---
schema_version: "1.0.0"
date: 2026-04-24
type: tracker
title: "Deal Aggregator Weekly Digest — 2026-04-24"
window_start: 2026-04-18
window_end: 2026-04-24
volume_7d_avg: 0.0
volume_prior_week_avg: 1.6
volume_status: "🔴 Critical"
proposed_additions: 3
proposed_retirements: 2
tags:
  - date/2026-04-24
  - tracker
  - topic/deal-aggregator
  - topic/weekly-digest
  - status/draft
---

# Deal Aggregator Weekly Digest — 2026-04-24

**Window:** 2026-04-18 → 2026-04-24 (Fri-Thu). Sat/Sun no-scan by design. Scan days in window: Mon 4/20, Tue 4/21, Wed 4/22 (+ afternoon), Thu 4/23 (+ afternoon). Fri 4/24 morning scan has not run yet — digest invoked manually ahead of the scheduled 6 AM ET plist firing.

**Executive summary:** Zero matches all five scan days. Seven-day rolling average dropped from 1.6/day (Apr 11–17) to 0/day (Apr 18–24) — this is a -100% week-over-week trend, not a random-noise zero-day. Two structural throttles remain unresolved (BizBuySell 403 block; `agent-browser` CLI missing so three highest-flow sources are dark). Fingerprint store is empty — likely infrastructure gap, not a natural zero-state, since two of the last three scan days (4/13, 4/16) produced 8 total matches that should have written fingerprints. Surfaced below.

---

## 1. Source Productivity (Last 7 Days)

**Caveat:** The `brain/context/deal-aggregator-fingerprints.jsonl` store is 0 bytes. Per 4/23 scan scorecard, every source's `Last Match Date` renders as "—" — the helper either isn't wired into the active scan path or nothing has been fingerprinted since the store was initialized 4/22. Per `feedback_test_before_concluding_channel_dead`, I'm treating "Last Match" as unknown-from-fingerprint but cross-referencing the prior week's (Apr 11–17) scan artifacts to attribute where matches originated. This row is an architecture gap to fix before next week's digest — see §5 Recommended Actions.

| Source | Category | 7d Matches | 7d Listings Reviewed | Last Known Match | Trend |
|--------|----------|-----------:|---------------------:|------------------|:-----:|
| Business Exits | General | 0 | ~120 | Apr 16 (via prior-week scan) | ↓ |
| Empire Flippers | General | 0 | ~30 | None recorded | → |
| Synergy Business Brokers | General | 0 | ~80 | None recorded | → |
| Website Closers | General | 0 | ~60 | None recorded | → |
| BizBuySell | General | 0 | 0 | 403 blocked entire window | ↓ |
| Flippa | General | 0 | 0 | JS shell / `agent-browser` missing | → |
| Quiet Light | General | 0 | 0 | 403 Cloudflare (email-only covers) | → |
| DealForce (email) | General | 0 | 0 | None | → |
| IAG M&A Advisors (email) | General | 0 | 0 | Flavia Milano active thread 4/16 | → |
| Rejigg (email) | General | 0 | 0 | Platform match 4/20 (off-thesis) | → |
| Everingham & Kerr (email) | General | 0 | 0 | 4/18-20, 4/22 all off-thesis | → |
| Viking Mergers (email) | General | 0 | 0 | Closest-read yacht brokerage 4/22 (below floor) | → |
| Benchmark International (email) | General | 0 | 0 | **Jun 30, 2025** (>10 months silent) | ↓↓ |
| Searchfunder | General | 0 | 0 | Alerts not enabled (Kay action pending) | → |
| Acquire.com | General | 0 | 0 | Not registered | → |
| Axial | General | 0 | 0 | Not registered — highest-leverage unblock | → |
| BizScout | General | 0 | 0 | Not registered | → |
| FE International | General | 0 | 0 | Not registered | → |
| Kumo (withkumo.com) | General | 0 | 0 | Not registered | → |
| Paine Pacific | General | 0 | 0 | Relationship-only, no public inventory | → |
| Woodbridge (Mariner) | General | 0 | 0 | Relationship-only, rebranded | → |
| ProNova Partners | General | 0 | 0 | 403, relationship-only | → |
| PCO Bookkeepers | Niche (Pest) | 0 | 0 | Tombstone images only | → |
| Anticimex US | Niche (Pest) | 0 | 3 | Intel-only (acquirer, not seller) | → |
| Keystone Business Advisors | Niche (Pest) | 0 | 0 | Login-gated, decision carried 5th day | → |
| Sica Fletcher | Niche (Insurance) | 0 | 7 | Feb 27 tombstone (Safe Harbour → ALKEME) | → |
| Agency Checklists | Niche (Insurance) | 0 | 3 | Intel-only; Jan 26 last MA tombstone | → |
| IA Magazine | Niche (Insurance) | 0 | 0 | Trade publication, no deals | → |
| MarshBerry | Niche (Insurance) | 0 | 7 | URL fix needed (/recent-transactions/ 404) | → |
| Reagan Consulting | Niche (Insurance) | 0 | 0 | Member-gated, no marketplace | → |
| Synergy Real Estate | Niche (Estate Mgmt) | 0 | 16 | Two below-floor listings 4/21 | → |
| Exit Strategies Group | Niche (Estate Mgmt) | 0 | 0 | Marketing-only page, CA-flagged | → |
| CMM Online | Niche (Cleaning) | 0 | 0 | Industry publication only | → |
| Inside Self-Storage | Niche (Art Storage) | 0 | 4 | Commodity self-storage REITs only | → |
| MidCap Advisors | Niche (Art Storage) | 0 | 4 | 2023 Artemis → Cadogan Tate (only US fine-art-logistics deal in 3 years) | → |
| DealFlow Agent | Niche (Pest) | 0 | 0 | **Not a listings board — confirmed 4/20** | ↓↓ |

**Trend arrow logic:** ↑/↓ = ±50% week-over-week match count; → = within ±50%. Prior-week baseline (Apr 11–17): 8 matches across 6 scan days (Apr 13: 6, Apr 16: 2). This week: 0 across 5 scan days. The two sources with clear prior-week activity attribution (Business Exits, BizBuySell) are both marked ↓. Benchmark + DealFlow Agent marked ↓↓ because they're structurally broken, not just off-week.

## 2. Volume Check

- **7-day rolling average:** 0.0/day (0 matches ÷ 5 scan days)
- **Prior-week rolling average:** 1.6/day (8 matches ÷ 5 scan days, Apr 11–17)
- **Week-over-week change:** -100%
- **Target:** 1–3/day
- **Status:** 🔴 **Critical**

**Diagnosis:** This is not a flow problem at the source-universe level — Kay's accessible sources produced 8 matches the prior week. The primary delta this week is BizBuySell staying dark for 5 consecutive scan days (prior-week matches originated disproportionately there per 4/20 scan note), combined with the niche portfolio narrowing from 15 active theses (Apr 17) to 8 (Apr 20 onward). Both cuts reduce surface area. Neither is a scan bug.

**Not a calibration failure:** Data Availability Rule is functioning (4/23 scan shows zero auto-rejects on missing fields). Hard-excludes are holding. Near-miss list on the 4/22 and 4/23 artifacts is dense — the filter is finding things, just nothing in-thesis AND in-band AND above floor.

## 3. Proposed Additions

### 3.1 Helen Guo — SMB Deal Hunter (newsletter, off-market blasts)

- **Why:** Appeared in inbox 4/20 ($2.9M blast), 4/22 ($2.9M blast), 4/23 (5 listings — all below $1.5M EBITDA floor this week). Consistent weekly cadence, specific-deal format (not marketing), human-curated (not algo feed). Not currently on the Sourcing Sheet. Listings this week were all sub-floor, but the channel format is legitimate BLAST source and at ~5 deals/week it expands SMB screening volume for niches sitting just below the $10M revenue threshold (Premium Pest, Specialty Coffee Equipment Service, High-End Commercial Cleaning where lower-mid-market inventory can surface unexpectedly).
- **Recommended tab:** General Sources
- **Row values:** Status = "Active - email-only" · Source = "SMB Deal Hunter (Helen Guo)" · Type = "Newsletter blast" · Access = "Public (subscribed)" · URL = [not yet captured — Kay's inbox header holds sender domain] · Notes = "Weekly ~5-listing blast; 4/20–4/23 inventory all below buy-box floors but format is legitimate BLAST source. Monitor 30 days — retire if 0 hits."
- **Access:** Free (already subscribed)
- **RECOMMEND: Add to General Sources** → YES / NO / DISCUSS

### 3.2 Activate Axial (elevate from "Pending registration" to active priority)

- **Why:** Axial is the single most-repeated unblock recommendation in the scan artifacts (flagged 4/20, 4/21, 4/22). Major LMM M&A deal network; brokers post into vetted-buyer network. Requires membership by invite/request. Already on the Sourcing Sheet as "Pending G&B registration" but has been stuck there without a registration push. Elevating this doesn't add a row — it adds a Kay-action to register, which would unblock the most frequently-cited coverage gap across a month of scans.
- **Recommended tab:** General Sources (status change only, no new row)
- **Access:** Membership by invite/request
- **Why elevate now:** Five consecutive scan days with zero matches makes the opportunity cost of the structural gap tangible. Registration is a single Kay action; scraping is automatic thereafter.
- **RECOMMEND: Priority-flag Axial registration this week** → YES / NO / DISCUSS

### 3.3 Activate GP Bullhound (flip from "Not yet scanning" to Active)

- **Why:** Already on the Niche-Specific Sources sheet under Vertical SaaS as "Not yet scanning." Repeatedly flagged across 4/17, 4/20, 4/21 scans as the sole meaningful addition that would close the vertical-SaaS source coverage gap. Global tech M&A advisor, $58B+ deal value since 1999, 183 M&A deals. Public news-release page. Flipping status to Active is a one-line sheet edit plus adding the URL to the weekly scan rotation.
- **Recommended tab:** Niche-Specific Sources (status change only)
- **Access:** Public (tombstones / news releases)
- **Caveat:** Vertical SaaS is the **only** niche on the current 8-niche active list where GP Bullhound is relevant. If the Vertical SaaS niche gets deprioritized (Kay's 4/20 ranking put it rank 6), this activation becomes lower-value.
- **RECOMMEND: Flip GP Bullhound to Active** → YES / NO / DISCUSS

---

**Sources considered and rejected as additions:**

- **Karlton Dennis / Tax Alchemy, Athena Simpson / Acquimatch, Walker Deibel / BuyThenBuild, Michael Girdley, Nick Huber, Peter Lang DigitalAgencyBusiness** — newsletter/course/workshop pitches, not deal sources. Skip.
- **Beacon / Anacapa** — investor AI newsletter, not a deal source.
- **PE Hub (autism care platform scaling)** — industry publication, already captured adjacent niches as intel-only, autism not a G&B thesis.
- **NAIFA-NY / IA Magazine** — already on sheet as intel-only for Specialty Insurance.
- **Frieze NY 2026 invite** — conference/event, belongs in conference-discovery queue, not deal-aggregator sources.
- **ALKEME Intermediary Holdings** — dominant PE consolidator in Q1 2026 Specialty Insurance. Not a source for Kay (they're her buyer competition), but worth tracking as market-intel. Does not belong on Sourcing Sheet.

## 4. Proposed Retirements

### 4.1 DealFlow Agent → Dormant

- **Match history:** 0 matches since added to scan rotation
- **4/20 confirmation:** "Confirmed NOT a listings board — sell-side landing page marketing to pest owners. Recommend removing from scan list."
- **4/21 re-verification:** Landing page only; `/listings` 404; marketing-buyer-counts content only; no live seller listings.
- **Three live-checks:**
  1. URL resolves — ✅ `dealflowagent.com` loads
  2. Domain registered — ✅ (active)
  3. Purpose check — ❌ **Not a deal source.** Landing page for acquirers (buyer-side marketing tool), no seller-side listings feed. This fails the "is this a source we can pull deals from" test.
- **Rationale:** Not a retirement due to staleness — this source should never have been on the list as a deal source. Move to Dormant (preserving history per spec) with a note explaining it's a marketing landing page, not a marketplace. If DealFlow Agent launches a seller-side marketplace in the future, re-evaluate.
- **RECOMMEND: Move DealFlow Agent to Dormant on Sourcing Sheet (Niche-Specific tab)** → YES / NO / DISCUSS

### 4.2 Benchmark International → Dormant (formalize existing flag)

- **Match history:** Welcome + confirmation emails 2/24-27/2025; match alerts through 6/30/2025 then silence. 10+ months no activity.
- **Three live-checks:**
  1. URL resolves — ✅ `embracebenchmark.com` loads
  2. Domain registered — ✅ (active firm, Nexus Buyer Portal exists)
  3. Email channel status — ❌ **No activity in 90+ days** (per Sourcing Sheet notes, no activity since 6/30/2025). Gmail query for `from:benchmarkintl` returned zero hits in last 90 days per 4/23 email-scan.
- **Current sheet status:** Labeled "Registered - dormant" already. Proposal is to formalize as "Dormant" for system consistency and to surface whether Kay wants to re-engage (re-activate saved searches on Nexus Buyer Portal) or formally retire.
- **Edge case per `feedback_test_before_concluding_channel_dead`:** Firm is alive and publishes M&A reports; inactivity is on our subscription, not theirs. Dormant (not retired) is the right status.
- **RECOMMEND: Formalize Benchmark International as Dormant on Sourcing Sheet (General tab)** → YES / NO / DISCUSS

---

**Retirements considered and rejected:**

- **Business Exits** — 4th consecutive off-mix day flagged 4/17; 4/20 scan proposed moving to weekly cadence if 0-match pattern held through 4/24. Pattern did hold. But Business Exits produced Kay's only prior-week matches (Apr 16: 2 listings) and 30 listings reviewed on 4/23 — the source is still flowing inventory, just not in-thesis this week. **Proposed:** keep daily, re-evaluate next Friday. Not a retirement.
- **ProNova Partners, Paine Pacific, Woodbridge (Mariner)** — All relationship-only, not expected to produce marketplace volume. Keep on sheet for relationship context. Not retirements.
- **Sica Fletcher** — Flagged falsely as 404 earlier in April, reactivated 4/21 per `feedback_test_before_concluding_channel_dead`. Intel-only but live. Keep.

## 5. Recommended Actions (Kay's Review Bucket)

All proposals are approval-gated. On YES, I'll execute the sheet write (with the pre-write snapshot per `feedback_subagent_sheet_write_safety`) and write a trace to `brain/traces/`. NO/DISCUSS = no write.

**Additions:**
1. **RECOMMEND: Add Helen Guo / SMB Deal Hunter to General Sources** — consistent weekly BLAST source, all sub-floor this week but legitimate format → YES / NO / DISCUSS
2. **RECOMMEND: Priority-flag Axial registration this week** — single most-cited unblock across the month → YES / NO / DISCUSS
3. **RECOMMEND: Flip GP Bullhound from "Not yet scanning" to Active** — closes Vertical SaaS coverage gap → YES / NO / DISCUSS

**Retirements:**
4. **RECOMMEND: Move DealFlow Agent to Dormant on Niche-Specific Sources** — confirmed not a deal source → YES / NO / DISCUSS
5. **RECOMMEND: Formalize Benchmark International as Dormant on General Sources** — 10+ months silent, already flagged → YES / NO / DISCUSS

**Infrastructure (outside the additions/retirements spec, but blocking volume):**
6. **RECOMMEND: Install `agent-browser` CLI on this host** — unblocks BizBuySell, Flippa, Quiet Light web-scrapes (3 highest-volume general platforms) → YES / NO / DISCUSS
7. **RECOMMEND: Debug empty fingerprint store** — `brain/context/deal-aggregator-fingerprints.jsonl` is 0 bytes. Either the helper script isn't wired into the active scan path or fingerprints never wrote during Apr 13/16 match days. Blocks accurate source-attribution in future digests → YES / NO / DISCUSS

---

**CFO ownership:** 6, 7 (infrastructure / tooling spend + hygiene)
**CIO ownership:** 2, 3 (source activation decisions tied to thesis coverage)
**CMO ownership:** 1 (content-channel / voice-of-source additions)
**GC ownership:** 4, 5 (tracker/source housekeeping with write-back to sheet)

## Slack Notification Status

Per spec: send to `SLACK_WEBHOOK_OPERATIONS` when ≥1 proposed change OR volume = 🔴. Both conditions are met — normally fires automatically.

**Held for Kay approval** per `feedback_draft_before_send`. Draft below:

> 🔴 Deal Aggregator — Weekly Digest 2026-04-24
>
> Volume: 0/day (critical, down from 1.6/day last week)
> Proposals: 3 additions, 2 retirements, 2 infrastructure fixes — awaiting approval
> Full digest: `brain/trackers/weekly/2026-04-24-deal-aggregator-digest.md`

Fire to `#operations`? → YES / NO

---

## Validation

- [x] Digest file exists at `brain/trackers/weekly/2026-04-24-deal-aggregator-digest.md`
- [x] All 5 required sections present (Source Productivity, Volume Check, Proposed Additions, Proposed Retirements, Recommended Actions)
- [x] Each proposed addition includes rationale + recommended tab + access method
- [x] Each proposed retirement includes 3 live-check results (URL resolves, domain registered, email/purpose check)
- [x] Trend column populated via prior-week (Apr 11–17) scan-artifact comparison (not fabricated)
- [x] Fingerprint data gap surfaced honestly (store is 0 bytes; attribution is from scan artifacts, not JSONL)
- [x] Slack notification drafted but not sent — awaiting Kay approval per `feedback_draft_before_send`
- [x] No auto-writes to the Sourcing Sheet — all 5 proposals await Kay's approval before any sheet write

## Data Sources (this digest)

- `brain/context/deal-aggregator-scan-2026-04-20.md`
- `brain/context/deal-aggregator-scan-2026-04-21.md`
- `brain/context/deal-aggregator-scan-2026-04-22.md` (+ afternoon)
- `brain/context/deal-aggregator-scan-2026-04-23.md` (+ afternoon)
- `brain/context/deal-aggregator-scan-2026-04-17.md` (prior-week reference)
- `brain/context/email-scan-results-2026-04-{18,19,20,21,22,23}.md`
- `brain/context/deal-aggregator-fingerprints.jsonl` (empty — data gap flagged)
- `G&B Deal Aggregator - Sourcing List` sheet ID `1z8o2obq2mOG9drQ0umCmBk31K3OS2afMNGpVAlbLljw` (General Sources + Niche-Specific Sources tabs)

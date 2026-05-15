---
schema_version: "1.0.0"
date: 2026-05-15
type: tracker
title: "Deal Aggregator Weekly Digest — 2026-05-15"
window_start: 2026-05-08
window_end: 2026-05-15
volume_7d_avg: 0.0
volume_prior_week_avg: 0.0
volume_status: "🔴 Critical"
proposed_additions: 1
proposed_retirements: 0
opportunistic_count: 0
sourcing_sheet_source: live
fingerprint_store_status: empty
tags:
  - date/2026-05-15
  - tracker
  - topic/deal-aggregator
  - topic/weekly-digest
  - status/draft
---

# Deal Aggregator Weekly Digest — 2026-05-15

Window: **2026-05-08 → 2026-05-15** (5 weekday scans: Thu 05-08, Mon 05-11, Tue 05-12, Wed 05-13, Thu 05-14; Fri 05-15 morning daily-scan runs on a separate plist and isn't read by this digest. Weekend gaps 05-09/05-10 are expected — no scheduled scan.)

## 1. Source Productivity (Last 7 Days)

| Source | Category | 7d Matches | 7d Listings Reviewed | Last Match | Trend |
|---|---|---:|---:|---|:---:|
| Business Exits | General | 0 | 150 | — | → |
| Synergy Business Brokers | General | 0 | 100 | — | → |
| Empire Flippers | General | 0 | 90 | — | → |
| Website Closers | General | 0 | 63 | — | → |
| Synergy Business Brokers Real Estate | Niche / Estate Mgmt | 0 | 28 | — | → |
| Sica Fletcher | Niche / Specialty Insurance | 0 | 7 | — | → |
| Flippa | General | 0 | 6 | — | → |
| GP Bullhound | Niche / Vertical SaaS | 0 | 6 | — | → |
| BizBuySell | General | 0 | 0 | — | → |
| DealForce | General | 0 | 0 | — | → |
| Everingham & Kerr | General | 0 | 0 | — | → |
| IAG M&A Advisors | General | 0 | 0 | — | → |
| PCO Bookkeepers | Niche / Premium Pest | 0 | 0 | — | → |
| Quiet Light | General | 0 | 0 | — | → |
| Rejigg | General | 0 | 0 | — | → |
| SMB Deal Hunter (Helen Guo) | General | 0 | 0 | — | → |
| Viking Mergers | General | 0 | 0 | — | → |

- Sources listing rows = 17 (all sheet-Active sources on General + Niche-Specific tabs).
- Total listings reviewed across the week: **450** — concentrated on Business Exits / Synergy / Empire Flippers / Website Closers (general-platform horsepower).
- Total buy-box matches across the week: **0**.
- Trend column compares to prior digest 2026-05-02 (window 04-25 → 05-02), which also reported 0 matches across all sources → `→` (within ±50%) is unanimous.
- **`fingerprint_store_status: empty`** — `brain/context/deal-aggregator-fingerprints.jsonl` is 0 bytes (no historical hits have been appended). Per SKILL.md failure handling, Source Productivity is computed from the daily scan artifacts' Source Scorecard tables (not the fingerprint JSONL) and "Last Match" reads `—` for every source.

## 2. Volume Check

- 7-day rolling average: **0.0/day**
- Target: 1–3/day
- Status: **🔴 Critical**
- Prior-week average (04-25 → 05-02): 0.0/day → no week-over-week movement.
- Read: 450 listings reviewed across 5 weekday scans is healthy scan throughput; the gap is at the buy-box gate, not at scan coverage. Either (a) the active niche corpora are too narrow to convert general-platform scan volume, or (b) the disclosed-field discipline is auto-flagging every candidate to FLAG/NEAR-MISS rather than PASS. Worth a calibration pass — see Section 5.

## 3. Proposed Additions

1. **NPMA (National Pest Management Association)** — Niche / Premium Pest Management | https://www.npmapestworld.org/
   - Why: Recurring inbound from `npma@npmapestworld.org` in this and prior week's email-scan-results (NPMA Events, PestWorld 2026 registration). Listed in this skill's SKILL.md Channel 4 (Association Deal Boards) as the canonical pest-management association deal board (4,000+ member companies), but missing from the Sourcing Sheet — so it doesn't appear in any Source Scorecard or fingerprint attribution. Adding it formalises the channel and lets the daily scan track classifieds / member-transition signals.
   - Recommended tab: **Niche-Specific Sources → Premium Pest Management**
   - Access: **Public (free)** — `https://www.npmapestworld.org/` returns HTTP 200 on web-verify (2026-05-15). Member directory/classifieds may require Kay's existing NPMA membership for full visibility; public-tier scan available regardless.
   - Type: `association deal board`
   - **RECOMMEND: Add to Niche-Specific Sources (Premium Pest Management) — status `Active - newsletter`** → YES / NO / DISCUSS

(All other unknown sender domains in the inbox window were classified out: BK Growth = independent-sponsor peer, not a deal source; Pacific Lake / Terramar Search = search-fund LPs / peer searchers; Meetmax / Cvent = conference-scheduling infrastructure; Uber / Dodo / Google / SF mail = operational/transactional. None merit a Sourcing Sheet row.)

## 4. Proposed Retirements

None this week.

- Per SKILL.md `<weekly_digest>` retirement-side spec, a proposed retirement requires (a) 30+ days no fingerprint-attributed match AND (b) 3 live-checks performed (URL resolves, domain registered, email-channel status). The fingerprint JSONL is empty across all sources, so signal (a) is undefined — silence on an instrument that has never been written is not silence from the source. Per `feedback_test_before_concluding_channel_dead`, never retire on absent data.
- The fingerprint instrumentation gap is itself a Section 5 item — that's the right place to flag it, not Section 4.

## 5. Recommended Actions (Kay's Review Bucket)

1. **NPMA → add to Niche-Specific Sources (Premium Pest Management)** — RECOMMEND: ADD → YES / NO / DISCUSS
2. **Volume = 🔴 second consecutive week (0 deals/day vs 1–3/day target)** — 450 listings reviewed, 0 PASS. RECOMMEND: schedule a corpus-tuning pass on the active niches' DEALSX keyword sets + WR-row enrichment terms next Tuesday (alongside niche-intelligence) → YES / NO / DISCUSS
3. **Fingerprint store has never been written (`fingerprints.jsonl` 0 bytes)** — every Slack-notification call site is supposed to `add` after `check`, but the file has stayed empty since file creation 2026-05-07. Either (a) no matches have actually hit the Slack path in 8 days (consistent with 0 PASS verdicts above) or (b) the helper is silently failing. RECOMMEND: have the next morning run print the `deal-aggregator-fingerprint.sh add` exit code to its scan artifact so we can distinguish those cases → YES / NO / DISCUSS

---

### Sources read

- Daily scans (5): `brain/context/deal-aggregator-scan-{2026-05-08,11,12,13,14}.md`
- Email-scan results (7): `brain/context/email-scan-results-{2026-05-08,09,10,11,12,13,14}.md`
- Fingerprint store: `brain/context/deal-aggregator-fingerprints.jsonl` (0 bytes — empty)
- Sourcing Sheet: `1z8o2obq2mOG9drQ0umCmBk31K3OS2afMNGpVAlbLljw` — General Sources (22 rows) + Niche-Specific Sources (24 rows), live-read this run
- Prior digest for trend comparison: `brain/trackers/weekly/2026-05-02-deal-aggregator-digest.md`

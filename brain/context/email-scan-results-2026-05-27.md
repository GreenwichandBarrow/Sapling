---
date: 2026-05-27
type: context
title: "Email Scan Results — 2026-05-27 (Wed AM, headless 7am)"
tags:
  - date/2026-05-27
  - context
  - topic/email-scan-results
  - topic/email-intelligence
  - status/done
---

# Email Scan Results — 2026-05-27

Headless 7am ET weekday run. Scanned 21 inbound threads (`newer_than:2d label:INBOX`), 2 outbound, 14 Gmail drafts, 2 Granola notes since yesterday. No CIM, NDA, or LOI attachments detected today. No bookkeeper P&L from `startvirtual.com` this run — bookkeeper chain not fired. One Granola call note backfilled (Oswaldo Ponce, recovering the stuck 5/26 post-call-analyzer queue item). One new entity stub created (Carlos at in3o). Two DEAL_NEWSLETTER digests parsed for per-listing extraction (Helen Guo SMB Deal Hunter 5/26 + Flippa Daily 5/26) — 9 listings extracted across both.

---

## 1. Actionable Items Created

| File | Source | Trigger | Urgency |
|---|---|---|---|
| [[brain/inbox/2026-05-27-carlos-in3o-anacapa-circle-back]] | Gmail thread `19e661bafc8d39e9` (Carlos @ in3o, 5/26 17:05 ET) | Kay committed "I will circle back" after her Anacapa call today | normal |
| [[brain/calls/2026-05-26-oswaldo-ponce]] | Granola note `not_Gn4BVFoV13pDKF` (Oswaldo / POZA Capital Partners, 5/26 12:00 ET) | Backfill — original post-call-analyzer queue item silent-crashed 5/26 (per session-decisions Open Loop #4); ingested this run | normal |

**Carlos in3o entity stub created** at [[entities/carlos-in3o]] — new contact (carlos@in3o.com), last name unknown, in3o portfolio includes Renue Environmental + Recvoil (CL) + IA Energy.

**No CIM, NDA, or LOI attachments detected today.** Project Drone thread (`19e41c8761d4c882`) had no inbound from Carlos Nieto in the 2-day window — last activity was Kay's outbound on 5/26 19:44 asking about Slide 36. Already in pipeline at `Financials Received` per session-decisions 5/26. No new fast-path action.

---

## 2. Deal Flow Classified

| Class | Count | Notes |
|---|---|---|
| DIRECT | 3 | Carlos @ in3o (intro request) · Katie Walker @ Plexus Capital (personal check-in) · Carlos Nieto / DCA (Project Drone — ongoing Active Deal thread, no new inbound today, Kay's outbound is most recent message) |
| BLAST | 0 | No multi-recipient broker BLAST today |
| NEWSLETTER | 18 | Includes 2 DEAL_NEWSLETTER subtypes (Helen Guo SMB Deal Hunter, Flippa Daily) — listings extracted to section 7; classified NEWSLETTER here per `<broker_blast_listing_extraction>` reconciliation rule. Other 16: Axios x3, DMARC report, SMBootcamp Live promo, Stumptown receipt, CorpNet Delaware tax promo, Attio product update, XPX events x4, Acquiring Minds podcast newsletter (content-only, no listings), Art Market post-event, 1Password promo, Axial Middle Market Review (case-study NEWSLETTER, no active listings) |

**Section-2 reconciliation note:** Helen Guo + Flippa counted under NEWSLETTER (no double-count); their per-listing rows are in Section 7. Section 7 row count is the deal-flow KPI, not Section 2 BLAST count.

---

## 3. Draft Status

14 Gmail drafts pending in account. **Not addressed this run** — per session-decisions-2026-05-26 Deferred #9, drafts are related to investor update + DealsX/JJ wind-down work in flight; Kay is handling personally. No new drafts created today (no NDA/CIM auto-ack triggers fired). No drafts flagged stale (>48h) for surfacing because the underlying threads are still live work.

**One-line metadata only** returned by `gog gmail draft list` — message-body details not surfaced this run; pipeline-manager has visibility from prior runs.

---

## 4. Introductions Detected

None per the strict `<intro_detection>` pattern (no "I'd like to introduce", no CC-pattern intros, no "thought you two should connect" forwards in the 2-day window).

**Adjacent — flagged but not a section-4 intro:** Carlos @ in3o asked Kay for an outbound intro into Anacapa for his portfolio company Renue Environmental. That is a meta-intro request (Carlos wants Kay to introduce HIM), not an incoming intro to a new person — handled via inbox item, not Section 4.

---

## 5. Niche Signals

- **Pest management (HIGH SIGNAL — direct intel for [[brain/outputs/2026-05-26-pest-10-co-june-experiment-plan|June 10-co experiment]]):** From Oswaldo Ponce call 5/26 — POZA Capital Partners invested $35M into a pest platform. Account-monetization economics: sell mature accounts at 1.5-2x ARR to fund new account acquisition at ~70% ARR cost. Op's read: "strong business model, market tapped out on multiples." Surface to pest experiment thread.
- **Insurance brokerage (CONFIRMING SIGNAL):** Op confirms 20x earnings multiples are pricing deals out of economic range, but $200-500K small-book opportunities exist on existing-platform basis. Aligns with [[feedback-insurance-revenue-buybox]] (Kay's existing $40M floor).
- **Search-fund market dynamics:** Op reports close rate dropped from ~65% to ~40%; investors carrying 12+ searchers past 24-month mark. Validates [[project-dealsx-jj-windown-by-summer]] thesis that traditional structure is under pressure.
- **PE down-market pressure:** Op confirms PE moving down-market into $2-7M EBITDA range, validating Kay's 2026-05-19 floor-relaxation decision per [[feedback-deal-screen-300k-salary-15pct-margin]].
- **Industrials M&A outlook (Axial Middle Market Review 5/26):** Axial respondents bullish on 2026 industrials M&A despite macro uncertainty. HVAC at 13x, defense at 12x, metals <5x. Context only — no buy-box implication today.
- **From Helen Guo 5/26 listings:** Trucking licensing/compliance (CA, $412K EBITDA, recurring annual filings, remote-operable) and dairy equipment sales/service (UT, 50yr franchise relationships, secular robotic-milking adoption + service-radius moat) are niche-adjacent observations. Both screened out of pest experiment but cataloged for niche memory.

---

## 6. In-Person Meetings Today

| Time | Meeting | Granola reminder? |
|---|---|---|
| TBD | Anacapa Partners call | YES — Granola on, Kay's 5/26 reply to Carlos in3o committed to "circle back" with intel post-call |

*(Calendar pull deferred to pipeline-manager / brief-decisions pre-flight per workflow split.)*

---

## 7. Broker BLAST Listings (per-deal extraction)

Two DEAL_NEWSLETTER triggers fired today (Helen Guo SMB Deal Hunter known-sender + Flippa Daily known-sender). 9 listings extracted total. No broker BLAST with broker-signal keywords detected today.

| source | headline | geo | revenue | ebitda | margin | industry | flag_reason | gmail_msg_id | listing_ordinal |
|---|---|---|---|---|---|---|---|---|---|
| Helen Guo, SMB Deal Hunter | Absentee-Run Commercial Sign Manufacturer ($2.95M ask) | MO | $4.36M | $661K | 15% | Sign manufacturing + LED retrofit service | deal-newsletter-known-sender | 19e656820ec74fd6 | 1 |
| Helen Guo, SMB Deal Hunter | Trucking Licensing and Compliance Services Platform ($1.43M ask) | CA | $1.04M | $412K | 40% | Trucking compliance / recurring annual filings | deal-newsletter-known-sender | 19e656820ec74fd6 | 2 |
| Helen Guo, SMB Deal Hunter | Facility Maintenance Contractor for National Grocery + Convenience ($3.2M ask) | UT | $4.51M | $838K | 19% | Facility maintenance / multi-state | deal-newsletter-known-sender | 19e656820ec74fd6 | 3 |
| Helen Guo, SMB Deal Hunter | Specialty Copper-Infused Lumber Wholesaler ($2.35M ask) | NC | $4.72M | $698K | 15% | Specialty lumber wholesale | deal-newsletter-known-sender | 19e656820ec74fd6 | 4 |
| Helen Guo, SMB Deal Hunter | Dairy Equipment Sales, Service & Installation, 50-yr franchise ($1M ask) | UT | $2.5M | $443K | 18% | Dairy equipment / robotic milking + consumables | deal-newsletter-known-sender | 19e656820ec74fd6 | 5 |
| Flippa Marketplace | Established Audio Production / Dubbing / Localization Service (11 yrs, 100+ clients) | MD (broker Amber Burke) | $2.1M | undisclosed | undisclosed | Audio post-production / entertainment services | deal-newsletter-known-sender | 19e65ab925842cad | 1 |
| Flippa Marketplace | Reliable Fire Alarm Equipment Reseller (Shopify+eBay liquidation play, 2 yrs) | undisclosed | $440K | undisclosed | 56% | Fire alarm equipment resale / e-commerce | deal-newsletter-known-sender | 19e65ab925842cad | 2 |
| Flippa Marketplace | All-In-One Waitlist SaaS (4 yrs, API + no-code widgets, F500 customers) | undisclosed | $142K ($13K MRR) | undisclosed | 74% | SaaS / waitlist + analytics | deal-newsletter-known-sender | 19e65ab925842cad | 3 |
| Flippa Marketplace | Thriving Survival Game YouTube Channel (Rust, 12 yrs, 252K subs) | undisclosed | $56K | undisclosed | 98% | YouTube / gaming content | deal-newsletter-known-sender | 19e65ab925842cad | 4 |

**Pipeline-manager screening notes (preview):** Helen Guo #2 (CA) hits [[feedback-no-california]] hard exclude. Helen Guo #1, #3, #4, #5 are sub-$1M EBITDA single-state operators; outside Kay's NY-sourcing-concentration lens per [[feedback-industry-is-output-of-network]] (2026-05-20 structural reframe — industry is output of network access, not input). Flippa listings all sub-$1M revenue or pure-SaaS / content — outside thesis. Per [[project-athena-simpson-sourcing-review]] buyer-fingerprint screen, these surface as flow-volume context only; not advancing to outreach.

---

## 8. Auto-Drafts Created

None. No inbound emails this run carried NDA-like or CIM-like attachments matching `<auto_ack_drafts>` triggers.

---

## Granola Action Items

From [[brain/calls/2026-05-26-oswaldo-ponce|Oswaldo Ponce / POZA Capital Partners — 5/26 12pm ET call]]:

- [ ] Kay: send Op any logistics/manufacturing deals outside POZA's $3-7M EBITDA range that surface in pipeline (mutual deal-sharing pact established verbally on call). Continuous trigger.
- [ ] Kay: incorporate Op's $35M pest platform intel + account-monetization economics (sell mature 1.5-2x ARR / acquire 70% ARR) into pest 10-co June experiment thread.
- [ ] Kay: file Op's "self-funded searcher 50/50 partnership" structure as a Plan-B option for next investor update cycle.
- [ ] `relationship-manager`: set Op's Attio `next_action` to "share first logistics/manufacturing deal outside POZA mandate."

Sam Curcio Granola note `not_v0sa5nV8gTSYNO` updated 5/26 15:58 but call note already exists at [[brain/calls/2026-05-22-sam-curcio]] — skipping (idempotency per `<granola_ingestion>` rule).

---

## System Status

- **🟢 Bookkeeper P&L chain — wired (not fired today):** No inbound from `*@startvirtual.com` and no "Management Report" subject in scan window. Trigger remains armed per [[feedback-bookkeeper-pl-auto-trigger-budget-manager]].
- **🟢 Helen Guo deal-newsletter parser — fired correctly:** Patched parser shipped 2026-05-26 (per session-decisions) extracted all 5 listings from `In Today's Issue` section while ignoring the Chelsea pet-food Member Spotlight + Robert home-health Podcast Episode sections. The 2026-05-26 case-study coexistence bug is resolved.
- **🟢 Flippa marketplace digest — fired correctly:** Extracted 4 active listings; excluded 3 "Daily Just Sold" comparables + 1 Saudi Arabia funding-round opportunity (per [[feedback-us-tam-not-global]]).
- **🟡 Post-call-analyzer queue file `not_Gn4BVFoV13pDKF.json`:** Backfilled via email-intelligence this run (Oswaldo call note written). Queue file in `brain/trackers/post-call-analyzer/queue/` should be removed by the next post-call-analyzer fire to avoid duplicate processing.
- **🟢 1Password credential resolve — verified:** `source scripts/op-env.sh` clean; Gmail + Granola REST both 200.
- **🟢 Granola REST (via `granola-api`) — verified:** 2 notes pulled, transcripts + summaries intact.

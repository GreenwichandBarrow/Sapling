---
schema_version: 1.1.0
date: 2026-04-24
type: context
title: "Email Scan Results — 2026-04-24"
tags: [date/2026-04-24, context, topic/email-intelligence, topic/morning-workflow, person/jim-vigna, person/barrie-green, person/scott-etish, person/amanda-lo-iacono, person/will-bressman, person/evan-reinsberg, person/kristin-wihera, person/mark-gardella, company/live-oak-bank, company/coventry, company/two-bridges-legacy-partners]
people: ["[[entities/jim-vigna]]", "[[entities/barrie-green]]", "[[entities/scott-etish]]", "[[entities/amanda-lo-iacono]]", "[[entities/will-bressman]]", "[[entities/evan-reinsberg]]", "[[entities/kristin-wihera]]", "[[entities/mark-gardella]]"]
companies: ["[[entities/live-oak-bank]]", "[[entities/coventry]]", "[[entities/two-bridges-legacy-partners]]"]
---

# Email Scan Results — 2026-04-24

Scan window: 2026-04-22 07:15 ET → 2026-04-24 07:00 ET (48h). Inbound (`kay.s@`): ~24 threads. Outbound from `kay.s@`: 4 threads touched on 4/22 (Amanda reply, Bettina/Denning thread, InsurTech Spring thread, "Hi" thread) — all within session-decisions window. Granola meetings since last scan: 2 captured on 4/23 ([[entities/kristin-wihera|Kristin Wihera]] WSN post-mortem 4 PM + XPX NYC LMM panel 8:30 AM) — **both still unlanded in `brain/calls/`** (most recent is `2026-04-22-wsn-group.md`), vault writes blocked per [[context/session-decisions-2026-04-23]]. Superhuman CLI: **G&B OAuth token still expired** (4/22 incident, 3 days running). Cross-checked against [[context/session-decisions-2026-04-22]], [[context/session-decisions-2026-04-23]], and [[context/session-decisions-2026-04-24]] (bookend-only) — resolved items suppressed.

## 1. Actionable Items Created

None. No new inbox items written — no CIMs, no NDAs, no LOIs, no active-deal fast-path triggers, no new warm intros in the 48h window. Material signals below route to pipeline-manager / relationship-manager / CPO.

## 2. Deal Flow Classified

- **DIRECT deal-related: 0** — No personalized owner/intermediary inbound.
- **DIRECT relationship/networking: 2**
  - **[[entities/jim-vigna|Jim Vigna]] (SVP Small Business Lending, [[entities/live-oak-bank|Live Oak Bank]]) 4/23 17:04** — warm follow-up from an in-person meeting earlier that day (context not in vault yet — likely XPX NYC panel networking, same-day as Axial/XPX transcript). Offers: coffee/lunch, deal-review sanity-checks, ongoing touchpoint through search. Classic river-guide-adjacent lender contact. **Routes to relationship-manager** (CPO) — add to Attio with nurture cadence + suggest 15-min reply today thanking him and accepting deal-review offer. No urgency, but 24-48h reply window per `feedback_followup_timing`.
  - **[[entities/scott-etish|Scott Etish]] ([[entities/coventry|Coventry]]) 4/23 10:26** — sent a life-insurance/fiduciary-considerations article. Coventry = secondary life-insurance market (life-settlements). Adjacent to Specialty Insurance niche but not a target. Nurture-cadence touch, low-urgency reply within a week. **Routes to relationship-manager** (CPO).
- **DIRECT internal/ops: 1**
  - **[[entities/barrie-green|Barrie Green]] (assistant, internal) 4/23 08:49** — "Heads up: your calendar has upcoming conflicts." Two overlaps flagged for next week: **Tue 4/28 1:00-2:00 PM ET** (Athena Simpson MatchMaker Method + AcquiMatch MatchMaker Method Live Training — likely same program, duplicate invite) and **Wed 4/29 2:30-2:45 PM ET** (Megan<>Kay 2:30-3:00 vs `p/u KI` 2:30-2:45 on personal calendar). Barrie is asking two preference questions: (a) should `p/u KI`-style family pickups be auto-protected Do Not Schedule, (b) should webinars/trainings default to "flexible/recorded." **Routes to pipeline-manager Decisions bucket** (CPO) — two one-line Obama-framed decisions for Kay.
- **BLAST: 6** (mostly One Hanover googlegroups + marketing)
  - [[entities/evan-reinsberg|Evan Reinsberg]] (Two Bridges Legacy Partners, One Hanover list) 4/23 17:09 — FedEx shipping favor ask, not relevant to Kay (not in NYC office). **Suppress.**
  - [[entities/will-bressman|Will Bressman]] (One Hanover) 4/23 11:57 — HBS parody ETA video, light/community post. [[entities/andrew-saltoun|Andrew Saltoun]] replied in thread 4/23 14:27 ("Hahahah"). No action. **Suppress.**
  - Athena Simpson / AcquiMatch ×3 — post-promo marketing ("You sent the offer, they chose someone else," "VIDEO 1 of 3 I recorded for you," "Same buyer, completely different outcome"). Noise; the MatchMaker Method training duplicate invite is what Barrie flagged. **Suppress.**
  - Tory @ Flippa 4/23 14:59 — $16M B2B Trade Fair Exhibitor Recruitment Service. Off-thesis (not luxury-adjacent B2B services to luxury); pass-through to deal-aggregator for dedup.
  - Mitchell Baldridge 4/23 15:00 — "Better Bookkeeping is now Visor" rebrand announcement. G&B does not use them. **Suppress.**
- **NEWSLETTER: ~9** — Axios AM (Day 1 impeachment 4/24), Axios PM (Stock split 4/23), Axios Finish Line 4/23, HBR ("five-day workweek" 4/24), David Gritz InsurTech News ("Knowing the Heart of the Problem" 4/23 — insurance niche signal, filed §5), Frieze NY VIP ("Behind the Scenes at Frieze NY 2026" 4/23 — art-infrastructure niche signal, filed §5), NAIFA-NY April newsletter 4/22 (insurance niche signal, filed §5), Wispr Flow product update 4/23, Slack onboarding reminder 4/24. Auto-filed.
- **OPERATIONAL / SYSTEM: 2** — DMARC aggregate reports ×2 (Google + Microsoft, 4/23-24, routine domain-auth reporting).

## 3. Draft Status

**Superhuman CLI still unavailable** — G&B OAuth token expired 4/22 (3 days), draft-status suppressed per `feedback_superhuman_down_suppress_drafts`. Kay must manually re-auth to restore draft visibility. **Re-flagging as carry-forward open loop.**

Known pending draft work from session decisions:
- **[[entities/filippe-chagas|Filippe Chagas]] (Standard Pest Control) reply** — blocked on re-auth, original draft existed on Kay's personal Superhuman account pre-4/22.
- **3 XPX business-card follow-ups** — deferred from 4/23; Kay to paste card details, I'll draft 3 in parallel (Axial BD manager as warmest entry point).
- **Megan → Greg Geronimus intro** — 4/23 decision was REJECT (Megan already knows Greg), so this is now **closed** — suppress from any further surfacing.

## 4. Introductions Detected

None new in the 48h window.

Ongoing / prior intros still in flight:
- [[entities/bettina-huang|Bettina Huang]] → [[entities/denning-rodriguez|Denning Rodriguez]] (BI Law Firm) — thread originated 2026-02-07, 9 messages total, Kay most recently replied 4/22 ("Hi"). Active nurture, not a new intro event. **Routes to relationship-manager** for cadence tracking only.

## 5. Niche Signals

- **Insurance (Specialty Insurance — G&B top-ranked niche per 4/21):**
  - David Gritz InsurTech NY newsletter 4/23 — "Knowing the Heart of the Problem." Direct-market color for MGA/brokerage thesis. File for skim.
  - NAIFA-NY April 2026 newsletter 4/22 — trade association content. Member-list source for future JJ call lists if/when Kay decides to expand Specialty Insurance pipeline to brokerages. Hold as inventory.
  - [[entities/scott-etish|Scott Etish]] / Coventry article on life-insurance fiduciary considerations 4/23 — life-settlements market, adjacent to but not inside G&B's Specialty Insurance buy-box. Context only.
- **Art Infrastructure (currently Active-Outreach with Art Storage reactivated per 4/19 Saltoun greenlight):**
  - Frieze NY 2026 VIP invite 4/22 12:10 + "Behind the Scenes" 4/23 12:40 — Frieze is 5/7-5/11 NYC. **Decision point**: does Kay want to attend any day for art-infrastructure reconnaissance? Low-cost industry immersion, aligns with Art Storage reactivation. **Routes to pipeline-manager Decisions bucket** (CMO/CIO).
  - Amanda Lo Iacono "Women Shaping the Art World" 5/12 at Will Cotton Studio — **already RSVP'd yes by Kay 4/22, confirmed by Amanda 4/23**. Closed loop, suppress.
- **SMB Lending (adjacent advisor layer):**
  - [[entities/jim-vigna|Jim Vigna]] / [[entities/live-oak-bank|Live Oak Bank]] — SBA / small-business-lending specialist. Live Oak is **the** dominant SBA lender for search-fund / self-funded-searcher deals. This is a river-guide-adjacent contact worth nurturing independent of any specific niche. Already flagged in §2.

## 6. In-Person Meetings Today (Granola reminder)

Calendar scan 2026-04-24:
- **12:00-1:00 PM ET — AI Friday: Building an AI-Powered Outbound Engine That Converts** — virtual webinar, no counterparty to meet. No Granola needed.
- **1:00-2:00 PM ET — `HOLD mtg w/ Mark`** — HOLD prefix + 0 non-Kay attendees = **UNCONFIRMED** per `feedback_hold_calendar_prefix` + CLAUDE.md Brief-Decisions pre-flight Step 1. **Skip brief generation**; do not surface in Decisions bucket unless Kay wants a soft-nudge decision. Mark Gardella has not converted the Kay-proposed Friday 1pm into an accepted calendar invite since her 4/22 reply.
- **No other external in-person meetings today.**

## 7. Carry-Forward Open Loops (informational)

From [[context/session-decisions-2026-04-23]] — items email-intelligence surfaced or touched, still unresolved, **not** re-decisions but flagged so pipeline-manager knows they're live:
- **4/23 Granola vault writes still blocked** — `2026-04-23-xpx-panel.md` and `2026-04-23-kristin-wihera.md` not yet written. Blocked on entity stubs ([[entities/kristin-wihera|Kristin Wihera]], [[entities/axial]], [[entities/wiggin-and-dana]], [[entities/saunders-street-capital]]). Kristin call has G&B-strategy implications (email decay, solo-search risk, 35% IRR mismatch, investors-not-therapists doctrine) that Kay and I deferred discussing.
- **Axial buyer registration form** — Kay to fill `https://www.axial.net/request-information?utm_campaign=navbar-join` when she has 5 min.
- **River-guide-builder skill upgrade** — 4 sessions deferred, escalating concern. Highest-priority next-session agenda item.
- **Superhuman re-auth** — blocks Filippe + future drafts; 3 days running.
- **Sarah de Blasio Goodwin finder's-fee doc** — Kay-owned, blocks her outreach.
- **Jeff Stevens 4/30 deal-surface commitment** — 6 days remaining; 4/23 decision was REJECT on creating a Motion task (it's a goal, not a task). Carry as context only.

---

**Validation:**
- ✓ All 6 required sections present (plus optional §7 carry-forward)
- ✓ Deal flow counts: DIRECT-deal 0, DIRECT-relationship 2, DIRECT-internal 1, BLAST 6, NEWSLETTER ~9, OPERATIONAL 2 = ~20 (reconciles with ~24 threads seen)
- ✓ No CIM / NDA / LOI detected → no fast-path execution required → no Attio write needed
- ✓ No new intros → no entity creation required
- ✓ Session-decisions cross-check complete (4/22, 4/23, 4/24-bookend)
- ✓ Granola idempotency: 4/23 transcripts captured but blocked on vault write (pre-existing open loop, not regression)

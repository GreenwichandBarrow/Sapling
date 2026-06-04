---
date: 2026-06-04
type: context
title: "Email Scan Results — 2026-06-04"
schema_version: 1.1.0
tags:
  - date/2026-06-04
  - context
  - topic/email-scan
  - status/done
---

# Email Scan Results — 2026-06-04

Scan window: newer_than:2d. Run time: 2026-06-04 07:xx ET (headless). Granola ingested: 0 new notes (1 already in brain/calls/). No bookkeeper P&L detected. No CIM detected. No Active Deal fast-path triggered (NDA was outbound from Kay, not inbound). No bookkeeper management report from anthony.b@startvirtual.com.

---

## 1. Actionable Items Created

| item | urgency | source_ref | entity |
|------|---------|------------|--------|
| Create Attio entry — E&K Metal Manufacturing deal at NDA Signed stage | high | thread:19e28b9600f7365b | [[entities/everingham-kerr]] |

**File created:** `brain/inbox/2026-06-04-ek-metal-manufacturing-nda-attio.md`

**Context:** Kay signed and sent back the E&K NDA for the Precision Machining/Metal Manufacturing deal (Mid Atlantic) on June 3. Email to admin1@everkerr.com: "If this is still available, I'm interested in exploring the opportunity. NDA Signed & Attached." Attio entry at "NDA Signed" stage needs to be created — pipeline-manager should action on next run.

**Outbound actions noted (no inbox items required):**
- Kay cancelled VA service at StartVirtual (Jun 2, to Justine). 30-day notice period applies per Justine's reply. Kay is keeping bookkeeping services only. JJ is aware he finishes end of notice period. Call with Abigail (StartVirtual) on Jun 3 re: JJ transition — call note already in vault (`brain/calls/2026-06-03-abigail-startvirtual-jj-transition.md`).
- Kay sent "Great meeting you" follow-up (thread 19dcfe99a6a3a792) — outbound, no inbox item needed.
- Kay payment to Stone Street Software confirmed via BILL on Jun 3.
- PeekWire (adam@peekwireinc.info) media inquiry — asking to include G&B in "top 5 boutique luxury acquisition firms" article alongside Vendôme Global Partners and Dyens & Co. Article URL shared. No action required unless Kay wants to respond.

---

## 2. Deal Flow Classified

| classification | count | notes |
|----------------|-------|-------|
| DIRECT | 6 | Harrison Wells (vendor), Carlos x2 (solicitation + old intro thread), Adam PeekWire (media), Sam Singh DealsX (invoice), Kay personal gmail self-note |
| BLAST | 4 | E&K Metal Manufacturing, E&K Children's Platform, E&K Machining Services, ACG NY Summer Conference invitation |
| NEWSLETTER | 6 | Cornell Alumni, Axios AM, XPX event reminder, Zoom webinar, SMBootcamp, CounterA |

**Total inbound emails scanned: ~16**

**Outbound sent (last 2 days, Kay): ~8 threads** including: Cancelling VA, forwarding 3 E&K BLASTs to Camilla, signing/sending Metal Manufacturing NDA, Harrison Wells invoice reply, Warren Chan (Anacapa), "Great meeting you" follow-up.

**Notable DIRECT items:**
- **Harrison Wells** (harrison@dododigital.ai) — Invoice for June + Codex transition check-in. Kay replied she's swamped but will run Codex transition overnight. Payment issue with Stripe — Harrison sent Mercury invoice link as alternative. No action item generated (Kay handling directly).
- **Sam Singh, DealsX** — June invoice. Payoneer payment request also from Saurabh Singh (same entity). Vendor billing, no deal signal.
- **Adam, PeekWire** (adam@peekwireinc.info) — Media inquiry, article inclusion request. Not a deal.

---

## 3. Draft Status

**Total drafts in queue: 11**

Draft IDs retrieved via `gog gmail draft list`:
- r6313621414716482441 (msg 19e31a778b04ee7c) — recent
- r442603803878436480 (msg 19e31a774cac4261) — recent
- r2253803435468898722 (msg 19e1c82ed0eda9dd) — moderate age
- r989550462937595579 (msg 19caf4d9fea643b1) — older (thread 19caf435aed1cf61)
- 7 additional drafts (msg IDs starting 19c81...) — these share a date cluster from late May/early June, likely stale

**Cross-check against session-decisions-2026-06-03.md:** No SENT/DRAFTED entries for recent draft message IDs. The two most recent drafts (19e31a77...) were not flagged in session decisions.

**Stale flag:** The 7 drafts with msg IDs 19c81c... are notably older. Without subject-line visibility (draft-read CLI not available), cannot confirm contents. Pipeline-manager should surface these for Kay's review if they remain unsent next run.

**No NDA/CIM auto-acknowledgment drafts created** (see Section 8).

---

## 4. Introductions Detected

**Carlos Medina (carlos@in3o.com) → Kay + Oswaldo Ponce (Poza Capital)**

Thread: "Introduction" (19e40a9e2638c28d, initiated May 19, 7 messages, most recent Jun 3).

Carlos from in3o.com introduced Kay to Oswaldo Ponce at Poza Capital Partners (op@pozacp.com) — entity [[entities/oswaldo-ponce]] already exists in vault. Thread has been active through June 3 (7 messages). No new entity stub needed. No inbox item created — already in system.

**Carlos Medina (carlos@in3o.com) — Anacapa solicitation (NOT an intro to Kay)**

Thread: "Intro Anacapa" (19e661bafc8d39e9, May 26, 5 messages through Jun 3).

Carlos is pitching his portfolio company (Renue Environmental, renueenvironmental.com) to Kay, asking her to facilitate an introduction to Anacapa because "they have an interest in amlongroup.com." This is an inbound solicitation (Carlos seeking access to Anacapa via Kay), NOT an introduction of a person to Kay. Intro-detection does NOT fire. Kay replied on May 26: "They are a search fund investor... I will circle back." No action pending.

**No new entity stubs created** (both contacts already in system or not qualifying intros).

---

## 5. Niche Signals

- **Manufacturing / Precision Machining deal flow:** Three E&K BLAST listings in 2 weeks (Metal Manufacturing May 14, Machining Services Jun 2, plus Children's Platform May 18). Suggests E&K is an active channel for manufacturing-sector deal flow. Metal Manufacturing (Precision Machining/Stamping/Tool&Die) is an industrial niche — consistent with aerospace-defense adjacency discussed in session-decisions-2026-06-03.
- **Aerospace-Defense deal track live:** Kay has coffee meeting with Matt Luczyk / Peapack advisor scheduled for week of Jun 8 (per session-decisions Jun 3). Metal Manufacturing deal from E&K may offer a parallel data point on mid-Atlantic industrial multiples. No scorecard action — niche signal only.
- **PeekWire brand positioning:** G&B was listed alongside Vendôme Global Partners and Dyens & Co. as "boutique luxury acquisition firms" by PeekWire (peekwire.com). Kay has not responded. This is a passive branding observation — potentially useful as a credibility signal if vetted.
- **ACG NY Summer Dealmaking Conference — Hamptons, July 28-30:** Danielle Sheptin (dsheptin@acg.org) invitation. Per `feedback_no_conferences_in_morning_briefing`, this routes to Conference Pipeline tracker, NOT morning Decisions briefing. For pipeline-manager to triage on Monday conference review.
- **XPX Long Island — June 5 (tomorrow):** Kay is a member; event reminder received for "Wrapping up the 2026 Case Study – How did it end up?" No RSVP action apparent from email scan. Low urgency.
- **StartVirtual / JJ separation:** VA services cancelled, bookkeeping continues. Kay mentioned on the Abi call wanting to give JJ cold calling work during 30-day wind-down. JJ is aware of the timeline.

---

## 6. In-Person Meetings Today

| time | event | contact | location |
|------|-------|---------|----------|
| 12:00–13:00 EDT | Lunch | James Emden (jemden@helmsleyspear.com), Helmsley Spear | In-person |

**Source:** Gmail thread 19e7e23e77fbc2d4 ("Re: Updated invitation: Lunch James I Kay @ Thu Jun 4, 2026 12pm - 1pm (EDT)") — James Emden confirmed via updated calendar invite.

**Granola note:** No Granola note yet for this meeting (it's in the future). If meeting is recorded, a note will appear in tomorrow's scan.

**Already-ingested Granola meetings:** "Abi I Kay" (Jun 3, 5pm — VA cancellation call with Abigail/StartVirtual) is already in `brain/calls/2026-06-03-abigail-startvirtual-jj-transition.md`. "Harrison <> Kay: AI Coaching" (Jun 1) is already in `brain/calls/2026-06-01-harrison-wells-ai-coaching.md`. Both skipped (idempotent).

---

## 7. Broker BLAST Listings (per-deal extraction)

Three E&K BLAST emails in the scan window. Each is a single-listing BLAST. Trigger: BLAST classification + broker-signal keywords ("new acquisition opportunity", "retained to arrange the sale").

| source | headline | geo | revenue | ebitda | margin | industry | flag_reason | gmail_msg_id | listing_ordinal |
|--------|----------|-----|---------|--------|--------|----------|-------------|--------------|-----------------|
| Everingham & Kerr, Inc. (admin1@everkerr.com) | Provider of Metal Manufacturing; Precision Machining, Stamping & Tool & Die | Mid Atlantic (undisclosed) | undisclosed (behind NDA) | undisclosed | undisclosed | Metal Manufacturing / Precision Machining | single-listing-blast | 19e28b9600f7365b | 1 |
| Everingham & Kerr, Inc. (admin1@everkerr.com) | IP-Led Children's Sport and Education Platform | UK (virtual/digital) | undisclosed | undisclosed | undisclosed | Children's Educational Platform / IP licensing | single-listing-blast | 19e3cfa63b87ec38 | 1 |
| Everingham & Kerr, Inc. (admin1@everkerr.com) | Machining Services, Engineering & Waterjet Cutting Company | Southeastern US (undisclosed) | ~$2.3M (partial) | undisclosed | undisclosed | Machining / Engineering Services | single-listing-blast | 19e8a094b1a214f4 | 1 |

**Buy-box notes:**
- Metal Manufacturing (listing 1): Kay SIGNED NDA on Jun 3 — active pursuit. Mid Atlantic. Inbox item created for Attio entry.
- Children's Platform (listing 2): UK-based + virtual/digital + children's platform = multiple hard-excludes (US TAM only, B2C). Forwarded to Camilla for analyst awareness only.
- Machining Services (listing 3): Southeastern US, $2.3M revenue. Revenue is below the $5M floor in buy-box. Forwarded to Camilla for analyst awareness only.

---

## 8. Auto-Drafts Created

None.

No inbound emails this scan triggered the `<auto_ack_drafts>` criteria. The E&K BLASTs did not contain NDA/CIM attachments — they contained download links. Kay proactively downloaded, signed, and returned the NDA for the Metal Manufacturing deal via her own reply (outbound action, not a triggered inbound).

---
date: 2026-05-29
type: context
title: "Session Decisions — 2026-05-29 (Fri, E&K buy-side declined + intel-probe deferred, weekly-tracker, morning briefing dropped; + Attio relationship logging / Superhuman cleanup / PA owner pitch)"
tags:
  - date/2026-05-29
  - context
  - topic/session-decisions
  - topic/buy-side-advisor
  - topic/intermediary
  - topic/morning-briefing
  - topic/pipeline
  - topic/attio
  - topic/owner-outreach
  - topic/superhuman
  - topic/conference
  - person/joe-vanore
  - person/leigh-fryxell
  - person/amanda-forrestall
  - person/paul-giannamore
  - company/ever-kerr
  - company/pest-end
  - company/the-potomac-company
  - status/active
---

# Session Decisions — 2026-05-29 (Friday)

> Captured 2026-05-31 — the 5/29 session ended on a dropped SSH connection ("Connection reset by peer") before the evening bookend ran. Reconstructed from the session transcript.

## Decisions

### E&K / Joe Vanore buy-side engagement
- **REJECT (as structured):** [[entities/joe-vanore|Joe Vanore]] of [[entities/ever-kerr|E&K]] proposed a $3K/mo retainer ($9K upfront for the first 3-month term) + success fee (lesser of $100K+3% of total consideration or 10%, $50K floor; monthly payments credit toward the success fee). Retainer violates G&B's success-fee-only doctrine for buy-side advisors ([[../../memory/feedback_buyside_advisor_success_fee_only]]).
- **CFO verdict:** Affordable but TIGHT. Cash $190K (~$150K after $40K DD reserve), net burn ~$21K/mo → 7.1mo runway, already ~2mo short of the Feb-2027 deadline. $3K/mo eats 69% of the $4,325/mo savings target. Success fee can shave ~3–5 IRR pts on sub-$5M deals.
- **Strategic fit:** Weak. E&K's proven flow is landscaping/turf + B2C (restaurants, spas), off-thesis. 12-month scan of 347 E&K emails = **zero pest-control listings** (the niche G&B is building toward). His "we'd have a lot of success here" claim is unsupported by his own deal flow.
- **DEFER final call:** Kay chose to probe E&K's pest track record + multiples before a clean decline/counter (see Deferred + [[traces/2026-05-29-buyside-advisor-intel-probe]]).

### Friday weekly-tracker
- **APPROVE / run:** weekly-tracker executed (Friday cadence, needed by 10am ET). Sheet + vault snapshot written, validator passed, Slack notified (200).

### Morning briefing (5 Decisions presented — no responses captured)
- 5-item Decisions briefing delivered (investor report draft, Project Drone CIM red-flag list, 19 staged call-tasks, Sam Curcio thank-you + Heels-to-Deals discard, RED stale-insurance batch-close). Session dropped before Kay replied → all carried to Open Loops.

## Actions Taken
- **CREATED:** weekly-tracker Google Sheet + vault snapshot (week-ending metrics: NDAs 0 · Financials 1 [Project Drone, trending quasi-decline] · LOIs 0 · email response 33% (3/9) · JJ dials 157 · **owner conversations 0 for 2nd consecutive week**).
- **DRAFTED:** Reply to [[entities/joe-vanore|Joe Vanore]] probing recent pest transactions + multiples in the $1–3M EBITDA band, framed around "what the engagement could look like." **Chat only — NOT placed in Gmail** (per Kay's instruction). Kay to send in-thread.
- **CREATED:** Entity stubs [[entities/joe-vanore]] and [[entities/ever-kerr]]; trace [[traces/2026-05-29-buyside-advisor-intel-probe]].

## Deferred
- **E&K engage/decline** → trigger: Joe Vanore's reply to the pest track-record + multiples probe. If he names recent pest closings with credible multiples → continue on success-fee-only terms; if vague or pivots back to landscaping → clean pass. Intel useful to the pest thesis regardless of outcome.

## Open Loops
- **5 morning-briefing Decisions unanswered** (session dropped): (1) draft Q1-close investor report for Guillermo + the 12; (2) Project Drone CIM red-flag list → quasi-decline; (3) approve 19 staged call-tasks with day assignments (StartVirtual cancellation + investor-report/Drone tasks excepted); (4) Sam Curcio thank-you Mon AM + discard 13-day Heels-to-Deals follow-ups; (5) batch-close 9 RED stale insurance entries + orphan-link backfill (RED 3rd straight week). → re-surface in next briefing.
- **7 calibration proposals** from earlier this week still parked awaiting Kay's go.
- **Data quality:** Attio `meaningful_conversation` checkbox unpopulated across all 152 entries — owner-conversation metric fell back to call-notes. Non-urgent cleanup.
- **Owner conversations = 0** for 2nd consecutive week (all external meetings intermediary/investor). Expected during JJ wind-down + pest-cohort pivot, but the metric to watch before the 6/30 pest verdict.

---

# Session 2 — Attio relationship logging + Superhuman cleanup + PA owner pitch

> Captured 2026-05-31 — a second 2026-05-29 session segment (the Attio CRM-logging work) was never bookended; its SSH connection also reset. Reconstructed from the session transcript. Distinct from the E&K session above.

## Decisions

### Owner-outreach financing line — accuracy correction
- **REJECT "committed capital" framing → APPROVE "investors behind me / bespoke structure":** On the direct-to-owner PA pest pitch (Rejigg marketplace), Kay corrected the financing line. "Committed capital in place" overclaims — the accurate reality is investors hold a first right of refusal, not pre-committed capital. Final line leads with flexibility: "investors behind me who give me the flexibility to build a bespoke structure around what matters most to you, whether that's price, timing, your team, or how involved you stay after a sale." See [[traces/2026-05-29-owner-outreach-bespoke-structure-financing]] and [[../../memory/feedback_owner_outreach_bespoke_structure_financing]].

### Paul Giannamore DM framing — advisor, not seller
- **APPROVE search-fund/lead-investor framing:** Kay's LinkedIn DM to [[entities/paul-giannamore|Paul Giannamore]] ([[entities/the-potomac-company|The Potomac Company]]) used explicit "search fund / lead investor based in PR" language. Appropriate because Paul is an industry **M&A advisor, not a seller** — distinct from owner-outreach forbiddens. Kay authored the DM; Claude logged it.

### Superhuman teardown
- **APPROVE delete 21 [Superhuman]/* Gmail labels:** Subscription cancelled. Deleted all 21 Superhuman-applied labels (0 failures); the deliberately-built `auto/*` Gmail filters + labels were left untouched. Confirmed via AskUserQuestion (scope = Superhuman labels only).

## Actions Taken
- **CREATED (Attio):** Person [[entities/leigh-fryxell|Leigh Fryxell]] — LinkedIn DM note (5/29), LinkedIn URL, linked to [[entities/pest-end|Pest-End]]. No verified email yet.
- **CREATED (Attio):** Person [[entities/amanda-forrestall|Amanda Forrestall]] — NY-firm-intro note (tied to Leigh thread), LinkedIn URL, linked to [[entities/pest-end|Pest-End]]. No verified email yet.
- **CREATED (Attio):** Company [[entities/pest-end|Pest-End]] (Leigh + Amanda's firm).
- **CREATED (Attio):** Person [[entities/paul-giannamore|Paul Giannamore]] + Company [[entities/the-potomac-company|The Potomac Company]] (potomaccompany.com) — LinkedIn DM note (5/29, referral from Jason Palamatary), LinkedIn URL. Kept separate from the pre-existing "Potomac View Partner(s)" record. No verified email yet.
- **CREATED (Attio):** Company "Pest Management Business — Rejigg #38863 (PA)" + note logging the **buyer NDA signed on Rejigg (2026-05-29)**, PA pest context, the drafted owner pitch, and source channel (Rejigg direct-to-owner, no intermediary). Named by Rejigg conversation ID since the owner/company is still redacted on-platform.
- **DELETED:** 21 [Superhuman]/* Gmail labels (0 failures, 0 remaining); `auto/*` filters/labels untouched.
- **DRAFTED:** Direct-to-owner PA pest-control pitch (Rejigg) — owner-outreach-safe (no "fund," no financials, "I"-centric, community-connectivity hook, bespoke-structure financing line). Kay refined; send-ready. Chat-only.
- **CREATED (vault):** Entity stubs for the 5 new records above; trace [[traces/2026-05-29-owner-outreach-bespoke-structure-financing]]; memory [[../../memory/feedback_owner_outreach_bespoke_structure_financing]].

## Deferred
- **Axial project optimization** → Arturo Alvarado's 5/18 email (3 best-practice video links + Success Fee Primer attachment) to be mined from Gmail msg `19e3cfec8ee9f6b5` and applied to Kay's Axial project profile for better lead targeting. Kay interrupted before completion. Trigger: next time Axial profile work surfaces.
- **Apollo email enrichment** for Leigh Fryxell, Amanda Forrestall, Paul Giannamore (all lack verified emails) → trigger: when any replies via email or before a scheduled call.
- **Jason Palamatary (referrer)** not in Attio → create + link as Paul's intro source once firm/email known.

## Open Loops
- **Superhuman Google access not yet revoked** — cancelling the subscription does NOT stop server-side labeling; only revoking access at https://myaccount.google.com/permissions does. **Kay action required** (browser click, cannot be done via API). Until revoked, labels could technically re-apply.
- **Axial project optimization** unfinished (see Deferred).
- **3 contacts unenriched** (Leigh / Amanda / Paul) — no verified emails.

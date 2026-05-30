---
date: 2026-05-30
type: context
title: "Email Scan Results — 2026-05-30 (Sat)"
schema_version: 1.1.0
tags:
  - date/2026-05-30
  - context
  - topic/email-scan-results
  - topic/broker-deal-flow
  - source/gmail
  - source/granola
  - company/everingham-kerr
  - company/transworld
  - person/samuel-curcio
  - person/becky-wuest-creavin
  - status/done
---

# Email Scan Results — 2026-05-30

Saturday run (weekend, lighter volume as expected). Inbound 41 threads, outbound 11 threads, 12 Gmail drafts, 2 Granola notes (both previously ingested). **No CIM, no NDA/CIM attachment, no Active-Deal fast-path match, no bookkeeper P&L email** this run — none of the critical auto-triggers fired. The two Anthony/`startvirtual.com` emails are an End-Of-Week status update and a "MAY 2026 RECAP — Client Connect" relationship note (no `Management Report` + month/year subject, no P&L/Balance-Sheet PDF attachment) → bookkeeper P&L chain did NOT fire. Primary deal-flow output is Section 7: two NEW Everingham & Kerr broker BLASTs decomposed into per-listing rows. The Transworld/Samuel Curcio 20-listing digest (msg `19e70c13b9b6fc60`, 5/28) was already extracted in the 2026-05-29 run and is suppressed here per gmail_msg_id idempotency.

## 1. Actionable Items Created

**None.** No new inbox items written this run.

- No CIM detected → no `urgency: critical` inbox item, no deal-evaluation invocation.
- No bookkeeper/`startvirtual.com` P&L email with a Management Report attachment → bookkeeper P&L chain did not fire. No inbox trigger, no `budget-manager monthly` invocation. Nothing to log for `BOOKKEEPER-PL-CHAIN`.
- Becky Wuest Creavin "Virtual introduction" (Becky → [[entities/sam-transworld|Samuel Curcio]]) — both entities already exist ([[entities/becky-wuest-creavin]], [[entities/sam-transworld]], [[entities/peapack-private]], [[entities/transworld]]); the [[entities/sam-transworld|Sam Curcio]] thank-you was chat-DRAFTED 2026-05-28 (session-decisions). No new entity/inbox item required.
- Franchise intro ([[entities/greg-pitkoff|Greg Pitkoff]] fwd of [[entities/marsha-weiner|Marsha Weiner]], `mweiner@thecorpcoach.com`) is **already in flight from 2026-05-28** and re-confirmed on the 5/29 run. The forwarded note introduces Kay herself to a franchise contact (referral OF Kay), not a new contact TO Kay. Not re-created. Kay handles personally per session-decisions 5/28.

## 2. Deal Flow Classified

| Class | Count | Notes |
|-------|-------|-------|
| DIRECT | 8 | [[entities/becky-wuest-creavin\|Becky Wuest Creavin]] (Peapack — virtual intro to Sam Curcio), Warren Chan/Anacapa (art-world fit Q + Jun 9 call ask, investor), Amanda Lo Iacono/WIAC (Women in Art & Culture thank-you + future-event opt-in), [[entities/greg-pitkoff\|Greg Pitkoff]] (franchise fwd — tracked), Katie Walker/Plexus Capital (Checking In), James Emden/Helmsley Spear (RE: Meeting You Yesterday — 14-msg thread), Eric Mendelsohn/Archveo (XPX follow-up + Jun 1 11am invite), Barrie Green (internal — calendar-conflict heads-up) |
| BLAST | 2 | Everingham & Kerr — Southern NJ Residential Landscaping (5/30 resend, NEW msg id, 1 listing), Everingham & Kerr — Provider of Security Solutions HK/Macau (5/29, 1 listing) → both extracted to Section 7 |
| NEWSLETTER | 31 | Axios AM, PE Hub Deals Wire, Michael Girdley, Roger Ledbetter/Plug, Grant Hensel/This Week in ETA, Peter Lang/Digital Agency, Brian Moran/12 Week Year, XPX ×2, PestWorld 2026, Beacon AI Friday ×3, Warren Chan recap (Beacon), Paul Giannamore LinkedIn digest, Attio changelog, 1Password, Tailscale, Team Tailscale, Howie.ai, UOVO, CorpNet DE-LLC-tax, Claude Team, plus notifications/receipts (2× DMARC Google, DMARC Microsoft, 2× Google Voice SMS) |

**Total: 41 inbound threads.** No DIRECT email carried a new deal requiring CIM/fast-path processing. The Transworld/Samuel Curcio digest (msg `19e70c13b9b6fc60`) reappears in the 2-day window but was classified + extracted on 5/29; not re-counted here.

## 3. Draft Status

12 Gmail drafts pending. Cross-checked against session-decisions-2026-05-28 (no 5/29 file).

| Draft | To | Subject | Age | Status |
|-------|-----|---------|-----|--------|
| Aerospace Defense | Jeff Stevens | Aerospace Defense | ~1.5d (5/29 00:03) | Within 48h window — not stale |
| (2 recent thread drafts) | — | (~5/27 thread drafts) | ~3d | Aged slightly >48h — low priority |
| Heels to Deals f/u | mchawla@norris-law.com | Great meeting you at Heels to Deals | 14d | **Aged >48h** |
| Heels to Deals f/u | dchichester@schulmanlobel.com | Great meeting you at Heels to Deals | 14d | **Aged >48h** |
| Thank you | — | Thank you | 2026-02-21 | Long-standing persistent draft |
| Reply to Introduction | — | Reply to Introduction (no times) | 2026-02-21 | Long-standing persistent draft |
| Introduction to Broker | — | Introduction to Broker | 2026-02-21 | Long-standing persistent draft |

Notes for pipeline-manager:
- **Sam Curcio thank-you is NOT a Gmail draft** — it was DRAFTED in chat on 5/28 per `feedback_chat_drafts_dont_land_in_gmail`, still awaiting Kay's send approval. Do NOT surface as a stale Gmail draft.
- The two **Heels to Deals follow-up drafts (now 14 days old)** remain unsent — surface for Kay decision (send / discard).
- The three 2026-02-21 drafts are long-standing persistent drafts (not newly stale).

## 4. Introductions Detected

**1 confirmed warm introduction — already known, no new entity/inbox item.**

- **Becky Wuest Creavin ([[entities/peapack-private|Peapack Private]]) → [[entities/sam-transworld|Samuel Curcio]] (Transworld).** "Virtual introduction" email (msg `19e3c48aad15ba85`) connecting Kay with Sam Curcio. Both entities + the relationship already exist in the vault; the Sam Curcio thank-you was chat-drafted 2026-05-28. No new stub or inbox item required. Routed to relationship-manager / Kay (handles replies).

No other new intros. The Greg Pitkoff / Marsha Weiner franchise-forward routes Kay herself as a referral (not a new inbound contact) and is already tracked.

## 5. Niche Signals

- **Art world (load-bearing — women-led throughline):** THREE surfaces this scan — Warren Chan/Anacapa asking Kay's perspective on "services to the art world and their fit with the search fund model" + Amanda Lo Iacono / WIAC (Women in Art & Culture) gathering thank-you + UOVO art-storage marketing. Aligns with `user_kay_women_led_purpose_throughline` (fashion→art→women-led). Surface to Kay for the art-world thesis question Warren raised (he wants a Jun 9 call, 8am-5pm PT).
- **Pest (active):** Kay's outbound "Reconnect - Pest" + "Pest Management" threads (5/29) still in motion; PestWorld 2026 keynote inbound. Pest 10-co June experiment is the standing wind-down verdict trigger (6/30).
- **Aerospace Defense:** Aerospace Defense draft to Jeff Stevens (5/29) references a Guillermo-prompted lead; niche in-scope (aerospace defense NOT excluded per `feedback_no_aviation_targets`).
- **Broker deal-flow geography:** E&K Southern NJ landscaping = within PA/CT/LI/NYC/NJ footprint. E&K Security Solutions = **Hong Kong & Macau (non-US — hard exclude per `feedback_us_tam_not_global`)**; extracted to Section 7 for KPI completeness but out of box.

## 6. In-Person Meetings Today

**None.** Saturday 5/30 — no external meetings on calendar. Eric Mendelsohn / Archveo invite is for **Mon Jun 1, 11:00-11:15am EDT** (virtual). Warren Chan proposes a call **on/after Tue Jun 9**. No in-person meeting today requiring a Granola reminder.

## 7. Broker BLAST Listings (per-deal extraction)

| source | headline | geo | revenue | ebitda | margin | industry | flag_reason | gmail_msg_id | listing_ordinal |
|--------|----------|-----|---------|--------|--------|----------|-------------|--------------|-----------------|
| Everingham & Kerr, Inc. | Southern NJ Residential Landscaping Company (5/30 resend) | Southern NJ | $1M | ~$300K normalized cash flow | ~30% (cash flow) | Residential landscaping | single-listing-blast | 19e7958e322d7bd2 | 1 |
| Everingham & Kerr, Inc. | Provider of Security Solutions (cargo x-ray, explosives detection, radio accessories) | Hong Kong & Macau (NON-US — hard exclude) | $7.1M | $1.5M normalized EBITDA | ~21% | Security solutions distribution / installation (B2B/B2G) | single-listing-blast | 19e75601f80f7c17 | 1 |

**2 listings extracted today.** The Transworld/Samuel Curcio 20-listing digest (msg `19e70c13b9b6fc60`, 5/28) was already decomposed into 20 per-listing rows in `email-scan-results-2026-05-29.md` and is **suppressed here per gmail_msg_id idempotency** — not re-extracted. Notes for pipeline-manager/CIO: extraction is decoupled from qualification. The E&K Southern NJ landscaping ($1M rev / ~$300K cash flow) is sub-box ($2-10M EBITDA) but the closest evaluable owner-operator profile; the E&K Security Solutions deal hits the buy-box on size ($7.1M rev / $1.5M EBITDA) but is **Hong Kong & Macau — US-only TAM hard-exclude**. Neither warrants an Active Deal entry; routing left to pipeline-manager.

## 8. Auto-Drafts Created

**None.** No inbound email carried an NDA or CIM PDF **attachment** this run. Everingham & Kerr offered its confidentiality agreements as **download links** (`everkerr.com/.../Confidentiality-Agreement_*.pdf`), not attached files — the `<auto_ack_drafts>` trigger requires an attached PDF, so no auto-acknowledgment draft was created. Per `feedback_kay_handles_all_replies`, drafts are CREATED only, never sent; none applicable today.

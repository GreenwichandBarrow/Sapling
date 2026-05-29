---
date: 2026-05-29
type: context
title: "Email Scan Results — 2026-05-29 (Fri)"
schema_version: 1.1.0
tags:
  - date/2026-05-29
  - context
  - topic/email-scan-results
  - topic/broker-deal-flow
  - source/gmail
  - source/granola
  - company/everingham-kerr
  - company/transworld
  - person/samuel-curcio
  - status/done
---

# Email Scan Results — 2026-05-29

Headless weekday run (7am ET). Inbound 25 threads, outbound 13 threads, 13 Gmail drafts, 6 Granola notes (all previously ingested). **No CIM, no NDA/CIM attachment, no Active-Deal fast-path match, no bookkeeper P&L email** this run — none of the critical auto-triggers fired. Primary deal-flow output is Section 7: two broker BLASTs decomposed into 21 per-listing rows.

## 1. Actionable Items Created

**None.** No new inbox items written this run.

- No CIM detected → no `urgency: critical` inbox item.
- No bookkeeper/`startvirtual.com` P&L email detected → bookkeeper P&L chain did not fire (no inbox trigger, no `budget-manager monthly` invocation). Nothing to log for `BOOKKEEPER-PL-CHAIN`.
- Franchise intro (Greg Pitkoff fwd → Marsha Weiner, `mweiner@thecorpcoach.com`) is **already in flight from 2026-05-28** (session-decisions 5/28 tagged `person/greg-pitkoff` + `person/marsha-weiner`; Kay's "Franchise" reply thread active). Not re-created.

## 2. Deal Flow Classified

| Class | Count | Notes |
|-------|-------|-------|
| DIRECT | 5 | Harrison Wells (team/Claude update), Greg Pitkoff (franchise fwd — tracked), Carlos Nieto/DCA (Project Drone pitch — existing thread, prior REJECT), August Felker/Oberle (insurance DD advisor — existing 23-msg thread), Danielle Sheptin/ACG (Women of Leadership golf clinic invite) |
| BLAST | 2 | Everingham & Kerr (landscaping, 1 listing), Transworld/Samuel Curcio (20 listings) → both extracted to Section 7 |
| NEWSLETTER | 18 | 12 newsletters/promos (XPX ×2, Claude Team, PestWorld keynote, Beacon AI Friday, NPMA Women's Forum, CorpNet DE-LLC-tax, Frank Sondors/Salesforge, Mark Edler exit program, Women's Search Network June events, Squarespace) + 6 receipts/notifications (Google Voice SMS, Hetzner price adj, Uber receipt, Anthropic receipt, XPX payment receipt, XPX registration confirmed) |

**Total: 25 inbound threads.** No DIRECT email carried a new deal requiring CIM/fast-path processing.

## 3. Draft Status

13 Gmail drafts pending. Cross-checked against session-decisions-2026-05-28.

| Draft | To | Subject | Age | Status |
|-------|-----|---------|-----|--------|
| Aerospace Defense | (cold-outreach) | Aerospace Defense | 2026-05-29 | Fresh (today) — not stale |
| Harrison Wells reply | harrison@dododigital.ai | Re: Check in + claude update | 2026-05-29 | Fresh (today) |
| (2 drafts) | — | (recent ~5/27 thread drafts) | ~2d | Within window |
| Heels to Deals f/u | mchawla@norris-law.com | Great meeting you at Heels to Deals | 13d | **Aged >48h** |
| Heels to Deals f/u | dchichester@schulmanlobel.com | Great meeting you at Heels to Deals | 13d | **Aged >48h** |
| Thank you | — | Thank you | 2026-02-21 | Long-standing persistent draft |
| Reply to Introduction | — | Reply to Introduction (no times) | 2026-02-21 | Long-standing persistent draft |
| Introduction to Broker | — | Introduction to Broker | 2026-02-21 | Long-standing persistent draft |

Note for pipeline-manager: two **Heels to Deals follow-up drafts (5/16, 13 days old)** remain unsent — surface for Kay decision (send / discard). The three 2026-02-21 drafts are long-standing persistent drafts (not newly stale).

## 4. Introductions Detected

**None new.** The only intro-shaped item (Greg Pitkoff fwd "Franchse interest") routes to Marsha Weiner, already tracked from 2026-05-28. No new entity stub or inbox item required.

## 5. Niche Signals

- **Pest (active):** Kay sent two outbound today — "Reconnect - Pest" and "Pest Management" (5/29 08:00). PestWorld 2026 keynote + NPMA Women's Forum inbound. Pest niche outreach in motion.
- **Aerospace Defense:** fresh outbound draft today (niche not excluded per `feedback_no_aviation_targets` carve — aerospace defense is in-scope).
- **Women-led network (load-bearing per Kay's throughline):** Women's Search Network June events + ACG "Women of Leadership" golf clinic (June 2) + NPMA Women's Forum — three women-led network surfaces this scan.
- **Insurance:** August Felker / Oberle Risk insurance-DD-for-searchers thread active (advisor, not target).
- **Broker deal-flow geography:** Transworld listings cluster NY/CT/MA/PA; E&K = Southern NJ. Within PA/CT/LI/NYC/NJ conference geography footprint.

## 6. In-Person Meetings Today

**None.** Today's calendar (Fri 5/29): AI Friday (13:00, Streamyard — virtual) and Megan ↔ Kay (13:30, no location → Google Meet default, virtual). No in-person meeting requiring a Granola reminder.

## 7. Broker BLAST Listings (per-deal extraction)

| source | headline | geo | revenue | ebitda | margin | industry | flag_reason | gmail_msg_id | listing_ordinal |
|--------|----------|-----|---------|--------|--------|----------|-------------|--------------|-----------------|
| Everingham & Kerr, Inc. | Southern NJ Residential Landscaping Company | Southern NJ | $1M | ~$300K normalized cash flow | ~30% (cash flow) | Residential landscaping | single-listing-blast | 19e706ebf5e90642 | 1 |
| Samuel Curcio, Transworld | High-Growth Distribution Co. Operating Partner Needed | Suffolk County, NY | undisclosed | $1,446,050 SDE | undisclosed | Distribution | multi-listing | 19e70c13b9b6fc60 | 1 |
| Samuel Curcio, Transworld | Growing Multi-Location Restaurant Portfolio | Norfolk County, MA | ~$4M (2026 proj) | $459,435 SDE | undisclosed | Restaurant (B2C) | multi-listing | 19e70c13b9b6fc60 | 2 |
| Samuel Curcio, Transworld | Established Commercial Restroom Partitions Business | Suffolk County, NY | $2.3M sales | $-25,256 SDE | negative | Building products | multi-listing | 19e70c13b9b6fc60 | 3 |
| Samuel Curcio, Transworld | Established Eatery with Strong Local Following | Fairfield County, CT | undisclosed | $74,513 SDE | undisclosed | Restaurant (B2C) | multi-listing | 19e70c13b9b6fc60 | 4 |
| Samuel Curcio, Transworld | Absentee Run Recording Studio (20-yr, Brooklyn) | Kings County, NY | undisclosed | $134,988 SDE | undisclosed | Recording studio | multi-listing | 19e70c13b9b6fc60 | 5 |
| Samuel Curcio, Transworld | Established Legal Funding Firm Seeking Partner | New York | undisclosed | $1,473,572 SDE | undisclosed | Legal funding (lending — hard exclude) | multi-listing | 19e70c13b9b6fc60 | 6 |
| Samuel Curcio, Transworld | UNDER CONTRACT - High-End Midtown Med. Skincare Spa | New York County, NY | undisclosed | $0 SDE | undisclosed | Med spa (under contract) | multi-listing | 19e70c13b9b6fc60 | 7 |
| Samuel Curcio, Transworld | Gov Con & Corporate B2B Interiors Firm | New York | undisclosed | $389,464 SDE | undisclosed | Commercial interiors (B2B) | multi-listing | 19e70c13b9b6fc60 | 8 |
| Samuel Curcio, Transworld | Multilingual Translation & Language Services Business | Pennsylvania | undisclosed | $2,418 SDE | undisclosed | Translation services | multi-listing | 19e70c13b9b6fc60 | 9 |
| Samuel Curcio, Transworld | Authentic Asian Restaurant, Upper West Side | New York County, NY | undisclosed | $102,991 SDE | undisclosed | Restaurant (B2C) | multi-listing | 19e70c13b9b6fc60 | 10 |
| Samuel Curcio, Transworld | Profitable Home-Based Production & Animation | New York County, NY | undisclosed | $53,604 SDE | undisclosed | Production/animation | multi-listing | 19e70c13b9b6fc60 | 11 |
| Samuel Curcio, Transworld | Seafood Restaurant, A+ Suffolk Location | Suffolk County, NY | undisclosed | $264,976 SDE | undisclosed | Restaurant (B2C) | multi-listing | 19e70c13b9b6fc60 | 12 |
| Samuel Curcio, Transworld | Semi-Passive Multi-Territory Services Franchise (NY/CT) | NY/CT | undisclosed | $0 SDE | undisclosed | Services franchise | multi-listing | 19e70c13b9b6fc60 | 13 |
| Samuel Curcio, Transworld | Solo Electrical Practice (Net $150k, Turnkey) | Suffolk, NY | undisclosed | $125,985 SDE | undisclosed | Electrical contracting | multi-listing | 19e70c13b9b6fc60 | 14 |
| Samuel Curcio, Transworld | Boutique Nail Studio (Premium Build-Out) | New York County, NY | undisclosed | $0 SDE | undisclosed | Nail salon (B2C) | multi-listing | 19e70c13b9b6fc60 | 15 |
| Samuel Curcio, Transworld | High-Volume Queens Collision Center | Queens, NY | undisclosed | $809,063 SDE | undisclosed | Auto collision repair | multi-listing | 19e70c13b9b6fc60 | 16 |
| Samuel Curcio, Transworld | Established Sign & Graphics Franchise | Erie County, NY | undisclosed | $261,368 SDE | undisclosed | Sign & graphics franchise | multi-listing | 19e70c13b9b6fc60 | 17 |
| Samuel Curcio, Transworld | Profitable Industrial Cleaning Business | Rensselaer County, NY | undisclosed | $80,811 SDE | undisclosed | Industrial cleaning (B2B) | multi-listing | 19e70c13b9b6fc60 | 18 |
| Samuel Curcio, Transworld | Upscale Skincare & Aesthetics Spa | Saratoga County, NY | undisclosed | $231,013 SDE | undisclosed | Skincare/aesthetics spa | multi-listing | 19e70c13b9b6fc60 | 19 |
| Samuel Curcio, Transworld | Exquisite High-End Kitchen Cabinet Business | Richmond County, NY | undisclosed | $0 SDE | undisclosed | Kitchen cabinetry | multi-listing | 19e70c13b9b6fc60 | 20 |

**21 listings extracted.** Note for pipeline-manager/CIO: extraction is decoupled from qualification — these rows are the deal-flow KPI, not pre-screened targets. Most fall below G&B buy-box ($2-10M EBITDA) and several are pure-B2C (restaurants, spas, nail/salon) or hard-exclude (legal funding = lending). The E&K Southern NJ landscaping ($1M rev / ~$300K cash flow) is the closest to an evaluable owner-operator profile but sub-box. None warrant an Active Deal entry; routing left to pipeline-manager.

## 8. Auto-Drafts Created

**None.** No inbound email carried an NDA or CIM PDF **attachment** this run. Everingham & Kerr offered its confidentiality agreement as a **download link** (`everkerr.com/.../Confidentiality-Agreement_SNJRLC.pdf`), not an attached file — the `<auto_ack_drafts>` trigger requires an attached PDF, so no auto-acknowledgment draft was created. (Per `feedback_kay_handles_all_replies`, drafts are CREATED only, never sent; none applicable today.)

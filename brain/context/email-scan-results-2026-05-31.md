---
date: 2026-05-31
type: context
title: "Email Scan Results — 2026-05-31 (Sun)"
schema_version: 1.1.0
tags:
  - date/2026-05-31
  - context
  - topic/email-scan-results
  - topic/broker-deal-flow
  - source/gmail
  - source/granola
  - company/flippa
  - company/everingham-kerr
  - status/done
---

# Email Scan Results — 2026-05-31

Sunday run (weekend, lightest volume as expected). Inbound 36 threads in the 2-day window, outbound 8 threads, 12 Gmail drafts (unchanged from Saturday), 2 Granola notes (both already ingested — `not_RBVjFhMF2BBE7l` Megan 5/29 and `not_bE9HS6Eck0mGcK` Guillermo 5/28 only show 5/30 `updated_at` from a sync, no content change). **No CIM, no NDA/CIM attachment, no Active-Deal fast-path match, no bookkeeper P&L Management Report** this run — none of the critical auto-triggers fired. The two Anthony/`startvirtual.com` emails are an End-Of-Week status reply and a "MAY 2026 RECAP — Client Connect" relationship note (no `Management Report` + month/year subject, no P&L/Balance-Sheet attachment) → bookkeeper P&L chain did NOT fire. **NEW since Saturday's run: one Flippa marketplace deal-newsletter (msg `19e7a497b8b41bc4`, 5/30) decomposed into per-listing rows in Section 7.** Everything else new is finance/notification noise (Stone Street invoice, Gusto payroll auto-run notice, DMARC reports) or pure educational newsletter (Walker Deibel — no listings). The E&K Security Solutions BLAST (`19e75601f80f7c17`, 5/29) was already extracted in the 2026-05-30 run and is **suppressed here per gmail_msg_id idempotency**.

## 1. Actionable Items Created

**None.** No new inbox items written this run.

- No CIM detected → no `urgency: critical` inbox item, no deal-evaluation invocation.
- No bookkeeper/`startvirtual.com` P&L email with a Management Report attachment → bookkeeper P&L chain did not fire. No inbox trigger, no `budget-manager monthly` invocation. Nothing to log for `BOOKKEEPER-PL-CHAIN`.
- No new warm introduction. All DIRECT threads (Warren Chan, Eric Mendelsohn, Katie Walker, James Emden, Amanda Lo Iacono, Barrie Green) carried over from prior scans and are Kay-handled / already tracked.

## 2. Deal Flow Classified

| Class | Count | Notes |
|-------|-------|-------|
| DIRECT | 7 | Warren Chan/Anacapa (art-world fit Q + Jun 9 call ask), Katie Walker/Plexus (Checking In), James Emden/Helmsley Spear (14-msg thread), Eric Mendelsohn/Archveo (XPX follow-up + Mon Jun 1 11am invite), Amanda Lo Iacono/WIAC (12 May thank-you), Anthony/StartVirtual (EOW report reply), Barrie Green (internal calendar-conflict heads-up) — all carried from prior scans, none new since Saturday |
| BLAST | 1 | Everingham & Kerr — Security Solutions HK/Macau (`19e75601f80f7c17`, 5/29) → already extracted 5/30, suppressed per idempotency |
| NEWSLETTER | 28 | Includes 1 DEAL_NEWSLETTER (Flippa marketplace digest `19e7a497b8b41bc4`, 5/30 — extracted to Section 7). Others: Walker Deibel (educational, no listings), Axios AM, PE Hub Deals Wire, Michael Girdley, Grant Hensel/This Week in ETA, Peter Lang, Brian Moran/12 Week Year, XPX, UOVO, Beacon AI Friday ×2, Paul Giannamore LinkedIn digest, Attio changelog, 1Password, Team Tailscale, Howie.ai, plus notifications/receipts (Stone Street invoice, Gusto payroll auto-run notice, CorpNet DE-LLC-tax warning, 3× DMARC Google, 1× DMARC Microsoft, 1× Google Voice SMS) |

**Total: 36 inbound threads in window.** No DIRECT email carried a new deal requiring CIM/fast-path processing. **NEW deal-flow signal since Saturday = the single Flippa marketplace digest** (Section 7).

## 3. Draft Status

12 Gmail drafts pending — unchanged count from Saturday's run. Cross-checked against session-decisions-2026-05-28 (no 5/29 or 5/30 file).

| Draft | To | Subject | Age | Status |
|-------|-----|---------|-----|--------|
| Aerospace Defense | Jeff Stevens | Aerospace Defense | ~2.3d (5/29 00:03) | Aged slightly >48h — low priority |
| (recent thread drafts) | — | (~5/27 thread drafts) | ~4d | Aged >48h — low priority |
| Heels to Deals f/u | mchawla@norris-law.com | Great meeting you at Heels to Deals | 15d | **Aged >48h — surfaced 5/30, holds for Kay** |
| Heels to Deals f/u | dchichester@schulmanlobel.com | Great meeting you at Heels to Deals | 15d | **Aged >48h — surfaced 5/30, holds for Kay** |
| Thank you | — | Thank you | 2026-02-21 | Long-standing persistent draft |
| Reply to Introduction | — | Reply to Introduction | 2026-02-21 | Long-standing persistent draft |
| Introduction to Broker | — | Introduction to Broker | 2026-02-21 | Long-standing persistent draft |

Notes for pipeline-manager:
- **Sam Curcio thank-you is NOT a Gmail draft** — chat-drafted 5/28 per `feedback_chat_drafts_dont_land_in_gmail`, awaiting Kay's send approval. Do NOT surface as a stale Gmail draft.
- The two **Heels to Deals follow-up drafts (now 15 days old)** were already surfaced on the 5/30 run. No new draft activity since Saturday — do not re-flag as fresh; carry the existing send/discard decision.
- The three 2026-02-21 drafts are long-standing persistent drafts (not newly stale).

## 4. Introductions Detected

**None new.** The Becky Wuest Creavin → Samuel Curcio "Virtual introduction" (msg `19e3c48aad15ba85`) was detected and handled on prior runs (Sam Curcio thank-you chat-drafted 5/28; both entities exist). No new warm intro landed since Saturday.

## 5. Niche Signals

- **Art world (load-bearing — women-led throughline):** Warren Chan/Anacapa still awaiting Kay's perspective on "services to the art world and their fit with the search fund model" (Jun 9 call ask) + Amanda Lo Iacono / WIAC (Women in Art & Culture) thank-you. Aligns with `user_kay_women_led_purpose_throughline`. Carried from 5/30 — no change.
- **Fine jewelry / luxury (Flippa signal):** Flippa digest surfaced a $1.5M-rev moissanite/lab-grown engagement-ring Shopify store. Pure B2C e-commerce, online marketplace listing — out of G&B box (B2B/B2B2C-to-luxury only, pure B2C rejected per `feedback_b2b_b2b2c_ok_no_b2c`). Noted for completeness only.
- **Pest (active):** Kay's outbound "Reconnect - Pest" + "Pest Management" threads (5/29) still in motion. Pest 10-co June experiment = standing wind-down verdict trigger (6/30).
- **Aerospace Defense:** Aerospace Defense draft to Jeff Stevens still pending; niche in-scope (aerospace defense NOT excluded per `feedback_no_aviation_targets`).
- **ETA / M&A market commentary:** Walker Deibel "infrastructure over products" + Michael Girdley + Grant Hensel SBA rule — educational, no actionable niche signal.

## 6. In-Person Meetings Today

**None.** Sunday 5/31 — no external meetings on calendar. Eric Mendelsohn / Archveo invite is for **Mon Jun 1, 11:00-11:15am EDT** (virtual). Warren Chan proposes a call **on/after Tue Jun 9**. No in-person meeting today requiring a Granola reminder.

## 7. Broker BLAST Listings (per-deal extraction)

| source | headline | geo | revenue | ebitda | margin | industry | flag_reason | gmail_msg_id | listing_ordinal |
|--------|----------|-----|---------|--------|--------|----------|-------------|--------------|-----------------|
| Flippa Marketplace (Sebastien Stanley Jones, broker) | iGames Affiliate Site Portfolio (100+ WordPress iGaming/casino affiliate sites) | undisclosed (broker NL) | $3.1M | undisclosed | 98% profit margin | iGaming affiliate / online media | deal-newsletter-known-sender | 19e7a497b8b41bc4 | 1 |
| Flippa Marketplace | Fine Jewelry Shopify Store (moissanite / lab-grown engagement rings) | undisclosed | $1.5M | undisclosed | undisclosed ($545 AOV) | B2C e-commerce / fine jewelry | deal-newsletter-known-sender | 19e7a497b8b41bc4 | 2 |
| Flippa Marketplace | Home Decor PrestaShop Brand (wall stickers, photo murals, vinyl rugs, wallpaper) | undisclosed | $127K | undisclosed | 97% profit margin | B2C e-commerce / home decor | deal-newsletter-known-sender | 19e7a497b8b41bc4 | 3 |
| Flippa Marketplace | Dog Breeding Marketplace (breeder listings + display ads) | undisclosed | $15K | undisclosed | undisclosed | online marketplace / pet | deal-newsletter-known-sender | 19e7a497b8b41bc4 | 4 |
| Flippa Marketplace | AI Design Academy (architecture & design courses) — investment opportunity | undisclosed (global) | $475K TTM | $220K TTM profit | ~46% (profit/rev) | edtech / online courses | deal-newsletter-known-sender | 19e7a497b8b41bc4 | 5 |
| Flippa Marketplace | School Management SaaS Platform (digest) | undisclosed | $817K | undisclosed | 44% profit margin | B2B SaaS / edtech | deal-newsletter-known-sender | 19e7a497b8b41bc4 | 6 |
| Flippa Marketplace | AI Outreach SaaS (digest) | undisclosed | $72K | undisclosed | 72% profit margin | B2B SaaS | deal-newsletter-known-sender | 19e7a497b8b41bc4 | 7 |
| Flippa Marketplace | Home & Kitchen Shopify Store (digest) | undisclosed | $135K | undisclosed | undisclosed ($113 AOV) | B2C e-commerce | deal-newsletter-known-sender | 19e7a497b8b41bc4 | 8 |

**8 listings extracted from the Flippa marketplace digest** (4 featured + 4 secondary digest rows; the "Wellness Shopify Brand $5.2M" item is flagged "Just Sold" and excluded as not actively for-sale). The E&K Security Solutions BLAST (`19e75601f80f7c17`, 5/29) and the Transworld/Samuel Curcio 20-listing digest (`19e70c13b9b6fc60`, 5/28) were extracted on prior runs and are **suppressed here per gmail_msg_id idempotency**. Notes for pipeline-manager/CIO: extraction is decoupled from qualification. **Every Flippa listing here is out of the G&B box** — all are pure B2C e-commerce / online-marketplace / affiliate businesses, sub-scale ($15K–$3.1M rev, none at $2-10M EBITDA), and Flippa is a marketplace not a sell-side intermediary (`feedback_marketplace_vs_broker_distinction`). Extracted for KPI completeness only; none warrants an Active Deal entry. Routing left to pipeline-manager.

## 8. Auto-Drafts Created

**None.** No inbound email carried an NDA or CIM PDF **attachment** this run. No broker sent a confidentiality agreement or teaser as an attached file. The `<auto_ack_drafts>` trigger requires an attached PDF; none applicable today. Per `feedback_kay_handles_all_replies`, drafts are CREATED only, never sent.

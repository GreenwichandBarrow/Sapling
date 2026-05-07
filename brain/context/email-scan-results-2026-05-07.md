---
date: 2026-05-07
type: context
title: "Email Scan Results — 2026-05-07"
tags:
  - date/2026-05-07
  - context
  - topic/email-scan
  - topic/morning-briefing
  - topic/deal-flow
schema_version: 1.1.0
---

## Summary

- Inbox scanned (newer_than:2d, 50-thread cap): 22 threads visible.
- Outbound scanned (kay.s@greenwichandbarrow.com newer_than:2d): 7 threads (1 still in DRAFT state — already SENT per yesterday's session-decisions, see Draft Status).
- CIM auto-trigger fires: 0
- NDA auto-trigger fires (PDF attached): 0
- Active Deal Fast-Path fires: 0
- Bookkeeper P&L auto-fires: 0
- Broker BLAST per-listing rows: 1 (Everingham & Kerr)
- Auto-acknowledgment Gmail drafts created: 0
- Granola new transcripts: 0 (yesterday's 2 calls already captured to `brain/calls/`)

## 1. Actionable Items Created

| timestamp | source | item | inbox_file | urgency |
|---|---|---|---|---|
| 2026-05-06 08:26 | Eric Mendelsohn (Archveo Advisors) | Email-address change — `eric@archveoadvisors.com`. Update entity + Attio. | none (entity-update only — handled by relationship-manager) | normal |
| 2026-05-06 09:32 | Jackson Niketas (Terra Mar Search) | AI Coaching call — Jackson offered 6 windows Wed 5/6 → Wed 5/13. Kay needs to pick + reply. | surface in briefing 🟡 | normal |
| 2026-05-06 10:37 | Megan Benson (KeyBank) | KeyBank Women's Dinner Thu evening 5/14 after ACG NY WOL Summit. RSVP. | surface in briefing 🟡 | normal |
| 2026-05-05 11:49 | Payal Keshvani (Taft Law) | Taft Dinner same evening 5/14 after ACG WOL Summit. Conflicts with KeyBank dinner — pick one. | surface in briefing 🟡 (paired with KeyBank above) | normal |
| 2026-05-06 18:10 | GJ King (BK Growth) | Tomorrow's Zoom guests: Jay Davis + Caroline DiMatteo from Nashton. (Investor / G&B program.) | surface in briefing 🟢 (informational — already on calendar) | low |
| 2026-05-06 17:32 | Everingham & Kerr | Family Medical Practice BLAST (Southern NJ, $1.5M rev / $400K EBITDA). Out of buy-box (healthcare practice). | none — log to broker BLAST table only | low |

No `brain/inbox/` files written this run (all items routable by pipeline-manager + relationship-manager downstream).

## 2. Deal Flow Classified

| classification | count | notes |
|---|---|---|
| DIRECT (personalized to Kay) | 6 | Eric Mendelsohn, Jackson Niketas, Megan Benson, Payal Keshvani, GJ King thread, Andrew Lowis Axial invitation update |
| BLAST (broker / deal-flow) | 3 | Everingham & Kerr (single-listing), Tory @ Flippa (marketplace — not broker per `feedback_marketplace_vs_broker_distinction`), Kaitlinn @ Axial (Top Deals Q1 — platform digest, not broker) |
| NEWSLETTER | 7 | Mike Allen / Axios ×3, HBR, Attio promo, AXS promo, NAEPC conference reminder |
| OPS / SYSTEM | 6 | Hetzner verification code, Slack notification, Ria Bautista StartVirtual quality audit, Barrie Green calendar conflict alert, Yahoo travel reservation forward, Andrew Lowis calendar update |

## 3. Draft Status

Gmail draft list returned 9 drafts.

| draft_id | thread_subject | state | age | action |
|---|---|---|---|---|
| `r-7216983259268091776` | "Tomorrow's call — could we push to 10:30 ET?" (Andrew Lowis Axial reschedule) | **Already SENT 2026-05-06** per session-decisions; ghost draft persists in list | 2d | Suppress — do NOT flag stale |
| `r989550462937595579` | (legacy thread `19caf...`) | Stale | >60d | Already known-stale (carried forward across many runs) |
| `r-5013177138505427051` thru `r8922907573534439329` (7 entries) | All on `19c81...` thread family | Stale | >60d | Already known-stale (legacy from pre-2026 testing) |

**No new unsent drafts > 48 hours.** No fresh draft creation needed.

## 4. Introductions Detected

None this scan window.

- Andrew Lowis Axial coaching follow-up may produce an Arturo intro (per yesterday's session-decisions Open Loops); not yet present.
- GJ King "Tomorrow's Zoom Guests" is a meeting briefing, not an intro request.

## 5. Niche Signals

| signal | source | direction |
|---|---|---|
| Family medical practice (Southern NJ, $1.5M/$400K) — broker BLAST | Everingham & Kerr | NEUTRAL — out of buy-box (healthcare practice ≠ B2B services); volume signal only |
| Search-fund AI-tooling discussion offer | Jackson Niketas (Terra Mar) | NEUTRAL — Kay's experience requested, not deal flow |
| Axial Q1 2026 Top Deals digest | Kaitlinn / Axial | NEUTRAL — review later for buy-box matches if needed |
| KeyBank middle-market sponsor presence | Megan Benson | POSITIVE — KeyBank in lender-channel discussions per Guillermo lender list (project memory `project_guillermo_lender_list.md`) |

## 6. In-Person Meetings Today

**None.** Today's only external meeting is **James Emden / Helmsley Spear** at 10:00–10:30 ET — Google Meet (video, not in-person). Brief landed yesterday: vault `brain/briefs/2026-05-07-james-emden-intermediary.md` + Drive Doc `1Px_x_JHpHDdDojDozotBk8Zc4Pfu-hyKhPYnXkCdGSQ`. No Granola in-person reminder needed.

## 7. Broker BLAST Listings (per-deal extraction)

| source | headline | geo | revenue | ebitda | margin | industry | flag_reason | gmail_msg_id | listing_ordinal |
|---|---|---|---|---|---|---|---|---|---|
| Everingham & Kerr, Inc. (admin1@everkerr.com) | Family Medical Practice | Southern New Jersey | $1.5M+ | $400K+ (normalized) | ~26.7% | Family medical practice / healthcare | single-listing-blast | 19dff3511a04ba4c | 1 |

**Out of buy-box note:** Healthcare practice (clinical, not B2B services). Not advancing to target-discovery. Logged for broker-channel volume tracking only.

## 8. Auto-Drafts Created

None.

**Reasoning:** The only inbound with NDA/CA-related content was Everingham & Kerr's "Family Medical Practice" BLAST, which links to an external download URL (`https://www.everkerr.com/wp-content/uploads/2025/01/3087V-Confidentiality-Agreement_FMP.pdf`) rather than attaching a PDF. Per `<auto_ack_drafts>` trigger spec, the NDA-RECEIVED template requires a PDF attachment whose filename contains NDA/CA/non-disclosure/confidentiality. Download links do not satisfy this trigger. No auto-draft fired, by design. Listing also out of buy-box (healthcare), so even on manual review no acknowledgment is owed.

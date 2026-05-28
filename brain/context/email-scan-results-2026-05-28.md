---
date: 2026-05-28
type: context
title: "Email Scan Results — 2026-05-28 (Thu AM headless run)"
tags:
  - date/2026-05-28
  - context
  - topic/email-scan-results
  - source/email-intelligence
  - person/greg-pitkoff
  - person/marsha-weiner
  - person/jeff-stevens
  - person/jerome-madrona
  - person/katie-walker
  - person/harrison-wells
  - person/carlos-in3o
  - company/anacapa-partners
  - company/plexus-capital
  - company/dodo-digital
  - company/grip-communications
  - company/the-corporate-coach
---

# Email Scan Results — 2026-05-28

Headless 7am ET run. Window: inbound + outbound `newer_than:2d`, Granola updated since 2026-05-27 00:00Z.

System status: Gmail healthy, Granola REST healthy (2 new notes ingested). No bookkeeper P&L this run (no `*@startvirtual.com` Anthony email in the 2-day window) — no BOOKKEEPER-PL-CHAIN fire. No CIM, no NDA, no Active-Deal Fast-Path match this run.

## 1. Actionable Items Created

| inbox file | entity | urgency | source_ref | summary |
| --- | --- | --- | --- | --- |
| `brain/inbox/2026-05-28-greg-pitkoff-franchise-intro-reply.md` | [[entities/greg-pitkoff]] | normal | msg:19e6b9872e9d73c7 | Warm 2-way intro from Marsha Weiner → Greg Pitkoff (franchise PR/advisor, 30yr / 50 brands). At Javits Fri. Reply pending Kay's call (`feedback_chat_drafts_dont_land_in_gmail`). |

Entity stubs created (warm-intro grounding): [[entities/greg-pitkoff]], [[entities/grip-communications]], [[entities/marsha-weiner]], [[entities/the-corporate-coach]].

## 2. Deal Flow Classified

Window: `newer_than:2d label:INBOX` — 35 threads.

| classification | count | notes |
| --- | --- | --- |
| DIRECT | 9 | Greg Pitkoff (warm intro), Marsha Weiner (warm intro), Carlos (in3o.com) intro-ask Anacapa, Harrison Wells (Dodo Digital — Claude pricing update + check-in), Katie Walker (Plexus Capital, check-in), Rebekah Stender (Inzo Technologies — cold IT/Cyber sales pitch to `contact@`), Barrie Green (internal — calendar conflicts), August Felker (insurance DD thread, existing), Danielle Sheptin (ACG NY Women of Leadership Golf Clinic invite) |
| BLAST | 0 | (per-listing detail in section 7) |
| DEAL_NEWSLETTER | 3 | Helen Guo SMB Deal Hunter (5 listings), Flippa marketplace digest (3+ listings), Quiet Light single-listing alert (HVAC filter brand) |
| NEWSLETTER (non-deal) | 16 | Axios x3, HBR, SMBootcamp Playbook, Squarespace, Mark Edler (exit program promo), Brian Moran 12weekyear, Women's Search Network (June events), Axios Mobility, XPX x5, Attio Josie product update, Hetzner price change, CorpNet compliance reminder |
| TRANSACTIONAL (receipts/reports) | 7 | Anthropic receipt, Uber Business receipt, DMARC reports (Google + Microsoft), XPX payment + registration confirmations |

Notes:
- Carlos (in3o.com) `Intro Anacapa` is an OUTGOING intro request from Carlos asking Kay for an intro to Anacapa portfolio (Renue Environmental / Amlon Group). Not a Kay-bound intro and not a deal in our pipeline — Kay handles. Carlos in3o.com is a DIFFERENT person from Carlos Nieto DCA (Project Drone) — confirm; do not conflate.
- Kaitlinn @ Axial (`LOI terms for $45M turnkey electrical contractor`) is an **Axial newsletter case study**, not a deal offered to Kay. Reclassified to NEWSLETTER (educational LOI breakdown).
- Rebekah Stender (Inzo Technologies) is a cold IT/cyber sales pitch sent to `contact@greenwichandbarrow.com` — reactive only, no action required.
- Greg Pitkoff + Marsha Weiner = same intro, two emails — surfaced once as a single warm-intro thread.

## 3. Draft Status

13 Gmail drafts present (oldest dating back months — many superseded by Kay handling replies directly per `feedback_kay_handles_all_replies`). Per 2026-05-22 session decisions, "14 stale Gmail drafts not addressed today; related to investor update + wind-down work in flight." Status unchanged from yesterday — no new drafts created this run.

Session-decisions cross-check (2026-05-26 file): all current drafts are either superseded by Kay-direct handling (Sam Lamson sent, Carlos/August re-framed by Project Drone reversal) or part of the investor-update / wind-down work-in-flight. No flag-as-stale action needed today.

## 4. Introductions Detected

| date | introducer | introducee | direction | inbox item |
| --- | --- | --- | --- | --- |
| 2026-05-27 | [[entities/marsha-weiner\|Marsha Weiner]] (The Corporate Coach, met at Heels and Deals) | [[entities/greg-pitkoff\|Greg Pitkoff]] (Grip Communications PR, franchise advisor) | Inbound to Kay | `brain/inbox/2026-05-28-greg-pitkoff-franchise-intro-reply.md` |
| 2026-05-26 | n/a — outgoing-intro REQUEST from [[entities/carlos-in3o\|Carlos (in3o.com)]] | (asks Kay to intro him to Anacapa Partners portfolio re. Renue Environmental / Amlon Group) | Outbound ASK on Kay | Surfaced; Kay decides whether to broker. No inbox item — needs Kay judgment first. |

## 5. Niche Signals

- **Franchise sector:** warm intro from Marsha Weiner via Heels and Deals women's network (Greg Pitkoff, 30yr franchise PR advisor). Franchise is NOT in current G&B buy-box (not on the Industry Research Tracker active list), but the network connection is the asset. Surface as relationship infrastructure, not deal flow.
- **Environmental remediation / industrial services:** Carlos (in3o.com) flagged Renue Environmental + Amlon Group as Anacapa-portfolio adjacent. Industrial services thesis-shape-positive but Carlos is asking Kay for an intro out, not surfacing a target. Note only.
- **HVAC adjacency:** Quiet Light listing — washable HVAC filter DTC brand, $125K rev / $57K SDE — far below buy-box ($2M+ EBITDA floor relaxed per 5/19 doctrine but still wants $300K salary + 15% margin + IRR support). Sub-scale; pure-DTC consumer; skip.
- **Truck / logistics:** Helen Guo #4 (IA trucking, 12-month contracts, $1.5M EBITDA) sits at the lower edge of buy-box. Geographically OK (Iowa, US). Mention only — broker-channel decision belongs to Kay if anything.
- **Pest management:** no new pest signals in inbox this run (the active 10-co June experiment per 5/26 decisions runs in-channel via target-discovery / outreach-manager, not email-intel).

## 6. In-Person Meetings Today

None. Today's calendar (Thu 5/28) is virtual-only:
- 10:00-10:45 ET — WP Career Coach: Erika Teresko (NYU Zoom)
- 11:00-11:30 ET — Abigail | Kay (Google Meet)
- (Plus any later-day Guillermo Lavergne biweekly per cadence — confirm in goodmorning brief.)

No Granola in-person reminder needed.

## 7. Broker BLAST Listings (per-deal extraction)

| source | headline | geo | revenue | ebitda | margin | industry | flag_reason | gmail_msg_id | listing_ordinal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Helen Guo, SMB Deal Hunter | Semi-Absentee Auto Repair & Smog Check Shop | Southern CA | $1.22M | $500K | ~41% | Auto repair / smog inspection | deal-newsletter-known-sender | 19e6aadd6eceb46d | 1 |
| Helen Guo, SMB Deal Hunter | Wholesale Ice Cream Distributor (30-year route network) | Central CA | $1.1M | $385K | ~35% | Frozen food distribution | deal-newsletter-known-sender | 19e6aadd6eceb46d | 2 |
| Helen Guo, SMB Deal Hunter | Automotive Aftermarket Parts & Services (70 dealership clients) | MN | undisclosed | $1.7M | undisclosed | Automotive aftermarket | deal-newsletter-known-sender | 19e6aadd6eceb46d | 3 |
| Helen Guo, SMB Deal Hunter | Trucking Company (12-month contracts) | IA | undisclosed | $1.5M | undisclosed | Trucking / logistics | deal-newsletter-known-sender | 19e6aadd6eceb46d | 4 |
| Helen Guo, SMB Deal Hunter | Truss Manufacturing Company (recent growth) | FL | undisclosed | $400K | undisclosed | Building products / manufacturing | deal-newsletter-known-sender | 19e6aadd6eceb46d | 5 |
| Tory, Flippa Marketplace | Premium Home Sauna Shopify Brand (broker: Amber Burke) | undisclosed (US) | $20M | undisclosed | undisclosed | DTC e-commerce / home wellness | deal-newsletter-known-sender | 19e6acf9abae37c2 | 1 |
| Tory, Flippa Marketplace | Established SEO Agency (10-year, $95K contract value, 10 active clients) | undisclosed | $755K | undisclosed | undisclosed | Digital marketing services | deal-newsletter-known-sender | 19e6acf9abae37c2 | 2 |
| Tory, Flippa Marketplace | Global Travel Connectivity Brand (portable Wi-Fi + eSIM, 12-year-old) | undisclosed (global) | $331K | undisclosed | 79% | Travel tech / DTC | deal-newsletter-known-sender | 19e6acf9abae37c2 | 3 |
| Tory, Flippa Marketplace | 4.4-Star Headwear Brand (per subject line) | undisclosed | undisclosed | undisclosed | undisclosed | DTC apparel | deal-newsletter-known-sender | 19e6acf9abae37c2 | 4 |
| Riad Bekhit, Quiet Light | Washable HVAC Filter DTC Brand (patent-pending, 219% revenue growth) | North America (US sellable, USMCA Canada-mfg) | $125,173 | $57,462 SDE | 46% net | DTC consumer products / HVAC consumables | single-listing-blast | 19e6aa0907b11b00 | 1 |

Section-7 KPI total this run: **10 broker-channel listings extracted** across 3 emails (1 multi-listing newsletter @ 5, 1 multi-listing marketplace digest @ 4, 1 single-listing alert @ 1). No California, sub-scale, DTC consumer, and broker-marketplace listings dominate — none clear the G&B four-gate; Kay can scan in seconds.

## 8. Auto-Drafts Created

None. No inbound NDA or CIM PDF attachments this run. (Carlos in3o.com's `Company Update 2026.pdf` is a portfolio company update, not an NDA/CIM; Katie Walker's `image001.png` is a signature image. Neither matches the `<auto_ack_drafts>` trigger.)

---

## Granola Action Items (ingested this run)

| call file | classification | granola id | notes |
| --- | --- | --- | --- |
| `brain/calls/2026-05-27-jeff-kay-mtg.md` | partner | not_Uq2NMa3Kz51FFq / `b55f5f1e-3fe1-4993-882c-752328623a48` | Monthly Jeff Stevens / Anacapa cadence. Post-call-analyzer (1pm fire) will extract structured action items. |
| `brain/calls/2026-05-27-team-tb-jj-kay.md` | internal | not_lrTNq6HzuDmTck / `2b0a551c-a17d-42c0-8ba0-f37f4fe0d972` | Weekly JJ/Abby ops sync. Per `feedback_jj_operations_review_mondays_only`, decisions wait until Monday window. |

Both files written idempotently — pre-existing brain/calls/ files were checked by date+slug before write.

---

*Generated by `email-intelligence` headless weekday run 2026-05-28 07am ET.*

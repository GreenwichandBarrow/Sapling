---
date: 2026-05-15
type: context
title: "Email Scan Results — 2026-05-15"
tags:
  - date/2026-05-15
  - context
  - topic/email-scan-results
  - topic/morning-briefing
  - topic/broker-blast
  - topic/dealsx-inbound
  - topic/mid-search-summit
  - company/everingham-and-kerr
  - company/quietlight
  - company/flippa
  - company/business-exits
  - company/pacific-lake-partners
  - company/dealsx
  - company/anacapa-partners
  - company/breakpoint-growth
  - person/hannah-barrett
  - person/julie-diorio
  - person/harrison-wells
  - person/barrie-green
  - person/david-freeman
schema_version: 1.1.0
---

# Email Scan Results — 2026-05-15

Headless 7am ET run (Friday). Scanned `newer_than:2d label:INBOX` (50-msg cap) + outbound from `kay.s@greenwichandbarrow.com` AND `admin@greenwichandbarrow.com` per [[memory/feedback_kay_outbound_includes_admin_alias]] + Gmail drafts + calendar for today's in-person meetings.

**No bookkeeper P&L detected in window.** No sender from `startvirtual.com`, no "Management Report" subject, no Profit-and-Loss/Balance-Sheet attachment. Chain NOT fired (correct — would have re-fired April 2026 trigger; chain already executed 2026-05-13 per `brain/outputs/2026-05-13-budget-report-april-2026.md`). No `BOOKKEEPER-PL-CHAIN:` marker required this run.

**No CIM detected.** No PDF attachments matching CIM/offering-memorandum/teaser size+filename heuristic. CIM auto-trigger not fired.

**No NDA attachment detected.** E&K BLAST includes "DOWNLOAD NDA HERE" link in body (typical broker teaser pattern) but no attached NDA — auto-ack draft not fired per `<auto_ack_drafts>` trigger conditions (attachment required, not body link).

**No Active Deal Fast-Path triggered.** No inbound matched a stages-3-through-9 Active Deals entry.

**Granola MCP not invoked this run** — graceful-degrade noted in Section 6. Calendar-based in-person reminder still emitted.

## 1. Actionable Items Created

| # | Item | Source | Why surfaced |
|---|------|--------|--------------|
| 1 | Hannah Barrett (Pacific Lake) — Mid-Search Summit logistics 5/18–5/19 | Gmail thread `19e075d37b49da50` (6-message thread, unchanged since 2026-05-14 artifact) | Carryover from 2026-05-14 — no new replies in 24h. Travel + agenda confirm needed before Sunday flight. Pipeline-manager to verify Kay's reply status before re-surfacing. |
| 2 | Barrie Green — calendar conflict heads-up | Gmail thread `19e26825d89f7c07` (5/14 11:42 ET) | Team-internal, informational. Surface in briefing as 🟢 only if conflict requires Kay's decision; pipeline-manager opens the thread to check what conflict was flagged. |

DealsX inbound (3 leads from `dealsx.notifaction@gmail.com` to `admin@`) lives in DealsX channel funnel per `feedback_dealsx_is_cold_email_infra` — not surfaced here, no vault entity created. Leads: Matthew Feldman (`yulacorp.com`, 5/14 12:03), 2 unnamed leads (5/13 23:22 and 5/13 10:25).

No new entity stubs needed — `julie-diorio.md`, `hannah-barrett.md`, `everingham-kerr.md`, `dealsx.md` already exist.

## 2. Deal Flow Classified

| Class | Count | Notes |
|-------|-------|-------|
| DIRECT | 4 | Hannah Barrett (Pacific Lake), Harrison Wells (AI security thread — Kay already engaged 5/13), Barrie Green (internal), Kay S forwarded "Greenwich & Barrow / Aspect" (self-forward from `kaycschneider@gmail.com`) |
| BLAST | 6 | E&K, Helen Guo SMB Deal Hunter, Tory @ Flippa, Chuck Mullins quietlight, Jon Hainstock quietlight, Business Exits |
| DealsX inbound | 3 | Prospect Geni notification emails, structured-lead format (not BLAST, not DIRECT) |
| NEWSLETTER | 24 | Axios (4 issues), DMARC report, Tailscale (3), Anacapa (2 — reminder + Q2 mid-quarter update), 1Password (2), Cornell, Howie, Le Pain Quotidien receipt, XPX, Live Oak, Michael Girdley, Frank Sondors, Nick Huber, Slack, Royal Sonesta confirm, CorpNet Delaware franchise tax, Granola receipt, Uber receipts (2), Peter Lang |

Total inbound threads scanned: 40.

## 3. Draft Status

9 Gmail drafts surfaced via `gog gmail draft list --json`. Composition:

| Draft ID | Thread | Age | Note |
|---|---|---|---|
| `r2253803435468898722` | `19e1c6aaee6123b7` | <24h | Active — related to Aspect Investors thread (Kay forwarded 5/14 15:38). Not stale. |
| `r989550462937595579` | `19caf435aed1cf61` | >48h, very old | Long-stale, pre-Superhuman-sunset. Defer to weekly cleanup, do not surface to Kay in daily briefing. |
| `r-5013177138505427051` | `19c81d2d5f656082` | >48h, very old | Same: long-stale legacy draft. |
| `r-2787224895918893720` | `19c81cd7f43d3b45` | >48h, very old | Same. |
| `r-5225012692018162578` | `19c81ccca79c19d9` | >48h, very old | Same. |
| `r1586280898950821814` | `19c81cc21ac2c6d0` | >48h, very old | Same. |
| `r-8150415091260429779` | `19c81caebabc77e0` | >48h, very old | Same. |
| `r-4571119820160089244` | `19c81ca150066bf3` | >48h, very old | Same. |
| `r8922907573534439329` | `19c81c8d5cc42def` | >48h, very old | Same. |

Cross-checked against `brain/context/session-decisions-2026-05-12.md` (most recent) — none of the legacy drafts appear with SENT/DELETED verbs. They are pre-existing Gmail accumulation, not session-driven. Recommend Kay sweep at next maintenance pass; not blocking morning briefing.

## 4. Introductions Detected

None this run. Kay's `Fwd: Greenwich & Barrow / Aspect` (thread `19e1c6a8f4376653`) is a self-forward from her personal Gmail (`kaycschneider@gmail.com`) to `kay.s@`, not an external warm intro. No CC patterns suggesting new-person introduction.

## 5. Niche Signals

Passive observations from inbound (broker BLASTs + DealsX leads):

- **Metal Manufacturing / Precision Machining / Tool & Die** (E&K, Mid-Atlantic, $20M+ rev / $4.2M EBITDA) — industrial precision manufacturing aligning with Aerospace, Oil & Gas, Heavy Industrial customers.
- **Residential HVAC w/ recurring service agreements** (Helen Guo, LA, 400+ active service agreements, $434K EBITDA) — recurring-revenue HVAC signal; current G&B niche tracker has HVAC under review.
- **Commercial Glass & Glazing Contractor** (Helen Guo, AL, $1.335M EBITDA, $7.03M revenue, established 1970s) — specialty trades / commercial construction services.
- **Cabinetry Fabrication & Installation** (Helen Guo, AZ, $515K EBITDA, repeat GC relationships) — specialty trades / building products.
- **Medical / Med Spa & Regenerative Medicine** (Business Exits, Florida) — health & wellness adjacency.
- **Customizable Plant Kit / Corporate Gifting** (Jon Hainstock @ quietlight, Q1 rev +179% YoY, four sales channels) — DTC corporate-gifting.
- **20-yr-old Women's Health Authority Website** (Chuck Mullins @ quietlight, DR60, 15K forum posts, 500+ articles) — content-authority site, digital-only, unlikely-fit.
- **Hair Styling Brand, $3.5M ARR** (Tory @ Flippa) — DTC consumer brand.

No active G&B niche-level pattern shifts detected — these are typical broker-BLAST distribution. Surface to niche-intelligence Tuesday for potential niche-tracker observations on HVAC + specialty trades.

## 6. In-Person Meetings Today

| Time (ET) | Meeting | Notes |
|---|---|---|
| 9:30–10:30 AM | Coffee w/ Julie Diorio | Calendar event has no Google Meet link → in-person assumed. Granola reminder applies if Kay records via mobile. |

Other Friday calendar events (virtual, not flagged for Granola in-person):
- 1:00–2:00 PM ET — Harrison <> Kay AI Coaching Session (Google Meet `wzs-jhqe-bne`).
- AI Friday speaker session (Mike Molinet @ Branch/Thena via askoneguide.com — virtual).

**Granola MCP not invoked this run** — call ingestion skipped. No new `brain/calls/` writes. Per `feedback_check_credential_source_before_auth`, attempting Granola OAuth bypass in a headless wrapper is the wrong tradeoff at 7am ET. Kay's most-recent ingested call is `brain/calls/2026-05-13-carlos-nieto-dca.md`. Backlog catches up on next interactive session or 1pm/6pm `post-call-analyzer` fires.

## 7. Broker BLAST Listings (per-deal extraction)

11 listings extracted across 6 broker BLASTs. Multi-listing blasts decomposed per row per `<broker_blast_listing_extraction>`.

| source | headline | geo | revenue | ebitda | margin | industry | flag_reason | gmail_msg_id | listing_ordinal |
|---|---|---|---|---|---|---|---|---|---|
| Everingham & Kerr | Provider of Metal Manufacturing; Precision Machining, Stamping & Tool & Die | Mid-Atlantic (state undisclosed) | $20M+ | $4.2M | ~21% | Metal Manufacturing / Precision Machining | single-listing-blast | 19e28b9600f7365b | 1 |
| Helen Guo SMB Deal Hunter | Commercial Glass and Glazing Contractor (asking $7.9M) | AL | $7,030,996 | $1,335,113 | ~19% | Commercial Glass & Glazing | multi-listing | 19e2753aa2a436e7 | 1 |
| Helen Guo SMB Deal Hunter | Cabinetry Fabrication and Installation Company | AZ | undisclosed | $515,000 | undisclosed | Cabinetry / Building Products | multi-listing | 19e2753aa2a436e7 | 2 |
| Helen Guo SMB Deal Hunter | Residential HVAC Service Company with 400+ Active Service Agreements | LA | undisclosed | $434,000 | undisclosed | Residential HVAC | multi-listing | 19e2753aa2a436e7 | 3 |
| Helen Guo SMB Deal Hunter | Gas Station with Triple-Net McDonald's Lease | WI | undisclosed | $512,000 | undisclosed | Gas Station / Convenience Retail | multi-listing | 19e2753aa2a436e7 | 4 |
| Helen Guo SMB Deal Hunter | Fully Staffed High-Volume Convenience Store | MD | undisclosed | $500,000 | undisclosed | Convenience Retail | multi-listing | 19e2753aa2a436e7 | 5 |
| Tory @ Flippa | $3.5M Annual Revenue Hair Styling Brand | undisclosed | $3,500,000 | undisclosed | undisclosed | DTC Consumer Brand | multi-listing | 19e27e87c21f3d5d | 1 |
| Tory @ Flippa | 96% Margin Automated Trading SaaS (10K active subscribers) | undisclosed | undisclosed | undisclosed | 96% | SaaS | multi-listing | 19e27e87c21f3d5d | 2 |
| Tory @ Flippa | Video to Blog SaaS (462 active subscribers, 12K MRR) | undisclosed | $144,000 ARR (~12K MRR) | undisclosed | undisclosed | SaaS | multi-listing | 19e27e87c21f3d5d | 3 |
| Chuck Mullins, Quiet Light | 20-Year-Old Women's Health Authority Website (DR60, 15K forum posts) | undisclosed | undisclosed | undisclosed | undisclosed | Content / Media | single-listing-blast | 19e27adc6685475f | 1 |
| Jon Hainstock, Quiet Light | Customizable Plant Kit Brand (Q1 rev +179% YoY, 4 sales channels) | undisclosed | undisclosed | undisclosed | undisclosed | DTC Consumer Brand | single-listing-blast | 19e26d27d000a73d | 1 |
| Business Exits | Florida Med Spa and Regenerative Medicine Clinic | FL | undisclosed | undisclosed | undisclosed | Healthcare / Med Spa | single-listing-blast | 19e270139cbb89f1 | 1 |

## 8. Auto-Drafts Created

None. No inbound emails this run triggered `<auto_ack_drafts>`: zero NDA attachments, zero CIM-classified attachments. E&K's "DOWNLOAD NDA HERE" is a body link, not an attached file — does not match the trigger schema (attachment-based, per `<auto_ack_drafts>` lines 198–207).

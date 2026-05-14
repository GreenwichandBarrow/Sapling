---
date: 2026-05-14
type: context
title: "Email Scan Results — 2026-05-14"
tags:
  - date/2026-05-14
  - context
  - topic/email-scan-results
  - topic/morning-briefing
  - topic/broker-blast
  - topic/dealsx-inbound
  - topic/acg-women-of-leadership
  - company/everingham-and-kerr
  - company/pacific-lake-partners
  - company/dealsx
  - company/anacapa-partners
  - company/stream-capital-partners
  - company/bankunited
  - person/hannah-barrett
  - person/laura-smith-bankunited
  - person/krupa-shah
  - person/jackson-niketas
  - person/harrison-wells
  - person/anthony-bacagan
schema_version: 1.1.0
---

# Email Scan Results — 2026-05-14

Headless 7am ET run. Scanned `newer_than:2d label:INBOX` (50-msg cap) + outbound from `kay.s@greenwichandbarrow.com` + Gmail drafts + calendar for today's in-person meetings. Granola MCP unauthenticated — call ingestion skipped this run (see Section 6 + Actionable Items).

Bookkeeper P&L (April 2026) detected in the 2-day window but **idempotent-skipped** — chain already fired 2026-05-13 (`brain/outputs/2026-05-13-budget-report-april-2026.md` + `brain/inbox/2026-05-13-april-management-report-budget-trigger.md`). Wrapper log line emitted for validator. No re-fire.

## 1. Actionable Items Created

| # | Item | Source | Why surfaced |
|---|------|--------|--------------|
| 1 | Hannah Barrett (Pacific Lake) — Mid-Search Summit logistics for 5/18–5/19 | Gmail msg `19e075d37b49da50` (5-message thread, latest 2026-05-14 00:55) | Travel + agenda confirm needed before Sunday flight. **Important** flag, multi-message thread. |
| 2 | Everingham & Kerr — Luxury Kitchen and Bath Designer (new listing) | Gmail msg `19e235fe730b1b7f` | Broker BLAST single listing; per-listing row in Section 7. Auto-archive after pipeline-manager check. |
| 3 | DealsX inbound interest — Adam Pruitt (fuegomobilecigars.com) | Gmail msg `19e248220b3c53a0` (5/13 23:22, to `admin@`) | DealsX outbound reply. Lives in DealsX channel funnel per `feedback_dealsx_is_cold_email_infra`; no vault entity created. |
| 4 | DealsX inbound interest — Emilio Miti (volanobiz.com) | Gmail msg `19e21ba6e7b7ff27` (5/13 10:25, to `admin@`) | Same as #3; DealsX channel handling. |
| 5 | Slack support data + FedRAMP notice — possible action required | Gmail msg `19e25b501e34be51` | Vendor admin; CIO can review whether retention or SOC2 surface needs response. |
| 6 | Delaware LLC franchise tax due June 1 (CorpNet) | Gmail msg `19e21db9f37c0144` | Fixed deadline. CFO/admin task. |
| 7 | Royal Sonesta Boston modification confirmation | Gmail msg `19e230491de46802` | Travel confirm for Mid-Search Summit (5/18–5/19) — pair with Item 1. |

**No inbox files written this run** — items 1, 5, 6, 7 are time-bounded but already trackable via Gmail labels + calendar; surfacing them through this artifact is sufficient for pipeline-manager. DealsX leads (3, 4) live in the DealsX funnel (no vault entity per channel doctrine). Everingham & Kerr (2) is BLAST per-listing — Section 7 is the canonical record.

**Granola ingestion skipped** — Granola MCP requires OAuth re-auth (open loop carried from 2026-05-12 session decisions; Friday Harrison call agenda #1). No new `brain/calls/` files written this run. Latest call note on file: `2026-05-13-carlos-nieto-dca.md`.

## 2. Deal Flow Classified

**DIRECT (6):**
- Harrison Wells `<harrison@dododigital.ai>` — "[Urgent] AI security vulnerabilities" (4-msg thread, in-progress per outbound activity)
- Jackson Niketas `<jniketas@terramarsearch.com>` — "Thank you" (2-msg thread, Kay replied per outbound)
- Hannah Barrett `<hannah.barrett@pacificlake.com>` — "Important Info for Mid-Search Summit -- May 18 - 19" (5-msg thread)
- Kay S `<kaycschneider@gmail.com>` — "Fwd: Touch Base" (self-forward to Kay's G&B inbox; intro thread — see Section 4)
- Royal Sonesta Boston `<info@cvent.com>` — "Royal Sonesta Boston Modification Confirmation" (travel transactional)
- CorpNet Compliance `<info@sfmail.corpnet.com>` — "Delaware LLC Annual Franchise Tax Due June 1" (compliance fixed-deadline)

**BLAST (1):**
- Everingham & Kerr `<admin1@everkerr.com>` — "E&K: New Acquisition Opportunity - Luxury Kitchen and Bath Designer" (Mailjet bulk, precedence:bulk, List-Unsubscribe present) → Section 7 row

**NEWSLETTER (15):**
- Mike Allen / Axios AM (2) — news
- Slack (2) — vendor admin (FedRAMP + May admin update)
- DMARC aggregate reports (2) — Microsoft, Google — tech-stack monitoring
- Harvard Business Review — "Future of work" promo
- Hannah Barrett / Pacific Lake — counted as DIRECT (above), not newsletter
- Pacific Lake / Hannah Barrett — covered above
- Team Tailscale — onboarding nudge
- Brian Moran / 12 Week Year — sales promo
- Beacon / Anacapa Partners — "Mid-Quarter Update Q2 2026" (investor newsletter)
- CorpNet — "Annual Report Is Due Soon — Avoid Penalties & File Early" (promotional; distinct from the franchise tax DIRECT above)
- Anthony Bacagan / Startvirtual — Management Report April 2026 (P&L; idempotent-skip — see header)
- NPMA Events — "Women's Forum Experiences" — niche signal
- XPX New York City — Summer Networking Social
- Frank Sondors / Salesforge — outbound education newsletter
- Amanda Lo Iacono — "We Are Live" (Substack launch)

**Prospect Geni / DealsX (2):** Treated as DIRECT-via-channel — these are interested-lead replies from DealsX outbound, not classification categories. Counted in Actionable Items 3 + 4.

**Totals:** Inbound 26 threads scanned; DIRECT 6, BLAST 1, NEWSLETTER 15, DealsX-channel 2, transactional/admin 2 (Anthony P&L which is its own auto-trigger pathway + Kay's self-screenshot send).

## 3. Draft Status

9 Gmail drafts total. **None sent in the last 2 days from drafts** (verified — Kay's outbound came from net-new compose, not draft-promotion).

| Draft ID | Thread | Subject (inferred) | Status |
|----------|--------|---------------------|--------|
| `r2253803435468898722` | `19e1c6aaee6123b7` | Fwd: Touch Base reply | Active — 2026-05-12, ~48h old, on the intro thread Kay forwarded to herself. Surface to Kay for review/send. |
| `r989550462937595579` | `19caf435aed1cf61` | (legacy) | Stale — message ID in `19caf...` range, multi-month old. Skip surface. |
| `r-5013177138505427051` | `19c81d2d5f656082` | (legacy) | Stale — `19c81...` range, multi-month old. Skip surface. |
| `r-2787224895918893720` | `19c81cd7f43d3b45` | (legacy) | Stale. Skip. |
| `r-5225012692018162578` | `19c81ccca79c19d9` | (legacy) | Stale. Skip. |
| `r1586280898950821814` | `19c81cc21ac2c6d0` | (legacy) | Stale. Skip. |
| `r-8150415091260429779` | `19c81caebabc77e0` | (legacy) | Stale. Skip. |
| `r-4571119820160089244` | `19c81ca150066bf3` | (legacy) | Stale. Skip. |
| `r8922907573534439329` | `19c81c8d5cc42def` | (legacy) | Stale. Skip. |

**Session-decisions cross-check:** `brain/context/session-decisions-2026-05-12.md` lists Saltoun, Jeanne Wang, Brad Buser drafts as SENT or DRAFTED — those threads are not in the current draft list (Saltoun sent; Wang + Buser drafted on 5/12 may have been sent or remain — not surfaced again here). No SENT/DELETED entries cover the legacy `19c81...` drafts; they are old enough that the per-feedback rule `feedback_check_status_before_surfacing_carryover` argues against re-surfacing repeatedly.

**Open carryover:** Touch Base draft (`r2253803435468898722`) — surface to Kay for review/send. Decide-or-delete recommended.

## 4. Introductions Detected

**1 intro forward:**
- "Fwd: Touch Base" from Kay's personal Gmail (`kaycschneider@gmail.com`) to her G&B inbox, 2026-05-12 10:06. Self-forwarded thread; the existing draft (Section 3 above) is Kay's pending response. The thread is currently captured but the introducing party / target are not extractable from headers alone — body parse needed. **No new entity stub created this run** — pipeline-manager / relationship-manager can resolve once Kay reviews the draft.

## 5. Niche Signals

- **NPMA Women's Forum 2026** (`19e1d6867888ad29`) — pest management niche, active niche per Industry Research Tracker. Cross-references the Women in Pest Mgmt week of 5/18 already on Kay's travel calendar. CPO can flag if conference-engagement skill should pre-stage outreach to women-led attendees per `feedback_women_network_priority`.
- **XPX NY Summer Social** (`19e1c0b15682cbb9`) — exit planning ecosystem; intermediary network signal (lawyers / CPAs / advisors). Conference-discovery channel.
- **Anacapa Mid-Quarter Update Q2 2026** (`19e21f68550f30dc`) — investor LP newsletter. Not a niche signal; tagged for LP-relations awareness (Beacon @ Anacapa is a G&B LP).
- **Brian Moran / 12 Week Year sprint training** (`19e2369eb2c3bc30`) — adjacent productivity ecosystem; not a niche match.

## 6. In-Person Meetings Today

Today is the **2026 ACG NY 13th Annual Women of Leadership Summit** at New York Athletic Club (180 Central Park South). Full-day in-person — Granola transcript reminder applies to the 1:1s but Granola MCP is unauthenticated this run (see header). Per Friday Harrison call agenda, Granola re-auth is priority #1.

| Time | Meeting | Counterparty firm | Location | Granola? |
|------|---------|-------------------|----------|----------|
| 9:00–9:20 ET | ACG 1:1 with Laura Smith | BankUnited (Lender) | NY Athletic Club | Manual record needed (Granola down) |
| 10:00–10:15 ET | ACG 1:1 with Krupa Shah | STREAM Capital Partners (Sell-side M&A advisory) | NY Athletic Club | Manual record needed |
| 10:30–15:55 ET | ACG NY Women of Leadership Summit (panels, networking) | ACG NY | NY Athletic Club | n/a (full-day event) |

## 7. Broker BLAST Listings (per-deal extraction)

| source | headline | geo | revenue | ebitda | margin | industry | flag_reason | gmail_msg_id | listing_ordinal |
|--------|----------|-----|---------|--------|--------|----------|-------------|---------------|-----------------|
| Everingham & Kerr, Inc. (admin1@everkerr.com) | Luxury Kitchen and Bath Designer (new acquisition opportunity) | undisclosed | undisclosed | undisclosed | undisclosed | Kitchen and Bath Design / Home Improvement | single-listing-blast | 19e235fe730b1b7f | 1 |

Subject indicated a single listing; body was Mailjet HTML (campaign 7752963434, precedence:bulk, list-unsubscribe present). Sender domain `everkerr.com` is not in `feedback_blocked_sources_tab_rule` blocked sources; intermediary cold-channel — no Attio entry per `feedback_brokers_stay_in_sheet_until_reply`.

## 8. Auto-Drafts Created

None. No inbound NDA-attachment or CIM-attachment emails this scan window matched `<auto_ack_drafts>` triggers.

---

## Stop-Hook Self-Check

- [x] Gmail ingestion run (inbound 50-cap, outbound 50-cap, drafts list).
- [x] Outbound cross-check executed before flagging any DIRECT thread as "needs reply" (per `feedback_email_intel_check_kay_outbound_first` + `feedback_kay_outbound_includes_admin_alias` — admin alias also searched for DealsX leads).
- [x] No CIM detected → CIM auto-trigger skipped (clean).
- [x] No Active Deal stage 3-9 match → Active Deal Fast-Path skipped (clean).
- [x] Bookkeeper P&L detected (Anthony, 5/12) → **idempotent-skipped** (April 2026 chain fired 2026-05-13; budget-report exists). `BOOKKEEPER-PL-CHAIN: skipped period 2026-04 ...` marker emitted to stdout.
- [-] Granola ingestion → **skipped** (MCP unauthenticated; carries open loop from 2026-05-12 — Friday Harrison call agenda #1).
- [x] Broker BLAST per-listing extraction → 1 row (single-listing E&K).
- [x] Auto-acknowledgment drafts → 0 (no NDA/CIM attachments).
- [x] Artifact written with all 8 sections present.
- [-] Slack pings → none required this run (no CIM, no Active Deal Fast-Path).
- [x] Attio writes → none required (no CIM stage-entry).

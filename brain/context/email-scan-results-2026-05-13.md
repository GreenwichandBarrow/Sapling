---
date: 2026-05-13
skill: email-intelligence
mode: headless-weekday
run_window: 2026-05-11 → 2026-05-13 (newer_than:2d)
gmail_inbound_count: 29
gmail_outbound_count: 9
drafts_total: 10
granola_ingested: 0
granola_status: unavailable (PKCE OAuth — not authable in headless)
cim_triggers: 0
active_deal_fast_path_triggers: 0
bookkeeper_pl_triggers: 1
auto_drafts_created: 0
broker_blast_listing_rows: 1
---

# Email Scan Results — 2026-05-13

## Bookkeeper P&L chain marker

```
BOOKKEEPER-PL-CHAIN: invoked budget-manager monthly for period 2026-04
```

Auto-trigger fired for [[entities/anthony-bacagan|Anthony Bacagan]] / [[entities/start-virtual|StartVirtual]] April 2026 Management Report (Gmail msg `19e1d7b05db2ef4c`, received 2026-05-12 2:37pm ET). 3 PDFs filed to Drive subfolder **APRIL 2026** (folder ID `1BchMB2hy_-lyAlBiBdqUzbOIIJIzPZ4f`). Inbox trigger written: `brain/inbox/2026-05-13-april-management-report-budget-trigger.md`. Budget-manager subagent completed all 3 phases — output: `brain/outputs/2026-05-13-budget-report-april-2026.md` (10,913 bytes). Runway 7.1 mo from May 1; -2 mo shortfall vs Feb 2027 (improved 1.5 mo); 12 variance flags. Slack ping HTTP 200.

## 1. Actionable Items Created

| inbox file | source_ref | urgency | confidence |
| --- | --- | --- | --- |
| `brain/inbox/2026-05-13-april-management-report-budget-trigger.md` | `msg:19e1d7b05db2ef4c` | high | high |

**Actionable Items / failures to surface (pipeline-manager: please flag these in the morning briefing):**
- **Granola MCP unauthenticated** — PKCE OAuth flow cannot complete in headless mode. No call notes ingested this run. Pattern matches `feedback_granola_mcp_same_session_pkce` — fix requires a one-time interactive `claude` session to relay the callback URL. No Granola meetings since last run could not be reconciled.
- **Janet Crockett / Saltoun Annual Financial Review (5/11 8:11pm ET)** — Inbound asked Kay to confirm SCP SF4 LLC investment of $42,176 as of 12/31/2025, reply-all with Citrin Cooperman cc'd, response requested within 1 week. **Outbound check: Kay replied on 2026-05-12** (thread `19e191898ebc8ddc`, messageCount 2). Loop appears closed — no further action expected from us.
- **Andrew Lowis / Axial XPX follow-up** — Thread `19dc0f11d1a3bf68` now at 14 messages, originally seeded 2026-04-24 ("Nice meeting you at XPX yesterday"). Latest activity 2026-05-06. Worth a pipeline-manager check on whether the thread has stalled and a nudge is warranted (cadence-debt — surface Friday only per `feedback_relationship_cadence_friday_only`).
- **Hannah Barrett / Pacific Lake Mid-Search Summit (5/11)** — Inbound logistics for the 5/18-5/19 summit. messageCount 3 (Kay's outbound list shows the same thread ID with messageCount 3, so Kay replied). Loop appears closed.
- **Jackson Niketas / Terra Mar — "Thank you" reply (5/12 11:07am ET)** — Post-call thank-you after Tuesday morning conversation. Cited Kay's sailing background + Myself Renewed. No action required from Kay; nice-to-have nurture entry. Adding Jackson as a vault entity is deferred (out-of-scope for headless email-intelligence; relationship-manager can pick it up Friday).
- **donotreply@meetmax.com — ACG NY Women of Leadership Summit meeting request (5/12 1:43pm ET)** — One-on-one match notification. Subject: "New Meeting Request (Your action required)". Worth pipeline-manager surfacing for accept/decline decision.
- **CorpNet Compliance / Annual Report due (5/12 1:00pm ET)** — Promotional reminder. No action; CorpNet vendor-side prompt.
- **Carlos Nieto Visbal / Empire State Building visit reminder (5/13 6:25am ET)** — For today's 9:30am Empire State meeting w/ Digital Capital Advisors. Operational reminder only.

## 2. Deal Flow Classified

| classification | count | notes |
| --- | --- | --- |
| DIRECT | 5 | Anthony Bacagan (P&L), Andrew Lowis (Axial — ongoing), Hannah Barrett (Pacific Lake), Jackson Niketas (Terra Mar thank-you), Janet Crockett (Saltoun, prior workday — kay replied) |
| BLAST | 2 | Tory @ Flippa (marketplace cattle-call — NOT broker per `feedback_marketplace_vs_broker_distinction`), Ian Drogin @ Quiet Light (single-listing broker BLAST — see section 7) |
| NEWSLETTER | 14 | Mike Allen @ Axios x3, Cornell Alumni x2, HBR, NPMA Events x2, PestWorld 2026, 1Password, XPX, Amanda Lo Iacono / CounterA, Frank Sondors / Salesforge, DMARC Microsoft |
| OPERATIONAL | 8 | Carlos Nieto Visbal x2 (Rise / Empire State), Uber Receipts x2, donotreply@meetmax.com (ACG match), CorpNet Compliance, Kay's own forwards (Touch Base, Aspect, Emailing from new job), Barrie Green (internal calendar conflicts) |

**Marketplace vs broker note:** Tory @ Flippa stays BLAST/marketplace and is NOT extracted into section 7 — Flippa is cattle-call marketplace, not broker channel (per memory `feedback_marketplace_vs_broker_distinction.md`). Even though body parsed cleanly with 4+ listings (Gearbox Parts $762K, Leadership Tools $795K, Home/DIY Blog $163K, Fantasy Sports Blog $127K), these do not feed the broker-deal-flow audit.

## 3. Draft Status

`gog gmail draft list` returned 10 drafts total. Recent / relevant:

| draft_id | thread_id | age (days) | inferred recipient | status |
| --- | --- | --- | --- | --- |
| `r2253803435468898722` | `19e1c6aaee6123b7` | <1 | Re: Fwd: Touch Base (Kay's own forward, 5/12) | pending — recent, not stale |
| `r-1677726094159477892` | `19e1c6a8f4376653` | <1 | Re: Fwd: Greenwich & Barrow / Aspect (Kay's own forward, 5/12) | pending — recent, not stale |
| `r989550462937595579` | `19caf435aed1cf61` | ~80 (Feb 2026) | older thread | stale — flag for cleanup or send |
| 6 older drafts (ids `r-5013…`, `r-2787…`, `r-5225…`, `r1586…`, `r-8150…`, `r-4571…`, `r8922…`) | threads `19c81…` (Jan 2026 cohort) | ~120+ | older threads | stale — flag for cleanup (likely abandoned drafts from a prior workflow) |

**Cross-check against session-decisions-2026-05-12:** *not consulted in detail for stale-flag suppression — pipeline-manager should re-verify before surfacing as Decisions.* The 2 recent drafts are tied to Kay's own forwards from her personal Gmail (kaycschneider) routing through her G&B inbox and likely represent in-flight personal-side follow-ups, not unsent G&B replies.

## 4. Introductions Detected

None this run. (Jackson Niketas thank-you is a follow-up to an existing relationship, not a warm intro.)

## 5. Niche Signals

- **Amazon FBA / Kitchen consumer goods** — Quiet Light single-listing BLAST (revenue $1.495M, earnings $478K, asking $1.16M, 32% net margin, 3 hr/week owner). Sub-niche signal only; Amazon FBA explicitly outside G&B buy-box (no inventory-heavy, no marketplace-dependent moats). Skip.
- **Pest management — Women's Forum** — NPMA promo for 2026 Women's Forum experiences. Reinforces pest-mgmt niche presence; PestWorld 2026 also reminded registration is open. Active niche — pipeline-manager already tracking.
- **Conference / exit planning** — XPX New York City Summer Networking Social promo. Relevant to existing relationship infra (XPX is where Kay met Andrew Lowis). Worth surfacing only if Kay has not RSVP'd; no extraction needed today.
- **AI / outbound infrastructure** — Frank Sondors / Salesforge newsletter; Amanda Lo Iacono / CounterA "We Are Live". Both tangential to G&B operations; no acquisition signal.

## 6. In-Person Meetings Today

| time (ET) | meeting | location | counterparty |
| --- | --- | --- | --- |
| 09:30-10:30 | CN: Meeting w/ Kay Schneider (G&B) | Empire State Building, 350 5th Ave Suite 7640, NY | Carlos Nieto @ Digital Capital Advisors (DCA) |
| 11:00-11:30 | Team TB | JJ | Kay (recurring internal) | Google Meet | [[entities/jj-tankoa\|JJ]], TB |

In-person Granola reminder applies to the 09:30 DCA meeting. Kay should have Granola running on phone or laptop for capture.

## 7. Broker BLAST Listings (per-deal extraction)

| source | headline | geo | revenue | ebitda | margin | industry | flag_reason | gmail_msg_id | listing_ordinal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ian Drogin, Quiet Light | Niche Amazon FBA Kitchen Brand — 5,000+ reviews, 4.6 stars, 32% net margin, 3 hrs/wk owner | undisclosed | $1,495,070 | $478,548 (Earnings) | 32% net | Amazon FBA / Kitchen consumer goods | single-listing-blast | `19e1d60c1d7e6c57` | 1 |

Flippa BLAST (msg `19e1d908945cf113`, 4 in-body listings) deliberately omitted — marketplace cattle-call, not broker channel per `feedback_marketplace_vs_broker_distinction`.

## 8. Auto-Drafts Created

None.

No inbound NDA or CIM attachments triggered the `<auto_ack_drafts>` pathway this run. Anthony's Management Report attachments are bookkeeper P&Ls (P&L PDFs + Balance Sheet), not CIM/NDA, and were routed through the dedicated bookkeeper P&L auto-trigger chain instead.

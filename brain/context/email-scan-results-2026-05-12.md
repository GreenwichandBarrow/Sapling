---
schema_version: "1.0.0"
date: 2026-05-12
type: email-scan-results
generated_by: email-intelligence
run_mode: headless-weekday
tags: ["date/2026-05-12", "email-scan", "automated"]
---

# Email Scan Results — 2026-05-12

Headless 7am ET fire. Gmail inbound + outbound + drafts scanned (newer_than:2d). Granola MCP unavailable (OAuth not refreshable in headless mode) — graceful-degraded per SKILL.md failure handling. No CIM, no NDA, no bookkeeper P&L, no broker-signal-keyword matches in inbound. One DIRECT investor-admin item routed to inbox.

## 1. Actionable Items Created

| Inbox file | urgency | entity | source_ref | confidence |
|---|---|---|---|---|
| `brain/inbox/2026-05-12-saltoun-annual-financial-review.md` | high | `[[entities/andrew-saltoun]]` | msg:19e191898ebc8ddc | high |

[[entities/janet-crockett]] (Controller at Saltoun, Andrew Saltoun's family office) sent annual financial review request — Citrin Cooperman accountants performing portfolio review. Pre-populated G&B investment figures as of year-end 12/31/2025; Kay needs to confirm or correct. Same cadence as last year. Janet entity stub created.

## 2. Deal Flow Classified

| Class | Count | Notes |
|---|---|---|
| DIRECT | 3 | Janet Crockett @ saltouncapital.com (investor admin); Hannah Barrett @ pacificlake.com (Mid-Search Summit logistics — Kay already replied 5/11, loop-closed); Barrie Green internal calendar conflict alert (older auto from 5/6) |
| BLAST | 1 | Tory @ Flippa (marketplace promo — per `feedback_marketplace_vs_broker_distinction` Flippa is marketplace cattle-call, NOT broker channel) |
| NEWSLETTER | 11 | Mimecast DMARC report, Axios AM, HBR, Axios Finish Line, Helen Guo SMB Deal Hunter (case-study newsletter format, not for-sale listing), 1Password, Axios PM, PestWorld 2026 registration promo, Carlos Nieto Visbal @ risebuildings.com (Empire State Building visitor invite — auto-notification), Cornell alumni, Andrew Lowis @ axial.net (older thread surfaced in 2d query) |

No broker-signal keywords ("for sale", "exclusive listing", "asking price", "we represent", "new listing", "now available", "teaser") matched in any inbound body — Section 7 per-listing extraction not triggered.

## 3. Draft Status

8 Gmail drafts present, all aged > 48 hours (oldest from 2026-02-21, newest from 2026-03-02). All long-stale, none from any active workflow this week. No drafts from the last 2 days. Cross-checked against `session-decisions-2026-05-10.md`: no SENT/DELETED entries for these draft IDs. Carryover known-stale pile — surface to triage only if Kay asks.

| Draft ID prefix | Approx created (UTC) | Age |
|---|---|---|
| r989550462937595579 | 2026-03-02 16:07 | ~71 days |
| r-5013177138505427051 | 2026-02-21 20:10 | ~80 days |
| r-2787224895918893720 | 2026-02-21 20:04 | ~80 days |
| r-5225012692018162578 | 2026-02-21 20:03 | ~80 days |
| r1586280898950821814 | 2026-02-21 20:02 | ~80 days |
| r-8150415091260429779 | 2026-02-21 20:01 | ~80 days |
| r-4571119820160089244 | 2026-02-21 20:00 | ~80 days |
| r8922907573534439329 | 2026-02-21 19:59 | ~80 days |

## 4. Introductions Detected

None.

## 5. Niche Signals

- **PestWorld 2026 registration open** (NPMA, npma@npmapestworld.org) — pest mgmt niche cadence. Active niche per `project_kay_lifestyle_dress_filter` (NJPMA preppy-casual norms). Surface to conference-discovery for conference pipeline append decision.
- **Flippa promo** mentions Test Prep App / SocMed SaaS / Connected Lifestyle Brand / card game store / family gift brand / education app — all OUT of G&B buy-box (consumer / digital / education — not services + tristate). No-action.
- **Helen Guo SMB Deal Hunter** profiled a $1.38M business buyer (case study, not for-sale listing). Continued evidence that searcher-as-buyer marketplace channel is saturated — informs `feedback_searcher_overlap`.

## 6. In-Person Meetings Today

For Granola pre-meeting reminders (Granola MCP unavailable this run — see Actionable Items section, will retry next fire):

| Time (ET) | Event | Location | In-person |
|---|---|---|---|
| 09:30–10:00 | Coffee w/ Robe | TBD | yes (coffee context) |
| 12:00–12:30 | Jackson Niketas — AI Coaching Discussion | Google Meet | no (virtual) |
| 17:00–19:00 | Women Shaping the Art World | 14 Harrison St, NYC | yes |

Also passive: Carlos Nieto Visbal sent an Empire State Building (350 Fifth Ave) visitor invite at 13:53 ET on 5/11 — likely tied to an upcoming Kay visit (not on today's calendar). Surface to pipeline-manager for cross-check against this week's meetings.

## 7. Broker BLAST Listings (per-deal extraction)

None.

No inbound BLAST this run matched broker-signal keywords ("for sale", "exclusive listing", "asking price", "we represent", "new listing", "now available", "teaser", "project [codename]"). Tory @ Flippa promo is marketplace-channel per `feedback_marketplace_vs_broker_distinction` and Helen Guo is newsletter case-study format — neither triggers per-listing extraction.

## 8. Auto-Drafts Created

None.

No inbound NDA-like or CIM-like PDF attachments this run. No auto-acknowledgment drafts fired via `<auto_ack_drafts>`.

## Actionable Items (system-level)

- **Granola MCP OAuth requires re-auth** — `mcp__granola__authenticate` surfaced as the only available tool; headless run cannot complete the PKCE callback. No Granola meetings ingested this fire; if any calls happened since last successful poll, they remain queued in Granola's side. Re-auth on next interactive session. Pattern: `project_granola_mcp_shape.md` + `feedback_granola_mcp_same_session_pkce.md`.
- **No bookkeeper P&L trigger fired this run.** Anthony's monthly Management Report typically lands end-of-month; March 2026 report still the most recent (filed 2026-04-29 per session-decisions log). April 2026 P&L not yet received. No `BOOKKEEPER-PL-CHAIN:` marker emitted — validator should pass on absence-of-trigger.
- **Attio writes skipped** — no CIM, no NDA, no Active Deal stage-3-9 match this run. No Attio mutations.

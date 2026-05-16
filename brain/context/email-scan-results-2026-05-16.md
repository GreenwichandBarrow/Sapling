---
schema_version: 1.1.0
date: 2026-05-16
type: output
output_type: email-scan-results
status: done
people: ["[[entities/kay-schneider]]", "[[entities/krupa-shah]]", "[[entities/ninad-singh]]", "[[entities/brad-buser]]", "[[entities/harrison-wells]]"]
companies: ["[[entities/greenwich-and-barrow]]", "[[entities/stream-capital-partners]]", "[[entities/aspect-investors]]"]
tags: ["date/2026-05-16", "output", "output/email-scan-results", "client/greenwich-and-barrow", "status/done", "person/kay-schneider", "person/krupa-shah", "person/ninad-singh", "person/brad-buser", "company/greenwich-and-barrow", "company/stream-capital-partners", "topic/email-intelligence", "source/gmail", "source/granola"]
---

# Email Scan Results — 2026-05-16 (Saturday)

Scan window: `newer_than:2d` inbound + outbound Gmail, Gmail drafts, Granola since 2026-05-14. No active-session-only sources trusted. Cross-checked `brain/context/session-decisions-2026-05-12.md` (most recent).

---

## 1. Actionable Items Created

- **Granola call note created:** `brain/calls/2026-05-14-krupa-shah-stream-capital.md` — ACG NY Women of Leadership Summit 1:1 with [[entities/krupa-shah|Krupa Shah]] ([[entities/stream-capital-partners|STREAM Capital Partners]]). Source ref: Granola note `not_TkppcODRRcTIly`. Action items embedded (Kay to send AI consultant contact, set quarterly real-estate-deal check-ins, learn about Krupa's mgmt conference; Krupa to route real-estate-component deal flow to Kay).

No inbox items created — no CIM / NDA / LOI / financials / Bookkeeper-P&L detected this run.

---

## 2. Deal Flow Classified

| Class | Count | Items |
|---|---|---|
| DIRECT | 4 | Ninad Singh (Beaconsfield Growth — peer, push call out 1 week); Harrison Wells x3 (AI coaching / server setup — internal advisor); Barrie Green (internal calendar-conflict alert); Anthony Bacagan (Start Virtual EOW report — internal vendor) |
| BLAST | 0 | None |
| NEWSLETTER | 4 | Beacon/Anacapa (AI Friday recap); NPMA Events (Women's Forum); Austin Petersmith/Howie (product update); — promotional/subscription |
| Personal/self-fwd | 3 | Kay fwd "Greenwich & Barrow / Aspect" (Brad Buser investor check-in — ALREADY REPLIED 5/13); Kay outbound "Re: Reconnecting on search fund raise experience"; Kay screenshot self-send |

Total inbound threads scanned: 11. No broker BLASTs, no broker-signal keyword bodies.

---

## 3. Draft Status

| Draft | To | Subject | Age | Status |
|---|---|---|---|---|
| r2253803435468898722 | jeanne@villagesearchpartners.com | Re: Touch Base | 4 days (5/12) | UNSENT — DRAFTED 5/12 per session-decisions (Jeanne Wang / Village Search Partners Coalition breakfast decline). Approved as draft; Kay sends herself. |
| 8 drafts (Feb 21 2026 / Mar 2 2026) | — | "Thank you", "Reply to Introduction", "Introduction to Broker", "Introduction to Lender", "Follow Up to Intermediary", etc. | n/a | CANONICAL EMAIL TEMPLATES — Kay's standing reusable scaffolds. NOT pending outreach. Excluded from staleness flagging. |

No drafts created by automation this run. Brad Buser/Aspect reply: DRAFTED 5/12, Kay SENT her own version 5/13 (confirmed in thread) — loop CLOSED, not surfaced.

---

## 4. Introductions Detected

None. Ninad Singh is an existing peer relationship (prior calls/met); Krupa Shah met in person at ACG (call note created, not a new email intro). No new warm introductions in email this window.

---

## 5. Niche Signals

- **Pest control:** NPMA "2026 Women's Forum — Know Before You Go" — Kay registered/attending (Women in Pest Mgmt week of 5/18 per session-decisions). Reinforces active pest niche + women-network priority.
- **Searcher/peer landscape (Granola, Krupa Shah):** LMM searchers actively dropping software (AI disruption) and avoiding California; convergence on digital services + industrials. Real-estate-component deals (sale-leaseback bridge) flagged as a structuring lever. Krupa offered reciprocal deal flow on real-estate-owning targets.
- **ETA ecosystem:** Ninad Singh (Beaconsfield Growth Partners) early-campaign, 0% first-email response — peer data point on cold-email decay.

---

## 6. In-Person Meetings Today

None. No calendar events on 2026-05-16 (Saturday). No Granola reminder needed.

---

## 7. Broker BLAST Listings (per-deal extraction)

None. No broker BLAST or broker-signal-keyword email landed in the scan window.

---

## 8. Auto-Drafts Created

None. No inbound email carried an NDA-like or CIM-like attachment, so the auto-acknowledgment trigger did not fire. No auto-ack Gmail drafts created.

---

## Side-Effect Triggers — Status

- **CIM auto-trigger:** NOT fired (no CIM attachment / no >5pg PDF with financials).
- **Active Deal Fast-Path:** NOT fired (no inbound matched an Active Deals stage 3-9 entry).
- **Bookkeeper P&L auto-trigger:** NOT fired. Anthony Bacagan (startvirtual.com) email is an "End Of Week Report" (accomplishments narrative, no attachments) — NOT a monthly "Management Report" with P&L/Balance Sheet PDFs. Trigger conditions not met. `BOOKKEEPER-PL-CHAIN` marker intentionally not emitted (no detection this run).
- **Auto-ack drafts:** NOT fired (no NDA/CIM attachment).

## Granola Ingestion Summary

7 Granola notes since 2026-05-14. Disposition:
- `not_U1ou7lmFRtIFtH` AI Friday — already in `brain/calls/2026-05-15-ai-friday-automating-business-ops.md` (idempotent skip)
- `not_f6APj5PQS9UqEk` Harrison <> Kay AI Coaching — already in `brain/calls/2026-05-15-harrison-wells-coaching-session.md` (idempotent skip)
- `not_TkppcODRRcTIly` ACG 1:1 Krupa Shah — **call note CREATED** (substantive peer/co-invest meeting)
- `not_JcRDEjx4sCqEnF` / `not_a28XxDqYhJlp8q` / `not_aRQ6m737SNOg0t` / `not_EfdPMln30QjYZK` — ACG NY Summit panels/workshops/summit overview (passive conference content) → niche signals only (Section 5), no individual call notes per skill scope.

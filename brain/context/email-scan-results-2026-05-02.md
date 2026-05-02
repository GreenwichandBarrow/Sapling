---
date: 2026-05-02
type: email-scan-results
schema_version: 1.0.0
generated_by: email-intelligence
day_of_week: Saturday
window_hours: 48
inbound_count: 21
outbound_count: 8
draft_count: 8
tags:
  - date/2026-05-02
  - email-scan
  - source/gmail
---

# Email Scan Results — 2026-05-02 (Saturday)

Window: `newer_than:2d` (2026-04-30 → 2026-05-02 morning)
Source: Gmail via `gog gmail` CLI (Superhuman sunset 4/29)

## 1. Actionable Items Created

**None.** No new inbox items created. No CIM, NDA, LOI, or active-deal documents detected. No P&L Management Report (April P&L not yet sent — Anthony's 5/2 EOW is a routine status update, not the monthly Management Report).

## 2. Deal Flow Classified

**Counts:** DIRECT: 4 | BLAST: 0 | NEWSLETTER: 7 | TRANSACTIONAL/SYSTEM: 10

### DIRECT (4)

1. **[[entities/bob-williamson]] (Cetane Associates)** — 2026-04-30 12:30. Subject: "NJPMA Business Management workshop." Post-NJPMA-workshop follow-up offering free Value Range Analysis (VRA). Attachment: `Value Range Analysis - Bugo Pest Remover_v2.pdf` (sample VRA, 69.6 KB). **Classification: sell-side prospecting** per `feedback_free_valuation_equals_sell_side` — Bob is a sell-side M&A advisor (Cetane Pest & Lawn Director), free VRA = lead-magnet for sell-side engagement. **Wrong layer for buy-side intent.** Surface to pipeline-manager: do not engage as a deal-source; record as a contact in the pest network only if useful for ecosystem mapping.

2. **[[entities/anthony-bacagan]] (StartVirtual)** — 2026-05-02 04:21. Subject: "Re: Start Virtual - End Of Week Report: Greenwich & Barrow." Routine weekly status update (transactions recorded, bank rec done, book review, sent Management Report + Excel). **NOT a P&L auto-trigger** — separate from monthly Management Report cadence. April Management Report has not yet arrived (March was filed 4/29). No action needed.

3. **[[entities/abower-njpma]] (NJPMA — Adam Bower)** — 2026-04-30 12:09. Subject: "**THANK YOU TO OUR ATTENDEES**." Generic thank-you to NJPMA workshop attendees. Per `feedback_post_conference_replies_reactive_only` — silent thank-you, no reply needed.

4. **[[entities/andrew-lowis]] (Axial)** — 2026-04-30 17:30. Thread: "Nice meeting you at XPX yesterday." Andrew sent the Axial member-firm form link; Kay replied "Great will do, thank you!" 2026-04-30 17:30. Open loop: Kay still needs to **fill out the Axial form** (`https://www.axial.net/request-information?utm_campaign=navbar-join`). Surface to pipeline-manager as 🟡 this-week task — Andrew is connecting Kay to an Axial colleague who works with search funds, and the form gates the intro.

### NEWSLETTER (7) — niche signals only

- Mike Allen (Axios PM) — travel, no niche signal
- Grant Hensel (This Week in ETA) — Pre-LOI Seller Relationships piece (signal: ETA community continues focus on pre-LOI relationship building per `feedback_buyer_fingerprint_first` doctrine)
- Peter Lang (Digital Agency Business) — outbound copy newsletter (signal: aligned with `reference_ai_friday_outbound_principles` two-stage scoring)
- Frank Sondors (Salesforge) — AI sales tooling, no niche signal
- Mitchell Baldridge — tax/wealth planning, no niche signal
- Frieze VIP — art fair invite (Kay's mom-network art space, no acquisition signal)
- Attio Changelog — product update (current platform)

### TRANSACTIONAL / SYSTEM (10)

DMARC reports (Google, Microsoft) ×2; Stripe receipts (StartVirtual, Art Newspaper) ×2; Gusto April 2026 invoice paid; Stripe direct debit confirmation for Dodo Digital (Harrison Wells coaching, monthly); ACG NY portal access link (1-1 Meetings registration confirmation for 5/14 — already wired into Conference Pipeline); Anthony Client Connect & Learn Recap (BLAST to all StartVirtual clients, undisclosed-recipients); Harrison Wells engagement scope/invoice (Kay confirmed payment 5/1); Harrison Wells server setup guide (thread closed).

## 3. Draft Status

**8 drafts in Gmail mailbox — all legacy stale, but NOT actionable outreach.**

All 8 drafts share message-IDs from the `19c81c...` and `19caf4...` ranges (October 2025 era). Inspection of `r989550462937595579` confirmed the pattern: empty `To:` field, generic "Introduction" subject, and body templated as the canonical "Hi (name)... I'll let you take it from here. Enjoy!" warm-intro snippet. These are template stubs from Kay's pre-Superhuman-sunset workflow — they're personal scaffolding, not pending outreach owed to anyone. No flag.

**No new drafts created in the 48h window.** Per `feedback_no_sunday_emails`, any reply drafts produced this weekend should be queued for Monday AM regardless.

**Cross-check vs `session-decisions-2026-05-01.md`:** All Friday email actions logged as SENT (Hallie Berk Candlewood ACG outreach) or DELETED (Bellizio row 6). No DRAFTED-but-unsent items from yesterday hanging.

## 4. Introductions Detected

**None.** No new "I'd like to introduce you" emails or CC-pattern intros in the window.

Open intro-in-progress (carried from yesterday, not new): [[entities/andrew-lowis]] is **mid-process** of intro'ing Kay to an Axial search-fund-focused colleague — gated on Kay completing the Axial member form. Tracked in section 1 / item #4 above.

## 5. Niche Signals

**Pest management** — [[entities/bob-williamson]] (Cetane) post-workshop outreach reinforces NJPMA = active sell-side prospecting hunting ground. His VRA sample is on a target ("Bugo Pest Remover") — useful artifact for understanding how Cetane positions valuation in the niche. File the sample VRA PDF if useful for buy-side reference, but do not engage Bob as a deal-source per the free-valuation-equals-sell-side memory.

**Search-fund ecosystem (Axial)** — [[entities/andrew-lowis]] willing to connect Kay to an Axial colleague who works with search funds. Live warm-intro path. Continues the post-XPX network thread.

**ETA community** — Grant Hensel newsletter on Pre-LOI Seller Relationships aligns with `feedback_buyer_fingerprint_first` and Kristin Wihera's debrief lessons (`project_g_b_doctrine_kristin_lessons`) — relationship-building beats process-engineering pre-LOI.

## 6. In-Person Meetings Today

**None.** Calendar `2026-05-02` returns zero events. No Granola transcripts to ingest (Granola MCP tools not available in this environment — `mcp__granola__list_meetings` not registered).

---

## Validator Notes

- All 6 required sections present.
- File non-empty.
- Counts: inbound 21 (4 DIRECT + 7 NEWSLETTER + 10 SYSTEM), outbound 8, drafts 8 (all legacy stubs, no flag).
- No urgent auto-triggers fired. No CIM, NDA, LOI, Active Deal Fast-Path, or Bookkeeper P&L detected.
- No Granola meetings ingested (tool unavailable).
- No new entity stubs created (all referenced entities exist or are conference-context).

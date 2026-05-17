---
date: 2026-05-17
type: context
title: "Email Scan Results — 2026-05-17 (Sunday)"
tags:
  - date/2026-05-17
  - context
  - topic/email-scan
  - topic/email-intelligence
  - source/gmail
  - source/granola
  - status/done
---

# Email Scan Results — 2026-05-17

Sunday scan. Window: `newer_than:2d` (inbound + outbound). gog unlocked via op-sa-token path (verified `op vault list` → "GB Server"). Granola via `granola-api` REST wrapper (MCP not OAuth-connected; wrapper is the sanctioned fallback per post-call-analyzer doctrine).

**Headline:** Quiet Sunday. No CIM/NDA/LOI/financials. No introductions. No active-deal documents. Bookkeeper P&L trigger evaluated and correctly did NOT fire. No items require Kay's same-day decision from this scan.

## 1. Actionable Items Created

None. No inbound email produced an inbox-worthy action item. Anthony's StartVirtual email is an End-Of-Week operational report (no financial documents) — does not meet the bookkeeper P&L trigger (see Section 5 / Niche & System Signals). Kay's four self-addressed reminder emails (from kaycschneider@gmail.com) are personal capture notes, not system-actionable; left for Kay's own triage.

## 2. Deal Flow Classified

21 inbound INBOX threads (newer_than:2d):

- **DIRECT (3):**
  - Harrison Wells <harrison@dododigital.ai> — "Ask Harrison login instructions" (2026-05-15). Advisor/coach onboarding info. Non-deal.
  - Barrie Green <barrie.g@greenwichandbarrow.com> — "Heads up: your calendar has upcoming conflicts" (2026-05-17). Internal system/scheduling alert.
  - Anthony James Balleras Bacagan <anthony.b@startvirtual.com> — "Re: Start Virtual - End Of Week Report: Greenwich & Barrow" (2026-05-15). Internal VA EOW report. **Not a bookkeeper P&L** (see Section 5).
- **Kay self-notes (4):** kaycschneider@gmail.com voice-memo-style reminders to self — "Circle back with Ima. Year in - talk to Paul Moffat", "Email later for intro at noma", "Email later to meet at moms", "Message Layne later to meet at conference". Personal capture; not inbound intros, not system actions.
- **NEWSLETTER (9):** Helen Guo SMB Deal Hunter "It's finally out!" (content/pitch, CATEGORY_UPDATES — not a per-listing broker blast), Acquiring Minds Webinars ×2, Axios AM (Mike Allen), Walker Deibel / Buy Then Build, The Art Business Conference, Cornell CTBN Forum, Beacon @ Anacapa Partners (AI Friday recap).
- **BLAST / transactional / admin (5):** Hungry Llama Square receipt, Merriweather Coffee Square receipt, CorpNet Compliance ("Action Required: Compliance Filings Due" — vendor dunning, not deal), National Pest Management Assn login/confirm ×2 (NPMA app account, conference follow-on), Google DMARC aggregate report.

No BLAST body matched broker-signal listing keywords → no per-listing extraction triggered (Section 7).

## 3. Draft Status

13 Gmail drafts total. Cross-checked against `brain/context/session-decisions-2026-05-16.md` (DEFERRED: "6 Gmail drafts → Kay reviews/sends personally").

- **4 drafts dated 2026-05-16 (NOT stale — intentionally pending Kay):** "Heels to Deals + circling back on Matt"; "Great meeting you at Heels to Deals" ×3. These are the Heels-to-Deals follow-ups (Deborah Chichester / Monica Chawla / Marsha Weiner) + Becky/Matt circle-back from the 5/16 session. <48h old AND explicitly deferred for Kay's personal send per `feedback_kay_handles_all_replies`. Not flagged.
- **1 draft dated 2026-05-12 "Re: Touch Base" (~5 days, >48h):** Not recorded as DRAFTED/SENT/DELETED in 5/16 or 5/15 session logs. **Genuinely stale — surfaced for Kay (low priority).**
- **8 drafts dated 2026-02-21 / 2026-03-02:** Standing canonical reply templates ("Introduction to Broker", "Reply to Introduction (with/no times)", "Follow Up to Intermediary", "Introduction to Lender / Capital Provider", etc.). Saved reference scaffolds, not action-pending outreach. Not flagged.

No drafts were sent or deleted by this skill (CREATE-only governance; this scan created none).

## 4. Introductions Detected

None. No inbound "I'd like to introduce" / forwarded-intro / new-CC-with-context patterns. (Kay's self-note "Email later for intro at noma" is her own outbound reminder, not an inbound warm intro — no entity/inbox action.)

## 5. Niche Signals

- **Bookkeeper P&L trigger — evaluated, did NOT fire (correct).** Anthony @ startvirtual.com email is subject "Re: Start Virtual - End Of Week Report" with **zero attachments** (`has:attachment` count = 0). Per `feedback_bookkeeper_pl_auto_trigger_budget_manager`, the trigger is scoped to monthly "Management Report" / "Profit and Loss" / "Balance Sheet" content or matching PDF attachments — an EOW operational status reply is none of these. budget-manager NOT invoked. No `BOOKKEEPER-PL-CHAIN:` marker (no detection this run, by design).
- **NPMA app activity** (login/email-confirm ×2) — residual from pest-management conference engagement; no new niche signal, account housekeeping only.
- No substantive industry/niche observations in inbound newsletters this window worth carrying to pipeline-manager.

## 6. In-Person Meetings Today

None. Calendar 2026-05-17 returned 0 events (Sunday). No Granola pre-meeting reminder needed.

## 7. Broker BLAST Listings (per-deal extraction)

None. No inbound email this window was a broker BLAST containing listing-signal keywords ("for sale", "asking price", "we represent", "new listing", "now available", "teaser", "project [codename]"). Helen Guo SMB Deal Hunter "It's finally out!" is a content/newsletter email (CATEGORY_UPDATES, AI/Pitch label) with no per-listing deal body — not decomposable into listing rows.

## 8. Auto-Drafts Created

None. No inbound email carried an NDA-like or CIM-like attachment, so `<auto_ack_drafts>` did not trigger. No acknowledgment drafts created.

---

### Granola Ingestion (idempotency confirmed)

`granola-api since 2026-05-15` returned 2 notes, both already ingested:
- `not_U1ou7lmFRtIFtH` "AI Friday: Automating Everyday Business Operations with Claude" → `brain/calls/2026-05-15-ai-friday-automating-business-ops.md` (exists)
- `not_f6APj5PQS9UqEk` "Harrison <> Kay: AI Coaching Session" → `brain/calls/2026-05-15-harrison-wells-coaching-session.md` (exists)

No new transcripts since the 5/16 email-intelligence run. 0 call notes written this run (correct — duplicates skipped per idempotency rule).

### Outbound (from:kay.s@greenwichandbarrow.com newer_than:2d) — 7 sent

- 2026-05-17 11:36 "Re: Follow up from the ETA Breakfast" — Kay-sent reply.
- 2026-05-16 12:59 "Heels to Deals + circling back on Matt"
- 2026-05-16 12:38 "Great meeting you at Heels to Deals" ×3
- 2026-05-16 12:21 "Re: Reconnecting on search fund raise experience"
- 2026-05-16 11:44 "Your receipt from Granola #2551-3150" (system receipt — Granola billing, not outreach)

Kay sent the Heels-to-Deals batch + ETA Breakfast follow-up + search-fund-raise reply herself on 5/16–5/17 (consistent with the 5/16 session "Kay sends every reply herself" pattern). No active-deal-pipeline cadence updates warranted (none addressed to a stage-3-9 Active Deals target). relationship-manager / pipeline-manager own any nurture-cadence consequence.

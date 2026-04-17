---
date: 2026-04-20
type: context
title: "Tomorrow Pins — 2026-04-20 (Monday)"
saved_at: 2026-04-17T13:00:00Z
tags: ["date/2026-04-20", "context", "topic/pins"]
---

## Monday priority — resume Q1 FY2026 investor update prep

Kay set Fri 4/17 aside to get to inbox zero, deal flow, and Fri review skills. Q1 prep is paused until Mon 4/20.

### State as of Fri 4/17 end-of-day
- **Data collector (Sub-Agent 1) ran 4/17 afternoon.** Output: `brain/context/q1-2026-mulling-pack.md` (Q1 metrics, pipeline, niches, calls, strategic pivots, Q4 narrative frame, gaps).
- **Rollout decisions locked 4/17:**
  - Option B — proactive (send deck + embed scheduling ask in same email)
  - Formal prep for ALL 12 investors including Clayton (no in-office-only catch-up)
  - Q4 2025 narrative architecture is the frame for Q1 2026
  - Q1 numbers will be "sad again" (DealsX launches 5/7, same day Q1 due) — frame as infrastructure-heavy quarter
- **Q4 2025 deck flag:** sitting in DRAFTS folder (file `107WA9cpc2aAPKvJd593byF-R0H4ab7e1YlZkW63XYS8`), never moved to QUARTERLIES SENT. Verify whether it was actually sent to investors on/around 2/7/26.

### Open decisions needed before narrative v1 (Fri 4/24)
1. Guillermo Apr 22 bi-weekly — use slot for Q1 preview + plant sourcing question early, OR keep clean and include in batch?
2. Investor Ask on Slide 1 = the sourcing question (Q1 from `investor-standing-questions.md`)? Yes/no.
3. Budget/runway numbers — Kay to provide or flag for budget-manager pull (depends on what gaps the mulling pack surfaces).

### Cadence going forward
- **Fri 4/24 check-in:** Kay shares mulling direction; Claude drafts narrative v1.
- **Fri 5/01 check-in:** Narrative v2 + deck build + 12 scheduling emails drafted.
- **Target ship: Wed May 6** (1 day early vs. May 7 due date).

### Sourcing-question standing file
`brain/context/investor-standing-questions.md` Q1 auto-pulls into every investor prep until retired. Clayton, Steuart Botchford + Sam Hyde, and BK Growth (Bressman/King) are top 3 highest-probability targets per 4/17 cap-table research.

## Carry-forward loops from 4/17 (for Monday briefing)

- Katie Walker thank-you — draft approved 4/17 by Kay for her own Superhuman paste. Status: Kay handling personally. Confirm sent.
- 4 ACG LinkedIn DMs — still pending Kay copy-paste to LinkedIn.
- Barrie AI calendar conflict question (Apr 22 Guillermo vs WSN) — 2 pref questions still open.
- Conference Pipeline picks — 4/20 Art Lawyering Bootcamp, 4/21 ACG Family Office, 4/22 EPCNYC (evening → skip). Decision needed early in week.
- Philip Hoffman warm intro — **14+ days aging**, RED. Kill / do now / re-defer with trigger?
- Mark Gardella reply — **10+ days aging**, RED. Draft / kill / defer with trigger?
- Calibration 4/16 proposals — 12 items still pending bulk/cherry-pick approval.
- 3 overdue Chanel contacts: Ashlee Walter, Robert DiMartini, David Wolkoff.

## Today's agenda (Friday 4/17 remainder)
1. Inbox zero (triage skill active)
2. Deal flow items (2 Synergy BB carried deals + whatever surfaces)
3. Review Fri artifacts: weekly-tracker, health-monitor, calibration proposals

## Pipeline-manager hardening — CRITICAL before May 7 DealsX launch

The Project Restoration deal (EQA, 3/19-4/17) exposed that pipeline-manager's **CIM Auto-Trigger did NOT fire** on 3/20 when the CIM arrived. Specifically, all four of these failed silently:

1. No ACTIVE DEALS Drive folder was created for Project Restoration (CIM/ subfolder, FINANCIALS/, LEGAL/, etc.)
2. No inbox item was written to `brain/inbox/` with `urgency: critical` and `topic/cim-received` tag
3. No `#active-deals` Slack notification fired (NDA Executed OR CIM Received)
4. Stage-progression tracking jumped Identified → Closed / Not Proceeding on 3/26 without recording intermediate NDA Signed (3/20) and Financials Received (3/20) stages

Attio entry exists but lacks the audit trail. Kay had to manually request this be recorded on 4/17. An audit note has been added to the Attio list entry (entry_id `15b11bdf-09f7-490f-b303-b59cb176e774`) documenting the real timeline.

**Fix required before May 7:**
- Verify email-intelligence CIM detection logic (CIM in email attachment + PDF > 5 pages + "Confidential Information Memorandum" keyword match)
- Verify pipeline-manager Phase 1 CIM Auto-Trigger actually executes its 4 automated steps
- Verify Slack webhook `$SLACK_WEBHOOK_ACTIVE_DEALS` is alive and firing
- Verify stage progression recording captures NDA Signed → Financials Received intermediate stages, not just final state
- Add regression test: manually replay Project Restoration scenario, confirm all 4 triggers fire correctly

Trace written at `brain/traces/2026-04-17-pipeline-manager-cim-trigger-gap.md`.

## Health flags still open
- gog calendar CLI 404s (persistent since 4/16)
- Superhuman MCP not authenticated (2 days)
- Payoneer/bank AWS (since 4/14)
- Orphaned entities 22 → 46 (knowledge graph degrading)
- Granola Conwell miss pattern

## Mon/Tue external meetings (manual preview — CLI broken)
- **Mon 4/20:** C-suite Week 1 kickoff (CIO + CFO agent refactor) — internal
- **Tue 4/21:** Guillermo Lavergne bi-weekly — moved to Apr 22 per 4/16 reschedule

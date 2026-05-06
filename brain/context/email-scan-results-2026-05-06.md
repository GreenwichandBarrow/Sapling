---
date: 2026-05-06
type: context
title: "Email Scan Results — 2026-05-06"
tags: ["date/2026-05-06", "context", "topic/email-scan-results", "topic/morning-workflow"]
schema_version: 1.1.0
---

# Email Scan Results — 2026-05-06 (Wednesday)

Skill: email-intelligence
Inbound scan window: `newer_than:2d label:INBOX` (50 max)
Outbound scan window: `from:kay.s@greenwichandbarrow.com newer_than:2d`
Cross-reference: `brain/context/session-decisions-2026-05-05.md`

---

## 1. Actionable Items Created

None. No CIM/NDA/LOI/financials attachments landed in the 2-day window. Eric Carter close-the-loop and Ninad Singh reschedule are surfaced for pipeline-manager via Section 4 / Decisions logic (already DEFER'd in session-decisions-2026-05-05) — no new inbox files written.

---

## 2. Deal Flow Classified

**Total inbound threads scanned:** 17

| Class | Count | Senders |
|-------|-------|---------|
| DIRECT | 5 | Jackson Niketas (Terra Mar Search) — AI coaching scheduling. Ninad Singh (Beaconsfield) — Re: push the call by 1 week. Eric Carter (Cohort Peak) — "last note" close-the-loop. Allison Allen (NPMA / pestworld.org) — Women's Forum first-timer welcome. Payal Keshvani (Taft) — Taft Dinner May 14 invitation (TO line is internal Taft attorney; functionally a BCC list to WOL attendees, but personalized salutation absent — borderline BLAST/DIRECT, classified DIRECT given handcrafted invite tone). |
| BLAST | 5 | Everingham & Kerr — single-listing broker BLAST, Healthcare SaaS / Reg-Compliance, $700K rev (mailjet bulk infra). Will Bressman (BK Growth) — concert-ticket giveaway to one-hanover@googlegroups.com (group blast, non-deal). NPMA Events — Women's Forum push reminder. CorpNet — compliance filings reminder. Athena Simpson (Acquimatch) — MatchMaker Pro free Buyer Profile pitch. |
| NEWSLETTER | 6 | Axios AM. Axial Top Deals Q1 2026. Gabriella @ Wealth Management — managed-services webinar. XPX NYC (May 28). XPX CT (May 28). XPX NJ (May 13). GJ King — BK Growth 1st-Thursday Zoom recap (no deal content; Jay Davis + Caroline DiMatteo from Nashton). |

**Notes:**
- E&K BLAST contains broker-signal keywords ("retained to arrange the sale", confidentiality agreement link) → triggers per-listing extraction → see Section 7.
- Will Bressman email is a peer-network giveaway, not a deal blast. No broker-signal keywords. Skipped from Section 7.
- Athena Simpson is acquirer-side platform marketing, not a broker BLAST. No Section 7 row.

---

## 3. Draft Status

| Draft ID | Subject | To | Age | Status | Action |
|----------|---------|----|----|--------|--------|
| `r-7216983259268091776` | Tomorrow's call — could we push to 10:30 ET? | andrew.lowis@axial.net | ~22h | Pending Kay's send | DRAFTED 2026-05-05 per session-decisions; surface in pipeline-manager only if still unsent by mid-morning. **Note:** Andrew has not replied — Kay's last outbound on the parent thread was 5/5 19:14 ET. |

8 historical drafts dated 2025 (IDs `r989550462937595579` through `r8922907573534439329`) are pre-sunset Superhuman residue, not generated this cycle. Suppressed (already aged out — none reference live deals).

**Cross-reference of session-decisions-2026-05-05:** No drafts in DELETED state. Andrew Lowis draft is the only DRAFTED+pending item. No "stale" flag warranted.

---

## 4. Introductions Detected

None. No "I'd like to introduce" / "thought you two should connect" / new-CC patterns in the 2-day window.

**Adjacent signal (not an intro):** Allison Allen (NPMA) offered to connect Kay with PWIPM (Professional Women in Pest Management) Council members ahead of Women's Forum. That's an *opt-in offer*, not a triggered intro — Kay can reply to activate. Surface to pipeline-manager as a 🟡 Decision (women-network-priority lens applies).

---

## 5. Niche Signals

- **Pest management (Active-Outreach):** Allison Allen (NPMA) Women's Forum first-timer welcome + offer of PWIPM connections. Reinforces women-led-network angle for pest mgmt vertical (per `feedback_women_network_priority`). NPMA Events reminder also landed (registration push, no new info).
- **Healthcare / Regulatory Compliance SaaS:** E&K listing — $700K rev, virtual, 1,500+ healthcare facilities. Below G&B $2M EBITDA floor (`feedback_deal_screen_300k_salary_15pct_margin`). Niche signal only — no acquisition action.
- **AI-coaching / search-fund advisory:** Jackson Niketas (Terra Mar) wants Kay's testimonial on Harrison Wells's coaching program. Not a niche signal for G&B; relationship/network signal only.
- **ETA / search-fund peer ecosystem:** GJ King BK Growth Zoom featured Jay Davis + Caroline DiMatteo from Nashton talking inorganic-growth strategy + industry-attractiveness criteria. Recap-only; Kay attended live.
- **Wealth management / trust services:** Gabriella @ Wealth Mgmt Black-Diamond webinar (managed services). Not in Active-Outreach. No action.
- **M&A advisory ecosystem (XPX):** 3 invites landed (NYC 5/28, CT 5/28, NJ 5/13). XPX is the same network where Kay met Andrew Lowis (Axial) on 5/4. XPX New Jersey 5/13 conflicts with Guillermo bi-weekly (proposed Wed 5/13 10 AM ET). Surface to pipeline-manager as scheduling note.

---

## 6. In-Person Meetings Today

Today (Wed 2026-05-06) — calendar pulls:
- 09:30 ET — Coffee w/ Robe (recurring; brief-exempt per `feedback_robe_no_briefs`)
- 10:00 ET — Axial: Andrew & Kay (Axial.net, 3 attendees) — pending Andrew's reply on 10:30 reschedule (draft `r-7216983259268091776`)
- 11:00 ET — How to use Clay + Claude Code to GTM (self-block / training, no external attendees)
- 13:30 ET — Guillermo I Kay Bi-Weekly Mtg (2 attendees) — Kay proposed Tue 5/12 1:30 PM ET / Wed 5/13 10 AM ET reschedule per session-decisions; awaiting her pick

**No truly external in-person meetings today** — all video. Granola pre-meeting reminders not needed.

---

## 7. Broker BLAST Listings (per-deal extraction)

| source | headline | geo | revenue | ebitda | margin | industry | flag_reason | gmail_msg_id | listing_ordinal |
|--------|----------|-----|---------|--------|--------|----------|-------------|---------------|------------------|
| Everingham & Kerr (admin1@everkerr.com) | Cloud-Based SaaS Healthcare / Regulatory Compliance Software Company — Environment of Care Automation, served 1,500+ healthcare facilities, also temperature monitoring (aerospace adjacent) | undisclosed (virtual / remote) | $700K (mostly recurring) | undisclosed | undisclosed | Healthcare SaaS / Regulatory Compliance Software | single-listing-blast | 19dfa04e841fe261 | 1 |

Below G&B $2M EBITDA floor; surface to pipeline-manager as KILLED-by-floor not actionable.

---

## 8. Auto-Drafts Created

None. No inbound NDA-like or CIM-like PDF attachment landed in the 2-day window.

**Note:** E&K listing email referenced a confidentiality agreement via download LINK (`https://www.everkerr.com/wp-content/uploads/2026/03/3475V-Confidentiality-Agreement_CBSH.pdf`) but did NOT attach the PDF. Auto-ack trigger requires an actual PDF attachment per `<auto_ack_drafts>` rule. No draft created. (Even if a draft fired, the deal is below floor — no commercial reason to acknowledge.)

---

## Skill Health

- Gmail inbound + outbound + draft-list: scanned cleanly via gog CLI.
- Calendar: pulled via `gog calendar events --today --json`.
- Granola MCP: server connected (per `claude mcp list`) but tool schemas not loaded into agent harness this session — **0 meeting transcripts ingested this run**. No new `brain/calls/` files written. Idempotency check: latest call note is `2026-04-30-team-tb-jj-kay.md`; nothing has been ingested since 4/30. If Kay had Granola-recorded sessions Mon-Tue, that backlog is unprocessed (would need a session with `mcp__granola__*` tools loaded).
- No CIM auto-trigger fired. No Active Deal Fast-Path fired. No bookkeeper P&L trigger.
- Session-decisions cross-reference clean: 5 DEFER items from yesterday all consistent with today's mailbox state.

---

## Validation

- [x] File exists, non-empty
- [x] All 8 sections present
- [x] Each section populated or marked "None"
- [x] Section 7: every BLAST whose body matched broker-signal keywords (E&K only) has a row
- [x] Section 8: zero auto-drafts triggered, marked "None"

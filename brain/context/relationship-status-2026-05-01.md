---
date: 2026-05-01
type: relationship-status
---

> **Today is Friday.** Per `feedback_relationship_cadence_friday_only.md`, this section IS surfaced in today's morning briefing.

## Overdue Contacts (Top 5)

1. **Kristina Marcigliano (WTW)** — Quarterly, last contact 2025-12-23, **129 days since / 31 days overdue**. Next_action empty. Art-insurance broker (former Risk Strategies, now WTW Associate Director). Was already overdue last Friday (4/30 artifact); no contact since. Suggested action: short check-in email re art-insurance niche pipeline.
2. **Hunter Hartwell (Ellirock)** — Quarterly, last contact 2026-01-14, **107 days since / 9 days overdue**. Next_action empty. Suggested action: light check-in email; no urgent thread.
3. **Dan Tanzilli (Third Eye)** — Monthly, last contact 2026-03-26, **36 days since / 1 day overdue**. Art World relationship via Karaugh Brown intro. Strongest connection: Good. Suggested action: check-in email or coffee invite.

Only 3 surfaced. **Quarterly bucket review:** all other Quarterly contacts within 98-day window OR carry trigger-based next_action ("re-engage when insurance deal", "when art restoration deal of interest", etc.) and are correctly suppressed. **Occasionally bucket:** Lauren Young (326 days) is trigger-based ("re-engage when specific intro available") — suppressed per next_action rule. No other Occasionally contacts beyond 213-day threshold without trigger language.

**Caveat:** Gmail/calendar are the only verified channels for last_interaction. Text and phone interactions are not captured; surfaced contacts may already be live via those channels.

## Auto-Resolved (No Action Needed)

- **Andrew Lowis (Axial):** Replied 2026-04-30 17:30 to Axial colleague intro request. Thread now active (11 messages); not overdue. Awaiting Kay's read on the new reply — surfacing to email-intelligence, not relationship-manager.
- **Megan Lawlor (ML Capital):** Recurring meeting series active (calendar update 2026-04-28). Within Quarterly cadence; auto-resolved.
- **Kristina Marcigliano / Hunter Hartwell / Dan Tanzilli:** No outbound from `kay.s@greenwichandbarrow.com` in last 14 days. Surfaced above.
- **Yesterday's session sends (Hoffman LinkedIn DM, Ali Doswell reply, Andrew Lowis Axial intro, Transworld NY form):** Confirmed in `session-decisions-2026-04-30.md`. Hoffman + Andrew Lowis colleague intro both still in awaiting-reply state — Andrew Lowis personal reply landed (above), but the colleague intro is a separate outstanding loop.

## Pending Intros

- **Andrew Lowis → Axial colleague:** Sent 2026-04-30. Andrew personally replied today (5/1) but colleague reach-out is the actual deliverable — still outstanding from Andrew's side.
- **William Hoffman LinkedIn DM:** Sent 2026-04-30 via LinkedIn (not Gmail — would not show in email search). Reply window opens today; not yet overdue. No action needed unless he replies.
- No other intro promises in `next_action` fields. Kendall Warson → Amanda completed. Rachel → Zoe completed.

## Warm Intro Opportunities (from target-discovery)

- None new. No target-discovery handoff this run.

## Vault → Attio Syncs

- **Kristin Wihera** ([[entities/kristin-wihera]]) — vault entity has no `attio_synced_at`; Attio search for "Kristin Wihera" returns only Kristina Marcigliano + Kristina Baynes-Reid (different people). Person record does not yet exist in Attio. Sync deferred — auto-creation will fire on next email signal. Same state as 4/30 artifact.
- 5 other entities modified in last 7d are companies (saunders-street-capital, cfo-consulting-partners, helmsley-spear, axial, wiggin-and-dana), not person-type — outside this skill's sync scope.
- All other person entities synced from prior runs.

## Open Loops from Yesterday — Reply Status

| Thread | Status | Action |
|---|---|---|
| William Hoffman LinkedIn DM | No reply yet (LinkedIn, not Gmail-visible) | Wait — reply window opens today |
| Ali Doswell reply | SENT 4/30; thread closed | None |
| Andrew Lowis Axial intro | SENT 4/30; **Andrew replied 4/30 17:30** — colleague intro still pending Andrew's forward | Email-intelligence to surface his reply for Kay's read |
| Transworld NY form | SENT 4/30; awaiting broker assignment | None |
| Megan / Walker (Apollo job postings advice) | Recurring meeting active 4/28 update | None |
| Kristin Wihera (search-fund doctrine) | Debrief processed in `feedback_*` memories 4/30 | None — not an email loop |
| Jeff Stevens (monthly investor) | Last call 2026-04-22; next monthly cadence ~5/22 | None |
| Guillermo Lavergne (biweekly investor) | Last touch 2026-04-21 (call) + 2026-04-16 (calendar reschedule); next biweekly ~5/5 | None |
| Colin Woolway (advisor) | Occasionally cadence, last 2026-02-17 (74d) — within 213d window | None |
| Sam (DealsX) | Daily channel, no nurture surfacing | None |
| JJ | Daily ops, no nurture | None |

## Attio Dedup Needed

- None new today. Three "Kristina" results (Marcigliano @ WTW with kristina.marcigliano@wtwco.com, Marcigliano-CLCS unmapped, Baynes-Reid) are distinct individuals or unmapped duplicates carried over from 4/30 — no merge action needed by this skill.

## Metadata Drift

- None. No surfaced contact has `next_action` text conflicting with `nurture_cadence` field.

## System Status Alerts

- **Attio MCP:** Working (per-cadence-value filter pattern, batch fetch via record IDs). The `is_set`/`is_not_empty` 400-error workaround from 4/30 still in effect — keep per-value loop.
- **Gmail/calendar verified-only channels:** Restated as permanent caveat. Hoffman is the live example today — DM was via LinkedIn, intentionally invisible to this skill's email scan.
- **Friday-only surfacing rule:** Today is Friday. Pipeline-manager SHOULD include the Overdue Contacts section in this morning's briefing.

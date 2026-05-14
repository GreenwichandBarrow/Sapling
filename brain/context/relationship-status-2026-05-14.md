---
date: 2026-05-14
type: relationship-status
---

## Overdue Contacts (Top 5)

Thursday morning run. Gmail outbound probes covered BOTH aliases (`from:kay.s@greenwichandbarrow.com` + `from:admin@greenwichandbarrow.com`) for `newer_than:2d` and `newer_than:14d` per `feedback_kay_outbound_includes_admin_alias` (2026-05-12). Captured Kay-side outbound since the 2026-05-13 artifact: (1) Jackson Niketas thank-you reply 2026-05-12 20:15 (peer-searcher; new contact, no cadence assigned), (2) Barrie Green internal calendar-prep request 2026-05-13 21:16 (assistant routing, not cadence-tracked). No NEW substantive Kay → cadence-tracked-contact emails landed since yesterday's run.

After applying all suppression rules — action-already-taken, trigger-based, explicit PASS, within-cadence-commitment-drift, assistant-vs-principal, and off-system-closed (`feedback_off_system_resolution_closes_loop`) — one contact remains surfaceable:

1. **Sarah de Blasio** ([[entities/sarah-de-blasio]] — Chartwell, Industry Expert, Quarterly cadence) — last interaction 2026-01-23 (Gmail "Happy New Year" sent by Kay, `sdeblasio@chartwellins.com`). **111 days overdue against the 98-day Quarterly threshold (13 days past).** Carry-forward awareness from 2026-05-05.
   Suggested action: **outreach BLOCKED** pending the Goodwin finder's-fee doc on G&B letterhead. Once the doc lands, drafting moves to outreach-manager. Surface only as awareness today — do not draft.

**Net delta from 2026-05-13 artifact:** None. Sarah's day-count incremented +1 (110 → 111 days). No new overdue contacts entered or rolled in.

Caveat: Gmail and calendar are the only verified channels in this run. Texts, phone calls, in-person interactions, and LinkedIn-only outreach are not captured. If Kay has touched any contact via SMS/phone/LinkedIn/personal-email in the last quarter, treat as resolved.

## Auto-Resolved (No Action Needed)

Carry-forward from 2026-05-13 with ages incremented +1 day (Wed → Thu). **Ali Doswell rolls off the 14-day Gmail-verification window today** (15 days since 2026-04-30). Two new entries land from yesterday's activity: Jackson Niketas (thank-you exchange) and Carlos Nieto (first in-person meeting).

- **Jackson Niketas** ([[entities/jackson-niketas]] — Terra Mar Search, peer-searcher, no cadence assigned in Attio yet) — Kay sent thank-you reply 2026-05-12 20:15 to Jackson's "Thank you" note. 2 days. Fresh peer-searcher relationship (first call 2026-05-12, AI-coaching discussion). Auto-create-on-send: Jackson already has `attio_id: 8fa6e92b-5153-414d-beaa-e33b01448105`; vault entity is up-to-date. No nurture cadence assigned yet — surface to Kay for cadence-decision via pipeline-manager only if/when relationship warms further. Tracked here as orientation.
- **Carlos Nieto** ([[entities/carlos-nieto-dca]] — DCA, intermediary/IB, no cadence assigned in Attio yet) — first in-person meeting 2026-05-13 09:30 ET, ESB Suite 7640. 1 day. Reciprocity owed per call-note signal (Carlos shopped 3 deals + offered Miami-PE intros + Osvaldo intro — G&B owes flow back). No outbound from Kay to Carlos yet captured in Gmail; calendar attendance is the only confirmed interaction. Surface to outreach-manager on next pass if/when Carlos forwards deal materials. Vault entity has populated `## Relationship Notes`; vault→Attio sync queued (no `attio_id` yet).
- **Lauren Young** ([[entities/lauren-young]] — Union Square Ventures, Friend/Personal, Occasionally) — Kay wrote back via personal email 2026-05-12 (off-system). Per `feedback_off_system_resolution_closes_loop`, loop is CLOSED — no longer surfaced as overdue.
- **Andrew Lowis** ([[entities/andrew-lowis]] — Axial, Quarterly) — last interaction 2026-05-06 (Axial 12pm meeting + thread "Nice meeting you at XPX yesterday"). 8 days. Within Quarterly threshold. Open follow-ups (Axial member-application, panel deck digital copy) tracked in pipeline-manager open-loops, not here.
- **Guillermo Lavergne** ([[entities/guillermo-lavergne]] — Investor, Weekly) — last interaction 2026-05-06 (biweekly call). 8 days. Within Weekly threshold (10 days). Next interaction confirmed 2026-05-20 on Attio.
- **Nikki Higgins** ([[entities/nikki-higgins]] — Jet Aviation, Quarterly) — last interaction 2026-04-22. 22 days. Within Quarterly threshold (98 days).
- **James Emden** ([[entities/james-emden]] — Helmsley Spear, Occasionally) — Gmail thread "RE: Meeting You Yesterday" last active 2026-05-07. 7 days. Filter add executed 2026-05-10 (label `auto/personal & network`). Within Occasionally threshold by a wide margin.
- **Harrison Wells** ([[entities/harrison-wells]] — Dodo Digital, Occasionally) — Gmail thread "[Urgent] AI security vulnerabilities" 2026-05-13 16:59 (4 msgs). 1 day. Active engagement, multiple threads running. Next major touchpoint is Friday 5/15 call (brief landed per `brain/briefs/2026-05-15-harrison-wells-call-5.md`). Within Occasionally threshold.
- **Stanley Rodos** ([[entities/stanley-rodos]] — Crate Capital, Quarterly) — last interaction 2026-03-17. 58 days. Within Quarterly threshold. Per `feedback_within_cadence_commitment_drift`: aged commitment text in `next_action` does not justify surfacing inside cadence window. Suppressed.
- **Britta Nelson** ([[entities/britta-nelson]] — Quarterly, Art World) — Gmail-silent since 2025-12-16 but `next_action` documents "Texted recently (late March 2026). No follow-up needed." Per SKILL.md, recent text-channel evidence in `next_action` overrides Gmail silence. Suppressed.
- **Janet Crockett** ([[entities/janet-crockett]] — Saltoun Capital Controller, transactional/no cadence assigned) — Kay sent Saltoun annual-review reply 2026-05-12. 2 days. Not a cadence contact (Controller handling annual investor admin); auto-create-on-send will land an Attio stub but no nurture cadence applies.

(**Ali Doswell** — Potomac View Partners, Quarterly — last interaction 2026-04-30. **15 days now — rolled OFF the 14-day Gmail-verification window today**, as projected in yesterday's artifact. Still within Quarterly threshold (98 days). Not surfaced. Next eligible to re-enter the window only if a new interaction lands and resets the timer.)

(Jim Vigna — Live Oak Bank, Quarterly — last interaction 2026-04-27, 17 days. Outside the 14-day Gmail-verification window. Still within Quarterly threshold; not surfaced.)

## Trigger-Based Contacts (Excluded from Overdue Logic)

Contacts whose `next_action` text contains trigger language ("when", "if", "once", "until") — correctly excluded from cadence surfacing today (unchanged from 2026-05-13):

- **Richard Augustyn** (Endurance Search, Quarterly) — "Reach out when insurance deal enters Active Deals pipeline."
- **Michael Topol** (MGT Insurance, Quarterly) — "Re-engage when we have an insurance deal for him to review. Trigger: deal flow only, not elapsed time."
- **Rachele Adelman** (Oberle Risk, Quarterly) — "When insurance DD needed on a target, reach out to August Felker, cc Rachele."
- **Alexandra Kelly** (UOVO, Occasionally) — "On maternity leave. Do not contact until she returns."
- **Scott Casper** (EQA, Quarterly) and **Eric Dreyer** (EQA, Quarterly) — "Re-engage ~July 2026 if no new deals cross."

## PASS-Suppressed Contacts (Session Decision Log)

Per `session-decisions-2026-05-01.md` Friday nurture cluster — Kay PASS'd these and they remain suppressed until further notice:

- **Kristina Marcigliano** (WTW, Quarterly) — would otherwise be 143 days overdue.
- **Hunter Hartwell** (Ellirock, Quarterly) — would otherwise be 120 days overdue.
- **Dan Tanzilli** (Third Eye, Monthly) — would otherwise be 49 days overdue.

Per `feedback_lauren_della_monica_dead_end.md` and `session-decisions-2026-05-06.md`:
- **Lauren Della Monica** — confirmed dead end. Never surface.
- **Eric Carter** (Cohort Peak) — Dormant suppression stub. Spam-tier marked.

Per `feedback_off_system_resolution_closes_loop.md` and `session-decisions-2026-05-12.md`:
- **Lauren Young** — closed via personal-email response 2026-05-12. No further surfacing (also listed under Auto-Resolved above for clarity on the transition).

Per assistant-vs-principal rule (SKILL.md):
- **Chase Lacson** (Goodman Taft, Monthly) — assistant. Would be 198 days overdue against Monthly. Suppressed in favor of principal **Molly Epstein** (Occasionally cadence, last interaction 2026-03-31, 44 days — within Occasionally threshold). Net: nothing surfaced.

Per recent session-decisions (`-2026-05-08.md` through `-2026-05-12.md`):
- No new PASS/REJECT decisions on cadence contacts. The only new relationship-relevant decision on 5/12 was the Lauren Young off-system closure (captured above) and the admin@-alias scan-pattern confirmation (captured under System Status Alerts).
- No session-decisions file written for 2026-05-13 (Wednesday) — Carlos Nieto first-meeting + Hannah Barrett Mid-Search Summit logistics dominated the day, no cadence-contact PASS/REJECT decisions made.

## Pending Intros

None outstanding this morning. Last cycle's intros all closed (Rachel Tepper → Zoe Wen 2026-04-01; Melissa Goldberg → Kendall → Amanda 2026-02-03 era). Andrew Lowis's offered intro to Arturo (Axial founder) remains gated on Kay submitting the Axial member-application form post-call — pipeline-manager owns that open loop, not relationship-manager.

New intro offers landed yesterday from Carlos Nieto (Osvaldo — peer searcher at similar stage; Miami-PE rollup contacts — both gated on Carlos forwarding) but these are inbound-pending, not Kay-owed-outbound, so they do not surface here. They will appear in pipeline-manager's open-loops until Carlos sends.

## Warm Intro Opportunities (from target-discovery)

None this morning — no target-discovery handoff has landed yet today. Thursday is not the standard target-discovery refill day (Sundays at 3pm via Phase 2 launchd job); if any niche flags refill-needed via the morning workflow, warm-intro paths will surface on the next run, not this artifact.

Note: Kay's 2026-05-12 LinkedIn-Connect outreach to **Kevin O'Connell** ([[entities/kevin-oconnell]] — President Hampton Pest Management, ex-Toplands Capital searcher) remains pending LinkedIn-side response. Tracked here only for orientation; not a target-discovery warm path.

## Vault → Attio Syncs

Sweep covered all `brain/entities/*.md` files modified on/after 2026-05-07 (now ~162 files in the 7-day window) where `type: person` AND has `## Relationship Notes` section with populated body AND `attio_id` is missing/empty (or `attio_synced_at` is missing/older than file `modified`).

**Net candidate delta from 2026-05-13:** +1 candidate (**carlos-nieto-dca** — `## Relationship Notes` body now populated with 2 dated bullets after 5/13 meeting; no `attio_id`. Yesterday this entity was held back because the Relationship Notes section was empty pre-meeting. Today it qualifies). Jackson Niketas is intentionally NOT a candidate — he already has `attio_id: 8fa6e92b-...` set from prior; the post-call note he qualifies for would be a fresh note attached to the existing Attio record, not a vault→Attio person-record creation. Logging him separately under "Existing-Record Note Attachments" below.

Updated queue: **16 candidates** (15 from yesterday + carlos-nieto-dca): kevin-hong, mark-gardella, august-felker, megan-lawlor, clayton-sachs, katie-walker, adilene-dominguez, tom-jackson, sarah-rowell, ali-potomac-view, jake-stoller, ali-doswell, hunter-hartwell, christine-kobel, kevin-oconnell, carlos-nieto-dca.

**Existing-Record Note Attachments (new sub-track):**
- **jackson-niketas** — has `attio_id` from prior; 2026-05-12 first-call note + thank-you exchange should attach as a fresh engagement-context note on the existing Attio person record. Currently blocked on the same MCP-unavailable path as the queue above.

**Net syncs executed this run: 0.** Status unchanged: Attio direct-API auth is healthy (op-resolved key returns 200), but `mcp__attio__*` tool inventory is still empty in this server-side session (re-confirmed via ToolSearch this run — `select:mcp__attio__list_records,mcp__attio__list_notes,mcp__attio__create_note,mcp__attio__search_records` returned no results). SKILL.md sync flow is written against the MCP path; raw-HTTP re-implementation of idempotent note-attachment outside the tested code path remains deferred. All 16 person-record candidates + 1 existing-record note attachment remain queued. Idempotency guard (note-title check) will hold when sync resumes.

## Attio Dedup Needed

None detected — no Attio reads attempted via MCP this run. Direct API is live but full People-list enumeration was not run (out of scope for headless 7am fire; dedup detection is a sweep-level concern, best handled on a host with MCP connected).

## System Status Alerts

- **Carlos Nieto first-meeting capture landed in vault** — entity `carlos-nieto-dca` now has populated `## Relationship Notes` post-5/13 meeting. Moves him out of the "empty-notes hold" status from 2026-05-13's artifact and into the vault→Attio sync queue (position 16). Auto-create-on-send via Gmail has NOT yet occurred — Kay has not emailed Carlos. If Kay sends outbound to `carlos@digitalcapitaladvisors.com` today, Attio will auto-create the person record and the queued note attachment will become resolvable on the next MCP-up cycle.
- **Jackson Niketas thank-you-exchange captured** — Kay's 5/12 20:15 reply landed cleanly. Jackson already has `attio_id`. The relationship-note attachment for the 5/12 first call is queued under the new "Existing-Record Note Attachments" sub-track within Vault → Attio Syncs.
- **No session-decisions-2026-05-13 file written** — Wednesday session ended without a goodnight ceremony (or it was written but not yet committed to the file path). Today's run pulled the most-recent file (2026-05-12) and cross-referenced against it; no cadence decisions were missed because Wednesday's activity was Carlos Nieto first meeting + Mid-Search Summit logistics, neither of which generated PASS/REJECT decisions on cadence contacts. Flagging for awareness in case Wednesday context is needed elsewhere.
- **Gmail outbound scans continue checking BOTH aliases** per `feedback_kay_outbound_includes_admin_alias.md` (2026-05-12). Today's probes ran `from:kay.s@greenwichandbarrow.com OR from:admin@greenwichandbarrow.com` at both `newer_than:2d` (recent-window) and `newer_than:14d` (action-already-taken-verification window). No new admin@-originated material captured today.
- **Attio API auth — HEALTHY** (carry-forward). Direct curl with op-resolved key returns 200. 1Password migration landed 2026-05-09; backup at `~/.config/op-sa-token.env` (chmod 600).
- **Attio MCP server-side still not connected** (carry-forward from 2026-05-08+). `mcp__attio__*` tool inventory remains empty in this session. The SKILL.md sync flow targets the MCP path; raw API is live but note-attachment writes require MCP-side scope handling. Carry-forward gap: Attio MCP needs to come up on this server before the queued 16 vault→Attio person-record syncs + 1 existing-record note attachment can execute through the documented path. Pipeline-manager surfaces this for Kay's awareness; no daily-fire mitigation work added.

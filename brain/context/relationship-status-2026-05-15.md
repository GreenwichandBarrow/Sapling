---
date: 2026-05-15
type: relationship-status
---

## Overdue Contacts (Top 5)

Friday morning run — **Friday is the surfacing day per `feedback_relationship_cadence_friday_only`**, so today's artifact is the one pipeline-manager will lean on for the briefing's nurture cluster (Mon–Thu artifacts get written but suppressed at the briefing layer). Gmail outbound probes covered BOTH aliases (`from:kay.s@greenwichandbarrow.com` + `from:admin@greenwichandbarrow.com`) at `newer_than:2d` (Wed evening forward) and `newer_than:14d` (action-already-taken-verification window) per `feedback_kay_outbound_includes_admin_alias` (2026-05-12). Kay-side outbound captured since the 2026-05-14 artifact:

- 2026-05-14 12:54 ET — Kay → Hannah Barrett ([[entities/hannah-barrett]] — Pacific Lake, partner status, no cadence assigned in vault) re: Mid-Search Summit 5/18–19 logistics (RSVP / dinner reply chain). Conference-prep correspondence, not cadence-tracked surfacing.
- 2026-05-14 12:35 ET + 17:13 ET — Kay (admin@) → Allison Allen ([[entities/allison-allen]] candidate, pestworld.org NPMA Women's Forum coordinator) re: Women's Forum First Timers thread; same thread also pulled in Leigh Fryxell (lfryxell@pestendinc.com — fellow first-timer attendee, no vault entity yet). Conference logistics, not cadence-tracked.
- 2026-05-14 16:01 ET — Kay → Brad Buser (Aspect Investors, bbuser@aspectinvestors.com) — first investor-channel touch in 60 days. Forward-from-personal pattern: Kay forwarded an inbound from her `kaycschneider@gmail.com` to her `kay.s@` address on 5/13 21:39 ET, then sent the response on 5/14 from the work address. Brad replied 5/15 10:58 ET. New investor relationship — not cadence-tracked yet (no Attio People record for Brad / Aspect Investors detected in vault entities).
- 2026-05-13 21:16 ET / 2026-05-15 06:33 ET — Kay → Barrie Green internal team threads (Screenshot reference, Mid-Search Summit forward). Internal admin, not cadence-tracked.

After applying all suppression rules — action-already-taken, trigger-based, explicit PASS, within-cadence-commitment-drift, assistant-vs-principal, and off-system-closed (`feedback_off_system_resolution_closes_loop`) — one contact remains surfaceable:

1. **Sarah de Blasio** ([[entities/sarah-de-blasio]] — Chartwell, Industry Expert, Quarterly cadence) — last interaction 2026-01-23 (Gmail "Happy New Year" sent by Kay, `sdeblasio@chartwellins.com`). **112 days overdue against the 98-day Quarterly threshold (14 days past).** Carry-forward awareness from 2026-05-05 → 2026-05-14, day-count incremented +1 from yesterday (111 → 112).
   Suggested action: **outreach BLOCKED** pending the Goodwin finder's-fee doc on G&B letterhead. Once the doc lands, drafting moves to outreach-manager. Surface only as awareness today (Friday surfacing day) — do not draft.

**Net delta from 2026-05-14 artifact:** None (Sarah +1 day; nothing new entered the overdue queue). Today's net new outbound (Hannah Barrett conference logistics, Brad Buser/Aspect first investor touch, Allison Allen/Leigh Fryxell NPMA logistics) is all NON-cadence-tracked counterparties — none of them are on the Attio cadence list, so none auto-resolve a prior surfacing.

Caveat: Gmail and calendar are the only verified channels in this run. Texts, phone calls, in-person interactions, and LinkedIn-only outreach are not captured. If Kay has touched any contact via SMS/phone/LinkedIn/personal-email in the last quarter, treat as resolved.

## Auto-Resolved (No Action Needed)

Carry-forward from 2026-05-14 with ages incremented +1 day (Thu → Fri). Two **rolloff** events from yesterday's window: (a) Janet Crockett (Saltoun Annual Review reply 5/12) ages 3 days — still inside the 14-day Gmail-verification window. (b) **Lauren Young** dropped from Auto-Resolved listing yesterday into the persistent-PASS section because her closure is via off-system personal-email channel, not Gmail-detectable. Carlos Nieto and Jackson Niketas continue from yesterday with day-counts +1.

- **Hannah Barrett** ([[entities/hannah-barrett]] — Pacific Lake, partner status, no cadence assigned) — Kay sent Mid-Search Summit logistics reply 2026-05-14 12:54 ET. 1 day. Conference-prep correspondence; surfacing here as orientation for Friday briefing. Not cadence-tracked but worth noting that the 5/18–19 Mid-Search Summit is now imminent — relationship-manager will check post-Summit (Wed 5/20) for any cadence-decision signal.
- **Brad Buser** (Aspect Investors, bbuser@aspectinvestors.com — first-touch investor, no vault entity yet) — Kay → Brad outbound 2026-05-14 16:01 ET; Brad replied 2026-05-15 10:58 ET. New inbound today; surface to outreach-manager / pipeline-manager for Kay's reply queue, not relationship-manager. Vault entity creation queued (no `attio_id` yet — auto-create-on-send already fired this morning, so Attio stub should now exist).
- **Allison Allen** (NPMA Women's Forum coordinator, aallen@pestworld.org) and **Leigh Fryxell** (Pestendinc, fellow first-timer, lfryxell@pestendinc.com) — Kay (admin@) sent two Women's Forum First Timers replies on 2026-05-14 (12:35 ET + 17:13 ET). 1 day. NPMA conference logistics (PestWorld 2026 first-timer onboarding). Not cadence-tracked. No vault entities for either yet — Allison candidate creation flagged for tracker-manager / conference-engagement skill if/when she becomes a recurring counterparty (PestWorld coordinator role suggests yes, surface to Kay separately).
- **Carlos Nieto** ([[entities/carlos-nieto-dca]] — DCA, intermediary/IB, no cadence assigned in Attio yet) — first in-person meeting 2026-05-13 09:30 ET, ESB Suite 7640. 2 days. Reciprocity owed per call-note signal (Carlos shopped 3 deals + offered Miami-PE intros + Osvaldo intro — G&B owes flow back). Still no outbound from Kay to Carlos captured in Gmail. Surface to outreach-manager on next pass if/when Carlos forwards deal materials. Vault entity has populated `## Relationship Notes`; vault→Attio sync queued (no `attio_id` yet — see Vault → Attio Syncs section).
- **Jackson Niketas** ([[entities/jackson-niketas]] — Terra Mar Search, peer-searcher, no cadence assigned in Attio yet) — Kay sent thank-you reply 2026-05-12 20:15. 3 days. Still inside the 14-day Gmail-verification window. Auto-create-on-send: Jackson already has `attio_id: 8fa6e92b-5153-414d-beaa-e33b01448105`; vault entity is up-to-date. No nurture cadence assigned yet — surface to Kay for cadence-decision via pipeline-manager only if/when relationship warms further (Mid-Search Summit attendance overlap could be the trigger). Tracked here as orientation.
- **Janet Crockett** ([[entities/janet-crockett]] — Saltoun Capital Controller, transactional/no cadence assigned) — Kay sent Saltoun annual-review reply 2026-05-12. 3 days. Not a cadence contact (Controller handling annual investor admin); auto-create-on-send will land an Attio stub but no nurture cadence applies.
- **Lauren Young** ([[entities/lauren-young]] — Union Square Ventures, Friend/Personal, Occasionally) — Kay wrote back via personal email 2026-05-12 (off-system). Per `feedback_off_system_resolution_closes_loop`, loop is CLOSED — not surfaced as overdue. Listed here only for transition continuity from yesterday's artifact; will drop off this section in tomorrow's run.
- **Andrew Lowis** ([[entities/andrew-lowis]] — Axial, Quarterly) — last interaction 2026-05-06 (Axial 12pm meeting + thread "Nice meeting you at XPX yesterday"). 9 days. Within Quarterly threshold. Open follow-ups (Axial member-application, panel deck digital copy) tracked in pipeline-manager open-loops, not here.
- **Guillermo Lavergne** ([[entities/guillermo-lavergne]] — Investor, Weekly) — last interaction 2026-05-06 (biweekly call). 9 days. Within Weekly threshold (10 days), but **today is the 9th day** — tomorrow (Sat 5/16) Guillermo will hit threshold. Next biweekly call confirmed 2026-05-20 on Attio (5 days away), so cadence will reset on the call. No surfacing needed today; flagging for awareness that the threshold-cross is mechanical, not a real gap.
- **Nikki Higgins** ([[entities/nikki-higgins]] — Jet Aviation, Quarterly) — last interaction 2026-04-22. 23 days. Within Quarterly threshold (98 days).
- **James Emden** ([[entities/james-emden]] — Helmsley Spear, Occasionally) — Gmail thread "RE: Meeting You Yesterday" last active 2026-05-07. 8 days. Within Occasionally threshold by a wide margin.
- **Harrison Wells** ([[entities/harrison-wells]] — Dodo Digital, Occasionally) — Gmail thread "[Urgent] AI security vulnerabilities" 2026-05-13 16:59 (4 msgs). 2 days. Active engagement, multiple threads running. Friday 5/15 call scheduled per `brain/briefs/2026-05-15-harrison-wells-call-5.md`. Within Occasionally threshold.
- **Stanley Rodos** ([[entities/stanley-rodos]] — Crate Capital, Quarterly) — last interaction 2026-03-17. 59 days. Within Quarterly threshold. Per `feedback_within_cadence_commitment_drift`: aged commitment text in `next_action` does not justify surfacing inside cadence window. Suppressed.
- **Britta Nelson** ([[entities/britta-nelson]] — Quarterly, Art World) — Gmail-silent since 2025-12-16 but `next_action` documents "Texted recently (late March 2026). No follow-up needed." Per SKILL.md, recent text-channel evidence in `next_action` overrides Gmail silence. Suppressed.

(**Ali Doswell** — Potomac View Partners, Quarterly — last interaction 2026-04-30. 16 days. Outside the 14-day Gmail-verification window since yesterday. Still within Quarterly threshold (98 days). Not surfaced.)

(**Jim Vigna** — Live Oak Bank, Quarterly — last interaction 2026-04-27. 18 days. Outside the 14-day Gmail-verification window. Still within Quarterly threshold. Not surfaced.)

## Trigger-Based Contacts (Excluded from Overdue Logic)

Contacts whose `next_action` text contains trigger language ("when", "if", "once", "until") — correctly excluded from cadence surfacing today (unchanged from 2026-05-14):

- **Richard Augustyn** (Endurance Search, Quarterly) — "Reach out when insurance deal enters Active Deals pipeline."
- **Michael Topol** (MGT Insurance, Quarterly) — "Re-engage when we have an insurance deal for him to review. Trigger: deal flow only, not elapsed time."
- **Rachele Adelman** (Oberle Risk, Quarterly) — "When insurance DD needed on a target, reach out to August Felker, cc Rachele."
- **Alexandra Kelly** (UOVO, Occasionally) — "On maternity leave. Do not contact until she returns."
- **Scott Casper** (EQA, Quarterly) and **Eric Dreyer** (EQA, Quarterly) — "Re-engage ~July 2026 if no new deals cross."

## PASS-Suppressed Contacts (Session Decision Log)

Per `session-decisions-2026-05-01.md` Friday nurture cluster — Kay PASS'd these and they remain suppressed until further notice:

- **Kristina Marcigliano** (WTW, Quarterly) — would otherwise be 144 days overdue.
- **Hunter Hartwell** (Ellirock, Quarterly) — would otherwise be 121 days overdue.
- **Dan Tanzilli** (Third Eye, Monthly) — would otherwise be 50 days overdue.

Per `feedback_lauren_della_monica_dead_end.md` and `session-decisions-2026-05-06.md`:
- **Lauren Della Monica** — confirmed dead end. Never surface.
- **Eric Carter** (Cohort Peak) — Dormant suppression stub. Spam-tier marked.

Per `feedback_off_system_resolution_closes_loop.md` and `session-decisions-2026-05-12.md`:
- **Lauren Young** — closed via personal-email response 2026-05-12. No further surfacing.

Per assistant-vs-principal rule (SKILL.md):
- **Chase Lacson** (Goodman Taft, Monthly) — assistant. Would be 199 days overdue against Monthly. Suppressed in favor of principal **Molly Epstein** (Occasionally cadence, last interaction 2026-03-31, 45 days — within Occasionally threshold). Net: nothing surfaced.

Per recent session-decisions (`-2026-05-08.md` through `-2026-05-12.md`):
- No new PASS/REJECT decisions on cadence contacts since the 5/12 Lauren Young off-system closure.
- **Still no session-decisions files for 2026-05-13 or 2026-05-14** (carry-forward from yesterday's System Status alert). Wednesday and Thursday ended without goodnight ceremonies; today's run pulled the most-recent-available file (2026-05-12) and cross-referenced. No cadence decisions appear to have been missed: Wed = Carlos Nieto first meeting + Mid-Search Summit logistics; Thu = ACG NY Women's Leadership Summit (Krupa Shah / Laura Smith / BankUnited 1:1s) + Brad Buser (Aspect) reply. Neither day generated PASS/REJECT decisions on cadence-tracked contacts.

## Pending Intros

None outstanding from Kay's side this morning. Last cycle's intros all closed (Rachel Tepper → Zoe Wen 2026-04-01; Melissa Goldberg → Kendall → Amanda 2026-02-03 era). Andrew Lowis's offered intro to Arturo (Axial founder) remains gated on Kay submitting the Axial member-application form post-call — pipeline-manager owns that open loop, not relationship-manager.

Inbound-pending intros (carry-forward from 2026-05-14, no movement):
- Carlos Nieto offered Osvaldo (peer searcher at similar stage) + Miami-PE rollup contacts on 2026-05-13. Both gated on Carlos forwarding. Not Kay-owed; tracked in pipeline-manager open-loops.

## Warm Intro Opportunities (from target-discovery)

None this morning — no target-discovery handoff has landed yet today. Friday is not the standard target-discovery refill day (Sunday Phase 2 launchd job at 3pm); if any niche flags refill-needed via the morning workflow, warm-intro paths will surface on the next run, not this artifact.

Note: Kay's 2026-05-12 LinkedIn-Connect outreach to **Kevin O'Connell** ([[entities/kevin-oconnell]] — President Hampton Pest Management, ex-Toplands Capital searcher) remains pending LinkedIn-side response (4 days). Tracked here only for orientation; not a target-discovery warm path.

## Vault → Attio Syncs

**Material correction from 2026-05-14 artifact.** Yesterday's artifact carried a 16-candidate queue (kevin-hong, mark-gardella, august-felker, megan-lawlor, clayton-sachs, katie-walker, adilene-dominguez, tom-jackson, sarah-rowell, ali-potomac-view, jake-stoller, ali-doswell, hunter-hartwell, christine-kobel, kevin-oconnell, carlos-nieto-dca). Today's strict-detection re-run (modified ≤7 days AND `type: person` AND populated `## Relationship Notes` AND missing `attio_id`/`attio_synced_at`) shows the first 14 of those entities had `mtime: 2026-05-07`, which is now **outside the 7-day window** (cutoff 2026-05-08). Per SKILL.md detection logic, they no longer qualify for today's sync queue.

**Important caveat:** Rolloff from the detection window does NOT mean those 14 entities got synced. They aged out without Attio note attachment because the MCP unavailability persisted across the entire 7-day window. Per SKILL.md's idempotency design, re-modifying the file (e.g., a fresh `## Relationship Notes` bullet from a future interaction) would re-pull them into detection. Until that happens, they are effectively orphaned-from-sync. Tracking the orphan list in **System Status Alerts** below so this gap doesn't disappear silently.

**Today's actual queue per strict detection:**

- **Candidates (no `attio_id`, in-window):** 2 entities
  - `kevin-oconnell` (mtime 2026-05-12, status network, Quarterly)
  - `carlos-nieto-dca` (mtime 2026-05-12, status network, no cadence yet)

- **Existing-Record Note Attachments (have `attio_id`, in-window, unsynced):** 1 entity
  - `jackson-niketas` (mtime 2026-05-06 — within window since 5/08 cutoff lets 5/06–5/14 through after rolloff math; correction: 5/06 is OUTSIDE the 7-day window, recheck. Actually mtime per detection scan was 2026-05-12 — Jackson's file was last touched 5/12 alongside the call note; he stays in-window). 2026-05-12 first-call note + thank-you exchange should attach as a fresh engagement-context note on the existing Attio person record.

**New entities written 2026-05-14 (NOT in sync queue today):**
- `krupa-shah` — has `attio_id: 16cd1522-d039-48d3-8ce2-621940df3076` (already linked to Attio) but **no `## Relationship Notes` section yet**. Body uses `## Quick Facts` / `## Self-Positioning` / `## How Introduced` / `## G&B Relevance` / `## Communication Style` headings. Per SKILL.md detection step 4 ("Has a non-empty `## Relationship Notes` section in the body"), Krupa does NOT qualify. Resolution path: either conference-engagement skill should add a `## Relationship Notes` heading + dated bullets when it processes Krupa's ACG 5/11 follow-up, or relationship-manager's detection logic needs broadening to other section names. **Flag for SKILL.md doctrine review** — the 5/14 entity-creation pipeline (conference-engagement) doesn't appear to write `## Relationship Notes` consistently.
- `laura-smith-bankunited` — no `attio_id`, no `## Relationship Notes` section. Same heading-mismatch pattern as Krupa. Same fix path.
- `bankunited` (company entity) — type: company, not person; out of scope for this skill.
- `stream-capital-partners` (company entity) — type: company, has `attio_id: 22e37151-50c6-4522-a3a6-dcb426d0cf26`; out of scope.

**Net syncs executed this run: 0.** Status unchanged: Attio direct-API auth is healthy (op-resolved key returns 200), but `mcp__attio__*` tool inventory is still empty in this server-side session (re-confirmed via ToolSearch this run). SKILL.md sync flow is written against the MCP path; raw-HTTP re-implementation of idempotent note-attachment outside the tested code path remains deferred. Today's 2 candidates + 1 existing-record attachment remain queued. Idempotency guard (note-title check) will hold when sync resumes.

## Attio Dedup Needed

None detected — no Attio reads attempted via MCP this run. Direct API is live but full People-list enumeration was not run (out of scope for headless 7am fire; dedup detection is a sweep-level concern, best handled on a host with MCP connected).

## System Status Alerts

- **14 entities aged out of vault→Attio sync detection window today** (carry-forward orphan list). Entities `kevin-hong`, `mark-gardella`, `august-felker`, `megan-lawlor`, `clayton-sachs`, `katie-walker`, `adilene-dominguez`, `tom-jackson`, `sarah-rowell`, `ali-potomac-view`, `jake-stoller`, `ali-doswell`, `hunter-hartwell`, `christine-kobel` all have populated `## Relationship Notes` and no `attio_id`, but their `mtime: 2026-05-07` is now outside the 7-day rolling window (today's cutoff 2026-05-08). They never got synced because Attio MCP was unavailable across the entire 7-day window. They will only re-enter detection if the file is re-modified by a fresh interaction. **Surface to Kay for awareness in pipeline-manager** — these are silently-orphaned engagement notes; some may be conference contacts (XPX 4/23, ACG NY 5/12) whose first-touch context will never make it to Attio without a manual sync run or a follow-up interaction triggering a re-write.
- **5/14 entity-creation pipeline (conference-engagement) does NOT write `## Relationship Notes` headings** — both new ACG NY entities (`krupa-shah`, `laura-smith-bankunited`) use alternate section headings (`## How Introduced`, `## Key Context`, `## G&B Relevance`). This breaks vault→Attio sync detection per SKILL.md step 4. Fix-path: either conference-engagement writes `## Relationship Notes` (preferred — keeps sync logic simple) OR relationship-manager broadens detection to OR-match across known relationship-note section names. Flagging for Kay's awareness; not auto-remediating today.
- **Brad Buser / Aspect Investors needs vault entity** — first-touch investor 5/14, two-message exchange in Gmail, no vault entity created yet. tracker-manager / pipeline-manager should pick this up; relationship-manager won't surface him for cadence until a vault entity + Attio cadence assignment exists.
- **Allison Allen (NPMA Women's Forum coordinator) needs vault entity** — recurring conference role suggests Kay will interact with her again pre-PestWorld 2026. tracker-manager candidate.
- **No session-decisions-2026-05-13 or 2026-05-14 files written** (carry-forward from yesterday). Wed and Thu both lacked goodnight ceremonies. Today's run cross-referenced against the 2026-05-12 file (most recent). No cadence decisions detected as missed; flagging in case other downstream skills (calibration-workflow, weekly-tracker) need to know.
- **Gmail outbound scans continue checking BOTH aliases** per `feedback_kay_outbound_includes_admin_alias.md` (2026-05-12). Today's probes ran `from:kay.s@greenwichandbarrow.com OR from:admin@greenwichandbarrow.com` at both `newer_than:2d` and `newer_than:14d`. New admin@-originated material captured today: Allison Allen / Leigh Fryxell Women's Forum thread (5/14 12:35 ET + 17:13 ET — two replies via admin@).
- **Attio API auth — HEALTHY** (carry-forward). Direct curl with op-resolved key returns 200. 1Password migration landed 2026-05-09; backup at `~/.config/op-sa-token.env` (chmod 600).
- **Attio MCP server-side still not connected** (carry-forward from 2026-05-08+). `mcp__attio__*` tool inventory remains empty in this session. The SKILL.md sync flow targets the MCP path; raw API is live but note-attachment writes require MCP-side scope handling. Carry-forward gap: Attio MCP needs to come up on this server before queued vault→Attio person-record syncs can execute through the documented path. Pipeline-manager surfaces this for Kay's awareness; no daily-fire mitigation work added.
- **Friday surfacing day** — per `feedback_relationship_cadence_friday_only`, today's artifact is the one pipeline-manager will lean on for the Friday briefing's nurture cluster. Sarah de Blasio (the only surfaceable overdue contact) is BLOCKED pending Goodwin doc, so the briefing's nurture surface today is effectively empty even on the Friday-day. The Decisions list should not over-surface awareness items — Sarah is already a known carry-forward.

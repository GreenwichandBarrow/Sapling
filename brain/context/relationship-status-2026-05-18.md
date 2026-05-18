---
date: 2026-05-18
type: relationship-status
---

## Overdue Contacts (Top 5)

**Monday run — no surfaceable overdue contacts. The overdue queue is empty.**

Per `feedback_relationship_cadence_friday_only`, Friday is the surfacing day for the briefing's nurture cluster; Sun–Thu artifacts are written but suppressed at the briefing layer. Written today for continuity and queue-state tracking only.

Gmail outbound probes ran across BOTH aliases (`from:kay.s@greenwichandbarrow.com OR from:admin@greenwichandbarrow.com`) per `feedback_kay_outbound_includes_admin_alias` at `newer_than:14d`, plus inbound `newer_than:7d`. gog auth verified healthy this run (calendar + Gmail both returned live data; op SA-token + keyring resolve via the scheduled-env path). Empty cadence results are genuine absence, not auth failure.

**Re-verified at the morning-workflow run (post-06:53 scheduled write).** Fresh outbound probe (`newer_than:4d`, both aliases) and inbound probe (`newer_than:2d`) confirm NO new substantive Kay → cadence-tracked-counterparty email since 2026-05-16. Heels to Deals drafts (Deborah/Monica/Marsha) still DRAFT status (Gmail re-confirms NOT sent). Inbound signal items (Ninad Singh reply 5/17, Guillermo "Accepted" 5/16, Everingham & Kerr deal blasts, Kay self-notes from kaycschneider@gmail.com) are email-intelligence / pipeline-manager territory, not relationship-manager cadence triggers. Attio REST curl-verified HEALTHY (HTTP 200, `/v2/self`); Attio MCP still disconnected (`mcp__attio__*` inventory empty, re-confirmed via ToolSearch). Queue state from the 06:53 write holds unchanged.

**No cadence-tracked contact crossed its threshold this cycle.** Carry-forward state from 2026-05-17 holds unchanged:

- **Sarah de Blasio** — permanently retired to Dormant 2026-05-15 (`feedback_sarah_de_blasio_already_connected`). Kay manages directly. Never surface. The 11-day "blocked on Goodwin doc" carry-forward thread remains terminated. (Final reference; not re-listed below.)
- Within-threshold, not surfaced (all unchanged from 2026-05-17): Andrew Lowis / Axial (Quarterly, last 2026-05-06 ≈12d, within 98d), Nikki Higgins / Jet Aviation (Quarterly, within), James Emden / Helmsley Spear (Occasionally, last active 2026-05-07, within 213d), Harrison Wells / Dodo Digital (Occasionally, active multi-thread engagement 5/13–5/15), Stanley Rodos (Quarterly, within window — within-cadence-commitment-drift suppression holds), Britta Nelson (Quarterly, text-channel evidence in next_action overrides Gmail silence), Ali Doswell / Jim Vigna (Quarterly, within), Molly Epstein / Goodman Taft (Occasionally ≈48d, within — surfaced in place of assistant Chase Lacson, nothing to surface).

Caveat: Gmail and calendar are the only verified channels in this run. Texts, phone calls, in-person interactions, and LinkedIn-only outreach are not captured. If Kay touched any contact via SMS/phone/LinkedIn/personal-email, treat as resolved.

## Auto-Resolved (No Action Needed)

Kay-side activity since the 2026-05-17 artifact (none are cadence-tracked counterparties — all conference / first-touch / transactional, logged for orientation; none auto-resolves a prior cadence surfacing because the queue was already empty):

- **Guillermo Lavergne** ([[entities/guillermo-lavergne]] — Investor, Weekly) — biweekly meeting invite Accepted 2026-05-16 10:29 ET. Next call confirmed (2026-05-20 per prior artifact); Weekly cadence resets on the call. No gap, no surfacing. Unchanged from 5/17.
- **"Reconnecting on search fund raise experience"** — Kay SENT a reply 2026-05-16 12:21 in a 25-msg thread. Peer/search-fund correspondence, not a cadence-tracked counterparty; pipeline-manager / email-intelligence territory, not relationship-manager surfacing. Orientation only.
- **Ninad Singh** ([[entities/ninad-singh]] — Beaconsfield Growth) — inbound "Re: Follow up from the ETA Breakfast" 2026-05-17 11:36 (16-msg thread). Inbound reply to Kay; reactive-mode item for Kay personally / email-intelligence, not a cadence trigger. Not cadence-tracked. Orientation only.
- **Kevin Hong** ([[entities/kevin-hong]] — Caprae Capital) — inbound SBA-webinar invite 2026-05-15. Informational broadcast, not a cadence trigger. Kevin remains in the orphaned-from-sync carry-forward list (see System Status Alerts).
- **Heels to Deals 5/13 drafts** — Deborah Chichester, Monica Chawla, Marsha Weiner ("Great meeting you at Heels to Deals") all still DRAFT status as of 2026-05-16 12:38 ET (Gmail re-confirms NOT sent). Awaiting Kay's send. New conference counterparties, not cadence-tracked yet. Send-queue item owned by Kay / pipeline-manager.
- **Becky / Carlos / Matt drafts** (DRAFTED 5/16 per `session-decisions-2026-05-16` APPROVE #9) — Becky circle-back + Carlos Nieto/DCA send-ready, Matt send-blocked (no verified email — do not construct). Gmail confirms still in Kay's draft queue. pipeline-manager / outreach-manager draft-queue items, not relationship-manager cadence surfacing.

(Jackson Niketas — thank-you exchange 2026-05-12, now outside the 14-day verification relevance window; has `attio_id`, no cadence assigned. Orientation only — surface for a cadence decision only if the relationship warms via the Mid-Search Summit 5/18–5/19 overlap.)

## Trigger-Based Contacts (Excluded from Overdue Logic)

Unchanged from 2026-05-17 — `next_action` contains trigger language, correctly excluded from cadence surfacing:

- **Richard Augustyn** (Endurance Search, Quarterly) — "Reach out when insurance deal enters Active Deals pipeline."
- **Michael Topol** (MGT Insurance, Quarterly) — "Re-engage when we have an insurance deal for him to review."
- **Rachele Adelman** (Oberle Risk, Quarterly) — "When insurance DD needed on a target, reach out to August Felker, cc Rachele."
- **Alexandra Kelly** (UOVO, Occasionally) — "On maternity leave. Do not contact until she returns."
- **Scott Casper** (EQA, Quarterly) and **Eric Dreyer** (EQA, Quarterly) — "Re-engage ~July 2026 if no new deals cross."

## PASS-Suppressed Contacts (Session Decision Log)

Unchanged from 2026-05-17. Session-decisions reviewed this run: `-2026-05-16.md` (latest; Saturday session, closed 2026-05-17). No new PASS/REJECT on cadence-tracked contacts.

- **Sarah de Blasio** — permanent Dormant suppression (`feedback_sarah_de_blasio_already_connected`). Never surface.
- **Kristina Marcigliano** (WTW, Quarterly), **Hunter Hartwell** (Ellirock, Quarterly), **Dan Tanzilli** (Third Eye, Monthly) — PASS'd per `session-decisions-2026-05-01`, remain suppressed.
- **Lauren Della Monica** — confirmed dead end (`feedback_lauren_della_monica_dead_end`). Never surface.
- **Eric Carter** (Cohort Peak) — Dormant suppression stub, spam-tier.
- **Lauren Young** — closed via personal-email response 2026-05-12 (`feedback_off_system_resolution_closes_loop`). No further surfacing.
- **Chase Lacson** (Goodman Taft, Monthly) — assistant; suppressed in favor of principal Molly Epstein (Occasionally, within threshold). Net: nothing surfaced.
- **Bayonne Exterminating / Sandra Fernandez** — REJECTED 5/16 from JJ-Call-Only routing (non-principal, no email; NPMA NJ event card). Not a cadence contact.

## Pending Intros

None Kay-owed this morning. Standing items (NOT relationship-manager-owned, tracked elsewhere — listed for completeness):

- **Carlos Nieto** offered Osvaldo (peer searcher) + Miami-PE rollup contacts 2026-05-13 — gated on Carlos forwarding. Not Kay-owed; pipeline-manager open-loop.
- **Laura Smith** — 2 warm intros offered (Stephanie super-connector + a BankUnited colleague) — BLOCKED: no verified email for Laura, address will not be constructed (`session-decisions-2026-05-16` Open Loop #3). Resolves when a verified email surfaces.
- **Andrew Lowis** → Arturo (Axial founder) — gated on Kay submitting the Axial member-application form. pipeline-manager open-loop.
- Krupa Shah AI-consultant intro — explicitly NOT owed (REJECTED 5/16 as mis-capture; Kay already provided the name directly).

## Warm Intro Opportunities (from target-discovery)

None this morning — no target-discovery handoff has landed. (target-discovery is PAUSED per `feedback_target_discovery_paused`; warm-intro paths would surface on the run following any future handoff.)

## Vault → Attio Syncs

**Net syncs executed this run: 0** — Attio MCP server-side remains disconnected (carry-forward from 2026-05-08+; `mcp__attio__*` tool inventory empty this session, re-confirmed via ToolSearch). The SKILL.md sync flow is written against the MCP path; raw-HTTP idempotent note-attachment outside the tested code path remains deferred. Diagnosis was APPROVED 2026-05-16 (diagnose-only); MCP path not yet restored.

In-window vault entities (`type: person`, modified ≤7 days, populated `## Relationship Notes`, missing `attio_id`) — queued, not synced:

- `david-freeman` (mtime 2026-05-15, no cadence) — queued.
- `stephanie-unknown-surname` (mtime 2026-05-16, stub, surname unknown) — queued.
- `carlos-nieto-dca` (mtime 2026-05-12, network status, no cadence) — queued (carry-forward).
- `kevin-oconnell` (mtime 2026-05-12, network status; yesterday noted Quarterly, frontmatter shows none — informational drift) — queued.
- `brad-buser` (mtime 2026-05-16) — queued.
- `laura-smith-bankunited` (mtime 2026-05-16) — queued (also send-blocked at outreach layer, no verified email).

Already have `attio_id` (REST-created via the conference-engagement / triage-approved path 2026-05-16, NOT this skill's MCP flow): `krupa-shah`, `becky-wuest-creavin`, `matt-becky-colleague`. `jackson-niketas` has `attio_id` — existing-record note attachment (5/12 first-call + thank-you context) remains queued for the MCP path.

`sarah-de-blasio` (Dormant) and `janet-crockett` (no `## Relationship Notes` section) correctly excluded from sync detection. Two entities modified 2026-05-18 also correctly excluded: `tristate-stl` (`type: company` — sync is `type: person` only) and `greg-bruyere` (`type: person` but no `## Relationship Notes` section). No net-new sync candidates entered the 7-day window this run.

Idempotency guard (note-title check) will hold when the MCP sync path resumes. Re-running this skill does not duplicate notes.

## Attio Dedup Needed

None detected — no Attio reads attempted via MCP this run (MCP disconnected). Full People-list enumeration is out of scope for a headless run; dedup detection is a sweep-level concern best handled on a host with MCP connected.

## System Status Alerts

- **Attio MCP server-side still disconnected** (carry-forward 2026-05-08+). `mcp__attio__*` inventory empty this session. Diagnosis APPROVED 2026-05-16 (diagnose-only). Until MCP is restored, all queued vault→Attio person-record syncs cannot execute through the documented path. Attio direct REST auth is HEALTHY (1Password op-resolved token, op vault `GB Server` resolves) — used 5/16 for the Heels to Deals People creates. Note-attachment writes still require MCP-side scope handling. Surface to Kay via pipeline-manager for awareness; no daily-fire mitigation added.
- **Orphaned-from-sync engagement notes (carry-forward).** ~14 vault entities (`kevin-hong`, `mark-gardella`, `august-felker`, `megan-lawlor`, `clayton-sachs`, `katie-walker`, `adilene-dominguez`, `tom-jackson`, `sarah-rowell`, `ali-potomac-view`, `jake-stoller`, `ali-doswell`, `hunter-hartwell`, `christine-kobel`) have populated `## Relationship Notes` and no `attio_id`, but aged out of the 7-day detection window without sync because Attio MCP was unavailable across the entire window. They re-enter detection only if re-modified by a fresh interaction. Some are conference first-touch context (XPX 4/23, ACG NY 5/12) that will not reach Attio without a manual sync run or a follow-up interaction. Surface to Kay for awareness — silently-orphaned, not auto-remediating.
- **Section-heading mismatch breaks vault→Attio detection.** Conference-engagement / follow-up pipeline writes `## How Introduced` / `## Key Context` / `## G&B Relevance` instead of `## Relationship Notes` on some entities. SKILL.md detection step 4 requires a non-empty `## Relationship Notes` section. Fix-path: either the upstream pipeline writes `## Relationship Notes`, or relationship-manager broadens detection to OR-match known relationship-note section names. Flagged for SKILL.md doctrine review; not auto-remediating today.
- **gog/op resolution HEALTHY this run.** Calendar + Gmail both returned live data through the scheduled-env path (`. ~/.config/op-sa-token.env; source scripts/load-env.sh; load_env scripts/.env.launchd`). The 5/16 "gog down" premise was a confirmed false alarm (interactive shell does not source the SA-token env; scheduled jobs do). Empty cadence results this run are genuine absence. No action needed — logged to close the carry-forward concern.
- **Gmail outbound scans cover BOTH aliases** per `feedback_kay_outbound_includes_admin_alias` — `from:kay.s@greenwichandbarrow.com OR from:admin@greenwichandbarrow.com` at `newer_than:14d`, inbound `newer_than:7d`.

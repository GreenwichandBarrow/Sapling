---
date: 2026-05-17
type: relationship-status
---

## Overdue Contacts (Top 5)

**Sunday run — no surfaceable overdue contacts today. The overdue queue is empty.**

Per `feedback_relationship_cadence_friday_only`, Friday is the surfacing day for the briefing's nurture cluster; Sun–Thu artifacts are written but suppressed at the briefing layer. Today's run nonetheless materially changes the standing queue and that change must be recorded.

**Material change — the single carry-forward overdue contact has been permanently retired:**

- **Sarah de Blasio** ([[entities/sarah-de-blasio]] — Chartwell Insurance Services, `sdeblasio@chartwellins.com`) — carried as the lone surfaceable overdue contact from 2026-05-05 → 2026-05-15 (peaking at 112 days against the 98-day Quarterly threshold, BLOCKED on a Goodwin finder's-fee doc). **On 2026-05-15 Kay confirmed she is already connected and manages this relationship directly.** Vault entity `nurture_cadence` is now `dormant`; new doctrine memory `feedback_sarah_de_blasio_already_connected` instructs: never propose outreach, never surface as overdue, never re-classify regardless of days-since. Per SKILL.md cadence table, **Dormant = never surface**. Sarah is now permanently suppressed — this is the last artifact that will reference her at all (transition continuity only). She is NOT a dead end; she is Kay-managed off-system.

Net effect: with Sarah retired to Dormant, **zero contacts remain surfaceable as overdue.** Gmail outbound probes ran across BOTH aliases (`from:kay.s@greenwichandbarrow.com OR from:admin@greenwichandbarrow.com`) per `feedback_kay_outbound_includes_admin_alias`, at `newer_than:5d` and (for action-already-taken verification) `newer_than:14d`/`30d`. No cadence-tracked contact crossed its threshold this cycle.

Caveat: Gmail and calendar are the only verified channels in this run. Texts, phone calls, in-person interactions, and LinkedIn-only outreach are not captured. If Kay touched any contact via SMS/phone/LinkedIn/personal-email, treat as resolved.

## Auto-Resolved (No Action Needed)

Kay-side outbound and confirmed interactions captured since the 2026-05-15 artifact (none of these are cadence-tracked counterparties — all conference / first-touch / transactional, so none auto-resolves a prior cadence surfacing; logged for orientation):

- **Guillermo Lavergne** ([[entities/guillermo-lavergne]] — Investor, Weekly) — biweekly meeting invite **Accepted 2026-05-16 10:29 ET** ("Guillermo I Kay Bi-Weekly Mtg"). Next call confirmed; the Weekly cadence resets on the call (2026-05-20 per prior artifact). Mechanical threshold-cross flagged in the 5/15 artifact is now closed — no gap, no surfacing.
- **Carlos Nieto/DCA** ([[entities/carlos-nieto-dca]] — Digital Capital Advisors, intermediary/IB, no cadence assigned) — follow-up email DRAFTED 2026-05-16 (per `session-decisions-2026-05-16.md` APPROVE #9). Gmail confirms NOT yet sent (still in Kay's draft queue). This is a pipeline-manager / outreach-manager draft-queue item, not relationship-manager cadence surfacing. Vault entity has populated `## Relationship Notes`; vault→Attio sync remains queued (no `attio_id`).
- **Heels to Deals 5/13 contacts** — Deborah Chichester (Schulman Lobel), Monica Chawla (Norris McLaughlin), Marsha Weiner (Corporate Coach), plus Becky Wuest-Creavin circle-back — all DRAFTED 2026-05-16 (3 "Great meeting you at Heels to Deals" drafts + "Heels to Deals + circling back on Matt" draft, all DRAFT status as of 2026-05-16 12:38–12:59 ET). Awaiting Kay's send. New conference counterparties; 3 new Attio People records APPROVED 5/16 (source=conference/heels-to-deals-2026-05-13). Not cadence-tracked yet.
- **Krupa Shah** ([[entities/krupa-shah]]), **Laura Smith** ([[entities/laura-smith-bankunited]]), **Matt (Becky's colleague)** ([[entities/matt-becky-colleague]]) — verbally-shared engagement notes APPROVED to Attio 2026-05-16. Krupa quarterly RE-deal-flow check-in (To Do row 86) stands; the AI-consultant intro (row 85) was correctly REJECTED 5/16 as a mis-capture (Kay already gave Krupa the name directly — **no intro owed**). Matt draft is send-blocked (no verified email — do not construct). Not cadence-tracked.
- **Jackson Niketas** ([[entities/jackson-niketas]] — Terra Mar Search, peer-searcher) — thank-you exchange 2026-05-12 20:15, now 5 days old (outside the 14-day verification window relevance but inside record). Has `attio_id: 8fa6e92b-5153-414d-beaa-e33b01448105`. No cadence assigned; surface to pipeline-manager for a cadence decision only if/when the relationship warms (Mid-Search Summit overlap could trigger). Orientation only.

(Andrew Lowis / Axial — Quarterly, last interaction 2026-05-06, 11 days, within Quarterly threshold; Axial open follow-ups owned by pipeline-manager. Nikki Higgins / Jet Aviation — Quarterly, 25 days, within threshold. James Emden / Helmsley Spear — Occasionally, last active 2026-05-07, within threshold. Harrison Wells / Dodo Digital — Occasionally, active multi-thread engagement. Stanley Rodos — Quarterly, within window, within-cadence-commitment-drift suppression holds. Britta Nelson — Quarterly, text-channel evidence in next_action overrides Gmail silence, suppressed. Ali Doswell / Jim Vigna — Quarterly, outside 14d verification window, within Quarterly threshold, not surfaced. All unchanged from 2026-05-15.)

## Trigger-Based Contacts (Excluded from Overdue Logic)

Unchanged from 2026-05-15 — `next_action` contains trigger language, correctly excluded from cadence surfacing:

- **Richard Augustyn** (Endurance Search, Quarterly) — "Reach out when insurance deal enters Active Deals pipeline."
- **Michael Topol** (MGT Insurance, Quarterly) — "Re-engage when we have an insurance deal for him to review."
- **Rachele Adelman** (Oberle Risk, Quarterly) — "When insurance DD needed on a target, reach out to August Felker, cc Rachele."
- **Alexandra Kelly** (UOVO, Occasionally) — "On maternity leave. Do not contact until she returns."
- **Scott Casper** (EQA, Quarterly) and **Eric Dreyer** (EQA, Quarterly) — "Re-engage ~July 2026 if no new deals cross."

## PASS-Suppressed Contacts (Session Decision Log)

- **Sarah de Blasio** — **NEW permanent suppression** per `session-decisions-2026-05-15` + `feedback_sarah_de_blasio_already_connected`. Cadence set Dormant. Kay manages directly. Never surface again. (Replaces her prior carry-forward "overdue, blocked" status entirely.)
- **Kristina Marcigliano** (WTW, Quarterly), **Hunter Hartwell** (Ellirock, Quarterly), **Dan Tanzilli** (Third Eye, Monthly) — PASS'd per `session-decisions-2026-05-01.md`, remain suppressed.
- **Lauren Della Monica** — confirmed dead end (`feedback_lauren_della_monica_dead_end.md`). Never surface.
- **Eric Carter** (Cohort Peak) — Dormant suppression stub, spam-tier.
- **Lauren Young** — closed via personal-email response 2026-05-12 (`feedback_off_system_resolution_closes_loop`). No further surfacing.
- **Chase Lacson** (Goodman Taft, Monthly) — assistant; suppressed in favor of principal **Molly Epstein** (Occasionally, ~47 days, within threshold). Net: nothing surfaced.
- **Bayonne Exterminating / Sandra Fernandez** — REJECTED 5/16 from JJ-Call-Only routing (non-principal, no email; NPMA NJ event card). Not a cadence contact; logged so it does not re-enter any surface.
- Recent session-decisions reviewed: `-2026-05-13.md`, `-2026-05-14.md` (reconstructed), `-2026-05-16.md`. No new PASS/REJECT on cadence-tracked contacts beyond the Sarah retirement. 5/13 + 5/14 were confirmed scheduled-only / conference days (reconstruction complete per 5/16 APPROVE) — no cadence decisions lost.

## Pending Intros

None Kay-owed this morning. Prior-cycle intros all closed. Standing items (NOT relationship-manager-owned, tracked elsewhere — listed for completeness):

- **Carlos Nieto** offered Osvaldo (peer searcher) + Miami-PE rollup contacts on 2026-05-13 — both gated on Carlos forwarding. Not Kay-owed; pipeline-manager open-loop.
- **Laura Smith** — 2 warm intros offered (Stephanie super-connector + a BankUnited colleague) — BLOCKED: no verified email for Laura, address will not be constructed (`session-decisions-2026-05-16` Deferred #3). Resolves when a verified email surfaces.
- **Andrew Lowis** → Arturo (Axial founder) — gated on Kay submitting the Axial member-application form. pipeline-manager open-loop.
- Krupa Shah AI-consultant intro — explicitly NOT owed (REJECTED 5/16 as mis-capture; Kay already provided the name directly).

## Warm Intro Opportunities (from target-discovery)

None this morning — no target-discovery handoff has landed yet today. Sunday Phase 2 target-discovery launchd job (3pm) may produce handoffs; warm-intro paths would surface on the next run, not this artifact.

## Vault → Attio Syncs

**Net syncs executed this run: 0** — Attio MCP server-side remains disconnected (carry-forward from 2026-05-08+; `mcp__attio__*` tool inventory empty in this session, re-confirmed via ToolSearch). Per `session-decisions-2026-05-16`, an Attio MCP disconnect diagnosis was APPROVED (diagnose-only) but the MCP path is not yet restored. The SKILL.md sync flow is written against the MCP path; raw-HTTP idempotent note-attachment outside the tested code path remains deferred.

In-window vault entities (`type: person`, modified ≤7 days, populated `## Relationship Notes`, missing `attio_id`/`attio_synced_at`) — queued, not synced:

- `carlos-nieto-dca` (mtime 2026-05-12, network status, no cadence) — queued.
- `kevin-oconnell` (mtime 2026-05-12, network status, Quarterly) — queued.
- `jackson-niketas` (mtime 2026-05-13, has `attio_id`) — existing-record note attachment queued (5/12 first-call + thank-you context).

New 2026-05-16 entities written by the Heels to Deals / ACG follow-up pipeline — `becky-wuest-creavin`, `brad-buser`, `krupa-shah`, `laura-smith-bankunited`, `matt-becky-colleague`, `stephanie-unknown-surname` (+ company entities `aspect-investors`, `peapack-private`, `xpx`). Per `session-decisions-2026-05-16` APPROVE, engagement notes for Krupa/Laura/Becky/Matt were APPROVED to Attio and 3 new Attio People records created (source=conference/heels-to-deals-2026-05-13) — those writes route through the conference-engagement / triage-approved path, NOT this skill's MCP sync flow. Detection-eligibility for any still-needing `## Relationship Notes`-section sync re-checks tomorrow; section-heading mismatch (`## How Introduced` / `## Key Context` vs `## Relationship Notes`) flagged below.

Idempotency guard (note-title check) will hold when the MCP sync path resumes. Re-running this skill does not duplicate notes.

## Attio Dedup Needed

None detected — no Attio reads attempted via MCP this run (MCP disconnected). Direct API is live but full People-list enumeration is out of scope for a headless run; dedup detection is a sweep-level concern best handled on a host with MCP connected.

## System Status Alerts

- **Attio MCP server-side still disconnected** (carry-forward 2026-05-08+). `mcp__attio__*` inventory empty this session. Diagnosis APPROVED 2026-05-16 (diagnose-only). Until MCP is restored, all queued vault→Attio person-record syncs cannot execute through the documented path. Attio direct API auth is HEALTHY (1Password op-resolved token, op vault `GB Server` resolves). Note-attachment writes still require MCP-side scope handling. Surface to Kay via pipeline-manager for awareness; no daily-fire mitigation added.
- **Orphaned-from-sync engagement notes (carry-forward).** ~14 vault entities (`kevin-hong`, `mark-gardella`, `august-felker`, `megan-lawlor`, `clayton-sachs`, `katie-walker`, `adilene-dominguez`, `tom-jackson`, `sarah-rowell`, `ali-potomac-view`, `jake-stoller`, `ali-doswell`, `hunter-hartwell`, `christine-kobel`) have populated `## Relationship Notes` and no `attio_id`, but aged out of the 7-day detection window without sync because Attio MCP was unavailable across the entire window. They re-enter detection only if re-modified by a fresh interaction. Some are conference first-touch context (XPX 4/23, ACG NY 5/12) that will not reach Attio without a manual sync run or a follow-up interaction. Surface to Kay for awareness — silently-orphaned, not auto-remediating.
- **Section-heading mismatch breaks vault→Attio detection.** Conference-engagement / follow-up pipeline writes `## How Introduced` / `## Key Context` / `## G&B Relevance` instead of `## Relationship Notes` (seen on `krupa-shah`, `laura-smith-bankunited`, and likely the 5/16 batch). SKILL.md detection step 4 requires a non-empty `## Relationship Notes` section. Fix-path: either the upstream pipeline writes `## Relationship Notes`, or relationship-manager broadens detection to OR-match known relationship-note section names. Flagged for SKILL.md doctrine review; not auto-remediating today.
- **Sarah de Blasio retired to Dormant (resolved, not a problem).** Logged here so downstream skills (calibration-workflow, pipeline-manager) know the long-running carry-forward overdue item is closed by Kay's instruction, not by an outreach action. The 11-day "Sarah blocked on Goodwin doc" carry-forward thread is now terminated.
- **Gmail outbound scans cover BOTH aliases** per `feedback_kay_outbound_includes_admin_alias` — `from:kay.s@greenwichandbarrow.com OR from:admin@greenwichandbarrow.com` at `newer_than:5d` / `14d` / `30d`. gog unlock verified (op vault `GB Server` resolves); empty results this run are genuine absence, not auth failure.
- **5/13 + 5/14 session-decisions reconstructed** (per 5/16 APPROVE) — confirmed scheduled-only / conference days, no human cadence decisions lost. Carry-forward "missing files" alert from prior artifacts is now CLOSED.

---
date: 2026-05-20
type: relationship-status
---

## Overdue Contacts (Top 5)

**Wednesday run — no surfaceable overdue contacts. The overdue queue is empty.**

Per `feedback_relationship_cadence_friday_only`, Friday is the surfacing day for the briefing's nurture cluster; Sun–Thu artifacts are written for continuity and queue-state tracking only and are suppressed at the briefing layer. This is a Wednesday write.

Gmail outbound probes ran across BOTH aliases (`from:kay.s@greenwichandbarrow.com OR from:admin@greenwichandbarrow.com`) at `newer_than:14d`, plus inbound `newer_than:3d`, per `feedback_kay_outbound_includes_admin_alias`. gog auth HEALTHY this run (op-resolved env via `source scripts/op-env.sh`). Empty cadence results are genuine absence, not auth failure.

**No cadence-tracked contact crossed its threshold this cycle.** Carry-forward state from 2026-05-19 holds unchanged:

- **Sarah de Blasio** — permanently retired to Dormant 2026-05-15 (`feedback_sarah_de_blasio_already_connected`). Never surface.
- Within-threshold, not surfaced: Andrew Lowis / Axial (Quarterly, last 2026-05-06 ≈14d, within 98d), Nikki Higgins / Jet Aviation (Quarterly, within), James Emden / Helmsley Spear (Occasionally, last active 2026-05-07, within 213d), Harrison Wells / Dodo Digital (Occasionally, active multi-thread engagement 5/13–5/15 — coaching, not deal-flow), Stanley Rodos (Quarterly, within window — within-cadence-commitment-drift suppression holds), Britta Nelson (Quarterly, text-channel evidence in next_action overrides Gmail silence), Ali Doswell / Jim Vigna (Quarterly, within), Molly Epstein / Goodman Taft (Occasionally ≈50d, within — surfaced in place of assistant Chase Lacson; nothing to surface).

Caveat: Gmail and calendar are the only verified channels in this run. Texts, phone calls, in-person interactions, and LinkedIn-only outreach are not captured. If Kay touched any contact via SMS/phone/LinkedIn/personal-email, treat as resolved.

## Auto-Resolved (No Action Needed)

Kay-side activity since the 2026-05-19 artifact (none are cadence-tracked counterparties — all conference / warm-intro / transactional; none auto-resolves a prior cadence surfacing because the queue was already empty). Logged for orientation:

- **Laura Smith** ([[entities/laura-smith-bankunited]] — BankUnited VP, network) — **MATERIAL STATE CHANGE.** Sent the Randi Mason warm intro herself 2026-05-19 18:57 ET from `LSmith@bankunited.com` (verified address, sent FROM it; carry-forward "no verified email" Open Loop #3 from `session-decisions-2026-05-19` is now **RESOLVED — verified email captured this run**). Cc'd Stephanie Tetreault (`STetreault@bankunited.com`) — likely the BankUnited super-connector previously stubbed as [[entities/stephanie-unknown-surname]]; entity-merge candidate, flagged under "Metadata Drift" below, not auto-mutated here. Followed at 19:44 ET with "LUNCH HOLD" proposing 6/3 lunch (Laura + Randi + Kay). Randi Mason (Morrison Cohen) auto-replied OOO 18:58 ET. Active warm thread, Kay handles replies — not a cadence surfacing.
- **Morgan Endicott / LCG Advisors** (Strategic Growth Director, Western Region — sell-side advisor) — sent group "ACG NY Women In Leadership Conference Follow Up" 2026-05-19 17:12 ET (firm-overview PDF, broadcast "Hi ladies" to attendees; not a personal-to-Kay note). Self-IDs as M&A advisor / sell-side per `feedback_classify_intermediary_by_self_id`. Intermediary List territory, not relationship-manager / cadence — surfaced here for orientation only. Recall received 17:27 ET (Morgan re-sent within the original window; ignore the recall, treat the 17:12 send as the canonical message). New entity stub needed (deferred — Kay-confirmation pattern; no `attio_id`, no relationship history yet).
- **Becky Wuest-Creavin** ([[entities/becky-wuest-creavin]] — Network, has `attio_id`) — carry-forward. Becky→Sam intro fully resolved 5/18 (no new activity 5/19). Parallel "Heels to Deals" thread (7 msgs total, last 5/18 08:00) — quiet, no new activity. Orientation only.
- **Sam Curcio / Transworld** ([[entities/sam-transworld]] — prospect/broker, no cadence) — carry-forward. Active warm thread, Kay handles replies. Entity still has name/email pending fields; correction is a deferred Kay-confirmation item per `session-decisions-2026-05-19` Deferred, not auto-mutated.
- **Matt (Becky's XPX colleague)** ([[entities/matt-becky-colleague]] — has `attio_id`) — carry-forward. Follow-up DRAFTED → FINAL per `session-decisions-2026-05-19`, awaiting Kay to schedule (~8am Mon–Wed opener — today is Wednesday, so this is the last day of the proposed send window). No Gmail outbound to Matt yet (consistent with "awaiting Kay schedule"). Not a relationship-manager surfacing; pipeline-manager / send-queue territory.
- **Heels to Deals 5/13 drafts** — Deborah Chichester, Monica Chawla, Marsha Weiner — carry-forward. All still DRAFT status as of 2026-05-16 12:38 ET (no new sends 5/19). Send-queue item owned by Kay / pipeline-manager. Orientation only.
- **Carlos Nieto** ([[entities/carlos-nieto-dca]] — Network/DCA) — sent industry deal blast 2026-05-19 20:34 ET ("Invest in the Future of Farming with AI-Driven Drone Technology"). Inbound pitch, not a relationship signal — DealsX-channel / pipeline-manager territory. Offered Osvaldo + Miami-PE intros still gated on Carlos forwarding (carry-forward Open Loop).
- **Guillermo Lavergne** ([[entities/guillermo-lavergne]] — Investor, Weekly) — biweekly meeting confirmed earlier this week. No gap, no surfacing. Unchanged.
- Inbound-only / informational since last artifact (NOT cadence triggers — email-intelligence / pipeline-manager territory): Rebekah Stender intro re Nick Akers / Inzo (5/19 14:09), Tailscale trial-ending notice (5/19 20:00, ops-systems alert not relationship), broker / aggregator blasts (Quietlight, Flippa, Helen Guo, Buy Then Build, Axial — all 5/19), Axios / Manhattan Chamber / CorpNet (transactional). Orientation only.

## Trigger-Based Contacts (Excluded from Overdue Logic)

Unchanged from 2026-05-19 — `next_action` contains trigger language, correctly excluded from cadence surfacing:

- **Richard Augustyn** (Endurance Search, Quarterly) — "Reach out when insurance deal enters Active Deals pipeline."
- **Michael Topol** (MGT Insurance, Quarterly) — "Re-engage when we have an insurance deal for him to review."
- **Rachele Adelman** (Oberle Risk, Quarterly) — "When insurance DD needed on a target, reach out to August Felker, cc Rachele."
- **Alexandra Kelly** (UOVO, Occasionally) — "On maternity leave. Do not contact until she returns."
- **Scott Casper** (EQA, Quarterly) and **Eric Dreyer** (EQA, Quarterly) — "Re-engage ~July 2026 if no new deals cross."

## PASS-Suppressed Contacts (Session Decision Log)

Session-decisions reviewed this run: `-2026-05-19.md` (previous workday). No new PASS/REJECT on cadence-tracked contacts; 5/19 was Becky→Sam intro + Matt follow-up + two infra fixes (1Password-first creds, pull-template-live doc). Carry-forward unchanged:

- **Sarah de Blasio** — permanent Dormant suppression (`feedback_sarah_de_blasio_already_connected`). Never surface.
- **Kristina Marcigliano** (WTW, Quarterly), **Hunter Hartwell** (Ellirock, Quarterly), **Dan Tanzilli** (Third Eye, Monthly) — PASS'd per `session-decisions-2026-05-01`, remain suppressed.
- **Lauren Della Monica** — confirmed dead end (`feedback_lauren_della_monica_dead_end`). Never surface.
- **Eric Carter** (Cohort Peak) — Dormant suppression stub, spam-tier.
- **Lauren Young** — closed via personal-email response 2026-05-12 (`feedback_off_system_resolution_closes_loop`). No further surfacing.
- **Chase Lacson** (Goodman Taft, Monthly) — assistant; suppressed in favor of principal Molly Epstein (Occasionally, within threshold). Net: nothing surfaced.

## Pending Intros

None Kay-owed this morning. State delta from 2026-05-19:

- **Laura Smith → Randi Mason** intro — **CLOSED** this cycle. Laura executed the intro herself 2026-05-19 18:57 ET (Kay was the recipient, not the broker). No Kay-owed action; Kay handles reply to the lunch HOLD if accepting.
- **Carlos Nieto** offered Osvaldo (peer searcher) + Miami-PE rollup contacts 2026-05-13 — gated on Carlos forwarding / Carlos reply trigger (`session-decisions-2026-05-18` Deferred). Not Kay-owed; pipeline-manager open-loop.
- **Laura Smith** — second warm intro (a BankUnited colleague Stephanie Tetreault per `session-decisions-2026-05-16`) — Stephanie was cc'd on the Randi intro 5/19 18:57 ET, so the connection is acknowledged but no standalone intro yet. Not Kay-owed; whether Laura will deliver Stephanie as a separate intro is Laura's call.
- **Andrew Lowis** → Arturo (Axial founder) — gated on Kay submitting the Axial member-application form. pipeline-manager open-loop.

## Warm Intro Opportunities (from target-discovery)

None this morning — no target-discovery handoff has landed. (target-discovery is PAUSED per `feedback_target_discovery_paused`; warm-intro paths would surface on the run following any future handoff.)

## Vault → Attio Syncs

**Net syncs executed this run: 0** — Attio MCP server-side still disconnected (carry-forward 2026-05-08+; `mcp__attio__*` tool inventory empty this session, re-confirmed via ToolSearch "No matching deferred tools found"). The SKILL.md sync flow is written against the MCP path (`search_records` / `list_notes` / `create_note`); raw-HTTP idempotent note-attachment outside the tested code path remains deferred. Attio direct REST auth is HEALTHY this run (curl `/v2/self` → **HTTP 200**, 1Password op-resolved `ATTIO_API_KEY` via `scripts/op-env.sh`).

In-window vault entities (`type: person`, modified ≤7 days, populated `## Relationship Notes`, missing `attio_id`) — queued, not synced:

- `sam-transworld` (mtime 2026-05-18, prospect/broker, active warm thread) — queued. Sam replied from `scurcio@tworld.com` 5/18 so the Attio person record may now auto-exist; cannot confirm/attach without MCP. High-priority for the first post-MCP-restore sync.
- `laura-smith-bankunited` (mtime 2026-05-16, no cadence yet, **send-block resolved this run** — verified email `LSmith@bankunited.com` captured from 5/19 Randi intro; entity should be updated with the verified address on Kay-confirmation pass) — queued; relationship notes will need a 2026-05-19 bullet adding the Randi intro execution + 6/3 lunch HOLD.
- `david-freeman` (mtime 2026-05-15, no cadence) — queued (carry-forward).
- `stephanie-unknown-surname` (mtime 2026-05-16) — queued (carry-forward). **Metadata Drift** candidate: 5/19 Randi intro thread cc'd `STetreault@bankunited.com` — Stephanie Tetreault at BankUnited may resolve this stub. Surname resolution flagged for Kay-confirmation rename, not auto-mutated.
- `carlos-nieto-dca` (mtime 2026-05-12, network status, no cadence) — queued (carry-forward).
- `kevin-oconnell` (mtime 2026-05-12, network status) — queued (carry-forward).
- `brad-buser` (mtime 2026-05-16) — queued (carry-forward).
- `emilio-mitidieri` (mtime 2026-05-19, **NEW this cycle**, DealsX inbound interested-lead) — queued, but DealsX-channel ownership per `feedback_dealsx_lead_interested_is_outbound_reply`; relationship-manager not the primary owner. Surface logged here for completeness; downstream handling is DealsX/outreach-manager.

Already have `attio_id` (existing-record note attachment queued for the MCP path, NOT this skill's flow): `krupa-shah`, `jackson-niketas`, `matt-becky-colleague`, `becky-wuest-creavin`. The Becky 5/18 intro note (Becky→Sam warm intro logged), Matt 5/18–5/19 follow-up context, and a new entry for the Laura→Randi intro execution (5/19 18:57) are queued for attachment when MCP resumes.

Correctly excluded from sync detection: `sarah-de-blasio` (Dormant, no `## Relationship Notes`), `janet-crockett` / `greg-bruyere` (`type: person` but no `## Relationship Notes` section), and all `type: company` entities (sync is `type: person` only — `transworld`, `peapack-private`, `aspect-investors`, `digital-capital-advisors`, `xpx`, `terra-mar-search`, `bankunited`, `breakpoint-growth`, `art-ship-co`, `tristate-stl`, `jw-allen-co-insurance-brokers`, `personal-risk-management-solutions`, `stream-capital-partners`).

Idempotency guard (note-title check) will hold when the MCP sync path resumes. Re-running this skill does not duplicate notes.

## Attio Dedup Needed

None detected — no Attio reads attempted via MCP this run (MCP disconnected). Full People-list enumeration is out of scope for a headless run; dedup detection is a sweep-level concern best handled on a host with MCP connected. One entity-merge candidate (`stephanie-unknown-surname` → Stephanie Tetreault @ BankUnited) flagged under "Vault → Attio Syncs" Metadata Drift, not auto-mutated.

## System Status Alerts

- **Attio MCP server-side still disconnected** (carry-forward 2026-05-08+). `mcp__attio__*` inventory empty this session (re-confirmed via ToolSearch). Until MCP is restored, all queued vault→Attio person-record syncs and existing-record note attachments cannot execute through the documented path. **Attio direct REST auth is HEALTHY** (curl `/v2/self` → HTTP 200, op-resolved token via `scripts/op-env.sh`) — note-attachment writes still require MCP-side scope handling. Surface to Kay via pipeline-manager for awareness; no daily-fire mitigation added. Time-sensitive: `sam-transworld` (active warm thread) and now `laura-smith-bankunited` (verified email + 6/3 lunch HOLD landed 5/19) — engagement context not reaching Attio.
- **Orphaned-from-sync engagement notes (carry-forward).** ~14 vault entities (`kevin-hong`, `mark-gardella`, `august-felker`, `megan-lawlor`, `clayton-sachs`, `katie-walker`, `adilene-dominguez`, `tom-jackson`, `sarah-rowell`, `ali-potomac-view`, `jake-stoller`, `ali-doswell`, `hunter-hartwell`, `christine-kobel`) have populated `## Relationship Notes` and no `attio_id`, aged out of the 7-day detection window without sync because Attio MCP was unavailable across the entire window. They re-enter detection only if re-modified by a fresh interaction. Surface to Kay for awareness — silently-orphaned, not auto-remediating.
- **Section-heading mismatch breaks vault→Attio detection.** Some conference-engagement / follow-up entities write `## How Introduced` / `## Key Context` / `## G&B Relevance` instead of `## Relationship Notes`; SKILL.md detection step 4 requires a non-empty `## Relationship Notes` section. Fix-path: upstream pipeline writes `## Relationship Notes`, or relationship-manager broadens detection to OR-match known section names. Flagged for SKILL.md doctrine review; not auto-remediating today.
- **Laura Smith Open Loop closure surfaced.** `session-decisions-2026-05-19` Open Loop #3 ("Laura Smith — 2 warm intros still BLOCKED (no verified email; will not construct)") is **resolved by inbound** this cycle — Laura sent the Randi Mason intro herself from `LSmith@bankunited.com`. The verified email landed without Kay or system needing to construct it. Surface to evening session-decisions writer for closure verb (CLOSED) and to Kay for awareness that the carry-forward open loop is done.
- **gog/op resolution HEALTHY this run.** Gmail returned live outbound + inbound data through `source scripts/op-env.sh` (the 5/19 durable 1Password-first fix continues to hold). Empty cadence results this run are genuine absence. No action needed — logged to confirm the fix.
- **Gmail outbound scans cover BOTH aliases** per `feedback_kay_outbound_includes_admin_alias` — `from:kay.s@greenwichandbarrow.com OR from:admin@greenwichandbarrow.com` at `newer_than:14d`, inbound `newer_than:3d`.

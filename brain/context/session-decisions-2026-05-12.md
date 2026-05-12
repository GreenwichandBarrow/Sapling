---
date: 2026-05-12
type: context
title: "Session Decisions — 2026-05-12"
tags:
  - date/2026-05-12
  - context
  - topic/session-decisions
  - topic/excel-to-sheets-migration
  - topic/drive-restructure
  - topic/deal-aggregator-expansion
  - topic/conference-pipeline-rogue-status
  - topic/donut-charts
  - topic/sourcing-list-standardization
  - topic/morning-briefing
  - topic/voice-calibration
  - topic/kevin-oconnell-outreach
  - topic/saltoun-annual-review
  - person/janet-crockett
  - person/andrew-saltoun
  - person/kevin-oconnell
  - person/carlos-nieto-dca
  - person/harrison-wells
  - person/jeanne-wang
  - person/brad-buser
  - person/sam-singh
  - person/lauren-young
  - person/allison-allen
  - company/saltoun-capital
  - company/digital-capital-advisors
  - company/hampton-pest-management
  - company/aspect-investors
  - company/village-search-partners
schema_version: 1.1.0
---

# Session Decisions — 2026-05-12

Tuesday. Huge multi-thread day. Morning briefing → migrated personal task tracker Excel → Google Sheets (new bookmarkable surface), restructured Drive to channel-based hierarchy (OPERATIONS = SOURCING / ANALYST = RESEARCH & DILIGENCE), reconciled Conference Pipeline rogue status (`Future / Map-Only` → `NEW` w/ validator hardening), standardized Sourcing List Access + Type columns to 3-value enums + alphabetical sort, scoped Deal Aggregator Expansion project (17 items / 11 sections on new flat checklist surface), drafted Saltoun + Jeanne Wang + Aspect replies, sent Kevin O'Connell LinkedIn outreach (Kay's voice canonical phrases captured), prepped Carlos Nieto / DCA brief for tomorrow 9:30am + Harrison Wells brief for Friday 5/15. ~12 memories locked. Note: 5/11 evening had no `/goodnight` — only `/savestate`, so 5/11 has continuation file only, no session-decisions.

## Decisions

### Morning briefing (5 items)

- **APPROVE** Item 1 — Generate brief for [[entities/carlos-nieto-dca]] / Digital Capital Advisors Wed 5/13 9:30am at Empire State Building. New external, no prior brief; subagent delivered to `brain/briefs/2026-05-13-carlos-nieto-dca.md`.
- **APPROVE** Item 2 — Reply to [[entities/janet-crockett]] (Saltoun Controller) confirming year-end 12/31/2025 G&B investment figures. Draft saved to Gmail; Kay edited & sent.
- **APPROVE** Item 3 — Triage 5/10 Conference Pipeline corruption. Subagent found: validator was fixed 5/11 (3 commits `cf70d64`, `c5b402a`, `c043fc0`) but had codified `Future / Map-Only` as a legitimate status — a rogue agent-invented value Kay never authorized. Real reconciliation work followed.
- **APPROVE** Item 4 — Sweep iMac-path files in `scripts/`. Subagent recon: only `generate_systemd_units.py` has the literal (intentional translation-source constant). Validator files already portable. No refactor needed; this morning's launchd-debugger failures had different root causes.
- **DEFER** Item 5 — Taft (Payal) vs KeyBank (Megan) Thu 5/14 dinner pick. Resolved later in day: not attending either, conference-conflict reply drafted (see Actions Taken).

### Conference Pipeline rogue-status reconciliation

- **APPROVE** Adding `NEW` to the Decision-field dropdown on the Pipeline tab as the canonical agent-discovery marker (replaces invented `Future / Map-Only`). Kay added the dropdown value herself with yellow fill.
- **APPROVE** Stripping `Future / Map-Only` from `scripts/validate_conference_discovery_integrity.py` ALLOWED_STATUS_PROGRESSIONS + adding `NEW → {dropdown values}` transitions + adding AUTHORIZED_STATUSES set + new `check_c` validator that rejects any value outside Kay's dropdown.
- **APPROVE** Remapping 2 live rogue rows (AM&AA Chicago row 42, NPMA Orlando row 57) from `Future / Map-Only` → `NEW`.
- **APPROVE** Updating SKILL.md + headless-sunday-prompt to instruct the agent to write `NEW` (not blank, not invented) for newly-discovered conferences.
- **APPROVE** Fixing the validator's reference to `Registered` → `Registered Only` (matching the actual dropdown value Kay uses).

### Excel → Google Sheets task tracker migration

- **APPROVE** Migrate `TO DO 4.26.26.xlsx` → new Google Sheet `TO DO 5.12.26` (id `1ewqQshtN5pz8kmMTEvBZgAFy-0XB37-MVONkN_mdZmk`). Sheet ID + URL captured.
- **APPROVE** Kay's reversal of prior preference (Excel) — Sheets gives browser access from anywhere (parallel to Streamlit dashboard + Conference Pipeline).
- **APPROVE** Native Sheets primitives: data-validation checkboxes (not Unicode ☐ ✅), native dropdowns, native conditional formatting; sage palette ported (`#e8efd8`, `#7a8c4d`, `#f3f7e8`).
- **APPROVE** Drop the `lsof` guardrail in `scripts/task_tracker.py` (no file-lock issue on Sheets). Add API-quota retry with exponential backoff. Snapshot-to-JSON replaces `.xlsx` `.bak` backups.
- **APPROVE** Old Excel left in place — Kay decides when to retire it.

### Donut charts on Live Week tab

- **APPROVE** Build 7 native Google Sheets pie charts (`pieHole=0.5`) per day, replacing the prior big-% text display. The Excel `openpyxl` constraint that originally banned donut charts does NOT apply to Sheets (native chart rendering works on all clients).
- **APPROVE** Hidden `_donut_data` helper tab feeds Done/Left counts to each chart via formulas; updates live when checkboxes toggle.
- **APPROVE** Workbook theme palette: ACCENT1 = sage-dark `#7a8c4d` (Done slice), ACCENT2 = pure white `#ffffff` (Left slice). One API call, all 7 charts inherit; Kay's manual Mon-Done green override stays.
- **APPROVE** Sat/Sun (and any 0-task days) render as placeholder full rings: Left formula = `IF(COUNTA=0, 1, ...)` so an empty day still shows a donut shape.

### `sync-done-status` verb (text-match Sunday batch sync — Option A)

- **APPROVE** Build `sync-done-status` verb on `task_tracker.py`. Logic: walk weekly slots, for each checked slot find To Do row by exact task-text match, flip To Do checkbox TRUE → existing conditional formatting auto-applies strikethrough + sage-light fill.
- **APPROVE** Auto-invoke `sync-done-status` as a pre-step inside `archive-todo` (Sunday-night cleanup). `--skip-sync` flag opt-out exists.
- **REJECT** Option B (hidden Linked-Slot column + INDIRECT live-formula) — more complex, schema change required.
- **REJECT** Option C (Apps Script onEdit live sync) — adds infra surface that's avoided per `feedback_integration_priority_mcp_api_local`.
- **APPROVE** Snapshot before every write; trace only when > 0 To Do rows actually synced (no-op runs don't pollute calibration input).

### Drive restructure — channel-based, audience-tagged

- **APPROVE** Rename conceptual frame: `OPERATIONS` = SOURCING; `ANALYST` = RESEARCH & DILIGENCE. Top-level folders keep current names; conceptual purpose explicit.
- **APPROVE** Drive sub-organization by CHANNEL inside OPERATIONS (not by function):
  - `OPERATIONS/PROPRIETARY SOURCING/` (`BUY BOX`, `TARGET LISTS`, `COLD CALLING` (was `JJ` renamed by Kay per the function-not-person rule), `EMAIL & LINKEDIN/DEALSX`)
  - `OPERATIONS/INTERMEDIARY SOURCING/` (`BUY BOX`, `SOURCING LIST`, `INTERMEDIARY TARGET LIST`, `PREP DOCS`)
- **REJECT** Earlier proposal that grouped by FUNCTION (single BUY BOX folder, single OUTREACH folder). Channel-based is better because the 2 buy boxes are GENUINELY DIFFERENT documents (proprietary = niche-specific tristate $2-10M services; broker = industry-agnostic $2M floor opportunistic).
- **APPROVE** `CONFERENCES` lives in Kay's view-only `RESEARCH` folder, not inside either channel sub-folder — conferences span both proprietary + intermediary depending on the event.
- **APPROVE** Templates stay in `MANAGER DOCUMENTS / G&B MASTER TEMPLATES/` (canonical home; channel folders reference templates by Doc/Sheet ID, never replicate).
- **APPROVE** Kay executes all Drive moves; Claude proposes only. Exception was the templates-back-to-MASTER-TEMPLATES move where Kay said "I did it" (no Claude execution needed).

### Sourcing List structural standardization

- **APPROVE** Add 5 funnel-metrics columns to `General Sources` + `Niche-Specific Sources` tabs: `Listings Scanned (cum)`, `Near-Misses (cum)`, `Funnel Entries (cum)`, `Entry Rate %`, `Last Reviewed`. Blocked Sources tab skipped (not scanned).
- **APPROVE** Entry Rate % is the quality signal (Funnel Entries / Listings Scanned). NOT LOI Conversions — that's too downstream; quality means meets-basic-criteria-to-enter-funnel.
- **APPROVE** Access column → 3-value enum: `need to register` / `registered` / `public`. Tooling-failure notes ("Web broken", "Web blocked") moved to Notes column.
- **APPROVE** Type column → 3-value enum: `marketplace` / `email newsletter` / `direct relationships`. Combined-source rows collapsed to primary (e.g., `Marketplace + Email` → `marketplace`).
- **APPROVE** Sort `General Sources` + `Niche-Specific Sources` + all 9 tabs of `Intermediary Target List` alphabetically by Source/Firm column (native Sheets API `sortRange` so Entry Rate % formula references stay correct).

### Deal Aggregator Expansion project — restructure + scope

- **APPROVE** Convert project tab from Gantt format (15 milestones × 13 weekly columns) to FLAT CHECKLIST (Status / Section / Task / Due / Notes; weekly columns deleted).
- **APPROVE** Granularity: project items describe META action, NOT per-instance enumeration. Per-row work belongs in source list (Sourcing List, Intermediary Target List), not duplicated on project tab.
- **APPROVE** 1-week target deadline (5/17) for setup work; 50-broker outreach campaign is the exception (runs 5/13 → 5/27 at 5/day pace).
- **APPROVE** Section-by-section review (workshop mode) — 7 sections fully reviewed in chat before final write; 3 sections (Sourcing List Structure, Intermediary Target List, 50 Broker/IB Outreach) added at end without explicit section review for Kay's return.
- **APPROVE** Final tab state: 17 items / 11 sections (rows 6-22):
  - MARKETPLACE (5) — Sourcing List structure update ✅, marketplace status updates, sign-ups, review-pattern decision, Axial per-industry split
  - EMAIL & BLAST MONITORING VERIFICATION (2) — Active Deal Fast-Path E2E, broker BLAST multi-listing
  - CONFERENCE BROKER PIPELINE (1) — verify broker contacts from ACG land in Intermediary Target List by EOD 5/16
  - COLD CALLING DASHBOARD SYNC (1) — verify jj-snapshot-refresh + dashboard tile
  - DEALSX DASHBOARD SYNC (1) — verify DealsX email outreach activity flows to dashboard
  - QUARTERLY BROKER REVIEW (1)
  - OPEN DECISIONS (1) — lock broker buy-box geography window
  - SOURCING LIST STRUCTURE (2) — wire skill to update metrics, build dashboard tile by Entry Rate %
  - INTERMEDIARY TARGET LIST (1) — full hygiene pass
  - 50 BROKER/IB OUTREACH (2) — 50 email + 50 LinkedIn, 5/day × 2 weeks from 5/13, in morning brief
- **DROP** Standalone Broker Dashboard Tile section — Sourcing List view captures it inbound.
- **DROP** Calder Buy-Side Advisor section — Kay doesn't recognize the name; not using any buy-side advisor firm.
- **DROP** Axial Per-Industry Split as standalone section — Axial is a marketplace, item folds into MARKETPLACE section.
- **DROP** Conference Broker Pipeline as multi-item section — collapsed to one verification item; pre-conference outreach + T+2 card processing owned by existing skills.

### External email replies (drafts saved, Kay sends)

- **APPROVE** Draft Saltoun annual review reply to [[entities/janet-crockett]] (Citrin Cooperman CC'd). Kay edited her own final version (captured in voice memory): "happy to confirm" opener instead of "thank you for sending"; dropped "Looking forward to hearing from you"; "All the best to you and the team" multi-stakeholder sign-off. Sent.
- **APPROVE** Draft Jeanne Wang (Village Search Partners) reply declining Coalition breakfast meetup citing conferences this week. Saved to Gmail Drafts.
- **APPROVE** Draft [[entities/brad-buser]] @ Aspect Investors reply confirming stay-connected for gap funding at LOI. Saved to Gmail Drafts.

### Kevin O'Connell LinkedIn outreach

- **APPROVE** Send LinkedIn Connect-note to [[entities/kevin-oconnell]] (President Hampton Pest Mgmt, formerly Toplands Capital searcher, Southampton NY). 4-5 voice iterations in chat converged on Kay's final version. Kay sent.
- **APPROVE** Create vault entities: `kevin-oconnell.md`, `hampton-pest-management.md`, `toplands-capital.md` with proper cross-wiki-linking.
- **APPROVE** Marked task done on tracker (Tue slot 8 ✅ via direct status update).

### Off-system / channel-alias resolution

- **APPROVE** Close Lauren Young loop — Kay wrote back via personal email (off-system). Memory written so future runs don't re-surface based on Gmail silence.
- **APPROVE** Confirm Allison Allen reply on 2026-05-11 from `admin@greenwichandbarrow.com` (not `kay.s@`). Memory written so future relationship-manager + email-intelligence scans search BOTH aliases.

### Morning task tracker updates

- **APPROVE** Add Saltoun annual review to Tue slot 1; Yahoo→Gmail migration (`kaystrash@yahoo.com` → `kaystrash23@gmail.com`) + bday/baby cards to inbox + tracker.
- **APPROVE** Mon retroactive logs: March P&L budget-manager (already run 5/11), Test day of full server run, ACG WOL Summit 1:1 requests sent, Travel confirms for Mid Search Summit + Women in Pest Mgmt week of 5/18, Allison Allen PWIPM Northeast Council ask.
- **APPROVE** Move Friday personal-admin items (SLD video, PSLF, GLP1, Lois gift) to Sunday — keep Friday clean for Harrison call + budget review + Coalition breakfast.
- **APPROVE** Move Granola transcript trigger item from Tue → Fri (gated on Harrison architectural-path discussion).
- **APPROVE** Thursday CLEARED (ACG NY WOL Summit all-day); both items moved to Wed.
- **APPROVE** Compact slot order after every move (no blank rows above filled items; pull up).
- **APPROVE** Reorder by project priority: Deal Aggregator > Quarterly Update > Thesis Deck > Website Rebuild.

## Actions Taken

### Personal task tracker
- **CREATED** Google Sheet `TO DO 5.12.26` (id `1ewqQshtN5pz8kmMTEvBZgAFy-0XB37-MVONkN_mdZmk`) with 6 tabs (Live Week, To Do, To Do Long Term, Projects, Myself Renewed Healthcare, Deal Aggregator Expansion).
- **CREATED** `scripts/build_tasks_sheet.py` (one-shot rebuild script for future yearly refresh).
- **REWROTE** `scripts/task_tracker.py` — full Sheets API rewrite. CLI surface unchanged. Snapshot-to-JSON replaces `.xlsx` backups. `lsof` guardrail dropped. API-quota retry added.
- **ADDED** `sync-done-status` verb + `--skip-sync` flag on `archive-todo`.
- **DEPRECATED** `scripts/build_tasks_excel.py`, `scripts/populate_tasks_from_motion.py`, `scripts/maintain_tasks_excel.py` (headers marked).
- **CREATED** `scripts/build_donut_charts.py` + `scripts/fix_donut_empty_days_and_theme.py` (one-shot builders).
- **UPDATED** `.claude/skills/task-tracker-manager/SKILL.md` + `memory/project_personal_task_tracker.md` + new `memory/project_task_tracker_sheets_migration_2026-05-12.md`.

### Deal Aggregator Expansion project tab
- **RESTRUCTURED** Tab from Gantt → flat checklist (Status / Section / Task / Due / Notes; weekly cols dropped).
- **POPULATED** 17 items across 11 sections (rows 6-22). Row 6 pre-checked ✅ (today's Sourcing List structure work).
- **UPDATED** Projects index row 3 for Deal Aggregator Expansion (Notes reflect 17 items / 11 sections).

### Sourcing List standardization
- **ADDED** 5 funnel-metrics columns to General Sources + Niche-Specific Sources tabs.
- **STANDARDIZED** Access column to 3-value enum (need to register / registered / public). Tooling-failure notes moved to Notes column.
- **STANDARDIZED** Type column to 3-value enum (marketplace / email newsletter / direct relationships). Combined sources collapsed to primary.
- **SORTED** General Sources, Niche-Specific Sources, and all 9 Intermediary Target List tabs alphabetically by Source/Firm column.

### Conference Pipeline reconciliation
- **UPDATED** `scripts/validate_conference_discovery_integrity.py` — added `AUTHORIZED_STATUSES` set, new `check_c` function rejecting unauthorized values, stripped 3 `Future / Map-Only` transitions from `ALLOWED_STATUS_PROGRESSIONS`, added 6 `NEW` → {decided} transitions, fixed `Registered` → `Registered Only` references.
- **UPDATED** `.claude/skills/conference-discovery/SKILL.md` + `headless-sunday-prompt.md` — replaced `Future / Map-Only` references with `NEW` convention; agents now write `NEW` on discovery.
- **UPDATED** Live Pipeline tab rows 42 + 57 from `Future / Map-Only` → `NEW`.

### Drive restructure (Kay executed; Claude proposed)
- Drive folders reorganized into channel-based subfolders inside `OPERATIONS` (PROPRIETARY SOURCING / INTERMEDIARY SOURCING). One unauthorized move by Claude (DEAL AGGREGATOR ANALYST → OPERATIONS) — matched Kay's intent, not reverted.

### Gmail drafts saved (Kay sends)
- **DRAFTED** Saltoun annual review reply (Janet Crockett + Citrin Cooperman CC) — Kay edited & SENT.
- **DRAFTED** Jeanne Wang Coalition breakfast decline (Village Search Partners).
- **DRAFTED** Brad Buser @ Aspect Investors gap-funding stay-connected reply.

### External outreach sent
- **SENT** Kevin O'Connell LinkedIn Connect note (Kay sent her own final version after voice iterations).
- **MARKED DONE** Saltoun reply (Tue slot 1 ✅) + Kevin outreach (Tue slot 8 ✅) on tracker.

### Vault entity creates
- **CREATED** `brain/entities/kevin-oconnell.md` (President Hampton Pest Mgmt, ex-searcher, Southampton NY).
- **CREATED** `brain/entities/hampton-pest-management.md` (East End LI pest control acquired by Kevin via Toplands 2016).
- **CREATED** `brain/entities/toplands-capital.md` (Kevin's traditional search vehicle).
- **CREATED** `brain/entities/carlos-nieto-dca.md` + `brain/entities/digital-capital-advisors.md` (tomorrow 9:30am meeting).

### Briefs
- **CREATED** `brain/briefs/2026-05-13-carlos-nieto-dca.md` (Wed 9:30am ESB meeting prep). DCA = tech IB; sector mismatch with G&B thesis; sell-side prospecting suspected.
- **CREATED** `brain/briefs/2026-05-15-harrison-wells-call-5.md` (Friday agenda: Granola MCP re-auth priority #1, Family Office architecture, conference-discovery regression, infra batch).

### Inbox captures
- **CREATED** `brain/inbox/2026-05-12-saltoun-annual-financial-review.md`
- **CREATED** `brain/inbox/2026-05-12-yahoo-to-gmail-migration.md` (`kaystrash@yahoo.com` → `kaystrash23@gmail.com`; typo on the Gmail address confirmed/corrected by Kay)
- **CREATED** `brain/inbox/2026-05-12-bday-and-baby-cards.md`

### Memory writes (~12)
- **CREATED** `memory/feedback_kay_outbound_includes_admin_alias.md`
- **CREATED** `memory/feedback_off_system_resolution_closes_loop.md`
- **CREATED** `memory/feedback_inbox_schema_enums.md`
- **CREATED** `memory/feedback_always_polite_and_warm.md`
- **CREATED** `memory/feedback_check_status_before_surfacing_carryover.md`
- **CREATED** `memory/feedback_no_state_paste_when_live_surface_open.md`
- **CREATED** `memory/feedback_compact_slots_after_move_or_clear.md`
- **CREATED** `memory/feedback_project_tab_notes_concise.md`
- **CREATED** `memory/feedback_folders_not_named_after_people.md`
- **CREATED** `memory/feedback_templates_live_in_master_templates_folder.md`
- **CREATED** `memory/user_outreach_voice_kay_canonical_phrases.md`
- **CREATED** `memory/project_task_tracker_sheets_migration_2026-05-12.md`

## Deferred

- **Quarterly update (Q1 FY26 wrap-up)** — Tue slot 7 today (stretch goal if time). If not done today, carries to Wed.
- **Thesis deck build** — Wed slot 4. Project priority #3.
- **Website rebuild** — Wed slot 5. Project priority #4.
- **Friday 5/15 Harrison call** — brief landed; topics: Granola architectural path (priority #1), Family Office architecture, conference-discovery validator regression discussion.
- **Sat 5/16 T+2** — verify conference-engagement skill fires on ACG broker cards and routes to Intermediary Target List.
- **Tue 5/13** — Carlos Nieto / DCA meeting 9:30am ESB. Brief landed.
- **Wed 5/13 onward** — 50 broker/IB outreach campaign begins (5/day × 2 weeks → 5/27), surface in morning brief daily.
- **Sam Singh DealsX API touchpoint** — confirm whether DealsX/KeyReach exposes REST API. Determines `dealsx-snapshot-refresh` build path.
- **Broker buy-box geography window** — lock decision (`feedback_broker_channel_opportunistic_floor` open since 5/3).
- **Calder Capital** — dropped from project; not pursuing buy-side advisor channel.
- **5/11 session-decisions reconstruction** — NOT done today; file remains missing. Continuation file `2026-05-11-3.md` is the only record. Low priority; calibration pipeline has the gap noted.
- **Stale Word lock files** in OPERATIONS root (`~$Lead Gen Job Description...`, `~$B Lead Gen Process Flow...`, `~$B List Building SOP...`) — Kay to trash from Drive UI.

## Open Loops

- **Donut chart preservation across Sunday archive ceremony** — `task_tracker.py archive` duplicates the live tab; charts duplicate with it but source ranges still point at `_donut_data` (persistent hidden tab). New live-week label will need new chart references on next Sunday rollover. Flagged in SKILL.md follow-up.
- **`reformat` verb additive only** — duplicate CF rules can stack on repeated runs. Future enhancement: delete-then-readd.
- **`report` verb stale-projects detection** — placeholder; needs per-Gantt-tab week-cell scan.
- **3 newly-added Deal Aggregator Expansion sections** (rows 18-22: SOURCING LIST STRUCTURE, INTERMEDIARY TARGET LIST, 50 BROKER/IB OUTREACH) — written without explicit section-by-section review. Kay to confirm wording when she returns.
- **Project tab subtitle** updated mid-session ("Section-grouped checklist — items checked as completed; rows strikethrough on done"). Stable; not an open loop, just a state note.
- **OPERATIONS root stale `~$...docx` lock files** — 3 zombies from past Word sessions; Kay to trash.
- **Templates moved out of MANAGER DOCUMENTS / G&B MASTER TEMPLATES by subagent error** — Kay moved them back herself. No follow-up.
- **CALL LOGS renamed to JJ by subagent** then back to COLD CALLING by Kay — correct end state. No follow-up.
- **Granola MCP auth lapse** — 4 days silent; needs re-auth in interactive session. Friday Harrison call agenda item #1.
- **Phase 4.5 post-call-analyzer-poll validation watch** — 48-72h after 5/10 Mac sidecar retirement. Server timer sole processor.

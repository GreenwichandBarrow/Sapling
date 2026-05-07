---
schema_version: 1.1.0
date: 2026-05-01
type: context
title: "Session Decisions — 2026-05-01 (Friday)"
tags: ["date/2026-05-01", "context", "topic/session-decisions", "topic/personal-task-tracker", "topic/skill-graduation", "topic/excel-tooling", "topic/dashboard-merge", "topic/intermediary-cleanup", "topic/launchd-debugger", "topic/morning-workflow", "topic/active-deals-cleanup", "topic/templates-doc", "topic/intermediary-target-list", "topic/conference-pipeline", "topic/acg-women-summit", "topic/npma-wipm", "topic/women-network", "topic/pest-industry", "topic/art-lawyers", "topic/association-heads", "topic/harrison-coaching", "topic/cetane-rejection", "topic/franchise-dedup", "person/harrison-wells", "person/bob-williamson", "person/denning-rodriguez", "person/dan-tanzilli", "person/hunter-hartwell", "company/wiggin-and-dana"]
---

# Session Decisions — 2026-05-01 (Friday)

Friday — full Friday workflow ran (email-intel, relationship-manager, weekly-tracker, health-monitor, calibration-workflow). Heaviest day of the week. Major themes: (1) **personal task tracker** graduated from one-off to managed skill (`task-tracker-manager`); (2) **dashboard M&A surface consolidation** — M&A Analytics + M&A Activity merged into one nested page; (3) **intermediary tab cleanup ceremony** — franchise-dedup × 8 tabs + 2 conference adds + Transworld brokers fix; (4) **launchd-debugger skill ship** v1 + v1.1 with failure-trigger architecture + niche-intelligence Tuesday hardening (ai-ops-5wx CLOSED); (5) **Active Deals 4-cluster cleanup** — 18 entity stubs created (entities count 127 → 145), 6 archived, 6 audited and stage-rolled-back; (6) **Templates V2-V8 LIVE EDIT** of G&B Intermediary Outreach Templates Drive doc with mid-flight Kay calibration (SBA stripped from V8 Lender, single-name-drop for warm intros, 12-investor capital-credibility line in body); (7) **Intermediary Target List major cleanup** 172 → 162 rows + Industry Lawyers populated with 20 Art Lawyers (gender-audit 7 women) + Association Heads populated with 27 pest associations; (8) **Pest industry women network research** — 6 Brokers + 1 IB + 1 Lawyer added (Heather Rahilly @ Wiggin & Dana 100+ pest deals for EQT/Anticimex; Allie Allen @ NPMA = central PWIPM entry); (9) **Conference Pipeline 10-month forward extension** (May 2026 → Feb 2027), 21 new conferences mapped + 15 new host orgs; (10) **ACG NY Women of Leadership Summit 5/14** confirmed registered + IB-heavy 6-meeting strategy (TM Capital, Netrex, Candlewood, Capstone) — Hallie Berk send done; (11) **NPMA WIPM Forum 5/19-21 Charlotte NC** confirmed registered. Three email follow-ups triaged. 8 new memories saved.

## Decisions

### Personal task tracker workflow

- **APPROVE:** Mid-day capture flow — when Kay-actionable items surface in chat, surface ONE-line `RECOMMEND: Add to To Do — "X" / Type / Project / Due → YES/NO`. Both Kay and Claude write to the To Do tab; Claude moves items to per-day priority slots on Kay's instruction (never Kay drag — drag inherits source cell's conditional-formatting rules and breaks the destination grid).
- **APPROVE:** Capture trigger points — `goodmorning` capture pass at end of morning workflow + ad-hoc during midday conversation. NOT just briefing-time.
- **APPROVE:** Donut chart fix path C — delete openpyxl `DoughnutChart` objects from This Week tab; promote per-day % into the freed merged anchor cells (rows 17-21) at large 36pt sage-dark font; clear redundant row 22 % display. Reason: openpyxl-generated DoughnutCharts render blank on Excel-Mac due to OOXML compatibility. Trace-worthy: future agent might re-add charts.
- **APPROVE:** Re-apply strike+green conditional formatting on This Week priorities, To Do tab, To Do Long Term, Healthcare Gantt — verified rules exist in `scripts/build_tasks_excel.py:226-234, :363-368, :444-449, :669-674`. If broken in live file, manual edits overwrote them; fix is `reformat` verb (idempotent).
- **APPROVE:** Sunday rollover ceremony moves from manual to `goodnight` Sunday automation — copy live tab → hide as `archive_{label}` → rename live to next week's `Mmm D-D` → clear habit/priority/notes data. Date formulas already auto-update via TODAY().
- **APPROVE:** Tab-naming convention — live tab renamed each Sunday to current Mon-Sun range (`Apr 27-May 3`, `May 4-10`, etc.). Replaces static "This Week" name. Allows Kay to see week at bottom of Excel without opening tab. Date formulas tab-name-agnostic. Trace-worthy: future agent might keep tab statically named.
- **APPROVE:** Build `task-tracker-manager` skill (parallels `tracker-manager` for operational sheets but owns ONE personal file). Six verbs: `append`, `promote`, `archive`, `reformat`, `report`, `gantt-tick`. Reports to Chief of Staff. Trace-worthy: skill namespace separation matters.

### Skill graduation pattern

- **APPROVE:** When ad-hoc one-off (built ~5 days prior) starts requiring frequent Chief-of-Staff intervention, graduate to specialized subagent. Memory `feedback_remove_kay_from_loop` already covers automation-out, but graduation-from-one-off-to-skill is the inverse: Claude was doing it, Claude should NOT keep doing it ad hoc once lift increases. Surfacing pattern for review next calibration cycle.

### Dashboard — M&A Analytics + M&A Activity merge (this session)

- **APPROVE:** Nest "M&A Activity" (week-archive) inside "M&A Analytics" instead of running as a separate sidebar entry. Same surface across time → one page, not two. Kay flagged the duplication via screenshot at 10:24am.
- **APPROVE Path A (nested at bottom of page)** over Path B (full single-page selector merge). Path B deferred until DealsX zones go live May 7 and zone layouts can be unified. Kay's specific direction: "tabs at the bottom, not the top" — implemented as inline section divider + week-archive section nested below the live page-note.
- **REJECT** standalone "Weekly Archive" sidebar rename. Architectural reasoning (nested same-surface) cleaner than rename-only. Trace-worthy: codifies "same-surface across time = nested view" UI principle.

### Email triage — three new follow-ups (from `email-scan-results-2026-05-01.md`)

- **REJECT** reply to Bob Williamson (Cetane Associates) VRA offer. Cetane is **sell-side** advisory; the free Value Range Analysis is a sell-side prospecting tool offered to OWNERS, not a buy-side deal pipeline. Wrong layer for our buy-side intent. NJPMA warm intro maintained but no further outreach. See `[[inbox/2026-05-01-bob-williamson-cetane-vra-followup]]`. Trace-worthy: future agent could mistake free-VRA gesture for warm-intermediary signal.
- **DEFER** Rebekah Stender (Inzo) IT/cybersecurity due-diligence intro → post-LOI bucket. No active deal at LOI stage; revisit when first deal hits LOI.
- **REJECT (polite decline)** Natalie Evans (Methodnode) outbound deal-flow vendor. Same lane as DealsX, which is already our cold-email infra layer per `feedback_dealsx_is_cold_email_infra`.

### Intermediary tab cleanup ceremony (8 tabs + 2 conferences)

- **APPROVED + EXECUTED** franchise-dedup pass across all 8 intermediary tabs: Associations, Brokers, Corp Advisors, CPAs, Family Offices, IBs, Lawyers, Lenders. Each had its own pre-write rollback snapshot + post-write dedup snapshot in `brain/context/rollback-snapshots/`.
- **APPROVED + EXECUTED** intermediary-associations-conference-hosts add (NPMA + others), intermediary-associations-pest-add, intermediary-lawyers-denning-add, intermediary-brokers-transworld-fix (col J error diagnosis → row repair, see `[[inbox/2026-05-01-brokers-tab-col-j-error-diagnosis]]`).

### Conference Pipeline tab maintenance

- **APPROVED + EXECUTED** ACG Women Leadership Summit add → ACG Women dedup-fix follow-up (cleared duplicate row created during the add) → NPMA-WIPM status update → conference-pipeline-extension cleanup pass.

### Skill / infrastructure builds

- **APPROVED + EXECUTED** `launchd-debugger` skill ship — `SKILL.md` + `headless-daily-prompt.md` + `headless-on-failure-prompt.md` written; `run-skill.sh` updated to route the new modes; `brain/trackers/health/known-incidents.json` initialized (suppression registry for launchd-debugger Slack noise).
- **APPROVED + EXECUTED** `niche-intelligence` `headless-tuesday-prompt.md` added (graduates the Tuesday-night fire to the mutating-skill-hardening pattern per `feedback_mutating_skill_hardening_pattern`).

### Vault / entity work

- **APPROVED + EXECUTED** `[[entities/mm-environmental]]` entity stub created (untracked — captured in goodnight commit).
- Granola call notes from 4/30 ingested as `brain/calls/`: `anacapa-qofe-webinar`, `harrison-wells-coaching-session`, `team-tb-camilla-kay`. Two new entities created (`hollywell`, `mike-hollywell`) for the Q-of-E vendor lead.

## Actions Taken

- **CREATED:** `/Users/kaycschneider/My Drive/STRATEGIC PLANNING/TO DO 4.26.26.bak.20260501-171110.xlsx` — pre-maintenance backup of live xlsx.
- **CREATED:** `scripts/maintain_tasks_excel.py` — bootstrap one-shot maintenance script (donut delete + percent promotion + conditional-formatting reapply + tab rename). Idempotent.
- **CREATED:** `.claude/skills/task-tracker-manager/SKILL.md` — full skill definition (when-to-invoke, verb contracts, decision matrix auto vs surface-for-approval, hard guardrails including lsof file-lock check + backup-before-write + trace-every-write + tab-name validation).
- **CREATED:** `scripts/task_tracker.py` — skill helper with six argparse subcommands (append/promote/archive/reformat/report/gantt-tick). Each verb backs up the live file, lsof-checks before opening, writes a trace under `brain/traces/{date}-task-tracker-{verb}-{slug}.md`, echoes single-line confirmation/refusal.
- **REGISTERED:** New skill auto-loaded into Claude Code skill list — visible in system reminder.

### Dashboard merge (auto-committed in `e7a45f0` at 17:00 ET)

- **UPDATED:** `dashboard/theme.py` — removed "M&A Activity" from `NAV_ITEMS`; added `gb-archive-divider` + `gb-archive-section-head` CSS.
- **UPDATED:** `dashboard/command_center.py` — removed `week_archive` import + page-registry entry.
- **UPDATED:** `dashboard/pages/week_archive.py` — moved week selector from sidebar → inline column-constrained dropdown with new section header.
- **UPDATED:** `dashboard/pages/ma_analytics.py` — appended divider + `week_archive.render()` call after the live page-note.

### Skill / infra writes (earlier today)

- **CREATED:** `.claude/skills/launchd-debugger/SKILL.md`, `headless-daily-prompt.md`, `headless-on-failure-prompt.md`.
- **CREATED:** `.claude/skills/niche-intelligence/headless-tuesday-prompt.md`.
- **UPDATED:** `scripts/run-skill.sh` (route new headless modes); `CLAUDE.md` (launchd-debugger row + niche-intelligence hardening note).
- **CREATED:** `brain/trackers/health/known-incidents.json`.

### Vault writes

- **CREATED:** `brain/calls/2026-04-30-anacapa-qofe-webinar.md`, `brain/calls/2026-04-30-harrison-wells-coaching-session.md`, `brain/calls/2026-04-30-team-tb-camilla-kay.md`.
- **CREATED:** `brain/entities/hollywell.md`, `brain/entities/mike-hollywell.md`, `brain/entities/mm-environmental.md`.
- **CREATED:** 11 inbox items dated 2026-05-01 (bob-williamson, brokers-tab error, build-discuss-skill, build-learnings-md-pattern, dodo-digital-may-invoice, harrison-ask-mcp-install, harrison-secure-api-key-tool-name, harrison-server-setup-email-watch, natalie-evans-methodnode, prep-harrison-call-may-15, rebekah-stender-inzo-it).
- **CREATED:** `brain/notes/weekly/2026-05-01-deal-aggregator-digest.md`, `brain/trackers/weekly/2026-05-01-weekly-tracker.md`.
- **CREATED:** Morning artifacts — `email-scan-results-2026-05-01.md`, `relationship-status-2026-05-01.md`, `deal-aggregator-scan-2026-05-01.md` + afternoon variant.

### Sheet operations

- **UPDATED:** Industry Research Tracker — Conference Pipeline tab (ACG Women Leadership add + dedup fix, NPMA-WIPM status, conference-pipeline-extension cleanup). Rollback snapshots written.
- **UPDATED:** Intermediary tabs (Associations, Brokers, Corp Advisors, CPAs, Family Offices, IBs, Lawyers, Lenders): franchise-dedup pass + targeted adds (associations conference hosts, associations pest, lawyers denning, brokers Transworld fix). All with rollback snapshots in `brain/context/rollback-snapshots/`.

## Deferred

### Carried in / created today (existing as inbox items)

- **Build `/discuss` (or `/think`) skill** — Harrison's recommendation from 4/30. Strategic-conversation phase BEFORE plan mode. See `[[inbox/2026-05-01-build-discuss-skill]]`. Trigger: when Kay decides to ship a calibration-pipeline upgrade.
- **Add `learnings.md` pattern to skills** — Harrison pattern. Pilot suggestion: pipeline-manager or target-discovery. See `[[inbox/2026-05-01-build-learnings-md-pattern]]`.
- **Prep Harrison call May 15** — `[[inbox/2026-05-01-prep-harrison-call-may-15]]`. Trigger: 2026-05-14.
- **Harrison engagement renewal decision** — Re May renewal at $1,200/mo. Trigger: when Harrison's scope email lands.
- **Dodo Digital May invoice** — Due today (2026-05-01). `[[inbox/2026-05-01-dodo-digital-may-invoice-due-today]]`. Goes overdue tomorrow if unpaid.
- **Three Harrison infra inbox items**: `[[inbox/2026-05-01-harrison-ask-mcp-install]]`, `[[inbox/2026-05-01-harrison-secure-api-key-tool-name]]`, `[[inbox/2026-05-01-harrison-server-setup-email-watch]]`. Trigger: scheduled work block on Claude infra.
- **Rebekah Stender Inzo intro** — post-LOI bucket. Trigger: first deal hits LOI.
- **Hollywell as Q of E vendor option** — surface for first LOI'd deal. Working-capital gotchas baked into post-LOI checklist (per Granola action item).
- **Camilla XPX corporate-advisor referral** — aerospace/defense woman-owned business. Trigger: pursue if industry fits next active niche.

## Open Loops

### Personal task tracker (from earlier-evening write)

1. **Maintenance pass on TO DO 4.26.26.xlsx blocked on Excel close.** PID 24057 (Microsoft Excel) still has handle on the file. Wakeup polling stopped after 4-min wait per Kay's instruction. When Kay Cmd+Q's Excel, run `python3 scripts/maintain_tasks_excel.py` — will delete charts, promote %, reapply CF, rename tab `This Week` → `Apr 27-May 3`. ~10 second run.
2. **Update `memory/project_personal_task_tracker.md` post-maintenance** to reflect new skill ownership + tab-naming convention + donut-fix decision. Do this AFTER maintenance run so the memory matches live file state.
3. **Wire `goodnight` Sunday step to call `task_tracker.py archive`.** Currently the skill defines the contract; the goodnight workflow doesn't yet branch on weekday=Sunday to invoke the verb. Add this Sunday before May 3rd evening rollover.

### Carried from `[[notes/daily/2026-04-30|session-decisions-2026-04-30]]` and re-checked tonight

4. **Axial activation gated on Membership Agreement / Success Fee disclosure** — still pending. Email to `help@axial.net` not yet replied. No change since 4/30.
5. **Calder Capital fee structure** — unknown. Pending first call. No change.
6. **BizBuySell profile completion** — incomplete. No change.
7. **William Hoffman LinkedIn DM** — sent 4/30, awaiting reply. Not yet overdue (LinkedIn cadence longer than email).
8. **Andrew Lowis colleague intro** — Andrew personally replied 4/30 (relationship-status auto-resolved his cadence) but the colleague reach-out is a separate outstanding loop. Awaiting Axial colleague's outreach.
9. **Tech Stack Inventory Total Costs formula** — `SUM(D2:D18)` doesn't include rows 19-21. Stale by ~$24.95/mo. Bookkeeper or Kay to extend SUM range.
10. **Variations 2-8 of Templates Doc** — old framing still uncalibrated. No urgency-driver this week.
11. **Sub-agent's flagged edge cases from Attio cleanup (4/30)** — defaulted to recommendations; Kay never explicitly reviewed. Decay risk: low.

### New tonight

12. **Andrew Lowis 5/6 10am EDT meeting** — confirmed; brief generation should fire Tuesday morning briefing.
13. **Ninad Singh Friday 12:30 ET (today)** — Kay confirmed window 4/30. Outcome unknown without explicit confirmation in this session.
14. **Untracked at goodnight** — `mm-environmental.md` entity, ~11 rollback-snapshot JSONs from today's intermediary cleanup, scripts (`maintain_tasks_excel.py`, `task_tracker.py`, `scan_launchd_failures.py`, `validate_launchd_debugger_integrity.py`, `validate_niche_intelligence_integrity.py`). Goodnight commit captures all.

## Additional Decisions (later-session arc)

### Morning briefing items (5 total — Friday triumvirate ran clean)

- **REJECT:** Bob Williamson Cetane reply (PASS upgraded to formal REJECT). Cetane = sell-side; free VRA = sell-side prep tool. Inbox item closed as SKIPPED. Same call as the email-triage above; surfaced again in Decisions per briefing flow.
- **DONE:** Harrison Wells coaching $1,000 May invoice already paid before briefing surfaced. Inbox item closed as DONE. May coaching engagement active through 5/31. First May session 5/15 12-1pm ET.
- **APPROVE:** Active Deals cleanup bundle. 18 vault entity stubs created (entities count 127 → 145). 6 archived to Closed/Not Proceeding (Genser 109d, ARCIS sub-floor, Freedman sub-floor, Clark Fine Art CA, Fine Art Shippers, VF Global). 6 audited (all 0 Gmail hits → 5 stage-rolled-back to Identified, 1 left as Identified with note). Active Deals: 18 → 12 in pipeline + 6 archived.
- **REJECT:** Cold-but-live insurance nudge batch. Channel-routing rationale: DealsX owns insurance re-engagement, not Kay direct. Saved as `feedback_cold_relive_insurance_dealsx_channel.md`.
- **PASS:** Friday nurture cluster ([[entities/kristina-marcigliano|Kristina Marcigliano]] + [[entities/hunter-hartwell|Hunter Hartwell]] + [[entities/dan-tanzilli|Dan Tanzilli]]). Kay said no, all do not need to be addressed.

### Active Deals 4-cluster framework (durable triage method)

- **APPROVE:** Stale-pipeline triage uses 4 clusters: Dead / Cold-but-live / Process-broken / Genuinely-active.
- **APPROVE:** Decision rule per cluster:
  - **Dead** (zero activity 90+ days, no path forward) → archive to Closed/Not Proceeding (6 deals)
  - **Cold-but-live** (last touch >30d, no Gmail hits but still open) → audit + stage-rollback to Identified, leave note (5 deals)
  - **Process-broken** (stuck stage with no clear next action) → 1 left as Identified with note for next sprint
  - **Genuinely-active** (recent touch + Gmail evidence) → leave alone (12 deals)
- **APPROVE:** Audit method: 0 Gmail hits in 30 days = stage-rollback default; only override with explicit reason.

### Templates V2-V8 LIVE EDIT (G&B Intermediary Outreach Templates Drive doc)

- **APPROVE:** First pass: V2-V8 rebuilt per V1 BROKERS pattern. SHARED CORE Footer Reference + WARM-INTRO LANGUAGE BANK additions.
- **REJECT:** SBA references in V8 Lender. Kay flagged G&B equity structure won't qualify for SBA — stripped from V8 entirely.
- **REJECT:** Enumerate Guillermo's 9-firm lender list in V8. Single-name-drop pattern for warm intros, not full enumeration. Cleaner footer, doesn't burn the relationship list.
- **APPROVE:** "12 investors" capital-credibility line moved into BODY of all V2-V8 (not just footer). Body-level signal of capital backing matters for intermediary trust.

### Intermediary Target List major cleanup

- **APPROVE:** Bulk row removals: 172 → 162 rows (10 removed: 4 brokers + 1 IB + 4 CPAs + 1 lender). 33 rows flagged for review.
- **APPROVE:** Two structural problems surfaced + queued for fix:
  1. Industry Lawyers tab had ZERO named partners (only firm names) → fixed via Art Lawyers add
  2. Association Heads tab was empty → fixed via 27-row pest association populate
- **APPROVE:** Brokers schema-drift fix: 45 rows realigned to canonical 16-col schema. [[entities/jeremy-black|Jeremy Black]] cluster verified as 10 distinct firms (NOT franchise dups). Final row count: 73 (1 header + 72 data).
- **APPROVE:** Brokers col J #ERROR fix: schema drift had phone numbers in LinkedIn col; 9 cells cleared.
- **APPROVE:** Franchise dedup pass — Transworld 6→1 (kept Sam Curcio NYC `scurcio@tworld.com`), First Choice Brokers 3→1, Murphy Business 2→1. 8 franchise dups removed total.
- Saved as `feedback_franchise_firm_one_entry_only.md`.

### Industry Lawyers — 20 Art Lawyer additions + warm-intro path

- **APPROVE:** 20 Art Lawyers added. Top 5: Wierbicki/Loeb, Noh/Pryor Cashman, Olsoff/Olsoff Cahill Cossu, Lever/Kurzman Eisenberg, Schindler/SCH.
- **APPROVE:** Gender-audit completed: 7 of 20 are women. Aligns with `feedback_women_network_priority`.
- **APPROVE:** [[entities/denning-rodriguez|Denning Rodriguez]] (Bellizio + Igel) added at row 26 as warm-intro path. Old firm-only Bellizio row 6 deleted (replaced by Denning).
- **APPROVE:** Attio Denning Rodriguez duplicates merged.

### Association Heads — 27 pest associations populated

- **APPROVE:** 27 pest associations populated from Premium Pest Management target sheet (NJPMA, NPMA, NYPMA, PPMA, NEPMA, CTPCA, PWIPM, TPCA, FPMA, PCOC, SCPCA, GPCA, NCPMA + 6 certs + 4 confs + 3 trade press).
- **APPROVE:** 12 of 13 pest assocs subsequently updated with named women leaders. NCPMA flagged as gap — all-male officers, no woman leader surfaced yet.
- Top contact identified: Allie Allen at NPMA = central PWIPM (Professional Women in Pest Management) entry point.

### Pest industry women network research (cross-tab additions)

- **APPROVE:** 6 new Brokers rows: 3 Cetane + 3 Lion Business Advisors.
- **APPROVE:** 1 new Investment Bankers row: Lauren Morera @ Heritage Holding.
- **APPROVE:** 1 new Industry Lawyers row: Heather Rahilly @ [[entities/wiggin-and-dana|Wiggin & Dana]] — 100+ pest deals for EQT/Anticimex.
- Saved as `feedback_women_network_priority.md` (with pest-industry refinement appended).

### Conference Pipeline 10-month forward extension (May 2026 → Feb 2027)

- **APPROVE:** 21 new conferences mapped + 15 new host orgs added to Association Heads + 7 women-led conference hosts identified.
- **APPROVE:** Calibration: dedup must use date+venue+host triple, NOT name-string match. Agent C adding to conference-discovery SKILL.md.

### ACG NY Women of Leadership Summit (5/14) — registration + IB-heavy meeting strategy

- **APPROVE:** Kay confirmed registered + attending. Conference Pipeline row 21 status updated `Discovered` → `Registered`.
- **APPROVE:** Duplicate row 80 (mistakenly added) deleted.
- **APPROVE:** ACG profile form filled out: Buyouts / Business Services + Financial Services / Mid Atlantic + New England / $1M-$24M deal size.
- **REJECT:** Initial proposal of 25 outreach drafts. Reframed: 6 in-person 1:1 meetings with IB-heavy focus.
- **APPROVE:** Top 6 IB picks surfaced by subagent: TM Capital (Gillespie + Kohli), Netrex Capital (Sadocha — insurance specialist), Candlewood (Hallie Berk), Capstone (Conway + Tolliver).
- **SENT:** First meeting request drafted + sent (Hallie Berk @ Candlewood, 10:20 slot).
- **DEFER:** Calendar gap flagged — event not on Google Cal yet.

### NPMA Women in Pest Management Forum (5/19-21 Charlotte NC)

- **APPROVE:** Kay registered + on calendar. Conference Pipeline row 28 updated to Registered.

### launchd-debugger v1.1 enhancements + ai-ops-5wx CLOSED

- **APPROVE:** v1.1 added on top of v1: known-incident registry, cross-day dedup, on-failure trigger architecture (auto-fire on every non-zero scheduled-skill exit), wrapper case for niche-intelligence:tuesday.
- **APPROVE:** ACTIVATED via `launchctl load`. First fire 5/2 5am ET. Failure-trigger live.
- **APPROVE:** ai-ops-5wx pre-suppressed in known-incident registry to avoid Slack spam during Agent B fix.
- **APPROVE:** ai-ops-5wx CLOSED — headless-tuesday-prompt + validate_niche_intelligence_integrity.py + plist mode arg + reload all wired. Tuesday 5/5 22:30 ET = production verification.

## Additional Actions Taken

### External sends (additional)

- **SENT:** Hallie Berk (Candlewood) ACG meeting request — 10:20 slot, 5/14 ACG NY Women of Leadership Summit.

### Drive doc edits (additional)

- **UPDATED:** G&B Intermediary Outreach Templates (V2-V8 LIVE EDIT). SHARED CORE Footer Reference + WARM-INTRO LANGUAGE BANK additions. SBA stripped from V8. Single-name-drop pattern for warm intros. "12 investors" line in body of V2-V8.

### Sheet operations (additional)

- **UPDATED:** Intermediary Target List — 172 → 162 rows (10 deletions + 33 flagged for review).
- **UPDATED:** Brokers tab — schema-drift fix on 45 rows, col J #ERROR fix (9 cells cleared), franchise dedup (Transworld 6→1, First Choice 3→1, Murphy Business 2→1, 8 dups removed total). Final: 73 rows (1 header + 72 data).
- **CREATED:** 20 Art Lawyer rows on Industry Lawyers tab. Plus Denning Rodriguez at row 26.
- **DELETED:** Old firm-only Bellizio row 6 (replaced by Denning).
- **CREATED:** 27 pest association rows on Association Heads tab. 12 of 13 pest assocs updated with named women leaders.
- **CREATED:** 6 new Brokers rows (3 Cetane + 3 Lion Business Advisors).
- **CREATED:** 1 new Investment Bankers row (Lauren Morera @ Heritage Holding).
- **CREATED:** 1 new Industry Lawyers row (Heather Rahilly @ Wiggin & Dana).
- **UPDATED:** Conference Pipeline — 21 new conferences mapped (May 2026 → Feb 2027). Row 21 (ACG NY Women of Leadership Summit 5/14) `Discovered` → `Registered`. Row 80 duplicate deleted. Row 28 (NPMA WIPM 5/19-21) Registered.
- **CREATED:** 15 new host orgs on Association Heads tab from conference extension.

### Vault writes (additional)

- **CREATED:** 18 vault entity stubs from Active Deals cleanup. Entities count 127 → 145.

### Active Deals archival

- **UPDATED:** 6 deals archived to Closed/Not Proceeding (Genser 109d, ARCIS sub-floor, Freedman sub-floor, Clark Fine Art CA, Fine Art Shippers, VF Global).
- **UPDATED:** 6 deals audited (0 Gmail hits) → 5 stage-rolled-back to Identified, 1 left as Identified with note.

### Memory writes (5 new + 1 updated)

- **CREATED:** `feedback_parallel_tracks_pipeline_during_build.md`
- **CREATED:** `feedback_cold_relive_insurance_dealsx_channel.md`
- **CREATED:** `feedback_franchise_firm_one_entry_only.md`
- **CREATED:** `feedback_women_network_priority.md` (with pest-industry refinement appended)
- **CREATED:** `feedback_gog_sheets_value_delimiters.md`
- **UPDATED:** `MEMORY.md` — indexed all 5 new memories

## Additional Deferred / Open Loops

15. **#25 conference-engagement T-7 fires** for ACG (5/7) + NPMA WIPM (5/12) — needs scheduling, but skill needs Gmail refactor first. (Manual invocation required for each conference; no auto-fire on Registered status.)
16. **#26 stale agent note on Conference Pipeline row 28** — flagged for cleanup pass.
17. **#27 conference-engagement Superhuman → Gmail refactor** — Agent B is doing this in parallel goodnight work.
18. **#29 conference-engagement bundled scheduling** — will run after refactor lands.
19. **Morgan Stanley row swap** (R5 vs R11 metadata richness question) — deferred; default = keep richer row, drop sparser.
20. **V2-V8 em-dash sweep on meta blocks** — passes pending after Templates LIVE EDIT.
21. **Conference Pipeline calibration codification:** dedup must use date+venue+host triple. Agent C adding to conference-discovery SKILL.md.
22. **Founder & CEO title recommendation** for Kay-Schneider title pending Kay's explicit confirmation.
23. **Apollo enrichment of pest associations** — deferred to "leave on file with firms".
24. **NCPMA gap research** — no woman leader surfaced; needs follow-up sweep.
25. **Cetane re-look** — Pam Giordano is Cetane woman director, but Kay declined Cetane after Bob Williamson sell-side rejection. Open question whether woman-director presence changes the call.
26. **Calendar add for ACG NY Women of Leadership Summit (5/14)** — event not on Google Cal yet.
27. **ACG outreach drafts pending** — 5 of 6 IB outreach drafts pending (Hallie Berk sent). TM Capital (Gillespie + Kohli), Netrex Capital (Sadocha), Capstone (Conway + Tolliver) still need drafts.
28. **NPMA WIPM Forum 5/19-21** — registration confirmed, no pre-conference outreach drafted yet (T-7 = 5/12).

## Calibration candidates

- **Pattern:** "one-off file" → "lift growing" → "skill graduation." Worth a feedback memory if it recurs (e.g., when the next one-off — possibly the budget tracker, dashboard scripts, or another ad-hoc — hits the same threshold). Single instance today, not yet 3x. Watch for next instance.
- **UI architecture principle:** "Same surface across time = nested view, not separate sidebar entry." Codified through M&A Analytics + Activity merge. Worth a feedback memory — saves the next dashboard surface from spawning a parallel "X Archive" sidebar entry.
- **Sell-side advisor pattern:** Free VRA / pre-sale audit / valuation tool offered by an "M&A advisor" = sell-side prospecting (advisor finds sellers, not buyers). Layer mismatch for our buy-side intent. Bob Williamson today; Cetane is the second sell-side firm encountered after Calder Capital rebuild work last week. Watching for third instance to graduate to feedback memory.

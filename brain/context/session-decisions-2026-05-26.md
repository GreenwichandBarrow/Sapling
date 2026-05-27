---
date: 2026-05-26
type: context
title: "Session Decisions — 2026-05-26 (Tue, day-after-Memorial-Day; Project Drone reversed, weekly-files refactor Phases 1-4 shipped, pest 10-co June head-to-head defined)"
tags:
  - date/2026-05-26
  - context
  - topic/session-decisions
  - topic/project-drone
  - topic/intermediary-doctrine
  - topic/dealsx-jj-windown-experiment
  - topic/task-tracker-refactor
  - topic/outreach-channel-separation
  - topic/email-intelligence-bug
  - person/carlos-nieto-dca
  - person/sam-curcio
  - person/james-emden
  - person/allison-allen
  - person/leigh-fryxell
  - person/oswaldo-ponce
  - status/done
---

# Session Decisions — 2026-05-26

Long Tuesday after Memorial Day. Two major doctrine shifts (three-lane intermediary intake + no-auto-retirement of verbs + pack-to-top tracker discipline), one deal reversal (Project Drone REJECT → active pipeline), one A/B test framing (pest 10-co June experiment as the wind-down decision criterion for DealsX + JJ), and a four-phase weekly-files architecture refactor of task-tracker-manager that auto-fires Sunday 5/31. Plus the usual: Helen Guo deal-newsletter parser fix, JJ tabs DealsX dedup, James Emden cleared.

## Decisions

### Deal pipeline

- **APPROVE (REVERSES 2026-05-20 REJECT):** [[entities/carlos-nieto-dca|Project Drone (Carlos Nieto / DCA)]] into active pipeline. NDA signed 5-23, CIM landed 5-25, Kay reply held the door 5-25 22:03 ET, Kay directed 5-26 to move forward. Drive ACTIVE DEALS / PROJECT DRONE folder structure + CIM + countersigned NDA filed; Attio company `08d198dc...` created with Active Deals list entry at "Financials Received"; Slack #active-deals 200 OK. Both 2026-05-25 conflict-escalation inbox items marked `resolved` pointing at new `2026-05-26-project-drone-cim-intake-deal-evaluation-trigger`. Company is a placeholder ("Project Drone") until CIM de-anonymized; Carlos's person record not yet linked. See [[brain/traces/2026-05-26-project-drone-reject-reversed]].

### Doctrine — outreach intake

- **APPROVE:** **Three-lane intake rule (NEW doctrine).** Intermediary-presented deal lead = default YES (admit to pipeline, evaluate properly, decline only post-CIM if criteria fail). Broker BLAST offering = SELECTIVE (screen at intake). Personal intro = default YES. Reverses prior REJECT-at-intake pattern. Thesis-shape mismatch alone no longer suppresses intermediary leads at intake. Memory: [[feedback-intermediary-lead-default-yes-broker-selective]]. See [[brain/traces/2026-05-26-three-lane-intake-doctrine]].

### Doctrine — outreach channel separation

- **APPROVE:** **Outreach channel universes stay separate (HARD rule).** No company appears in two channels' active target lists. Build-time dedup, REMOVE rows (not annotate-and-keep, retired pattern), Apollo enrichment AFTER dedup never before. First-touch channel owns until cadence closes. Memory: [[feedback-outreach-channel-universes-separate]] + [[feedback-jj-excludes-dealsx-touched-companies]] updated.

### Doctrine — verb retirement

- **APPROVE:** **No auto-retirement of user-visible verbs / skills / features without Kay's explicit review.** Soft-deprecate-then-remove pattern requires sign-off. Helpers (`_underscore`) are internal — refactor freely. User-visible surfaces (CLI verbs, slash commands, skills, config flags) — never. Memory: [[feedback-explicit-review-before-retiring-verbs]].

### Doctrine — task-tracker UI discipline

- **APPROVE:** **Pack-to-top for day tabs + Week tab.** Every writing verb keeps items packed at the TOP of the 15-slot range, no leading empty rows, no gaps between items. `reformat` extended to auto-compact gaps from manual deletes. Memory: [[feedback-task-tracker-pack-to-top]].

- **APPROVE:** **Week tab is FROZEN as Sunday plan-of-record once set; no mid-week mirroring from day tabs.** Drift between Week tab and day tabs during the week is information, not a bug. The "rebuild Week tab from current day tabs" anti-pattern (executed once today and corrected) is forbidden.

- **APPROVE:** **No time-blocking — item-list scheduling.** Don't propose "block this morning to draft X" framings. Item appended to To Do + placed on today + tomorrow's priority slots. Memory: [[feedback-no-time-blocking-item-list-scheduling]].

### DealsX + JJ wind-down

- **APPROVE:** **Pest 10-co June experiment as wind-down decision criterion.** Both channels produced 0 NDAs / 0 financials / 0 LOIs across full ramp (per [[brain/outputs/2026-05-26-dealsx-vs-jj-performance-analysis]]). Kay directive: drive a 10-company pest-management research effort through June (Kay + Claude). If 10-co effort wins by 6/30 (≥1 NDA OR ≥1 meaningful conversation + ≥3 positive replies @ 30% rate floor), wind down DealsX + JJ. If not, both stay. **Wind-down notices NOT sent this week — paused pending experiment outcome.** See [[brain/outputs/2026-05-26-pest-10-co-june-experiment-plan]] and [[brain/traces/2026-05-26-pest-10co-june-experiment-as-windown-test]].

### Task-tracker-manager weekly-files architecture

- **APPROVE (plan):** **Weekly-files architecture refactor.** Each Sunday `build-week` Drive-copies prior week's file → new `TO DO M.D.YY` file in `To Do Archive` folder. Day tabs become the SINGLE edit surface; Week tab cells are in-file formulas (`=Tue!B14` etc.) — live read-only mirror. Cross-file carryover-pull at rollover. No IMPORTRANGE (avoids manual auth click). See [[plans/peppy-leaping-honey]] and [[brain/traces/2026-05-26-weekly-files-architecture-choice]].

- **APPROVE (shipped):** Phases 1-4 + 6+ landed tonight (resolver + SheetsClient refactor + cross-file `cmd_build_week_v2` + sandbox rehearsal + `reformat` auto-compact). Phase 5 (first real rollover) auto-fires Sun 5/31 via `/goodmorning`. Phase 6 distribute-week retirement review deferred until post-5/31 usage data.

### Relationship + cadence

- **PASS:** [[entities/james-emden]] cleared from Attio next_action (lunch is scheduled — supersedes the "share scheduling windows for intro w/ Peter Shakalis" follow-up). Post-call-analyzer will set new next_action after lunch.

### Email-intelligence parser fix

- **APPROVE (shipped):** `email-intelligence` SKILL.md patched with `DEAL_NEWSLETTER` detection. Triggers per-listing extraction on Helen Guo / Acquiring Minds / Flippa / BizBuySell / Walker Deibel / Empire Flippers / Quiet Light / Synergy / Viking digests AND on body-structure pattern (`In Today's Issue` header + ≥2 numbered listings + structured deal-data). Explicit anti-pattern guard against the 2026-05-26 case-study coexistence bug (Helen Guo Member Spotlight section caused 5 listings to be misclassified "content marketing"). 5 Helen Guo 5/26 listings screened — none pass thesis (1 CA hard-exclude + 4 outside NY-sourcing-concentration). Tomorrow's 7am email-intelligence run will use the patched parser.

## Actions Taken

- **CREATED:** `scripts/tracker_sheet_resolver.py` (~200 lines) + `~/.claude/config/current-tracker-sheet.json` pointer
- **UPDATED:** `scripts/task_tracker.py` — `SheetsClient` accepts `sheet_id` constructor arg + `.current()` factory; new helpers `_drive_copy_file`, `_drive_move_file`, `_find_to_do_archive_folder_id`, `_stamp_recurring_day_tabs`, `_carryover_cross_file`, `_build_week_formulas`; new `cmd_build_week_v2`; `cmd_build_week` dispatcher with `--legacy` fallback; `--title-prefix` / `--no-pointer-update` / `--no-folder-move` test flags; day-tab A1 retitle in step 8 (today's bug fix); `cmd_reformat` extended with pack-to-top auto-compact
- **UPDATED:** `scripts/build_day_tabs.py` + `scripts/build_week_tab.py` — `--sheet-id` arg
- **UPDATED:** `.claude/skills/task-tracker-manager/SKILL.md` — weekly-files architecture doctrine, pack-to-top rule, retired-pattern flags
- **UPDATED:** `.claude/skills/email-intelligence/SKILL.md` — DEAL_NEWSLETTER detection (4 edit blocks)
- **UPDATED:** `.claude/skills/jj-operations/SKILL.md` + `headless-sunday-prep-prompt.md` — DealsX cross-reference step + Stop Hook check
- **UPDATED:** `.claude/skills/health-monitor/SKILL.md` + `pipeline-manager/SKILL.md` + `post-call-analyzer/headless-on-trigger-prompt.md` — resolver-driven sheet ID pattern
- **UPDATED:** `.claude/commands/goodmorning.md` — Sunday section rewritten for weekly-files auto-fire
- **UPDATED:** `memory/MEMORY.md` (index + 3 new entries) + `memory/project_personal_task_tracker.md` (weekly-files architecture) + `memory/user_task_management.md`
- **CREATED:** `memory/feedback_explicit_review_before_retiring_verbs.md`, `memory/feedback_outreach_channel_universes_separate.md`, `memory/feedback_task_tracker_pack_to_top.md`, `memory/feedback_no_time_blocking_item_list_scheduling.md`, `memory/feedback_intermediary_lead_default_yes_broker_selective.md` (5 new doctrine memories)
- **CREATED:** `brain/outputs/2026-05-26-dealsx-vs-jj-performance-analysis.md`, `brain/outputs/2026-05-26-pest-10-co-june-experiment-plan.md`, `brain/outputs/2026-05-26-cross-channel-dedup-audit.md`
- **CREATED:** `brain/inbox/2026-05-26-project-drone-cim-intake-deal-evaluation-trigger.md`; UPDATED prior 5-25 conflict-escalation items to `status: resolved`
- **CREATED:** `~/.claude/plans/peppy-leaping-honey.md` (weekly-files refactor plan, ExitPlanMode approved)
- **CREATED:** Drive ACTIVE DEALS / PROJECT DRONE / {CIM, FINANCIALS, LEGAL, DILIGENCE, CORRESPONDENCE} subfolder structure + filed CIM (6.1 MB) + countersigned MNDA
- **CREATED:** Attio Company `Project Drone` (placeholder) + Active Deals list entry at "Financials Received"
- **SENT:** Slack #active-deals 200 OK — Project Drone CIM filed notification
- **UPDATED:** Attio Person `james-emden` — `next_action` cleared (lunch scheduled)
- **UPDATED:** JJ Premium Pest Management `Call Log 5.26-5.29.26` tabs — 44 rows removed (DealsX overlap dedup, snapshot at `brain/context/rollback-snapshots/jj-dealsx-dedup-2026-05-26T17-23-52Z.json`), then 42 rows backfilled from Full Target List (Fri short by 13, still ≥20 floor)
- **UPDATED:** TO DO 5.24.26 sheet — Week tab + day tabs populated, Tue/Wed/Thu/Fri/Sat planned + Wed outreach emails (Krupa/Deborah/Hamptons/Jay/Jason), Mon recurring restored, Bday cards completed on Tue, Sun-Sat day tab titles updated to "May 24-30", Week tab rows 17-23 + 33-50 cleared of stale content, all day-blocks packed-to-top
- **UPDATED:** Dashboard JSON `brain/context/dealsx-weekly-snapshot.json` — week 5/18-5/22 row appended; weekly tracker vault snapshots `brain/trackers/weekly/2026-05-22-weekly-tracker.md` + `brain/trackers/weekly/2026-05-15-weekly-tracker.md` updated with DealsX metrics
- **UPDATED:** Weekly Tracker Google Sheet — DEALSX section added rows 55-61 on Weekly Detail (no numeric population pending time-axis refresh; Kay decision deferred)
- **DELETED (Drive):** 2 sandbox files (`[SANDBOX] TO DO 5.24.26` + `[SANDBOX-PRIOR] TO DO 5.17.26`) — permanent delete via `gog drive delete --permanent` after Phase 4 rehearsal
- **DRAFTED → NOT SENT:** Decline-with-calibration to Carlos Nieto — superseded by REVERSAL; no draft needed

## Deferred

- **Investor update Q1 draft** — top priority Wed 5/27 (this morning's slot consumed by financials work). Trigger: Wed AM. Placed on Week tab Tue slot 1 + Wed slot 2.
- **DealsX + JJ wind-down notices** — paused pending pest 10-co June experiment outcome. Trigger: 2026-06-30 verdict (per win/loss/inconclusive criteria in pest plan).
- **Phase 5 weekly-files first real rollover** — Sun 5/31 AM auto-fires via `/goodmorning`. Trigger: that date.
- **Phase 6 distribute-week retirement review** — needs post-5/31 usage data ("0 calls since rollover"). Trigger: 2026-06-07.
- **Allison Allen + Leigh Fryxell warm-intro asks** for pest firms 8-10 — pending Kay approval to send this week. Trigger: Kay confirmation.
- **Helen Guo 5/26 listings manual sweep** — offered earlier, low-value per thesis screen (1 CA exclude + 4 outside thesis). Trigger: Kay says yes.
- **Weekly Detail Google Sheet time-axis refresh + DealsX backfill** — Kay decision pending. Trigger: Kay says yes/no.
- **Other DCA AI-exposed tech deal REJECT (5-20)** — three-lane doctrine MAY reverse this too; surface for Kay. Trigger: Kay reopens.
- **Post-call-analyzer silent-crash root cause** — Oswaldo Ponce 12pm call queued at 1pm, headless detached wrapper crashed without logs. Trigger: investigate before tomorrow's 1pm/6pm polls.
- **14 stale Gmail drafts** — not addressed today; related to investor update + wind-down work in flight.

## Open Loops

1. **Project Drone direction post-CIM-review** — Kay reviews CIM, deal-evaluation continues from `Financials Received` stage.
2. **James Emden lunch** — calendar set; post-call-analyzer will set new `next_action` after.
3. **Allison Allen + Leigh Fryxell warm-intro approval** — bottleneck for pest firms 8-10.
4. **Post-call-analyzer Oswaldo note** — stuck in queue (`brain/trackers/post-call-analyzer/queue/not_Gn4BVFoV13pDKF.json`); re-trigger needed or root cause fix.
5. **Sun 5/31 first weekly-files rollover** — auto-fires via `/goodmorning` Sunday AM.
6. **Investor update draft** — Wed 5/27 top priority.
7. **DealsX Google Sheet section** — Kay decision on time-axis refresh + backfill.

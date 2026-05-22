---
schema_version: 1.0.0
date: 2026-05-21
task: Thursday meta-calibration — 38 traces from 2026-05-15 through 2026-05-20 + 6 Thursday buckets
agents: [coordinator, architecture-strategist, simplicity-advocate, pattern-recognizer]
status: active
tags: [date/2026-05-21, agents, calibration, trace]
---

# Agent Chatroom: Calibration Analysis 2026-05-21

## Coordination Log

### coordinator -> OPEN [2026-05-21]
Calibration room is OPEN. Scope: 38 traces (2026-05-15 → 2026-05-20) + 6 Thursday buckets.

Expected agents (parallel):
- architecture-strategist
- simplicity-advocate
- pattern-recognizer

Protocol:
1. Each agent reads traces, posts findings to this chatroom.
2. Each agent appends "-> READY" when complete.
3. Once all three are READY, I post "-> CLOSE" and synthesize.

Format for each proposal:
- target_file (skill SKILL.md, memory/*.md, CLAUDE.md, schema, hook)
- importance: critical | high | medium | low
- concrete change (text to add/modify/remove)
- trace evidence (filenames or "cross-cutting")
- one-line rationale

Deadline: keep findings tight. Each agent ≤ 1,500 words. Critical/high-confidence > exhaustive.

Begin.

## simplicity-advocate findings

Lens: cut, don't add. Generic-playbook scaffolding gets pruned. The week's signal is unmistakable — Kay corrected over-engineering at every level (don't pad a list, don't add a maintenance agent, don't repoint dashboard, don't add Mac↔VPS sync, don't keep snapshot templates, single tab not multi-tab tracker, strict metric reading 0 not loose metric reading 4-but-wrong). The system should match.

### Proposal 1 — DELETE 13 task-tracker operational "traces" (and stop generating them)
- **target_file:** `brain/traces/2026-05-17-task-tracker-schedule-to-day-slot-*.md` (10 files), `2026-05-17-task-tracker-archive-todo-sweep-3.md`, `2026-05-17-task-tracker-reformat-rules-reapplied.md`, `2026-05-17-task-tracker-build-week-2026-05-17.md`, `2026-05-17-task-tracker-distribute-week-2026-05-17.md`, `2026-05-15-task-tracker-recurring-add-tue-row6.md`, `2026-05-15-task-tracker-recurring-remove-row6.md`, `2026-05-18/19-task-tracker-move-day-item-incomplete-*.md`. Also fix `task-tracker-manager` SKILL to stop emitting them.
- **importance:** high
- **rationale:** These fail the litmus ("would a future agent make a different choice without knowing this?"). They are receipts — "fri-2 slot filled," "swept 3 rows," "applied 16 conditional-format rules." Pure verb logs. They drown the real traces (pest list, dashboard-no-agent, network-driven-thesis) in the queue Kay reviews. Receipts belong in rollback snapshots (which already exist at the path each file cites); they do not belong in `brain/traces/`. 13 of 24 May-15→20 traces are noise — over half the calibration input was structurally junk.

### Proposal 2 — DELETE 13 dated session memories (March/April 2026)
- **target_file:** `memory/project_session_march_19.md` through `project_session_april_4.md`, plus `project_monday_march_23.md`, `project_tuesday_march_24.md`, `project_testing_day_march20.md`, `project_testing_weekend_march21.md`, `project_pending_march_27.md`, `project_morning_report_march21.md`, `project_niche_discovery_march20.md`, `project_architecture_optimization_march24.md`, `project_thursday_morning_items.md`, `project_april_focus.md`, `project_april_goal.md`.
- **importance:** high
- **rationale:** 567 memory files is unreadable. MEMORY.md is already over its 200-line budget per the system warning. Dated session snapshots from March/early-April are point-in-time scratchpads — nothing in them is durable doctrine that isn't already captured in a `feedback_*` file or charter file. They contribute to the recall-degradation problem CLAUDE.md flags. Bulk-delete by date pattern.

### Proposal 3 — DELETE stale weekly-tracker memories AND retire the skill
- **target_file:** delete `memory/project_weekly_tracker_audit.md`, `project_weekly_tracker_status.md`, `reference_weekly_tracker.md`. Move `.claude/skills/weekly-tracker/` to retired (or delete outright).
- **importance:** high
- **rationale:** Trace `2026-05-17-no-weekly-tracker-sheet-repoint.md` is explicit: "The M&A Analytics page already implements a 9-snapshot weekly archive. The Sheet was never populated because weekly-tracker has never actually run." Skill is 752 lines (3.7x archetype cap per its own warning). Three memory files describe a March-22 audit and March-17 build status of a skill that never produced data. The dashboard already owns this capability. Retire the skill, delete the memories. (Don't be talked into "fix the skill" — the trace already rejected that path.)

### Proposal 4 — REMOVE Cursor-terminal references; update mac-first memory
- **target_file:** `memory/feedback_mac_first_not_mobile.md` (rewrite: drop "Cursor terminal" and "Mac" specificity → "Kay's morning entry is the VPS terminal via SSH from whichever machine she's on"). Optional bonus: delete `project_branch_divergence_imac_vs_main.md` outright (its own header says "DISSOLVED, do not action").
- **importance:** medium
- **rationale:** Trace `2026-05-18-mac-macbook-thin-clients-single-vps.md` is explicit: no local repos, no Cursor, both Macs are pure SSH windows. The mac-first memory still says "Cursor terminal on Mac" and frames mobile-vs-Mac as the axis. Architecture change removed the problem class — retire the memory's old framing rather than keep answering it. Quote the trace: "When an architecture change removes a problem class, retire the problem's memory — don't keep answering it."

### Proposal 5 — COLLAPSE women-led memories from 3 active files to 1 canonical + 2 deprecation stubs
- **target_file:** keep `user_kay_women_led_purpose_throughline.md` as canonical. Reduce `feedback_women_network_priority.md` to a 3-line pointer ("Superseded by user_kay_women_led_purpose_throughline. Use that file."). Same for `feedback_industry_is_output_of_network.md` — fold its operational rules INTO the throughline file rather than maintaining a parallel structural-reframe file.
- **importance:** medium
- **rationale:** All three memories say overlapping things, with `feedback_women_network_priority` already carrying a "SUPERSEDED IN SCOPE" disclaimer at the top. Three files, one organizing principle, partial supersession = guaranteed drift. MEMORY.md already lists all three with cross-references trying to disambiguate scope. One canonical file with the full doctrine inside is simpler than a graph of partially-superseded files. The 2026-05-20 traces are explicit that this is one principle, not three.

### Proposal 6 — DELETE obsolete project/feedback files for retired channels and resolved problems
- **target_file:** `memory/project_branch_divergence_imac_vs_main.md` (resolved/dissolved), `feedback_linkt_cancelled.md` + `feedback_linkt_is_list_builder.md` + `feedback_linkt_api_requirements.md` (Linkt replaced by Apollo per other memories), `project_outreach_model_pivot.md` and `feedback_outreach_model_april.md` (April pivots now baked into current outreach-manager doctrine), `feedback_motion_api_python_not_jq.md` (Motion lapsing per `user_task_management.md`), `project_pending_march_27.md`, `project_thursday_morning_items.md`.
- **importance:** medium
- **rationale:** These are dated snapshots of resolved/abandoned states. Each one is a landmine — a future agent grepping for "Linkt" or "Motion" or "iMac branch" gets an answer that has been explicitly retired. The doctrine "retire the problem's memory, don't keep answering it" applies here too. Delete, don't archive.

### Proposal 7 — SHRINK CLAUDE.md "Pre-Flight Checklists" section by externalizing repeating rules
- **target_file:** `/home/ubuntu/projects/Sapling/CLAUDE.md` — the "Before writing any external message" bullet is ~16 dense lines, "Before handling secrets / config" is ~7. These are doctrine summaries of doctrine that already lives in `memory/feedback_*.md`. 
- **importance:** low-medium
- **rationale:** CLAUDE.md is loaded into EVERY session's system prompt. Every byte trades against working context. The checklists are valuable BUT each bullet already cites a `feedback_*` file as the source. The bullets repeat what they cite. Cut each bullet to the trigger + the action verb + the cite — drop the explanatory clauses. Example: "Recipient verified from verified source. Never guess/construct. See `feedback_never_guess_emails`." Not 4 sentences explaining bouncing. This is the equivalent of `feedback_strategic_thresholds_need_grounding` applied to CLAUDE.md itself.

### Proposal 8 — RULE: scheduled-skill VERB OPERATIONS should NOT auto-emit decision traces
- **target_file:** `.claude/skills/task-tracker-manager/SKILL.md` (and similar pattern in other CRUD-style skills). Add explicit instruction: do not write `brain/traces/` files for pure-mechanical verb runs (schedule-to-day-slot, archive-todo-sweep, reformat, build-week). Snapshot artifacts in `brain/context/rollback-snapshots/` are sufficient for rollback.
- **importance:** high (process)
- **rationale:** Root cause of Proposal 1. Skills are confusing "operational log" with "decision trace." Decision trace litmus: "would a future agent make a different choice WITHOUT knowing this?" Filling Tue slot 5 with TEST ROW does not pass that bar. This rule, codified, prevents the 13-receipts-per-week noise that hit this calibration cycle.

### Cross-cutting observation
Five of the highest-signal traces this week (`pest-list-keep-7`, `no-dashboard-maintenance-agent`, `no-maintenance-agent-fix-plumbing`, `no-weekly-tracker-sheet-repoint`, `todo-consolidation-weekly-cadence`, `mac-macbook-thin-clients-single-vps`) are all the SAME pattern: **reject the elaborate fix, fix the plumbing or accept the simpler real shape**. That is the meta-finding. The current system's bias is toward adding (agents, tabs, automation, sync). Kay's repeated correction is subtractive. Calibration should reward subtraction explicitly — perhaps a `#pattern/subtract-not-add` decision-trace tag that the briefing surfaces when 3+ accumulate in a week.

-> READY

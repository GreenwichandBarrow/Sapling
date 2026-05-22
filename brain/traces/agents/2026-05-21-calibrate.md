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

## architecture-strategist findings

**Lens:** structural gaps — where doctrine exists in `memory/` but execution skills don't enforce it; where one part of the system contradicts another; missing routing between skills. The recurring failure across this week's traces is that **memory hopes recall fires; execution-side skill text and hooks force it.** Kay keeps re-correcting the same drift because the drafting / scoring / routing skills never gate on the new rule.

Trace clusters reviewed: (A) women-led-throughline + industry-as-network-output [2026-05-20 x2], (B) intro-vs-deal classification [2026-05-20], (C) canonical-source-first credentials + templates [2026-05-19 x2], (D) thin-client VPS architecture [2026-05-18], (E) dashboard plumbing-not-agent [2026-05-17 x2 + parallel-session false alarm], (F) niche/JJ routing gates [2026-05-15, 2026-05-16, 2026-05-18 carlos], (G) conference auto-archival schema projection [2026-05-18], (H) gog false alarm [2026-05-16].

### Proposal 1 — CRITICAL — Wire women-led network gate into niche-intelligence + target-discovery + list-builder

**target_files:** `.claude/skills/niche-intelligence/SKILL.md`, `.claude/skills/target-discovery/SKILL.md`, `.claude/skills/list-builder/SKILL.md`

**Change:** Add a primary-gate referencing `[[feedback_industry_is_output_of_network]]` and `[[user_kay_women_led_purpose_throughline]]`:
- niche-intelligence Step 4 (SCORE) — add as a PRIMARY lock-in criterion BEFORE financial scorecard: "Female-led-network availability: name the women-led association/network in NY that Kay can plug into. If none exists → mark LOW lock-in regardless of financial fit. Software-grade negative control."
- target-discovery — before invoking list-builder, REQUIRE confirmed female-led network for the niche; if absent, surface as 🟡 to Kay rather than generating a list.
- list-builder — hard warning if asked to generate >50 targets for a niche without an associated female-led network ("1000-target screen drift — pull back to 3 buckets of 10").

**Trace evidence:** `2026-05-20-women-led-throughline-organizing-principle.md`, `2026-05-20-industry-is-output-of-network.md`.

**Rationale:** Highest-signal structural shift in the entire trace set. Grepping the skill tree finds ZERO references to women-led / network-driven / throughline. Memory exists; no skill enforces. Without skill-level gates, niche-intelligence keeps producing financially-scored sector recs and target-discovery keeps generating buy-box-screen lists — the exact drift Kay called out. Reverts within 2 weeks otherwise.

### Proposal 2 — CRITICAL — Add inbound-classification step to email-intelligence + outreach-manager BEFORE drafting

**target_files:** `.claude/skills/email-intelligence/SKILL.md`, `.claude/skills/outreach-manager/SKILL.md`

**Change:** Add a mandatory classification step that runs BEFORE any reply drafting. Four routes per `feedback_bias_yes_on_introductions`:
(a) Personal introduction → default-accept template; offer later time if timing bad; NEVER recommend decline.
(b) Specific deal pitch → fit-gate-evaluate; decline cleanly with calibration ("what to send next time").
(c) Warm-network check-in → cadence template.
(d) Advisor counsel → strategic-response template.

Hard rule: "If you find yourself recommending decline on category (a), STOP — the intro is not the pipeline."

**Trace evidence:** `2026-05-20-bias-yes-introductions-evaluate-deal-pitches.md` (HUMAN OVERRIDE — Kay lost a contact from prior agent advice).

**Rationale:** Verified cost-of-relationship miss. Current email-intelligence "Introductions Detected" surface treats intros as just one of N items, not as default-accept. Without skill-level classification before drafting, recurrence is guaranteed.

### Proposal 3 — HIGH — Acquirer-relationship-lifecycle gate in post-call-analyzer + outreach-manager

**target_files:** `.claude/skills/outreach-manager/SKILL.md`, `.claude/skills/post-call-analyzer/SKILL.md`

**Change:** When a call note or pipeline item tags an intro to "active PE roll-up / strategic acquirer in our buy-band" as high-value:
- post-call-analyzer must label `relationship_value: exit-and-intel`, NOT `deal-flow`, if the counterparty is a same-band consolidator.
- outreach-manager: do NOT generate "request the intro" as a same-cycle ask to the intermediary. Park as separate long-game thread.

**Trace evidence:** `2026-05-18-carlos-pe-rollup-intro-not-dealflow.md`.

**Rationale:** The post-call-analyzer's AI Analysis produced the BAD label ("highest-value asset, take forward") that flowed into the email draft. The skill itself produced the misroute; without lifecycle-stage logic in the analyzer, this exact failure repeats whenever an intermediary offers an active-acquirer intro.

### Proposal 4 — HIGH — Principal-only gate in JJ-routing

**target_file:** `.claude/skills/jj-operations/SKILL.md` (and outreach-manager JJ-Call-Only section)

**Change:** Pre-routing gate: "Named contact must be a principal/decision-maker. CSR / sales / admin / customer-service titles do NOT auto-route to JJ even when firm is niche-fit + blue-collar. Either enrich for owner contact first or park the card."

**Trace evidence:** `2026-05-16-bayonne-non-principal-no-jj-route.md`.

**Rationale:** AI proposed YES on Bayonne; Kay overrode. The heuristic "niche-fit + blue-collar = JJ" is durable enough it WILL fire again. Memory `feedback_jj_blue_collar_only` doesn't include the principal-level gate.

### Proposal 5 — HIGH — Retire Mac↔VPS sync guidance in project CLAUDE.md

**target_file:** `/home/ubuntu/projects/Sapling/CLAUDE.md` (Evening Workflow section)

**Change:** The current line `Commit AND push to origin — Mac↔VPS sync depends on every evening commit reaching remote` is now wrong. Replace with: `Commit AND push to origin — single VPS is source of truth; push for backup/redundancy. (No Mac↔VPS sync surface exists — both Macs are thin SSH clients.)` Also add to a new "Workflow Architecture" anchor: "Mac + MacBook are pure Tailscale-SSH thin clients into VPS. NO local repos. Machine switching = reconnect + `/pickingback`. NEVER generate `git pull origin main` advice for Kay's machines."

**Trace evidence:** `2026-05-18-mac-macbook-thin-clients-single-vps.md`.

**Rationale:** Project CLAUDE.md DIRECTLY contradicts the trace's correction. Loaded every session, so wrong guidance fires consistently. Architecture-class memory must update when architecture changes; doctrine "retire the problem's memory" applies to CLAUDE.md too.

### Proposal 6 — HIGH — Bake "check existing implementation before rebuilding" into plan-refinery + health-monitor

**target_files:** `.claude/skills/plan-refinery/SKILL.md`, `.claude/skills/health-monitor/SKILL.md`

**Change:** Pre-flight: "Before recommending a new data source, watchdog agent, or sheet repoint to fix unreliable data, grep across `dashboard/`, `scripts/`, and skill outputs for an existing implementation of the same capability. The default failure mode is 'never wired / never ran / different layer already covers it,' NOT 'needs new layer.' Reserve agents for judgment, never for plumbing reliability."

**Trace evidence:** `2026-05-17-no-dashboard-maintenance-agent.md`, `2026-05-17-no-weekly-tracker-sheet-repoint.md`, `2026-05-17-no-maintenance-agent-fix-plumbing.md`.

**Rationale:** Three traces in one day, same anti-pattern. plan-refinery is where alternatives get weighed; this is the natural gate. health-monitor should refuse to propose watchdog agents over silent-absence failures. Pairs with simplicity-advocate Proposal 3 (retire weekly-tracker skill).

### Proposal 7 — MEDIUM — Parallel-session order-and-read-fully gate in goodnight/pickingback

**target_file:** `.claude/commands/goodnight.md`

**Change:** Pre-escalation step: "If two `session-decisions-{date}.md` files exist for the same date, ORDER by timestamp before evaluating contradictions. Read the LATER session's actual Actions Taken in full (not the summary headline). A later session that USES an earlier session's artifact is complementary, not conflicting. Default to 'reconcile and explain,' not 'make Kay choose.'"

**Trace evidence:** `2026-05-17-parallel-session-tracker-architecture-conflict.md`.

**Rationale:** Direct decision-fatigue-mandate violation (manufactured a blocking decision). Parallel sessions keep happening; without an explicit gate, false escalation repeats.

### Proposal 8 — MEDIUM — DO-NOT-DRAFT banner on snapshot template files + canonical_template_guard hook

**target_files:** `brain/outputs/2026-05-04-broker-outreach-templates.md` (and any future "LOCKED FINAL" snapshots), new `.claude/hooks/canonical_template_guard.py`

**Change:** Prepend a loud banner to the snapshot file:
```
> WARNING: DO NOT DRAFT FROM THIS FILE.
> This is a creation-time snapshot, NOT the canonical template.
> Pull live: `bash scripts/fetch-template-doc.sh`
> Canonical Drive doc: 1gTQoCbaX8IyrTDli4Xd6IBtCqCT-DwciOUnNmgv0_J4
```
Add hook that blocks `Read` on `brain/outputs/*-templates.md` and redirects to the fetch script.

**Trace evidence:** `2026-05-19-stale-vault-snapshot-not-canonical-template.md`.

**Rationale:** "LOCKED FINAL" header is actively misleading — even the same-evening supersession note didn't stop drafting from it. Hook enforcement (per the op-env precedent) is the durable fix. Same meta-failure class as the 1Password skip — canonical-source-first is a pattern, hook it once.

## architecture-strategist coordination notes

Read simplicity-advocate findings. Overlaps and complements:

- **Complement (not duplicate):** simplicity Prop 3 (retire weekly-tracker skill) pairs with my Prop 6 (plan-refinery checks for existing impl before rebuilding). Hers removes the dead skill; mine prevents the next agent from rebuilding around it. Both should ship.
- **Complement:** simplicity Prop 5 (collapse 3 women-led memories to 1 canonical) pairs with my Prop 1 (wire the gate into skills). Hers consolidates the source; mine forces execution-side enforcement. Both should ship.
- **Complement:** simplicity Prop 4 (rewrite mac-first memory) pairs with my Prop 5 (fix project CLAUDE.md Mac↔VPS line). Hers fixes the memory; mine fixes the CLAUDE.md doctrine that's loaded every session. Both should ship — they're different surfaces.
- **No conflict** on simplicity Props 1, 2, 6, 7, 8 (deletions and CLAUDE.md shrinkage). My proposals are additive (wire gates into skills); hers are subtractive (delete cruft). Together they're net-neutral on system size while net-positive on enforcement.
- **Cross-cutting alignment:** simplicity's meta-finding ("subtract not add") and mine ("memory exists but skills don't enforce") are two sides of the same coin: the system over-adds memory files and under-wires execution. Both halves of the fix are needed.

-> READY

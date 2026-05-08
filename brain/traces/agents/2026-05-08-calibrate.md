---
schema_version: 1.0.0
date: 2026-05-08
task: Calibration analysis of 35 traces from 2026-05-01 through 2026-05-07
agents: [coordinator, architecture-strategist, simplicity-advocate, pattern-recognizer]
status: active
tags:
  - date/2026-05-08
  - trace
  - topic/calibration
---

# Agent Chatroom: Calibration Analysis — Friday 2026-05-08

Trace list: `/tmp/calibrate-trace-list.txt` (35 traces, May 1–7)

## Coordination Log

### simplicity-advocate — 2026-05-08 (working)
Reading 35 traces. 6 of them are task-tracker append-only logs (essentially backup receipts) which is the dominant complexity signal — auto-generated trace noise. Other simplification candidates:
- Two intermediary cadence revisions (5+5 → 7-total) churned the memory file twice in 48h.
- M&A Advisor classification rule and "two-way engagement" rule both tried to add binary refinements that Kay collapsed with one-sentence overrides.
- MEMORY.md is at 490 lines / 85.6KB with self-flagged bloat warning; multiple feedback files clearly duplicate (same-surface-nested, dashboard-same-surface-nested).
- Two "false alarm" traces (hung-jobs-false-alarm, capacity-letter routing) point to over-engineering of monitoring/escalation paths.
Filing proposals next.

### simplicity-advocate — READY
12 proposals filed below.

**Proposal S1** — Importance: critical
Target: `.claude/skills/task-tracker-manager/SKILL.md` (trace-emission policy)
Trace evidence: 2026-05-02-task-tracker-append-call-gusto-about-invoice-amount.md, 2026-05-02-task-tracker-append-submit-the-boys-to-ny-models.md, -state-models.md, -stellar.md, -teri-b.md, -zuri-model-and-talent.md (6 traces in one day, all identical-shape backup receipts)
What can be removed/simplified: task-tracker-manager emits a trace file per `append` verb invocation. These traces contain no decision (just task + row + backup path) — they're rollback receipts disguised as decision traces. They flooded `brain/traces/` with 6 entries in a single afternoon, polluting calibrate's input set. Backup paths are already in the .bak filename; rollback is already a `cp` away.
Concrete edit: Strip trace emission from the `append` verb. Keep traces for `archive`, `rollback`, and `reformat` (those have decision content). For `append`, write the rollback line to a per-day operational log at `logs/scheduled/task-tracker-{date}.log`, NOT to `brain/traces/`. Litmus per CLAUDE.md: "Would tomorrow's briefing present this differently if it knew?" Six identical-shape append rows: no.
Cost of keeping it: Calibration noise (6/35 traces in this batch were these — 17% of input was dead weight); MEMORY.md/trace-grep pollution; future calibrate runs spend tokens reading shapes-of-decisions.

**Proposal S2** — Importance: high
Target: delete `/Users/kaycschneider/.claude/projects/-Users-kaycschneider-Documents-AI-Operations/memory/feedback_dashboard_same_surface_nested.md`
Trace evidence: 2026-05-01-dashboard-nested-archive-not-sidebar.md
What can be removed/simplified: TWO memory files for the same rule: `feedback_same_surface_nested_view.md` (May 1) and `feedback_dashboard_same_surface_nested.md` (May 1). Both summarized in MEMORY.md index lines 47 and 68 with effectively identical content ("time-shifted views of same data = nested page, not parallel sidebar").
Concrete edit: Delete `feedback_dashboard_same_surface_nested.md` (the dashboard-specific narrower one). Keep `feedback_same_surface_nested_view.md` (the general principle). Remove MEMORY.md line 68.
Cost of keeping it: MEMORY.md already self-warns it's bloated at 490 lines; agents reading both will assume there are two distinct rules and try to apply both, generating phantom-distinction churn.

**Proposal S3** — Importance: high
Target: `/Users/kaycschneider/.claude/projects/-Users-kaycschneider-Documents-AI-Operations/memory/feedback_intermediary_outreach_7_per_day.md` (consolidate)
Trace evidence: 2026-05-05-intermediary-outreach-5-email-5-linkedin.md, 2026-05-06-cadence-misread-7-per-day-not-additive.md
What can be removed/simplified: Within 24h, the intermediary cadence rule was rewritten twice (5+5 split → 7 total). The 5+5 file was deleted, but the trace pair and the doctrine-rewrite pattern indicates these numbers churn with the campaign — they're not durable doctrine. The truly durable rule is "channel selection per-person + total-cap-not-additive-cap" — the specific number is operational state.
Concrete edit: Rename the memory to `feedback_intermediary_cadence_total_cap_not_additive.md` and rewrite to capture the DURABLE pattern (cap means total across channels, per-person tool selection, Apollo-no-match → LinkedIn). Move the current daily target number (7) to a campaign-state file or session-decisions where churn is expected. Update MEMORY.md line 158.
Cost of keeping it: Every cadence bump triggers a memory rewrite + agent confusion (the 5/6 trace shows COO already misread the bump direction once). Numbers belong in operational state, not memory doctrine.

**Proposal S4** — Importance: high
Target: CLAUDE.md "Pre-Flight Checklists" section, "Before writing any external message" sub-block
Trace evidence: 2026-05-04-broker-cadence-and-paths-pruned.md, 2026-05-04-day-5-voice-no-soft-signal-stacking.md, 2026-05-04-intermediary-template-doctrine.md, 2026-05-04-strip-user-context-from-public-copy.md, 2026-05-04-pe-vibe-comes-from-we-centric-copy.md
What can be removed/simplified: The pre-flight has bloated to a 12+ bullet checklist. Five 5/4 traces all hit the same root cause: ad-hoc drafting outside the canonical template. The template-doctrine bullet (already added) supersedes the older sub-rules ("don't fabricate Kay's inner state," "no fund/search-fund language," "lead with curiosity," "no em dashes," "no buy-box in body" — all live IN the templates already). Once the template is the source of truth, repeating its contents in the pre-flight is redundant.
Concrete edit: Collapse the 12-bullet pre-flight into 5 bullets: (1) verify recipient address, (2) for intermediaries, pull from canonical template before drafting (forbid ad-hoc), (3) lead with what THEY cared about (cite trigger language check), (4) plain text + no em dash + day-aware sign-off, (5) no Sunday sends + no stranger outreach. Move detailed voice-rules into the templates themselves where they're load-bearing at composition time.
Cost of keeping it: CLAUDE.md is in every system prompt — every redundant bullet costs tokens on every turn AND increases the chance Kay's actual rule (template-first) gets buried under stylistic noise.

**Proposal S5** — Importance: high
Target: delete `feedback_no_search_fund_language_intermediaries.md` OR collapse into template doctrine memory
Trace evidence: 2026-05-04-intermediary-template-doctrine.md, 2026-05-04-pe-vibe-comes-from-we-centric-copy.md
What can be removed/simplified: With the new template-doctrine rule (`feedback_no_intermediary_drafts_outside_template`), the no-search-fund-language rule is enforced by the templates themselves — Kay reviews voice ONCE in the canonical doc. A separate "don't say search fund" memory is now defensive code for a doctrine the template surface already enforces.
Concrete edit: Delete `feedback_no_search_fund_language_intermediaries.md`. Update MEMORY.md line 30 to remove. The template-doctrine memory's body should mention "voice rules live in the canonical templates — don't re-encode them as separate memories."
Cost of keeping it: Belt-and-suspenders memories for rules already enforced at the template layer create the impression that drafts can be written ad-hoc as long as the rules are followed — exactly the trap Kay flagged on 5/4.

**Proposal S6** — Importance: high
Target: `.claude/skills/pipeline-manager/SKILL.md` (orphan-PID detection logic)
Trace evidence: 2026-05-06-hung-jobs-false-alarm-stale-snapshot.md
What can be removed/simplified: Pipeline-manager has logic to flag scheduled jobs as "hung/orphan" based on log file size. Today this generated TWO 🔴 false-alarm Decisions, triggered launchd-debugger fan-out, and wasted Kay's morning attention on jobs that had already finished cleanly. The simpler answer: stop trying to detect liveness from log size at all. launchd-debugger ALREADY runs on every non-zero exit (per `feedback_launchd_debugger_failure_trigger`). Pipeline-manager re-implementing the detection in a different (worse) way is duplicate logic.
Concrete edit: Remove the orphan-PID / log-size-based "hung job" detection from pipeline-manager. Trust launchd-debugger's exit-code + POST_RUN_CHECK pipeline as the single source of truth. If pipeline-manager wants to surface a broken-system Decision, query the known-incidents registry, NOT log-size inference.
Cost of keeping it: Every false alarm is a Decision Kay must triage — directly violates `feedback_decision_fatigue_minimization`. Two false alarms today = the system actively damaged the briefing.

**Proposal S7** — Importance: medium
Target: delete `feedback_lauren_della_monica_dead_end.md`
Trace evidence: (none directly in this batch — but MEMORY.md line 76)
What can be removed/simplified: Person-specific "dead-end" memory for a single dormant contact. This is data, not doctrine. Belongs in Attio (status = dormant) or in the entity file body as a note, not in MEMORY.md.
Concrete edit: Delete the memory file. Move the rule "Lauren = dead-end, do not surface" to `entities/lauren-della-monica.md` body or set Attio status. Remove MEMORY.md line 76.
Cost of keeping it: Per-person memories don't scale. If we accumulate 50 of them as relationships sour, MEMORY.md becomes a CRM in markdown — a job Attio already does.

**Proposal S8** — Importance: medium
Target: collapse `feedback_classify_intermediary_by_self_id.md` into the M&A-Advisor=Broker rule
Trace evidence: 2026-05-04-ma-advisor-equals-broker.md
What can be removed/simplified: The 5/4 trace itself documents that the original `feedback_classify_intermediary_by_self_id` rule produced wrong answers on 7+ firms when applied literally. Kay's actual rule is simpler: "Investment Bank = explicit IB/FINRA self-ID. Everything else = Brokers tab." That's a one-sentence override; the multi-step self-ID heuristic is now noise.
Concrete edit: Rewrite `feedback_classify_intermediary_by_self_id.md` as a 3-line rule: "(1) Firm self-IDs as 'Investment Bank' or 'Investment Banking' explicitly + FINRA/SIPC = IB tab. (2) Everything else (incl. 'M&A Advisor', 'M&A Advisory', 'Business Brokerage') = Brokers tab. (3) When in doubt → Brokers." Delete the original heuristic's deeper reasoning.
Cost of keeping it: Future verification subagents will re-litigate the 7-firm misclassification because they see the broader heuristic and apply it before reaching the override.

**Proposal S9** — Importance: medium
Target: `.claude/skills/conference-engagement/SKILL.md` — classification step
Trace evidence: 2026-05-01-acg-conference-meeting-strategy-pivot.md
What can be removed/simplified: The trace identifies that the skill burned ~5,000 tokens producing 25 outreach drafts that were thrown out because the skill defaulted to "max attendee coverage" without classifying conference type first. The fix is a pre-execution classification (trade show vs curated summit), NOT additional drafting variants.
Concrete edit: Add the classification gate as the FIRST step of conference-engagement: read attendee count + ticket price + program format → if curated summit (<300 attendees, premium ticket, networking-format), output goes to 6-10 IB-heavy in-person meeting requests; if trade show, existing max-coverage flow. Surface classification to Kay BEFORE drafting any body copy. Don't add this as a new path — REPLACE the default with the gate.
Cost of keeping it: Each conference outreach campaign re-burns the 5K-token waste cycle.

**Proposal S10** — Importance: medium
Target: `feedback_email_intel_check_kay_outbound_first.md` + Granola-summary-insufficient pattern
Trace evidence: 2026-05-01-granola-summary-insufficient-for-coaching-calls.md, 2026-05-07 referenced memory
What can be removed/simplified: Two May-period rules added to email-intelligence: (1) cross-check Kay's outbound on a thread before flagging "needs reply" (2) for substantive calls, re-read full Granola transcript not summary. These are both "don't trust the surface artifact, check the source" rules. They could be one memory.
Concrete edit: Consolidate into a single memory `feedback_email_intel_check_source_not_summary.md` covering both: "Email-intelligence and pipeline-manager MUST verify against the source artifact (full Gmail thread, full Granola transcript) before generating action items. Surface summaries are necessary-but-insufficient." Delete the two narrower files.
Cost of keeping it: Two memories for one principle = future agents apply one and miss the other. The unified rule is the actual pattern.

**Proposal S11** — Importance: medium
Target: `feedback_no_clear_rewrite_populated_sheets.md` (note: rule + hook + deny-list overlap)
Trace evidence: 2026-05-04-universal-post-run-check-doctrine.md
What can be removed/simplified: The conference-discovery wipe incident produced FOUR layers of defense: (1) the memory rule, (2) the universal POST_RUN_CHECK doctrine, (3) the project deny-list `Bash(gog sheets clear:*)`, (4) the per-skill validator. Layers 3 and 4 actually prevent the failure mode. Layers 1 and 2 are documentation about it. The memory rule is a duplicate of the dashboard-green-can-lie + universal-validator memories.
Concrete edit: Delete `feedback_no_clear_rewrite_populated_sheets.md`. The deny-list rule + POST_RUN_CHECK validator on conference-discovery + `feedback_dashboard_green_can_lie.md` cover the same ground. Remove MEMORY.md line 164.
Cost of keeping it: When the same incident generates 4 defensive layers AND 3 memory entries, agents reading the memory file see what looks like 3 distinct rules and treat them as separate context — but they're one rule with redundant restatements.

**Proposal S12** — Importance: low
Target: CLAUDE.md "Scheduled Skills (launchd)" table
Trace evidence: 2026-05-07-server-replaces-mac-runtime.md, 2026-05-07-scheduler-adapter-synthesizes-plist-shape.md
What can be removed/simplified: The scheduled-skills table contains heavy provenance text inline ("Hardened with POST_RUN_CHECK validator + headless-tuesday-prompt 2026-05-01 (bead ai-ops-5wx closed)" etc.) — this kind of historical justification is for traces, not for the skill table. With the server migration locking the runtime model and POST_RUN_CHECK now universal per the 5/4 doctrine, every row's hardening provenance is redundant — readers can assume it.
Concrete edit: Strip per-row hardening provenance. Each row keeps: skill name, schedule, one-sentence purpose. Hardening status is universal (per the doctrine line above the table). Provenance lives in traces. Reduces the table from ~50 lines to ~20.
Cost of keeping it: CLAUDE.md is in every system prompt; the table is the densest passage. Every reader pays the historical-trace tax on every turn even though the doctrine line at the top already says "all hardened."

-> READY

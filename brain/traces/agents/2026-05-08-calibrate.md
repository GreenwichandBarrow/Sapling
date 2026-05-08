---
schema_version: 1.0.0
date: 2026-05-08
task: Calibration analysis of 35 traces from 2026-05-01 through 2026-05-07
agents: [coordinator, architecture-strategist, simplicity-advocate, pattern-recognizer]
status: completed
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

### architecture-strategist — 00:56
Read all 35 traces (frontmatter + Decision/Learning) plus pipeline-manager, email-intelligence, conference-engagement, investor-update, meeting-brief, deal-evaluation, relationship-manager SKILL.mds, plus weekly trackers for 2026-04-24 and 2026-05-01, plus existing memory index. Confirmed which traces have already produced memories and which structural fixes never landed in SKILL.md. Filing 8 proposals below.

**Pattern across the week:** the system keeps generating durable lessons in `memory/feedback_*.md` but failing to graduate them into SKILL.md sections where they're guaranteed to load. Memory is recall-dependent; SKILL.md is mandatory. Several 🔴-class incidents this week (Andrew/Guillermo crash-briefs 5/6, hung-jobs false alarm 5/6) recurred because the lesson lived in memory but not in the skill that needed to act on it.

**Cross-cutting flag for simplicity-advocate:** the `learnings.md` per-skill feedback loop pattern (currently piloted on pipeline-manager) is the right surface for skill-local anti-patterns — but several of my proposals put rules in SKILL.md proper rather than learnings.md because they are structural skill behavior, not anti-patterns to avoid. Don't conflate the two. Note: simplicity-advocate's S6 proposes REMOVING orphan-PID detection from pipeline-manager; my A1 proposes HARDENING it with `ps -p` verification. Recommend coordinator land on S6 (remove, trust launchd-debugger as SoT) — cleaner architecture and resolves my A1's structural concern as well. Treat A1's D+0 brief-preflight half as still-needed regardless of S6 outcome.

**Cross-cutting flag for pattern-recognizer:** sell-side advisor "free tool" pattern (Williamson 5/1, Calder 4/30) and template-doctrine pattern (5/4 traces) are both at 2 instances — graduating them is your call.

---

**Proposal A1** — Importance: critical
Target: `.claude/skills/pipeline-manager/SKILL.md`
Trace evidence: `2026-05-06-same-day-externals-preflight-gap.md`, `2026-05-06-hung-jobs-false-alarm-stale-snapshot.md`
Problem: Two structural pipeline-manager gaps each cost 🔴 incidents this week but the fixes only landed as memory files (`feedback_preflight_covers_today_and_tomorrow.md`, `feedback_pipeline_manager_ps_verify_before_orphan_claim.md`). SKILL.md still says brief-preflight covers "tomorrow's external meetings" and the hung-jobs detection logic still reasons from log size, not `ps -p`. Memory recall is unreliable mid-briefing; SKILL.md is loaded.
Proposed change: (a) Edit pipeline-manager SKILL.md brief-preflight section to enumerate D+0 + D+1, mirror the CLAUDE.md invariant (line 38 already requires it; SKILL.md must match). (b) For the hung-job detection: align with simplicity-advocate's S6 — remove pipeline-manager's orphan-PID logic entirely; defer to launchd-debugger + POST_RUN_CHECK as single source of truth. If S6 isn't accepted, fall back to `ps -p`-verification rule.
Risk if not done: Same two failure modes recur within 1-2 weeks. The 5/6 same-day-externals miss is the second instance in 3 weeks.

**Proposal A2** — Importance: high
Target: `.claude/skills/conference-engagement/SKILL.md`
Trace evidence: `2026-05-01-acg-conference-meeting-strategy-pivot.md`
Problem: Skill defaults to "max coverage of attendee list" regardless of conference type. ACG NY Women of Leadership triggered 25 drafts thrown out and pivoted to 6 IB-heavy 1:1s — wasting ~5,000 subagent tokens. The trade-show vs. curated-summit taxonomy is the missing classifier. (Convergent with simplicity-advocate S9 — same proposal.)
Proposed change: Add `<conference_classification>` Step-0 gate before any drafting: trade show (1000+ attendees) → max-coverage retained; curated summit (50-300 attendees, premium positioning) → 6-10 pre-set in-person 1:1 requests, IB/IB-adjacent filter first. Surface classification to Kay BEFORE drafting body copy.
Risk if not done: Each premium summit Kay registers for repeats the 25-draft pivot waste — at minimum once per month given conference-discovery's velocity.

**Proposal A3** — Importance: high
Target: `.claude/skills/email-intelligence/SKILL.md` AND `.claude/skills/post-call-analyzer/SKILL.md`
Trace evidence: `2026-05-01-granola-summary-insufficient-for-coaching-calls.md`
Problem: Granola summary treated as authoritative for downstream processing. Harrison Wells 4/30 coaching call dropped 5 action items + 4 promised emails when summary-only was used. Doubly important now post-call-analyzer is real-time (`feedback_post_call_analyzer_realtime_on_granola.md`, 5/7) — it'll process more substantive calls without the re-read gate.
Proposed change: Add Call Type Classification step in post-call-analyzer SKILL.md (routine vs substantive). Substantive (counterparty role contains coach/investor/deal/intermediary OR call duration >30min OR vault entity tagged `relationship_type: coach|investor|advisor`) routes to full-transcript-read mode. Email-intelligence inherits the same classification when surfacing Granola notes for briefing.
Risk if not done: Coaching/investor relationships erode silently as promised follow-ups slip. Harrison's renewal calculus partially depends on whether his asks land.

**Proposal A4** — Importance: high
Target: `.claude/skills/deal-evaluation/SKILL.md` (new section)
Trace evidence: `2026-05-01-active-deals-4-cluster-triage-framework.md`
Problem: 4-cluster triage framework (Dead / Cold-but-live / Process-broken / Genuinely-active) took Active Deals from 18 stale → 12 clean + 6 archived, but the framework is trapped in the trace; nothing in deal-evaluation knows it. Without it, pipeline hygiene devolves back into per-row debate within 60-90 days.
Proposed change: Add `<weekly_pipeline_hygiene_audit>` section to deal-evaluation/SKILL.md codifying the 4-cluster classification. Either schedule a weekly run (Friday morning, parallel to weekly-tracker) OR document the on-demand verb invocation. Stage-rollback as the Cold-but-live action is the structural innovation — call it out explicitly.
Risk if not done: Active Deals re-bloats. Pipeline metrics distort. Kay's review burden grows back.

**Proposal A5** — Importance: high
Target: `.claude/skills/investor-update/SKILL.md`
Trace evidence: `2026-05-04-capacity-letter-via-meeting-brief-not-email.md`, `2026-05-06-same-day-externals-preflight-gap.md`
Problem: The capacity-letter routing decision created a new pattern (entity-file `Pending Discussion Topics` consumed by meeting-brief generation) with no codified home. Per `feedback_recurring_investor_briefs_owned_by_skill.md`, recurring investor briefs should auto-fire from `investor-update` 24h ahead. Today investor-update SKILL.md has no auto-fire schedule, no Pending Discussion Topics protocol, and no claim of ownership for recurring briefs. The Guillermo 5/6 miss happened because nothing actually owned it.
Proposed change: Add `<auto_fire_schedule>` to investor-update/SKILL.md naming each recurring trigger (biweekly Guillermo, monthly Jeff, quarterly all-LP) with a per-cadence cron + 24h-ahead semantics. Add `<pending_discussion_topics_protocol>` instructing the skill to read entity-file Pending Discussion Topics and surface them in every prep brief, removing on Kay's confirmation. File a bead for the launchd timer wiring.
Risk if not done: Investor-meeting brief misses recur; one missed prep on a $10M LP is unrecoverable. Pending Discussion Topics pattern dies because no skill reads it.

**Proposal A6** — Importance: medium
Target: `.claude/skills/email-intelligence/SKILL.md`
Trace evidence: `2026-05-01-sell-side-advisor-free-tool-pattern.md`
Problem: Williamson (Cetane 5/1) is the second sell-side-advisor "free deliverable" instance after Calder Capital (4/30). Email-intelligence currently classifies any M&A-advisor inbound with a free-service hook as warm-intermediary. The free-deliverable signal points the wrong direction (sell-side prospecting). Pattern is at 2 — pattern-recognizer may pick it up but skill code is the structural fix.
Proposed change: In email-intelligence's Direct-classification path, add a sell-side-prospecting marker check: if sender role includes "M&A advisor" / "investment banker" AND body contains free-deliverable language ("free Value Range Analysis", "complimentary pre-sale audit", "free valuation", "what's your business worth", "sample valuation") → tag `sell_side_prospect: true` and downgrade warmth-signal in artifact (suppress from "warm intermediary" briefing surfaces). Personal-relationship layer untouched.
Risk if not done: Every new sell-side advisor warm-introduced re-litigates the classification call; engagement-fee discipline gets compromised.

**Proposal A7** — Importance: medium
Target: `CLAUDE.md` (new `## Runtime Architecture` section)
Trace evidence: `2026-05-07-scheduler-adapter-synthesizes-plist-shape.md`, `2026-05-07-server-replaces-mac-runtime.md`
Problem: Migration to server runtime introduces invariants (server-as-default, Granola-as-Mac-sidecar exception, scheduler-adapter as intentional shape-match) not yet documented in CLAUDE.md. Trace authors flagged both risks: a future agent may "clean up" `_scheduler_adapter.py` and break dashboard, OR move post-call-analyzer to server during cleanup and break Granola integration silently.
Proposed change: Add `## Runtime Architecture` section to CLAUDE.md with: (a) server-as-default rule + Granola sidecar exception, (b) scheduler-adapter as intentional shape-match abstraction (do not refactor without separate scope), (c) Phase 4 Granola output sync follow-up note. One paragraph each. Cite the two 5/7 traces.
Risk if not done: Within ~30 days, an agent doing "general cleanup" breaks one of these load-bearing invariants. Both are silent-failure modes.

**Proposal A8** — Importance: medium
Target: `.claude/skills/outreach-manager/SKILL.md` (Subagent 3, intermediary path)
Trace evidence: `2026-05-06-cadence-misread-7-per-day-not-additive.md`, `2026-05-05-intermediary-outreach-5-email-5-linkedin.md`
Problem: Two consecutive intermediary-cadence calibrations in two days plus a misread by COO Kay had to correct. Cadence number lives in memory files, not as canonical value with derivation. Memory churn signals "this should be a parameter, not prose." (Convergent with simplicity-advocate S3.)
Proposed change: In outreach-manager Subagent 3, add `<intermediary_daily_cap>` block with single canonical TOTAL value (currently 7), derivation comment ("50 emails ÷ 8 workdays remaining 5/6 → 5/15 = 6.25 → 7"), explicit "TOTAL across all channels, not additive" rule, and a note that any future bump request must restate the total. Per simplicity-advocate's S3, retire stale 5+5 memory files.
Risk if not done: Each cadence change repeats the misread pattern. Memory accretion compounds.

---

**Cross-cutting observation for coordinator:** Five of my eight proposals (A1, A2, A3, A4, A5) are the same shape — a trace produced a clear lesson + memory file but never landed in the relevant SKILL.md. **Recurring graduation gap.** Recommend the coordinator surface to Kay as a meta-finding: decision-traces and memory writes are not enough; SKILL.md edits are the integration point and they're being skipped. Worth a follow-up that audits the last 90 days of feedback_*.md against SKILL.md grep results to find more orphans.

**SOP-update flags:** A2 (conference-engagement adds Step-0 classification, changes T-7 deliverable) and A5 (investor-update auto-fire schedule changes the cadence calendar) require SOP updates per the calibration SOP rule. A1, A3, A4, A6, A7, A8 are skill-internal or CLAUDE.md-only; no SOP touch.

### architecture-strategist — READY
8 proposals filed below.
-> READY

### pattern-recognizer — 2026-05-08 analysis filed

**Method:** Read all 35 trace bodies (Decision/Reasoning/Why/Key Insight sections). Cross-checked existing MEMORY.md feedback files + CLAUDE.md Pre-Flight Checklists + hook handlers in `.claude/hooks/router/handlers/`. Looked for ≥2-datapoint cross-trace patterns; deferred 1-of patterns to architecture-strategist. Read other agents' posts before filing — overlaps flagged inline.

**Six proposals: 3 critical, 2 high, 1 medium.** Differentiation note: my lane is multi-trace patterns. Where I overlap with other agents (P5/S3/A8 cadence, P2/S4 voice pre-flight) I add the cross-trace generalization or the missing memory file rather than the skill-code fix.

---

**Proposal P1** — Importance: **critical**
**Pattern:** Inherited-from-generic-playbook scaffolding gets pruned every time Kay's lens hits it. AI proposes a number/branch/cadence/template scenario from convention; Kay kills it because it doesn't fire in G&B's actual context.
**Trace evidence:**
- `2026-05-03-strategic-thresholds-need-grounding.md` ($1M EBITDA "opportunistic floor" — vibe, not constraint)
- `2026-05-04-broker-cadence-and-paths-pruned.md` (Day 12 broker template + Need-more-info CIM branch — both inherited, both killed)
- `2026-05-04-day-5-voice-no-soft-signal-stacking.md` (three soft-signals stacked from cold-email convention — killed)
- `2026-05-01-acg-conference-meeting-strategy-pivot.md` (25 outreach drafts from "max-coverage" convention — killed in favor of 6 in-person 1:1s)
**Frequency:** 4 times in 4 days. Existing memory `feedback_strategic_thresholds_need_grounding` covers the NUMBER case but not the BRANCH/SCAFFOLDING case.
**Proposed action:** **New Pre-Flight Checklist block in CLAUDE.md** + extend the existing memory file's scope.
**Concrete edit:**
- CLAUDE.md, after the "Before research / network discovery" block, add:
  ```
  ### Before adding any new template, cadence step, decision branch, or threshold
  - Cite the G&B-specific firing case ("this fires when ___ happens in our actual pipeline") OR admit it's inherited convention and ask Kay before adding.
  - Inherited-from-playbook scaffolding (3-touch cadences, "need more info" branches, "max-coverage" outreach, soft-signal stacks) gets pruned by Kay every time. Pre-empt by NOT proposing it. (Source: P1 cluster — `2026-05-03-strategic-thresholds-need-grounding`, `2026-05-04-broker-cadence-and-paths-pruned`, `2026-05-04-day-5-voice-no-soft-signal-stacking`, `2026-05-01-acg-conference-meeting-strategy-pivot`)
  ```
- Update MEMORY.md index entry for `feedback_strategic_thresholds_need_grounding.md` to: "Never propose a load-bearing number, branch, cadence, or template scenario without a G&B-specific firing case. Generic-playbook scaffolding gets pruned."

---

**Proposal P2** — Importance: **critical**
**Pattern:** Voice/copy doctrine fragmented across 8+ memory files; the day-5-voice trace explicitly notes the CLAUDE.md pre-flight gap ("does NOT yet have an explicit 'no soft-signal stacking' rule"). Future agents drafting copy have no consolidated voice gate.
**Trace evidence:**
- `2026-05-04-pe-vibe-comes-from-we-centric-copy.md` → `feedback_pe_vibe_from_we_centric_copy`
- `2026-05-04-strip-user-context-from-public-copy.md` → `feedback_strip_user_context_from_public_copy`
- `2026-05-04-day-5-voice-no-soft-signal-stacking.md` → **NO MEMORY FILE YET**
- `2026-05-04-intermediary-template-doctrine.md` → `feedback_no_intermediary_drafts_outside_template`
- Pre-existing in MEMORY.md index: `- [feedback_email_no_em_dashes.md] — No em dashes in email drafts`, `- [feedback_drafts_no_blockquote.md] — HARD RULE: ANY copy/paste text Kay might lift...is plain text`, `- [feedback_day_aware_signoffs.md] — Drafts include day-of-week close...matching SEND day`, `- [feedback_email_niceties.md] — Always open emails with a warm nicety`
**Frequency:** 3 voice corrections this week + 5 pre-existing voice memories. Differentiation from S4: simplicity-advocate proposes COLLAPSING the pre-flight; I propose ADDING two missing rules + creating the missing memory file. Both can land — S4 collapses redundant bullets, P2 ensures the new rules from this week aren't lost in the collapse.
**Proposed action:** **New pre-flight checklist lines** (the missing rules) + **new memory file** for the day-5-voice doctrine that has none.
**Concrete edit:**
- Add to CLAUDE.md "Before writing any external message" after "No em dashes":
  ```
  - **No soft-signal stacking.** If body has an exit door ("if not a fit"), close MUST not also defer ("looking forward..."), and opener MUST not also apologize ("no pressure"). Pick one. (Source: `2026-05-04-day-5-voice-no-soft-signal-stacking`)
  - **No exit-door-only CTAs.** "Take you off my list" / "tell me to go away" generates no replies. Pair any exit option with a real ask. (Same source)
  - **For owner-facing or website copy: observations beat claims.** "Some businesses run on trust that takes decades to build" beats "we hold for the long run / we don't run auctions." We-centric claim patterns read PE regardless of warmth. (Source: `feedback_pe_vibe_from_we_centric_copy`)
  ```
- Create `feedback_no_soft_signal_stacking.md` (single-line index entry: "No soft-signal stacking + no exit-door-only CTAs in any external copy. Source: 2026-05-04 Day 5 voice trace.")

---

**Proposal P3** — Importance: **critical**
**Pattern:** Wrapper-hardening / POST_RUN_CHECK doctrine has been universalized by the 5/4 trace, but the MEMORY.md index line for `feedback_mutating_skill_hardening_pattern.md` still says "Read-only skills exempt" — directly contradicting Kay's broadened doctrine.
**Trace evidence:**
- `2026-05-03-silent-success-failure-mode-wrapper-validator.md` (deal-aggregator hardening — "read-only-ish" skill, hardened anyway)
- `2026-05-04-universal-post-run-check-doctrine.md` (Kay broadens: "any launchd skill should be on there")
- `2026-05-01-launchd-debugger-failure-trigger-architecture.md` (recursion guard + known-incident registry — also implies universal coverage)
**Frequency:** 3 same-week traces refining the same doctrine. Existing index line is stale and contradicts the newer `feedback_dashboard_green_can_lie` line.
**Proposed action:** **Refresh outdated rule.** MEMORY.md index line + memory file body.
**Concrete edit:**
- MEMORY.md, replace existing index line (currently): `- [feedback_mutating_skill_hardening_pattern.md] — Every scheduled mutating skill needs headless prompt + POST_RUN_CHECK validator + SKILL.md mandatory-validator section. Read-only skills exempt. Pattern from ai-ops-1.`
  with: `- [feedback_mutating_skill_hardening_pattern.md] — UNIVERSAL (broadened 2026-05-04): EVERY launchd skill needs POST_RUN_CHECK validator + headless prompt + SKILL.md mandatory-validator section. Read-only skills get artifact-landed checks (lighter), NOT exempt. Source: conference-discovery May 3 wipe + dashboard-green-lie incident.`
- Update memory body: delete "Read-only skills exempt" language; reference `feedback_dashboard_green_can_lie` + `2026-05-04-universal-post-run-check-doctrine`.

---

**Proposal P4** — Importance: **high**
**Pattern:** "Free deliverable from M&A advisor = sell-side prospecting" — fired twice in two weeks. The 5/1 trace explicitly anticipates a third instance and predicts graduation to skill default.
**Trace evidence:**
- `2026-05-01-sell-side-advisor-free-tool-pattern.md` ("Watch for third instance after Calder Capital 4/30 and Cetane 5/1 to graduate this from a trace into a feedback_*.md durable rule")
- Existing memory: `feedback_free_valuation_equals_sell_side` (created May 1) — exists, but skill-side enforcement isn't there
**Frequency:** 2 instances in 7 days. Trace explicitly flagged the graduation threshold. **Convergent with architecture-strategist A6** — A6 proposes the skill-code fix; my P4 confirms the pattern crossed the 2-instance threshold and graduation is now warranted (not premature).
**Proposed action:** **Update skill default** — adopt A6's proposal. Pattern recognition supports the graduation timing.
**Concrete edit:** Per A6 — `.claude/skills/email-intelligence/SKILL.md` adds classifier "Sell-side prospecting markers" with 5 trigger phrases ("free Value Range Analysis", "complimentary pre-sale audit", "what's your business worth", "sample valuation", "pre-listing review") + downgrade rule. Reference `feedback_free_valuation_equals_sell_side` and the two trace files.

---

**Proposal P5** — Importance: **high**
**Pattern:** Multi-channel cadence — AI proposes additive, Kay corrects to total. Same correction twice in 2 days. Trace explicitly flags generalization risk to JJ dials and DealsX volume.
**Trace evidence:**
- `2026-05-05-intermediary-outreach-5-email-5-linkedin.md` (5+5 split)
- `2026-05-06-cadence-misread-7-per-day-not-additive.md` (7-total, NOT 7+5; explicitly: "Same misread pattern could happen on JJ dial counts, DealsX volume, or any other multi-channel cadence")
- Existing memory: `feedback_intermediary_outreach_7_per_day` — current rule is intermediary-only
**Frequency:** 2 corrections in 2 days on same memory file. **Convergent with simplicity-advocate S3 + architecture-strategist A8.** My differentiation: I propose generalizing the rule across ALL multi-channel cadences (intermediary + JJ + DealsX + owner outreach), not just intermediary. S3 keeps it intermediary-scoped, A8 puts the canonical value in outreach-manager.
**Proposed action:** **Consolidate memory** — broaden the file to cross-channel cadence rule.
**Concrete edit:**
- Rename `feedback_intermediary_outreach_7_per_day.md` → `feedback_cadence_cap_is_total_not_additive.md`. Update body: "When recommending a cadence bump in any multi-channel context, state TOTAL touches/day explicitly. Default interpretation: cap = total across channels, not channel-isolated. Applies to intermediary outreach (currently 7/day total — see outreach-manager `<intermediary_daily_cap>`), JJ dials, DealsX volume, owner outreach, any future multi-channel cadence."
- Update MEMORY.md index entry. Coordinator: land P5+S3+A8 together — A8 puts the live number in skill, S3 retires stale memories, P5 generalizes the doctrine.

---

**Proposal P6** — Importance: **medium**
**Pattern:** Intermediary-vocabulary creep — 4+ memory files address "what label does G&B use / how do we classify the firm." Each fires a separate trace; agents synthesizing across them re-derive the same lookup table.
**Trace evidence:**
- `2026-05-04-ma-advisor-equals-broker.md` ("M&A Advisor" → Brokers, NOT IB)
- Existing memories per MEMORY.md index: `feedback_classify_intermediary_by_self_id`, `feedback_no_search_fund_language_intermediaries`, `feedback_kay_title_founder_ceo`, `feedback_marketplace_vs_broker_distinction`
**Frequency:** 4 vocabulary memories now active. **Differentiation from simplicity-advocate S5+S8:** S5 deletes `feedback_no_search_fund_language_intermediaries`; S8 collapses `feedback_classify_intermediary_by_self_id`. My P6 proposes ADDING a canonical lookup file as the agent's first read — source memories can stay or be deleted per S5/S8, but the lookup table becomes the single point of truth.
**Proposed action:** **New consolidation reference file.** Coordinator should sequence: P6 first (build the lookup), then S5/S8 (retire redundant feedbacks once lookup carries the load).
**Concrete edit:**
- New file `memory/reference_intermediary_vocabulary.md` with table: COLUMNS = Label / Used-For-G&B-Self-ID? / Counterparty-Classification / Source memory. Rows for: "M&A Advisor", "Investment Banker", "Business Broker", "Search Fund", "Search Vehicle", "Holding Company in Formation", "Founder & CEO", "Principal", "Marketplace", "Buy-side Advisor", "Sell-side Advisor".
- MEMORY.md index entry: `- [reference_intermediary_vocabulary.md] — Canonical lookup for what label G&B uses for itself + how to classify counterparty self-ID. First read for any intermediary-classification or external-copy work. Consolidates 4+ vocabulary memories.`

---

### pattern-recognizer — READY
6 proposals filed (P1–P6: 3 critical, 2 high, 1 medium). Convergence flagged: P4↔A6, P5↔S3↔A8, P6↔S5↔S8.
-> READY

### coordinator — 2026-05-08
All three analysis agents reported READY (architecture-strategist: 8 proposals, simplicity-advocate: 12, pattern-recognizer: 6). Synthesized by orchestrator (coordinator agent exited early without finishing). Closing chatroom.
-> CLOSE

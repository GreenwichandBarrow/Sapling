---
schema_version: 1.0.0
date: 2026-04-23
task: Calibration analysis of 35 unreviewed traces from 2026-04-10 through 2026-04-22
agents: [coordinator, architecture-strategist, simplicity-advocate, pattern-recognizer]
status: active
---

# Agent Chatroom: Calibration Analysis 2026-04-23

## Coordination Log

### architecture-strategist @ 2026-04-23 start
-> STARTING analysis

### simplicity-advocate @ 2026-04-24 03:26 UTC
-> STARTING analysis

### simplicity-advocate @ 2026-04-24 03:40 UTC
-> READY

Summary:
- 8 high-impact simplifications, most around memory bloat (261 feedback files) and retired/duplicate skills (meeting-brief-manager per CLAUDE.md line 281, still 587 lines alive). Biggest wins: consolidate outreach-voice cluster (6→1), drafts cluster (6→2 with clear branching), briefing/numbering cluster (4→1), delete superseded morning-briefing-categories, retire meeting-brief-manager skill directory.
- Structural pattern: Kay has been codifying within-session corrections as durable memories without litmus-testing them. 4/21 stress-test trace flagged this explicitly but the pattern hasn't propagated — goodnight workflow is writing memories faster than calibration consolidates them. Recommend a 90-day sunset on feedback_* files unless re-cited.
- Biggest YAGNI violation: the 4-bucket briefing codified across CLAUDE.md + 2 memories + pipeline-manager SKILL.md + goodmorning command + stop-hooks + decision-fatigue memory (6 enforcement points for one format). Pick one canonical source and have the others reference it.

Full findings posted inline below; coordinator can paste into main report.

---

## simplicity-advocate findings

### F1. Retire meeting-brief-manager skill directory
**Importance:** high
**Action:** DELETE
**Target:** `.claude/skills/meeting-brief-manager/` (587 lines)
**Evidence:** CLAUDE.md line 281 explicitly says "retired `meeting-brief-manager` nightly automation (Apr 12)." Morning-workflow Step 9's "brief-decisions pre-flight" replaces it. Yet the SKILL.md still exists and describes it as "Runs nightly via launchd."
**Proposal:** `rm -rf .claude/skills/meeting-brief-manager/`. Verify launchd plist is unloaded first. Keep `.claude/skills/meeting-brief/` (405 lines) as the sole brief-generating skill — it's what the 4/22 template-architecture trace now supports with typed templates.
**Risk:** If any other skill imports from meeting-brief-manager (e.g., pipeline-manager's calendar scan), reroute to meeting-brief first. Low risk — grep confirms it's standalone.

### F2. Consolidate outreach-voice memories (6 files → 1)
**Importance:** high
**Action:** CONSOLIDATE
**Target:** `feedback_never_say_fund.md`, `feedback_never_say_fund_or_lead.md`, `feedback_outreach_about_them.md`, `feedback_outreach_no_strategy_leaks.md`, `feedback_outreach_no_fake_lines.md`, `feedback_no_revenue_in_outreach.md`
**Evidence:** Read all six — each is 11-16 lines. `feedback_never_say_fund` and `feedback_never_say_fund_or_lead` are 90% overlapping (same "PE kills trust" reasoning, same "I'm with G&B" examples, written 6 days apart). The other four are all rules about what NOT to put in cold outreach. Together they cover ~85 lines for one coherent topic already captured in `user_outreach_voice.md` (indexed as user memory).
**Proposal:** Merge all six into `user_outreach_voice.md` as a "hard rules" subsection. Delete the six feedback files. Update MEMORY.md index to drop all six entries.
**Risk:** `user_outreach_voice.md` grows ~100 lines. Mitigation: that file is exactly where outreach voice rules belong; it's currently under-specified for hard rules.

### F3. Consolidate drafts memories (6 files → 2 branches)
**Importance:** high
**Action:** CONSOLIDATE
**Target:** `feedback_drafts_superhuman.md`, `feedback_drafts_in_superhuman_not_cursor.md`, `feedback_superhuman_drafts_only.md`, `feedback_email_drafts_no_blockquote.md`, `feedback_drafts_always_gb_account.md`, `feedback_no_drafting_without_explicit_approval.md`
**Evidence:** `feedback_drafts_in_superhuman_not_cursor` (27d old) says "never show drafts inline in conversation, always Superhuman." `feedback_email_drafts_no_blockquote` (6d old) describes HOW to paste drafts inline in conversation. These directly contradict. A future agent reading the latter correctly won't know the former superseded it. Memory files accrete without supersede-and-delete discipline.
**Proposal:** Single `feedback_draft_workflow.md` with two clear branches: (a) external cold outreach → Superhuman bash wrapper draft, no inline text; (b) reply/quick edit where Kay is iterating with Claude → inline plain text, no blockquote. Delete the other five.
**Risk:** Requires Kay to confirm which branch is current reality. Single best-ask clarification.

### F4. Consolidate briefing-format memories (4 files → 1, delete superseded)
**Importance:** high
**Action:** DELETE + CONSOLIDATE
**Target:** 
- DELETE: `feedback_morning_briefing_categories.md` (explicit 5-section format, superseded by 4-bucket on 4/19 per trace)
- DELETE: `feedback_morning_briefing_format.md` (general "every item needs ask")
- CONSOLIDATE: `feedback_ascending_numbering.md` + `feedback_additive_numbering.md` + `feedback_numbered_lists.md` into one `feedback_numbering.md`
- KEEP: `feedback_briefing_three_buckets.md` as canonical (plus `feedback_decision_fatigue_minimization.md` as doctrine)
**Evidence:** `feedback_morning_briefing_categories.md` (28d old) still prescribes "Pipeline shifts / Pipeline summary / Motion steps / Superhuman drafts / Other" — the exact format 4/19 trace said Kay tuned out and replaced. Leaving it live means next context-refresh a future agent reads both and has to reconcile.
**Proposal:** Delete the two superseded files. Merge the three numbering files (they all say "numbers go up, don't reset"). Net: 7 files → 3 files on briefing. MEMORY.md index drops 4 lines.
**Risk:** None. Superseded file deletion is a pure win.

### F5. The 4-bucket format is codified in 6 places — pick one source
**Importance:** medium
**Action:** SIMPLIFY
**Target:** CLAUDE.md (Step 9) + `feedback_briefing_three_buckets.md` + `feedback_decision_fatigue_minimization.md` + pipeline-manager SKILL.md "Briefing Format" section + pipeline-manager format-enforcement stop hooks + goodmorning command Step 7
**Evidence:** Per the 4/19 trace directly: "Codified as: feedback_briefing_three_buckets.md, feedback_decision_fatigue_minimization.md, CLAUDE.md morning-workflow Step 9, pipeline-manager SKILL.md 'Briefing Format' section + format-enforcement stop hooks, goodmorning command Step 7." Six enforcement surfaces for one output format = drift-magnet.
**Proposal:** Canonical spec lives in pipeline-manager SKILL.md (it owns the output). CLAUDE.md Step 9 becomes one line: "See pipeline-manager SKILL.md for bucket format." Memories become one-liners that cite the canonical spec. Stop hook references the canonical spec by path, not its own copy.
**Risk:** Breaks the "file-level independence" pattern but every drift-risk surface argues for single-source.

### F6. `target-discovery` vs `list-builder` overlap — merge boundary
**Importance:** medium
**Action:** QUESTION
**Target:** `.claude/skills/target-discovery/SKILL.md` (589 lines) + `.claude/skills/list-builder/SKILL.md` (415 lines)
**Evidence:** target-discovery is documented as orchestrator that "calls list-builder when a niche needs new targets." List-builder is pure Apollo. But target-discovery is 589 lines — more than list-builder. Most of target-discovery's logic is "run Apollo, enrich, write to sheet, auto-advance" — exactly list-builder's job plus sheet hygiene. The "orchestration" layer is thin.
**Proposal:** Either (a) collapse list-builder into target-discovery as a subagent and delete list-builder as a top-level skill, OR (b) slim target-discovery to <200 lines of pure routing logic and push all "find + enrich + write" into list-builder. Option (b) is cleaner. Kay never invokes list-builder directly per current CLAUDE.md — it's always called by target-discovery.
**Risk:** Refactor has blast radius into scheduled launchd jobs and niche-refill triggers. Stage behind a Friday dry-run per `feedback_friday_test_write_skills`.

### F7. Kay is still the drafts bottleneck — revisit the "drafts only, never send" rule
**Importance:** critical
**Action:** QUESTION
**Target:** `feedback_superhuman_drafts_only.md` + CLAUDE.md Superhuman section + review protocol memories
**Evidence:** CLAUDE.md: "CRITICAL: superhuman MCP is drafts only. Never send. Kay reviews and sends manually." 5 weeks of zero owner conversations per the brief. Kay reviews every cold-outreach draft, then clicks send manually. 4/15 kay-focus-off-list-scrubbing trace explicitly moved Kay OFF grunt work; draft-send-click is the same class of grunt work that never graduated. `feedback_remove_kay_from_loop` doctrine says skills graduate Active Review → Spot Check → Auto-Advance. Cold outreach drafts have never graduated past Active Review.
**Proposal:** Propose to Kay a staged send-automation for targets that clear three gates: (a) on approved target sheet, (b) Attio verified Person, (c) template is a Kay-approved golden per `feedback_golden_examples_stable_deliverables`. Spot-check sample (1 in 5 audited) rather than review-all. DO NOT implement unilaterally — this is a Decisions-bucket item for Kay. But flag it loud: the bottleneck has 5 weeks of accumulated evidence.
**Risk:** Bounced email damages sender domain (explicit memory: `feedback_no_unverified_metrics` + Apollo verification discipline). Gate (b) mitigates. Kay should decide the gate threshold.

### F8. Decision traces are being written too liberally — raise the litmus bar
**Importance:** medium
**Action:** SIMPLIFY
**Target:** decision-traces skill + goodnight workflow Step 3 enforcement
**Evidence:** 35 traces in 13 calendar days = 2.7 traces/workday. Several (e.g., 4/21-silent-focus-protocol, 4/21-stress-test-constraint-methodology) are legitimate judgment-call captures. Others (4/12-saas-filter-vs-scorecard, 4/19-commercial-laundry-reject, 4/19-path-a-services-primary) read more like session meeting-notes than "a future agent would do this differently" decisions. CLAUDE.md's own litmus — "only trace choices between alternatives that change future behavior with non-obvious reasoning" — is under-applied. The goodnight workflow's enforcement clause ("step 3 MUST produce a visible artifact") has bias toward writing, not toward litmus filtering.
**Proposal:** Rewrite goodnight Step 3 to front-load the litmus question: "For each APPROVE/REJECT, answer literally: Would a future agent make a different choice without knowing this? If no, SKIP and log 'N items below litmus.'" Target traces/workday down from 2.7 to ≤1. Calibration filter works on smaller, sharper set.
**Risk:** Losing borderline-useful context. Mitigation: Session-decisions file already captures the full decision log; traces are for the slice that changes agent behavior specifically.

### Meta-observation (flagged but not a recommendation)

The 4/21 stress-test trace explicitly warned: "hypothetical constraints are NOT durable project facts." Yet four other April traces codified within-session corrections as feedback memories (silent-focus, niche-ranking-methodology, stress-test itself, calibrate-before-writes). The pattern the trace warned about — over-codifying conversation-phase signals — is itself being repeated at the memory-writing layer. The fix isn't more memories; it's a 90-day auto-sunset on feedback_* files that aren't re-cited by any trace or skill in that window. Calibration-workflow could own this sweep.

-> END simplicity-advocate findings

---

### architecture-strategist @ 2026-04-24 04:05 UTC
-> READY

Top findings (full report below):
- **Niche-intelligence has not absorbed 5 thesis-level evaluation axes** codified in 11 April traces (AI-native vs AI-enhanced, physical-workflow split, Saltoun 3-condition software filter, services-primary Layer-2 filter, luxury-fit as multiplier-not-dimension, OEM-authorized-dealer moat, external-data-only under time pressure). Axes live as memories + traces only; the skill still scores the old way. Every new niche evaluated before calibration absorbs these will re-surface the same corrections.
- **Pipeline-manager is architecturally a polling synchronizer where event-driven triggers are needed.** Two critical CIM/outbound gaps in one week (MMPC 4/15, Project Restoration 4/17) share one root cause: skill spec describes aspirational trigger behavior with no enforcement contract between "event fires" and "downstream action executes." DealsX launches 5/6 with ~10x deal volume — this architecture does not scale.
- **5 weeks of zero owner conversations + zero NDAs is not being monitored as a system-level signal.** Health-monitor watches skill logs and Attio hygiene but not funnel throughput. The infrastructure is being built while the pipeline is empty. Missing: a throughput-watchdog skill or health-monitor sub-agent that fires an alarm when conversion milestones (conversations, NDAs, LOIs) go N weeks at zero.

---

## architecture-strategist findings

### A1. Niche-intelligence skill is running an obsolete evaluation model
**Importance:** critical
**Target:** `.claude/skills/niche-intelligence/SKILL.md` + `.claude/skills/niche-intelligence/references/sub-agents.md` + new `references/evaluation-axes.md`
**Evidence traces:** 2026-04-10-vertical-saas-thesis-conviction, 2026-04-12-adam-right-to-win-reframe, 2026-04-12-saas-filter-vs-scorecard, 2026-04-15-saas-revenue-band-revised, 2026-04-16-ai-native-vs-ai-enhanced-lens, 2026-04-18-saltoun-software-multiple-compression-signal, 2026-04-19-path-a-services-primary-saas-supporting, 2026-04-21-oem-authorized-dealer-thesis, 2026-04-21-niche-ranking-methodology-pivot, 2026-04-21-peer-group-hll-methodology, 2026-04-19-commercial-laundry-reject-strategic-consolidation
**Problem:** Eleven traces in 12 days refined how niches are evaluated. Grep of niche-intelligence/ returns zero matches for "AI-native," "physical-workflow," "services-primary," "Saltoun," and only two instancs of "right-to-win" in sub-agents.md (both cosmetic). The evaluation brain is in traces + memories; the execution skill is still scoring against the April-1 scorecard. Next Tuesday's run re-produces the same errors Kay corrected for three consecutive weeks.
**Proposed change:** Create `.claude/skills/niche-intelligence/references/evaluation-axes.md` as the single canonical file. Encode: (1) the two-layer filter (structural criteria + identity: services-primary, SaaS only as supporting capability); (2) physical-workflow vs documentation-workflow split for AI-native exposure; (3) three-condition software filter (Saltoun); (4) three forms of right-to-win (operator / adjacent-tech / investor-pattern-recognition); (5) OEM-authorized-dealer = positive signal; (6) luxury-fit as multiplier (0.9-1.2x), not primary scoring dimension; (7) external-data-only when ranking under time pressure. SKILL.md Step 4 (SCORE) reads evaluation-axes.md before scoring; Step 5b validation uses the same file. This collapses 11 traces + 6 feedback memories into one load-bearing reference the skill actually reads.
**Expected impact:** Niche-intelligence produces scorecards that match Kay's current thesis on first pass. Eliminates the "Claude scores well, Kay manually downgrades" loop that consumed 4+ sessions in April.

### A2. Pipeline-manager needs an event-contract layer, not more scan paths
**Importance:** critical
**Target:** `.claude/skills/pipeline-manager/SKILL.md` + new `references/event-contracts.md` + health-monitor cross-check
**Evidence traces:** 2026-04-15-pipeline-manager-outbound-scan-gap, 2026-04-17-pipeline-manager-cim-trigger-gap
**Problem:** Both April gaps have identical structure: (a) skill spec describes an auto-trigger, (b) the trigger is implemented as a polling scan during morning run, (c) either the scan window misses the event OR the downstream action is agent-driven and silently skipped, (d) no reconciliation check catches the drop. The 4/17 trace names this: "Skill specs are aspirational until proven running." DealsX launches in 13 days with ~10x deal volume. Adding more polling paths (the current Band-Aid pattern) multiplies drift surface.
**Proposed change:** Introduce an event-contract model: for each named event (outbound email sent, CIM arrived, NDA signed, stage change), define: (a) detection source (which scan finds it), (b) required downstream actions (numbered list), (c) per-action verification probe (read-back or artifact check), (d) failure escalation (Slack alert + morning-briefing red flag). Encode as `pipeline-manager/references/event-contracts.md` with one entry per event. Add a nightly reconciliation subagent that walks Attio Active Deals against Gmail+Drive reality and flags any entry where the event contract has been violated (stage skipped, folder missing, deal-evaluation never invoked). Health-monitor already has the skeleton for cross-reference scans — extend its `pipeline-hygiene` sub-agent to run the reconciliation rather than duplicating it inside pipeline-manager.
**Expected impact:** Silent failures become loud failures before DealsX launch. Every "trigger fired" claim has a verification probe. This is the fix Kay's 4/17 trace explicitly demanded ("Fix the skill hardening BEFORE launch, not after").

### A3. Throughput-drought watchdog is missing entirely
**Importance:** critical
**Target:** `.claude/skills/health-monitor/SKILL.md` — new sub-agent `throughput-watchdog`
**Evidence traces:** weekly-tracker 2026-04-17 (0/5 weeks), weekly-tracker 2026-04-10, 2026-04-19-reality-check-aggressive-timelines
**Problem:** Weekly-tracker surfaces "0 conversations for 5 weeks" in the weekly Friday artifact. Nothing monitors this signal mid-week. Nothing alarms. Morning briefing (action-keyed buckets) surfaces only today's items — an accumulating drought is invisible. Kay is building C-suite agents, brief architecture, tracker methodology at exactly the moment throughput = zero. Per the 4/19 reality-check trace, the structural math for cold-target-to-LOI is 3-6 months; every additional week at zero pushes the first close further out.
**Proposed change:** Add `throughput-watchdog` sub-agent to health-monitor with thresholds: (a) YELLOW if zero meaningful owner conversations 2 consecutive weeks; (b) RED if zero 3+ weeks OR zero NDAs 4+ weeks; (c) ALARM (main-briefing top item, not System Status tail) if zero at the RED threshold. Fires daily, reads from weekly-tracker artifacts + Attio Active Deals recent stage-changes + Gmail inbound deal signals. When RED, briefing inserts a forcing-function Decision: "RECOMMEND: pause build, double outreach — YES / NO / DISCUSS." The watchdog exists specifically to counteract the "build mode feels like progress" failure mode Kay has been in for 5 weeks.
**Expected impact:** Drought becomes an addressable signal, not a retrospective Friday observation. Forces the build-vs-throughput trade-off to surface as a Decision before week 6.

### A4. Conference-discovery + river-guide-builder should merge — 4/15 trace explicitly said so and it didn't land
**Importance:** high
**Target:** merge `.claude/skills/conference-discovery/` + `.claude/skills/river-guide-builder/` into `.claude/skills/networking-pipeline/`
**Evidence traces:** 2026-04-15-conference-unlock-broker-breakfasts, 2026-04-20-calibrate-before-writes, 2026-04-20-network-yield-vs-lived-knowledge
**Problem:** The 4/15 trace has an explicit "skill merge observation" — same data source (event attendee lists), same downstream (vault entity + Attio Person + nurture_cadence + next_action). The 4/20 Phase-3 calibration traces show river-guide-builder's network-scan is thin yield because it only scans Attio employment_history, ignoring the other three data sources in spec. Conference-discovery already encodes the broker-breakfast pivot. Running them separately means duplicate entity creation, duplicate nurture tagging, and the Phase-3 instrument bugs (too-strict H criterion, tokenization collisions) stay siloed in river-guide-builder where they don't benefit from conference-discovery's attendee-pipeline maturity.
**Proposed change:** Merge into `networking-pipeline` skill with three phases: (1) Event Discovery (ex conference-discovery); (2) Network Scan (ex river-guide-builder Phase 3); (3) Post-Event Entity Hydration (shared). Shared data source: event attendee lists + Attio Network + LinkedIn CSV + vault + Gmail. Kay's 4/20 cap-check pattern ("calibrate before writes") becomes a standard phase gate for both. The Phase 3 instrument bugs get fixed once for both paths.
**Expected impact:** Eliminates duplicate entity-creation pathways. Fixes Phase 3 instrument via conference-discovery's more mature entity-hydration logic. One less skill to maintain.

### A5. Brief-skill template architecture (4/22 decision) has not generalized — outreach-manager and niche-intelligence need the same treatment
**Importance:** high
**Target:** `.claude/skills/outreach-manager/templates/` (new) + `.claude/skills/niche-intelligence/templates/` + `.claude/skills/niche-intelligence/examples/` (new)
**Evidence traces:** 2026-04-22-brief-skill-template-architecture, 2026-04-19-onepager-guardrail-tool-level-not-memory, 2026-04-15-channel-mix-by-route, 2026-04-21-peer-group-hll-methodology
**Problem:** 4/22 codified "one parent skill per family, typed templates + examples folder" for investor-update and meeting-brief. Grep confirms outreach-manager has zero template or example folders despite having three routing modes (Kay Email / DealsX / JJ-Call-Only) with explicitly different channel mixes per 4/15 trace. Niche-intelligence has no templates/ or examples/ despite one-pager output failing repeatedly on the same Kay/team-centric insertions (4/19 hook trace was the 3rd+ correction). The 4/22 insight — "skill boundaries track shared hygiene, not shared output format" — applies to both.
**Proposed change:** (a) outreach-manager: create `templates/{kay-email,dealsx-email,jj-call-only,intermediary,conference}.md` + `examples/{same}/*.md`; skill errors if `{mode}` unspecified. (b) niche-intelligence: create `templates/one-pager.pptx` (already has hook guardrail — make the template the canonical structure) + `examples/one-pager/` with Kay-approved goldens for Specialty Insurance, Premium Pest, Commercial Cleaning. Cite `feedback_golden_examples_stable_deliverables` as the governance doctrine. Apply same "no silent fallback" rule.
**Expected impact:** Mode-specific wrong-tone failures (which produced hook-level enforcement in one-pager's case) stop recurring. New modes are additive template files, not skill refactors.

### A6. C-suite labeling has no structural enforcement — it's a memory rule
**Importance:** medium
**Target:** new `.claude/hooks/router/handlers/c_suite_labeling.py` + pipeline-manager briefing contract + CLAUDE.md morning-workflow Step 9
**Evidence traces:** 2026-04-15-channel-mix-by-route (tags `role/cmo`, `role/cpo`), 2026-04-15-conference-unlock-broker-breakfasts (tags `role/cmo`, `role/cpo`), 2026-04-17-pipeline-manager-cim-trigger-gap (GC primary, CPO secondary), 2026-04-19-briefing-architecture-shift-to-action-keyed-buckets
**Problem:** `feedback_c_suite_naming` says every briefing item gets a CFO/CIO/CMO/CPO/GC tag. Grep across all 39 skills finds C-suite references in only 9 SKILL.md files, most passing mentions. The 4/19 briefing-architecture trace mandated labeling; there's no enforcement on the output. Same 3x-correction pattern that graduated onepager-guardrail to tool-level enforcement (4/19 trace: "When a correction has been given 3+ times on the same pattern, graduate from memory to tool-level").
**Proposed change:** Same pattern as onepager-guardrail: a PreToolUse hook on Write/Edit to `brain/outputs/*briefing*.md` and morning-briefing content that blocks the write if ≥1 Decisions-bucket item lacks a C-suite label. Narrow scope: briefing files only, not general drafts. Alternatively, encode as pipeline-manager stop hook inside its format-enforcement logic (pipeline-manager already has format hooks per F5 in simplicity-advocate). Hook-level is more robust since pipeline-manager is not the only briefing source (adhoc assembly is allowed per CLAUDE.md).
**Expected impact:** Kay's mental model of C-suite workload distribution (the whole point per 4/19 trace) actually builds. Removes a repeating manual correction.

### A7. Memory-vs-hook graduation criterion should become a standing discipline, not a one-off
**Importance:** high
**Target:** CLAUDE.md new section "Enforcement Escalation" + calibration-workflow
**Evidence traces:** 2026-04-19-onepager-guardrail-tool-level-not-memory (the graduation), 2026-04-21-silent-focus-protocol, 2026-04-21-stress-test-constraint-methodology, 2026-04-20-calibrate-before-writes, 2026-04-21-traditional-search-peer-disclosure
**Problem:** The 4/19 one-pager hook is the only structural enforcement that has graduated. Kay keeps articulating meta-rules (silent-focus, stress-test-vs-durable-fact, calibrate-before-writes, continuation-vehicle-disclosure) that could each hit the same 3x-correction threshold. Currently the only path is Kay explicitly saying "this is not the first time" — agent-initiated escalation is not a standing discipline.
**Proposed change:** Add to CLAUDE.md a "Enforcement Escalation" section: "A memory rule graduates to tool-level hook when (a) the same correction has been given 3+ times across sessions AND (b) memory alone is insufficient to prevent recurrence. Calibration-workflow tracks correction frequency by memory file and flags candidates for graduation on Friday reviews. Agents observing a 3rd repeat correction should proactively propose graduation in the session." Calibration-workflow extends: grep traces for "not the first time" / "called that out" / "I've told you" language; count distinct feedback_* memory files cited across ≥3 traces in rolling 30 days; output candidates list.
**Expected impact:** The one-pager precedent becomes the template. Repeated corrections have a clear path from "frustration" to "fixed." Agent-initiated escalation reduces Kay's burden of noticing patterns.

### A8. Channel-mix-by-route is partially encoded but jj-operations phone-gating contract is implicit
**Importance:** medium
**Target:** `.claude/skills/jj-operations/SKILL.md` + `.claude/skills/outreach-manager/SKILL.md` cross-reference
**Evidence traces:** 2026-04-15-channel-mix-by-route
**Problem:** Outreach-manager correctly encodes the three routes (Kay Email / DealsX Email / JJ-Call-Only). 4/15 trace says the JJ-Call-Only cadence has an explicit phone-acknowledgement gate: email only fires after JJ logs "Connected + Interested" or "Connected + Curious", never after voicemail / no-answer / wrong-number. Grep of jj-operations SKILL.md finds no match for "gate," "acknowledge," or "Connected + Interested" — the load-bearing contract the trace explicitly flagged ("JJ's call log schema is load-bearing for this entire gating logic") is not spec'd in the skill that owns the schema.
**Proposed change:** jj-operations SKILL.md gets an "Email-Trigger Gating" section: enumerate call-outcome statuses, which trigger post-call email (Connected + Interested / Connected + Curious), which never do (Voicemail / No Answer / Wrong Number / Not Interested). Cross-reference to outreach-manager Subagent 1 for the actual draft. Pipeline-manager's outbound scan consumes the ack status from JJ's call log as a stage-change signal rather than treating all JJ-route email as standalone.
**Expected impact:** JJ-Call-Only route's brand-preserving "no email after voicemail" invariant is spec'd where it can be enforced, not buried in a trace.

-> END architecture-strategist findings


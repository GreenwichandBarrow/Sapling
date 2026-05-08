---
schema_version: 1.0.0
date: 2026-05-08
type: output
output_type: calibration
status: draft
title: "Calibration — 2026-05-08 (35 traces, 2026-05-01 → 2026-05-07)"
tags: ["date/2026-05-08", "output", "output/calibration", "status/draft", "topic/calibration"]
---

# Calibration Report — 2026-05-08

**Traces analyzed:** 35 (May 1–7)
**Raw proposals:** 26 (architecture-strategist 8 · simplicity-advocate 12 · pattern-recognizer 6)
**After dedupe/merge:** 22 — 5 critical, 10 high, 6 medium, 1 low
**Agents:** architecture-strategist (A), simplicity-advocate (S), pattern-recognizer (P)
**Coordinator:** Exited early without synthesis; orchestrator synthesized inline after analyst agents posted findings.

## Cross-cutting observations

1. **Graduation gap.** 5 of 8 architecture proposals share the same root cause: a trace produced a clear lesson, a memory file was written, but the relevant SKILL.md never absorbed it. Memory is recall-dependent; SKILL.md is mandatory-load. Worth surfacing as its own meta-decision.
2. **Trace pollution from auto-emit.** 6 of 35 traces (17%) were task-tracker `append`-verb backup receipts. They have no decision content, just rollback metadata. Single biggest complexity-noise vector this batch.
3. **Memory bloat is real.** MEMORY.md is at 490 lines / 85.6KB and self-warned bloated. Confirmed ≥4 duplicate or superseded entries this week alone. Doctrine is being re-encoded in multiple files instead of consolidated.
4. **Numbers don't belong in memory doctrine.** The intermediary cadence (5+5 → 7-total) churned the same memory file twice in 48h. Same risk on JJ dial caps, DealsX volume, any campaign-state value.
5. **SOP touches required:** Proposal #6 (conference classification) and #9 (investor-update auto-fire) change deliverables/cadences in the G&B Weekly Operating Schedule.

## Proposals

### Critical (5)

#### 1. Pipeline-manager preflight covers D+0 + D+1 — `.claude/skills/pipeline-manager/SKILL.md`
**Importance:** critical
**Trace evidence:** 2026-05-06-same-day-externals-preflight-gap.md
**Source agent(s):** A
**Problem:** Brief-preflight enumerates "tomorrow's external meetings" only. Same-day externals fall through (Guillermo 4/21 + 5/6 = second instance in 3 weeks).
**Proposed change:** Edit pipeline-manager SKILL.md preflight section to enumerate D+0 AND D+1 external meetings, mirroring the CLAUDE.md invariant added 5/6 (`feedback_preflight_covers_today_and_tomorrow.md`). Cite memory file in the rule.

#### 2. Strip trace emission from task-tracker `append` verb — `.claude/skills/task-tracker-manager/SKILL.md`
**Importance:** critical
**Trace evidence:** 6 traces dated 2026-05-02 (`task-tracker-append-call-gusto-…`, `-ny-models`, `-state-models`, `-stellar`, `-teri-b`, `-zuri-model-and-talent`)
**Source agent(s):** S
**Problem:** task-tracker-manager emits a trace per `append` invocation. These are rollback receipts (task + row + .bak path), not decisions. They polluted 17% of this batch's input.
**Proposed change:** Strip trace emission from `append`. Keep traces for `archive` / `rollback` / `reformat` (those have decision content). Route append rollback line to `logs/scheduled/task-tracker-{date}.log`.

#### 3. New CLAUDE.md preflight — "Before adding any new template/cadence/branch/threshold"
**Importance:** critical
**Trace evidence:** 2026-05-03-strategic-thresholds-need-grounding.md, 2026-05-04-broker-cadence-and-paths-pruned.md, 2026-05-04-day-5-voice-no-soft-signal-stacking.md, 2026-05-01-acg-conference-meeting-strategy-pivot.md (4 instances in 4 days)
**Source agent(s):** P
**Problem:** Inherited-from-generic-playbook scaffolding gets pruned every time Kay's lens hits it. AI proposes a number/branch/cadence/template from convention; Kay kills it for not firing in G&B's actual context.
**Proposed change:** Add new preflight block to CLAUDE.md (after "Before research / network discovery"): `### Before adding any new template, cadence step, decision branch, or threshold` — with rule "Cite the G&B-specific firing case OR admit it's inherited convention and ask Kay before adding." Update existing `feedback_strategic_thresholds_need_grounding.md` index line to cover branches/cadences/templates beyond just numbers.

#### 4. Voice doctrine — close pre-flight gap from day-5 trace + new memory
**Importance:** critical
**Trace evidence:** 2026-05-04-day-5-voice-no-soft-signal-stacking.md (no memory yet), 2026-05-04-pe-vibe-comes-from-we-centric-copy.md, 2026-05-04-strip-user-context-from-public-copy.md
**Source agent(s):** P
**Problem:** 3 voice corrections this week, day-5-voice trace explicitly notes the CLAUDE.md gap, no memory file captures "no soft-signal stacking."
**Proposed change:** (a) Add 3 rules to CLAUDE.md "Before writing any external message" preflight: no soft-signal stacking; no exit-door-only CTAs; observations beat claims for owner/website copy. (b) Create `memory/feedback_no_soft_signal_stacking.md`. Land **with** Proposal #13 (S4 collapse) so new rules don't disappear in the cleanup.

#### 5. Refresh outdated POST_RUN_CHECK memory index line
**Importance:** critical
**Trace evidence:** 2026-05-03-silent-success-failure-mode-wrapper-validator.md, 2026-05-04-universal-post-run-check-doctrine.md, 2026-05-01-launchd-debugger-failure-trigger-architecture.md
**Source agent(s):** P
**Problem:** MEMORY.md still says "Read-only skills exempt" — directly contradicts Kay's 5/4 broadened doctrine and the dashboard-green-can-lie incident.
**Proposed change:** Replace the existing MEMORY.md index line for `feedback_mutating_skill_hardening_pattern.md` with: *"UNIVERSAL (broadened 2026-05-04): EVERY launchd skill needs POST_RUN_CHECK validator + headless prompt + SKILL.md mandatory-validator section. Read-only skills get artifact-landed checks (lighter), NOT exempt."* Update memory body to delete "Read-only skills exempt" language.

### High (10)

#### 6. Conference-engagement classification gate (MERGED A2 + S9) — `.claude/skills/conference-engagement/SKILL.md`
**Importance:** high · **SOP touch required**
**Trace evidence:** 2026-05-01-acg-conference-meeting-strategy-pivot.md
**Source agent(s):** A, S
**Problem:** Skill defaults to "max coverage of attendee list" regardless of conference type. ACG NY Women of Leadership triggered 25 drafts thrown out, pivoted to 6 IB-heavy 1:1s. ~5K tokens wasted.
**Proposed change:** Add `<conference_classification>` Step-0 gate BEFORE drafting. Trade show (1000+) → max-coverage. Curated summit (50–300, premium) → 6–10 pre-set in-person 1:1 requests, IB-filter first. Surface classification + plan to Kay before drafting body copy. Update G&B Weekly Operating Schedule T-7 deliverable definition.

#### 7. Post-call-analyzer call-type classification — `.claude/skills/post-call-analyzer/SKILL.md` + email-intelligence
**Importance:** high
**Trace evidence:** 2026-05-01-granola-summary-insufficient-for-coaching-calls.md
**Source agent(s):** A
**Problem:** Granola summary treated as authoritative. Harrison Wells 4/30 dropped 5 action items + 4 promised emails. Risk doubled now post-call-analyzer is real-time.
**Proposed change:** Add Call Type Classification step. Substantive (counterparty role contains coach/investor/deal/intermediary OR duration >30min OR vault entity tagged `relationship_type: coach|investor|advisor`) → full-transcript-read mode. Email-intelligence inherits the classification.

#### 8. Deal-evaluation 4-cluster pipeline hygiene audit — `.claude/skills/deal-evaluation/SKILL.md`
**Importance:** high
**Trace evidence:** 2026-05-01-active-deals-4-cluster-triage-framework.md
**Source agent(s):** A
**Problem:** 4-cluster triage (Dead / Cold-but-live / Process-broken / Genuinely-active) took Active Deals from 18 stale → 12 clean + 6 archived, but the framework lives only in the trace.
**Proposed change:** Add `<weekly_pipeline_hygiene_audit>` section codifying the 4-cluster rules. Stage-rollback as the Cold-but-live action is the structural innovation. Schedule weekly (Friday morning) OR document on-demand verb invocation.

#### 9. Investor-update auto-fire schedule + Pending Discussion Topics — `.claude/skills/investor-update/SKILL.md`
**Importance:** high · **SOP touch required**
**Trace evidence:** 2026-05-04-capacity-letter-via-meeting-brief-not-email.md, 2026-05-06-same-day-externals-preflight-gap.md
**Source agent(s):** A
**Problem:** (a) Capacity-letter routing created a `Pending Discussion Topics` entity-file pattern with no codified consumer. (b) Per `feedback_recurring_investor_briefs_owned_by_skill.md`, recurring briefs should auto-fire 24h ahead, but investor-update has no schedule and no claim of ownership. Guillermo 5/6 miss happened because nothing actually owned it.
**Proposed change:** Add `<auto_fire_schedule>` block (biweekly Guillermo, monthly Jeff Stevens, quarterly all-LP) with cron + 24h-ahead semantics. Add `<pending_discussion_topics_protocol>`. File a bead for the launchd timer wiring. Update SOP cadence calendar.

#### 10. Cadence cap doctrine — total, not additive (MERGED A8 + S3 + P5)
**Importance:** high
**Trace evidence:** 2026-05-05-intermediary-outreach-5-email-5-linkedin.md, 2026-05-06-cadence-misread-7-per-day-not-additive.md
**Source agent(s):** A, S, P
**Problem:** Two consecutive cadence calibrations in 2 days + COO misread the bump direction. Numbers churn with campaigns; the durable rule (cap = total, not additive) lived nowhere clean.
**Proposed change:** (a) Rename `feedback_intermediary_outreach_7_per_day.md` → `feedback_cadence_cap_is_total_not_additive.md`. (b) Generalize body to ALL multi-channel cadences (intermediary + JJ + DealsX + owner). (c) Add `<intermediary_daily_cap>` block to outreach-manager Subagent 3 with single canonical TOTAL value (currently 7), derivation comment, "TOTAL not additive" rule. (d) Move the operational number to session-decisions where churn is expected.

#### 11. Sell-side advisor classifier (MERGED A6 + P4) — `.claude/skills/email-intelligence/SKILL.md`
**Importance:** high
**Trace evidence:** 2026-05-01-sell-side-advisor-free-tool-pattern.md (Cetane), prior `feedback_free_valuation_equals_sell_side` (Calder Capital 4/30)
**Source agent(s):** A, P
**Problem:** Free-deliverable inbound from M&A advisor = sell-side prospecting. Pattern hit 2x in 7 days; the trace explicitly anticipated graduation timing.
**Proposed change:** Add classifier section "Sell-side prospecting markers" with 5 trigger phrases (free Value Range Analysis, complimentary pre-sale audit, what's your business worth, sample valuation, pre-listing review). If sender role includes "M&A advisor" / "investment banker" AND body matches → tag `sell_side_prospect: true` and downgrade warmth-signal.

#### 12. Delete duplicate `feedback_dashboard_same_surface_nested.md` — MEMORY.md hygiene
**Importance:** high
**Trace evidence:** 2026-05-01-dashboard-nested-archive-not-sidebar.md
**Source agent(s):** S
**Problem:** Two memory files for the same rule. Both index entries say effectively the same thing.
**Proposed change:** Delete the dashboard-narrower file. Keep `feedback_same_surface_nested_view.md`. Remove the corresponding MEMORY.md index line.

#### 13. Collapse "Before writing any external message" preflight from 12+ to 5 — `CLAUDE.md`
**Importance:** high
**Trace evidence:** 5 traces dated 2026-05-04 (broker-cadence, day-5-voice, intermediary-template, strip-user-context, pe-vibe)
**Source agent(s):** S
**Problem:** Preflight bloated to 12+ bullets. Five 5/4 traces hit the same root cause: ad-hoc drafting outside canonical template. Once template-doctrine bullet is in, the older sub-rules are already enforced AT the template layer. Repeating them in CLAUDE.md is token tax on every system prompt.
**Proposed change:** Collapse to 5 bullets: (1) verify recipient address, (2) for intermediaries pull from canonical template (forbid ad-hoc), (3) lead with what THEY cared about + trigger language check, (4) plain text + no em dash + day-aware sign-off, (5) no Sunday sends + no stranger outreach. **Land with Proposal #4** so new voice rules survive the collapse.

#### 14. Delete `feedback_no_search_fund_language_intermediaries.md` — covered by template doctrine
**Importance:** high
**Trace evidence:** 2026-05-04-intermediary-template-doctrine.md
**Source agent(s):** S
**Problem:** Template-doctrine memory enforces voice at the template layer. A separate "don't say search fund" memory is defensive code.
**Proposed change:** Delete the file. Remove MEMORY.md line. Update template-doctrine memory body to mention "voice rules live in canonical templates — don't re-encode as separate memories."

#### 15. Remove pipeline-manager log-size hung-job detection — `.claude/skills/pipeline-manager/SKILL.md`
**Importance:** high
**Trace evidence:** 2026-05-06-hung-jobs-false-alarm-stale-snapshot.md
**Source agent(s):** S (supersedes hung-job piece of A1)
**Problem:** Pipeline-manager generated 2 🔴 false-alarm Decisions on 5/6 morning. launchd-debugger already owns hung-job detection via exit-code + POST_RUN_CHECK. Two systems, one is wrong.
**Proposed change:** Remove orphan-PID / log-size detection from pipeline-manager. Single source of truth = launchd-debugger + POST_RUN_CHECK.

### Medium (6)

#### 16. CLAUDE.md `## Runtime Architecture` section — server + Granola sidecar invariants
**Importance:** medium
**Trace evidence:** 2026-05-07-scheduler-adapter-synthesizes-plist-shape.md, 2026-05-07-server-replaces-mac-runtime.md
**Source agent(s):** A
**Problem:** Server migration introduces invariants not yet documented. Future agent doing "general cleanup" risks breaking either silently.
**Proposed change:** Add `## Runtime Architecture` section to CLAUDE.md: (a) server-as-default + Granola sidecar exception, (b) scheduler-adapter as intentional shape-match abstraction (do not refactor without separate scope), (c) Phase 4 Granola output sync follow-up.

#### 17. New `memory/reference_intermediary_vocabulary.md` lookup table
**Importance:** medium
**Trace evidence:** 2026-05-04-ma-advisor-equals-broker.md + 4 existing memories
**Source agent(s):** P
**Problem:** 4+ memories address "what label does G&B use / how do we classify the firm." Each fires a separate trace; agents re-derive the same lookup table.
**Proposed change:** New `memory/reference_intermediary_vocabulary.md` with Label / Used-For-G&B-Self-ID? / Counterparty-Classification / Source memory. Rows for: M&A Advisor, Investment Banker, Business Broker, Search Fund, Search Vehicle, Holding Company in Formation, Founder & CEO, Principal, Marketplace, Buy-side Advisor, Sell-side Advisor. **Sequence:** land #17 first; then #18 + #14 (which retire memories the lookup subsumes).

#### 18. Rewrite `feedback_classify_intermediary_by_self_id.md` to "IB-only-if-explicit" 3-line rule
**Importance:** medium
**Trace evidence:** 2026-05-04-ma-advisor-equals-broker.md
**Source agent(s):** S
**Problem:** Original heuristic produced 7+ wrong moves Kay had to override.
**Proposed change:** 3 lines: (1) M&A advisor = broker by default. (2) Investment banker only if firm self-IDs as IB on homepage hero. (3) When in doubt, broker.

#### 19. Delete `feedback_lauren_della_monica_dead_end.md` — wrong layer
**Importance:** medium
**Source agent(s):** S
**Problem:** Person-status data belongs in Attio + entity files, not MEMORY.md. Memory is for transferable doctrine, not contact statuses.
**Proposed change:** Delete the file. Remove MEMORY.md line. Copy the dormancy data to the Lauren entity file if not already there.

#### 20. Consolidate two "don't trust the surface, check the source" rules
**Importance:** medium
**Trace evidence:** 2026-05-07 server traces (Kay-outbound check), 2026-05-01-granola-summary-insufficient-for-coaching-calls.md
**Source agent(s):** S
**Problem:** Two separate memories carry the same epistemic principle.
**Proposed change:** Consolidate into one memory `feedback_check_the_source_not_the_summary.md` with both subcases (email thread + Granola transcript) as concrete instances. Delete the two narrower entries.

#### 21. Delete `feedback_no_clear_rewrite_populated_sheets.md` — covered 3x already
**Importance:** medium
**Source agent(s):** S
**Problem:** Three layers of memory cover the same ground (deny-list + POST_RUN_CHECK validator + dashboard-green-can-lie). The clear-rewrite memory is the redundant fourth.
**Proposed change:** Delete the file + MEMORY.md line.

### Low (1)

#### 22. Strip per-row hardening provenance from CLAUDE.md scheduled-skills table
**Importance:** low
**Trace evidence:** 2026-05-04-universal-post-run-check-doctrine.md
**Source agent(s):** S
**Problem:** With universal POST_RUN_CHECK doctrine, the per-row "Hardened 2026-04-25 / Hardened 2026-04-29" history reads as redundant token tax in every system prompt.
**Proposed change:** Compress the table — keep skill name + schedule + 1-line purpose. Move hardening history to `docs/hardening-changelog.md` or rely on git log.

## Conflicts requiring Kay's call

None unresolved. The agents converged on every overlap (cadence, conference, sell-side, hung-jobs).

## Result

_Filled in after Kay approves changes._

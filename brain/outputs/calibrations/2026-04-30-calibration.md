---
schema_version: 1.0.0
date: 2026-04-30
type: output
output_type: calibration
status: draft
title: "Calibration — 2026-04-30 (69 traces, 2026-04-10 → 2026-04-29)"
tags: ["date/2026-04-30", "output", "output/calibration", "status/draft", "topic/calibration"]
---

# Calibration Report — 2026-04-30

**Traces analyzed:** 69 (decisions: 69, learnings: 33)
**Trace range:** 2026-04-10 → 2026-04-29 (covers 2 weeks since prior calibration on 4/16)
**Agents:** architecture-strategist, simplicity-advocate, pattern-recognizer
**Coordinator:** Timed out at 8min; orchestrator synthesized inline after analyst agents posted findings

## Executive Summary

23 proposals across 3 lenses, deduplicated. Three themes dominate:

1. **Rule-decay graduating to hooks/skill-files.** Memory-only rules with documented violation counts ≥3 (search-fund language for intermediaries, Friday-only relationship surfacing, HOLD-prefix gate) need belt-and-suspenders enforcement at the tool layer. The `onepager_guardrail.py` precedent works; pattern-recognizer counted 4 violations of the Friday-only rule in 9 days before durable codification.

2. **Source-of-truth-per-question, not per-system.** 6 traces in 6 weeks document the same class of bug — a system-level "always read X" rule misroutes when the operational question shifts (DealsX sprint, JJ pace, Lauren cadence, NDA-engagement, HOLD calendar, partner-state). CLAUDE.md needs a per-question lookup table.

3. **MEMORY.md is overflowing.** Index is 461 lines / 76.3KB and the loader explicitly warns "only part of it was loaded." Silent rule decay is happening NOW. 5 memory groups consolidate cleanly without semantic loss. Plus 3 deprecated Superhuman entries to delete outright.

One critical mutating-skill hardening still open: **niche-intelligence Tuesday fire** (bead `ai-ops-5wx`). Fails silently every Tuesday until shipped. Last mutating skill not yet on the hardening pattern.

## Proposals (23 — sorted critical → high → medium → low)

### CRITICAL (2)

**1. Harden niche-intelligence scheduled fire** [architecture]
- Target: `.claude/skills/niche-intelligence/headless-tuesday-prompt.md` (new), `scripts/validate_niche_intelligence_integrity.py` (new), `scripts/run-skill.sh` wrapper case, plist `POST_RUN_CHECK` env var
- Current: Last mutating scheduled skill not on the hardening pattern. Currently routes `claude -p` with bare `/niche-intelligence`. CLAUDE.md scheduled-skills row marks it "expected to fail next Tuesday too" until bead `ai-ops-5wx` ships.
- Why: Highest-blast-radius open hole. Silent failures every Tuesday at 22:30 ET. Doctrine exists, work is identified.
- Source: 2026-04-29-stagger-launchd-plists-collision, 2026-04-25-headless-prompt-as-wrapper-swap, CLAUDE.md scheduled-skills row.

**2. Graduate `no_search_fund_language` to a PreToolUse hook** [architecture]
- Target: `.claude/hooks/router/handlers/no_search_fund_language.py` (new)
- Current: Memory-only (`feedback_no_search_fund_language_intermediaries.md`). Brand-floor rule per `feedback_brand_floor_vs_voice_preference`.
- Change: Block Write/Edit on intermediary outreach drafts containing `search\s+fund`, `search\s+vehicle`, `committed\s+equity`, `\bETA\b`, `24-month\s+(acquisition\s+)?window`. Mirror `onepager_guardrail.py` shape.
- Why: Per `2026-04-19-onepager-guardrail-tool-level-not-memory` graduation rule. Asymmetric stigma documented; recipient class bounded; pattern mechanically detectable.
- Source: 2026-04-29-no-search-fund-language-intermediaries.

### HIGH (8)

**3. Add per-question source-of-truth lookup to CLAUDE.md** [architecture]
- Target: `CLAUDE.md` § Querying — Source of Truth bullets
- Change: Append per-question table (DealsX sprint → Drive Verticals; JJ dials → enumerate all Call Log tabs; cadence → Attio nurture_cadence field; NDA reach → meaningful_conversation checkbox; HOLD detection; partner state → partner artifact).
- Why: 6 traces in 6 weeks on Pattern B failure. CLAUDE.md loads in system prompt; lookup table reaches before per-skill reminders.
- Source: 2026-04-18-dealsx-sprint-source-of-truth, 2026-04-23-cadence-field-sole-source-of-truth, 2026-04-23-jj-col-u-overwrite, 2026-04-25-jj-call-log-tabs-via-sheets-api, 2026-04-25-attio-engagement-signal-for-post-nda-split, 2026-04-23-hold-calendar-prefix-no-brief.

**4. HOLD-prefix gate in pipeline-manager + meeting-brief-manager SKILL.md** [architecture]
- Target: Both skill files
- Current: Rule lives only in CLAUDE.md morning-workflow pre-flight. `grep HOLD` returns zero hits in either skill.
- Change: Add HOLD-skip clause to calendar-scan section of both skills.
- Why: CLAUDE.md gets compacted under context pressure; skill files reload on invocation. Belt-and-suspenders.
- Source: 2026-04-23-hold-calendar-prefix-no-brief.

**5. Friday-only relationship-cadence surface filter (skill rule + stop hook)** [architecture + pattern, MERGED]
- Target: `.claude/skills/pipeline-manager/SKILL.md` "Briefing Surface Filters" section + new `.claude/hooks/router/handlers/relationship_cadence_friday_only.py`
- Current: Memory-only enforcement. Documented 4 violations across 4/17, 4/21, 4/24, 4/26.
- Change: Skill section: "Mon-Thu omit relationship-cadence/nurture/dropped-balls items entirely. Active-deal cadence (NDA awaiting reply, financials chase, post-LOI) stays daily. Friday full surfacing." Plus stop hook that scans pipeline-manager output: if date is Mon-Thu AND output contains nurture/cadence patterns → block.
- Why: 4 violations in 9 days. Past 3x graduation threshold. Memory alone hasn't held.
- Source: 2026-04-26-relationship-cadence-friday-only.

**6. Split conference-engagement templates by audience** [architecture]
- Target: `.claude/skills/conference-engagement/templates/`
- Current: One combined `email-templates.md`. SKILL.md describes 3-bucket taxonomy.
- Change: Split into `templates/intermediary.md`, `templates/owner.md`, `templates/peer.md`. Update SKILL.md to require `{audience}` arg. No silent fallback.
- Why: Mirrors meeting-brief-manager refactor. 3-bucket taxonomy settled. Combined templates create wrong-tone outputs.
- Source: 2026-04-22-brief-skill-template-architecture, 2026-04-23-advisor-collapses-into-intermediary.

**7. Consolidate MEMORY.md from 110+ entries into doctrine files** [simplicity]
- Target: `memory/MEMORY.md` (and 5 new doctrine files)
- Current: 461 lines / 76.3KB. Loader truncation warning active. Rules at bottom may not load.
- Change: Merge 5 groups (briefing-format, outreach-voice, secret-handling, niche-evaluation, secrets) into doctrine files. Target index < 200 lines / < 30KB. Detailed list in agent chatroom output.
- Why: Silent rule-decay happening now. Consolidation reduces calibration noise.
- Source: 2026-04-19-briefing-architecture-shift, 2026-04-25-decisions-only-briefing, 2026-04-26-superhuman-hybrid-migration, 2026-04-29-no-search-fund-language-intermediaries, plus the file's own auto-warning.

**8. Delete deprecated Superhuman memories (3 files)** [simplicity]
- Target: `feedback_drafts_superhuman.md`, `feedback_superhuman_drafts_only.md`, update `feedback_draft_sharing_for_learning.md`
- Current: First explicitly DEPRECATED but still indexed. Second superseded by `feedback_gmail_only_no_superhuman.md`. Third references Superhuman.
- Change: Delete first two. Update third to remove Superhuman reference (calibration-signal logic still applies to Gmail drafts).
- Why: Stale memories actively mislead. "DEPRECATED" without removal defeats the purpose.
- Source: 2026-04-26-superhuman-hybrid-migration.

**9. New memory: `feedback_voice_lead_with_their_emphasis.md`** [pattern]
- Target: New file
- Current: 3 voice memories cover symptoms (about-them, no-strategy-leaks, continue-dont-reintroduce). None capture data-rich vs values-rich opener distinction.
- Change: Codify Hoffman litmus + Heritage-Holding voice-match + buy-box first-person rule. Cross-link from existing 3.
- Why: Same correction across 5 traces in 1 week.
- Source: 2026-04-29-lead-with-what-they-care-about, 2026-04-29-no-search-fund-language-intermediaries, 2026-04-23-buy-box-paragraph-kay-authored, 2026-04-23-seller-short-transition-matters, 2026-04-22-evening-event-override-will-cotton-studio.

**10. New memory: `feedback_check_schema_before_recommending.md`** [pattern]
- Target: New file
- Current: No memory captures the meta-rule. Domain-specific memories exist but principle not generalized.
- Change: Codify — before recommending behavioral intervention based on data pattern, verify the data model can represent the metric.
- Why: 4 traces show confident-wrong recommendations from data-model blind spots. JJ trace cost 3 wrong analyses before unlock.
- Source: 2026-04-23-jj-col-u-overwrite, 2026-04-23-cadence-field-sole-source-of-truth, 2026-04-29-stagger-launchd-plists-collision, 2026-04-19-onepager-guardrail-tool-level-not-memory.

### MEDIUM (7)

**11. New memory: `feedback_skill_creation_litmus.md`** [simplicity]
- Litmus: "Will Kay invoke this slash command >5x/year? If yes → skill. If no → memory + scripts." Reference personal-task-tracker precedent.
- Source: 2026-04-27-personal-tooling-not-skill.

**12. Rename `feedback_briefing_three_buckets.md` → `feedback_briefing_doctrine.md` + rewrite** [simplicity]
- Filename describes superseded structure. Rewrite to reflect Decisions-only state, or merge into `feedback_decision_fatigue_minimization.md`.
- Source: 2026-04-19-briefing-architecture-shift, 2026-04-25-decisions-only-briefing.

**13. New memory: `feedback_categorical_vs_behavioral_classification.md`** [simplicity]
- Codify: "Categorical rules → filters; behavioral importance → native ML. Don't propose hardcoded VIP filters."
- Source: 2026-04-26-vip-filters-replaced-by-native-learning.

**14. New memory: `feedback_offramp_at_smallest_commitment.md`** [pattern]
- Litmus: "Conditionals attach to smallest concrete ask in email — meeting/intro/follow-up — never to relationship overall." Pair with `pattern/disqualifier-skip-pitch` for banker/lender first-replies.
- Source: 2026-04-24-banker-first-reply-cut-buybox, 2026-04-24-offramp-attach-to-ask, 2026-04-23-buy-box-paragraph-kay-authored.

**15. EXPAND `feedback_stress_test_constraints_not_facts.md`** [pattern]
- Add subsections: (a) external-framework premise verification (Athena/Matchmaker), (b) audience-aware-disclosure check before applying philosophical reframes (WSN/Charter), (c) "fluff" tell — analyses on thin internal data must surface low confidence.
- Source: 2026-04-21-stress-test-constraint-methodology, 2026-04-22-kay-is-operator-not-absent-buyer, 2026-04-21-traditional-search-peer-disclosure, 2026-04-21-niche-ranking-methodology-pivot.

**16. New CLAUDE.md pre-flight: "Before bulk-destructive op"** [architecture]
- Target: `CLAUDE.md` § Pre-Flight Checklists
- Change: "Re-fetch live state immediately before any bulk-destructive op (Gmail filters, Attio batch, Sheet rows). Snapshot pre-write to `/tmp/{op}-snapshot.json` for rollback."
- Source: 2026-04-26-stale-snapshot-bulk-delete-bug, 2026-04-23-jj-col-u-overwrite.

**17. Author `scripts/audit_scheduled_skills.py` + fold into health-monitor Friday fire** [architecture]
- Target: New script, health-monitor SKILL.md
- For each plist flagged as mutating, verify wrapper case + headless prompt + validator + POST_RUN_CHECK env var. Slack summary on Friday morning.
- Source: 2026-04-17-pipeline-manager-cim-trigger-gap, 2026-04-29-stagger-launchd-plists-collision, 2026-04-25-tech-debt-three-hour-scope-cut.

**18. Verify relationship-manager vault→attio engagement-note daily sync runs** [architecture]
- Target: `.claude/skills/relationship-manager/SKILL.md`
- Verify (or add) daily step: scan `brain/entities/` for entities created last 7 days with empty `attio_id`. If Person now exists in Attio, attach idempotent note + set source/cadence.
- Source: 2026-04-24-vault-attio-sync-option-b.

### LOW (5)

**19. Audit `/triage` duplicate registration + 30-day skill invocation review** [simplicity]
- `/triage` appears registered twice in skill-loader output. Inventory which skills haven't fired in 30 days.
- Source: skill-loader output, sampled traces.

**20. New memory: `feedback_skill_boundaries_track_hygiene.md`** [simplicity]
- Codify: "Skill boundaries should track shared hygiene, not shared output format. Same hygiene + different templates → one skill."
- Source: 2026-04-22-brief-skill-template-architecture.

**21. Expand `decision-traces` SKILL.md litmus** [pattern]
- Add second-pass scan for: (a) sessions with 3+ draft iterations on same artifact (voice-calibration trace candidate), (b) suppression decisions where agent decided NOT to surface something Kay had previously asked to suppress.
- Source: 2026-04-26-relationship-cadence-friday-only (gap caught after 3 weeks of silent violations).

**22. New `brain/traces/correction-counts/{pattern-slug}.md` ledger** [pattern]
- When a correction repeats, append to per-pattern ledger. Calibration-workflow scans weekly; ≥3 entries = graduate to hook. Makes 3x threshold observable.
- Source: meta-pattern across feedback_relationship_cadence_friday_only (4 before catch), feedback_artifacts_pure_industry_analysis (3 before hook), feedback_no_search_fund_language_intermediaries (caught at 1).

**23. Document Sheets-API tab enumeration in `jj-operations` SKILL.md** [architecture]
- Target: SKILL.md
- Add "Tab enumeration via Sheets API" subsection pointing to `scripts/refresh-jj-snapshot.sh` and tab regex `^Call Log\s+\d+[./]\d+[./]\d+$`.
- Why: Pattern reusable for any multi-tab Sheets data source.
- Source: 2026-04-25-jj-call-log-tabs-via-sheets-api.

## Skill Usage / Sunset Notes

Today is Thursday 2026-04-30, NOT first Friday of month. Skipping monthly sunset audit (next runs 2026-05-01 if Friday treated as first Friday, otherwise 2026-06-05).

Flagged for follow-up but not cut this run:
- `/triage` duplicate registration (proposal #19)
- `migration-workflow` skill vs `/migrate` slash command (possibly redundant)
- `generate-prd`, `generate-stories`, `generate-visuals`, `github`, `plan-refinery` (general dev tooling, no invocations in sampled traces)

## Voice Calibration Notes

No draft-vs-sent diffs available this run (pipeline-manager `draft_calibration` section not yet wired per the SKILL.md spec — separate work). Voice patterns surfaced via the trace corpus instead, captured in proposals #9, #14, #15.

## Agent-Kay Alignment

Skipped this run (would require >5 min reading 5 target list sheets and pattern-recognizer judged corpus patterns sufficient). Recommend running on next Friday's calibration when Kay has acted on more agent recommendations.

## Source Chatroom

`brain/traces/agents/2026-04-30-calibrate.md` — full agent findings preserved.

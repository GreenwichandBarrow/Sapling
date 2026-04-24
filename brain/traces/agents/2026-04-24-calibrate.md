---
schema_version: 1.0.0
date: 2026-04-24
task: Calibration analysis of 35 traces from 2026-04-10 to 2026-04-22
agents: [coordinator, architecture-strategist, simplicity-advocate, pattern-recognizer]
status: completed
tags: [date/2026-04-24, trace, topic/calibration, agent-chatroom]
---

# Agent Chatroom: Calibration Analysis — 2026-04-24

**Trace range:** 2026-04-10 through 2026-04-22 (35 traces, 35 decisions, 22 learnings)
**Friday weekly calibration run.**

## Coordination Log

## [14:35 ET] architecture-strategist

Completed structural analysis of all 35 traces. Five meaningful architecture gaps identified:

1. **Pipeline-manager outbound scan gap** (critical) — 2 traces (4/15 MMPC, 4/17 CIM) show silent automation failures. Skill spec is aspirational. Missing: end-to-end regression test + Attio list-entry bridge logic + launchd health verification. This is G&B-existential given May 7 DealsX 10x volume bump.

2. **Universal calibrate-before-writes hook** (high) — 4/20 trace surfaced via river-guide-builder but pattern is generic: any bulk-scan skill writing to Attio/Sheets needs dry-run + cap check + instrument-vs-lived-knowledge gate. `feedback_calibrate_before_bulk_writes.md` exists but memory is insufficient (per onepager-guardrail precedent — 3+ violations = graduate to hook). Propose PreToolUse cap-check hook.

3. **Audience-aware disclosure filter** (high) — 4/21 WSN trace + 4/22 Matchmaker trace + 4/16 Kovr trace all show "tier mismatch" failure. No hook/memory prevents continuation-vehicle leak, tier-below content misapplication, or premature-frame-mapping. Propose new memory `feedback_audience_tier_check_before_external_draft.md` + meeting-brief template hook.

4. **Source-of-truth per-question router** (high) — 4/18 DealsX trace = 3-wrong-answers from wrong source selection. CLAUDE.md has per-system routing but not per-question. Propose CLAUDE.md "Source-of-Truth by Question Type" table (niche status → tracker; partner sprint → Drive artifact; JJ actuals → call log; bookkeeping → Start Virtual PDF).

5. **Niche-intelligence filter-then-scorecard gate** (high) — 5 April traces (4/10, 4/11, 4/12 x2, 4/16, 4/18) converge on "SaaS filter vs G&B scorecard" architecture. niche-intelligence SKILL.md doesn't explicitly sequence Filter → Scorecard. Needs Step 2 update: SaaS vs non-SaaS classification + Jake+Adam gate before one-pager/score spend.

Minor/dropped from top 5:
- AI-native-vs-enhanced lens: covered well in memory already (feedback_ai_native_vs_enhanced_lens if it exists; if not, single memory update)
- Silent-focus / stress-test-constraint / silent-focus-protocol: all already have memory files
- Brief skill template architecture (4/22): landed as skill-internal refactor, no cross-system gap
- Evening-event rule softening (4/22): single trace, low; memory only
- Relationship-time ROI (4/17): covered by existing feedback_river_guide_gates + feedback_startup_vs_mature_layer

→ @pattern-recognizer — I'm seeing gap #1 (pipeline-manager) as a 2-trace cluster, gap #3 (disclosure/tier) as a 3-trace cluster, gap #5 (SaaS filter) as a 5-trace cluster. Do you see any clusters I'm missing? In particular: is "ask before drafting felt content" (4/21 WSN) a one-off or part of a broader inference-vs-dictation pattern?

→ @simplicity-advocate — My proposals 2 and 3 might be over-engineered. Challenge welcome: (a) Is gap #2 really a hook, or just a doctrine line in CLAUDE.md saying "any skill with bulk writes must default to dry-run + report + await confirmation"? (b) Is gap #3 a hook on meeting-brief, or just a checklist item in the existing brief templates? I'd downgrade either if you push.

→ READY

## [14:52 ET] pattern-recognizer

Finished tagging all 35 traces + 4-week tracker scan. Posting pattern map now so architecture-strategist can cross-check clusters and simplicity-advocate can pressure-test before I finalize proposals.

### Tag clusters (2+ items only)

**A. filter-vs-scorecard / thesis-refinement (8 items, CRITICAL)**
- 4/10 vertical-saas-thesis-conviction (scorecard is validation not selection; parallel thesis tracks)
- 4/11 specialty-healthcare (filter-vs-niche distinction; VC contamination check; consolidator check)
- 4/12 adam-right-to-win (three forms of right-to-win; don't auto-kill on incumbent concentration)
- 4/12 saas-filter-vs-scorecard (Jake+Adam filter runs BEFORE scorecard; don't re-tune scorecard)
- 4/16 ai-native-vs-enhanced (physical-workflow vs documentation-workflow split as disruption lens)
- 4/18 saltoun-multiple-compression (three-condition SaaS filter; sell-side data > sentiment)
- 4/19 path-a-services-primary (identity filter: services primary, SaaS supporting)
- 4/21 niche-ranking-methodology-pivot (external data > internal vault scoring when ranking)

**B. automation-gap / silent-failure (3 items, CRITICAL)**
- 4/15 pipeline-manager-outbound-scan (Attio List entry not auto-created from Person)
- 4/17 pipeline-manager-cim-trigger-gap (CIM auto-trigger never fired; launchd not installed 3 weeks; aspirational spec)
- 4/20 calibrate-before-writes (bulk scan about to write 800 rows; Kay's cap caught it)
- 4/20 network-yield-vs-lived-knowledge (skill returned 0 hits for niches Kay knows are populated; "instrument broken" prior)

**C. audience-tier / disclosure-calibration (5 items, HIGH)**
- 4/16 lacey-mention-vs-reengage (no-contact rule scope interpretation)
- 4/16 cold-warm-linkedin-dm (route hybrid, not warm-intro for low-ROI)
- 4/21 peer-group-hll-methodology (ask before drafting felt content; disclosure ceiling by group maturity)
- 4/21 traditional-search-peer-disclosure (no continuation-vehicle leak to traditional searchers)
- 4/22 kay-is-operator-not-absent-buyer (tier-below-searcher content premature-frame-mapping)

**D. source-of-truth routing (3 items, HIGH)**
- 4/18 dealsx-sprint-source-of-truth (3 wrong answers from wrong source — Drive sheet is partner's artifact, not tracker)
- 4/21 stress-test-constraint-methodology (hypothetical constraints ≠ durable facts)
- 4/22 brief-skill-template-architecture (typed templates under one skill, no silent fallback)

**E. outreach-routing / channel-cadence (4 items, HIGH)**
- 4/15 channel-mix-by-route (DealsX/Kay-Email/JJ-Call routing differs)
- 4/15 conference-unlock-broker-breakfasts (grass-roots intermediary events > industry conferences)
- 4/15 kay-focus-off-list-scrubbing (demote work that puts Kay in wrong mode)
- 4/17 relationship-time-roi (Gate A + Gate B 30-day test for new contacts; startup vs mature layer)

**F. silent-focus / soft-rule-softening (3 items, MEDIUM)**
- 4/21 silent-focus-protocol (prioritization ≠ deprioritization-with-announcement)
- 4/22 evening-event-override-will-cotton (durable rule with exception shape)
- (paired with 4/15 kay-focus-off-list-scrubbing — "not worth my focus" ≠ kill)

**G. niche-evaluation-framework (3 items, MEDIUM)**
- 4/12 dealsx-industry-bucket-model (broad sourcing bucket → narrow tracker niches; additive columns)
- 4/19 international-oem-structural-moat (OEM origin = disintermediation predictor)
- 4/19 commercial-laundry-reject (PE-untouched + fragmented is a TRAP; 20-min M&A desk check required)
- 4/21 oem-authorized-dealer-thesis (OEM-authorized networks are POSITIVE, don't re-litigate)

**H. reality-check / expectation-calibration (2 items, MEDIUM)**
- 4/19 reality-check-aggressive-timelines (render verdict before executing; don't match energy)
- 4/19 onepager-guardrail-tool-level (3x-correction threshold = graduate to hook)

### Funnel signals (4-week tracker scan)

Every metric that matters is **flat at zero** for 5 consecutive weeks:

| Week | Meaningful Owner Conversations | Outreach Emails | JJ Dials | NDAs | LinkedIn DMs |
|------|-------------------------------|-----------------|----------|------|--------------|
| 3/27 | 0 | 4 | 0 | 1 | 0 |
| 4/03 | 0 | 6 | 0 | 0 | 0 |
| 4/10 | 0 | 1 | 0 | 0 | 0 |
| 4/17 | 0 | 0 | 0 | 0 | 4 drafted, 0 sent |

Pattern: **system is structurally offline.** Every trace about filter refinement, tier calibration, or thesis articulation is happening against a backdrop of zero throughput. Tracker 4/17 explicitly flags: "Five consecutive weeks without a meaningful owner conversation." This reinforces **Cluster B (automation-gap)** and **Cluster A (filter-vs-scorecard thesis work)** as critical — because if the pipeline is offline, (1) automation failures are invisible (no volume to test), and (2) thesis refinement is replacing pipeline throughput, not adding to it.

It also validates **4/15 kay-focus-off-list-scrubbing** — Kay pulling back on manual outreach is a deliberate choice, not a gap; but the system needs to convert DealsX 5/6 launch + JJ reactivation into measurable throughput, NOT keep refining the filter layer.

### Response to architecture-strategist questions

**@architecture-strategist:**
- Confirm Cluster A is bigger than your 5 — I count 8 traces including 4/16 AI-native lens + 4/19 path-a-services + 4/21 ranking-methodology-pivot as all being about "how do we filter before we score." The pattern is not just "SaaS filter before scorecard" but broader: **"identity/thesis filter (pass/fail) runs BEFORE any ranking/scoring exercise."** niche-intelligence SKILL.md needs both: the SaaS-specific Jake+Adam filter AND a parent "does this fit G&B Charter identity" filter (services-primary per Path A).
- "Ask before drafting felt content" (4/21 WSN) is part of **Cluster C (audience-tier)** not a one-off. The underlying pattern is "inference substitutes for dictation at the cost of accuracy in audience-calibrated content." Combined with 4/22 Matchmaker (premature frame mapping) and 4/21 traditional-searcher-disclosure, the cluster is 5-deep. Downgrading to memory alone is risky — these are repeat failures (Kay corrected same pattern 3+ times across 2 traces in one night).
- Your Cluster D (source-of-truth) matches my D. Support adding CLAUDE.md table.

**@simplicity-advocate:** — in advance of your pass —
- Cluster B (automation-gap) genuinely needs hooks. 4/17 CIM trigger failed silently for 3 weeks because memory-level "run this on CIM" was insufficient. DealsX 5/6 is 12 days out. This is not over-engineering; this is pre-May-7 hardening that Kay explicitly asked for.
- Cluster C (disclosure) — memory alone has failed repeatedly. But a hook is hard to specify (context-dependent). Middle path: **meeting-brief / investor-update skill template pre-flight checklist** that the skill must surface before draft. Not a tool-level hook, but not pure memory either.
- Cluster F (silent-focus) and Cluster H (reality-check) are doctrine, not automation. Memory + CLAUDE.md is sufficient.

### Patterns → system targets map

| Pattern Cluster | Items | Severity | Target |
|---|---|---|---|
| A. Identity/thesis filter before scorecard | 8 | CRITICAL | skill:niche-intelligence (Step 2 refactor), CLAUDE.md ("Source of Truth" section), memory:feedback_identity_filter_before_scorecard |
| B. Automation-gap / silent failures | 4 | CRITICAL | skill:pipeline-manager (regression test), hook:calibrate-before-bulk-writes (PreToolUse), launchd health verification |
| C. Audience-tier / disclosure | 5 | HIGH | memory:feedback_audience_tier_check, skill:meeting-brief + investor-update (pre-flight checklist), skill:outreach-manager (draft-time filter) |
| D. Source-of-truth per-question | 3 | HIGH | CLAUDE.md ("Source of Truth" per-question table), memory:feedback_source_of_truth_per_question |
| E. Outreach routing / channel cadence | 4 | HIGH | skill:outreach-manager (route-specific cadence enforcement), memory already covers most |
| F. Silent-focus / soft rule softening | 3 | MEDIUM | Existing memories (codified 4/21, 4/22) — no further action |
| G. Niche-evaluation framework | 4 | MEDIUM | skill:niche-intelligence (add M&A desk check + OEM-origin screen) |
| H. Reality-check / expectation | 2 | MEDIUM | Existing memories — no further action |

### Top 5 proposals (prioritized)

#### 1. niche-intelligence Step-2 Identity Filter + SaaS Filter + M&A Desk Check
**Target:** skill:niche-intelligence + memory:feedback_identity_filter_before_scorecard
**Pattern:** 8 traces converge on "run filter before scorecard; filter and scorecard are different tools." Currently SKILL.md doesn't explicitly sequence this, and the filter is SaaS-specific (Jake+Adam) when the pattern is broader (Path A services-primary identity filter ALSO runs).
**Source items:** 2026-04-10-vertical-saas, 2026-04-11-specialty-healthcare, 2026-04-12-adam-right-to-win, 2026-04-12-saas-filter-vs-scorecard, 2026-04-16-ai-native-vs-enhanced, 2026-04-18-saltoun-software-multiple-compression, 2026-04-19-path-a-services-primary, 2026-04-21-niche-ranking-methodology-pivot
**Importance:** CRITICAL (8 items, recurring)
**Change:** Rewrite niche-intelligence Step 2 as three sequential gates: (a) **Identity Filter** — services-primary check per Path A, AI-native disruption check per physical-workflow rule, hard exclusions (no California, no lending, no PE-owned, no continuation-vehicle leak); (b) **Structural Filter** — VC contamination, active consolidator, OEM origin, 20-min M&A desk check (named sponsors/public strategics); (c) **Scorecard (ranking only, not selection)**. If any gate fails, niche does NOT proceed to one-pager. Codify gates in `examples/filter-checklist.md` + update `.claude/skills/niche-intelligence/SKILL.md` Step 2.

#### 2. Pipeline-manager Regression + calibrate-before-writes Hook
**Target:** skill:pipeline-manager + hook:.claude/hooks/router/handlers/calibrate_before_bulk_writes.py
**Pattern:** Silent automation failures have already happened twice (MMPC 4/15, CIM 4/17). DealsX 5/6 launch = ~10x volume. Bulk-write scans without dry-run / cap-check nearly clobbered Network Matches (4/20).
**Source items:** 2026-04-15-pipeline-manager-outbound-scan, 2026-04-17-pipeline-manager-cim-trigger, 2026-04-20-calibrate-before-writes, 2026-04-20-network-yield-vs-lived-knowledge
**Importance:** CRITICAL (existential before 5/6)
**Change:** (a) Add end-to-end regression test: seed fake outbound email → verify Attio list-entry auto-created. (b) PreToolUse hook on Write/Edit/MultiEdit for bulk Attio/Sheet writes: require `dry_run: true` first OR explicit `kay_approved_count: N` matching actual write count. Blocks silent 800-row clobbers. Narrow scope per onepager-guardrail precedent.

#### 3. Audience-Tier Disclosure Filter for External-Facing Drafts
**Target:** memory:feedback_audience_tier_disclosure + skill:meeting-brief + skill:investor-update + skill:outreach-manager (pre-draft checklist)
**Pattern:** 5 traces of "wrong frame/tier applied to external content." Includes: continuation-vehicle leak to traditional peers, tier-below-searcher content misapplication, premature frame-mapping from newsletter content, oversharing vulnerability with month-2 peers, strategic-context leaking into artifacts.
**Source items:** 2026-04-16-lacey-mention, 2026-04-16-cold-warm-linkedin-dm, 2026-04-21-peer-group-hll, 2026-04-21-traditional-search-peer-disclosure, 2026-04-22-kay-is-operator
**Importance:** HIGH (5 items, multiple same-night repeat corrections)
**Change:** New memory `feedback_audience_tier_disclosure.md` with: (a) Prohibited-language list for traditional-searcher contexts (HoldCo, continuation vehicle, multi-acquisition portfolio, Wertheimer); (b) Disclosure-ceiling calibration by group maturity (Month-2 peers ≠ established advisors) + Kay's relative position in room; (c) "Ask before drafting felt content" default for any H/L/L, reflection, or peer-group prep. Plus pre-draft checklist embedded in meeting-brief/investor-update templates that surfaces the audience classification BEFORE drafting begins.

#### 4. Source-of-Truth Per-Question Routing Table
**Target:** CLAUDE.md Querying section + memory:feedback_source_of_truth_per_question
**Pattern:** 3 traces of "wrong source read, wrong answer." DealsX sprint = Drive artifact not tracker; stress-test constraints ≠ durable facts; brief templates must be explicitly routed by mode (no silent generic fallback).
**Source items:** 2026-04-18-dealsx-sprint-source-of-truth, 2026-04-21-stress-test-constraint-methodology, 2026-04-22-brief-skill-template-architecture
**Importance:** HIGH (3 items, different contexts same failure mode)
**Change:** Add Source-of-Truth table to CLAUDE.md "Querying" section keyed by question type, not by system. Rows: "What is partner X building against THIS sprint?" → Partner's working Drive artifact, not internal tracker. "What are niche STATUSES?" → tracker. "What has JJ actually DIALED?" → JJ's call log. "Is this constraint DURABLE?" → explicit commitment language required, default to stress-test interpretation. "What template for brief mode X?" → `{skill}/templates/{mode}.md`, error if unspecified.

#### 5. Niche-Evaluation Heuristics Pack (M&A Desk Check + OEM Origin)
**Target:** skill:niche-intelligence Step 1 (reference doc additions)
**Pattern:** 4 traces show "surface pattern looks fragmented/attractive, structural reality is consolidating or disintermediating." Reusable heuristics that should run on every new niche before spending one-pager cycles.
**Source items:** 2026-04-12-dealsx-industry-bucket-model, 2026-04-19-commercial-laundry-reject, 2026-04-19-international-oem-structural-moat, 2026-04-21-oem-authorized-dealer-thesis
**Importance:** MEDIUM (4 items, reusable framework)
**Change:** Add `.claude/skills/niche-intelligence/references/structural-screens.md` with two named heuristics: (a) **20-minute M&A Desk Check** — named sponsors + public strategics + searcher activity; if EVI-style accumulator exists with 10+ deals in <5 years, window is closing; absence of searcher activity in attractive-looking category = warning sign. (b) **OEM-origin Disintermediation Screen** — international/family-owned = low risk; US-origin/PE-backed/scale = high risk; OEM-authorized independent dealer = POSITIVE structural moat. Surface both in Step 1 before tracker row is created.

→ @architecture-strategist — my Cluster A is larger than your Gap 5 (I count 8 not 5). Your proposal is correct but should scope to BOTH the SaaS-specific filter AND the Path A services-primary identity filter — they're layered. Agree your Gap 1 (pipeline-manager) is CRITICAL; timing against 5/6 DealsX launch makes it existential.
→ @simplicity-advocate — Cluster B needs hooks (pre-launch hardening, Kay explicitly asked). Cluster C and D I've softened from hooks to checklist/memory+template based on your anticipated pushback. Cluster F/H I'm leaving as pure memory. Please challenge Proposal 2's scope if you think the regression test alone is enough without the bulk-write hook.

→ READY

## [15:10 ET] simplicity-advocate

Read 35 traces + full system inventory (39 skills, 4 hooks, 392 memory files, 317-line CLAUDE.md). Both arch-strat and pattern-recognizer have posted. Responding to their direct questions, then my own proposals.

### Direct replies to @architecture-strategist

**(a) Gap #2 — universal calibrate-before-writes hook: CONDITIONALLY UPGRADE.** Reversing my initial stance after reading pattern-recognizer's Cluster B data. I originally said "1 violation = memory only" per onepager-guardrail precedent. Pattern-recognizer counts 4 items (4/15 MMPC + 4/17 CIM + 4/20 calibrate + 4/20 network-yield) and notes DealsX 5/6 = 12 days out. That crosses the 3x threshold. BUT narrow the hook aggressively: do NOT make it a universal PreToolUse on Write/Edit/MultiEdit — that will false-positive on every legitimate edit. Narrow to: bulk Attio `batch_records` / `create_record` calls with `N > 10`, AND bulk Sheet writes to `gog sheets update` with range spanning >10 rows. Two specific tool-call signatures, not a generic blanket. Same narrow-scoping discipline as onepager-guardrail (path-pattern only fires on niche-one-pager files).

**(b) Gap #3 — audience-tier filter: STILL DOWNGRADE.** Pattern-recognizer moved it to memory+template checklist, which matches what I'd recommend. Don't add a hook. The meeting-brief template architecture (2026-04-22) is the right home. BUT consolidate the new `feedback_audience_tier_disclosure.md` with existing `feedback_never_say_fund.md`, `feedback_never_say_fund_or_lead.md`, `feedback_outreach_no_strategy_leaks.md`, `feedback_outreach_no_fake_lines.md`, `feedback_no_revenue_in_outreach.md` — all five express facets of "audience-calibrated disclosure." One file, not six.

### Direct replies to @pattern-recognizer

**Cluster B hooks support: qualified yes.** Only if the hook fires on specific tool-call signatures, not a blanket bulk-write filter. See answer to arch-strat (a).

**Cluster C memory+template approach: yes.** But per my reply to arch-strat — CONSOLIDATE with 5 existing disclosure/voice memory files instead of adding a new one.

**Cluster A (8 items) and identity-filter-before-scorecard:** Support. But the fix is niche-intelligence SKILL.md Step 2 refactor + one new memory file. No new skills, no new hooks. Pattern-recognizer's proposal #1 is correctly scoped.

**On funnel flat-at-zero observation:** This is the most important system-level signal in the entire calibration. 5 weeks of zero meaningful owner conversations means Claude-Kay has been REFINING while the pipeline is offline. Simplicity implication: resist any proposal that adds complexity without directly moving throughput. Every hook/skill/memory added this cycle should be justified against "does this help throughput hit positive numbers in 2 weeks?" Otherwise it's polishing the machine that isn't running.

### Complexity Issues Found

| Component | Problem | Recommendation |
|-----------|---------|----------------|
| `.claude/skills/meeting-brief-manager/` | Retired Apr 12 per CLAUDE.md L281, still 587 lines on disk | Remove directory |
| `.claude/skills/nightly-tracker-audit/` | Overlaps tracker-manager; fuzzy seam | Fold into tracker-manager `--mode=nightly-audit` |
| Superhuman memory files (3 stale) | Rule in 5 places; 27-31 days old; contain stale March-23 bug as live guidance | Delete 3 files; CLAUDE.md L155-158 canonical |
| Briefing-format rules (8 memory files) | Same doctrine expressed 8x; `feedback_morning_briefing_categories` superseded unmarked | Consolidate into `feedback_briefing_doctrine.md` |
| Audience-disclosure memory files (5 existing + arch-strat's new one) | 6 memory files on one doctrine | Consolidate into `feedback_audience_disclosure.md` |
| `feedback_draft_before_send.md` | Indexed 2x in MEMORY.md (L101, L107) | De-duplicate index |
| `project_session_*.md` (13 files) | Never cited in 4/10-4/22 traces; duplicate session-decisions | Delete 13 files |
| `feedback_art_storage_tabled_rationale.md` | Self-marked SUPERSEDED 4/19 | Delete |
| CLAUDE.md Brief-decisions pre-flight (L276-281) | 6-line nested rule with HOLD sub-rule added 4/23 | Move body to pipeline-manager SKILL.md; 1-line ref in CLAUDE.md |

### Proposals (max 5, prioritized)

#### 1. Remove retired meeting-brief-manager skill directory
**Target:** skill:meeting-brief-manager
**Issue:** CLAUDE.md line 281 explicitly retires this skill ("replaces the retired `meeting-brief-manager` nightly automation (Apr 12)"). Still 587 lines on disk, still appears in skill enumeration, still has a launchd trigger possibility. Future agents will try to invoke it. Replacement split between `meeting-brief` (generation) and CLAUDE.md briefing pre-flight (trigger).
**Source traces:** 2026-04-19-briefing-architecture, 2026-04-22-brief-skill-template-architecture, CLAUDE.md L281
**Importance:** high
**Proposed change:**
Delete `.claude/skills/meeting-brief-manager/`. Verify no launchd plist still loads it. Remove stale CLAUDE.md references. Confirm `meeting-brief` has absorbed the external-meeting logic per 2026-04-22 trace.

#### 2. Fold nightly-tracker-audit into tracker-manager
**Target:** skill:nightly-tracker-audit
**Issue:** Two skills own Industry Research Tracker hygiene with overlapping scope. tracker-manager SKILL.md L15 explicitly says "End-of-day cleanup beyond what nightly-tracker-audit handles" — forcing Claude to guess. tracker-manager has snapshot/validate/verify guardrails nightly-tracker-audit lacks.
**Source traces:** 2026-04-21-tracker-manager-rank-reorder (tracker-manager already doing the work), general observation
**Importance:** high
**Proposed change:**
Add `--mode=nightly-audit` to tracker-manager running the deterministic cleanup (move Tabled/Killed, re-sort, re-rank, Drive folder moves, blank-row removal). Update launchd plist to invoke `tracker-manager --mode=nightly-audit`. Delete `.claude/skills/nightly-tracker-audit/`. Update CLAUDE.md scheduled skills table.

#### 3. Consolidate briefing-format doctrine; consolidate audience-disclosure doctrine
**Target:** memory:consolidate:feedback_briefing_three_buckets,feedback_decision_fatigue_minimization,feedback_morning_briefing_format,feedback_morning_briefing_categories,feedback_briefing_no_done_items,feedback_ascending_numbering,feedback_additive_numbering,feedback_c_suite_naming AND memory:consolidate:feedback_never_say_fund,feedback_never_say_fund_or_lead,feedback_outreach_no_strategy_leaks,feedback_outreach_no_fake_lines,feedback_no_revenue_in_outreach (plus arch-strat's proposed new audience-tier memory)
**Issue:** Two overlapping rule-clusters. Eight memory files express the briefing format doctrine captured in CLAUDE.md L261-275. Five (soon to be six) memory files express audience-disclosure rules. Each bloats memory directory and creates read-tax at draft time.
**Source traces:** 2026-04-19-briefing-architecture, 2026-04-21-peer-group-hll, 2026-04-21-traditional-search-peer-disclosure, 2026-04-22-kay-is-operator
**Importance:** high
**Proposed change:**
Create `feedback_briefing_doctrine.md` (absorb 8 briefing rules). Create `feedback_audience_disclosure.md` (absorb 5-6 disclosure rules including new audience-tier content). Delete the 13 source files. Update MEMORY.md index.

#### 4. Delete 3 stale Superhuman memory files; de-duplicate draft-before-send; delete 13 session retrospective files; delete superseded art-storage file
**Target:** memory:delete:feedback_drafts_superhuman,feedback_superhuman_drafts_only,feedback_drafts_in_superhuman_not_cursor,project_session_march_19,project_session_march_22,project_session_march_24,project_session_march_25,project_session_march_26,project_session_march_27,project_session_march_28,project_session_march_29,project_session_march_30,project_session_march_31,project_session_march_31_pm,project_session_april_1,project_session_april_4,feedback_art_storage_tabled_rationale
**Issue:** 17 memory files collectively: (a) 3 Superhuman files are 27-31 days old, predate the canonical Bash wrapper in CLAUDE.md L155-158, contain stale March-23 bug as live guidance; (b) 13 project_session_* retrospectives never cited in 4/10-4/22 traces and duplicate `brain/context/session-decisions-*`; (c) 1 art-storage file self-marked SUPERSEDED 4/19. Also: MEMORY.md indexes `feedback_draft_before_send.md` twice (L101, L107).
**Source traces:** general observation; `feedback_vault_single_source.md` doctrine
**Importance:** medium
**Proposed change:**
Delete 17 files. Remove from MEMORY.md index. Remove duplicate L107 entry for `feedback_draft_before_send.md`. Net: memory directory drops from 392 to 375 files; 4 memory-query-spots collapse.

#### 5. Move brief-decisions pre-flight logic from CLAUDE.md to pipeline-manager SKILL.md
**Target:** claude-md (lines 276-281) + skill:pipeline-manager
**Issue:** CLAUDE.md Morning Workflow L276-281 contains a 6-line nested rule with a HOLD-prefix sub-rule added 2026-04-23. This is skill-specific logic in top-level orchestration doc. It will accrete as more exceptions are added (currently HOLD-prefix; next will be "soft-confirm" or similar). CLAUDE.md should describe WHAT happens in morning workflow; pipeline-manager should describe HOW.
**Source traces:** general observation of recent CLAUDE.md growth (L278 HOLD-prefix sub-rule added 4/23)
**Importance:** medium
**Proposed change:**
Move full brief-decisions pre-flight logic (HOLD gate + session-decision lookback + RECOMMEND framing) into `.claude/skills/pipeline-manager/SKILL.md`. Leave one line in CLAUDE.md Step 9: "Before delivering the brief, run pipeline-manager's brief-decisions pre-flight (see SKILL.md)." Net: CLAUDE.md drops ~5 lines; future exceptions land in the skill file where they logically belong.

---

### Challenges to Architecture-Strategist

1. **Gap #2 (calibrate-before-writes hook): PARTIAL CHALLENGE.** I initially said "downgrade to doctrine only" but pattern-recognizer's 4-item Cluster B + DealsX 5/6 timing crosses the 3x threshold. Upgrade OK. But narrow the hook aggressively to two specific tool-call signatures (Attio batch N>10; gog sheets update range >10 rows). Do NOT make it a blanket PreToolUse on all Write/Edit/MultiEdit — that will false-positive on legitimate edits.
2. **Gap #3 (audience-tier hook): STILL CHALLENGE.** No new hook. Pattern-recognizer already downgraded to memory+template checklist. Further: consolidate the new `feedback_audience_tier_check` with 5 existing disclosure-rule memory files into one `feedback_audience_disclosure.md`. Adding a 6th memory file to an existing cluster of 5 is the wrong direction — memory directory needs consolidation, not accretion.
3. **Gap #4 (source-of-truth table): support with caveat.** Support adding the per-question table to CLAUDE.md. But do NOT also create a parallel `feedback_source_of_truth_per_question.md` memory file (which pattern-recognizer's Proposal #4 proposes). One location, not two.
4. **Gap #5 (niche-intelligence filter-then-scorecard): support.** Keep entirely inside niche-intelligence SKILL.md Step 2 + one supporting memory file per pattern-recognizer Proposal #1. No new skill.

### Challenges to Pattern-Recognizer

1. **Proposal #1 (identity filter): support as-is.** Pattern-recognizer has the scope right. One skill, one memory file.
2. **Proposal #2 (pipeline-manager regression + hook): support with narrowing.** See arch-strat challenge (1) above — narrow the hook to specific tool-call signatures.
3. **Proposal #3 (audience-tier): CHALLENGE on "new memory file + pre-draft checklist."** Consolidate with 5 existing disclosure files into ONE `feedback_audience_disclosure.md` that includes the new audience-tier content. Pre-draft checklist stays in templates per 2026-04-22 architecture.
4. **Proposal #4 (source-of-truth): support CLAUDE.md table.** Drop the parallel memory file — duplication. CLAUDE.md Querying section is the right home.
5. **Proposal #5 (niche heuristics pack): support, but put in references/ folder not top of SKILL.md.** Agree with the reference-doc placement pattern-recognizer already proposed.

→ READY


## [15:14 ET] coordinator (orchestrator-closed)

All 3 analysts posted → READY. Orchestrator absorbed analyst outputs directly (synthesis path) and is generating the calibration proposal at brain/outputs/calibrations/2026-04-24-calibration.md.

Conflicts resolved:
- Cluster B hook scope: simplicity-advocate's narrow-scoping accepted (specific tool-call signatures, not blanket Write/Edit hook).
- Cluster C target: pattern-recognizer's downgrade-to-memory+template accepted; simplicity-advocate's consolidation-with-existing-files folded in.
- Cluster D source: arch-strat + pattern-recognizer agree on CLAUDE.md table; pattern-recognizer's parallel memory file dropped per simplicity-advocate.

→ CLOSE

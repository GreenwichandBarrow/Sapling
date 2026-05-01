---
schema_version: 1.0.0
date: 2026-04-30
task: Calibration analysis of 69 unreviewed traces (2026-04-10 to 2026-04-29)
agents: [coordinator, architecture-strategist, simplicity-advocate, pattern-recognizer]
status: active
tags: [date/2026-04-30, trace, agent-chatroom, topic/calibration]
---

# Agent Chatroom: Calibration Analysis 2026-04-30

## Coordination Log

### coordinator @ 2026-04-30 (post-poll-8)

STUCK — polled chatroom 8 times over ~8 minutes (60s intervals). Zero `-> READY` markers, zero posts from architecture-strategist, simplicity-advocate, or pattern-recognizer. Chatroom never received any agent output beyond this header.

Closing per timeout protocol. No synthesis possible because no findings were posted.

-> CLOSE

---

## simplicity-advocate findings

Sampled 28 of 69 traces with focus on: skill architecture, briefing format, taxonomy splits, schema decisions, memory consolidation, and migration patterns. Cross-checked against `MEMORY.md` (110+ entries) and `.claude/skills/` inventory (40 active skills).

### YAGNI / Over-engineering observations

- **Brief-skill family architecture decision was already YAGNI-correct** (trace `2026-04-22-brief-skill-template-architecture`): rejected splitting into 7 sibling skills, kept 2 parent skills with templates/. This is the canonical anti-proliferation pattern — but the precedent is buried in a single trace and not surfaced as a generalizable rule. **Not a cut**, but propose promoting to a memory rule so future skill-design decisions reach for it by default.

- **Audience taxonomy: 4 buckets collapsed to 3** (trace `2026-04-23-advisor-collapses-into-intermediary`). Same anti-proliferation pattern: "If two titles resolve to the same body, they're one bucket." Already memory-codified as `feedback_audience_taxonomy_conferences` per trace; verify still present.

- **Tech Stack page collapsed into Infrastructure** (trace `2026-04-24-merge-tech-stack-into-infrastructure`). 7-section IA → 6-section after Kay's "wow I love infrastructure now." Memory: `feedback_collapse_thin_boundaries.md`. Same family of cut.

- **Briefing buckets: 5 source-org → 4 action-keyed → 1 Decisions-only** (traces `2026-04-19-briefing-architecture-shift-to-action-keyed-buckets`, `2026-04-25-decisions-only-briefing-emoji-tags`). Two structural cuts in two weeks. Each migration required preserving signal in alternative encoding (clustering, urgency emojis). **Pattern is mature** — codified in CLAUDE.md and `feedback_briefing_three_buckets`.

- **VIP Gmail filters → native Gmail Important learning** (trace `2026-04-26-vip-filters-replaced-by-native-learning`). Deleted 12 hardcoded rules in favor of native ML. Pattern: "Defaulting to filters for everything misuses the rule layer for problems the ML layer solves better." Memory missing — propose codifying.

- **Personal task tracker stayed memory + scripts, did NOT become a skill** (trace `2026-04-27-personal-tooling-not-skill`). Litmus: "Will Kay invoke this slash command >5x/year?" Skills proliferate; clutter has cost. **Codify as skill-creation pre-flight** — this is the only documented anti-skill heuristic in the corpus.

- **Niche-ranking first-pass (4-dimension internal-data lens) rejected as "full of holes and fluff"** (trace `2026-04-21-niche-ranking-methodology-pivot`). Lesson: external-data-only methodology, internal scoring layered on weak data is YAGNI failure mode. Already codified as `feedback_niche_ranking_searcher_criteria_only`.

- **Bumping retry count was the wrong layer fix** for parallel-fire collisions (trace `2026-04-29-stagger-launchd-plists-collision`). Stagger at plist layer, not retries at wrapper layer. Codified `feedback_launchd_parallel_fire_collisions`.

### Memory consolidation candidates

The MEMORY.md index is **461 lines / 76.3KB** and the warning at the bottom says "Only part of it was loaded." This is a critical signal that the index has crossed an operational threshold. Direct consolidation candidates:

1. **Briefing-format memories overlap heavily**:
   - `feedback_briefing_three_buckets.md` (now describes single Decisions list, not 3 buckets — name is stale)
   - `feedback_morning_briefing_format.md` ("every item needs explicit question or action")
   - `feedback_morning_briefing_categories.md` ("organized by action type, not source")
   - `feedback_decision_fatigue_minimization.md`
   - `feedback_briefing_no_done_items.md`
   - `feedback_post_conference_replies_reactive_only.md` (briefing surface rule)
   - `feedback_relationship_cadence_friday_only.md` (briefing surface rule)
   - `feedback_scheduled_vs_todo_presentation.md` (briefing surface rule)
   - **Propose: merge into one `feedback_briefing_doctrine.md`** — single rule file with sub-sections (format, surface filters, decision fatigue, urgency tags). Rename `feedback_briefing_three_buckets` to match current reality.

2. **Outreach-voice memories are 8+ files saying related things to overlapping audiences**:
   - `feedback_no_revenue_in_outreach.md`
   - `feedback_never_say_fund.md`
   - `feedback_outreach_about_them.md`
   - `feedback_outreach_no_strategy_leaks.md`
   - `feedback_outreach_no_fake_lines.md`
   - `feedback_email_no_em_dashes.md`
   - `feedback_email_niceties.md`
   - `feedback_sign_off_style.md`
   - `feedback_first_reply_formal_name.md`
   - `feedback_day_aware_signoffs.md`
   - `feedback_no_search_fund_language_intermediaries.md`
   - `feedback_no_sunday_emails.md`
   - `feedback_continue_dont_reintroduce.md`
   - `feedback_buyside_advisor_success_fee_only.md` (different — keep)
   - `feedback_email_direct_ask_only.md`
   - **Propose: merge into `feedback_outreach_voice_doctrine.md`** with audience sub-sections (Owner / Intermediary / Reply / Banker). The Pre-Flight checklist in CLAUDE.md already covers most of these inline; the per-rule files are reference depth.

3. **Superhuman migration memories are now contradictory/stale**:
   - `feedback_drafts_superhuman.md` — explicitly DEPRECATED per index entry
   - `feedback_gmail_only_no_superhuman.md` — supersedes it
   - `feedback_draft_sharing_for_learning.md` — references Superhuman
   - `feedback_superhuman_drafts_only.md` — references Superhuman as drafts-only
   - **Propose: delete the 3 deprecated/Superhuman-named entries**. Keep `feedback_gmail_only_no_superhuman.md`. The deprecated entry being still indexed wastes context budget.

4. **Secret-handling memories**:
   - `feedback_never_echo_secrets.md`
   - `feedback_never_echo_phone_number_in_chat.md`
   - `feedback_never_read_config_with_secrets.md`
   - `feedback_secrets_to_terminal.md`
   - `feedback_secrets_tmp_method.md`
   - `feedback_curl_verify_before_mcp.md`
   - **Propose: merge into `feedback_secrets_handling.md`** — already a Pre-Flight checklist in CLAUDE.md. Single doctrine file with each rule as a section.

5. **Niche-evaluation memories**:
   - `feedback_no_lending.md`
   - `feedback_no_california.md`
   - `feedback_no_carveouts.md`
   - `feedback_searcher_overlap.md`
   - `feedback_niche_not_industry.md`
   - `feedback_oem_authorized_dealer_supports_thesis.md`
   - `feedback_niche_search_direction.md`
   - `feedback_niche_ranking_searcher_criteria_only.md`
   - `feedback_silent_focus_not_formal_drop.md`
   - **Propose: merge into `feedback_niche_doctrine.md`** with sections (hard exclusions / soft filters / methodology). Currently scattered.

6. **Skill-architecture memories** (newer, important to preserve, but consolidate):
   - `feedback_mutating_skill_hardening_pattern.md`
   - `feedback_launchd_parallel_fire_collisions.md`
   - `feedback_skills_build_on_each_other.md`
   - `feedback_remove_kay_from_loop.md`
   - **Propose: keep separate** — these are operational doctrine for different problem classes (hardening vs scheduling vs composition vs autonomy), not redundant.

### Skill sunset candidates

Inspecting the 40-skill inventory against the 28 sampled traces:

- **`generate-prd`, `generate-stories`, `generate-visuals`, `github`, `plan-refinery`** — none invoked in any of the sampled traces. These are general-purpose dev tooling; they're either useful elsewhere or unused. **Defer cut** unless calibration-workflow has invocation telemetry that confirms zero use.
- **`onboard`** — Kay's already onboarded; the skill is one-shot. **Defer**: harmless dormant skill.
- **`triage`** — appears once in inventory, listed twice in skill-loader output (suggests duplicate registration). Sampled traces don't exercise it. **Investigate**: confirm whether Kay actively uses `/triage`; if not, candidate for removal.
- **`migration-workflow`** vs `/migrate` slash command — appears redundant at first glance. Trace `2026-04-23-jj-col-u-overwrite-and-schema-migration` shows actual schema-migration work happened via subagent + scripts, NOT via `migration-workflow` skill. **Investigate**: is migration-workflow skill being used at all, or has it been superseded by ad-hoc subagent migrations?
- **`obsidian-vault-ops`** — fundamental but does it have invocations or is its work folded into other skills' direct vault writes? Likely the latter. **Defer**: probably load-bearing as a reference, low cost to keep.

No confident sunset recommendations from the sampled traces alone. The above are flags for the architecture-strategist or human review, not cuts.

### Proposed changes (importance: critical|high|medium|low)

1. **[high]** Target: `memory/MEMORY.md` (index file)
   - Current: 461 lines / 76.3KB, partial-load warning, 110+ entries with significant overlap
   - Change: Consolidate per the 6 groups above. Target index < 200 lines / < 30KB. Move detail into topic files; keep index entries to one line < 200 chars (already the policy in the file's own warning).
   - Why: Loader truncation means rules at the bottom of MEMORY.md may not be loading at all. This is silent rule-decay. Consolidation also reduces calibration noise — calibration-workflow has to reason over fewer files.
   - Source: traces `2026-04-19-briefing-architecture-shift-to-action-keyed-buckets`, `2026-04-25-decisions-only-briefing-emoji-tags`, `2026-04-26-superhuman-hybrid-migration`, `2026-04-29-no-search-fund-language-intermediaries`, plus the file's own auto-warning.

2. **[high]** Target: `feedback_drafts_superhuman.md` + 2 other Superhuman-named memories
   - Current: explicitly DEPRECATED but still indexed; `feedback_superhuman_drafts_only.md` still active; `feedback_draft_sharing_for_learning.md` references the deprecated workflow
   - Change: Delete `feedback_drafts_superhuman.md` (deprecated). Delete `feedback_superhuman_drafts_only.md` (superseded by `feedback_gmail_only_no_superhuman.md` per Apr 29 sunset). Update `feedback_draft_sharing_for_learning.md` to remove Superhuman reference (the calibration-signal logic still applies to Gmail drafts).
   - Why: Stale memories actively mislead. Index entry says "DEPRECATED" but the file still loads — defeats the purpose of deprecation.
   - Source: trace `2026-04-26-superhuman-hybrid-migration`, MEMORY.md index entries.

3. **[medium]** Target: `memory/feedback_skill_creation_litmus.md` (new file)
   - Current: No memory codifies the skill-vs-memory split, despite trace `2026-04-27-personal-tooling-not-skill` documenting it explicitly.
   - Change: Create memory with the litmus question: "Will Kay invoke this slash command >5x/year? If yes → skill. If no → memory + scripts." Reference the personal-task-tracker precedent.
   - Why: Skill proliferation has real cost (loader budget, mental model, calibration noise). Without a codified rule, the next "should this be a skill?" decision will likely default to yes.
   - Source: trace `2026-04-27-personal-tooling-not-skill`.

4. **[medium]** Target: `memory/feedback_briefing_three_buckets.md`
   - Current: Filename and possibly content describe a 3-bucket briefing structure that's been superseded twice (3-bucket → 4-bucket Apr 19 → Decisions-only Apr 25).
   - Change: Rename to `feedback_briefing_doctrine.md` and rewrite to reflect current Decisions-only state, or delete if `feedback_decision_fatigue_minimization` covers the same ground.
   - Why: Stale filename → wrong rule retrieved → format regression.
   - Source: traces `2026-04-19-briefing-architecture-shift-to-action-keyed-buckets`, `2026-04-25-decisions-only-briefing-emoji-tags`.

5. **[medium]** Target: `memory/feedback_categorical_vs_behavioral_classification.md` (new)
   - Current: trace `2026-04-26-vip-filters-replaced-by-native-learning` documents the rule, no memory codifies.
   - Change: Create memory: "Categorical rules → filters; behavioral importance → native ML. Don't propose hardcoded VIP filters."
   - Why: Recurring future decision: every time Kay or Claude considers a routing rule, this distinction needs to be at hand.
   - Source: trace `2026-04-26-vip-filters-replaced-by-native-learning`.

6. **[low]** Target: skill inventory hygiene
   - Current: 40 skills registered; `/triage` appears duplicated in skill-loader output (registered twice).
   - Change: Audit duplicate `/triage` registration. Inventory which skills haven't been invoked in 30 days; flag for sunset review (don't auto-cut without Kay sign-off).
   - Why: Skills carry loader cost even when dormant; duplicate registration is a config bug.
   - Source: skill-loader output in this session showing two `triage` entries; absence of invocation in sampled traces.

7. **[low]** Target: `memory/feedback_skill_boundaries_track_hygiene.md` (new)
   - Current: trace `2026-04-22-brief-skill-template-architecture` documents the heuristic but no memory.
   - Change: Codify: "Skill boundaries should track shared hygiene, not shared output format. Same hygiene + different templates → one skill, multiple templates. Different hygiene + same template → separate skills."
   - Why: Anti-proliferation rule. Will recur on every "should we split this skill?" question.
   - Source: trace `2026-04-22-brief-skill-template-architecture`.

-> READY

---

## pattern-recognizer findings

Sampled ~22 traces across voice/communications, process/skills, technical/launchd, and audience-taxonomy buckets. Cross-referenced against existing memory feedback files and existing hooks (`.claude/hooks/router/handlers/`). Three traces from 2026-04-30 not yet present in the trace folder — the 2026-04-30 sweep itself will produce them later today.

### Repeated patterns (rule graduation candidates)

1. **"Lead with what THEY cared about, not what we noticed."** Appears in:
   - 2026-04-29-lead-with-what-they-care-about (Hoffman community-fit)
   - 2026-04-29-no-search-fund-language-intermediaries (Heritage-Holding voice match)
   - 2026-04-23-buy-box-paragraph-kay-authored ("able to retain employees" — what owners care about)
   - 2026-04-23-seller-short-transition-matters (encode flexibility implicitly)
   - 2026-04-22-evening-event-override-will-cotton-studio (Kay rejecting "kind of room I love being in" as cheesy = explicit room-labeling = self-centered)
   - Count = 5
   - Current handling: `feedback_outreach_about_them.md`, `feedback_outreach_no_strategy_leaks.md`, `feedback_continue_dont_reintroduce.md` — three separate memories, all directionally correct but none catch the **specific failure mode** (data-rich opener vs values-rich opener).
   - Suggested graduation: **New consolidated memory** `feedback_voice_lead_with_their_emphasis.md` that codifies the litmus from the Hoffman trace ("if recipient reads opener and thinks 'this person actually listened,' it works; if they think 'this person caught the headline numbers,' it doesn't"). Cross-link from existing 3 memories. Not yet hook-worthy because detection is semantic.

2. **Premature/false codification of session-only constraints as durable facts.** Appears in:
   - 2026-04-21-stress-test-constraint-methodology (6-month deadline)
   - 2026-04-22-kay-is-operator-not-absent-buyer (premature frame mapping; charter tension)
   - 2026-04-21-traditional-search-peer-disclosure (charter content leaking to wrong audience)
   - 2026-04-21-niche-ranking-methodology-pivot ("fluff" = papered over thin data with confidence)
   - Count = 4
   - Current handling: `feedback_stress_test_constraints_not_facts.md` exists. Memory covers timelines/budgets/scope. Doesn't yet cover: framework-mapping (Athena Matchmaker), audience-leak (Charter to traditional searchers), confidence-language-on-thin-data ("fluff").
   - Suggested graduation: **Expand existing memory** `feedback_stress_test_constraints_not_facts.md` to include: (a) external-framework mapping requires premise-verification before applying; (b) durable codification requires explicit commitment language; (c) "fluff" pattern — analyses leaning on internal data known to be thin should be flagged as low-confidence in the output, not papered over.

3. **Schema/structural fix beats behavioral fix.** Appears in:
   - 2026-04-23-jj-col-u-overwrite-and-schema-migration (3 confident wrong recommendations before Kay's domain insight)
   - 2026-04-23-cadence-field-sole-source-of-truth (Lauren overdue 3 weeks because skill read text not field)
   - 2026-04-29-stagger-launchd-plists-collision (don't bump retries; fix the schedule)
   - 2026-04-19-onepager-guardrail-tool-level-not-memory (3+ corrections → tool-level hook)
   - Count = 4
   - Current handling: No single memory captures this meta-rule. `feedback_mutating_skill_hardening_pattern.md` and `feedback_launchd_parallel_fire_collisions.md` are domain-specific.
   - Suggested graduation: **New memory** `feedback_check_schema_before_recommending.md` — before recommending behavioral fixes (talk to JJ about pace, change cadence on contact, retry harder), verify the underlying data model can represent the metric being measured. Pattern tag from JJ trace explicit: `#pattern/check-schema-can-represent-question-before-analyzing-data`.

4. **Off-ramp / softening placement on outreach.** Appears in:
   - 2026-04-24-banker-first-reply-cut-buybox (cut buy-box when capital-fit mismatched)
   - 2026-04-24-offramp-attach-to-ask (off-ramp at smallest commitment, not whole relationship)
   - 2026-04-23-buy-box-paragraph-kay-authored (encoding implicit flexibility, not explicit naming)
   - Count = 3
   - Current handling: No memory exists. Pattern is encoded only in traces.
   - Suggested graduation: **New memory** `feedback_offramp_at_smallest_commitment.md`. Litmus: "Conditional language ('if it still makes sense for you', 'if useful') attaches to the smallest concrete ask in the email — meeting/intro/follow-up — never to the relationship overall." Pair with `pattern/disqualifier-skip-pitch` from the banker trace.

5. **Silence ≠ approval; calibration before bulk writes.** Appears in:
   - 2026-04-27-silent-approval-assumption (Motion triage — wrote 35 Work items without explicit yes)
   - 2026-04-20-calibrate-before-writes (river-guide cap check)
   - 2026-04-26-stale-snapshot-bulk-delete-bug (refresh state)
   - 2026-04-26-vip-filters-replaced-by-native-learning (don't push my model of importance over Kay's stated preference)
   - Count = 4
   - Current handling: `feedback_silent_approval_assumption.md`, `feedback_calibrate_before_bulk_writes.md`, `feedback_refresh_state_before_bulk_destructive.md`, `feedback_never_batch_changes_without_review.md` — all exist. Coverage is good, but the four memories overlap and the rules are not centralized.
   - Suggested graduation: **No new memory; consider stop hook** for Write/Edit on file paths matching `brain/context/session-decisions-*` or new tracker tabs — should require an explicit "approved" marker in the immediate prior turn. Or at minimum: add a **PreToolUse warning hook** that fires on multi-item batch writes (>3 entities in a single Edit/Write) and prompts agent to verify per-batch approval.

6. **Briefing structure migration with signal preservation.** Appears in:
   - 2026-04-25-decisions-only-briefing-emoji-tags (4-bucket → emoji tags)
   - 2026-04-19-briefing-architecture-shift-to-action-keyed-buckets (5-section → 4-bucket)
   - 2026-04-26-relationship-cadence-friday-only (Mon-Thu noise suppression)
   - Count = 3
   - Current handling: All memorized in `feedback_briefing_three_buckets`, `feedback_relationship_cadence_friday_only`, `feedback_decision_fatigue_minimization`, CLAUDE.md morning workflow.
   - Suggested graduation: **No graduation needed**, but `pipeline-manager` SKILL.md should be cross-checked to ensure the Friday-only cadence rule is enforced at skill-output-validation level (not just memory). Worth a stop-hook that blocks pipeline-manager output containing `🟢 *CRO*` items on Mon-Thu.

### Voice / communication patterns

- **Plain-text drafts only** — multiple traces (Hoffman, Vigna, Will Cotton acceptance) all show Kay rewriting drafts to strip explicit value-labeling, room-naming, and salesy closers. The "cheesy" callout is a recurring tell. Existing `feedback_drafts_no_blockquote`, `feedback_email_no_em_dashes`, `feedback_outreach_no_fake_lines` cover symptoms; the underlying principle is **understated warmth, no explicit self-evaluation of the situation**.
- **Audience-aware disclosure is load-bearing** — the WSN/Charter trace shows that even philosophically-correct content can leak strategic positioning. Voice rules need an audience-tier check, not just a topic check. Already partially codified in `feedback_no_search_fund_language_intermediaries.md` for intermediaries; the WSN traditional-searcher case needs a parallel memory.
- **First-person ("I am looking to acquire") beats institutional ("Greenwich & Barrow is acquiring")** for owner outreach — codified in buy-box trace, should propagate to all owner-facing copy. Conference-engagement skill snippets tab is locked correct; verify outreach-manager and DealsX templates match.
- **Conditional softening attaches to smallest ask, not to relationship.** New pattern not yet in memory.

### Decision-trace gaps

Categories underrepresented in the 69-trace corpus:
- **Email/draft iteration micro-edits** — most voice corrections happen inline ("change this line") and never become traces. The Hoffman/Vigna/Will Cotton traces are the exception. The `decision-traces` skill needs a litmus for catching voice-iteration-only sessions even when no explicit APPROVE/REJECT verb fires.
- **Silent skips** — when an agent decides NOT to surface something (e.g., suppressing a relationship-cadence Mon-Thu), the decision rarely produces a trace because nothing visible happened. Kay's "we had said you only remind on Fridays" surfaced this gap on 2026-04-26.
- **Repeated process violations** before they reach 3x correction threshold. The onepager hook trace establishes 3x as graduation criterion, but the count itself is implicit. **Recommend: add a small log file** `brain/traces/correction-counts/{pattern-slug}.md` that increments on each violation, so the 3x threshold is observable rather than memory-recalled.
- **Approval-gate verification** — how the system detects whether an artifact write was actually approved per-batch. The 2026-04-27 Motion triage error suggests this category needs more traces to find a structural fix (currently behavioral only).

### Agent-Kay alignment

Skipped this run. Validating 5 target list sheets against agent advances vs Kay overrides would have required >5 min and the patterns above are already strong from the trace corpus alone.

### Proposed changes (importance: critical|high|medium|low)

1. **[high]** Target: `memory/feedback_voice_lead_with_their_emphasis.md` (NEW)
   - Current: 3 separate voice memories cover symptoms (about-them, no-strategy-leaks, continue-dont-reintroduce). None capture the data-rich vs values-rich opener distinction.
   - Change: Create new memory with the Hoffman litmus + Heritage-Holding voice-match heuristic + buy-box first-person-voice rule. Cross-link from the 3 existing memories.
   - Why: Same correction across 5 traces in 1 week, recurring failure mode.
   - Source: 2026-04-29-lead-with-what-they-care-about, 2026-04-29-no-search-fund-language-intermediaries, 2026-04-23-buy-box-paragraph-kay-authored, 2026-04-23-seller-short-transition-matters, 2026-04-22-evening-event-override-will-cotton-studio.

2. **[high]** Target: `memory/feedback_check_schema_before_recommending.md` (NEW)
   - Current: No memory captures the meta-rule. Domain-specific memories exist for JJ schema and cadence-field-vs-text but the principle isn't generalized.
   - Change: Create memory codifying: before recommending a behavioral intervention based on data-pattern observation, verify the data model can represent the metric. Pattern tags from JJ + Lauren traces.
   - Why: 4 traces show confident-wrong recommendations from data-model blind spots. JJ trace explicitly cost 3 wrong analyses before unlock.
   - Source: 2026-04-23-jj-col-u-overwrite, 2026-04-23-cadence-field-sole-source-of-truth, 2026-04-29-stagger-launchd-plists-collision, 2026-04-19-onepager-guardrail-tool-level-not-memory.

3. **[medium]** Target: `memory/feedback_offramp_at_smallest_commitment.md` (NEW)
   - Current: No memory. Pattern only in 2 traces.
   - Change: New memory with off-ramp placement litmus. "Conditionals attach to the smallest concrete ask in the email, never to the relationship overall." Pair with `pattern/disqualifier-skip-pitch` for banker/lender contacts.
   - Why: Same correction across 3 outreach drafts in close succession. Will recur on every banker/lender first-reply.
   - Source: 2026-04-24-banker-first-reply-cut-buybox, 2026-04-24-offramp-attach-to-ask, 2026-04-23-buy-box-paragraph-kay-authored.

4. **[medium]** Target: `memory/feedback_stress_test_constraints_not_facts.md` (EXPAND)
   - Current: Covers session-only timelines/budgets/scope.
   - Change: Add subsections for (a) external-framework premise verification (Athena/Matchmaker case), (b) audience-aware-disclosure check before applying philosophical reframes to peer-group content (WSN/Charter case), (c) "fluff" tell — analyses on thin internal data must surface low confidence in output.
   - Why: 4 traces in 9 days show the same meta-pattern in different domains (timeline / framework / peer-content / data-confidence).
   - Source: 2026-04-21-stress-test-constraint-methodology, 2026-04-22-kay-is-operator-not-absent-buyer, 2026-04-21-traditional-search-peer-disclosure, 2026-04-21-niche-ranking-methodology-pivot.

5. **[medium]** Target: `pipeline-manager` SKILL.md + new stop hook in `.claude/hooks/router/handlers/relationship_cadence_friday_only.py` (NEW)
   - Current: Memory-only enforcement (`feedback_relationship_cadence_friday_only`). Documented violation from 4/17, 4/21, 4/24, 4/26.
   - Change: Stop hook that scans pipeline-manager / morning-briefing output. If date is Mon-Thu AND output contains relationship-cadence patterns (overdue contact, slipped follow-up on cadence, "🟢 *CRO*" items) → block with reason citing memory.
   - Why: Per `feedback_artifacts_pure_industry_analysis` precedent — 4 violations in 9 days = past the 3x graduation threshold. Memory alone hasn't held.
   - Source: 2026-04-26-relationship-cadence-friday-only (lists the 4 prior briefings that violated).

6. **[low]** Target: `decision-traces` skill SKILL.md
   - Current: Litmus is "would future agent make different choice without knowing this." Catches APPROVE/REJECT verbs but misses silent-skip decisions and voice-iteration micro-edits.
   - Change: Add second-pass scan for (a) sessions with 3+ draft iterations on the same artifact (voice calibration trace candidate), (b) suppression decisions where agent decided NOT to surface something Kay had previously asked to suppress.
   - Why: The 2026-04-26 Friday-only rule violation went undetected for 3 weeks because suppression-decisions don't trip the existing litmus.
   - Source: 2026-04-26-relationship-cadence-friday-only, the absent traces between 4/17–4/26 that should have caught this earlier.

7. **[low]** Target: New tracking file `brain/traces/correction-counts/{pattern-slug}.md` (NEW lightweight ledger)
   - Current: 3x-correction-graduation rule from `feedback_artifacts_pure_industry_analysis` is implicit. No explicit count.
   - Change: When a correction is repeated, append to a per-pattern ledger file. Calibration-workflow scans these weekly; ≥3 entries = graduate to hook.
   - Why: Without explicit counting, the 3x threshold relies on memory-recall by Claude — exactly the failure mode the rule is meant to fix.
   - Source: meta-pattern across `feedback_relationship_cadence_friday_only` (4 violations before catch), `feedback_artifacts_pure_industry_analysis` (3 before hook), `feedback_no_search_fund_language_intermediaries` (caught at 1 because the violation was prominent).

-> READY

---

## architecture-strategist findings

Sampled ~22 traces with structural keywords (architecture, source-of-truth, gap, protocol, migration, schema). Cross-checked against `.claude/skills/` (38 SKILL.md files), `.claude/hooks/router/handlers/` (24 handlers), CLAUDE.md, schemas/vault/ (10 files).

### Cross-trace patterns

- **Pattern A — Aspirational vs. running automation drift.** Skill specs claim "auto-trigger" or "auto-create" behavior that isn't actually wired end-to-end (no plist, no enforcement hook, no validator). Failures are silent because the agent only executes when in-session. Traces: `2026-04-15-pipeline-manager-outbound-scan-gap`, `2026-04-17-pipeline-manager-cim-trigger-gap`, `2026-04-29-stagger-launchd-plists-collision`, `2026-04-25-headless-prompt-as-wrapper-swap`, `2026-04-25-tech-debt-three-hour-scope-cut`. Root cause = `feedback_mutating_skill_hardening_pattern.md` exists but isn't enforced — `niche-intelligence` is still listed in CLAUDE.md as "expected to fail next Tuesday" until bead `ai-ops-5wx` ships. No automated audit confirms each scheduled mutating skill has plist + headless prompt + POST_RUN_CHECK validator + wrapper case.

- **Pattern B — Source-of-truth-per-question, not per-system.** Six traces in 6 weeks document the same class of bug: a global "always read X" rule misroutes when the operational question shifts. `2026-04-18-dealsx-sprint-source-of-truth` (sprint = Drive Verticals sheet, not tracker Col D), `2026-04-23-cadence-field-sole-source-of-truth` (cadence = Attio field only, not free text), `2026-04-23-jj-col-u-overwrite-and-schema-migration` (per-day dials require per-attempt columns, not "latest call date" snapshot), `2026-04-25-jj-call-log-tabs-via-sheets-api` (JJ activity = enumerate ALL Call Log tabs, not just working tab — undercounted by 98%), `2026-04-25-attio-engagement-signal-for-post-nda-split` (engagement = notes/checkbox proxy, not stage history), `2026-04-23-hold-calendar-prefix-no-brief` (confirmed meeting requires non-Kay attendees + non-HOLD title). CLAUDE.md `## Querying` lists source-of-truth by tool/path, not by question-type — agents fall back to first matching rule.

- **Pattern C — Rule placement: skill-file + hook outweighs memory + system-prompt.** Several rules with documented violation counts ≥2 are still memory-only and not protected by hooks: search-fund-language for intermediaries (`2026-04-29`), HOLD calendar prefix (`2026-04-23` — only in CLAUDE.md, not in pipeline-manager or meeting-brief-manager SKILL.md), Friday-only relationship surfacing (`2026-04-26` — "we had said," verbal rule decayed across 4/17, 4/21, 4/24, 4/26 briefings before durable codification). The `2026-04-19-onepager-guardrail-tool-level-not-memory` precedent established the "3x → graduate to hook" doctrine; it isn't being applied consistently.

- **Pattern D — Skill architecture: parent + typed templates beats sibling skills.** `2026-04-22-brief-skill-template-architecture` codified one parent + `templates/{mode}.md` + `examples/{mode}/`, no silent fallback. `2026-04-23-advisor-collapses-into-intermediary` reinforces "if email body is the same, bucket is the same." Doctrine partially applied: `meeting-brief/templates/` has 4 mode files, but `conference-engagement/templates/` still has only `email-templates.md` (one combined file) — needs splitting per the 3-bucket taxonomy already in SKILL.md.

- **Pattern E — Snapshot/state staleness on multi-step writes.** `2026-04-26-stale-snapshot-bulk-delete-bug` (deleted 2 freshly-created Gmail filters via stale snapshot), `2026-04-23-jj-col-u-overwrite` (subagent snapshot-first protocol), `2026-04-15-pipeline-manager-outbound-scan` (Attio Person ≠ list-entry coverage). CLAUDE.md "Before writing to a Google Sheet" pre-flight covers Sheets but not Gmail filter deletes or Attio batch ops. `feedback_refresh_state_before_bulk_destructive.md` is memory-only — same Pattern C decay risk.

- **Pattern F — Closing-loop sync gap when downstream record is created out-of-band.** `2026-04-24-vault-attio-sync-option-b`: vault entity created at card-collection time, Attio Person auto-created later by email send. Without a daily sync that bridges these, engagement notes never land in Attio. Same shape as Pattern A's "skill specs aspirational" — the Option-B daily sync was specced into relationship-manager but needs verification it actually runs.

### Proposed changes

1. **[critical]** Target: `.claude/skills/niche-intelligence/` — add `headless-tuesday-prompt.md` + validator + wrapper case
   - Current: CLAUDE.md scheduled-skills table marks the Tuesday 22:30 fire as "expected to fail next Tuesday too" until bead `ai-ops-5wx` ships. Mutating skill (writes one-pagers + scorecards + tracker WEEKLY REVIEW). Currently routes through bare `/niche-intelligence` slash command — exactly the failure mode `2026-04-25-headless-prompt-as-wrapper-swap` documented.
   - Change: Author `.claude/skills/niche-intelligence/headless-tuesday-prompt.md` (imperative runbook, no clarifying questions, artifact-first). Author `scripts/validate_niche_intelligence_integrity.py` (verify N one-pagers landed in `brain/outputs/`, scorecard rows have required columns, WEEKLY REVIEW row count grew). Add wrapper case in `scripts/run-skill.sh` for `niche-intelligence:tuesday`. Update plist with `POST_RUN_CHECK` env var.
   - Why: Only mutating scheduled skill not yet hardened per `feedback_mutating_skill_hardening_pattern.md`. Doctrine exists, work is identified, bead is open. Highest-blast-radius open hole — fails every Tuesday silently.
   - Source: `2026-04-29-stagger-launchd-plists-collision`, `2026-04-25-headless-prompt-as-wrapper-swap`, CLAUDE.md scheduled-skills row.

2. **[critical]** Target: `.claude/hooks/router/handlers/no_search_fund_language.py` (new hook)
   - Current: `feedback_no_search_fund_language_intermediaries.md` is memory-only. Brand-floor violation per `feedback_brand_floor_vs_voice_preference`. No hook exists (grep confirmed).
   - Change: PreToolUse hook on Write/Edit/MultiEdit when target path matches `brain/outputs/**/intermediary*.md`, `.claude/skills/**/templates/intermediary.md`, or any draft to recipient with email domain on a known broker/IB/lender list. Block on patterns: `search\s+fund`, `search\s+vehicle`, `committed\s+equity`, `\bETA\b`, `24-month\s+(acquisition\s+)?window`. Mirror `onepager_guardrail.py` shape — strip frontmatter + wiki-links before pattern match.
   - Why: Per `2026-04-19-onepager-guardrail-tool-level-not-memory` graduation rule, brand-floor violations on outreach copy belong at tool level. Asymmetric stigma is documented; recipient class is bounded; pattern is mechanically detectable.
   - Source: `2026-04-29-no-search-fund-language-intermediaries`, `2026-04-19-onepager-guardrail-tool-level-not-memory`.

3. **[high]** Target: `.claude/skills/conference-engagement/templates/`
   - Current: One combined `email-templates.md`. SKILL.md lines 44-48 describe a 3-bucket taxonomy and explicitly forbid a 4th "advisor" bucket.
   - Change: Split into `templates/intermediary.md`, `templates/owner.md`, `templates/peer.md`. Mirror to G&B MASTER TEMPLATES Drive folder per `pattern/templates-mirrored-to-drive`. Update SKILL.md to require `{audience}` arg and load matching template + `examples/{audience}/` folder. Error if audience not provided — no silent fallback.
   - Why: `2026-04-22-brief-skill-template-architecture` doctrine extends to outreach skills. Combined templates create the "wrong-tone output" failure that meeting-brief refactor solved. 3-bucket taxonomy is settled per `2026-04-23-advisor-collapses-into-intermediary`.
   - Source: `2026-04-22-brief-skill-template-architecture`, `2026-04-23-advisor-collapses-into-intermediary`.

4. **[high]** Target: `CLAUDE.md` § Querying — add "Source of truth by question type" lookup
   - Current: Source-of-truth listed by data system (Beads / Obsidian / Sheets / Drive), not by operational question.
   - Change: Add a per-question lookup table directly under the existing Source of Truth bullets:
     - "What is DealsX building this sprint?" → DealsX Verticals Drive sheet (`1n5zMVL4...`), NOT tracker Col D.
     - "What did JJ actually dial today?" → enumerate all `Call Log M.DD.YY` tabs via Sheets API, group by per-attempt date columns (T or V). NEVER tab name. NEVER working tab alone.
     - "Is this contact overdue?" → Attio `nurture_cadence` field. NEVER `next_action` text.
     - "Did this deal reach NDA?" → Attio `meaningful_conversation` checkbox or notes attached (engagement-signal proxy). NOT stage history (Attio doesn't expose it).
     - "Is tomorrow's meeting confirmed?" → calendar attendees ≠ {Kay only} AND title doesn't start with `HOLD `.
     - "What did partner X actually do?" → the artifact partner X is working from (their Drive sheet, their call log). Not Kay's strategy state.
   - Why: Six traces in 6 weeks on the same Pattern B failure. A lookup table beats per-skill reminders that get compacted out.
   - Source: `2026-04-18-dealsx-sprint-source-of-truth`, `2026-04-23-cadence-field-sole-source-of-truth`, `2026-04-23-jj-col-u-overwrite-and-schema-migration`, `2026-04-25-jj-call-log-tabs-via-sheets-api`, `2026-04-25-attio-engagement-signal-for-post-nda-split`, `2026-04-23-hold-calendar-prefix-no-brief`.

5. **[high]** Target: `.claude/skills/pipeline-manager/SKILL.md` + `.claude/skills/meeting-brief-manager/SKILL.md` (HOLD-prefix gate)
   - Current: HOLD-calendar-prefix rule lives only in CLAUDE.md morning-workflow brief-decisions pre-flight. pipeline-manager line 190 says "Brief needed for tomorrow's meetings → 🔴 Decision" without referencing the HOLD gate. `grep HOLD` against `.claude/skills/` returns zero hits in either skill.
   - Change: Add HOLD-prefix-skip logic to both skills' calendar-scan sections: "If event title starts with `HOLD ` (case-insensitive) AND attendees == {Kay only}, treat as unconfirmed. Skip brief generation. Surface only as soft-nudge decision if Kay should chase counterparty."
   - Why: CLAUDE.md gets compacted under context pressure; skill files reload on invocation. Belt-and-suspenders against Pattern A/C decay.
   - Source: `2026-04-23-hold-calendar-prefix-no-brief`.

6. **[high]** Target: `.claude/skills/pipeline-manager/SKILL.md` (Friday-only briefing surface filter)
   - Current: `feedback_relationship_cadence_friday_only.md` is memory-only. CLAUDE.md mentions weekly cadence but Mon-Thu suppression isn't a skill-level invariant. Violations recurred across 4/17, 4/21, 4/24, 4/26 before durable codification.
   - Change: Add a "Briefing Surface Filters" section: "Mon-Thu — omit relationship-cadence/nurture/dropped-balls items entirely. Active-deal cadence (NDA awaiting reply, financials chase, post-LOI) stays daily. Friday — full surfacing." Reference the trace + memory.
   - Why: Verbal-rule decay confirmed across 4 briefings. The skill assembling the briefing must own the filter, not the agent's recall.
   - Source: `2026-04-26-relationship-cadence-friday-only`.

7. **[medium]** Target: New `scripts/audit_scheduled_skills.py` + fold into health-monitor's Friday 12:30 AM ET fire
   - Current: No automated check that each scheduled mutating skill has full triple wired. Status documented prose-style in CLAUDE.md.
   - Change: Author script that, for each plist in `~/Library/LaunchAgents/com.greenwich-barrow.*.plist` flagged as mutating, verifies (a) wrapper case in `scripts/run-skill.sh`, (b) `.claude/skills/{skill}/headless-{mode}-prompt.md` exists, (c) `scripts/validate_{skill}_integrity.py` exists, (d) plist has `POST_RUN_CHECK` env var. Output Slack summary on Friday morning briefing.
   - Why: Pattern A's root cause is no inventory check. Claims live in CLAUDE.md prose and drift. Automated audit makes the gap visible.
   - Source: `2026-04-17-pipeline-manager-cim-trigger-gap`, `2026-04-29-stagger-launchd-plists-collision`, `2026-04-25-tech-debt-three-hour-scope-cut`.

8. **[medium]** Target: `CLAUDE.md` § Pre-Flight Checklists — add "Before bulk-destructive op (Gmail filter / Attio batch / Sheet rows)"
   - Current: Existing pre-flight covers "Before writing to a Google Sheet" only. `feedback_refresh_state_before_bulk_destructive.md` is memory-only.
   - Change: Add new pre-flight: "Re-fetch live state immediately before any bulk-destructive op. Any snapshot taken earlier in the same session is invalid if any mutation has occurred since. Snapshot pre-write state to `/tmp/{op}-snapshot.json` for rollback."
   - Why: Self-inflicted bug `2026-04-26-stale-snapshot-bulk-delete-bug` deleted 2 freshly-created filters silently. Pre-flight position (loads into system prompt) outweighs memory file.
   - Source: `2026-04-26-stale-snapshot-bulk-delete-bug`, `2026-04-23-jj-col-u-overwrite-and-schema-migration`.

9. **[medium]** Target: `.claude/skills/relationship-manager/SKILL.md` (verify Vault→Attio engagement-note morning sync runs)
   - Current: Skill scans cadence/overdue but the Option-B sync from `2026-04-24-vault-attio-sync-option-b` may not be wired into the daily run. Closing-loop gap from Pattern F.
   - Change: Verify (then add if missing) a daily step: scan `brain/entities/` for entities created in last 7 days with empty `attio_id`. For each, query Attio by email; if Person now exists, attach idempotent note titled `"{source} {date} — engagement context"`, set source/cadence. Surface "missing Attio scope" as Decision item (don't bury in System Status).
   - Why: Without daily landing-zone, deferred writes silently never close. Skill exists, daily fire exists; one-step extension.
   - Source: `2026-04-24-vault-attio-sync-option-b`.

10. **[low]** Target: `.claude/skills/jj-operations/SKILL.md` — document Sheets-API tab enumeration pattern
    - Current: SKILL.md was updated 4/23 to reference 6-col schema and "harvest reads across all weekly tabs," but doesn't document the OAuth-refresh-token + Sheets-API enumeration pattern from `2026-04-25-jj-call-log-tabs-via-sheets-api`.
    - Change: Add a "Tab enumeration via Sheets API" subsection pointing to `scripts/refresh-jj-snapshot.sh` and the regex `^Call Log\s+\d+[./]\d+[./]\d+$` for tab matching.
    - Why: Pattern is reusable for any multi-tab Sheets data source. Without explicit doc, next implementer re-discovers.
    - Source: `2026-04-25-jj-call-log-tabs-via-sheets-api`.

-> READY

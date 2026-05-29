---
schema_version: 1.0.0
date: 2026-05-28
task: Calibration analysis of 169 unreviewed traces (2026-04-10 to 2026-05-28) + Thursday meta-calibration
agents: [coordinator, architecture-strategist, simplicity-advocate, pattern-recognizer]
status: active
---

# Agent Chatroom: Calibration Analysis (2026-05-28)

## Coordination Log

### simplicity-advocate findings

MEMORY.md = 225 lines / ~68KB, over the ~200-line guidance. Confirmed duplicates and stale files below. Conservative on deletes — proposed MERGE where unsure.

**CONFIRMED EXACT DUPLICATES (DELETE one):**
1. `feedback_same_surface_nested_view.md` + `feedback_dashboard_same_surface_nested.md` — same dashboard nesting principle, both 2026-05-01 from same M&A Analytics/Activity merge. MERGE → keep `feedback_dashboard_same_surface_nested.md` (richer "how to apply" + impl paths + trace link), DELETE `feedback_same_surface_nested_view.md`. Collapse MEMORY.md line 152 to one ref. Neither load-bearing.

**STALE / SUPERSEDED (DELETE — describe sunset workflow):**
2. `feedback_morning_briefing_format.md` + `feedback_morning_briefing_categories.md` — BOTH describe the OLD 5-section briefing (Superhuman drafts, Motion steps, "Pipeline shifts") explicitly migrated 2026-04-25 to Decisions-only single-list. Reference sunset tools (Superhuman 4/29, Motion lapsing). Superseded by `feedback_briefing_three_buckets.md` + `feedback_decision_fatigue_minimization.md` + CLAUDE.md Morning Workflow. DELETE both; drop from MEMORY.md line 106. Not load-bearing.

**MERGE (4→1, all have real firing cases — not deletes):**
3. Conversation-discipline question-stacking cluster: `feedback_no_opposite_questions.md` + `feedback_no_counter_in_question.md` + `feedback_questions_one_at_a_time.md` + `feedback_single_yes_no_per_recommend.md` — all four = "one single-direction YES/NO at a time, never stack alternatives/caveats." MERGE into one `feedback_one_question_one_default.md`. Collapses 4 line-77 refs to 1.

**'fund' language pair — KEEP BOTH (distinct scope):**
4. `feedback_never_say_fund.md` (G&B-as-fund label) + `feedback_never_say_fund_or_lead.md` (Kay-as-PE + "I lead" framing). Overlap ~50% but the second adds the "I lead"/Brella-profile rules. Optional light MERGE into `feedback_never_say_fund_or_lead.md`; LOW priority.

**NEW UNCOMMITTED FILES — all clean, NOT duplicates:**
- `feedback_gog_drive_replace_equals_syntax.md` — genuine distinct bug memory (already in MEMORY.md L91). Keep.
- `feedback_jj_10am_slack_monday_only.md` — distinct from `feedback_jj_operations_review_mondays_only.md` (already in MEMORY.md L62). Keep.
- `feedback_no_direct_task_writes_from_skills.md` — NOT yet in MEMORY.md. ACTION: add one-line ref under Pipeline Hygiene cluster. Distinct rule (skills stage tasks, never write TO DO directly). Keep + index.

**TRIM MEMORY.md:** women_network_priority (L66) is NOT stale — supersession note says BOTH active; leave. Real trims = remove deleted files (#1, #2), collapse merged cluster (#3). Net ~6 lines + size reduction.

-> READY

### pattern-recognizer findings

Scanned all 169 traces (index + targeted reads) + 30 hooks across `.claude/hooks/router/handlers/`. Three live findings, one near-miss, one meta-diagnosis. Most CLAUDE.md-cited "recurring failures" are ALREADY hooked — credential op:// (`op_first_guard`), gog delimiter (`gog_sheets_delimiter_guard`), stale-template-read (`canonical_template_guard`), secrets (`secret_file_guard`), Sunday-send (`no_sunday_send_recommendations`), one-pager purity (`onepager_guardrail`), no-revenue (`no_revenue_in_outreach`), no-Kay-in-deliverables (`no_kay_in_deliverables`), verb-log traces (`trace_litmus_guard`). Calibration is mature on enforcement. The real rot is in the calibration PROCESS itself.

**META-DIAGNOSIS (the headline):** Of 169 traces, exactly **1 carries `review_status`**. The calibration-workflow SKILL.md explicitly says (L428-429) "Mark applied traces as applied / Mark skipped traces as skipped" and the helper `list-unreviewed-traces.py` filters on that field. So 4 prior calibrations consumed traces, applied a subset, and NEVER wrote the field back — making every prior-reviewed trace look unreviewed forever. The backlog is an accounting artifact, not 169 genuinely-unprocessed decisions. **Smallest fix: the calibration close-out MUST stamp `review_status: applied|skipped` on every trace it touched, and the move-to-`processed/` step (SKILL.md L410) must actually run. Add a calibration-stop hook OR a post-run validator that fails if any trace in the processed batch lacks `review_status`.** Without this, the next calibration re-faces 169+.

**NOISE: 33/169 (20%) are task-tracker CRUD receipts** (`schedule-to-day-slot`, `promote`, `append`, `build-week`, `distribute`, `reformat`, `sync`), dated 05-02 → 05-28. The `trace_litmus_guard` (built 2026-05-21 for exactly this) WOULD block 26 of them (they carry `verb/` tags, ≤15 lines, no Decisions heading) — but they predate the guard. Forward-going is fixed; backlog needs a ONE-TIME sweep: move all 33 to `brain/context/verb-logs/` or stamp `review_status: skipped`. The 05-22/05-28 ones slipping past the guard means task-tracker-manager is still emitting them through a path the guard doesn't intercept (likely subagent Write not routed through PreToolUse) — worth a 2-min check.

**GRADUATION CANDIDATE (clean 2+): strategic-threshold grounding.** `feedback_strategic_thresholds_need_grounding` — MEMORY.md itself flags "4 instances in 4 days 2026-05-01→05-04." Trace 2026-05-03 ($1M EBITDA floor guess) is the canonical firing. It has memory + a CLAUDE.md pre-flight line but NO hook — and it's un-hookable cleanly (no deterministic signal for "this number lacks a constraint chain"). Verdict: NOT a hook candidate; it's a reasoning-discipline rule that belongs where it is. Recommend leaving in memory + CLAUDE.md, mark traces applied. Flagging so the meta-calibration doesn't waste a hook-build cycle chasing it.

**NEAR-MISS (1 firing, watch): refresh-state-before-bulk-destructive.** Trace 2026-04-26 (deleted 2 freshly-created auto/* filters off a stale label snapshot). Has `feedback_refresh_state_before_bulk_destructive` memory + CLAUDE.md line, no hook. Single firing → below the 2+ graduation bar. If it fires again, it IS hookable (PreToolUse on bulk-delete gog calls → require a re-fetch in same session). Park for now.

**VOICE CALIBRATION: insufficient data.** Only 2 traces match voice/draft-calibration patterns and 1 is a mislabel (`task-tracker-append-call-gusto`). Real voice trace = `2026-05-04-day-5-voice-no-soft-signal-stacking` (already → `feedback_no_soft_signal_stacking`, in MEMORY.md). 6 traces mention "voice" but as topic tags on doctrine traces, not diff sets. No ≥10-diff corpus exists. Report: insufficient data, 1 genuine voice diff found. No new voice rules proposable this run.

**AGENT-KAY ALIGNMENT: not assessed this run** (requires live target-list sheet read; out of scope for trace-only analysis).

-> READY

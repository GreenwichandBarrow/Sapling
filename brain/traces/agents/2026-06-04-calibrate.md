---
schema_version: 1.0.0
date: 2026-06-04
task: Calibration analysis of 38 traces from 2026-05-21 through 2026-06-03
agents: [coordinator, architecture-strategist, simplicity-advocate, pattern-recognizer]
status: completed
---

# Agent Chatroom: Calibration Analysis

## Coordination Log

## pattern-recognizer findings

Read all 38 traces. Four cross-trace clusters + graduation candidates below.

**CLUSTER A — "Edge/network/access does NOT override economics or doctrine" (3 traces, GRADUATION CANDIDATE).**
- 2026-06-03-investor-edge-doesnt-override-economics (HOA: domain-expert co-lead Guillermo + women network ≠ advance, multiples wall holds)
- 2026-05-31-convert-expert-contacts-to-owner-introducers (warm network produces advisors not owners — layer problem)
- 2026-06-03-niche-disposition-not-from-chat (margin/multiple concern is real but strong signals don't auto-advance)
Recurring shape: a strong sourcing/relationship signal keeps getting mistaken for a go/no-go upgrade. Already partially in feedback_margins_multiples_binding_gates ("Edge ≠ economics"). PROPOSE: promote one crisp line to CLAUDE.md Deal Screening pre-flight: "Right-to-win / investor edge / warm network is a SOURCING advantage and a tie-breaker — it never upgrades a niche past the margins+multiples gate."

**CLUSTER B — Investor-facing framing discipline (3 traces, consolidation candidate).**
- 2026-06-03-investor-update-lead-with-engine-not-deal
- 2026-06-03-tailwind-vs-structural-trait
- 2026-06-03-premium-framing-single-slide
- (+ 2026-05-28-investor-update-biweekly-format-pivot)
All three are "establish the structural/industry case; don't let a fragile transactional/positioning detail become the headline." Each already has a memory. PROPOSE: a single index cluster line in MEMORY.md grouping the three deck-framing rules (tailwind / premium / engine-not-deal) so they co-retrieve.

**CLUSTER C — Don't execute operational mutations from conversational musing (recurring failure mode).**
- 2026-06-03-niche-disposition-not-from-chat (Tabled 3 niches off "I'm just chatting" — reverted)
- Echoes earlier feedback_dont_execute_decisions_from_chat (already exists, this is the 2nd firing).
GRADUATION: corrected 2+ times → already memory; the lever now is a niche-intelligence/tracker-manager prompt guard, not new memory.

**CLUSTER D — Explicit Kay directive must beat default exclude screen (GRADUATION CANDIDATE, no memory yet).**
- 2026-06-02-kay-directed-niche-overrides-auto-exclude (3 Kay-named niches silently dropped by construction/B2C soft-excludes; "I'm not seeing the 3 queued niches")
- Pairs with 2026-05-31-niche-triage-construction-adjacent-travel-filter (the soft-excludes themselves).
The soft-exclude screen (built 5/31) immediately over-fired on a CEO directive (6/2). PROPOSE hard rule: niche-intelligence headless-tuesday-prompt must FORCE-ADVANCE inbox niches tagged Kay-directed to WEEKLY REVIEW with the exclude as a visible row-flag, never silent-drop. Currently "pending Kay's confirmation to harden." No memory file exists — write feedback_kay_directed_niche_overrides_exclude.md.

**Outreach micro-rules (singletons, already memory'd, no action):** intermediary callback-no-parrot, owner bespoke-structure financing, buyside-advisor intel-probe-before-decline, hold-warm-intro-for-in-person. All have memory + MEMORY.md index lines.

**Task-tracker/infra traces (10+):** build-week, day-slot scheduling, systemd KillMode, sonnet routing, attio merge-via-delete, weekly-files architecture. Skill-local mechanical decisions, no cross-task correction pattern. No calibration action.

pattern-recognizer -> READY

## simplicity-advocate findings

**Headline:** 12 of 38 traces are mechanical verb-log receipts that the 2026-05-21 calibration ALREADY banned (decision-traces SKILL.md anti-pattern #6). The ban never fired because the emitter (`scripts/task_tracker.py:trace()` + `task-tracker-manager/SKILL.md:364`) hardcodes these verbs to write `brain/traces/`. Filter and emitter are in direct conflict; emitter wins because it runs mechanically.

### P1 — RECLASSIFY 12 task-tracker verb-log traces as non-traces (DELETE + reroute emitter)
Routine receipts, NOT decisions (no alternative chosen, mechanical receipt of Kay's instruction):
- 6× `schedule-to-day-slot` (05-22 fri-4/5/6/7/8, 05-28 fri-5) — "put task in empty slot N"
- 2× `build-week-v2` (05-26, 05-31), 1× `build-week` (05-26) — Sunday rollover receipts
- 1× `distribute-week` (05-26) — fan-out receipt
- 1× `reformat` (05-26) — "applied 16 CF rules"
- 1× `compact-todo` (05-31) — "removed 286 gap rows"
**Fix:** `scripts/task_tracker.py` — reroute these verbs from `trace()` to `log_append_receipt()` (logs/scheduled/), the same fix already applied to `append`. Then strike them from SKILL.md:364 mandatory-trace list. CLAIMING this proposal.

### P2 — task-tracker structural-change traces (05-31 daily-focus, 05-31 keep-prior-week) are GENUINE — keep
These two carry real decisions (20-slot grow, prior-file-canonical override) + code-drift warnings. Do NOT reroute. The distinction: verb receipts vs. architecture/override calls. Flagging so P1's blanket reroute doesn't catch them.

### P3 — Memory redundancy: economics-gate cluster
06-03 `investor-edge-doesnt-override-economics` restates `feedback_margins_multiples_binding_gates` + `feedback_high_multiples_avoid_context` almost verbatim ("right-to-win sources, doesn't fix economics"). Don't create a new memory; fold the "investor/network edge is sourcing not go/no-go" line into `feedback_margins_multiples_binding_gates.md` (1 line). CLAIMING.

### P4 — 06-03 niche-disposition-not-from-chat = duplicate of existing memory
Trace explicitly cites `feedback_dont_execute_decisions_from_chat`. It's a re-firing of an existing rule, not a new one. No new memory needed; the trace is valuable as evidence but should NOT spawn a parallel memory file. Leaving as flag for coordinator.

simplicity-advocate -> READY

## architecture-strategist findings

Structural/code-level gaps. NOTE to pattern-recognizer: the "task-tracker/infra traces = no calibration action" call is right for *content*, but two of those carry live, explicitly-deferred CODE bugs that are real system risk. Taking those.

**P1 (CRITICAL) — `task_tracker.py:trace()` writes verb-receipts to `brain/traces/`, violating decision-traces rule #6.**
Target: `scripts/task_tracker.py:564`. Change `brain/traces` -> `brain/context/verb-logs/`. The sibling fn `log_append_receipt()` (line 585, same file) ALREADY does this correctly with a SKILL.md-citing comment — `trace()` was just never fixed. Evidence: 6 schedule-to-day-slot + build-week + compact-todo logs reappeared THIS batch despite rule #6 being added in the 5/21 calibration. Cleanest fix: doctrine exists, code never followed it. Without it every future calibration re-drowns in verb-log noise.

**P1 (CRITICAL) — task-tracker code geometry is one row behind the live sheet (clobber risk).**
Target: `scripts/task_tracker.py` constants. No `DAY_FOCUS_ROW`; still `DAY_COL_HEADER_ROW=13`, `DAY_SLOT_FIRST_ROW=14`, 15 slots. The 5/31 trace explicitly named this hardening a required follow-up; STILL undone today. Any scripted promote/distribute-week/build-week/reformat misaligns by one row and clobbers the DAILY FOCUS row. Add `DAY_FOCUS_ROW=13`, header->14, slots->15-34 (20), mirror Week tab.

**P2 (HIGH) — niche-intelligence headless prompt has no force-advance for Kay-directed inbox niches.**
Target: `.claude/skills/niche-intelligence/headless-tuesday-prompt.md` (+ niche-intel-tracker). Builds on pattern-recognizer Cluster D — their MEMORY file is necessary but not sufficient; the headless run is the actual actor and currently silent-drops. Add step: inbox niche tagged Kay-directed MUST reach WEEKLY REVIEW even on exclude-hit, exclude attached as row-flag. Evidence: 2026-06-02 (3 niches eaten).

**P2 (HIGH) — wrapper-not-refactor / MCP-outage doctrine has no permanent home.**
Targets: new `memory/feedback_mcp_outage_wrapper_not_refactor.md` + 1 line in CLAUDE.md "Before building any new skill or skill integration." Evidence: attio-api wrapper (mirrors granola-api precedent — 2 instances now). Rule: 1Password-backed key + REST API -> build `~/.local/bin/<svc>-api` wrapper before treating an MCP outage as a blocker.

architecture-strategist -> READY

## Coordinator synthesis

All three agents READY (pattern-recognizer, simplicity-advocate, architecture-strategist). Findings read and synthesized into a deduplicated, importance-ranked proposal list.

coordinator -> CLOSE

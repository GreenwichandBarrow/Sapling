---
schema_version: 1.0.0
date: 2026-06-04
type: output
output_type: calibration
status: applied
title: "Calibration — 2026-06-04 (38 new traces 05-21→06-03 + 153-trace backlog reconcile)"
tags: ["date/2026-06-04", "output", "output/calibration", "status/applied", "topic/calibration"]
---

# Calibration Report — 2026-06-04

**Traces analyzed (deep):** 38 new (2026-05-21 → 06-03)
**Backlog reconciled:** 153 old (2026-04-10 → 05-20) → 152 already graduated to memory, 1 genuine gap
**Total traces reviewed this run:** 191 (190 marked applied, 1 skipped pending Kay)
**Agents:** architecture-strategist · simplicity-advocate · pattern-recognizer (coordinator synthesized) + reconciliation agent
**Proposals:** 9 — 3 critical, 3 high, 2 medium, 1 low. Applied 7-item bundle; held 1 (C3, clobber risk).

## Cross-cutting observation

All three analysis agents independently converged on one root cause: `scripts/task_tracker.py:trace()` dumps mechanical verb-receipts into `brain/traces/`, violating an anti-pattern the **2026-05-21 calibration already wrote** (decision-traces SKILL.md #6). 12 of the 38 new traces (32%) were that self-inflicted noise. The doctrine existed; the emitter never followed it, so it won mechanically every week. This was the highest-leverage fix — it removes ~32% of future calibration noise at the source.

The backlog confirms the system is otherwise healthy: 152 of 153 old traces had already graduated to memory/CLAUDE.md/skills — the "191 unreviewed" number was a marking-hygiene artifact (weekly calibration hadn't fired since 5/21), not 191 unincorporated learnings.

## Applied changes (7-item bundle)

### CRITICAL
1. **`scripts/task_tracker.py`** — Added `_RECEIPT_VERBS` + `log_verb_receipt()`. Receipt verbs (`compact-todo`, `schedule-to-day-slot`, `build-week`, `build-week-v2`, `distribute-week`, `reformat`) now route their rollback record to `brain/context/verb-logs/{date}-task-tracker.log` instead of `brain/traces/`. Decision verbs (`promote`, `move-day-item`, `recurring-*`, `projects-create-gantt`, `sync-done-status`) still trace. Compiles clean.
2. **`.claude/skills/task-tracker-manager/SKILL.md`** §4 + Output expectations — Struck receipt verbs from the mandatory-trace list to match the code; documents the verb-logs routing. (Code + spec changed together so they don't re-diverge.)

### HIGH
3. **`.claude/skills/niche-intelligence/headless-tuesday-prompt.md`** — Added Kay-directed override: an inbox niche Kay explicitly names/queues MUST force-advance to WEEKLY REVIEW even on a soft-exclude hit, with the exclude shown as a visible flag (never silent-drop); hard regulatory kill still kills. Also folded in the disposition-discipline guard (no status moves from conversational musing).
4. **NEW `memory/feedback_kay_directed_niche_overrides_exclude.md`** — Doctrine for #3. + MEMORY.md index line.
5. **NEW `memory/feedback_mcp_outage_wrapper_not_refactor.md`** — MCP down + 1Password key + REST API → build `~/.local/bin/<svc>-api` wrapper before treating it as a blocker (granola-api + attio-api precedent). + MEMORY.md cluster line. (CLAUDE.md line intentionally skipped to keep root lean.)

### MEDIUM
6. **`memory/feedback_margins_multiples_binding_gates.md`** — Sharpened the existing "Edge ≠ economics" line: edge/co-lead/warm-network is a sourcing + tie-break advantage, **never a go/no-go upgrade**, and never substitutes for a formal disposition. Linked the 3-trace cluster (HOA, expert-contacts, niche-disposition).
7. **`MEMORY.md`** — Added an investor-deck-framing co-retrieval cluster line (tailwind / engine-not-deal / premium=1-slide fire together on any investor/CIM deck).

### LOW (folded into #3)
8. Niche-disposition-from-chat guard — already in `feedback_dont_execute_decisions_from_chat`; added as a prompt guard in the niche-intelligence headless prompt rather than a new memory.

## Held for verification (NOT applied)

- **C3 (critical) — `scripts/task_tracker.py` day-grid geometry.** Constants are one row behind the live sheet: no `DAY_FOCUS_ROW`, still 15 slots at row 14, while the 2026-05-31 trace says the live file added a DAILY FOCUS row at 13 and grew to 20 slots. **Real bug — any scripted `promote`/`distribute-week`/`build-week`/`reformat` misaligns by one row and could clobber the DAILY FOCUS row.** Held because editing geometry constants blind carries clobber risk; needs a live-sheet read to confirm the exact layout before changing `DAY_FOCUS_ROW`/slot count. Recommend a follow-up bead.

## Reconciliation gap (1) — surfaced for Kay's keep/drop

- **`2026-04-19-reality-check-aggressive-timelines`** (marked `skipped`, not archived). Orphaned learning: cold→LOI timeline tiers (cold 3–6mo / warm 4–8wk / active 2–4wk) + the behavioral rule "reality-check an aspirational CEO timeline with structural math before committing; don't match energy with false commitments." `project_search_fund_benchmarks` has adjacent LOI cadence data but not these tiers or the behavioral rule. Surfaced rather than auto-adopted because it shapes how Claude pushes back on Kay's stated timelines — **Kay decides: graduate to a memory, or drop.**

## Dropped / non-proposals

- 10+ task-tracker/infra mechanical traces (systemd KillMode, sonnet routing, attio merge-via-delete, weekly-files architecture): skill-local, no cross-task correction pattern. Their *emission* into brain/traces was the critical bug; their *content* warrants no calibration.
- New parallel memory for niche-disposition-from-chat: rejected — it's a 2nd firing of an existing rule, not a new one.
- New standalone economics-gate memory: rejected — folded into the existing `feedback_margins_multiples_binding_gates` (1-line sharpen) to avoid a 3rd near-duplicate.

## Thursday meta-calibration buckets (note)

This was a manual Thursday run focused on the core trace calibration + backlog clear. The 6 Thursday buckets (rule graduation, memory consolidation, skill-doc refresh, open-loop promotion, learnings promotion, freshness audit) were partially exercised inline: rule graduation (#1/#2 code+doctrine, #3 Kay-directed), memory consolidation (#6 fold, dropped duplicates). Bucket 5 (skill `learnings.md` → evolve) and bucket 6 (freshness audit) not run — recommend folding into tomorrow's automated Friday run or a dedicated pass.

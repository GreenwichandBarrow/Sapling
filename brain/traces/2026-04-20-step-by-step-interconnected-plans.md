---
schema_version: 1.1.0
date: 2026-04-20
type: trace
title: "Step-by-step on interconnected plans — don't bundle forward"
had_human_override: true
importance: critical
target: "claude-md, process"
tags: ["date/2026-04-20", "trace", "topic/process", "topic/orchestration", "pattern/sequence-over-parallel"]
---

# Step-by-Step Execution on Interconnected Plans

## Context

Full-day arc of scope drift: river-guide-builder was planned in phases with Phase 2 explicitly scheduled "after Apollo enrichment + Attio MCP." I argued Phase 2 was "technically unblocked" on a narrow axis (doesn't need Apollo employment-history data) and ran it with 8 parallel subagents. Attio MCP turned out to be unavailable too — so Phase 2 ran in 4-of-5 source mode, producing 291 rows of low-quality warm-intro data. Kay then had to clear all 291 rows. Same pattern repeated on schema iteration (13-col → 8-col → 7-col) because I drafted before confirming intent.

## Decisions

### Sequencing rule for multi-step plans
**AI proposed:** Execute unblocked steps in parallel when dependencies allow. "Phase 2 doesn't need Apollo, so run it while we wait."

**Chosen:** **No parallel pulling-forward unless Kay explicitly green-lights the bundle.** For interconnected plans: step → present output → Kay confirms → next step. Even when a later step looks technically unblocked on one axis, downstream reality (other missing dependencies, intent drift) breaks the shortcut.

**Reasoning:** Kay's words: "these exact moments are why we need to go step by step when rolling out a new plan that has interconnected processes and steps."

The specific failure modes today:
1. **Bundled Phase 2 into Associations-only ship** → had to clear 291 rows
2. **Proposed River Guides schema three times** (13→8→7 cols) because drafted before confirming intent
3. **Stacked folder consolidation + tab normalization + template addition** on top of same thread without locking base step first

Building "in parallel" when steps are interconnected creates cleanup cost that exceeds the time saved.

**Pattern:** #pattern/sequence-over-parallel (for interconnected plans specifically)

### When parallel IS OK
**Chosen:** When Kay explicitly green-lights a bundle ("agreed on 1-3 steps", "go ahead with all of it"), parallel execution is fine. The rule is about unsolicited bundling, not disallowing parallel entirely.

### Principle: iterate on spec BEFORE execution, not after
**Chosen:** If there's any ambiguity about schema / format / columns / scope, draft the proposal in conversation FIRST, get confirmation, THEN execute. Don't draft-then-adjust-live.

**Reasoning:** 3 schema iterations today each triggered live cleanup. A 2-minute pre-proposal check would have collapsed it to one pass.

## Learnings

- When a plan has dependencies, the dependencies are usually MORE interconnected than they appear on the surface. "Phase 2 doesn't need Apollo" was true on one axis; untrue on the composite (Apollo + Attio MCP + Kay's scope intent).
- Bundling forward is often symptomatic of modeling the plan as linear-independent when it's actually interconnected-with-Kay-as-decision-node.
- The cost of pausing for confirmation is 30 seconds. The cost of clearing 291 rows of wrong output is 30 minutes + erosion of Kay's trust in the system. Asymmetric risk → always confirm.
- "Technically unblocked" is a red flag phrase — it usually means "I've rationalized a way to skip ahead."

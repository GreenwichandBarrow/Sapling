---
date: 2026-05-30
type: context
title: "Session Decisions — 2026-05-30 (BACKFILLED 2026-06-03 from shared notes; Claude programmatic-cost mitigation for the June 15 Anthropic billing change: ~$5k/mo finding, Sonnet model-routing SHIPPED, usage credits OFF, deal-aggregator downgrade target, Harrison brief drafted)"
tags:
  - date/2026-05-30
  - context
  - topic/session-decisions
  - topic/claude-infrastructure
  - topic/cost-optimization
  - topic/model-routing
  - topic/scheduled-skills
  - person/kay
  - person/harrison-wells
  - status/done
---

# Session Decisions — 2026-05-30

**Backfilled 2026-06-03** from notes Kay shared (sessions dropped before goodnight). Triggered by an AI-consultant heads-up about the **2026-06-15** Anthropic programmatic-billing change. Full state in memory [[project-claude-programmatic-cost-mitigation]] and `docs/scheduled-skills.md` "Model Routing (2026-05-30)".

## Decisions

### Claude programmatic cost mitigation
- APPROVE **Sonnet-default model routing** for all scheduled jobs; Opus only for `calibration-workflow` + `niche-intelligence` (allow-list); auth preflight on Haiku. Single chokepoint in `run-skill.sh`; subagents inherit parent model. Expected ~5x cut (~$5k → ~$1k/mo). → trace [[traces/2026-05-30-scheduled-jobs-default-sonnet-routing]].
- APPROVE **ship now, hear consultant in parallel** (not as a pre-gate) — change is live/reversible, free pre-cutover, gives a ~2-week observation window with Opus as fallback.
- APPROVE **usage credits OFF** as a hard floor (jobs throttle rather than over-bill); do NOT bulk-buy discounted credits yet; do NOT enable auto-reload. Reversed an earlier "keep credits ON" answer after Kay flagged the contradiction.
- REJECT the conservative variant (keep deal-aggregator + email-intelligence on Opus during observation) — Kay reviews that output anyway; full Sonnet routing left live as-is.
- Frame **deal-aggregator** (~$630/mo, most expensive, not top-value per [[project-kay-skill-value-assessment]]) as the prime downgrade candidate — evaluated on under-delivery, cost relief is the byproduct. Retirement is a minor lever; routing is the real saver.

## Actions Taken
- UPDATED `scripts/run-skill.sh` — `OPUS_SKILLS` allow-list + `SKILL_MODEL` routing on both `claude -p` invocation paths; preflight → Haiku; per-run `Model:` log line. (Committed; landed via auto-committer.)
- UPDATED `scripts/post_call_analyzer_mcp_poll.py` — pinned to Haiku defensively (dead code since the 5/13 granola-api REST migration).
- UPDATED `docs/scheduled-skills.md` — new "Model Routing (2026-05-30)" section (policy, Opus list, override, watch-and-promote).
- DRAFTED Harrison Wells call-6 cost brief (later saved as `brain/briefs/2026-06-01-harrison-wells-call-6.md`).

## Deferred
- **Re-measure programmatic spend before 2026-06-15** — re-run the 30-day transcript analysis with ~2 weeks of Sonnet data to confirm the landing spot. Scheduling parked pending the Harrison call (call #6 happened 6/1 → can now be scheduled).
- deal-aggregator downgrade shape (frequency vs model vs scope) — pending Harrison's read.
- Confirm exact new **Hetzner** rate + effective date (secondary, smaller magnitude).

## Open Loops
- Post-routing re-measure is the binding pre-6/15 task. Usage credits stay OFF until the tuned number is confirmed; flipping ON is an end-state decision.
- launchd-debugger reliability (the watchdog is itself the most frequent failer) — raised for Harrison.

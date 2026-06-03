---
schema_version: 1.1.0
date: 2026-05-30
type: trace
task: Mitigate the June 15 Anthropic programmatic-billing change for scheduled skills
had_human_override: true
importance: high
target: process
tags: [date/2026-05-30, trace, topic/claude-infrastructure, topic/cost-optimization, person/kay, pattern/sonnet-default-opus-allowlist, status/done]
---

# Decision Trace: Scheduled Jobs Default to Sonnet, Opus Only by Allow-List

## Context
Effective 2026-06-15, Anthropic bills programmatic Claude usage (`claude -p`, Agent SDK, cron) on a separate metered pool at full API rates. A 30-day transcript analysis put the scheduled fleet at ~$5k/mo, ~99% on Opus, because `run-skill.sh` passed no `--model` and every fire + its subagents inherited the Opus default.

## Decisions

### Model-routing policy
**Chosen:** default all scheduled jobs to **Sonnet**; keep only **`calibration-workflow` + `niche-intelligence`** on **Opus** (the two genuinely judgment-heavy jobs); auth preflight on **Haiku**. Single chokepoint in `run-skill.sh`; subagents inherit parent model so it routes the whole fan-out. Per-unit override via `SKILL_MODEL`.
**Reasoning:** the majority of scheduled work is data-gathering / scanning / classification / sheet-population where Kay is the judgment layer — Sonnet is sufficient. Expected ~5x cut (~$5k → ~$1k/mo). Reversible via one flag.
**Pattern:** #pattern/sonnet-default-opus-allowlist

### Ship now vs. gate on the consultant
**AI initial answer (reversed):** had earlier advised keeping usage credits ON for continuity.
**Chosen (Kay's correction):** usage credits **OFF** as a hard floor while tuning; ship the routing **now**, hear the consultant in **parallel**, not as a pre-gate.
**Reasoning:** the change is live-and-reversible (one flag), costs nothing extra pre-cutover (still on subscription with credits off), and gives a ~2-week free observation window with Opus still available as fallback. Waiting compresses or loses that window. Model routing is the uncontroversial floor under any structural workaround the consultant might propose.

## Alternatives Considered
- **Keep usage credits ON / opt into overflow** — rejected: removes the pressure to fix inefficiency and risks a real bill; OFF caps exposure with no surprise.
- **Conservative variant** (keep deal-aggregator + email-intelligence on Opus during observation) — offered, declined by Kay: she reviews that output anyway; full Sonnet routing left live as-is.
- **Gate rollout on the consultant meeting** — rejected: waiting buys nothing and wastes the free observation window.
- **Retire skills to cut cost** — reframed: retirement is evaluated on *failure/under-delivery*, not as a cost program; the fleet is mostly reliable, so routing is the real saver. Only deal-aggregator is a clean downgrade candidate (high cost, not top value).

## Why This Trace Matters
A future agent maintaining `run-skill.sh` could "helpfully" restore an Opus default or flip usage credits ON for reliability — both would silently undo the mitigation. The allow-list is deliberate; the OFF posture is deliberate.

## Key Insight
Cost is solved primarily by **model routing, not skill retirement.** Default cheap, allow-list expensive, and keep the hard floor (credits OFF) until a post-routing re-measure confirms the landing spot before 2026-06-15. State memory: [[project-claude-programmatic-cost-mitigation]]; value lens: [[project-kay-skill-value-assessment]].

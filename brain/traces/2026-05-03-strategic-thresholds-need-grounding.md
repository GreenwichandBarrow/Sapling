---
schema_version: 1.1.0
date: 2026-05-03
type: trace
title: "Strategic thresholds need grounding — the $1M EBITDA floor incident"
trace_type: reasoning-pattern
tags: ["date/2026-05-03", "trace", "topic/deal-aggregator", "topic/buy-box", "topic/reasoning-discipline", "topic/broker-channel"]
---

# Strategic thresholds need grounding — the $1M EBITDA floor incident

## Trigger

While building deal-aggregator's broker-channel relaxation, I proposed an "OPPORTUNISTIC floor" of $1M EBITDA / 12% margin for human-curated broker sources. Kay's response: "Why is the floor dropping?" — pushed back on the threshold itself. I had to admit the $1M was a guess, not derived from any constraint or data.

The actual constraint chain: $300K Kay salary + reasonable debt service → $2M practical EBITDA floor (per `feedback_deal_screen_300k_salary_15pct_margin`). That doesn't change by source. A $1M EBITDA broker-channel deal still doesn't pencil for Kay's structure. My proposed relaxation would have surfaced sub-floor deals as "opportunistic matches" — noise, not signal.

## Decision

Reverted the $1M floor. Adopted Kay's actual framing: separate Broker-Channel Buy Box with short criteria (geographic, industry-agnostic, financial floor unchanged at $2M). Geography window pending Kay's lock. Built channel-type infrastructure but parked the routing pending the buy-box doc build.

## Alternatives considered

1. **Defend the $1M floor** — would have required actual grounding (data on what brokers blast at, deal-economics math at the lower threshold). I had none.
2. **Relax other criteria instead** (margin, revenue band) — would have hit the same problem: any threshold relaxation needs a constraint reason, not a feel.
3. **Drop the niche-strict requirement only, keep $2M floor** — what I should have proposed first. This is what Megan Lawlor actually does: "filters for 2-3 industries but scans broadly" means scan industries broadly at the SAME financial gate.
4. **Build a separate buy-box for broker channel** — Kay's framing. Different criteria entirely (geo + agnostic + same financial floor + short list). This is the path adopted.

## Reasoning

The mistake: I conflated "Megan reviews broker deals opportunistically" with "Megan applies a relaxed floor." She doesn't. She applies a relaxed *industry* filter (any industry, not just her 2-3 thesis industries) at the same financial standard.

When I drafted the SKILL.md edit, I picked $1M because it was "lower than $2M" — a directional change, not a derived constraint. There was no math behind it. Kay's pushback exposed this immediately.

Strategic thresholds (financial floors, retention thresholds, scoring cutoffs) are NEVER feel-driven in this system. They're derived from constraints: $300K salary, debt service, runway, cohort econ, etc. If I can't show the constraint that produced a number, I shouldn't propose the number.

## Why this trace matters

Future agent doing similar buy-box work on this codebase — or any other domain with strategic thresholds — should follow this rule:

**Before proposing a strategic threshold, either:**
1. Cite the constraint that derives it (e.g., "$2M EBITDA = $300K salary / 15% margin floor / debt-service-affordable per memory X"), OR
2. Admit the threshold is a guess and ask the principal to set it.

Never paper over a guess with a confident-sounding number. The cost of a wrong threshold compounds — it becomes baseline, gets cited by future agents, and silently distorts decisions for weeks.

Specifically for G&B deal-aggregator: financial floors are constraint-driven (Kay's salary + debt service). Don't relax them by source type, channel, or any other axis. Relax INDUSTRY filters or GEOGRAPHY filters or NICHE filters when the source format justifies it. Don't touch the financial gate.

## Key insight

**"Lower than X" is not a derivation, it's a vibe.** Strategic thresholds need explicit constraint chains.

The same logic applies to any number I propose in this system: revenue bands, scoring weights, time windows, retry counts, cache TTLs. If the value is load-bearing — meaning future decisions cite it — it needs a reason. "It's what felt right" is not a reason. Either ground it in a derivable constraint, or surface the question and let Kay set it.

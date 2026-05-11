---
name: deal-aggregator calibration = volume-first
description: Deal-aggregator calibration measures VOLUME of surfaced deals, not accept rate. Assumption is filter already screens for buy-box fit.
type: feedback
originSessionId: 8bfb6c35-3c98-4296-85d8-07502729c766
---
Deal-aggregator calibration measures **volume** of leads surfaced per week (total count, distribution across niches, distribution across sources) — NOT accept rate.

**Why:** The skill's job is to filter deals to buy-box fit before Kay sees them. If Kay accepts 90% but only 2 deals surfaced that week, the skill failed — volume problem, not quality problem. Accept rate is a given by design; what matters is whether the aggregator is actually pulling enough qualified flow through. Stated directly by Kay on 2026-04-21: "If 90% meeting buy box, but its only 2 deals, its not enough. It doesnt matter. The assumption is that you are only surfacing things that meet the buy box, so its more about how much is surfacing."

**How to apply:**
- Skill Calibration row for deal-aggregator: use Presented column for total volume, Kay Notes for source + niche breakdown. Accept rate column is near-useless for this skill.
- Graduation criteria for deal-aggregator is volume-based: ">=5 deals/week sustained + 3+ contributing niches, 3 consecutive weeks" (matches SKILL.md target of 1-3 deals/day).
- If weekly volume is below target, diagnose: source coverage gap, niche corpus gap, or filter false-negatives — NOT accept-rate tuning.
- Applies only to deal-aggregator. Other skills (pipeline-manager, outreach-manager, etc.) continue to use accept-rate graduation.

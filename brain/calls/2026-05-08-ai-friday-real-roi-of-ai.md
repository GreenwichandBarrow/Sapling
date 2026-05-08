---
schema_version: 1.1.0
date: 2026-05-08
type: call
call_id: acd80cd9-a501-4028-80e4-830d37f8b976
source: granola
classification_type: internal
people: ["[[entities/kay-schneider]]"]
companies: ["[[entities/greenwich-and-barrow]]"]
tags: ["date/2026-05-08", "call", "client/greenwich-and-barrow", "person/kay-schneider", "company/greenwich-and-barrow", "topic/ai-friday", "topic/ai-roi", "topic/software-engineering-productivity", "topic/structured-ai-coding-practices", "topic/stanford-research"]
---

# AI Friday: Measuring the Real ROI of AI in Software Engineering

**Date:** 2026-05-08
**Attendees:** [[entities/kay-schneider|Kay]] ([[entities/greenwich-and-barrow|G&B]]); presenter "Yigar" (likely Yegor, Stanford Software Engineering Productivity / softwareengineeringproductivity.stanford.edu); co-host (introduces speaker, runs Q&A); webinar audience including Mark, Robert, Ben, Min
**Duration:** unknown (transcript captured mid-presentation through Q&A close)
**Source:** Granola meeting `acd80cd9-a501-4028-80e4-830d37f8b976`

---

## Summary

Webinar walkthrough of Stanford-affiliated research on measuring AI ROI in software engineering. Presenter shared findings from a dataset of ~46 enterprise teams + ~1,000 developers across 4 companies, with productivity scored via a custom ML model that quantifies "effective output" (not lines/PRs/commits). The research argues high performers pre-AI are NOT necessarily high performers post-AI (rank stability drops to ~0.50 from a normal ~0.70-0.80), that the slowest team member caps gains for everyone (heavy individual users get LESS lift than average users when teammates aren't AI-fluent), that structured AI coding practices (CLAUDE.md, cursor rules, agents.md, level 1-4 maturity) cut code-quality degradation by 3x, and that token-spend alone is a noisy proxy. Closing pitch was a "spicy" pilot: train an LLM on every employee's work over 90 days at a midsize company, then use it to materially reduce headcount, framed as an emerging private-equity playbook.

## Key points

- **Productivity metric is ML-derived, not commit-counting.** Code merged to main is rated for difficulty by ~15 reviewers, smoothed into a distribution; quality is part of the metric. PR review time is NOT accounted for, so coding-speed gains may be partially absorbed by review bottlenecks.
- **Team-level vs individual-level results diverge.** Top-quartile teams roughly 2x productivity post-AI; bottom-quartile teams use AI but get ~zero lift. Heavy individual users (76% lift) underperform mid users when teammates lag, because the bottleneck shifts to the slowest non-AI user.
- **Rank stability collapses.** Pre/post-AI quartile retention drops from ~0.70-0.80 (normal year) to ~0.50. Some bottom-quartile engineers (often senior/tech-lead with little code shipped pre-AI) jump to top quartile when AI lets them ship again. Some top performers fall by refusing to adopt.
- **Structured AI coding practices are a 3x quality moat.** Levels: L1 raw chat, L2 CLAUDE.md / cursor rules, L3 task-specific agents (reviewer, security, migration), L4 multi-agent swarm workflows. Repos at L2+ show 3x less code-quality degradation than L1 at similar productivity. Classifier paper pending peer review (~2 weeks); methodology uses cosine-similarity embeddings on artifacts, not filename matching.
- **Code-base cleanliness predicts AI gain.** Composite score (test coverage + type coverage + doc quality + modularity + static quality) on x-axis correlates strongly with productivity gains. Old enterprise / "ball of mud" code bases get hurt; clean code bases compound.
- **AI Spend Index (Stanford).** Median AI spend per developer per month ~$400; max observed ~$30K/dev/month. High-productivity-lift companies cluster at $500-$1K+/dev. Warning: companies treating AI like SaaS ($30-60/seat) statistically end up in low-performance bucket.
- **Communication overhead caps AI gains at scale.** A 5-person team has ~10 connections; a 50-person dept has ~1,200. Individual speed-ups don't compound past meeting/alignment overhead. Cited Eric Brynjolfsson research: AI productivity only materializes when companies redesign processes around the tech, not when they "bolt AI on" as a tool.
- **The pilot pitch.** Presenter is recruiting a midsized portfolio company for a 90-day observation, train internal LLM, significant headcount reduction. Framed as PE-friendly value-creation play. Payback claimed in days/months. Concession: when frontier LLMs catch up, "Anthropic takes your business anyway."
- **Free resources.** softwareengineeringproductivity.stanford.edu hosts papers + Stanford AI Spend Index. Give-get participation tier exists (share company data, get benchmarked results). Paid consulting tier for direct portfolio engagements.

## Action items

- [ ] Pull up softwareengineeringproductivity.stanford.edu and the Stanford AI Spend Index; review the free papers + benchmark Sapling/G&B's stack against per-developer spend distribution [Kay]
- [ ] Watch for the structured-AI-coding-practices classifier paper to clear peer review (presenter said ~2 weeks from 2026-05-08); revisit when published to score the Sapling repo's L1-L4 maturity [Kay]

## Decisions captured

(none, webinar attendance with no bilateral conclusions)

## Source

Granola meeting `acd80cd9-a501-4028-80e4-830d37f8b976`

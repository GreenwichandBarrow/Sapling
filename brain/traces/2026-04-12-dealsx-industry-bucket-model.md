---
schema_version: 1.0.0
date: 2026-04-12
type: trace
title: "DealsX Industry bucket = broad search mandate; tracker niches = narrow with shared bucket tag"
tags: ["date/2026-04-12", "trace", "topic/tracker-architecture", "topic/dealsx"]
target: skill:niche-intelligence
---

### Decouple DealsX sourcing breadth from tracker niche granularity
**Reasoning:** DealsX needs broad search terms (thousands of vendors) to source effectively, but G&B one-pager and scorecard templates assume narrow homogeneous niches (single margin range, single buyer profile). Considered three approaches: (a) one-pager averages across broad industry — hides signal; (b) industry one-pager with sub-vertical spotlight tables — works but adds new template complexity; (c) keep narrow tracker niches with a new "DealsX Industry" column tagging which ones share a sourcing bucket — preserves existing templates AND enables multi-niche-per-bucket sourcing. Chose (c) because it reuses proven deliverable formats and makes the bucket→niche relationship queryable.
**Trigger:** For every broad DealsX search bucket, create multiple narrow tracker niches inside it, each with their own one-pager/scorecard. All share the same value in the "DealsX Industry" column (Col L on WEEKLY REVIEW). Example: Specialty Healthcare PM/EHR bucket contains 5 tracker niches; EH&S bucket will contain Apparel Mfg Compliance + others.

### New columns appended, not inserted mid-sheet
**Reasoning:** Considered inserting DealsX Industry as new Col C (after Niche Hypothesis, logically adjacent) vs appending as last column. Chose append because mid-sheet insertion shifts every reference in pipeline-manager, target-discovery, col-lookup consumers, and raw gog commands — high breakage surface. Nothing reads past the last column, so appending is strictly additive.
**Trigger:** Any new tracker column goes at the end (currently L = DealsX Industry, M = SaaS Filter). Use col-lookup.sh for dynamic resolution — never hardcode letters.

## Learnings
- niche-intelligence: Skill identifier must tag each niche with its DealsX Industry bucket (or blank for non-DealsX niches). Tracker writer populates Col L.
- Tracker architecture: When sub-vertical-per-bucket rollups are needed for analysis, use Col L filter rather than separate tabs. One tab preserves sorting + review rhythm.
- target-discovery: Can source Apollo queries by DealsX Industry bucket (broad) and classify inbound targets into the right narrow tracker niche for routing + scoring.

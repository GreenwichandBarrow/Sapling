---
schema_version: "1.2.0"
date: 2026-04-15
type: trace
title: "SaaS revenue band revised: 2-6M ARR (was 3-10M) per Sam Singh / DealsX"
tags: ["date/2026-04-15", "trace", "role/cio", "topic/buy-box", "topic/vertical-saas", "topic/dealsx", "company/dealsx", "person/sam-singh"]
target: agent:cio
importance: high
---

### SaaS revenue band for G&B buy-box: 2-6M ARR, not 3-10M
**Reasoning:** On [[calls/2026-04-15-sam-singh-dealsx|Kay's 4/15 call with Sam Singh (DealsX)]], Sam pushed back on Kay's original 3-10M ARR filter for SaaS niches. His rationale: at 10M ARR, a software deal at 3-4x revenue = ~$30M acquisition, which is "too big" for search — deals at that size typically route to independent sponsors or private equity, not searcher-led LBOs. The SaaS sweet spot for search acquisitions is 2-6M ARR. 2M ARR is a valid floor if the underlying business is good. Kay approved on the call: "Happy to go down the fairway."

**Trigger:** All SaaS niches (vertical SaaS, horizontal SaaS, data platforms, specialty SaaS) must use 2-6M ARR as the size filter for target-discovery. This is distinct from the G&B generalist B2B services band (which may use revenue ranges appropriate to that business model). The CIO agent owns this band for SaaS verticals.

**Affected niches (immediate):**
- Vertical Software for Luxury & High-Value Asset Service Industries (existing Active-Outreach, via DealsX)
- Enterprise Software & Data Platforms (new DealsX vertical)
- Specialty Healthcare SaaS (new DealsX vertical)
- Female-Led Vertical SaaS (new DealsX vertical — manual enrichment)
- Any future SaaS niche under evaluation

**Affected skills/agents:**
- `target-discovery` — when querying Apollo/lists, cap at 6M ARR for SaaS niches, floor at 2M
- `niche-intelligence` — scorecard's size dimension should reference 2-6M for SaaS, not the generic G&B band
- `.claude/agents/cio.md` — update system prompt hard rule: "SaaS niches: 2-6M ARR. Flag targets outside this band as out-of-buy-box for SaaS evaluation."

## Learnings
- Searchers buy search-sized deals. 10M ARR SaaS is not search-sized — it's independent-sponsor or PE territory.
- Different business models need different revenue bands. One buy-box band across all niches over-fits to service businesses and excludes the SaaS sweet spot.
- DealsX (Sam Singh) has calibration data from hundreds of campaigns. Treat his band recommendations as high-signal input when they conflict with Kay's prior filters.

## Source
- Call: [[calls/2026-04-15-sam-singh-dealsx]]
- Granola meeting ID: b3dc3fff-1ece-4412-a9a1-f3061d0f1b4b
- Sam's exact phrasing: "Usually what searchers are looking at within software is, if it's a good company, even 2M ARR is good to like 6 is what the sweet spot is, is what we are seeing. Because usually 10 is like... those deals are just a little too big for a search acquisition."

frame_learning: true

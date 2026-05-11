---
name: conference-discovery and river-guide-builder share one event pipeline
description: Every broker-breakfast attendee is simultaneously a potential river guide AND a deal source
type: feedback
originSessionId: 86f718b9-b93e-4f82-8d6a-93917c8d6d15
---
conference-discovery and river-guide-builder operate on the same data source: event attendee lists. Don't run them as separate searches with separate pipelines. One event discovery per week feeds both skills.

**Why:** Kay's conference unlock (2026-04-15) is intermediary breakfasts — the same rooms where river guides live. Greg Donus's Smart Tours chain started at a broker breakfast → insurance broker → BDO connector → accountant → $25M deal. Intermediary = river guide = deal source. Artificial separation would duplicate work and split attention.

**How to apply:** Post-event, every attendee Kay meets gets (a) vault entity, (b) Attio People record, (c) `relationship_type` tagged (River Guide / Fellow Searcher / Industry Expert / Advisor / Broker), (d) `nurture_cadence` assigned, (e) `next_action` if Kay committed to something. Both conference-discovery and river-guide-builder read from this same post-event dataset.

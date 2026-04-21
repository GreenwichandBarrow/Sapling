---
schema_version: 1.1.0
date: 2026-04-20
type: trace
title: "Surface all relationship data; Kay decides per-context — data layer ≠ decision layer"
had_human_override: true
importance: high
target: "skill:river-guide-builder, skill:warm-intro-finder, skill:relationship-manager, process"
tags: ["date/2026-04-20", "trace", "topic/data-vs-decision", "topic/relationship-manager", "pattern/dont-prefilter-data"]
---

# Surface All Relationship Data; Kay Decides Per-Context

## Context

During Phase 2 cross-check of river guides, Lauren Della Monica came up as WARM for Art Storage (prior 1:1 call Jul 2025, existing vault entity). Same morning, Kay PASS'd Lauren on general relationship-manager catch-up ("no need to reconnect"). I flagged the conflict to Kay as a concern — "Lauren came up as WARM here even though you PASS'd her on general catch-up."

## Decisions

### How to handle conflicts between data layer and decision layer
**AI proposed:** Flag Lauren's appearance in Phase 2 output as a concern, possibly filter her out or caveat the result.

**Chosen:** Surface every hit. Don't pre-filter. Kay decides per-context whether to tap a contact for a specific deal.

**Reasoning:** Kay: "this work is different from relationship manager. please just add anyone you find to the tab and I will determine next steps." Also: "I am not going through all of these people I don't even know."

The two axes are different:
- **Relationship-manager** answers: "should the system prompt Kay to proactively reach out on a cadence?" Lauren: PASS (don't prompt).
- **Phase 2 / target sheets** answer: "who in Kay's network is a warm intro path for THIS niche?" Lauren: YES (art-storage WARM).

These aren't contradictions — they're different questions. A contact can be PASS'd for general nurture AND simultaneously be a lever if a specific deal surfaces in their expertise.

**Pattern:** #pattern/dont-prefilter-data — data-surfacing layer should show every hit. Filter happens at the decision layer (Kay), not the data layer.

### Exception: explicit Do Not Call lists
**Chosen:** `Do Not Call` tabs on target sheets ARE explicit DNC flags (e.g., Acumen/Uovo/Hangman for Art Storage per prior decisions). Those honor as hard filters.

**Reasoning:** DNC is a deliberate permanent exclusion signal, not a nurture-cadence state. Different category.

### Implication for future skill design
**Chosen:** When a skill produces data output (target sheet, warm-intro list, Network Matches), include every match. In the orchestrator's summary to Kay, don't caveat "X came up WARM but you PASS'd them on nurture" — just report the data. Kay is the decision layer.

## Why This Trace Matters

Before today, relationship-manager memories (feedback_intermediary_dormancy_monitoring, etc.) tell future agents how to handle nurture cadence. Without this trace, a future agent might apply those same filters to data-surfacing tasks — suppressing contacts from target sheets based on nurture PASS decisions.

That would silently erase real relationship data from Kay's view. She wouldn't see Lauren as an art-storage lever because the system decided Lauren "was out."

## Key Insight

Data surfacing ≠ action recommendation. The same person can be:
- Inactive for proactive cadence
- Active as an opportunistic lever for a specific deal

Build systems that preserve both axes independently. Don't collapse "doesn't want cadence" into "never mention this person again."

## Learnings

- A PASS on one axis is not a PASS on all axes. Preserve orthogonality.
- When unsure whether to filter a data result, default to surfacing + letting the user decide. Filters are easy to add later; missing data is invisible.
- Flagging conflicts to the user ("this person came up but you PASS'd them") can itself be noise. Only flag if the conflict is semantically meaningful, not mechanically automatic.

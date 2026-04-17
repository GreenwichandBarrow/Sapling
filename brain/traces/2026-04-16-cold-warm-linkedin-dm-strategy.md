---
schema_version: 1.2.0
date: 2026-04-16
type: trace
task: Route ACG NY DealSource attendee list (4 annotated targets) to action
had_human_override: true
importance: high
target: skill:conference-discovery
tags: ["date/2026-04-16", "trace", "pattern/cold-warm-hybrid-dm", "domain/outreach"]
---

# Decision Trace: Cold-Warm Hybrid LinkedIn DM Strategy (Attendee List Routing)

## Context

Kay received the ACG NY DealSource 4/14/2026 attendee list but didn't attend the event. She annotated 4 targets with "1" (would-have-met) and a mutual LinkedIn connection name. The question: how to route these 4 now that the in-person opportunity was lost?

## Decisions

### Routing Strategy

**AI proposed (default pattern):** For each annotated target, route through the warm connector — ask Luka, Rich, Gelila, (and initially) Lacey for a warm intro request. Standard warm-intro-finder flow.

**Chosen (by Kay):** Cold-warm hybrid — send a cold LinkedIn DM directly to each target and *mention the mutual connection by name* in the DM. The target can verify the connection on LinkedIn themselves. No intro asks to connectors required.

**Reasoning:**
1. **Lower friction on Kay's network.** Her connectors don't have to do anything for her. This preserves the connector relationships for higher-value asks later.
2. **Social proof is transferable without the connector being involved.** The target can verify the shared connection on LinkedIn in 5 seconds — the signal works even without the connector sending anything.
3. **Speed and volume.** 4 warm-intro asks would take days of back-and-forth with connectors; 4 cold-warm DMs go out the same day.
4. **Risk-adjusted return.** If the target ignores the DM, no favor was burned. If they reply, the connector can be looped in at that point.

**Pattern:** #pattern/cold-warm-hybrid-dm

### Attendee List Processing Scope

**AI proposed:** Catalog all 54 ACG attendees into Attio as a reference set for future cross-check.

**Chosen:** Only act on Kay's 4 annotated "1"s. Leave the remaining 50 un-ranked attendees as a reference file in Drive. No bulk Attio cataloging.

**Reasoning:** Per [[feedback_broker_competition]], IB/PE conference rosters are the "3000+ buyers" noise pool. Bulk-cataloging them dilutes signal quality in Attio. Kay's annotations ARE the signal — the un-annotated rows are intentionally deprioritized.

**Pattern:** #pattern/signal-over-volume

## Learnings

- **Conference attendee lists route differently from cold prospect lists.** The "annotation layer" Kay adds (LinkedIn lookup + mutual connection notes) is the actual prioritization work. Skills processing these lists must respect her annotations and NOT bulk-catalog un-annotated rows.
- **Cold-warm hybrid is a distinct outreach pattern.** Neither pure warm-intro-request nor pure cold outreach. Mention mutual connection in the DM body as verifiable social proof. Use when (a) in-person opportunity was missed, or (b) the warm connector is inconvenient to ask (time, relationship depth, or prohibited by another rule — e.g., Lacey).
- **Don't over-invest in connector relationships for low-ROI intros.** Save the connector asks for high-value targets where the connector's explicit endorsement is the thing.

## Targets for Calibration

- **conference-discovery skill:** When processing an annotated attendee list, detect "Column with connector notes + ranking" pattern and default to cold-warm hybrid DM routing (not warm-intro-finder routing) unless Kay specifies otherwise.
- **outreach-manager skill:** Add cold-warm hybrid as a third channel alongside warm-intro and pure-cold.
- **Memory:** Add `feedback_cold_warm_hybrid_dm_pattern` to MEMORY.md.

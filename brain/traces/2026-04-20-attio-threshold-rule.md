---
schema_version: 1.1.0
date: 2026-04-20
type: trace
title: "Attio records: event-driven creation, not skill-driven"
had_human_override: true
importance: high
target: "skill:river-guide-builder, skill:outreach-manager, skill:relationship-manager"
tags: ["date/2026-04-20", "trace", "topic/attio", "topic/threshold-rule", "pattern/event-over-schedule"]
---

# Attio Records: Event-Driven Creation on First Outbound

## Context

River-guide-builder Phase 1 + 2 output hundreds of external contacts (associations, industry CPAs, M&A lawyers, etc.). Original skill design had config flags (`ATTIO_WRITE_RIVER_GUIDES`, `ATTIO_TAG_NETWORK_MATCHES`) to auto-create Attio records. Kay pushed back on whether ANY automated Attio creation was correct.

## Decisions

### Attio creation trigger
**AI proposed:** Config-gated automatic creation at skill runtime — when river-guide-builder identifies a river guide, auto-create Attio People record (with `nurture_cadence=Dormant`, `relationship_type="River Guide"`). Flags default OFF until Kay flips them.

**Chosen:** NEVER auto-create from skill. Attio records created by **outreach-manager** at the moment Kay sends her first outbound (email / LinkedIn DM / intro ask). Until then, contacts live only on target-list Google Sheets.

**Reasoning:** Kay: "The way Attio naturally works is it doesn't add contacts to my CRM if they have emailed me — they get added when I reply or outreach to someone. I think that's a really smart filter because it avoids spam and bloat." The filter philosophy IS the signal. Attio is for "people I've actively engaged," not "people I might engage someday." Bulk skill-driven creation would undermine this filter and pollute the CRM.

**Pattern:** #pattern/event-over-schedule — triggers should be user actions, not scheduled skill runs.

### What DOES get persisted
**Chosen:** Associations tab + River Guides tab on the niche target-list Google Sheet. This is the target list Kay + Sam work from. Attio is reserved for the engagement layer.

### Relationship-type tag on creation
**AI proposed:** Set `nurture_cadence = "Dormant"` + `relationship_type = "River Guide"` on creation.

**Chosen:** Set `relationship_type` only (River Guide / Industry Expert / Advisor as appropriate). **Do NOT set `nurture_cadence`** — intermediaries are passively monitored via dormancy logic (separate trace), not cadence-prompted.

**Reasoning:** Setting Dormant suggests active cadence management which doesn't apply; leaving nurture_cadence blank signals "passively watched, not on a prompt cadence."

## Learnings

- When a CRM or system has a natural inbound/outbound filter, **don't bypass it with automation** — use it as the threshold signal.
- "Event-driven creation on user action" > "scheduled bulk creation with flags" when the goal is data-quality-signal.
- Config flags are a failure mode: they make it look like a reversible decision but actually encode the wrong mental model (should Attio auto-create at all?). The right answer is: no flags, event trigger.

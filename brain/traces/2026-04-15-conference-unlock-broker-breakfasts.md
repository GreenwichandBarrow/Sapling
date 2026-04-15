---
schema_version: "1.2.0"
date: 2026-04-15
type: trace
title: "Conference pipeline unlocked: grass-roots broker breakfasts + intermediary coffee chats, NOT big industry conferences"
tags: ["date/2026-04-15", "trace", "role/cmo", "role/cpo", "topic/conference-pipeline", "topic/river-guides", "topic/kays-approach"]
target: agent:cmo, agent:cpo, skill:conference-discovery, skill:river-guide-builder
importance: high
---

### Kay's conference strategy is intermediary networking, not industry events
**Reasoning:** On 2026-04-15, after listening to the Greg Donus / Smart Tours episode of SMB Deal Hunter (host: Helen Guo), Kay said:

> "In the podcast he mentioned he went to a broker breakfast on Long Island — that is exactly the kind of thing I want to attend. Broker morning coffees, same as that ACG speed dating type thing with deal makers. Those are not expensive conferences and I love coffee chats. Those are the best ways for me to get out there — build river guides and find businesses."

Donus's story: Long Island broker breakfast → insurance broker contact → Todd Kenny BDO connector → Capital One banker → accountant → $25M Smart Tours deal. The chain started at a 7am diner breakfast that cost nothing.

**Trigger for conference-discovery:**
- **Primary target format (priority 1):** broker breakfasts, intermediary coffee chats, M&A happy hours, ACG speed-networking, XPX chapter meetings, accounting/law firm sponsored events, wealth manager lunches.
- **Secondary format (priority 2):** Industry-specific conferences (CMAA, boat shows, etc.) — still valuable, but not the center of gravity.
- **De-prioritized:** Big industry events (SaaStr, HIMSS, ETA flagship conferences). Too expensive, too low signal, too exhausting for the intermediary density Kay actually wants.

**Event criteria filter for conference-discovery:**
1. Cost: under $100 preferred; $100-500 OK for high-signal; flag anything over $500
2. Duration: 2-3 hours preferred; willing to do 4-6 hour events if NYC
3. Format: breakfast / coffee / lunch / happy hour / speed networking
4. Geography: NYC + Long Island + NJ + CT + Philly + Boston
5. Timing: Monday full-day OK; Tues/Wed NYC-only (done by 1:30pm); Thursday (done by 4:30pm); NO Fridays; NO evening-only
6. Attendee profile: must skew intermediary (brokers, M&A advisors, CPAs, M&A lawyers, wealth managers, bankers) or SMB owner clusters

**Cadence:** Target 1/week minimum. More if discovery yields more viable events. Kay's physical capacity is high for this format (short, local); discovery rate is the constraint.

**Skill merge observation:**
- `conference-discovery` and `river-guide-builder` should share one event pipeline. Every broker-breakfast attendee is simultaneously a potential river guide AND a potential deal source. Don't run them as separate searches.
- Post-event protocol: within 48 hours, every attendee Kay met gets (a) vault entity, (b) Attio People record, (c) `relationship_type: Fellow Searcher / Industry Expert / River Guide / Advisor` tagged, (d) `nurture_cadence` assigned, (e) next_action if Kay committed to something.

**"Brief needed?" flip:**
For broker breakfasts and intermediary events, Kay does NOT need a full meeting-brief. She needs a 1-page attendee intelligence sheet: host of event, past attendee list (LinkedIn + prior invites), names Kay already knows, any prior outreach history. 15-minute prep max — not 90-minute brief.

**Storage:**
Events go into the existing **Conference Pipeline** Google Sheet (ID: 1bdf7xlcRjOTlVkuXA-HNGOQgjtDRmVN2RfDf9aUsDpY) as rows. Don't create a new sheet — Kay likes the existing one. Add a column if needed for event format (breakfast / speed-networking / happy hour / conference).

## Learnings
- Kay's highest-leverage channel is human chemistry in small rooms, not volume at large events. The podcast story confirmed what the system should have been doing already.
- Grass-roots intermediary events are the least-expensive, highest-ROI channel available to a solo searcher in NYC. They also compound — same breakfast, same 8 people, every month = relationships that deepen.
- Conference-discovery and river-guide-builder operate on the same data source (event attendee lists). Ideally they become one skill or share one event-pipeline datastore.

frame_learning: true

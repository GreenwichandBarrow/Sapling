---
schema_version: 1.1.0
date: 2026-05-04
type: trace
title: "Investor capacity letter ask routes via next meeting brief, not standalone email"
trace_type: routing-pattern
tags: ["date/2026-05-04", "trace", "topic/investor-relations", "topic/meeting-briefs", "topic/routing-pattern", "person/guillermo-lavergne", "person/jeff-stevens"]
---

# Investor capacity letter ask routes via next meeting brief, not standalone email

## Trigger

Carryover from prior session: capacity letter requests to Guillermo Lavergne + Jeff Stevens (needed to support broker-channel positioning per the new Megan Lawlor pattern). Both items were in the prior continuation file's "After hours" todo. I surfaced them tonight as deferred candidates for tomorrow.

Kay's response: "please just add that to their prep briefs for their next meetings with me. no need to do anything before"

This is a routing decision, not an execution timing decision.

## Decision

Capacity-letter ask is added as a "Pending Discussion Topics" section to each entity file:
- `entities/guillermo-lavergne.md`
- `entities/jeff-stevens.md`

Both contain the same standing instruction: surface in next meeting prep brief, do NOT email about it beforehand. Once Kay confirms the ask was made and committed/declined, the bullet gets removed from the entity file.

The meeting-brief skill reads entity files as part of brief generation (per `meeting-brief/SKILL.md` template structure), so the next time either Guillermo's bi-weekly or Jeff's next meeting is generated, the brief surfaces "ask about capacity letter" automatically.

## Alternatives considered

1. **Email both about the capacity letter now** — what I would have done if Kay hadn't redirected. Rejected by her. Investor asks via standalone email between calls fragments the relationship cadence and turns a natural in-call moment into a transactional email exchange.
2. **Add to brain/inbox/ as time-triggered items** — rejected because there's no specific date trigger. The trigger is "next meeting with this person" which is event-based, not date-based. Entity-file Pending Discussion Topics is the right home.
3. **Add to a separate brain/context/pending-asks.md aggregator** — rejected as over-engineering. Two entity-file edits is simpler than introducing a new persistence file. If pending-asks accumulate across more than 5 entities in the future, revisit.

## Reasoning

Investor relationship cadence has a rhythm (bi-weekly for Guillermo, less frequent for Jeff). Inserting standalone emails between scheduled touchpoints disrupts that rhythm and signals urgency where there isn't any. The capacity letter is supportive of the broker-channel build but not blocking — it can wait days/weeks until the next natural touchpoint.

Routing-pattern lesson: **for asks that aren't time-critical, prefer the next-natural-touchpoint over a standalone outreach.** The relationship surface (a scheduled call) absorbs the ask without adding friction. Email-between-touchpoints should be reserved for time-sensitive matters or when no near-term touchpoint exists.

Mechanism choice: entity-file Pending Discussion Topics section is the right home because (a) entity files are read by meeting-brief skill, (b) the data lives WITH the relationship context (so a future agent reading the entity for any reason sees the pending ask), (c) removal is trivial — one edit when the ask is closed out.

## What would change if reversed

If a future agent decides "we still need that capacity letter, let me draft an email" instead of waiting for the next meeting brief: investor receives a friction-creating ad-hoc email outside the established cadence. Worse: violates the new intermediary-template-only doctrine if the future agent improvises the email body (investors aren't intermediaries per se but the same rule of "don't draft ad-hoc to relationship-critical contacts" applies in spirit).

If a future agent doesn't see the entity-file note and the capacity letter falls through the cracks: broker-channel build's positioning loses a supporting element. The Pending Discussion Topics section is in the entity file body, so meeting-brief generation should pick it up automatically — but worth verifying once the next brief actually fires for Guillermo or Jeff.

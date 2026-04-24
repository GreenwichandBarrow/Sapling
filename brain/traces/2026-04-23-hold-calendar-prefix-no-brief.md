---
schema_version: 1.1.0
date: 2026-04-23
type: trace
title: "HOLD Calendar Prefix = Unconfirmed Meeting, Skip Brief Generation"
tags: ["date/2026-04-23", "trace", "topic/brief-decisions-pre-flight", "topic/calendar-conventions", "topic/meeting-brief", "topic/morning-briefing", "person/mark-gardella"]
had_human_override: true
importance: medium
target: process
people: ["[[entities/kay-schneider]]", "[[entities/mark-gardella]]"]
companies: []
---

# Trace: HOLD Calendar Prefix Means Unconfirmed

## Context

Morning briefing 2026-04-23 enumerated tomorrow's external meetings per the Brief-Decisions Pre-Flight invariant added 2026-04-21. Mark Gardella appeared on Friday 4/24 1pm — calendar event title `HOLD mtg w/ Mark` with zero non-Kay attendees. Skill flagged for brief generation per the existing Step 2 rule ("if not approved/declined in last 3 days, MUST surface as Decisions item").

Kay's correction: "No brief. I just put a hold on my calendar. He hasn't confirmed. Please update skill to note that if a calendar invite says 'HOLD' it is not confirmed."

This is a Kay-personal calendar convention (HOLD = self-placed placeholder awaiting external confirmation) that the agent had no way to know without being told.

## Decisions

### HOLD prefix + zero non-Kay attendees = unconfirmed = skip brief
**AI behavior before today:** Brief-decisions pre-flight applied to ANY external calendar event, regardless of confirmation status. Calendar event existed → brief flagged.
**Chosen rule:** Added Step 1 to the pre-flight check in CLAUDE.md morning workflow. If event title starts with `HOLD ` (or contains `HOLD mtg`/`HOLD call`/etc.) AND has zero non-Kay attendees, treat as unconfirmed. Skip brief generation. Surface only if Kay needs a soft-nudge decision on whether to chase the counterparty.
**Reasoning:** Generating a meeting brief for an unconfirmed meeting wastes both the prep effort AND Kay's time reviewing a brief for something that may not happen. The HOLD convention is Kay's signal to herself that the slot is held but the meeting isn't real yet. Treating that slot as a real meeting violates the convention.
**Pattern:** #pattern/respect-user-calendar-conventions

## Why This Trace Matters

The Brief-Decisions Pre-Flight was added 2026-04-21 to fix the Guillermo-miss (failed to surface a brief decision for a confirmed external meeting). It was a strict "must surface" rule — designed to fail loud. Today's correction adds the OPPOSITE failure mode: don't surface for unconfirmed events. The skill was right to be strict but missed the confirmation gate.

A future agent running morning workflow would see "HOLD mtg w/ Mark" and either (a) flag it for brief like today's bug, or (b) skip it and miss a real meeting if HOLD is being used inconsistently. The codified rule (HOLD + zero attendees = skip) gives a single, testable gate: presence of non-Kay attendees converts an unconfirmed HOLD into a confirmed event.

## Key Insight

Calendar event titles encode user-personal conventions that aren't visible to the agent until the user states them. When the agent surfaces an event for action, it should encode at least the obvious confirmation signals: title prefix conventions (HOLD / TENTATIVE / DRAFT) and attendee presence. Without those gates, calendar-driven workflows generate noise on every self-placed placeholder.

## Closure Mechanism

- Updated CLAUDE.md morning workflow Brief-Decisions pre-flight from 2-step to 3-step (added Step 1: HOLD + zero attendees = skip).
- Numbering of original steps shifted (old Step 1 → Step 2, old Step 2 → Step 3).
- Mark Gardella brief NOT generated for 4/24 1pm.

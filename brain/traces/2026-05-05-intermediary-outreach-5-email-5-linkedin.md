---
schema_version: 1.1.0
date: 2026-05-05
type: trace
today: "[[notes/daily/2026-05-05]]"
task: Define daily intermediary cold-outreach cadence after Apollo enrichment hit-rate landed
had_human_override: true
importance: high
target: skill:outreach-manager
tags: ["date/2026-05-05", "trace", "topic/intermediary-channel", "topic/broker-outreach", "pattern/two-channel-outreach-split", "pattern/per-person-tool-selection"]
---

# Decision Trace: Intermediary Outreach — 5 Email + 5 LinkedIn Per Day

## Context

Yesterday's session-decisions captured a plan to draft "10 broker first-touch emails per day" as the intermediary-channel cadence. Apollo enrichment ran this morning across the Intermediary Target List (sheet `18zzE1y-BU1xuD-y0BOmEl8GtJ4I-iclSuBqAi0q3pkk`): 15 lookups, 5 emails verified, 9 person-found-no-email, 1 suspect held back. Kay reviewed the hit-rate and re-shaped the cadence frame.

## Decisions

### Daily intermediary outreach is split across two channels, not stacked on one

**AI proposed (carried from yesterday):** 10 broker first-touch emails per day, single channel, all email.

**Chosen (Kay):** **5 emails + 5 LinkedIn DMs per day**, mutually exclusive person sets. The two channels are filled with **different people** — never the same person on both.

**Reasoning:**
- Two-channel diversification reduces single-channel risk (deliverability, sender reputation).
- Apollo's 9 "person found, no email on file" set is the natural LinkedIn pool — these brokers have active LI profiles but no Apollo-verifiable email. Pinging Apollo or Hunter again on the same person is wasted spend; LI gets the same person at zero enrichment cost.
- Email + LI hit different inboxes, which compounds first-touch surface area without burning either sender pattern.

**Pattern:** #pattern/two-channel-outreach-split

### Per-person channel selection (not blanket-by-cohort)

**AI proposed:** Default to email for all enriched contacts, LinkedIn as fallback when email unavailable.

**Chosen (Kay):** Pick the channel that matches the **individual**:
- Verified email available → email channel
- Email unreachable (Apollo no-match, dead bounce) but LinkedIn profile is active → LinkedIn channel
- Both available → email channel (default), LinkedIn slot goes to a different person

**Reasoning:** "Use the tool that's specific to that particular individual." Each person has a single optimal channel based on which inbox they actually live in (some senior brokers ignore LI entirely; some are more responsive on LI than email). The skill should never double-touch the same person on both channels in the same day — that reads as automation spam, not warmth.

**Pattern:** #pattern/per-person-tool-selection

### Apollo no-match → LinkedIn track, not Hunter retry

**AI proposed:** For the 9 Apollo no-match brokers, queue Hunter.io or Snov.io as secondary email enrichment.

**Chosen (Kay implicit, follows from above):** Route Apollo no-match brokers to LinkedIn DM track instead. Hunter/Snov.io stay as last-resort, not first-resort.

**Reasoning:** If a person isn't in Apollo's email index, they're often deliberately quiet on email. Hunter/Snov.io are likely to surface stale or guessed addresses — bouncing damages Kay's sender reputation, which is her entire business. LinkedIn is the right second-touch surface for these contacts.

**Pattern:** #pattern/lo-email-presence-suggests-non-email-channel

## Why This Trace Matters

The default frame for cold outreach has been "more email = more pipeline." Kay's frame here is different: **a daily cap that splits across channels, with mutual exclusivity per person, optimizes for response rate not raw volume.**

A future agent building outreach rosters will reach for "draft N emails" by reflex. This trace says: split the N. Build two rosters. Pick the per-person tool. Track per-channel response rates separately so the doctrine can self-validate over time.

The 5+5 number is not arbitrary either — it's a daily volume Kay can personally review and approve in the morning briefing without burning out, since per `feedback_kay_handles_all_replies` she sends every reply manually. Larger volumes break that handoff.

## Key Insight

**The right outreach cadence is N total touches per day across optimal-per-person channels, not N emails per day with channels as fallbacks.** When channel choice is reflexive ("email unless you can't"), the agent leaves response-rate gains on the table for contacts who live elsewhere. When channel choice is per-person ("which inbox is this person actually in"), the same daily volume produces better outcomes.

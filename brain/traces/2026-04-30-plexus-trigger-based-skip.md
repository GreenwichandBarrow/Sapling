---
schema_version: 1.1.0
date: 2026-04-30
type: trace
title: "Plexus skip — trigger-based contact handling beats time-based outreach"
people: ["[[entities/katie-walker]]"]
companies: ["[[entities/plexus-capital]]"]
tags: ["date/2026-04-30", "trace", "person/katie-walker", "company/plexus-capital", "topic/intermediary-outreach", "topic/contact-management", "signal/calibration-high"]
---

# Plexus skip — cross-reference call history before treating as fresh outreach

## Decision

Skipped Plexus / Katie Walker from the morning's lender outreach round despite her appearing on the 4/29 priority list. Reason: she's an existing relationship in active trigger-based mode (4/16 substantive Zoom call, last email 4/17, vault next-action = "loop in Katie when G&B reaches LOI on a vertical SaaS deal"). A generic "introducing myself, here's the buy-box" email today would re-pitch a relationship that's already past that stage and ignore her trigger-based wait.

## What almost happened

The 4/29 session decisions listed three priority lenders: Plexus (Katie Walker), Parkside (Zach Duprey), Avidbank (Anthony Rodriguez). All three were tagged for first-reach + warm-intro outreach with the "Will Bressman, GJ King, and Melissa Rosenblatt at BK Growth recommended I introduce myself" line.

For Plexus specifically, the 4/29 decision was based on the warm-intro framing without cross-checking the existing relationship state. The Lenders tab notes ("Already in correspondence") flagged it but didn't surface in the priority-list framing. The vault `brain/calls/2026-04-16-katie-walker-conwell.md` had the trigger-based next-action explicit but wasn't read at decision-time.

## What was caught

Pre-draft check pulled the actual Lenders tab row + the 4/16 call note. The call note includes:
- High satisfaction, high expansion potential
- Katie placed Kay in "strong searcher" bucket (~70% closure tier per her view)
- Trigger-based next-action: "loop in Katie when G&B reaches LOI on a vertical SaaS deal"
- "Sometimes you just need time to recalibrate" — Katie is patient with Kay's pace

A generic intro email at this stage would:
1. Read as if Kay forgot the 4/16 call
2. Ignore Katie's stated trigger (LOI on vertical SaaS)
3. Damage a relationship that's currently positive

## Why this matters for future agents

Two durable patterns emerge:

1. **Cross-reference recent call history (last 60 days) before treating ANY intermediary as a fresh outreach target.** Even if a 4/29 priority-list decision tagged them as "first-reach," the actual relationship state may have moved since. The vault `brain/calls/` files are the ground truth.

2. **Trigger-based next-actions override time-based cadence.** Per `relationship-manager` SKILL.md and `feedback_relationship_cadence_friday_only.md`, contacts whose `next_action` contains trigger language ("when," "once," "after," "if") should NOT be surfaced for time-based outreach. Wait for the trigger.

## How a future agent should apply

Before drafting any intermediary outreach:
1. **Pull the contact's row from the Intermediary Target List sheet** + the relevant tab (Brokers / IBs / Lenders / etc.)
2. **Check the Notes column for "Already in correspondence" or similar relationship-state markers**
3. **Glob `brain/calls/` for the contact's slug** — read the most recent call note
4. **Check Attio People record's `next_action` for trigger language**
5. If existing relationship + trigger-based next-action → SKIP the time-based outreach, wait for trigger
6. If existing relationship + time-based next-action → continue thread (don't reintroduce per `feedback_continue_dont_reintroduce.md`)
7. Only if NO existing relationship → first-reach outreach

## Related context

- 4/16 Katie Walker call note: `brain/calls/2026-04-16-katie-walker-conwell.md`
- Lenders tab row in Intermediary Target List sheet
- Plexus is a HIGH-VALUE relationship (warm equity coinvestor + warm debt source + community amplifier) — preserving it has more long-term value than any single outreach send
- Same pattern likely applies to other contacts on the 4/29 priority lists — should be audited before each is targeted

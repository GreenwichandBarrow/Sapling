---
schema_version: 1.1.0
date: 2026-04-30
type: call
call_id: 8c477f91-dae5-4832-acc1-39dcbbff5b15
source: granola
classification_type: internal
people: ["[[entities/jerome-madrona]]", "[[entities/abigail-quibilan]]"]
companies: ["[[entities/greenwich-and-barrow]]", "[[entities/start-virtual]]"]
tags: ["date/2026-04-30", "call", "client/greenwich-and-barrow", "person/jerome-madrona", "person/abigail-quibilan", "company/greenwich-and-barrow", "company/start-virtual", "topic/jj-operations", "topic/cold-calling", "topic/process-improvement", "topic/pest-management"]
---

# Team TB — JJ + Abby + Kay

**Date:** 2026-04-30 11:00 ET
**Attendees:** [[entities/jerome-madrona|JJ (Jerome Madrona)]] (StartVirtual cold caller), [[entities/abigail-quibilan|Abby (Abigail Quibilan)]] (StartVirtual relationship manager), Kay Schneider ([[entities/greenwich-and-barrow|G&B]] principal)
**Granola ID:** `8c477f91-dae5-4832-acc1-39dcbbff5b15`

## Context

Recurring weekly check-in on JJ's cold-calling shift performance. JJ working from a temporary location in the hillside (volcano displacement near home, second move, secured a small house for next 2-3 months). Confirmed offset hours have been logged with Abby for prior week's lost time. Two weeks into the Premium Pest Management cold-call sprint.

## Notes

### What's working
- **Pest management answer rate is unusually high.** Industry operators are accustomed to phone calls as part of daily business operations (customer issues), so they pick up at higher rates than other industries.
- **~1 solid lead per week** is JJ + Abby's normal baseline for cold-call work. Two leads in two weeks tracks normal.
- **Callbacks coming in** — last week JJ had 2-3 returning calls from customer-service-reps after he left messages with them. They're routing back through to him, asking for owner availability.
- **JJ's email-leaving practice** — when an IVR dumps him to customer service, he's been leaving Kay's email so the rep can pass it through.

### What's not working
- **IVR mazes** eat call time. Each "press 1, press 2, press 3" wait reduces total dial volume in the 4-hour shift.
- **Voicemail/customer-service script length** — when JJ followed the existing call guide verbatim, prospects mistook him for AI and hung up. He's been rephrasing in real time to make calls more personal. He'll send the rephrased voicemail / gatekeeper / main scripts to Kay via Slack today.
- **Google Voice recording broken** — JJ has been clicking record on his calls to send Kay reference material, but recordings are gone the next day. Needs admin-side fix.

### Spam-flagging risk + number rotation
Abby flagged that repeated dialing from one Google Voice number gets flagged as spam by carriers. Once flagged, prospects don't pick up because their carrier has labeled the call as spam. Mitigation:
- Watch for signals of flagging (sellers explicitly saying "your number was flagged" + drop in pickup rates).
- **Plan a proactive number swap when shifting from pest management to the next industry** (~2 weeks out).
- High-volume dialer tools have auto-rotation; Google Voice does not, so manual swap is the workaround.

### Workflow change — callback weeks
JJ and Kay agreed: alternate weeks between new-list dialing and callback dialing.
- Week N: dial fresh 200-contact list (40/day x 5 days).
- Week N+1: no new list. JJ uses the time to chase callbacks, no-answers, and "call back later" requests from prior week.
- Maximizes the 4-hour shift; lets aged contacts "rest" so carriers don't double-flag.

### Volume calibration
- Current pace: 25-40 calls/day, depending on IVR density.
- 200 contacts/week is the working list size.
- If JJ finishes the day's 40 fast, he can pull from later days in the same weekly list (200 contacts is a pool, not strict daily quotas).
- Abby/JJ flagged that more contacts in pool = better hit-rate on conversion. Worth watching whether 200/week is the right ceiling once we have more shifts logged.

### Industry transition planning
Kay is at a pest-management conference in Charlotte in ~2 weeks. She likes the niche and wants to keep going. But:
- The current 200-contact list will be exhausted by end of next week.
- After the callback-week, Kay needs to either refill the pest list OR move JJ to the next industry.
- Number swap will coincide with industry change.

## Action Items

| Owner | Action | Status |
|-------|--------|--------|
| Kay | Give JJ her direct phone number so he can leave it with gatekeepers/customer-service alongside email | DONE per Kay 2026-04-30 |
| Kay | Add Kay's phone number to the G&B Cold Call Guide (Drive Doc `12Hqfwxg4qJA3YdZh36ndd-flvYgWNZeL8sMZ9NAHlTY`) | OPEN |
| Kay | Investigate Google Voice recording capability via Google admin (recordings disappear after the call) | OPEN |
| Kay | Plan Google Voice number swap to coincide with industry change in ~2 weeks | OPEN — Tue 2026-05-12 trigger |
| Kay | Identify next industry for JJ to pivot to once pest list exhausted (~end of week of 2026-05-04) | OPEN |
| JJ | Send rephrased voicemail / gatekeeper / main call scripts to Kay via Slack today | OPEN |
| JJ | Continue callback-week pattern: this week new list, next week callbacks, no new list | OPEN — ongoing |
| Abby | Watch for spam-flag signals (prospects saying "your number was flagged"), alert Kay if pattern emerges | OPEN — ongoing |

## Decisions

- **APPROVE:** Alternate-week cadence — new-list weeks alternating with callback-only weeks. Maximizes 4-hour shift and reduces spam-flag risk.
- **APPROVE:** Proactive Google Voice number rotation at industry changes.
- **APPROVE:** JJ's script rephrasing is encouraged, not a deviation. Kay wants the rephrased versions documented so the call guide stays current.
- **APPROVE:** JJ's gatekeeper-callback workflow (give Kay's email + phone when customer-service-reps call back) is the right pattern.

## Signals

- **Satisfaction:** High. JJ and Kay both expressed that they've moved past the "bumpy start" into a working rhythm.
- **Operating risk:** Volcano displacement near JJ's home is a recurring environmental disruption. Two-three month housing secured. Watch for further displacement.
- **Process maturity:** JJ is iterating on the script independently (positive signal); recording broken (small fix needed); number rotation planned (mature thinking).

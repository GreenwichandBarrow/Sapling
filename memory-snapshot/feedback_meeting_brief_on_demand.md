---
name: Meeting briefs are on-demand, not automated
description: Morning briefing surfaces tomorrow's external meetings with a yes/no prompt per meeting — Kay opts in, then meeting-brief skill runs
type: feedback
originSessionId: a2e3bd41-8196-410f-9e93-8ea2d33c8ee5
---
Meeting-brief-manager nightly automation is retired. Kay doesn't need a brief for every external meeting — too much noise. New flow:

1. Morning briefing (pipeline-manager) lists tomorrow's external meetings (Mon-Fri). For each: "Brief needed for [meeting]? (y/n)"
2. Kay answers yes → meeting-brief skill runs for that meeting
3. Kay answers no → skip, no artifact created

**Friday rule:** On Fridays, the prompt must cover Mon AND Tue (not just Saturday), because the weekend briefing is lighter and may not catch Monday meetings in time.

**Why:** Automated nightly briefs generated material Kay didn't use. She wants control over which meetings get prep, and the one-day-ahead cadence gives her time to review without over-automation.

**How to apply:** (1) Pipeline-manager skill must surface tomorrow's external meetings with yes/no prompt. (2) Friday mode covers Mon+Tue. (3) Meeting-brief-manager launchd plist retired — do not redeploy.

---
name: Handoff prompt date arithmetic must match event timeline
description: Evening summary "tomorrow-morning prompts" must compute tomorrow's actual date and verify referenced events will have occurred by then. Off-by-one-day bug 2026-04-25.
type: feedback
originSessionId: 8cc9b9eb-89cd-43ea-8e11-34566c18e476
---
When writing the "tomorrow-morning session prompt" at the end of a /goodnight or evening summary, compute tomorrow's literal date AND day-of-week, then verify every event the prompt asks tomorrow-me to check will actually have happened by the time tomorrow-me reads it.

**Why:** Saturday 2026-04-25 evening, past-me wrote a handoff prompt asking Sunday-morning-me to verify "last night's Sunday 10pm Phase 2 fire." But tomorrow from Saturday = Sunday, and the Sunday Phase 2 fire happens Sunday *night*, not Saturday night. The recap message in the same session correctly said "verify Monday morning" — the error was in the handoff prompt body, not the underlying model. Filename was correct (`session-decisions-2026-04-25.md`); the prose was off by one day.

**How to apply:**
- Before writing any "Good morning. Three things to start with..." block, run: `python3 -c "from datetime import datetime, timedelta; t=datetime.now()+timedelta(days=1); print(t.strftime('%A %Y-%m-%d'))"`
- For each event the prompt references (scheduled job fire, calendar block, validator output, sheet population), trace its trigger schedule against tomorrow's date. If the event hasn't fired by tomorrow morning, the prompt is verifying nothing.
- Special case: skills that fire on a specific weekday (Phase 2 = Sunday 10pm; jj-operations-sunday = Sunday 6pm; weekly-tracker = Friday). The verification window is the morning AFTER the fire, never the morning OF.
- If tomorrow is the day-of-fire (not day-after), the handoff prompt should stage the verification for the day after that, not pretend it already happened.
- Cross-check: does the recap paragraph and the handoff prompt agree on which day verification happens? If they disagree, the handoff prompt is wrong.

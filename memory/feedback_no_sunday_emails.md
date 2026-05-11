---
name: No Sunday emails — schedule for Monday
description: Kay doesn't send business emails on Sundays. Draft on Sunday, schedule to send Monday morning.
type: feedback
originSessionId: 3d944631-1e1f-43d0-88c1-6fdd795901fd
---
Never send business emails on Sunday. If drafting on a weekend, schedule to send Monday morning.

**Why:** Kay considers Sunday emails unprofessional. She wants to maintain boundaries.

**Enforcement (added 2026-04-24):** graduated to Stop-hook `.claude/hooks/router/handlers/no_sunday_send_recommendations.py` (registered in `stop.py`). Hook checks `datetime.now().weekday() == 6` (Sunday) and scans the last assistant message for send-recommendation phrases ("go ahead and send", "ready to send", "push to send", "hit send", etc.). Blocks the stop with instructions to reframe as a Monday-AM-scheduled send.

**How to apply:**
- When drafting emails on Saturday/Sunday, note "schedule for Monday AM" in the draft
- Superhuman has scheduled send — use it
- This applies to all outreach, broker replies, and follow-ups. Not internal/personal.

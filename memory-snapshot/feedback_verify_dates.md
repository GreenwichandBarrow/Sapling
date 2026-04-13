---
name: Always verify dates and days of week
description: Calendar check hook runs at session start. Never guess day-of-week, always compute.
type: feedback
originSessionId: 4343e102-b52f-48a5-b85c-73dd1784544b
---
Claude makes frequent errors on dates and days of the week. Now enforced via session start hook (calendar_check handler in .claude/hooks/router/handlers/session.py).

**Why:** Claude doesn't have reliable internal day-of-week awareness. Guessing consistently produces wrong answers. Even source data can be wrong.

**How to apply:**
- Session start hook automatically injects today's + tomorrow's calendar as context — use it, don't guess
- NEVER guess what day of the week a date falls on. Always compute: `python3 -c "from datetime import datetime; print(datetime(2026,4,14).strftime('%A'))"`
- When referencing any date, verify the day-of-week before presenting it to Kay
- Don't trust day-of-week labels in source data (sheets, event listings) without verification
- Include the day when presenting dates: "Tuesday April 14" not just "April 14"
- Never quote meeting dates from session notes without cross-referencing the calendar

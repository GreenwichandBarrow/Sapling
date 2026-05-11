---
name: Kay's morning entry point is the Cursor terminal on Mac — skip mobile-first notifications
description: Kay's first work-wise action each morning is opening the Cursor terminal and saying "good morning." All briefings/alerts render there. Don't propose mobile/phone/Slack-to-phone flows.
type: feedback
originSessionId: 79f2536c-7455-4155-bafd-6653508b83e4
---

**Rule: Kay's morning flow is — wake up → Mac → Cursor terminal → "good morning." The Cursor terminal (Claude Code) IS her morning interface. Do not propose mobile-first notifications, Slack-to-phone alerts, or pre-laptop pings.**

**Why:** Kay's explicit morning ritual: "I wake up and the first thing I do work-wise is coming to my Mac and say good morning here in the Cursor terminal." She doesn't check Slack on phone, doesn't scroll email on mobile, doesn't need heads-up pings. By the time any morning alert would fire, she's already typing at the keyboard. Mobile-first engineering solves a problem she doesn't have.

**Implication:** the morning brief IS the morning interface. Everything the system learns overnight, every artifact email-intelligence and relationship-manager pre-warm at 6:50/7am, every launchd job that completes while she's sleeping — all of it lands in the brief that renders when she says "good morning." No parallel notification stream needed.

**How to apply:**

1. **Morning brief renders in the Cursor terminal.** Not Slack, not push notifications, not email, not phone. The 4-bucket brief in Claude Code IS the morning interface.

2. **Alerts about morning-critical items (active deals, CIMs, fast-path triggers) go into the brief, not around it.** Exception: genuinely time-critical events that fire *during the day* (not morning) — e.g., a CIM landing at 2pm — can Slack to #active-deals per existing rules, because those are mid-day, not morning.

3. **Don't propose phone-first flows** unless Kay asks explicitly. If a workflow improvement starts "push this to her phone," rework it to "surface this in the brief" before proposing.

**What this does NOT cover:**
- Slack notifications during the workday (after Kay is already at laptop) — still valid per existing rules
- JJ's 10am Slack — that's for JJ on his phone, not Kay
- Evening / night-before alerts — Kay may be away from laptop, can go to phone if genuinely critical

**Source:** 2026-04-19 — Kay on the proposed 7am dropped-balls Slack alert: "NO, I DONT NEED THAT. I ALWAYS GO TO MY MAC FIRST." Followed by: "I WAKE UP AND THE FIRST THING I DO WORK WISE IS COMING TO MY MAC AND SAY GOOD MORNING HERE IN THE CURSOR TERMINAL."

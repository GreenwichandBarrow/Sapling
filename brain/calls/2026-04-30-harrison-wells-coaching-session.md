---
schema_version: 1.1.0
date: 2026-04-30
type: call
call_id: 2adfdef5-bef8-4659-bd09-8843f686c8f8
source: granola
classification_type: vendor
people: ["[[entities/harrison-wells]]"]
companies: ["[[entities/dodo-digital]]", "[[entities/greenwich-and-barrow]]"]
tags: ["date/2026-04-30", "call", "client/greenwich-and-barrow", "person/harrison-wells", "company/dodo-digital", "company/greenwich-and-barrow", "topic/ai-coaching", "topic/claude-infrastructure", "topic/dashboard", "topic/launchd-reliability", "topic/server-migration"]
---

# Harrison Wells — Coaching Session

**Date:** 2026-04-30 14:00 ET
**Attendees:** [[entities/harrison-wells|Harrison Wells]] (Dodo Digital), Kay Schneider ([[entities/greenwich-and-barrow|G&B]])
**Granola ID:** `2adfdef5-bef8-4659-bd09-8843f686c8f8`

## Context

Follow-up coaching session with Harrison after Kay's first month of self-directed Claude Code build-out. Kay caught Harrison up on what's running, what she pulled back from (in-house cold email — outsourced to DealsX), and what she added (Command Center dashboard, scheduled skills, JJ's call ops, 7 conferences a week pipeline). Harrison shifted the conversation toward server migration + reliability hardening for the scheduled jobs that fail when keys disconnect overnight.

## Notes

### What Kay built since last session
- **Conference pipeline skill** — scrapes associations, builds tracker, generates registration links weekly. Hit her 1-2 conferences/week goal across 7 niches concurrently.
- **JJ cold-call quad system** — Sun prep tabs, Mon AM Slack, daily logs, weekly sync. Two warm leads in two weeks (industry norm).
- **DealsX outsourced** — 30 domains, warming through May 7, ~1,000 emails/mo + LinkedIn going live; expecting 5-7 owner replies/week.
- **Command Center dashboard** — Streamlit, localhost:8501, organized by C-suite (Chief of Staff, CIO, CMO, CPO, GC) showing skill schedule + status + system health + tech stack inventory + credits.
- **Niche intelligence skill** — scrapes weekly Tuesday night, drops new candidates into Wednesday tracker.
- **Budget manager + nightly tracker audit + health monitor** — all on launchd cron.

### Harrison's framing of next phase
- Kay has built end-to-end. The remaining problem is **operational reliability** of overnight scheduled jobs.
- Specific failure mode: API keys disconnect, scheduled job runs, fails silently, Kay finds out next morning.
- Today's afternoon session (2pm) is to work through the reliability solutions Harrison has.

### Server migration discussion (referenced from his earlier email)
- Harrison sent a separate "Server setup guide + Tailscale" email same morning — implies he has a recommended pattern for moving Kay off Mac-dependent launchd to a proper server with Tailscale for secure access.
- Engagement scope email (sent 4:26pm same day) confirmed: month-to-month, $1,200/mo, up to 2 hours of 1:1 calls + async email channel + invoicing through Stripe.

### Kay's framing — pre-launch energy
- "I have spent a lot of time in the operations piece of it and now... I don't want to anymore. I feel like I've built everything out. It should all be running."
- Goal for end of next week: engine fully operational + first deal in the funnel.
- Recognized she missed her end-of-April deal goal but feels close on the engine-built goal.

## Action Items

- [ ] **Kay:** Review Harrison's engagement scope + invoice email and confirm/decline by his next monthly cycle (currently Apr 30 → May 30).
- [ ] **Kay:** Walk through Harrison's server setup guide + Tailscale email; decide if/when to migrate scheduled jobs off Mac.
- [ ] **Harrison:** Provide reliability hardening recommendations from afternoon 2pm follow-up session.
- [ ] **Kay:** Decide whether to renew Dodo Digital engagement at $1,200/mo for May (cancel-anytime).

## Next Steps

- Afternoon follow-up session at 2pm same day to work through scheduled-job reliability.
- Engagement renews monthly on the 1st; first cycle invoiced.

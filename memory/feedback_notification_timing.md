---
name: No nighttime notifications, all Slack at 9am
description: All work-related Slack notifications must fire at 9am ET, never overnight. Agents can run overnight but hold notifications until morning.
type: feedback
---

All Slack notifications to Kay must fire at 9:00 AM ET. Never overnight, never before 9am.

**Why:** Kay does not want work notifications disrupting personal time. Agents can process overnight but must queue notifications for morning delivery.

**How to apply:** When a skill completes overnight (e.g., niche intelligence runs Friday night), the Slack notification should be scheduled or held until 9:00 AM ET the next morning. Use `at` scheduling, cron, or hold the curl command until 9am.

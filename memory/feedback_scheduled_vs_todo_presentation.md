---
name: Scheduled jobs are not to-do items — present them differently
description: Recurring scheduled jobs (launchd, cron, plists) are self-managing and should be presented as "running" not as "next fires at..." which reads like a to-do.
type: feedback
originSessionId: 0a4c27c7-bd63-4afe-8f7c-f9b27f550e64
---
When confirming a scheduled/recurring job is set up (launchd plist, cron, hourly refresh script), present it as "wired up and running" — do NOT call out the next scheduled fire time the same way a to-do or open-loop item is surfaced. That format makes Kay mentally track the fire, which is exactly the cognitive load the schedule was meant to remove.

**Why:** Kay reads "Apollo credits → next hour Mon 4/27 8am ET" the same way she reads a to-do reminder — as something to remember and watch for. But a scheduled job is the opposite: it runs itself, she doesn't need to do anything, and it's only worth surfacing if it FAILS. Listing the next fire time adds noise to her mental queue and undercuts the whole point of automation.

**How to apply:**
- Confirming a plist/cron is loaded → "✅ wired up, runs hourly Mon-Fri" (one line, no fire-time call-out).
- Listing checkpoints / open loops / "what's left" → never include scheduled jobs unless they failed.
- "When does X next fire?" only worth surfacing if she explicitly asks, OR if a known issue means she should watch the first run.
- Apply same rule to: launchd jobs, cron entries, hourly refresh scripts, plists, anything self-firing.
- Inverse: jobs that haven't been registered (plists on disk but not loaded) ARE to-do items until activated.

---
name: goodmorning
description: Morning operating bookend for Kay and Greenwich & Barrow. Use when Kay says "good morning", invokes /goodmorning, asks for a morning briefing, or starts the daily operating rhythm. Preserves the Claude-era morning orchestration: email intelligence, relationship manager, pipeline manager, prior decisions, day-of-week overlays, Sunday tracker build, and a concise decisions-only briefing.
---

# Good Morning

## Contract

Run the morning operating system, not a generic greeting. Preserve the Claude-era `/goodmorning` behavior unless a Phase 2.5 improvement explicitly changed it.

Non-negotiables:
- Never send emails.
- Do not depend on Superhuman.
- Use 1Password-backed credentials for external services.
- Do not make scheduled jobs depend on MCP until tested.
- Do not create duplicate weekly tracker files.
- Keep the final briefing decision-oriented, with no filler.

## Morning Flow

1. Read the latest Good Night / closeout context if available.
2. Run or review `email-intelligence` and `relationship-manager` in parallel when credentials and schedules allow.
3. Cross-reference open items from `brain/session-decisions/` and recent Good Night ledgers.
4. Run or review `pipeline-manager` for deal, niche, investor, and relationship context.
5. Check Active Outreach:
   - Skip DealsX Email unless Kay explicitly re-enables it.
   - Use Kay Email and cold-call channels only.
   - Treat old `JJ` references as legacy cold-call compatibility, not current user-facing naming.
6. Verify cold-call operations fired when scheduled. Do not re-run if the job already produced a current artifact.
7. Apply day-of-week overlays.

## Day Overlays

Sunday:
- Prepare the weekly task canvas.
- Use `task-tracker-manager` and `scripts/task_tracker.py build-week` where appropriate.
- Dry-run or check for an existing current-week file before creating anything.
- Prior week files are immutable history.
- Carry incomplete prior daily tasks into the new weekly review surface.
- Do not distribute tasks into new daily tabs until Kay has reviewed/approved the week.

Monday:
- Confirm `conference-discovery` status and whether the Conference Pipeline was updated.
- Keep Slack notification tight: link + number added this week + number added future weeks.

Wednesday:
- Confirm `niche-intelligence` analyst-prep status.
- Surface any new niches that emerged from calls, email, or pipeline activity.

Friday:
- Confirm weekly tracker snapshot/export, `health-monitor`, and `calibration-workflow` status.

## Briefing Format

Return at most five ordered decisions:

```
1. 🔴 [COO] RECOMMEND: ...
   → YES / NO / DISCUSS
```

Use:
- 🔴 urgent
- 🟡 important
- 🟢 optional / monitor

Include C-suite label where useful: CEO, COO, CIO, CFO, CMO, CPO, GC, Chief of Staff.

Include:
- current blockers
- dashboard pointer only when useful
- explicit note if no email was sent

Avoid:
- raw logs
- long summaries
- unapproved execution
- burying the recommendation

## Success Criteria

The run is complete when Kay has a concise daily decision brief, scheduled/core status has been checked, Sunday tracker behavior is safe, and no unreviewed email-sending or duplicate tracker action occurred.

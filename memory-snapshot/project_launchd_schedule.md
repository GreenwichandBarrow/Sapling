# Launchd Schedule — As of March 24, 2026

| Skill | Schedule | Notes |
|-------|----------|-------|
| intermediary-manager | Mon-Fri 6am ET | Platform scanning only, no email |
| meeting-brief-manager | Sun-Thu (9pm Thu, 10pm other days) | Calendar T+2, classify, brief/prep |
| niche-intelligence | Tuesday 11pm ET | Newsletter scrape, niche ID, one-pagers, scorecards |
| weekly-tracker | Thursday 10pm ET | Weekly activity data compilation |
| calibration-workflow | Thursday 11pm ET | System calibration |
| conference-discovery | Sunday 9pm ET | Conference scanning |

## Rules
- All staggered, no overlaps
- Mac must be in sleep mode (not shut down) for scheduled runs to fire

## Deleted Jobs
- investor-update launchd — DELETED (call-prep absorbed by meeting-brief-manager)
- granola-reminder launchd — DELETED (redesigned into pipeline-manager)

## Infrastructure
- Wrapper: scripts/run-skill.sh
- Env: scripts/.env.launchd
- Logs: logs/scheduled/{skill}-{date}.log (14-day rotation)
- Plists: ~/Library/LaunchAgents/com.greenwich-barrow.{skill}.plist

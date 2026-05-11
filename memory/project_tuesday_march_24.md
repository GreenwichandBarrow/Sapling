---
name: Tuesday March 24 agenda
description: Tomorrow's priorities — MacBook setup, launchd verification, conference-manager, outreach testing
type: project
---

## Tuesday March 24, 2026 Agenda

### Morning
- Kate Reibel coffee at 9:30am, Pura Vida NoHo. Brief ready in Drive + vault.
- "Coffee w/ Robe" at 9am (not a new contact, no brief needed)

### Priorities
1. **MacBook setup** — Clone repo from GitHub on MacBook, install Claude Code, auto-commit hooks handle syncing between machines. No manual push/pull needed. Per Harrison (3/13 session): "both connect to GitHub, it handles all the syncing for you."
2. **Verify launchd jobs** — `launchctl list | grep greenwich` to check if scheduled skills are loaded. If not, load them. Test with `launchctl start`. Harrison confirmed the approach works if machine stays on (sleep mode OK).
3. **Conference-manager** — Should run Mondays. Check if its launchd plist exists and is loaded. If not, create and load it.
4. **Continue outreach testing** — Test "Direct" variant with a second TCI target. Test the full Day 3 flow (reply check → JJ call prep → Slack).
5. **IPLC target sheet** — Still needs to be created. Pipeline-manager should detect Active status and trigger target-discovery.

### Harrison's Key Points (from 3/23 email)
- Cron/launchd requires machine always on. Desktop in sleep mode works. Laptop that closes does not.
- Consider a small server for both machines to schedule from.
- `claude -p "prompt" --dangerously-skip-permissions` is the non-interactive command.
- Run manually first, review output, then schedule.
- Full cron: `0 23 * * 2 cd /path/to/project && claude -p "prompt" --dangerously-skip-permissions`

**Why:** Harrison is the AI consultant guiding the build. His recommendations are authoritative for infrastructure decisions.

**How to apply:** Verify all launchd jobs Tuesday morning before moving to outreach testing. MacBook setup is a prerequisite for Kay working on the road this week.

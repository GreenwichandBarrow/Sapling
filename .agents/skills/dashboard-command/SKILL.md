---
name: dashboard-command
description: Dashboard status and recovery command for the Greenwich & Barrow command center. Use when Kay invokes /dashboard, asks for the dashboard link, asks whether the dashboard is healthy, or reports dashboard connection/staleness issues. Preserves the Claude-era dashboard command behavior.
---

# Dashboard Command

Use this skill for dashboard link, health, and recovery work.

Canonical dashboard:

`https://agent-vps-7731c88b.tail868ef9.ts.net/`

## Health Check

On the VPS, check:
- dashboard service status
- local smoke test
- recent logs
- data freshness markers

Preferred checks:
- `systemctl --user is-active dashboard.service`
- `systemctl --user status dashboard.service`
- local HTTP smoke test against the configured dashboard port

## Recovery

If the dashboard is down:
1. Restart the dashboard service once.
2. Re-check service status and local smoke test.
3. Report the result.

Do not:
- recreate the virtual environment without asking
- rewrite dashboard data plumbing during a simple health check
- confuse Tailscale/VPS connectivity with dashboard application failure

## Output

Keep the user-facing result concise:
- dashboard URL
- healthy / degraded / down
- what was restarted, if anything
- next action if still broken

## Success Criteria

Kay can use the dashboard as the G&B command center, and dashboard failures are diagnosed without unnecessary repo or environment churn.

---
name: Repeated scheduled-skill fails must surface proactively
description: Health-monitor must catch 2+ consecutive scheduled-skill failures and surface in morning briefing, not rely on Slack fail notifications
type: feedback
originSessionId: a2e3bd41-8196-410f-9e93-8ea2d33c8ee5
---
If a scheduled skill fails 2+ nights in a row, the morning briefing must surface it as a RED system-health item. Slack per-fail notifications exist but get lost; Kay should not have to screenshot a Slack message to tell Claude there's a pattern.

**Why:** Apr 10+11 2026 — nightly-tracker-audit failed two nights in a row with Claude CLI "Unexpected error." Claude did not catch it in the Sunday morning health review; Kay had to screenshot the Slack fails. Also: email-intelligence was listed in CLAUDE.md scheduled skills table but never had a plist deployed — health-monitor should have caught that drift too.

**How to apply:** When running health-monitor or any system-health check, always (1) grep last 7 days of `logs/scheduled/` for `exit: [1-9]` and flag any skill with 2+ consecutive fails, (2) cross-reference launchctl output against CLAUDE.md's scheduled skills table and flag any missing plist. Both are RED findings, not warnings.

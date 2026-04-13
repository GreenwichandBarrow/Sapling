---
name: Slack Webhooks for Notifications
description: Slack incoming webhooks (3 channels) stored as env vars — operations, active deals, SVA. All rotated 2026-03-19.
type: reference
---

Slack incoming webhooks for Claude Assistant notifications. **All URLs stored as env vars in ~/.zshrc — never hardcode.**

- **Workspace:** G&B (Slack Pro)
- **App name:** Claude Assistant

## Operations Webhook (#operations)
- **Env var:** `$SLACK_WEBHOOK_OPERATIONS`
- **Channel:** #operations (Kay's main notification channel)
- **Purpose:** Workflow completions — niche intel, weekly tracker, meeting briefs, pipeline updates
- **Rotated:** 2026-03-19

**Usage:**
```bash
curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
  -H "Content-Type: application/json" \
  -d '{"text":"Your message here"}'
```

## Active Deals Webhook (#strategy-active-deals)
- **Env var:** `$SLACK_WEBHOOK_ACTIVE_DEALS`
- **Channel:** #strategy-active-deals
- **Purpose:** Deal evaluation deliverables — Thumbs Up/Down deck, scorecard results, deal updates for Kay + analyst
- **Rotated:** 2026-03-19

## JJ / SVA Webhook (#operations-sva)
- **Env var:** `$SLACK_WEBHOOK_SVA`
- **Channel:** #operations-sva
- **Purpose:** JJ's daily call list from pipeline-manager
- **Rotated:** 2026-03-19

**When to use which:**
- **Operations** — workflow completions, system notifications to Kay
- **Active Deals** — deal evaluation deliverables for Kay + analyst
- **SVA** — JJ's daily tasks and call lists

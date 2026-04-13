---
name: Linkt Subscription Downgraded, API Key Needs Refresh
description: Linkt on Starter tier, API key invalid as of 2026-03-31. Kay must get new key from Linkt dashboard.
type: feedback
---

## Linkt Subscription Status

Linkt **downgraded to Starter tier** (NOT cancelled) as of March 31, 2026. Was on Pro plan ($300/mo, 300 credits/mo).

**API key is INVALID** as of 2026-03-31. The downgrade likely rotated the key. Kay needs to:
1. Log into app.linkt.ai
2. Get the current API key from account settings
3. Paste via `! cat > /tmp/linkt_key` then update `scripts/.env.launchd`

**Going forward:** Upgrade to Pro in sprints when actively running target discovery. Run full E2E test via MCP first before burning credits on real searches.

**Final Pro session:** 263 credits available, 96 burned on Art Insurance (only successful search), 4 other ICPs failed due to platform bug.

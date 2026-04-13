---
name: Outreach manager end-to-end test
description: Full outreach-manager test session 3/23, all fixes applied, Kirk Elken draft sent, A/B test wired, Apollo email verification added
type: project
---

## Session: March 23, 2026

### Outreach Manager Test — End to End

Tested the full chain: niche-intelligence → pipeline-manager → target-discovery → outreach-manager.

**Fixes applied during testing:**

1. **Superhuman draft method** — Line 226 was using MCP tool, fixed to CLI everywhere. Created `~/.local/bin/superhuman-draft.sh` wrapper that handles launch, token refresh, and draft creation. All skills updated to use wrapper.

2. **JJ call sheet location** — drive-locations.md said separate sheet, skill said master sheet columns Q-T. Fixed to master sheet (correct).

3. **One-pager titles invisible** — Generated one-pagers had title text but no `solidFill` color (rendered white on white). Fixed all 5 March 2026 one-pagers in Drive. Updated sub-agents.md generation instructions. Template reference updated to point to G&B Master Templates Drive ID.

4. **Target-discovery was writing to Attio prematurely** — Creating CRM records before Kay approved. Fixed: target-discovery is now read-only on Attio. Outreach-manager creates Attio records after approval.

5. **Outreach-manager Attio flow** — Single lookup does both dedup AND warm intro check. If found → warm intro. If not found → create and proceed cold.

6. **Pipeline-manager meeting brief trigger** — Hook wasn't mentioning calendar scan. Fixed `pipeline.py` to explicitly say "scan tomorrow's calendar." Also fixed lookahead from "2 days ahead" to "tomorrow" (Fridays also scan Monday).

7. **Pipeline-manager reply check before JJ calls** — Added Gmail reply check before building JJ's call list. If owner replied, JJ call is canceled.

8. **Pipeline-manager trigger** — Updated from "session start" to "good morning" trigger.

### New Capabilities Added

- **A/B email test** — Two variants: "Learning" (curiosity-first) and "Direct" (well-capitalized buyer). Alternating on cold targets, logged in Col Z. Calibration agent analyzes after 20-30 sends. Warm intros excluded.
- **Apollo.io email verification** — Free tier API (50 credits/month). Verifies non-Linkt target emails before drafting. Stored in `.env` as `APOLLO_API_KEY`. Added to Tech Stack Inventory as free tool.
- **Email voice calibration** — 5 new feedback memories: no revenue in outreach, never say "fund", outreach about THEM, no strategy leaks, no fake lines.

### Test Target: Kirk Elken (Securitas Global Risk Solutions)

- Attio: company + person created at "Identified" stage
- Superhuman: draft created (Learning variant)
- Target sheet: Col O=Approve, Q=Not Called, R=3/25/2026, X=blank, Y=Email Drafted, Z=Learning
- Slack: notification sent to #operations
- Call log: created for JJ with customized script

### Meeting Brief: Kate Reibel (3/24)

- Discovered pipeline-manager wasn't triggering meeting briefs (hook didn't mention calendar scan)
- Fixed the hook, ran meeting-brief manually
- Google Doc + vault file + 3 entity files created
- Slack notification sent

### Remaining Items

- Superhuman draft formatting needs G&B letterhead as native Google Doc template (current is .docx, can't be copied via API)
- IPLC niche has no target sheet yet (Active on tracker but no Linkt ICP created)
- Drive-locations reference in outreach-manager still has old archived sheet IDs
- Test the "Direct" variant with a second target
- Test conference outreach and intermediary outreach subagents

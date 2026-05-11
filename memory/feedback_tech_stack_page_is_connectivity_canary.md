---
name: Tech Stack page is a connectivity canary, not a reference list
description: Command Center's Tech Stack page primary purpose is monitoring external-service connectivity (OAuth/API/MCP), credit balances, and usage trends — not a static inventory. Same silent-failure-catching pattern as the C-Suite & Skills page.
type: feedback
originSessionId: ebd58436-6958-4e18-98eb-a6797b0d0b46
---
The Command Center's Tech Stack page is operational monitoring, not a reference list.

**Why:** 4/24 dashboard scope session — I initially scoped this as a monthly-reconcile tile showing runway + token burn, citing `feedback_budget_not_kays_job.md`. Kay corrected: "we need to monitor credits / usage and connectivity." Same mistake I made on the C-Suite & Skills page — under-scoping by treating silent-failure domains as static data.

**Page design (top-to-bottom):**
1. **Connectivity canary (primary):** per-service auth + health status — Superhuman OAuth, Attio MCP, Apollo API, gog CLI, Granola, Slack webhooks, Claude API, GitHub. Each shows last successful operation + time since. 🟢 healthy / 🟡 stale / 🔴 broken.
2. **Credit / usage trends (secondary):** Claude token burn, Apollo credits, Linkt credits (through 2026-05-30), subscription cost variance from prior month.
3. **Reference list (tertiary):** the full stack inventory, tucked below.

**Meta-pattern across the dashboard:** Kay's core concern isn't vanity metrics — it's **silent failures**. Any surface where things fail without screaming (launchd skills, OAuth tokens, MCP servers, API credits, webhooks) deserves a daily canary, not a weekly-or-monthly reference. When scoping any dashboard page, ask first: "what fails silently here?" — that's the page's load-bearing job.

**How to apply:**
- Treat Tech Stack's purpose as "am I still connected to everything?" not "what's my stack?"
- `feedback_budget_not_kays_job.md` still holds for monthly reconcile — Anthony handles P&L — but CONNECTIVITY and subscription-creep alerts are Kay's concern because they block her operations, not Anthony's books.
- Connectivity health overlaps with Infrastructure's system-health signal. Split: Tech Stack = external dependencies, Infrastructure = internal data/pipeline integrity, C-Suite & Skills = scheduled skill fires. Three distinct failure domains, three distinct canaries.

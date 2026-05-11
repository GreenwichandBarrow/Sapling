---
name: Outreach stack decision — Salesforge disconnected, evaluating alternatives
description: Salesforge caused spam, disconnected April 5. Reply.io trial also expiring. Evaluating personal-send (4-6/day) vs outsourced (DealsX, Austin's tool).
type: project
---

Decision made April 3, 2026 after extensive stack exploration.

**Final stack:**
- Apollo Basic ($64/mo) — list building + company discovery + email verification
- Salesforge Growth ($80/mo) — email sequencing + LinkedIn DMs + built-in warmup + email verification (1,000 credits/mo) + API for Claude + Attio bidirectional sync
- Attio (free) — CRM, pipeline tracking, Claude MCP interface
- Superhuman (existing) — personal/warm email client
- Total new spend: $144/mo

**Why Salesforge over Reply.io ($59/mo):**
- LinkedIn DMs built into sequences (Reply.io was $69/mo add-on)
- AI-native (Agent Frank — autonomous AI SDR option)
- Native Attio integration (bidirectional contact + engagement sync)
- Built-in email warmup (Warmforge)
- 1,000 email verification credits/mo on Growth
- API access on Growth for Claude automation

**Why not Mixmax:** No LinkedIn integration. Email-only.

**Why not stay with Reply.io:** No Attio integration, no LinkedIn without $69 add-on, not AI-native.

**Key architectural insight:** Attio automations CANNOT trigger Salesforge sequences. Claude must use Salesforge API directly to add contacts to sequences. The Attio-Salesforge integration is for contact sync + engagement data only.

**UPDATE April 5, 2026:** Salesforge caused spam. Kay deleted mailbox + LinkedIn from Salesforge, blocked Google Admin access, removed MCP config. Fully disconnected. Trial still active (~11 days) but no intention to reconnect without re-evaluation.

**Action:** Cancel Reply.io trial before ~Apr 15 charge. Decide on outreach model: personal send (Claude drafts in Superhuman, Kay sends 5/day) vs outsourced tool (DealsX, ask Austin Yoder what he uses).

**How to apply:** Do NOT rebuild outreach-manager around Salesforge or any mass tool until Kay decides. Default to personal-send workflow via Superhuman drafts.

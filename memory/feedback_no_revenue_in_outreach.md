---
name: Never reference revenue or financial metrics in outreach
description: Never include revenue, employee count, or financial figures in cold outreach emails to owners
type: feedback
originSessionId: 3d944631-1e1f-43d0-88c1-6fdd795901fd
---
Never reference revenue numbers, employee counts, or any financial metrics in outreach emails to owners.

**Why:** Two reasons: (1) the number could be wrong and you look careless, (2) it signals you're focused on the money, not the person, their business, or their legacy. That's not Kay's approach — she leads with genuine curiosity and respect for what the owner has built.

**Enforcement (added 2026-04-24):** graduated to PreToolUse hook `.claude/hooks/router/handlers/no_revenue_in_outreach.py` (registered in `pre_tool_use.py`, matcher `^Bash$`). Hook fires on `superhuman-draft.sh` invocations and scans the `--body` argument for owner-addressed financial patterns (`your $XM`, `your N employees`, `your revenue`, `your EBITDA`, etc.). Carve-out: Kay's own first-person buy-box language ("I am looking to acquire... ~$2-5M EBITDA...") is allowed because it describes her acquisition criteria, not the recipient's numbers. Blocks the send with exit code 2.

**How to apply:** When drafting any outreach (cold, warm, conference, intermediary), reference what makes the business special operationally — their reputation, longevity, specialization, independence — never their financials. Revenue/employee data is for internal scoring only.

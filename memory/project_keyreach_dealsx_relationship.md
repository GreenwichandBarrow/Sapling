---
name: KeyReach is covered by DealsX, not a separate line item
description: KeyReach is the outreach platform DealsX uses on Kay's behalf. Kay has her own KeyReach account (signed in 2026-05-10) but it is free — covered by the $1.5K/mo DealsX vendor fee. KeyReach must not be counted as separate burn or proposed for cutting in tech-audit.
type: project
originSessionId: 04c0c7a4-2876-4d40-bd0b-bb8d3584be53
---
KeyReach is the outreach platform that DealsX (Sam Singh's service) uses to run
email + LinkedIn DM sequences on Kay's behalf. Kay created her own KeyReach
account on 2026-05-10 so she can see the work directly — that account is free.
The platform cost is covered by the $1.5K/mo DealsX vendor fee.

**Why:** Without this fact, three things go wrong:
1. `/budget tech-audit` could propose cutting KeyReach as low-spend low-usage
   (it shows in the inventory but has no associated billing).
2. `/budget monthly` runway/burn math could accidentally add KeyReach as a
   separate cost when it should stay zero.
3. A future agent looking at the dashboard's `tech_stack.yaml` could ask
   "why is KeyReach listed but not in any P&L" — the answer is that DealsX
   pays for it as part of their service delivery.

**How to apply:**
- Treat KeyReach as a zero-cost tracked-only entry in the tech stack.
- Treat the $1.5K/mo DealsX line as the line item that covers both DealsX's
  labor and KeyReach access. They are not separable.
- If DealsX engagement ends, KeyReach access ends too — propose removing
  the entry, not cutting it as a saving.
- If Kay ever upgrades to her own paid KeyReach account independent of
  DealsX, this memory is stale — update it then.

Source: 2026-05-10 conversation where Kay added KeyReach to the tech stack
and confirmed "Hey reach is free for the foreseeable future. it is covered
by dealsx, I just needed to make my own account."

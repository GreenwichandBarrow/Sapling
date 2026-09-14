---
name: Budget Manager Skill Build
description: Budget-manager skill built 2026-03-23, refined same day — COA aligned, investor format locked, tech audit monthly during sprint
type: project
---

**Built:** 2026-03-23
**Skill:** `.claude/skills/budget-manager/SKILL.md` with 4 modes (monthly, runway, tech-audit, transition)

**Current instructions (September 11 discussion plus September 12 CFO follow-up):**
- $42K allocated to operations, $38K to diligence, contingency exhausted; not verified September bank cash.
- Fund period: February 7, 2025 through February 7, 2027. Use anniversary years, not calendar years.
- Rent ended August 31; $2K deposit pending receipt. DealsX prior pause is a forward assumption pending vendor confirmation; September 12 follow-up corrects unpaid invoices to $3,220. Avoid double-counting balances already net of these items.
- September 12 payroll cadence scenarios were discussed, but none chosen or executed; annual salary remains unchanged and skipped weeks would have no catch-up intended. No diligence reserve release authorized.
- Read `brain/outputs/2026-09-12-budget-runway-followup-aug-2026.md` before using older scenarios: rebuilt monthly forecast $20,388.75 before interest supersedes $19,635.76. Actual September cash and payroll cutoff remain unverified.

**Historical Fund Position (as of Feb 28, 2026; superseded for current planning):**
- Cash: $255,724 (46.3% of $551,825)
- DD Reserve then: $40K (current clarified allocation is $38K)
- Available for ops: $215,724
- Target burn: $17,300/month (11 months to Feb 2027 deadline)
- Current steady-state: $19,000-22,000/month
- Gap to close: $2,000-5,000/month

**Why:** Jan/Feb 2026 burn was $31K/month (inflated by $17K health insurance installments + $3.2K CPA annual). Post those one-time items, steady-state drops to $19-22K. Need tech/database/bookkeeper cuts to hit $17.3K target.

**How:** Budget Dashboard Google Sheet replaces broken Excel tracker. Monthly P&L from bookkeeper ingested, reconciled vs approved budget, runway calculated, variances flagged. Feeds investor-update skill.

**Refinements (2026-03-23 evening session):**
- COA alignment: example JSON keys now match actual QBO chart of accounts from brain/context/budget.md
- Tech audit frequency: monthly during active search sprint (was quarterly)
- Investor format: one inline bullet only — `$XXXK (XX% remaining of $550K raised) [context]`. No burn rate, runway, or DD reserve in investor decks. Those are internal CFO brief numbers only.
- First live test: April, when Anthony delivers March close

**Key decisions:**
- Health insurance: $33K/yr unbudgeted, paid in installments, one left
- DD reserve: current $38K after the September 11 original-budget clarification. No automatic LOI-stage escalation.
- Overseas support previously $2,500/mo (Jul-Dec 2025), replaced by JJ at $1,040/mo
- JJ: 2-3 week cold calling evaluation starting now. If subpar, find cheaper alternative.
- Bookkeeper: transition to Kick + Claude by June 2026 ($247/mo savings)
- Salary: $12,692/mo non-negotiable (investors suggested skipping months, Kay cannot)
- Rent: $1K/mo, open to giving up desk but strategic value (co-located investors, potential tech acquisition)
- Investor extension: would rather not test that hypothesis
- Kay has related budget tasks already set up in Motion

**Next steps:**
- Phase 3: Wire investor-update to read from Budget Dashboard
- Phase 4: Run tech stack audit for savings (monthly during sprint)
- Phase 5: Bookkeeper transition (April start)

---
name: Weekly Tracker Skill Status
description: Current state of the weekly-tracker skill build, test results, issues found, and next steps as of 2026-03-17
type: project
---

## Weekly Activity Tracker — Build Status (2026-03-17)

**Skill:** `.claude/skills/weekly-tracker/SKILL.md` — fully built, user-invocable via `/weekly-tracker`

### Architecture
- 4 parallel sub-agents: Gmail, Calendar/Granola, Attio, Vault
- Validation stop hook before Slack notification
- Slack notification with 4 key metrics + Sheet link
- Saves to Google Sheet (3 tabs) + vault snapshot

### Design Decisions
- **3-tab sheet structure:** Kay wanted separate views — Topline (4 key metrics), Detail (diagnostic), Quarterly Summary (investor)
- **Metrics not split by role:** Kay explicitly said not to split JJ/CEO — track the search funnel as a whole since JJ's scope is changing
- **Key metrics:** NDAs signed, financials received, LOIs submitted, LOIs signed — everything else is diagnostic
- **Goal framing:** 1 interesting deal/week, fed by 2-5 owner conversations/week
- **Stage 7 framing:** Tracker maps to "Model Updating" from G&B acquisition methodology — System Throughput (volume) + Signal Quality (conversion)
- **Investor quarterly view:** Cumulative totals and conversion funnels, not weekly noise — designed to feed quarterly investor updates

### Test Run Results (2026-03-17, partial week)
- Gmail: 2 outreach, 0 cold calls, 3 responses
- Calendar: 0 Stage 1, 0 Stage 2, 2 networking meetings
- Attio: 44 active pipeline, 1 at Financials Received
- Vault: 0 call notes, 0 new entities
- Sheet populated, vault snapshot saved, Slack sent — all validation passed

### Issues Found & Fixed
1. **Attio agent incomplete data** — only reported stages with deals, missed empty stages. FIXED: skill now has explicit stage mapping and uses `/attributes/stage/statuses` endpoint
2. **.env sourcing flaky** — caused auth errors. Needs clean test on Friday
3. **Attio reference was missing stage config** — FIXED: all 10 Active Deals stages now documented in reference_attio.md

### Next Steps
- **Friday 2026-03-20:** Clean full run to validate end-to-end
- **Pipeline management workflow:** Kay flagged herself as bottleneck on updating Attio stages. Need to build a lightweight process for moving deals through stages.
- **Kay may style the sheet** — formatting won't break the skill (writes by cell range, doesn't touch formatting)

**Why:** Kay wants an automated weekly pulse on the search. The tracker replaces manual Excel tracking and feeds the quarterly investor report. Pipeline management is the prerequisite — if Attio stages aren't current, the tracker outputs garbage.

**How to apply:** Run `/weekly-tracker` every Friday. Pipeline management workflow should be built next to ensure Attio data quality.

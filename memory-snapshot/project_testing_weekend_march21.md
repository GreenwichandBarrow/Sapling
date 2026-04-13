---
name: Testing Weekend March 21-22
description: Full testing weekend status — skills tested, improvements made, blockers, what's next for morning
type: project
---

## Testing Status (end of day 2026-03-21)

| Skill | Status | Notes |
|-------|--------|-------|
| Niche Intelligence | TESTED + MAJOR UPGRADES | 2-track, pattern recognizer, niche inbox, Attio dedup |
| Target Discovery | TESTED | Domestic TCI (17 targets), Export TCI (4 targets), Premium Audit (15 targets). Contact scraping done. |
| Pipeline Manager | UPDATED | Active sprint detection, nightly sort, Tabled/Killed auto-move, nightly audit stop hooks |
| Outreach Manager | LOADED, NOT TESTED | Superhuman MCP re-added but auth not verified. Next to test. |
| Deal Evaluation | Tested Mar 20 | Working |
| /start (today) | Tested Mar 20 | Working |
| Weekly Tracker | IN PROGRESS | Needs fixes |
| Meeting Brief | NOT TESTED | |
| Conference Discovery | NOT TESTED | |
| Investor Update | NOT TESTED | |
| Calibration | NOT TESTED | |

## Blockers for Monday
- Linkt credits at -29 — must replenish
- Superhuman MCP auth needs verification (/mcp reconnect)
- OneNote getPage bug — returns wrong content
- LinkedIn contacts → Attio (Motion task created, due Monday)
- Securitas Global needs classification (domestic vs export TCI)
- Unknown TCI companies (no websites) need verification — likely too small

## Architecture Changes Made Today
1. IDEATION tab eliminated → all niches to WEEKLY REVIEW with status "New"
2. TCI split into Domestic TCI + Export TCI (separate target lists, separate WEEKLY REVIEW entries)
3. Niche inbox system for ad-hoc niche ideas
4. Pattern Recognizer (Step 1b) between gathering and identification
5. Attio dedup / outreach routing flags
6. Orange header convention (agent-trigger columns)
7. Status dropdown lifecycle: New → Under Review → Active → Wind-Down → Tabled → Killed
8. Pipeline-manager nightly audit: sort, move Tabled/Killed, detect Active sprints
9. Target list sheets cloned from template (preserves dropdowns)
10. Column ownership: Kay: Decision/Pass Reason, Agent Notes, JJ: Call columns
11. Agent never writes to Kay's columns
12. Contact scraping as Step 2b (don't burn Linkt credits on enrichment)
13. Stop hook on missing contacts before outreach handoff

## Key Feedback Rules Added Today
- No carve-outs (investor-rejected)
- No lending businesses (too much liability)
- Flag rejections alongside leads in call mining
- Signals are triggers, not validation
- Never add raw niches to WEEKLY REVIEW (must go through pipeline)
- WEEKLY REVIEW grows, never auto-removes
- Orange header = agent-trigger column
- Niches must be specific angles, not broad industries
- Linkt for discovery only, not enriching external finds

## Open Items for Morning
1. Verify Superhuman MCP connection → test outreach-manager
2. Securitas Global — classify domestic vs export
3. Clean blank rows from Domestic TCI sheet
4. Continue skill testing: outreach-manager, meeting-brief, conference-discovery
5. Project Restoration CIM still needs Kay's review
6. Workplace H&S Compliance — Kay's ruling on distinct from killed Compliance E-Learning

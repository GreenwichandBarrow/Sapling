---
name: Niche Intelligence Pipeline — March 21 Test + Architecture
description: Full pipeline tested 2026-03-21 with major architecture changes. 2-track gathering, pattern recognizer, niche inbox, single WEEKLY REVIEW tab.
type: project
---

## Architecture (Updated 2026-03-21)

```
Step 1:  GATHER (parallel)       → RECENT (6 sources, 14 days) + HISTORICAL (orchestrator + 4 sub-agents)
Step 1b: SYNTHESIZE (sequential) → Pattern recognizer: cross-source matrix, company registry with Attio dedup, contact map, lead lifecycle, convergence report
Step 2:  IDENTIFY (sequential)   → New niche candidates (reads synthesis, not raw posts)
Step 3:  ONE-PAGER (parallel)    → pptx deliverables
Step 4:  SCORE (sequential)      → Industry scorecard + final report
Step 5:  UPDATE (sequential)     → Add to WEEKLY REVIEW with status "New" + Slack notification
```

## Key Changes from March 17 Test
1. IDEATION tab eliminated — all output goes to WEEKLY REVIEW with status "New"
2. 2-track gathering (RECENT + HISTORICAL) replaces 5-7 individual agents
3. Pattern Recognizer (Step 1b) added between gathering and identification
4. Niche inbox system — any source feeds ideas via brain/inbox/ with topic/niche-signal tag
5. `/niche-intelligence --from-inbox` processes ad-hoc niche ideas through Steps 2-5
6. Attio dedup / outreach routing flags on company registry (ACTIVE_DEAL, IN_CRM, WARM_INTRO, VAULT_HISTORY, NEW_TARGET)
7. Signals vs validation rule — contacts trigger investigation, data drives scores
8. "Fit for Kay" criteria added to identifier (would she operate this 5-7 years?)
9. Lead lifecycle tracking — dead ideas can't resurface as live recommendations

## Test Results (March 21)
- 3 niches scored: Premium Audit (2.32), Surplus Lines (2.65), Workplace H&S (2.51)
- 2 one-pagers created, 1 existing
- Tracker updated, Surplus Lines promoted to WEEKLY REVIEW
- All steps completed end-to-end

## Drive Structure
| Subfolder | Folder ID |
|-----------|-----------|
| WEEKLY REVIEW | `1eq7FjekjFhkV0RoBfgr9n6AXPtENEenT` |
| IDEATION (archived) | `1fQNl6mogJW-6u5XJeE5uYQGsDPx495_O` |
| TABLED | `1_k_c1F11ZNrv4MilATFrURLHdkNx0kRx` |
| KILLED | `19xsNk5KTVHF2jb6m_li8IAGjcw34nlMX` |

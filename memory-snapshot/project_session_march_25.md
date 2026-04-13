---
name: Session Summary — March 25, 2026
description: Full day session: morning workflow, scorecard architecture, niche-intel updates, MacBook setup, outreach workflow refinement
type: project
---

## Morning Workflow
- /start ran (daily note, 2 sub-agents). Pipeline-manager didn't fire (no email-scan-results).
- Motion API key rotated (old expired). 9 tasks created including address change cascade.
- UPS Store mailbox closing April 1, switching business address to home (mixed-use building).
- CorpNet dropped — Kay filing annual report directly, already in Motion for May 15.

## Niche Intelligence
- Tuesday night run fired successfully. 3 new niches scored (IMO/FMO 2.37, HNW Personal Lines 2.49, Insurance Back-Office 2.17).
- Per-niche scorecard xlsx architecture designed and implemented. Each niche gets own xlsx from G&B template in its Drive folder.
- 8 scorecards created (4 new niches + 4 legacy top-5). All 9 WEEKLY REVIEW folders now have one-pager + scorecard.
- Art Advisory created as #1 priority (score 2.73, highest ever). One-pager + scorecard + Drive folder.
- Tracker QSBS and Target Pool columns backfilled for all legacy rows.
- Pipeline: new niches go directly to WEEKLY REVIEW (not IDEATION first). Drive folders in WEEKLY REVIEW subfolder.
- Pre-notification stop hook added: verify all deliverables before Slack notification.
- Slack channel changed from #operations to #strategy-operations for niche-intel notifications.

## Fixes Applied
- Intermediary-manager: 1 Slack notification per deal (not batched). Results file added.
- 6 launchd plists routed through run-skill.sh (timestamped logging).
- GitHub push unblocked (217 commits). Webhooks already scrubbed in prior session.
- One-pager bullets fixed (double-bullet bug from python-pptx).
- "Kay" references removed from all one-pagers and skill instructions. Use "G&B" instead.
- Art Advisory risk bullet corrected per Deloitte report (allocation %, not advisory demand).
- Draft calibration loop added to calibration-workflow + pipeline-manager.

## MacBook Setup (Complete)
- Claude Code installed, repo cloned, git pulled (current)
- .env.launchd copied via OneNote/clipboard bridge
- openpyxl + python-pptx installed
- gog authenticated
- No launchd on MacBook — scheduled runs stay on desktop

## Outreach Workflow Updates (from call debrief)
- Howie scheduling: JJ emails barrie@greenwichandbarrow.com when owner wants to schedule
- Camilla added as target list approver (Col O: Kay/Camilla: Decision)
- Volume tracking added to weekly-tracker (daily average, flag if >6 or <3)

## Investor Call Preps
- Jeff Stevens + Guillermo Lavergne preps rewritten to short format (Productivity, Deal Flow, Thesis, Outlook, Discuss)
- Jeff: Ruby Au connection, Beacon sourcing resource
- Guillermo: transcript null (Granola didn't capture)

## Calls Reviewed (3 of 4)
- JJ: cadence confirmed (email → 3-4 day wait → call), scheduling via Howie, feedback via Slack
- Camilla: tracker walkthrough, niche review, approver role, impressed by system
- Jeff: conferences 1-2/week, AI investment endorsed, Ruby Au recommendation

## Late Session Additions
- "Ideation" status added to tracker dropdown — deprioritized niches sort to bottom of WEEKLY REVIEW
- Pipeline-manager nightly sort order updated: Active → Under Review → New → Wind-Down → Ideation

## Open Items for Next Session
- Attio Identified companies (37) need to be cross-referenced to target sheets + enriched
- Guillermo transcript to review when available
- Conference-discovery test still pending
- Col O header on Google Sheet needs updating to "Kay/Camilla: Decision"
- Call debrief discussion on cadence improvements (mostly confirmed existing system works)
- Ruby Au (Succession Story) connection via Jeff Stevens
- Beacon sourcing resource contact from Jeff

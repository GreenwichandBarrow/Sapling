# Architecture Optimization — March 24, 2026

## meeting-brief-manager (NEW)
- Unified skill replacing meeting-brief + investor-update call-prep
- Runs Sun-Thu at 9-10pm via launchd
- 2 subagents: External Brief + Investor Call Prep

## Email Scanning Consolidation
- Consolidated to pipeline-manager
- Writes brain/context/email-scan-results-{date}.md
- /start removed email scanner (now 2 sub-agents)
- Intermediary-manager removed Channel 2
- Outreach-manager removed delivery tracking

## investor-update Changes
- Reduced to 2 modes (quarterly + weekly-dd)
- Call-prep absorbed by meeting-brief-manager

## Granola Reminder Redesign
- Old: launchd every-5-min script
- New: pipeline-manager calendar scan + /start daily note reminder
- No more separate script/launchd job

## Pipeline-manager CIM Auto-trigger
- Detects CIM attachments in email
- Auto-creates deal folder, files CIM, creates inbox item
- Invokes deal-evaluation automatically

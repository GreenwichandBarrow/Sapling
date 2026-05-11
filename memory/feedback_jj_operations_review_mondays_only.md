---
name: JJ-operations Claude-side oversight is Monday-only
description: JJ's daily shift (Mon-Fri 10am-2pm) runs self-managed; Claude-side pace review, Slack-post monitoring, and operational oversight of JJ batch on Mondays only
type: feedback
originSessionId: 3d944631-1e1f-43d0-88c1-6fdd795901fd
---
JJ operates his own cold-call shift Mon-Fri 10am-2pm ET. The daily 10 AM Slack call-log post to JJ is a scheduled skill that runs and self-manages — Claude does NOT need to verify/monitor it daily. Claude-side oversight of JJ-operations (pace analysis, attendance check, Slack-post confirmation, harvest of prior week's call logs, master-sheet reconciliation) batches to Mondays only.

**Why:** Watching JJ every morning is decision-fatigue for Kay (creates daily surface for a self-running loop) and busywork for Claude (nothing to action on 4 of 5 days). JJ's cadence is a weekly rhythm — one review per week on Monday is sufficient to catch pace drift, attendance gaps, or Slack-post failures. The 4/23 pace analysis mistakes (tab-grouping → Col-U-as-last-touch → actual schema fix) confirmed that JJ analysis benefits from batching a full week of data, not eye-balling day-by-day.

**How to apply:** Do NOT include "Monitor JJ 10 AM Slack post" as a daily autonomous-work item or a daily System Status line. The System Status line `jj-operations: [status]` can stay in daily briefings (1 line) — that's passive surfacing, not active monitoring. Only escalate if the Slack post is missing 2+ consecutive weekdays OR JJ flags a problem in his own message. Active pace/attendance/harvest analysis happens Monday only, same cadence as conference-discovery overlay. If Kay asks about JJ mid-week, handle then — do not auto-surface.

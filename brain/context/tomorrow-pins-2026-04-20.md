---
date: 2026-04-20
type: context
title: "Tomorrow Pins — 2026-04-20 (Monday)"
saved_at: 2026-04-17T13:00:00Z
tags: ["date/2026-04-20", "context", "topic/pins"]
---

## Monday priority — resume Q1 FY2026 investor update prep

Kay set Fri 4/17 aside to get to inbox zero, deal flow, and Fri review skills. Q1 prep is paused until Mon 4/20.

### State as of Fri 4/17 end-of-day
- **Data collector (Sub-Agent 1) ran 4/17 afternoon.** Output: `brain/context/q1-2026-mulling-pack.md` (Q1 metrics, pipeline, niches, calls, strategic pivots, Q4 narrative frame, gaps).
- **Rollout decisions locked 4/17:**
  - Option B — proactive (send deck + embed scheduling ask in same email)
  - Formal prep for ALL 12 investors including Clayton (no in-office-only catch-up)
  - Q4 2025 narrative architecture is the frame for Q1 2026
  - Q1 numbers will be "sad again" (DealsX launches 5/7, same day Q1 due) — frame as infrastructure-heavy quarter
- **Q4 2025 deck flag:** sitting in DRAFTS folder (file `107WA9cpc2aAPKvJd593byF-R0H4ab7e1YlZkW63XYS8`), never moved to QUARTERLIES SENT. Verify whether it was actually sent to investors on/around 2/7/26.

### Open decisions needed before narrative v1 (Fri 4/24)
1. Guillermo Apr 22 bi-weekly — use slot for Q1 preview + plant sourcing question early, OR keep clean and include in batch?
2. Investor Ask on Slide 1 = the sourcing question (Q1 from `investor-standing-questions.md`)? Yes/no.
3. Budget/runway numbers — Kay to provide or flag for budget-manager pull (depends on what gaps the mulling pack surfaces).

### Cadence going forward
- **Fri 4/24 check-in:** Kay shares mulling direction; Claude drafts narrative v1.
- **Fri 5/01 check-in:** Narrative v2 + deck build + 12 scheduling emails drafted.
- **Target ship: Wed May 6** (1 day early vs. May 7 due date).

### Sourcing-question standing file
`brain/context/investor-standing-questions.md` Q1 auto-pulls into every investor prep until retired. Clayton, Steuart Botchford + Sam Hyde, and BK Growth (Bressman/King) are top 3 highest-probability targets per 4/17 cap-table research.

## Carry-forward loops from 4/17 (for Monday briefing)

- Katie Walker thank-you — draft approved 4/17 by Kay for her own Superhuman paste. Status: Kay handling personally. Confirm sent.
- 4 ACG LinkedIn DMs — still pending Kay copy-paste to LinkedIn.
- Barrie AI calendar conflict question (Apr 22 Guillermo vs WSN) — 2 pref questions still open.
- Conference Pipeline picks — 4/20 Art Lawyering Bootcamp, 4/21 ACG Family Office, 4/22 EPCNYC (evening → skip). Decision needed early in week.
- Philip Hoffman warm intro — **14+ days aging**, RED. Kill / do now / re-defer with trigger?
- Mark Gardella reply — **10+ days aging**, RED. Draft / kill / defer with trigger?
- Calibration 4/16 proposals — 12 items still pending bulk/cherry-pick approval.
- 3 overdue Chanel contacts: Ashlee Walter, Robert DiMartini, David Wolkoff.

## Today's agenda (Friday 4/17 remainder)
1. Inbox zero (triage skill active)
2. Deal flow items (2 Synergy BB carried deals + whatever surfaces)
3. Review Fri artifacts: weekly-tracker, health-monitor, calibration proposals

## CRITICAL — Scheduled Skill Reliability Audit + Remediation (pre-May 7 DealsX launch)

On 2026-04-17 a scheduled skill reliability audit discovered **4 broken skills** (silent failure, exit 0 with zero output), **2 vulnerable**, **3 clean**, and **1 critically missing**. Sequenced remediation plan below. **C-suite: GC primary (skill-reliability + audit-trail integrity), CPO secondary (JJ ops), CFO tertiary (paid-hours ROI).**

### The 9 scheduled skills, ranked

| Skill | Schedule | Status | Issue |
|---|---|---|---|
| jj-operations-sunday | Sun 23:00 | **BROKEN** | Prompt "Which mode?" — 0 tabs created week of 4/13 |
| target-discovery-sunday | Sun 22:00 | **BROKEN** | Prompt "Which niche(s)?" — feeds jj-operations, compounded failure |
| weekly-tracker | Thu 22:00 | **BROKEN** | Prompt "current vs prior week?" — REGRESSION between 4/9 (worked) and 4/16 (broke) |
| calibration-workflow | Thu 23:00 | **BROKEN** | Prompt "apply/review/select/cancel?" — latent bug, surfaced 4/16 when traces accumulated |
| niche-intelligence | Tue 23:00 | VULNERABLE | Runs headless but no artifact validation |
| conference-discovery | Sun 21:00 | VULNERABLE | Low risk but no post-run validation |
| email-intelligence | M-F 07:00 | CLEAN | Artifacts confirmed 4/13-4/17 |
| deal-aggregator | M-F 06:00 | CLEAN | Artifacts confirmed 4/10-4/17 |
| nightly-tracker-audit | Daily 23:00 | CLEAN | 15 consecutive runs exit 0, idempotent |
| **health-monitor** | (none) | **CRITICALLY MISSING** | NO plist exists. CLAUDE.md says Friday scheduled; actually only runs when orchestrator invokes it. Meta-failure. |

### Two systemic findings

1. **Wrapper retry blind to exit-0 silent failures.** `scripts/run-skill.sh` retries only on network/401 errors. Skill exits 0 with no artifact = no retry, no alert, no flag.
2. **Log retention 14 days.** Regressions older than 14d already permanently deleted. Bump to 30d during audit phase + retroactively investigate what's still available.

### Remediation sequence (pre-May 7, 20 days out)

**Monday 4/20:**
- Install generic post-scheduled-skill stop hook (`.claude/hooks/post-scheduled-skill.py`) per the audit's manifest. One file covers all 9 skills. If expected artifact missing/empty/incomplete → Slack to `#ai-operations` via `$SLACK_WEBHOOK_OPERATIONS` (or new `$SLACK_WEBHOOK_SYSTEM_ALERTS`).
- Bump log retention from 14d to 30d.

**Monday-Tuesday:**
- Fix the 4 broken skills. Pattern: hardcode default mode for launchd invocation, or accept mode as CLI arg from plist. 10-min fix each.
  - jj-operations: default to `prep` on Sunday runs
  - target-discovery: default to `assess all Active-Outreach niches` on Sunday
  - weekly-tracker: default to `current in-progress week` on Thursday (or move to Friday morning)
  - calibration-workflow: default to "generate proposals, queue to inbox item for Kay approval" instead of blocking prompt

**Wednesday:**
- Install health-monitor plist (Friday 6am ET, before morning workflow). Same wrapper, artifact validation enabled. Restores the detection layer.

**Thursday:**
- Regression test: deliberately break a skill (rename output file) → confirm stop hook fires + Slack lands.

**Friday 4/24:**
- Full cycle. All 9 skills write artifacts, stop hooks validate, health-monitor catches anything that slipped. Ready for May 7 DealsX volume.

### Expected artifact manifest (for stop hook)

```yaml
email-intelligence:
  artifact: "brain/context/email-scan-results-{YYYY-MM-DD}.md"
  min_bytes: 500
  required_sections: ["Actionable Items Created", "Deal Flow Classified"]

deal-aggregator:
  artifact: "brain/context/deal-aggregator-scan-{YYYY-MM-DD}.md"
  min_bytes: 300

jj-operations-sunday:
  validation: "5 new tabs matching 'Call Log {M.DD.YY}' pattern on 1Y0ZjEkc2LHhBoO4QGO8Ny9MvG90NpojQn8bloKA291I"
  dependency: "runs AFTER target-discovery-sunday completes"

target-discovery-sunday:
  validation: "Col K (Owner Name) populated count > prior-day snapshot on any Active-Outreach sheet"

weekly-tracker:
  artifact: "brain/trackers/weekly/{WEEK_ENDING_FRIDAY}-weekly-tracker.md"
  min_bytes: 1000
  secondary: "Weekly Detail tab on 1NGGZY... has new column for current week"

calibration-workflow:
  artifact: "brain/outputs/calibrations/{YYYY-MM-DD}-calibration.md"
  secondary: "git log shows commit with VERSION bump dated today"

niche-intelligence:
  artifact: "brain/outputs/{YYYY-MM-DD}-niche-intelligence-report.md"
  min_bytes: 2000
  secondary: "WEEKLY REVIEW has new rows OR report explicitly states '0 new niches'"

conference-discovery:
  validation: "Slack post to #ai-operations within last 2h OR log contains 'notification sent'"

nightly-tracker-audit:
  validation: "Exit 0 sufficient; skill is idempotent. Log should contain 'Status: Clean' OR 'moves processed'"

health-monitor:
  artifact: "brain/trackers/health/{YYYY-MM-DD}-health.md"
  min_bytes: 500
  secondary: "Slack notification sent to #ai-operations"
```

### Safety rules for ongoing subagent use

- Any subagent doing batch sheet writes MUST use bash not zsh, validate tab names before write, snapshot pre-write to /tmp. See memory `feedback_subagent_sheet_write_safety`.
- Near-miss 4/17: jj-operations prep subagent clobbered 41 rows of Premium Pest master sheet via empty tab_name in zsh loop. Caught and restored. Don't repeat.

## JJ Monday 10am Slack — ready to send (awaiting Kay's approval)

Draft at `brain/context/tomorrow-pins-2026-04-20.md` (below) OR see 4/17 session log. Tabs created Fri 4/17 afternoon for Mon 4/20 - Fri 4/24 (200 calls, 16 Tier 1 + 184 Tier 2).

**To do Monday 10am:** Kay approves the draft, Claude fires to #operations-sva via `$SLACK_WEBHOOK_SVA`.

### JJ Slack draft

```
Hey JJ, here are your calls for this week:

Quick heads-up: there was a system issue last week that delayed the tabs. Fresh tabs are ready for this week.

This week's call logs are on the sheet: https://docs.google.com/spreadsheets/d/1Y0ZjEkc2LHhBoO4QGO8Ny9MvG90NpojQn8bloKA291I/edit
Tabs: Call Log 4.20.26 through Call Log 4.24.26 (Mon-Fri)
Context: See the "Niche Context" tab on the same sheet for industry overview, owner profile, and key talking points for Premium Pest Management.
Scripts: G&B Cold Call Guide — https://docs.google.com/document/d/12Hqfwxg4qJA3YdZh36ndd-flvYgWNZeL8sMZ9NAHlTY/edit

40 calls per day, 200 total this week.
16 Tier 1 (owner name known, ask for them by name) and 184 Tier 2 (ask for the owner or person in charge).

Reminder: Log results directly on each day's tab (columns T-W — Call Status, Call Date, Call Notes, Owner Sentiment). If you learn an owner's name during a call, add it to Notes and we'll update the master list.

Any feedback on this process at all along the way is welcome and appreciated. Any questions, reply here and I will get them to the right person.

— Claude
```

## Pipeline-manager hardening — CRITICAL before May 7 DealsX launch

The Project Restoration deal (EQA, 3/19-4/17) exposed that pipeline-manager's **CIM Auto-Trigger did NOT fire** on 3/20 when the CIM arrived. Specifically, all four of these failed silently:

1. No ACTIVE DEALS Drive folder was created for Project Restoration (CIM/ subfolder, FINANCIALS/, LEGAL/, etc.)
2. No inbox item was written to `brain/inbox/` with `urgency: critical` and `topic/cim-received` tag
3. No `#active-deals` Slack notification fired (NDA Executed OR CIM Received)
4. Stage-progression tracking jumped Identified → Closed / Not Proceeding on 3/26 without recording intermediate NDA Signed (3/20) and Financials Received (3/20) stages

Attio entry exists but lacks the audit trail. Kay had to manually request this be recorded on 4/17. An audit note has been added to the Attio list entry (entry_id `15b11bdf-09f7-490f-b303-b59cb176e774`) documenting the real timeline.

**Fix required before May 7:**
- Verify email-intelligence CIM detection logic (CIM in email attachment + PDF > 5 pages + "Confidential Information Memorandum" keyword match)
- Verify pipeline-manager Phase 1 CIM Auto-Trigger actually executes its 4 automated steps
- Verify Slack webhook `$SLACK_WEBHOOK_ACTIVE_DEALS` is alive and firing
- Verify stage progression recording captures NDA Signed → Financials Received intermediate stages, not just final state
- Add regression test: manually replay Project Restoration scenario, confirm all 4 triggers fire correctly

Trace written at `brain/traces/2026-04-17-pipeline-manager-cim-trigger-gap.md`.

## Health flags still open
- gog calendar CLI 404s (persistent since 4/16)
- Superhuman MCP not authenticated (2 days)
- Payoneer/bank AWS (since 4/14)
- Orphaned entities 22 → 46 (knowledge graph degrading)
- Granola Conwell miss pattern

## Mon/Tue external meetings (manual preview — CLI broken)
- **Mon 4/20:** C-suite Week 1 kickoff (CIO + CFO agent refactor) — internal
- **Tue 4/21:** Guillermo Lavergne bi-weekly — moved to Apr 22 per 4/16 reschedule

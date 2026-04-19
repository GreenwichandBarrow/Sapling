---
schema_version: 1.0.0
date: 2026-04-19
title: "Proposal: relationship-manager launchd at 6:50am ET + optional 7am dropped-balls Slack alert"
status: backlog
source: manual
urgency: normal
automated: false
tags: [date/2026-04-19, inbox, source/manual, urgency/normal, topic/launchd, topic/morning-workflow, topic/system-improvement]
---

## Description

**Source:** 2026-04-19 Anacapa deck analysis, Lesson 5. Partial adoption of Harry Liu's "scheduled morning brief" pattern. We reject full-scheduled push (loses the interactive calibration loop), but adopt the *signal-gathering pre-warm* piece so the briefing is instant when Kay says "good morning."

### Proposal: two changes

**Change 1 — Add relationship-manager to launchd, 6:50am ET Mon-Fri.**

Currently: email-intelligence runs 7am Mon-Fri (launchd). Relationship-manager runs live when Kay invokes /goodmorning — adds 30-60s of wait time while scans run.

After: relationship-manager pre-runs at 6:50am ET → writes relationship-status-{date}.md artifact. When Kay says good morning, both artifacts already exist. Briefing renders instantly.

Plist template: copy `com.greenwich-barrow.email-intelligence.plist`, change name + StartCalendarInterval to 6:50, change skill target to `relationship-manager`. One new file in ~/Library/LaunchAgents/.

**Change 2 — Optional 7am Slack dropped-balls early-alert.**

After email-intel + relationship-mgr complete at 7am, a small "dropped-balls-alert" step reads both artifacts for Dropped Balls bucket items and posts to #ai-operations Slack at 7am ET: only a 1-line ping ("🔴 3 dropped balls — open brief when ready") OR silence if 0.

Purpose: Kay wakes up, sees Slack on phone, knows if there's urgency before opening laptop. Does NOT push full brief (Harry's mistake — loses conversation). Does NOT push every bucket. Only surfaces the one bucket that costs deals if missed.

### Prerequisites (Kay approves → Claude builds)

- Change 1: requires editing ~/Library/LaunchAgents/ (outside project dir). Per `feedback_collaboration_split` Claude plans, Kay executes via terminal. Claude can generate the plist file + launchctl load commands, Kay runs them.
- Change 2: new skill `dropped-balls-alert` in .claude/skills/ + new plist. Per `feedback_friday_test_write_skills` this is a write skill (posts to Slack) so needs a Friday-afternoon dry run before launchd activation.

### Execution order

1. Kay approves proposal
2. Claude generates `com.greenwich-barrow.relationship-manager.plist` artifact
3. Kay runs `launchctl load ~/Library/LaunchAgents/com.greenwich-barrow.relationship-manager.plist`
4. Verify Monday AM that relationship-status-{date}.md is created by 7am
5. Once stable (1 week), Claude builds `dropped-balls-alert` skill
6. Friday dry-run: manually invoke, verify Slack ping content
7. Add launchd for dropped-balls-alert at 7:05am
8. Monitor one week, confirm signal:noise acceptable

### Why not full-schedule the briefing

Per analysis of Lesson 5: live conversation = strong learning loop. Today's briefing reformat is the proof — Kay gave feedback and reformatted twice in-session. Scheduled push = one-way notification, lost calibration. Keep the brief live, pre-warm the scans.

## Notes

*Not started — awaiting Kay approval of proposal*

## Outcome

*Pending*

---
schema_version: 1.1.0
date: 2026-06-21
type: trace
task: Refine Good Morning brief action surface
had_human_override: true
review_status: pending
importance: high
target: skill:pipeline-manager
applied_to: [.agents/skills/pipeline-manager/SKILL.md]
tags: [date/2026-06-21, trace, status/pending, topic/good-morning, source/pipeline-manager]
---

# Good Morning Brief Action Surface

## Context

Kay corrected several Good Morning rows that were technically true but operationally low-value: generic draft counts, deal-flow email inventory inside Email Orchestration, reminders to read emails, and repeated To Do rows. The brief should be the morning edit surface, not a duplicate inbox, dashboard, or task list.

## Decisions

### Email Orchestration is follow-through, not inbox scan
**AI proposed:** Include generic `Draft review`, `Deal-flow email`, and unread Start Virtual email rows under Email Orchestration.
**Chosen:** Email Orchestration uses only the dashboard follow-up buckets: `24-hour thank-yous`, `48-hour follow-ups`, and `EOW follow-ups`. Drafts appear only when tied to a concrete follow-up bucket with recipient/subject/purpose. Deal-flow moves to Deal Aggregator. Generic unread-email reminders are omitted unless converted into a concrete analysis/action recommendation.
**Reasoning:** Kay does not need reminders to check email. She needs decision-ready follow-through items and concrete operating actions.
**Pattern:** #morning-brief-action-surface

### Tasks & Follow-up is not a second To Do list
**AI proposed:** Repeat To Do rows and suggest what Kay should work on.
**Chosen:** Report only the open task count, then surface only items not already in the To Do list or new post-call/routing candidates.
**Reasoning:** The To Do file is the canonical task surface. Repeating it in Good Morning creates noise and decision fatigue.
**Pattern:** #do-not-duplicate-canonical-tracker

### Dashboard sections precede non-dashboard operating follow-up
**AI proposed:** Place Meeting Briefs before System Health and omit C-Suite & Skills from the dashboard-ordered flow.
**Chosen:** Dashboard sections come first: Email Orchestration, Active Pipeline, Deal Aggregator, C-Suite & Skills, System Health. Meeting Briefs and Tasks & Follow-up follow afterward.
**Reasoning:** Good Morning should align with the dashboard reference model before moving into non-dashboard operating follow-up.
**Pattern:** #dashboard-aligned-briefing-order

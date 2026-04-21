---
schema_version: 1.1.0
date: 2026-04-20
type: trace
title: "Intermediaries: passive dormancy monitoring, not active cadence"
had_human_override: true
importance: high
target: "skill:relationship-manager"
tags: ["date/2026-04-20", "trace", "topic/relationship-manager", "topic/intermediary", "pattern/model-real-workflow"]
---

# Intermediary Relationship Management: Dormancy Watch, Not Cadence Prompts

## Context

Designing the relationship-manager intermediary handling. Initial proposal: quarterly cadence to touch river guides, brokers, CPAs, lawyers. 100-day window aligns with quarterly broker-blast pattern. Kay pushed back.

## Decisions

### Cadence model for intermediaries
**AI proposed:** Quarterly active cadence for intermediaries (River Guide / Industry Expert / Advisor). Surface overdue contacts in morning brief; prompt Kay to "touch base." Escalate to monthly for intermediaries who sent a deal or intro in last 90 days.

**Chosen:** **NO active cadence for intermediaries.** Instead: passive dormancy monitoring. Watch for last inbound from them; if >100 days silent after prior inbound pattern, flag as "newly dormant" for Kay's re-engage-or-drop decision.

**Reasoning:** Kay stated explicitly:
> "Most brokers send monthly updates, some every quarter, as I think about it I don't have any intermediary I reach out to with a particular cadence."
> "I build the relationship and then they send to me."

The workflow asymmetry is: Kay builds once (intentional outreach burst), then brokers/advisors send to her on their own cadence. A cadence prompt telling her to "touch base with [river guide]" describes a behavior she never runs. Building it creates notification noise she'd ignore and erodes briefing trust.

**Pattern:** #pattern/model-real-workflow — design for actual Kay behavior, not generic CRM defaults.

### Dormancy threshold
**AI proposed:** 90 days (matches quarterly cycle exactly).

**Chosen:** 100 days (90-day quarterly cycle + ~10-day buffer).

**Reasoning:** Kay: "some plan for 90 days, so we should go a week beyond that or so." Buffer prevents false positives on brokers who send on a regular quarterly cadence.

### Build-phase handling
**Chosen:** If an intermediary has no inbound yet (Kay just made outbound, relationship still being built), do NOT flag as dormant. Requires prior inbound pattern (≥2 messages) to trigger the dormancy classification.

**Reasoning:** Silence for a brand-new contact is expected. Dormancy only means something when there was a prior sending pattern that stopped.

## Learnings

- The question "should the system prompt a cadence for X?" should be answered by observing whether the user actually does X, not by defaulting to CRM best practice.
- Passive monitoring (silence-watch) > active prompting when the relationship asymmetry is "user-builds, counterparty-sends."
- Surface dormancy as a decision ("re-engage / drop / keep watching"), not a task ("touch base") — gives Kay agency without pretending she needs to act.

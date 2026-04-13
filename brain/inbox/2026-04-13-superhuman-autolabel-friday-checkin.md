---
schema_version: 1.0.0
date: 2026-04-13
title: "Superhuman Auto Label health check + email-intelligence skill update"
status: backlog
source: manual
urgency: normal
due_date: 2026-04-17
tags: [date/2026-04-13, inbox, source/manual, urgency/normal, topic/superhuman, topic/email-architecture, topic/skill-update]
---

# Superhuman Auto Label Friday Check-In

Created 9 Auto Labels across all 4 accounts (kay.s@, kaycschneider, kaycfofana, kaystrash23) on April 13. Need ~4 days of running before evaluating accuracy and back-fill behavior.

## Friday April 17 — Add to weekly review

### 1. Auto Label accuracy spot-check
For each of the 9 labels on each account, verify:
- Are messages being categorized correctly?
- Any obvious mis-categorizations?
- Counts on each label — does the volume distribution make sense?

If any label is misfiring, tighten or broaden the AI prompt. Labels and prompts documented in `feedback_email_label_architecture.md`.

### 2. Back-fill on existing mail
Check whether Superhuman's AI auto-labeled existing historical mail (16K+ across accounts) or only forward-going mail. If existing mail not back-labeled:
- Use Superhuman MCP `add_label` in batches with search queries to bulk-apply
- Or: leave existing mail alone, only auto-label going forward (Kay's call)

### 3. Superhuman AI label re-creation watch
Monitor whether Superhuman re-created any of the original `[Superhuman]/AI/*` labels after Kay renamed them. If yes: rename again, accept parallel labels, or add Gmail filter to relabel.

### 4. Update email-intelligence skill
**Confirmed today: skill does NOT currently read the Deal Flow Auto Label.** It runs its own BLAST/DIRECT/NEWSLETTER classifier on raw Gmail (line 36 + 77 of SKILL.md).

Update needed:
- File: `.claude/skills/email-intelligence/SKILL.md`
- Add: read messages tagged with the Superhuman `Deal Flow` Auto Label as high-confidence pre-classified deal source
- Keep existing Gmail scan + own classifier as fallback for un-categorized mail
- Confirm CIM auto-trigger, Active Deal Fast-Path, DIRECT/BLAST classification all still fire correctly

### 5. L picker verification on all 4 accounts
Confirm all 9 Auto Labels appear in Superhuman L (label) picker on each account. Especially check kay.s@ G&B since that's where deal-flow triggering matters most.

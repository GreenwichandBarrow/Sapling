---
schema_version: 1.1.0
date: 2026-06-09
type: trace
tags: [date/2026-06-09, trace, topic/email-drafting, topic/templates, status/pending]
had_human_override: true
importance: high
target: memory:feedback_kay_handles_all_replies
---

# Decision Trace: Email Drafts Stop Before Sending and Templates Live in Drive

## Context

During the daily rhythm thread, Codex audited stale Gmail drafts and treated some generic reusable email language as Gmail draft cleanup/restore candidates. Kay corrected the workflow: she handles all sends, Codex only drafts, and reusable templates live in the Google Drive G&B master template folder through the email/outreach skill workflow.

## Decisions

### Do not ask whether to send
**AI proposed:** Draft hygiene and follow-up decisions in terms of whether Kay should send or keep certain drafts.
**Chosen:** Codex should never send and should not ask whether to send. Kay handles all sends. Codex stops at draft/recommendation.
**Reasoning:** Sending is not a decision Codex owns; asking about it wastes decision budget and risks blurring the boundary of Kay's personal-send workflow.
**Pattern:** #email-draft-boundary

### Do not store generic templates as Gmail drafts
**AI proposed:** Restore/keep generic Gmail drafts as reusable templates.
**Chosen:** Generic language belongs in Google Drive templates, specifically the G&B master template folder and the relevant email/outreach skill. Gmail drafts are only actual messages Kay may personally send.
**Reasoning:** Gmail drafts are an execution surface, not a template repository. Keeping generic placeholders there creates stale-draft noise and confuses morning email-intelligence.
**Pattern:** #template-source-of-truth

## Learnings

- When drafting, reference the email/outreach skill and live Drive templates instead of old Gmail draft templates.
- Draft-status audits should distinguish actual pending messages from reusable template artifacts.
- Morning briefings should not ask Kay about sending; if a draft exists, surface review/cleanup only.

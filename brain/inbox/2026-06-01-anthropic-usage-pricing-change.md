---
schema_version: 1.0.0
date: 2026-06-01
title: Assess Anthropic June 15 programmatic usage pricing change — cost impact on cron jobs
status: backlog
source: email
urgency: high
due_date: 2026-06-12
entity: "[[entities/harrison-wells]]"
source_ref: "msg:19e6caa10b05350c"
confidence: high
automated: true
tags: [date/2026-06-01, inbox, source/email, urgency/high, topic/tech-stack, person/harrison-wells]
---

# Assess Anthropic June 15 programmatic usage pricing change — cost impact on cron jobs

## Description

Harrison Wells (Dodo Digital, harrison@dododigital.ai) emailed May 31 with an important infrastructure alert:

Starting **June 15**, Anthropic is changing programmatic usage rules:
- $100–$200 of credits/month included for automated/programmatic usage
- Usage beyond that will be pay-per-use
- This specifically affects **scheduled cron jobs** — could increase costs hundreds of dollars/month depending on setup

Harrison recommends running `claude -p` usage analysis to estimate potential costs. He has workarounds if costs are prohibitive.

**Deadline: June 15** (2 weeks away).

Action: Ask Claude to analyze current `claude -p` cron usage and estimate monthly cost impact under the new model. Reply to Harrison with findings.

## Notes
*Not started*

## Outcome
*Pending*

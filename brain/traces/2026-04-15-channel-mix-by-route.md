---
schema_version: "1.2.0"
date: 2026-04-15
type: trace
title: "Outreach channel mix varies by route: DealsX=email+LinkedIn, Kay=email+LinkedIn(ad-hoc), JJ=call+email(gated on phone ack)"
tags: ["date/2026-04-15", "trace", "role/cmo", "role/cpo", "topic/outreach-channels", "topic/cadence", "topic/jj-operations", "topic/dealsx"]
target: agent:cmo, agent:cpo, skill:jj-operations, skill:outreach-manager
importance: high
---

### Channel mix is determined by outreach route, not niche
**Reasoning:** Kay confirmed three distinct channel patterns on 2026-04-15:

1. **DealsX route (Sam Singh):** Email + LinkedIn, both automated via DealsX platform. Kay reviews copy week 1, spot-checks list week 2, then the platform runs both channels. Targets: all SaaS verticals routed through DealsX.

2. **Kay Email route:** Email (Superhuman drafts Kay approves and sends) is primary. LinkedIn outreach is Kay's ad-hoc judgment call on high-conviction targets — not systematic. Targets: Private Art Advisory, Estate Management, other relationship-driven niches where Kay's voice is the asset.

3. **JJ-Call-Only route:** Phone call is primary. Email follow-up is **gated on phone acknowledgement** — only sent after JJ confirms the owner is willing to hear more (Connected + Interested / Connected + Curious). No email after voicemail, no-answer, or wrong-number. Targets: Premium Pest Management, future blue-collar niches.

**Trigger:**
- `/cmo` reviewing any outreach draft: check the target's routing (Col D on tracker). Apply the right cadence rules for that channel mix. Do NOT push LinkedIn drafts for JJ-route targets; do NOT push cold email drafts for JJ-route targets who haven't been phone-acknowledged.
- `/cpo` reviewing JJ Slack instructions: ensure JJ's call log has a status column distinguishing "Connected + Interested" (email trigger) from "Voicemail / No Answer / Wrong Number" (no email). Flag any email sent to JJ-route targets before phone acknowledgement.
- `jj-operations` skill: call log structure must capture acknowledgement status clearly enough that email follow-up can be triggered only on positive ack.
- `outreach-manager` skill: DealsX-route targets skip G&B email drafts (DealsX handles). Kay Email route uses universal G&B cadence (Day 0/3/6/14, A/B). JJ-Call-Only route suppresses Day-0 email; first email is post-call if/when acknowledgement happens.

## Why this matters
- Sending email after voicemail = volume-outreach signal. Contradicts Kay's brand and her 5/day thoughtful approach. The JJ gating preserves the "I'm a person, not an institution" voice even for call-first niches.
- DealsX email and LinkedIn are Sam's infrastructure — G&B should not also send email or LinkedIn on DealsX-routed targets (duplication + bad signal). Attio dedup must catch this.
- LinkedIn from Kay's personal account is selectively valuable; automating it would erode the signal. Keep it ad-hoc, Kay's call.

## Learnings
- Route determines cadence, not niche. The same niche could theoretically run through two routes (e.g., a borderline target surfaced via DealsX that Kay wants to pull into Kay Email for warmer handling) — trust the Col D routing.
- JJ's call log schema is load-bearing for this entire gating logic. A single miscoded "Connected" vs "Voicemail" entry breaks the system.

frame_learning: true

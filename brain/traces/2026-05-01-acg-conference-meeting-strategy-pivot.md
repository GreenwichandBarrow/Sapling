---
schema_version: 1.1.0
date: 2026-05-01
type: trace
title: "ACG NY Women of Leadership Summit — pivot from 25 outreach drafts to 6 in-person 1:1 IB-heavy meetings"
tags: ["date/2026-05-01", "trace", "topic/acg-women-summit", "topic/conference-engagement", "topic/ib-outreach", "topic/conference-strategy", "domain/sales", "had_human_override"]
importance: high
target: skill:conference-engagement
---

# ACG conference meeting strategy pivot

## Context

ACG NY Women of Leadership Summit 5/14 confirmed registered + on calendar. Conference-engagement skill triggered to draft pre-conference outreach. Initial subagent proposal: 25 outreach drafts (broad blanket coverage of attendee list, mostly intermediary-classified). Kay reviewed and reframed.

## Decision

**AI proposed (initial):** 25 personalized outreach drafts to ACG attendees from the published list. Audience-mix matched the attendee classification (intermediary / owner / peer) per `conference-engagement` standard taxonomy.

**Chosen:** 6 in-person 1:1 meeting requests, IB-heavy. Subagent re-ran with this constraint and surfaced top 6 IB picks: TM Capital (Gillespie + Kohli), Netrex Capital (Sadocha — insurance specialist), Candlewood (Hallie Berk), Capstone (Conway + Tolliver). First send drafted + sent to Hallie Berk (10:20 slot).

**Reasoning (Kay's reframe):** A summit is not an inbox campaign. The unit of value is **a single in-person 1:1 conversation** at the event itself, not an email landing pre-event. 25 emails dilute attention (25 send-times to coordinate, 25 reply threads to manage, none of them differentiated). 6 confirmed in-person slots means 6 actual meaningful conversations, each pre-set with a specific person at a specific time.

The IB-heavy filter is strategic: investment bankers carry deal-flow that brokers don't, and ACG NY Women is a venue where senior IBs are accessible (junior brokers are at BizBuySell-style events). The summit's lower attendee count + premium positioning means IB representation is concentrated; capitalize on that scarcity.

## Why this matters for future agents

Default conference-engagement skill behavior is "max coverage of attendee list." This is the wrong default for **premium / curated / smaller summits** where the value is meeting fidelity (deep 1:1 conversations) not reach (many shallow contacts). For trade-show-style large conferences (NPMA, MSP-style), max-coverage may be right. For curated summits, in-person-1:1-first is right.

The taxonomy that matters:
- **Trade show** (1000+ attendees, exhibit-floor-driven) → max-coverage outreach OK
- **Curated summit** (50-300 attendees, networking-driven, premium positioning) → in-person-1:1 first, max 6-10 pre-set meetings, IB/investor-bank heavy if available

## How a future agent should apply

When conference-engagement runs for a registered conference:

1. **First question: trade show or curated summit?** Check attendee count, ticket price, and program format. ACG-style = curated.
2. **For curated summits:**
   - Default to 6-10 pre-set in-person meeting requests, not 25 mass outreach
   - Filter attendee list for IB / investor-bank / institutional-buyer roles first
   - Each request is specific: "would love to meet for 20 min during the {time slot} — happy to come to you"
   - Skip generic "hope to connect" outreach
3. **For trade shows:** existing max-coverage approach OK
4. **Surface the trade-show vs summit classification to Kay BEFORE drafting** so the strategy is pre-approved, not pivoted-after-25-drafts (today's failure mode wasted ~25 draft tokens).

## Concrete pivot waste

Today's first pass produced 25 drafts that were thrown out. ~5,000 tokens of subagent output discarded. The pivot to 6 IB-heavy meetings produced the actual deliverable. Future agents should burn the classification cycle FIRST to avoid this waste.

## Related

- `feedback_conference_pipeline_preserve_week_of_formatting` — Conference Pipeline sheet hygiene
- conference-engagement SKILL.md — needs classification step added (trade show vs curated summit)
- `feedback_post_conference_replies_reactive_only` — post-conference: silent attendees stay silent
- Voice calibration secondary-trace candidate: "mandates" + "deal flow" too industry-sounding for ACG voice; "what you're working on" + "from your side of the table" land naturally

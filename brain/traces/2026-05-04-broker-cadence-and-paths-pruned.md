---
schema_version: 1.1.0
date: 2026-05-04
type: trace
title: "Pruning premature scaffolding from broker pipeline — Day 12 + Need-More-Info both dropped"
trace_type: scope-discipline
tags: ["date/2026-05-04", "trace", "topic/broker-channel", "topic/cadence", "topic/scope-discipline"]
---

# Pruning premature scaffolding from broker pipeline — Day 12 + Need-More-Info both dropped

## Trigger

While auditing template gaps in the canonical Intermediary Email Templates Doc, I surfaced 5 missing scenarios for Kay's review (Day 5, Day 12, DECLINE-POST-REVIEW, NEED-MORE-INFO, NDA-SIGNED-BACK). Kay's response shipped two unexpected REJECTs:
- Day 12 soft-close → "drop from cadence"
- NEED-MORE-INFO → "too rare for broker engagement, we move to owners call. drop this"

Both had been treated as obviously-needed in the prior session's vault snapshot (Day 12 LOCKED yesterday) and pipeline-manager skill code ("Need more info" was a documented On-Kay's-Approval branch).

## Decision

Removed both from the system entirely:
- **Cadence:** Brokers + IBs reduced from 3-touch (Day 0 + Day 5 + Day 12) to 2-touch (Day 0 + Day 5). Day 12 template not added to canonical doc; outreach-manager Subagent 3 cadence rule rewritten in skill code.
- **CIM-screen branches:** "Need more info" path replaced with "Move to owner call" — pipeline-manager line 871-873 + 879 rewritten so the Pass/Owner-call/Save-for-later trichotomy replaces Pass/Need-more-info/Save-for-later. Owner-call triggers `deal-evaluation` Phase 4 with `pending_owner_call: true`.

## Alternatives considered

1. **Keep Day 12 — soft-close has value as a final relationship-out** — rejected. Day 12 template offers brokers nothing they didn't already have on Day 5; it just signals desperation. Kay's 2-touch read: if Day 5 didn't get a reply, Day 12 won't either, and the marginal pestering damages future re-approach options.
2. **Keep Need-more-info — info-gathering is cheap** — rejected. The actual data points the template would request (revenue, EBITDA, customer concentration, owner age) are all in the CIM 99% of the time. Need-more-info fires only when the broker sent a teaser without a CIM, in which case the right move is to NDA → CIM, not back-and-forth on metrics. The remaining edge (CIM exists but lacks one data point) is rare enough that "move to owner call" is the better escalation.
3. **Soft-deprecate (leave both in skill code with `deprecated: true`)** — rejected. Soft-deprecation invites future agents to re-enable. Hard removal forces explicit re-introduction with new justification.

## Reasoning

Pattern: both items were "scaffolding for scenarios that don't justify them." Day 12 was inherited from a generic 3-touch cold-email playbook; Need-more-info was inherited from a generic CIM-evaluation pipeline. Neither was specific to G&B's actual broker engagement reality (low broker conversion, high signal-density CIMs, owner-call as the actual decision point).

Same scope-discipline pattern as the $1M EBITDA floor incident (`2026-05-03-strategic-thresholds-need-grounding.md`): inherited convention without grounding gets pruned the moment Kay's lens hits it. Future agents should pre-empt this by asking "does this scenario actually fire in our context, or are we copying a pattern from a different operator's playbook?" before adding any branch.

## What would change if reversed

If a future agent restores Day 12 from the vault snapshot (which still says "3-touch LOCKED"): brokers get a third unanswered touch that adds noise without conversion. Voice drift toward desperation tone.

If a future agent restores Need-more-info from old skill code archaeology: pipeline gets a back-and-forth metric-gathering branch that competes with the cleaner owner-call escalation. CIM evaluation slows down.

The vault snapshot has been annotated with the supersession note ("Day 12 soft-close DROPPED, cadence is 2-touch") to prevent the snapshot itself from re-introducing the dropped item.

---
schema_version: 1.2.0
date: 2026-05-03
type: discussion-brief
status: draft
skill_origin: socrates
kay_approved: null
tags: ["date/2026-05-03", "output", "output/discussion-brief", "status/draft", "topic/intermediary-channel", "topic/deal-aggregator", "topic/broker-outreach"]
---

# Discussion — Intermediary Channel Build (Broker + IB)

**Direction chosen:** Build broker + IB intermediary channel as the 4th pipeline, hot in parallel with G&B Email / JJ / DealsX. Volume layer: 5 broker emails + 5 LinkedIn DMs every weekday from primary domain (no Apollo, no subdomain, no Sam dependency). Skill layer: durable upgrades to deal-aggregator (dual-filter), email-intelligence (reputation rules + auto-acknowledgments + new-broker detection), outreach-manager (broker draft jobs), and Command Center M&A Analytics dashboard. Targets: 50 verified brokers + IBs in Attio, 50 sends across 2 weeks, deal-aggregator complete this week, 1-2 conferences in next 60 days.

## Problem framing

G&B has 4 pipeline channels: G&B Email proprietary outreach, JJ cold calling, DealsX outsourced cold email + LinkedIn (launching this week), and intermediary (brokers / IBs / lawyers / CPAs / lenders). The intermediary channel is the most underleveraged. Industry close rate dropped 70%→30%; lender friend's reframe says top tier still 80%, pack diluting average. Megan's stat (60% of investor's searchers acquired through brokered deals) is WIN attribution not FLOW attribution, which preserves the existing memory that proprietary stays primary. G&B is at 0 NDAs/week, mental panic, 6-month effective window (Nov 2026 cash exhaustion vs Feb 2027 paper deadline). Year+ in. Stuck in one-off high-touch outreach, hasn't institutionalized volume.

## Goal hierarchy

- **Surface:** Rebuild intermediary channel into a high-volume pipe (friend's 10-NDA/week benchmark).
- **Underlying:** Reset to volume that produces closeable deals + build reputation as 80%-tier closer + reconcile Megan's broker-acquisition stat against existing memory cap on intermediary + do this within G&B's limited time and 6-month window.

## Alternatives considered

1. **Apollo email sequences from subdomain** — rejected. Over-engineered for stage. 5/day from primary domain doesn't burn it.
2. **JJ pivots to broker calls** — rejected. G&B doesn't want JJ leading those relationships.
3. **Sam runs broker outreach** — backup only. Architecture must work without Sam dependency.
4. **10 NDAs/week target** — rejected. Friend's benchmark is cautionary (2 yr, 0 close, multiple LOIs). Reset to 5-10 surfaced deals/week with closeable focus.
5. **Marketplace scraping workarounds** — deferred to backlog. Email/RSS feeds cover 80%.
6. **Two-filter architecture** — simplified to single filter, three-tier output (strict / opportunistic / out).
7. **NDA auto-draft pipeline** — replaced with Gmail manual snippets + auto-acknowledgment reply (skill-drafted).
8. **Standalone reputation report** — replaced with Command Center M&A Analytics dashboard extension. weekly-tracker stays archive.
9. **Mass intermediary scope** — narrowed to brokers + IBs only this build. Opportunistic intermediaries (lawyers / CPAs / lenders / FOs / associations) deferred to Q3 nurture cadence.

## Assumptions surfaced (load-bearing)

- Megan's 60% stat is WIN attribution, not FLOW attribution. Drove decision to keep proprietary primary, broker as fourth-channel-not-replacement.
- Top tier still closing at 80% per lender friend. Drove decision that machinery + quality interactions = 80% path.
- Existing email templates exist and need REVAMP not full draft. Mon scope is revamp.
- Preliminary broker target list has wrong-company-type errors (Apollo classified non-brokers as brokers). Mon list-verification subagent required before outreach starts.
- Jeremy's contacts auto-pass verification.
- 5/day manual is below Gmail spam/burn threshold. No subdomain or warm-up needed.

## Skill upgrades (durable code changes)

### deal-aggregator
1. Dual-filter architecture (single filter, three-tier output)
2. Broker email-list ingestion logic (BizBuySell, Sunbelt, IBBA digests)
3. Marketplace digest ingestion (Axial, BizQuest)
4. Buy-box config reference pulls live from Drive doc
5. Reliability/plumbing fixes (post-Mon-diagnosis)
6. Surfacing logic adjustments

### email-intelligence
1. Reputation rule v1: broker inbound flags Slack within 5 min
2. Unknown-broker detection rule + propose-to-add flow (writes to Attio on YES)
3. Broker sender list pulls from Attio dynamically
4. Auto-draft NDA/CIM acknowledgment reply with day-aware sign-off

### outreach-manager
1. Broker-channel daily draft job: 5 broker emails per weekday
2. Day-5 follow-up draft job (triggered by Attio `next_action`)
3. Day-12 soft-close draft job
4. Template references know where finalized templates live in Drive/vault

### Command Center dashboard
1. M&A Analytics page broker channel rows: emails sent, LinkedIn DMs sent, reply rate, NDAs received + signed, response time, conference meetings booked, follow-ups due

## Stored artifacts

### Drive primary + vault snapshot
- Broker-channel buy-box page (filter source for deal-aggregator + footer reference for templates)
- 3 outreach templates (intro / day-5 / day-12)
- Standing financing letters (Guillermo + Anacapa)

### Other storage
- 3 Gmail reply snippets (yes-NDA / no-thanks / more-info) → Gmail templates feature
- 2 auto-acknowledgment templates (NDA received / CIM received) → email-intelligence skill code + Drive reference
- Verified top-50 broker + IB list → Attio
- <1hr response SLA → CLAUDE.md pre-flight checklist

## 3-Week Plan (high level)

### Week 1 (May 4-10) — kickoff and foundation

**Mon May 4 (9am-7pm, biggest workday, 10:30-11:45 meeting blocked, no lunch break):**
1. 60-min deal-aggregator failure-mode diagnosis (9:30am)
2. Buy-box revamp + template revamp + Gmail snippets locked
3. List-verification subagent runs; trim to 50 verified brokers + IBs
4. First 5 broker emails + 5 LinkedIn DMs sent
5. Subscribe to broker email/RSS feeds
6. After hours: reputation rule v1 wired; Guillermo + Anacapa emailed for capacity letters

**Tue May 5 (9am-2pm):** 5/5 sends; dual-filter architecture build begins
**Wed May 6 (9am-2pm):** 5/5 sends; dual-filter continues
**Thu May 7 (9am-5pm):** 5/5 sends; dual-filter validation; Handwrytten platform setup; Gmail snippets review
**Fri May 8 (9am-2pm):** 5/5 sends; Command Center M&A Analytics extension; deal-aggregator end-to-end validation; end-of-week-1 review

### Week 2 (May 11-17) — conference week
- 5/day continues for second 25 of 50; day-5 follow-ups fire via Attio next_action
- 1 conference attended (G&B limited days)
- Handwrytten cards mailed to top-15 priority brokers

### Week 3 (May 18-24) — conference week
- 50 emails total sent; day-12 soft-closes fire
- 2nd conference if appetite
- Begin second-tier intermediary nurture cadence design (Q3 build prep)

## End-of-Week-1 targets

- 25 broker/IB emails + 25 LinkedIn DMs sent
- Deal-aggregator COMPLETE: dual-filter live, broker feeds ingested, surfacing 5-10 deals/week, reliability validated
- Reputation rules live; Gmail snippets locked; auto-acknowledgment templates wired
- Standing financing letters from Guillermo + Anacapa on file
- Top-50 verified broker + IB list locked in Attio
- Handwrytten platform setup complete
- Command Center M&A Analytics broker rows live

## Hard rules logged

- 5 emails + 5 LinkedIn DMs every weekday (M-F). No skip days. Sat/Sun off.
- <1 hour response SLA on broker inbound during 9am-5pm ET.
- Drive primary + vault snapshot for all templates and docs.
- No Sam dependency in primary architecture (backup only).
- No JJ broker pivot.
- All system-level reliability issues route to Harrison (G&B's resource); skill-level work is Claude + G&B.
- Brokers receive emails M-F because of THEIR work week, not G&B's preference.

## Open questions / deferred

- Industry vs geographic broker focus: geographic per Megan for broker channel, industry-strict for proprietary. Stays open, doesn't block this week.
- Second-tier intermediary nurture (lawyers / CPAs / lenders / FOs / associations): deferred to Q3 build.
- Marketplace scraping workarounds for blocked sites: backlog only if email/RSS feeds prove insufficient at Week 4+.
- Apollo re-entry: only if/when manual hits a real ceiling.

## Handoff

Ready for /plan with this brief as input. Plan mode produces granular work breakdown for each skill change: file paths, test plans, dependency ordering, estimated hours per task.

Day 1 anchor: Mon May 4 9:30am deal-aggregator diagnosis. Claude prep (audit + Slack summary) by 8am Mon.

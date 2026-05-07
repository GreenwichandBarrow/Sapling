---
schema_version: 1.2.0
date: 2026-05-04
type: slack-draft
status: review
skill_origin: null
kay_approved: null
kay_approval_date: null
people: ["[[entities/kay-schneider]]"]
companies: []
projects: []
hypothesis: null
trace: null
task_ref: null
published_url: null
tags: [date/2026-05-04, output, output/slack-draft, status/review, topic/broker-channel, topic/deal-aggregator, topic/email-intelligence]
---

# Slack Draft — #operations — Broker Ingestion 30-Day Audit

**Channel:** #operations
**Length:** ~120 words

---

30-day broker-channel audit done ahead of this week's IB launch. The dominant failure mode is filter, not ingestion. Sources are mostly working. The classifier kills Decision-worthy broker leads.

- ~42 named-broker BLAST emails ingested over 30 days (E&K, Quiet Light, IAG, Tory @ Flippa, Business Exits, Viking Mergers). Zero surfaced as Decision items. All auto-archived.
- Web-scrape side: 100+ listings parsed per scan day, only 10 broker-platform listings ever surfaced to Slack across 30 days, and 8 of those landed on two days (04-13 + 04-16).
- 11% of broker-active days lost to source blocks (BizBuySell + Quiet Light + Flippa + Rejigg). 12% lost to ingested-but-ignored.
- Two silent infrastructure fails (04-27 hallucinated parallel run, 04-30 missing artifact). Fingerprint store empty since 04-22.

Recommend Mon build: loosen email BLAST rule for named-broker senders (auto-promote to per-listing 🟡 Decision when sender is on Attio Intermediary Pipeline + body has structured financials). Full audit at `brain/outputs/2026-05-04-broker-ingestion-audit-30day.md`.

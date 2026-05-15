---
schema_version: 1.1.0
date: 2026-05-15
type: call
call_id: 55c9bcdb-de73-4a12-a8b1-de4640eca26c
source: granola
classification_type: partner
people: ["[[entities/harrison-wells]]", "[[entities/kay-schneider]]"]
companies: ["[[entities/dodo-digital]]", "[[entities/greenwich-and-barrow]]"]
tags: ["date/2026-05-15", "call", "client/greenwich-and-barrow", "person/harrison-wells", "person/kay-schneider", "company/dodo-digital", "company/greenwich-and-barrow", "topic/ai-coaching", "topic/deal-aggregator", "topic/web-scraping", "topic/claude-infrastructure", "topic/architecture"]
granola_link: https://notes.granola.ai/d/55c9bcdb-de73-4a12-a8b1-de4640eca26c
---

# Harrison Wells — AI Coaching Session

**Date:** 2026-05-15 12:00 ET
**Attendees:** [[entities/harrison-wells|Harrison Wells]] (Dodo Digital), [[entities/kay-schneider|Kay]] ([[entities/greenwich-and-barrow|G&B]])
**Granola ID:** `55c9bcdb-de73-4a12-a8b1-de4640eca26c`

## Notes

Monthly AI coaching session. Kay caught Harrison up on the automation stack: conference pipeline and niche intelligence both performing to target; deal aggregator broken (zero broker-email matches for weeks). Harrison gave a CASS-log debugging method, web-scraping fixes for recurring 403s (Browserbase, Sweet Cookie, GitHub scrapers), and recommended a unified context-engineered architecture over splitting personal vs. business agents. Server infrastructure confirmed stable (laptop-close does not interrupt; cross-device continuity working).

Full analysis Google Doc: https://docs.google.com/document/d/1pyApBUsJr5EZMGNHW7spXunLJkK_BXdBL58yg-k9JsM/edit
Granola transcript: https://notes.granola.ai/d/55c9bcdb-de73-4a12-a8b1-de4640eca26c

## AI Analysis

### Action Items
- [ ] Debug deal aggregator — CASS log review + manual run + email-source-filter audit @kay
- [ ] Test web-scraping fixes Harrison emails (Browserbase / Sweet Cookie / GitHub) for 403s @kay
- [ ] Implement evolving-skills framework Harrison shares @kay
- [ ] Email scraping tools + skills framework to Kay @harrison
- [ ] Schedule June follow-up at 10 AM (avoid lunch conflict) @kay

### Signals
- **Deal aggregator outage:** broker-email cross-reference dark for weeks — live sourcing gap, silent scheduled-job failure pattern
- **Channel validation:** conference networking out-performs online outreach; cold email confirmed low-quality
- **Architecture:** unified context-engineered skills model endorsed — no re-architecture warranted

---
*Auto-classified by Call Classifier*

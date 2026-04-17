---
date: 2026-04-17
type: context
title: "G&B Tech Stack Decisions — Kill / Keep / Re-activate Log"
tags:
  - context
  - topic/tech-stack
  - topic/budget-manager
  - topic/cfo
  - date/2026-04-17
---

# G&B Tech Stack Decisions — Kill / Keep / Re-activate Log

Persistent log of decisions to add, remove, or re-activate SaaS tools in Kay's stack. Each entry captures what was killed/kept/activated, when, why, and under what conditions it would be reversed.

---

## 2026-04-17 — Linkt: PAUSED (free month through May 30, decision deferred)

**Update 4/17 PM:** At cancellation, Linkt offered one free month (through May 30, 2026). Accepted. Cancellation decision deferred to May 30. Reason: DealsX launches May 7; by May 30 Kay will have seen the full stack (DealsX + Apollo) in operation and can judge whether Linkt fills a gap. Cheap option value.

**Previous status:** Active subscription, auto-renewing April 30, 2026. Intent was to cancel before renewal.

**Decision:** Let the subscription lapse April 30 rather than auto-renew. Pre-cancel, burn remaining credits on Premium Pest Management NYC enrichment (see `brain/outputs/2026-04-17-linkt-credit-burn-plan.md` if written).

**Why:**
- **DealsX replaces Linkt for outbound cadence** — go-live 5/7/2026. DealsX owns the email-send + cadence layer Linkt was providing.
- **Apollo replaces Linkt for contact enrichment** — Apollo's `/people/match` is G&B's verified email source per `feedback_apollo_only_emails`. Linkt was using Apollo under the hood anyway.
- **Overlap + cost** — paying Linkt when DealsX + Apollo cover the same work is a tech-stack duplication. CFO call.

**What we lose:**
- Bulk sheet-based enrichment UX — Apollo is API-per-call, Linkt was spreadsheet-friendly. When Kay wants to enrich 100+ rows fast, Apollo requires scripting.
- Possibly: Linkt-specific data that Apollo doesn't surface (unconfirmed; should spot-check post-cancel).

**Before the May 30 decision point:**
- [x] Lists already exported from Linkt to Google Drive per Kay (confirmed 4/17)
- [ ] Run Linkt enrichment on Premium Pest Management NYC subset (owner emails) during the free month — burn credits while the cost is $0
- [ ] Observe DealsX performance post-5/7 launch to determine if it covers Linkt's list-building role
- [ ] Spot-check Apollo coverage on 2-3 active niches vs. what Linkt provided
- [ ] May 30: reassess — cancel, renew, or continue on Starter

**Re-activation trigger:**
Per `feedback_linkt_cancelled` — re-subscribe in sprints only. Specifically: if a future niche activation requires rapid bulk list-building beyond Apollo's comfortable scripting threshold (e.g., 500+ companies in 48 hours), consider a single-month Linkt re-sub for that sprint, then cancel again.

**Owners:**
- CFO (tech-stack ROI decision)
- CIO (list-building infrastructure for active niches)

---

## (Future entries append below)

---
date: 2026-04-27
type: context
title: "Continuation — 2026-04-27 #2"
saved_at: 2026-04-27T20:30:00Z
session_number: 2
tags: ["date/2026-04-27", "context", "topic/continuation", "topic/dealsx", "topic/outbound", "topic/ai-friday"]
---

## Session Summary

Reviewed the AI Friday Granola notes ("Building an AI-Powered Outbound Engine That Converts", Apr 24 2026) for takeaways applicable to G&B's outbound buildout. Then audited the DealsX cold outreach campaign playbook through that lens. Researched TitanX (phone propensity), Handwrytten (robot-arm direct mail), Apollo job-postings endpoint. Saved 3 durable memories. 4 action items pending Kay's YES / NO / DISCUSS.

## Active Threads

### 1. DealsX campaign playbook — 7-item edit list awaiting Kay's send approval
**Doc:** https://docs.google.com/document/d/1l2ha5-ZzMYgjUrVe25rPI2FpiG6xJEJihbJyHVEia3s/edit

**Awaiting Kay's YES / NO / DISCUSS** before sending DealsX a consolidated edit list.

The 7 items:
1. **Kill `{{employee_count}}` token in Hyper-Personalized Email 2** — violates `feedback_no_revenue_in_outreach`. The line "A team of {{employee_count}} people doing that level of work…" reads as PE-due-diligence.
2. **Strip "Managing Partner of Greenwich & Barrow" from first lines of v1 emails** — conflicts with position-as-person rule. Affects Origin Story + Honest Question variants.
3. **Reframe "Most buyers would ruin {{company_name}}" + "The wrong buyer would undo everything"** — manufactured threat, not survival-brain done right. AI Friday's framing is naming a discomfort they *already feel* (succession uncertainty), not catastrophizing. Blocked by `feedback_outreach_about_them`.
4. **Reword "Companies where the founder's fingerprint is on everything" + "high-touch, relationship-driven companies in the {{Industry}} space"** — leaks thesis. Violates `feedback_outreach_no_strategy_leaks`.
5. **Fix token placement** — `{{company_name}}` at end of sentences ("Closing the loop on {{company_name}}", "Would you ever consider selling {{company_name}}…") is the exact slop pattern AI Friday flagged. Embed earlier in sentence.
6. **Add Kay's "Learning/Curiosity" variant as Email 1 v5** across General + Luxury sequences. All current sequences are 100% direct-acquirer. Kay was already A/B testing this.
7. **Add option to Email 5 breakup** — current 1/2/3 reply menu skips a "send me to the right person" option. Useful for broker/intermediary recovery.

### 2. Apollo job-postings hiring-signal feature — pending bead creation
Apollo (already paid for) exposes `latest_job_postings` + intent signals endpoint. We don't use it. Cheapest path to AI-Friday-style hiring-signal detection — already in stack, no Clay $800/mo needed. Target hiring CFO/COO/head of finance often = pre-sale signal.

**Awaiting Kay's YES / NO / DISCUSS** on bead-ing as target-discovery enhancement, scoped to first niche as test.

### 3. TitanX — pending demo call decision
Phone Intent platform. Claims 3-7% baseline → 20-30% connect rate. Sits on top of existing dialer.
**Caveat:** Training data heavy on tech/SaaS. Heritage business owner distribution shift. Lift could be smaller.
**JJ math:** Current ~5% × 30-50 dials/day = ~2 connects/day. If 25%, ~12/day = 6x lift.
**Pricing:** Not public. Probably $1K-3K/mo enterprise tier ($27M Series A signal).

**Awaiting Kay's YES / NO / DISCUSS** on submitting their contact form for demo + pricing before deciding.

### 4. Handwrytten direct mail pilot — pending niche selection
Vendor: Handwrytten (Phoenix AZ, robot-arm, JSON API). $3.25/card with bulk discounts.
**10-target pilot cost:** ~$32.50 with stock cursive, +$1,500 one-time for Kay's handwriting digitized.
**Target shape:** owners in Active-Outreach niche where (a) Kay sent email + got no response, (b) heritage/multi-generational business, (c) mailable address from public records. Use as "I emailed twice, wanted to try this instead" pattern interrupt.

**Awaiting Kay's YES / NO / DISCUSS** + niche selection before bead-ing.

### 5. Channel architecture clarification (durable correction — already saved)
Kay corrected my AI Friday review: I categorized "high-volume cold email infrastructure (30+ domains, SmartLead, spin tax)" as a reject. **DealsX IS that layer for us.** Two channels coexist:
- **Kay Email:** low-volume, warm-intro-required, sent from Kay's domain. No mass infra.
- **DealsX Email:** high-volume cold, DealsX-managed infrastructure. They own infra entirely.

Saved as `feedback_dealsx_is_cold_email_infra.md` — this won't recur.

### 6. Attio MCP disconnected (mechanical, resolves on restart)
End-of-session reminder noted Attio MCP server disconnected. Will reconnect on Claude Code restart. No action needed.

## Decisions Made This Session

- **APPROVE:** DealsX is cold-email infrastructure, not a rejected pattern. Saved as durable memory.
- **APPROVE:** AI Friday outbound principles framework saved as reference for future copy reviews.
- **DEFER:** All four action items (DealsX edit list, Apollo job-postings bead, TitanX demo, Handwrytten pilot) — awaiting Kay's YES/NO/DISCUSS in next session.

## Memories Written This Session

- `feedback_dealsx_is_cold_email_infra.md` — durable correction on channel architecture
- `reference_ai_friday_outbound_principles.md` — 6-principle outbound copy review checklist
- `reference_outbound_vendors.md` — TitanX + Handwrytten + Apollo job-postings vendor pointers

## Resume Cue

When session resumes: present the 4 pending YES/NO/DISCUSS decisions (items 1-4 above) for Kay's call. After her decisions, execute downstream:
- DealsX edit list → Slack/email to DealsX
- Apollo job-postings → bead creation
- TitanX → contact form submission
- Handwrytten → niche selection then pilot spec

**Pre-existing threads from `continuation-2026-04-27-1.md`** (Excel To Do tracker rebuild blocked by AutoSave) remain open and unaffected by this session. That thread requires Kay to fully quit Excel before next attempt.

**Pre-existing threads from `continuation-2026-04-26-1.md`** (dashboard-as-source pivot for weekly-tracker, cadence sweep, weekly-tracker backfill) remain open and unaffected.

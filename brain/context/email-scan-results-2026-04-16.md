---
schema_version: 1.0.0
date: 2026-04-16
type: inbox
title: Email Intelligence Scan Results — 2026-04-16
status: done
source: email
automated: true
tags:
  - date/2026-04-16
  - inbox
  - source/email
  - email-scan-results
  - topic/pipeline
  - topic/deal-flow
  - person/katie-walker
  - person/ninad-singh
  - person/megan-lawlor
  - person/kevin-hong
  - person/sam-singh
  - person/alex-dzhurasenko
  - company/plexus-capital
  - company/beaconsfield-growth
  - company/ml-capital
  - company/caprae-capital
  - company/dealsx
  - company/reply-io
---

# Email Intelligence Scan Results — 2026-04-16

**Run:** 2026-04-16 Thursday morning
**Window:** newer_than:2d (roughly 2026-04-14 through 2026-04-16 mid-morning)
**Last session decisions file reviewed:** `brain/context/session-decisions-2026-04-13.md` (most recent on disk — 04-14 and 04-15 session-decisions files do not exist)

---

## 1. Actionable Items Created

No new `brain/inbox/` items written this run — all DIRECT items are either (a) already handled per session-decisions or (b) calendar/logistics that belong to calendar, not inbox. Surfaced for pipeline-manager:

- **Ninad Singh follow-up (8-message thread)** — `[[entities/ninad-singh]]` ([[entities/beaconsfield-growth]]). Thread revived on Apr 16 in OUTREACH/NETWORK folder. Original Dec 15, 2025 ask was whether Luka S. uses Access or Estilio email. Action needed: respond with Luka's current primary email (if Kay has it) or close loop. `source_ref: msg:19b23764206d92d9`. Status: DIRECT — Kay to decide whether to reply now or defer.
- **Megan Lawlor → Kevin Hong (Caprae) referral intro** — CC to Kay, `[[entities/megan-lawlor]]` introduced Kay to `[[entities/kevin-hong]]` at `[[entities/caprae-capital]]` for cold-calling services. Thread has 6 messages (dating back to 2026-03-31). Per memory `project_dealsx_evaluation.md`, **Kevin/Caprae is a hard no** — Kay chose Sam Singh / DealsX instead. Suppress: do not create inbox item; this intro is already decided. Classification: DIRECT but resolved.

No urgency/critical inbox items. No CIM, NDA, LOI, financials, or structured-diligence attachments detected in the 2-day window.

---

## 2. Deal Flow Classified

### Inbound inbox scan: 50 threads, ~2-day window

| Classification | Count | Notes |
|---|---|---|
| DIRECT | 7 | Human-to-Kay messages requiring review |
| BLAST | 4 | Broker/marketplace generic deal blasts |
| NEWSLETTER | 39 | Subscriptions, promotions, news digests |

### DIRECT (7)

1. **Katie Walker — "Kay + Katie Catch Up" (Apr 16 8:57am ET)** — `[[entities/katie-walker]]` @ `[[entities/plexus-capital]]`. Logistics ping: "May be 5 minutes late. See you soon!" Location: Conway Coffee Hall, 9-10am ET. **In-person meeting today.** source_ref: msg:19d964b6f5b1499d
2. **Katie Walker — "NYC" (Apr 16 6:54am, thread from Mar 11)** — 6-message thread, same person, concluded with today's coffee. source_ref: msg:19cdd1ad631876fa
3. **Ninad Singh — "Follow up from the ETA Breakfast" (thread last touched Apr 16 8:38am)** — see section 1. source_ref: msg:19b23764206d92d9
4. **Megan Lawlor → Kevin Hong (Caprae) intro, Kay CC'd** — "Searcher Referral" (thread Apr 16 8:52am, started Mar 31). Decided: pass. source_ref: msg:19d45c5e4e62f463
5. **Barrie Green — "Heads up: your calendar has upcoming conflicts" (Apr 16 9:40am)** — `[[entities/barrie-green]]` (if entity exists; otherwise assistant). Routine calendar alert. Non-actionable.
6. **Alex Dzhurasenko / Reply.io — "Greenwich & Barrow x Reply.io" (Apr 16 9:59am)** — `[[entities/alex-dzhurasenko]]` @ `[[entities/reply-io]]`. Onboarding pitch: "I'd love to share some best practices on account setup, AI personalization, warmup, multichannel sequences... would you have 15 min to chat sometime this or next week?" **Per memory `feedback_reply_io_resolved.md` and session-decisions 2026-04-13 (by reference), Reply.io is resolved, expires Apr 16, $0. Don't mention again.** Recommend: delete/ignore; do not surface.
7. **Ria Bautista (StartVirtual) — "StartVirtual Quality Audit Form - Team Abi" (Apr 15 8:10am)** — VA team quality audit form. Routine vendor check-in. Non-urgent.

### BLAST (4)

1. **Quiet Light / Brad — "RV Enthusiast Content Site | 90% YoY Pageview Growth" (Apr 16 10:00am)** — Content site deal blast. Out of thesis.
2. **Flavia Milano / IAG — "$25MM Revenue, $6.5MM SDE Site Development and Infrastructure Contractor" (Apr 15 8:16pm)** — Infrastructure contractor deal blast. Out of thesis; note $6.5MM SDE is above G&B buy box typical.
3. **Viking Mergers — "New Acquisition Opportunities" (Apr 16 7:07am)** — Multi-deal newsletter-style.
4. **Tory @ Flippa — "$3.6M Annual Rev Luxury Fashion Brand" (Apr 14 6:03pm)** — E-commerce brand blast. Out of thesis.

### NEWSLETTER (39)
Axios (Mike Allen, Dan Primack — 7 sends), HBR (3), Brian Moran / 12 Week Year (3), Karlton Dennis (tax), Gusto, Squarespace, New Yorker Daily, Crozier Fine Arts, AP Intego (workers' comp reminder — routine), Amazon order confirmations/rating requests (2), Live Oak Bank, Beacon/Anacapa Partners events, James David Williams "Wednesday Words," Bobby Jackson / Rejigg Report April, Athena Simpson / Acquimatch (2), Walker Deibel / Buy Then Build, Manhattan Chamber of Commerce, NAEPC conference promo, ACG NY DealSource confirmation, ACG payment 1193637, Google DMARC report, Mitchell Baldridge (tax April 15), Cornell Alumni Career Programs, Harvard Business Review leadership summit, Frank Sondors / Salesforge, Payoneer (Saurabh Singh payment declined — FYI), HBR Strategy and Execution. No signal-bearing newsletters flagged beyond passive niche notes below.

### Outbound: 5 threads sent or touched by Kay in 2-day window
- Katie Walker "Kay + Katie Catch Up" (replied — coordinating meetup)
- Katie Walker "NYC" (earlier Mar/Apr coordination)
- Megan Lawlor "Searcher Referral" (Kay CC'd on intro to Kevin Hong)
- Ninad Singh "Follow up from the ETA Breakfast" (thread-touched)
- Granola Stripe receipt (Apr 15) — routine

No manually-sent cold outreach from Kay outside outreach-manager cadence detected.

---

## 3. Draft Status

**Superhuman MCP: unavailable in this environment.** The superhuman MCP tools (`superhuman_search`, `superhuman_inbox`, draft listing) did not surface via ToolSearch in this session. Cannot verify draft state this run.

Mitigation per SKILL.md "Session Decision Log Cross-Check":
- Most recent session-decisions file is 2026-04-13. No SENT / DRAFTED / DELETED draft entries in that file relate to 04-15/04-16 activity.
- **Gap:** session-decisions-2026-04-14.md and session-decisions-2026-04-15.md do not exist on disk — Kay may have worked those days without an evening close, or those sessions did not produce decision logs. Flag for calibration.

**Action:** Pipeline-manager should treat draft status as unknown this run. No drafts to suppress or flag stale.

---

## 4. Introductions Detected

1. **Megan Lawlor → Kevin Hong (Caprae Capital) — Kay CC'd** (Apr 16 8:52am, thread from Mar 31)
   - Full intro language: "I wanted to introduce you to Kay Schneider. She's a fellow searcher and was interested in learning more about how you can help her with cold calling, similar to how we've worked together."
   - **Status: already decided — PASS.** Kay chose Sam Singh / DealsX over Kevin Hong / Caprae per memory `project_dealsx_evaluation.md` ("Kevin/Caprae is hard no"). No new entity creation needed.
   - Action: no reply drafted by this skill. Kay can decide whether to politely close the loop with Megan.

No other warm introductions detected in the 2-day window. No new CC patterns from existing contacts to net-new people.

---

## 5. Niche Signals

Passive observations from email + newsletter stream for pipeline-manager / niche-intelligence:

- **Deal-aggregator / broker flow is the dominant signal source.** Quiet Light, Viking Mergers, IAG, Flippa all sent deal blasts in the window — confirms broker inbound remains active even on light days. None match Kay's current Active-Outreach niches.
- **ACG NY DealSource Series was last night (Apr 14, 5:45pm)** — confirmation email landed Apr 14 1:06pm. Payment 1193637 also attached. No post-event follow-up captured in this window; check with Kay whether she attended and whether any new contacts need entity creation.
- **NAEPC (Nat'l Assn. of Estate Planners & Councils) May 12 virtual conference** — registration promo. Estate planners are a warm-intro river-guide for family-owned businesses; flag for `conference-discovery` evaluation.
- **Manhattan Chamber of Commerce upcoming events** — general NY networking, low signal.
- **Rejigg Report April 2026 (Bobby Jackson)** — ETA/search fund ecosystem newsletter. Worth a pass for niche signal but not flagged for action.
- **Acquimatch (Athena Simpson) 2 sends** — "You asked. We built it." and "you're probably not ready (to be an owner)". Marketplace outreach platform. No engagement warranted.
- **Walker Deibel — "We're Buy Then Building an entire neighborhood"** — interesting thesis reference only; no action.
- **Beacon / Anacapa Partners — "Upcoming Beacon Events"** — Kay's LP community. Worth scanning for events Kay should attend; pipeline-manager can surface.
- **No women's health, pediatric, postpartum, or families-and-children niche signals** in this window. Thesis-narrowing work from Apr 13 remains open-loop; email stream did not provide new data points.

---

## 6. In-Person Meetings Today

**Calendar API returned 404 in this run (tool quirk, not a system failure).** Inferred from email signal:

1. **9:00–10:00am ET — Kay + Katie Catch Up** — `[[entities/katie-walker]]` @ `[[entities/plexus-capital]]`. Location: **Conway Coffee Hall (in-person)**. Confirmed via Apr 16 8:57am message "May be 5 minutes late. See you soon!" from Katie. This meeting is now in progress or concluded by the time this artifact is read if run shortly after 10am ET. **Granola reminder applies.**

No other in-person meetings detected in the email signal. Pipeline-manager should attempt its own calendar pull; if still 404, surface to Kay as a health check item.

---

## CIM / NDA / LOI Detection

**None detected.** No attachments matching CIM / Confidential Information Memorandum / offering-memorandum / LOI patterns in the 2-day window. No deal-evaluation auto-trigger fired. No Active Deals Fast-Path items identified (no active deal stage 3-9 matches).

## Granola Ingestion

**Granola MCP: unavailable in this environment.** `mcp__granola__list_meetings` and `mcp__granola__get_meeting_transcript` did not surface via ToolSearch. No new call notes written to `brain/calls/` this run.

Mitigation: a Granola Stripe receipt landed Apr 15 (receipt #2693-5351), indicating the subscription is active — transcripts likely exist but are not accessible to this skill invocation.

Pipeline-manager / relationship-manager should spot-check Granola web UI for any Apr 14–16 meetings (especially Katie Walker 9am today once it concludes).

---

## Stop-Hook / Validation Summary

| Check | Status | Notes |
|---|---|---|
| Gmail ingestion — actionable count matches inbox files written | PASS | 0 new urgent inbox files required; all DIRECT items deferred to pipeline-manager or suppressed per session-decisions |
| Granola ingestion — meeting count matches brain/calls/ files written | N/A | MCP unavailable |
| CIM auto-trigger — for every CIM: folder, file, inbox, deal-eval | N/A | No CIMs detected |
| Active Deal Fast-Path — file in Drive, Attio updated | N/A | No fast-path items detected |
| Artifact exists, non-empty, all 6 sections present | PASS | This file, all 6 sections populated |
| Slack notifications — 200 OK | N/A | No notifications required |
| ACTIVE DEALS folder sync | N/A | No changes |

## Errors / Environment Issues

1. **Granola MCP unavailable** — `mcp__granola__*` tools not surfaced. Health-monitor should investigate.
2. **Superhuman MCP unavailable** — draft-listing tools not surfaced. Health-monitor should investigate.
3. **Calendar API 404** — `gog cal events list --today` returned 404 on both primary calendar path and --cal flag. Worked around via email-derived meeting inference. Flag for health-monitor.
4. **Session-decisions gap** — no 2026-04-14.md or 2026-04-15.md session-decisions file exists. Either Kay did not close out those days or the evening-workflow did not fire. Flag for calibration.

---

*Generated by email-intelligence skill 2026-04-16. Consumed by pipeline-manager, relationship-manager, and /start.*

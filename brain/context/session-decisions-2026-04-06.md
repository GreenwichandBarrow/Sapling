---
schema_version: 1.1.0
date: 2026-04-06
type: context
title: "Session Decisions — April 6, 2026"
sessions: 2
last_updated: 2026-04-06T20:00:00Z
tags: ["date/2026-04-06", "context", "topic/session-decisions"]
---

# Session Decisions — April 6, 2026 (Monday)

## Session 1 — Early morning (pre-existing, overnight)

- APPROVE: Two-document cold calling system — static Niche Call Guide + Daily Call Tab
- APPROVE: Daily Call Tab lives on master target sheet as a new tab per day
- APPROVE: JJ's role is connector only — book intro call with Kay, no qualifying, no deal discussion

## Session 2 — Monday Morning Briefing + Work Session

### Decisions

- APPROVE: Domain protection — SPF, DKIM, DMARC all configured on greenwichandbarrow.com. DMARC at quarantine, tighten to reject in 2 weeks.
- APPROVE: G&B Cold Call Guide restructured as universal (not niche-specific). Based on Kevin Hong's Caprae LeadGen Guidelines as foundation.
- APPROVE: Niche context moved to target sheet tab (not in guide). Pest Management "Niche Context" tab created.
- APPROVE: Guide simplified for overseas caller — JJ redirects all deep questions to Kay, does not write follow-up emails (we draft), does not discuss deal structure.
- APPROVE: Lukewarm handoff model — JJ makes first contact, Kay follows up as principal. Added to guide.
- APPROVE: Ice-and-recall — "Not Interested" targets recycled after 4-6 weeks. Added to guide.
- APPROVE: JJ daily target stays at 40 calls/day.
- APPROVE: Schwartzman is a PASS (one man show). Margot Romano gave advice Apr 4, no intros offered.
- APPROVE: Kevin Hong / Caprae Capital is a HARD NO for service engagement. Success fee (up to $300k, % of EV) would expose relationship to investors. Value was the call — playbook captured in guide.
- APPROVE: DealsX (Sam Singh) is the leading candidate for outsourced email + LinkedIn outreach. $1,500/mo, $25k flat success fee, month-to-month. Waiting on deck and references before committing.
- APPROVE: Mark Gardella reply drafted — honest about not having formal TAM, references Brown & Brown/Accession deal, keeps Markel intro alive.
- PASS: Attio next_action items (Rachel Tepper, Dan Tanzilli) — don't surface these in briefings.

### Actions Taken

- CONFIGURED: SPF record on greenwichandbarrow.com (v=spf1 include:_spf.google.com ~all)
- CONFIGURED: DKIM on greenwichandbarrow.com (2048-bit, google selector)
- UPDATED: DMARC from p=none to p=quarantine with rua reporting
- VERIFIED: No blocklisting on MxToolbox (warnings only, no red flags)
- CREATED: G&B Cold Call Guide Google Doc (12Hqfwxg4qJA3YdZh36ndd-flvYgWNZeL8sMZ9NAHlTY) in Operations/Call Logs
- CREATED: Niche Context tab on Pest Management target sheet
- UPDATED: jj-operations SKILL.md — universal call guide doc ID wired in
- SENT: Slack to JJ — shift from validation to outreach, 40 calls/day, guide link, request for feedback
- DRAFTED: Mark Gardella reply (presented for Kay review, not yet sent)
- ENRICHED: 17 Northeast pest management targets with owner names via Apollo (11 NY metro + 6 expanded geo)
- CREATED: email-scan-results-2026-04-06.md artifact
- CREATED: relationship-status-2026-04-06.md artifact
- DRAFTED: Sam Singh follow-up email (references request). Gmail draft created in error — Kay sending from Superhuman manually.
- CREATED: 5 Art Advisory Day 0 draft emails (presented for review, not yet approved)

### Deferred

- DEFER: Art Advisory 5 drafts — presented but not reviewed yet. Resume next session.
- DEFER: Fractional CFO drafts — blocked on Art Advisory review and sequencing decision (interleave vs sequential)
- DEFER: Email sequencing decision — Art Advisory first, then interleave CFO? Discuss next session.
- DEFER: Philip Hoffman warm intro — TBD, Kay hasn't decided path (Ana/Anton/Chris Wise)
- DEFER: Pest Management owner enrichment — 17 targets enriched, need to go national (Kevin confirmed blue collar works in NY but recommended remote/distributed for best results)
- DEFER: Install launchd jobs — intermediary-manager, jj-operations, conference-discovery all need plist installation
- DEFER: Conference-discovery Monday run — skill still in draft, launchd not installed
- DEFER: Superhuman draft script — needs to be installed so drafts go to Superhuman not Gmail
- DEFER: DMARC tighten to p=reject — 2 weeks from now (~Apr 20)
- DEFER: Handwritten letter service — add to outreach after cold calling is running smoothly
- DEFER: Sam Singh / DealsX engagement — waiting on references and deck review
- DEFER: Levi (Acumen) email — scheduled send in Superhuman missed. Still in drafts. Kay to re-send.
- DEFER: Mark Gardella reply — drafted, Kay to review and send
- DEFER: Overdue contacts (Carlos Nieto, Kanayo, Michael Topol, Kristina Marcigliano, Lauren Della Monica) — same 5 from prior sessions

### Open Loops

- DealsX references and deck — Sam sent both. Kay wants to talk to references before committing.
- Kevin Hong's value captured in guide — no service engagement, hard no.
- If Sam takes over list building + email + LinkedIn, shifts focus: outreach-manager becomes reply management, deal-evaluation skills get real use, JJ stays as parallel cold calling channel.
- Kay needs 2 more high-volume niches for Sam (pest management is 1 of 3 needed).
- Domain: SPF + DKIM live, DMARC at quarantine. Check in 2 weeks to tighten.
- greenwichbarrow.com (without "and") exists on Squarespace — web team may have registered. Confirm.
- JJ guide shared as working document — awaiting his feedback.
- Salesforge trial — deletion requested, letting expire.
- Kay is a traditional funded searcher with ~12 months remaining in search timeline (started Feb 2025).

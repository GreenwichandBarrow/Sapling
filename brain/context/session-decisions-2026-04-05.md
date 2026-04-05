---
date: 2026-04-05
type: context
sessions: 3
last_updated: 2026-04-05T12:45:00Z
---

# Session Decisions — April 5, 2026

## Session 1 — Overnight (Autonomous Execution + Salesforge Disconnection)

## Decisions

- APPROVE: Disconnect Salesforge entirely — mailbox deleted, LinkedIn removed, Google Admin blocked, MCP config removed
- APPROVE: 5 owner emails/day hard stop starting April 5 — no zero days
- APPROVE: Evaluate outreach model — personal send (Claude drafts, Kay sends 5/day) vs outsourced (DealsX, Austin's tool)
- APPROVE: Cross-validate Art Advisory targets against Linkt's old lists before proceeding

## Actions Taken

- CREATED: scripts/col-lookup.py — full Python rewrite of col-lookup.sh (bash 3.2 doesn't support associative arrays). All 4 modes tested: column, batch, cell, range.
- UPDATED: scripts/col-lookup.sh — now thin bash wrapper delegating to col-lookup.py
- UPDATED: .mcp.json — Linkt removed (cancelled), Salesforge removed (spam/disconnected)
- UPDATED: scripts/.env.launchd — LINKT_API_KEY replaced with SALESFORGE_API_KEY
- UPDATED: ~/.zshrc — LINKT_API_KEY replaced with SALESFORGE_API_KEY, duplicate aliases cleaned
- UPDATED: Art Advisory target sheet — Winston Artory Group (Row 5) marked Pass (VC-backed: Strobe Ventures, CMT Digital, Galaxy Digital). 67 other targets cleared PE check.
- UPDATED: Fractional CFO target sheet — 25 targets auto-approved, 3 marked Pass (Breakwater = Cultivate Advisors, Cascade CPA = Northspring Partners, Kiwi Partners = Arabella Advisors)
- DELETED: Salesforge MCP connection from .mcp.json

## Deferred

- DEFER: Skill migrations to header-based column lookups — col-lookup.py works, incremental migration starting with Pest Management test
- DEFER: Outreach-manager skill rewrite — blocked on outreach tool decision
- DEFER: Salesforge trial cancellation — Kay may want to formally cancel vs let expire
- DEFER: Reply.io trial cancellation — ~11 days remaining
- DEFER: Linkt cross-validation of Art Advisory targets — compare data quality
- DEFER: Schwartzman warm intro routing — needs Kay's decision
- DEFER: Premium Pest Management initial target load

## Open Loops

- Outreach tool decision: personal-send vs outsourced — determines entire outreach-manager architecture
- Art Advisory 67 targets ready for outreach — blocked on tool decision
- Fractional CFO 25 approved targets — blocked on tool decision
- 5 emails/day starting today — need to build draft workflow
- Linkt cross-validation against Art Advisory targets
- Schwartzman & Associates warm intro via Margot Romano
- Reply.io trial ~11 days — cancel before charge
- Salesforge trial ~11 days — disconnected, decide formal cancellation
- Premium Pest Management initial target load
- 6+ skills need migration to header-based column lookups

---

## Session 2 — Morning (Salesforge Security + Outreach Redesign)

## Decisions

- APPROVE: Change G&B Google Workspace password immediately — Salesforge SMTP credentials compromised, sending spam from Kay's account
- APPROVE: Revoke unrecognized third-party app access (including Cronofy)
- APPROVE: Request Salesforge account deletion via chatbot
- APPROVE: Cancel Reply.io (let expire, ~10 days)
- APPROVE: New outreach model — Claude drafts in Superhuman, Kay sends. No third-party tool ever gets SMTP credentials again.
- APPROVE: 5 emails/day, every weekday, no zero days. 25+ per week.
- APPROVE: Day 0 emails Kay reviews. Day 3/6/14 follow-ups Kay just hits send (no review needed).
- APPROVE: LinkedIn DMs surfaced in briefing with message + URL, Kay pastes and sends
- APPROVE: Real-time tracking — Kay confirms "looks good" → Claude immediately updates sheet + Attio
- APPROVE: Attio notes for LinkedIn DMs (logged when Kay confirms sent)
- APPROVE: No staggering — 5/day straight through
- APPROVE: Kevin Hong call tomorrow (Mon 12:30pm) — take the call to learn, still plan to decline Caprae after
- APPROVE: Levi (Acumen) email scheduled for Monday 8am — creative structure pitch (investor + growth partnership)
- APPROVE: JJ fully decoupled from email cadence, focused on Pest Management cold calling
- APPROVE: Premium Pest Management target list build today (deferred from session — next session)

## Actions Taken

- UPDATED: G&B Google Workspace password (killed Salesforge SMTP access)
- UPDATED: Re-authenticated Attio, Superhuman, gog after password change
- DELETED: Unrecognized third-party app access (Cronofy, others)
- SENT: Salesforge account deletion request via chatbot (confirmed by Ankit)
- UPDATED: Art Advisory target sheet — 10 phone numbers patched from Linkt CSV export
- UPDATED: outreach-manager/SKILL.md — complete rewrite removing Salesforge, adding Superhuman + Claude cadence tracking model
- UPDATED: pipeline-manager/SKILL.md — all Salesforge references replaced with target sheet + Attio tracking
- COMPLETED: Linkt vs Apollo comparison for Art Advisory — all 14 Linkt companies already on Apollo sheet, zero new targets. Apollo wins volume (80 vs 14), Linkt wins phone enrichment.

## Deferred

- DEFER: Morning briefing — interrupted by Salesforge security emergency, never completed
- DEFER: Premium Pest Management target discovery — next session (read ICP from scorecard, don't ask Kay)
- DEFER: JJ cold call script for calls-first channel (not "following up on email" — true intro)
- DEFER: jj-operations skill update for calls-first flow
- DEFER: Outreach-manager channel flag per niche (email-first vs calls-first)
- DEFER: Pipeline-manager full briefing sections (pipeline shifts, summary, action items, carried items, system status)
- DEFER: Domain reputation check for greenwichandbarrow.com after spam incident

## Open Loops

- Kevin Hong call tomorrow Mon 12:30pm — learn, then decline Caprae
- Levi (Acumen) email scheduled Monday 8am
- 67 Art Advisory targets ready for Day 0 emails — start tomorrow
- 25 Fractional CFO targets ready — blocked on same workflow (starts tomorrow)
- Premium Pest Management target list — next session
- JJ calls-first workflow needs building (script, jj-operations update, channel config)
- Reply.io trial ~10 days — let expire
- Salesforge trial ~10 days — account deletion requested, let expire
- Schwartzman warm intro routing — still needs Kay's decision
- Domain reputation check pending

---

# Session 3 — Sunday Morning (Outreach Templates + Target Sheet Redesign + Pest Management)

## Decisions

- APPROVE: Per-touchpoint outreach tracking columns (Variant, Day 0 Sent, Day 3 Sent, Day 6 DM Sent, Day 14 Sent, Cadence Status) replacing single Outreach Stage column
- APPROVE: "Year Founded" and "Rev Source" columns added to all target sheets (from Caprae LeadGen template review)
- APPROVE: "LinkedIn Connection" column moved next to LinkedIn (Owner) for Kay to mark 1st/2nd/3rd degree
- APPROVE: Variant A Day 0 template rewritten — curiosity framing, light on target, "After a decade in the luxury world, I recognized the client crossover in the art world and have been really curious to learn more about art advisory"
- APPROVE: Variant B Day 0 template rewritten — direct intent, branding session content: father's entrepreneurship, mix of art and commerce, Chanel, "acquire one business and run it myself, full time"
- APPROVE: Kevin Hong branding pointers added to cadence doc — concise, every sentence adds value, bold and personable
- APPROVE: LinkedIn links included with every draft presentation (new standard for morning briefings)
- APPROVE: 4 new hard stops in target-discovery: HQ country verification, solo practitioner check, business type verification, company age (<5 years)
- APPROVE: Young owner check (<35) as soft filter in target-discovery
- APPROVE: Philip Hoffman routed as warm intro (2nd connection) — explore intro via Ana, Anton, or Chris Wise
- PASS: Todd Levin (one-man shop), Gurr Johns (London HQ), Beaumont Nathan (London HQ), Capital Art Advisory (one person, too young), Arcadia (owner too young), Kinzelman (one person), Private Art Consulting (design firm, not advisory)
- APPROVE: Premium Pest Management target sheet created, Apollo search in progress

## Actions Taken

- CREATED: 6 outreach tracking columns on Art Advisory sheet (Variant through Cadence Status)
- CREATED: Premium Pest Management target sheet (ID: 1Y0ZjEkc2LHhBoO4QGO8Ny9MvG90NpojQn8bloKA291I)
- UPDATED: Art Advisory sheet — 66 targets marked "Approve", 14 marked "Pass"
- UPDATED: Art Advisory sheet — "Rev Source" column inserted, "Year Founded" column added
- UPDATED: Art Advisory sheet — "LinkedIn Connection" moved next to LinkedIn (Owner)
- UPDATED: All 5 other target sheets aligned with new column layout (Rev Source, Year Founded, outreach tracking)
- UPDATED: outreach-manager/SKILL.md — both Day 0 templates rewritten, hard rules updated, variables simplified
- UPDATED: pipeline-manager/SKILL.md — Outreach Stage references replaced with per-touchpoint columns
- UPDATED: jj-operations/SKILL.md — column references updated
- UPDATED: target-discovery/SKILL.md — 4 new hard stops + 1 soft filter added
- UPDATED: list-builder/SKILL.md — column template updated with all new fields
- UPDATED: user_outreach_voice.md — branding session beats and key lines added
- UPDATED: G&B Cold Email Outreach Cadence doc on Drive — Variant A and B Day 0 rewritten (Kay updated)
- CREATED: feedback_linkedin_in_drafts.md — always include LinkedIn links with draft presentations
- MARKED: Philip Hoffman as 2nd connection on Art Advisory sheet

## Deferred

- DEFER: Art Advisory re-run with new stop hooks — tomorrow morning, present 5 clean drafts
- DEFER: Pest Management Apollo enrichment — search running, need to filter before spending credits on phone reveals
- DEFER: Variant B follow-up templates (Day 3/6/14) — may need updating to match new Day 0 tone
- DEFER: JJ cold call script for Pest Management
- DEFER: Philip Hoffman warm intro — surface in Monday briefing with Ana/Anton/Chris Wise paths

## Open Loops

- Pest Management Apollo search in progress — hundreds of results, need filtering before enrichment. JJ needs calls for Monday.
- Art Advisory 5 clean drafts needed — re-run with new stop hooks tomorrow
- Philip Hoffman warm intro routing — Ana, Anton, or Chris Wise
- Reply.io trial expires April 16 — no action needed, $0 invoice
- Salesforge trial — account deletion requested, let expire
- Schwartzman warm intro — still needs Kay's routing decision
- Kevin Hong call Sunday 12:30pm
- Domain reputation check still pending

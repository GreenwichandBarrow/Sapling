---
date: 2026-04-02
type: context
sessions: 1
last_updated: 2026-04-02T18:30:00Z
---

# Session Decisions — April 2, 2026

## Decisions

- APPROVE: Art Advisory moved to Active-Outreach on tracker. Thesis finalized: capital-light entry point into art value chain, fragmented market, 30-50% EBITDA margins.
- APPROVE: Art Advisory investment thesis rewritten (3 sentences, no growth drivers, no score, no G&B reference)
- APPROVE: Domestic TCI tabled — carrier concentration risk (Big 3 control 85%), no broker differentiation, countercyclical demand dependency
- APPROVE: TCI scorecard revised downward from 2.78 to 2.60 (87%) — supplier power, cyclicality, customer power, professionalization all marked down
- APPROVE: IPLC killed — AI vulnerability. AgentSync at $1.2B valuation actively automating the space. Service bureaus' moat is complexity that's being eliminated.
- APPROVE: Pipeline stage "Active-Diligence" eliminated from all skills. New pipeline: Under Review → Active-Outreach → Wind Down → Tabled/Killed
- APPROVE: Formal customer validation calls killed as pipeline gate. Validation now informal/parallel via Kay's network.
- APPROVE: Validation contacts still generated but simplified — one page, Slack to Kay, no scripts, no JJ. Prioritize Kay's network first, investor network if no warm contacts.
- APPROVE: Target list sheets standardized to 24 columns (A-X) across all 5 niches. Col X = Outreach Stage (trigger column).
- APPROVE: Agent Notes (Col Q) convention: start with "RECOMMEND: Approve" or "RECOMMEND: Pass" for calibration tracking
- APPROVE: Employee filter: 10+ for art advisory, 5+ for insurance niches
- APPROVE: Art advisory outreach is Kay-only (personal email, LinkedIn). No JJ cold calls for this niche.
- APPROVE: One-pager formatting rules: score as X.XX / 3.0 (XX%), no letter grades, no personal names, thesis ≠ growth drivers
- APPROVE: Briefing format updates: System Status section added, no completed items, no items Kay did herself, number everything including pipeline summary
- APPROVE: Morning briefing organized by action type with ascending numbering across all sections
- APPROVE: Reply.io MCP added to project config (needs restart to connect)
- APPROVE: Secret redaction hook built — scans Bash output for API keys/tokens before they hit conversation
- APPROVE: Superhuman CLI wrapper fixed — skips auth in happy path, 15s timeout on retry
- APPROVE: Apollo Basic confirmed working ($64/mo, 2,500 credits)
- APPROVE: list-builder skill created (Apollo API workflow, replaces Linkt as primary)
- APPROVE: DealsX call with Sam Singh moved to tomorrow (April 3)
- APPROVE: Kevin Hong Doodle call — Kay will decline, draft in Superhuman
- APPROVE: Investor paragraph drafted for Q4 catch-up email (skip Jeff/Anacapa and Guillermo/Ashford)
- PASS: California Property Tax Consultants — hard pass despite 70% margins, California soft filter
- PASS: Estate Management — AI replaceable (scheduling, coordination, logistics)
- PASS: Concierge Medicine — no healthcare domain knowledge, regulatory complexity, key-person risk
- PASS: Apollo geographic search (tri-state opportunistic) — same noise as JJ's lists, IT staffing dominated
- PASS: Art customs brokerage — volume business, thin margins per transaction, needs massive scale
- PASS: Trust administration — high multiples (7-9x EBITDA), modest margins (10-25%), PE already in space (GTCR)
- PASS: Estate planning firms — law firm ownership restriction in most states

## Actions Taken

- CREATED: Email scan results artifact for April 2
- CREATED: Mark Gardella entity (vault + Attio) + ZI Advisor company entity
- CREATED: Megan Lawlor call note ingested to vault from Granola transcript
- CREATED: Kevin Hong, Caprae Capital, Christine Kobel entities in vault
- CREATED: list-builder skill (.claude/skills/list-builder/SKILL.md)
- CREATED: Secret redaction hook (.claude/hooks/router/handlers/redact_secrets.py)
- CREATED: Mark Gardella thank-you draft in Superhuman
- CREATED: Acumen/Levi follow-up draft in Superhuman (investor offered to join call)
- CREATED: Kevin Hong decline draft in Superhuman
- UPDATED: All 5 target list sheets standardized to A-X (24 columns), Col X = Outreach Stage
- UPDATED: Freedman Risk Mgmt added to Art Insurance target list for JJ follow-up call
- UPDATED: Art Advisory target list — Apollo enriched 7 emails, added 19 new firms (5-50 employee filter), 26 sub-threshold rows flagged
- UPDATED: Art Storage target list — 7 new companies added via Apollo (ARTEX, Bohren's, Lowy, Red Hook Crating, Full Circle, IBI, Professional Art Handling)
- UPDATED: All 12 industry scorecards — total score formula fixed (weighted average calculation)
- UPDATED: TCI scorecard — 5 scores revised downward, total recalculated to 2.60
- UPDATED: TCI one-pager — score updated to 2.60 / 3.0 (87%), thesis rewritten, no letter grade
- UPDATED: IPLC one-pager — score updated to 2.60 / 3.0 (87%), status to Killed, thesis rewritten
- UPDATED: Art Advisory one-pager thesis rewritten (3 sentences, no score, no G&B)
- UPDATED: CLAUDE.md — System Status section added to briefing, briefing hygiene rules, Active-Outreach triggers
- UPDATED: niche-intelligence skill — Active-Diligence removed, validation contacts simplified, signal detection concept, network-first validation
- UPDATED: jj-operations skill — customer validation calls removed, Col X references updated
- UPDATED: pipeline-manager skill — Active-Diligence removed, post-meeting cleanup triggers added
- UPDATED: target-discovery skill — Linkt replaced with list-builder (Apollo), Active-Diligence throttle removed
- UPDATED: outreach-manager skill — Col X standardized, warm intro moved to Col Q, RECOMMEND prefix added
- UPDATED: calibration-workflow skill — Agent-Kay alignment tracking added
- UPDATED: one-pager-template reference — scoring format, thesis rules, no personal names
- UPDATED: Superhuman CLI wrapper — fixed hanging auth, try-first-retry-on-failure pattern
- UPDATED: Industry Research Tracker — TCI to 2.60, IPLC to 2.60
- UPLOADED: 127 contact data gaps fixed across all 5 target list sheets from Linkt CSV cross-reference
- MOVED: Old "Art Insurance Brokerage - Target List" to ARCHIVED LINKT EXPORTS

## Deferred

- DEFER: Reply.io MCP test → needs Claude Code restart. First priority tomorrow morning.
- DEFER: Art advisory target list review/approval → blocked on LinkedIn enrichment via Reply.io
- DEFER: DealsX call with Sam Singh → moved to April 3
- DEFER: Kevin Hong decline email → Kay sending later today/tomorrow
- DEFER: Investor Q4 catch-up emails → Kay reworking in OneNote, sending individually
- DEFER: Secondary sending domain registration → this week
- DEFER: Niche-intelligence redesign — shift from niche generator to signal tracker/antenna
- DEFER: Niche pipeline bottleneck — art ecosystem value chain fully explored, second niche needs to come from conversations/network signals
- DEFER: JJ geographic track — Apollo test produced same noise as JJ. No clear path for JJ cold calling.
- DEFER: Post-meeting tracker cleanup automation — designed but not yet coded as automatic trigger
- DEFER: Reply.io LinkedIn automation for target enrichment → after MCP connected
- DEFER: Q4 investor update → this week
- DEFER: Nikki Higgins draft, Denning Rodriguez draft → still needs Kay's direction
- DEFER: Superhuman CLI G&B token → was refreshed today but expires hourly
- DEFER: UPS mailbox renewal → Kay handling

## Open Loops

- Art advisory is ONLY niche in Active-Outreach. Pipeline is dry behind it.
- Niche pipeline bottleneck: top-down screening exhausted, ecosystem map tapped. Next niche comes from owner conversations, network signals, or conferences.
- Trust administration explored today — targets exist (50 companies, 10+ employees) but economics don't work for search fund (7-9x multiples, 10-25% margins, PE competition)
- PE trend analysis: fine art logistics being consolidated (Providence $1B+, TSG/Cadogan Tate, UOVO). Art storage/logistics in wind-down status but warming.
- Art advisory outreach is Kay-only — JJ doesn't have a productive niche to call into
- JJ test month running — validation calls produced zero conversations across 3 niches
- Reply.io trial expires ~April 15 — must test and decide
- Apollo credit budget: ~27 credits used today of 2,500/month
- Deloitte Art & Finance Report 2025 data extracted — key stats on family office outsourcing (85% outsource art advisory), next-gen collectors (80% want advisory vs 48% older), collection management surged to 93%
- Art advisory unit economics gap — no published firm-level revenue data. Molly at Goodman Taft emailed Mar 31, no reply. Revenue tiers estimated from court filings and APAA data.
- Margot Romano call Friday 10am (rescheduled from 9:30) — art advisory intel, West Village
- Megan Lawlor wants to connect on Claude Code — Calendly link shared
- Mark Gardella (InsurTech Spring) wants to make intros in insurance — thank-you draft sent
- Kevin Hong Doodle call Monday needs declining — draft in Superhuman
- StartVirtual QA form for JJ (Team Abi) — unanswered, relevant given JJ transition

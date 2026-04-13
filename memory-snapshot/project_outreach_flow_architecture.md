---
name: Outreach flow architecture — in flux, Salesforge disconnected
description: Outreach pipeline disrupted April 5 2026. Salesforge disconnected (spam). Apollo + Attio remain. Evaluating personal-send vs new tool.
type: project
---

## End-to-End Outreach Flow (Updated April 3, 2026)

1. Niche hits Active-Outreach on Industry Research Tracker
2. Target-discovery runs → Apollo (15+ keyword variations) + supplemental sources → populates target sheet
3. Slack to Kay: "Target list ready for review"
4. Kay reviews, marks Approve/Pass in Col O on target sheet
5. Morning briefing presents 5 rendered cold emails for Kay's review (Phase 1)
6. Kay approves batch → outreach-manager creates contacts in Salesforge with customVars
7. Pre-send email verification (Apollo verified = proceed, guessed/bounced = skip, LinkedIn only)
8. Creates Attio entry at "Identified" with verified email + contact data
9. Enrolls contact in Salesforge sequence via MCP API
10. Salesforge sends Day 0 email automatically through Gmail (A/B variant: Learning vs Direct)
11. Day 1: Bounce check → bounced + has LinkedIn → pivot to connection request
12. Day 2: LinkedIn profile view (warm social touch)
13. Day 3: Reply check → stop if replied
14. Day 5: Follow-up email (auto-send)
15. Day 7: Reply check + LinkedIn connection request if has URL
16. Day 10: Final email touch
17. Day 14: If connection accepted → LinkedIn DM
18. Pipeline-manager reads Gmail sent folder + Salesforge MCP → advances Attio stages
19. No response after Day 14 → Cadence Complete, nurture cadence

## Stack
- **Apollo Basic** ($64/mo) — list building + company discovery + email verification
- **Salesforge Growth** ($80/mo target, on trial now) — email + LinkedIn sequencing, MCP for Claude, Attio sync, built-in warmup
- **Attio** (free) — CRM, pipeline tracking, Claude MCP interface
- **Superhuman** (existing) — personal/warm emails only (thank-yous, intros, investor comms)

## Key Architectural Decisions (Updated)
- **Salesforge is source of truth for outreach tracking** — sheet stripped to discovery + approval + JJ call outcomes only
- **JJ fully decoupled from Salesforge cadences** — no Day 3 confirmation calls on sequenced targets
- Attio automations CANNOT trigger Salesforge sequences → Claude uses Salesforge MCP directly
- Salesforge sends through Kay's Gmail (IMAP/SMTP) → no warmup needed, domain already established
- Cold outreach goes through Salesforge, NOT Superhuman drafts
- Superhuman stays for relationship/warm emails only
- Reply.io cancelled and removed from .mcp.json
- LinkedIn Sales Navigator has no API → Claude can't operate it
- No secondary domain needed at 8-12 emails/day through Gmail
- A/B testing (Learning vs Direct) handled natively by Salesforge variant distribution
- Salesforge-Attio native integration syncs contact data only, NOT pipeline stages
- Pipeline-manager reads Salesforge events → advances Attio stages

## Review Model
- **Phase 1:** 5 rendered emails in morning briefing. Kay approves/edits. Zero edits = batch goes. High edits = keep reviewing.
- **Phase 2:** Auto-enrollment with spot-check summary. Graduation based on edit rate.

## Target Sheet (Simplified)
- Cols A-N: Discovery data from Apollo
- Col O: Kay's approval gate
- Col P: Pass reason
- Col Q: Agent notes/recommendation
- Cols X-AF: REMOVED — all tracked in Salesforge now

## Salesforge Config
- Workspace: wks_90dzvksqb1zcm2aifcfk6
- Sender Profile: 4116 (Kay Schneider, email + LinkedIn)
- Production Sequence: GB-Cold-FractionalCFO-v1 (ID: 9457, draft status)
- DNC: greenwichandbarrow.com, kaycschneider@gmail.com

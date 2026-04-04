---
date: 2026-04-04
type: context
sessions: 1
last_updated: 2026-04-04T23:00:00Z
---

# Session Decisions — April 4, 2026

## Decisions

- APPROVE: Universal G&B Cold Email Outreach Cadence — Day 0/3/6/14, two channels (email + LinkedIn DM)
- APPROVE: A/B test variants — Variant A (Learning/curiosity) and Variant B (Direct/acquisition intent)
- APPROVE: Subject line "Intro {first name} & Kay" for all cold outreach (replaces "Introduction, Greenwich & Barrow")
- APPROVE: Auto-advance model for targets — pass buy box + ICP = auto-approve to Salesforge/JJ. No manual Kay review.
- APPROVE: Warm intros + edge cases surfaced in morning briefing only. Kay decides: Draft or Salesforge.
- APPROVE: target-discovery runs on initial activation + weekly refill signal, NOT daily 4-6 targets
- APPROVE: target-discovery runs in morning workflow (step 5), not as launchd job
- APPROVE: Weekly tracker dashboard (Tab 0) with Signal Quality + System Throughput lenses, 2 active questions + 8 placeholders
- APPROVE: Premium Pest Management one-pager and scorecard templates aligned
- APPROVE: All 12 niche folders aligned to new template format (one-pager + scorecard)
- APPROVE: File naming convention: {Niche Name} {M.D.YY} (no zero-padding)

## Actions Taken

- CREATED: G&B Cold Email Outreach Cadence & Templates doc on Google Drive (master templates folder)
- CREATED: Premium Pest Management Scorecard 4.4.26.xlsx (rebuilt from template, 2.73/3.0)
- CREATED: 9 new one-pagers from template (all niches except 3 Active-Outreach which were already correct)
- CREATED: 10 new scorecards from template (9 niches + Premium Pest Mgmt replacement)
- UPDATED: target-discovery/SKILL.md — auto-advance model, one-time load, weekly refill, auto-advance stop hook (PE/email/owner/warm intro/edge case)
- UPDATED: outreach-manager/SKILL.md — G&B cold email cadence (Day 0/3/6/14), A/B templates, variables, rules, Salesforge enrollment stop hook, subject line fix
- UPDATED: pipeline-manager/SKILL.md — Targets for Review briefing section (warm intros + edge cases)
- UPDATED: weekly-tracker/SKILL.md — Dashboard tab (Signal Quality + System Throughput)
- UPDATED: jj-operations/SKILL.md — channel filter added (JJ-Call-Only only), hardened to hard stop
- UPDATED: target-discovery/SKILL.md — Col D reference fixed (was Col K)
- UPDATED: CLAUDE.md — morning workflow Step 5 (target-discovery conditional trigger), scheduled skills table, step renumbering
- DELETED: Unused launchd plist (com.greenwich-barrow.target-discovery.plist)
- DELETED: 13 old scorecards from Drive niche folders
- DELETED: 10 old one-pagers from Drive niche folders (2 couldn't delete — permission issue)
- DELETED: Dead Linkt config reference noted (still in .mcp.json — not yet removed)

## Deferred

- DEFER: Salesforge sequence creation in MCP — cadence designed but sequences not yet created in Salesforge. Do when test-running.
- DEFER: Art Advisory 81 targets — need to run through auto-advance stop hook. Do in next session.
- DEFER: Fractional CFO 28 targets — same, need auto-advance processing.
- DEFER: Fractional CFO niche flow walkthrough — started Art Advisory, haven't done CFO yet.
- DEFER: Active-Long Term niches (Specialty Insurance, Art Storage) — audit complete, both dormant. ARTMOVEMENT had positive response 6+ months ago, may be worth re-approach.
- DEFER: .mcp.json cleanup — Salesforge API key exposed in committed file, Linkt dead config still present.
- DEFER: Tier 3 plan fixes — pipeline-manager validation section, weekly-tracker sub-agent error detection, Salesforge key in /tmp.
- DEFER: 2 old one-pagers with permission errors — "Fine Art & Collectibles Insurance October 2025.pptx" and "Fine Art Logistics.pptx" need manual deletion by Kay.
- DEFER: Conference outreach cadence — separate from cold email, needs its own design.
- DEFER: Pest Management test-run — target-discovery for initial target load. Do Sunday.

## Open Loops

- Salesforge trial 12 days remaining — sequences need to be created and tested before expiry
- Art Advisory 81 targets sitting 14+ days with no outreach — highest priority for next session
- Fractional CFO 28 targets awaiting processing
- Premium Pest Management has no target sheet yet — needs initial load via target-discovery
- ARTMOVEMENT positive response from 6+ months ago — dropped lead, worth re-approach?
- .mcp.json security: Salesforge API key in plain text in committed file
- Reply.io trial ~11 days — cancel before charge

---
date: 2026-04-04
type: context
sessions: 2
last_updated: 2026-04-04T23:59:00Z
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
- Fractional CFO 28 targets awaiting processing
- Premium Pest Management has no target sheet yet — needs initial load via target-discovery (Sunday)
- ARTMOVEMENT positive response from 6+ months ago — dropped lead, worth re-approach?
- .mcp.json security: Salesforge API key in plain text in committed file
- Reply.io trial ~11 days — cancel before charge

---

# Session 2 — Evening (Target Discovery Pipeline Test Run)

## Decisions

- APPROVE: Art Advisory full pipeline test run — Apollo org search → web research (owners) → Apollo email reveal → warm intro check → sheet write
- APPROVE: 5+ employees threshold for art advisory (not standard 10+) — small-firm niche, acquirable at 5+
- APPROVE: Art Advisory is Salesforge Email only, no JJ calls — small world, everyone knows everyone, cold call would burn the relationship
- APPROVE: Apollo is the ONLY source for emails — web research provides names/titles/LinkedIn only, never scrape emails from websites
- APPROVE: Generic emails (info@, office@, etc.) are auto-pass — never used for outreach
- APPROVE: Wrong-domain emails are auto-pass — email domain must match company domain
- APPROVE: Warm intro check is a HARD STOP (Phase E) before any sheet write — no target enters automated pipeline without checking for warm paths first
- APPROVE: LinkedIn connections CSV stored in archives/linkedin/ and wired into warm-intro-finder as Source 0 (fastest check, grep before Attio)
- APPROVE: No LinkedIn Sales Navigator — no API/MCP, manual tool doesn't fit the system
- APPROVE: Add "LinkedIn Connection" column to target sheets for Kay to manually mark 1st/2nd/3rd degree
- APPROVE: Header-based column lookup plan — replace all hardcoded Col letter references with a script that resolves header names to column letters at runtime (INDEX/MATCH pattern, both axes)

## Actions Taken

- CREATED: Apollo API connection verified and tested (key in /tmp/apollo-key.txt)
- UPDATED: Art Advisory target sheet — 27 verified personal emails written via Apollo /people/match (40 credits)
- UPDATED: Art Advisory target sheet — 4 wrong-domain emails fixed (2 corrected via Apollo, 2 passed)
- UPDATED: Art Advisory target sheet — 13 total passes written (8 no-owner, 3 wrong-domain/generic from morning, 2 wrong-domain from evening)
- UPDATED: Art Advisory target sheet — LinkedIn URLs added for 6 unavailable-email targets
- UPDATED: Art Advisory target sheet — Col Y header "LinkedIn Connection" added
- UPDATED: target-discovery/SKILL.md — Phase E warm intro hard stop added before sheet write
- UPDATED: target-discovery/SKILL.md — Stop hooks 2-4 added (email verification allows LinkedIn-only, generic email check, wrong domain check)
- UPDATED: target-discovery/SKILL.md — Phase D Apollo-only email rule + domain-match validation
- UPDATED: target-discovery/SKILL.md — Summary list updated to 6 phases (A-F) including warm intro
- UPDATED: warm-intro-finder/SKILL.md — Source 0 LinkedIn CSV grep added before Attio check
- CREATED: archives/linkedin/connections.csv — 901 LinkedIn connections from 2026-03-23 export
- CREATED: scripts/col-lookup.sh — header-based column lookup script (needs bash fix, not yet tested)
- CREATED: Plan for header-based column lookups (approved, implementation Sunday)

## Deferred

- DEFER: col-lookup.sh script fix + testing — bash associative array issue, rewrite needed. Do Sunday.
- DEFER: Skill migrations to header-based lookups — 6+ skills, 100+ references. Do incrementally starting Sunday with Pest Management test.
- DEFER: LinkedIn Connection column placement — currently Col Y (end of sheet), move next to LinkedIn (Owner) after col-lookup.sh protects references
- DEFER: Salesforge sequence creation — cadence designed but sequences not created. Do when test-running.
- DEFER: Art Advisory 67 targets cleared for Salesforge — warm intro check complete, ready to route. Blocked on Salesforge sequences.
- DEFER: Schwartzman warm intro routing — Margot Romano path confirmed, needs Kay's decision: personal draft or Salesforge
- DEFER: Fractional CFO 28 targets — need auto-advance processing
- DEFER: Art Advisory PE ownership check — not yet run on any of the 70 active targets
- DEFER: .mcp.json cleanup — Salesforge API key exposed, Linkt dead config

## Open Loops

- Salesforge trial ~12 days remaining — sequences need creation + testing before expiry
- Art Advisory 67 targets ready for Salesforge (post warm-intro) — blocked on sequence creation
- Schwartzman & Associates — warm intro via Margot Romano, needs Kay's routing decision
- col-lookup.sh needs bash fix → Python rewrite for the parsing logic
- 6+ skills need migration from hardcoded Col letters to header-based lookups
- Art Advisory PE ownership check not yet run
- Fractional CFO 28 targets awaiting processing
- Premium Pest Management initial target load — Sunday
- Reply.io trial ~11 days — cancel before charge
- .mcp.json security: Salesforge API key in plain text

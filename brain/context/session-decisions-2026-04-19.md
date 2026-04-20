---
schema_version: 1.1.0
date: 2026-04-19
type: context
title: "Session Decisions — 2026-04-19"
tags: ["date/2026-04-19", "context", "topic/session-decisions", "topic/niche-evaluation", "topic/dealsx", "topic/tracker-management"]
---

# Session Decisions — 2026-04-19

Major strategic day. Covered: niche evaluation (Specialty Coffee Equipment Service, Commercial Laundry, Art Storage reactivation), Path A portfolio reshape (services-primary, one SaaS category), Sam DealsX sheet restructure, tracker-manager skill creation, JJ launchd timing change, Pest → Sam scheduled addition.

## Decisions

### Niche evaluation

- **PASS: Commercial Laundry Equipment Service** — 20-min desk check found EVI Industries (32 acquisitions since 2016, public strategic) + Alliance Laundry Systems (PE-owned OEM, IPO'd Oct 2025, going direct aggressively) actively rolling up the exact target universe. No searcher acquisitions identified. Alliance disintermediating its own dealer channel = 3-5yr existential risk on any Alliance-concentrated dealer. Thesis broken. Re-check in 12 months post-Alliance-IPO to see how direct strategy plays out.

- **PASS: TTCER Partners' linen service suggestion** — capex rejection (asset-heavy facility model) correct on original. Equipment-service reframe fails on thin target count + now-confirmed consolidation in adjacent commercial laundry equipment. Dropped.

- **PASS (x4): other high-end equipment service candidates** — commercial kitchen (fine dining segment is bad end-customer economics), luxury AV/Crestron (searcher-crowded), wine cellar climate (TAM below $500M floor), chandelier restoration (episodic not recurring, too small).

- **APPROVE: Specialty Coffee Equipment Service → Active-Outreach / DealsX Email** — scorecard 2.55/3.0 (85.1%), all 4 INITIAL SCREEN gates pass. International-OEM authorized-dealer structural moat (Italian-HQ OEMs — La Marzocco, Nuova Simonelli/Victoria Arduino, Gruppo Cimbali/Slayer, Sanremo, Astoria, Rancilio — structurally unable to run direct service in US metros). Closer analogue: Ferrari/Lamborghini authorized service (stable 50+ year pattern), not Alliance commercial laundry. Margin drag acknowledged (8-12% baseline → 15-18% post-ops-lift), Path 2 chosen: activate Sam sprint now, run warm validation in parallel.

- **APPROVE: Art Storage reactivation** — moved from TABLED → WEEKLY REVIEW (Rank 17) as Active-Outreach / DealsX Email with DNC carve-out (Acumen, Uovo, Hangman on Do Not Contact list). Prior LOI history documented. 4/19 reactivation on Saltoun greenlight + AI cost-efficiency thesis.

### Path A — Portfolio reshape for Sam

- **APPROVE: Services-primary, SaaS-as-supporting thesis** — G&B's primary acquisitions are services businesses with luxury / high-value-asset customer bases. SaaS becomes a supporting capability (tuck-in that automates an acquired services business OR operational software that manages a broader luxury-services portfolio). Strategic pivot documented.

- **APPROVE: Trim Sam's 4 SaaS categories to 1.** Kept: `Vertical SaaS for Luxury & High-Value Asset Service Industries` (renamed from "Software" → "SaaS"). Retired: Enterprise Software & Data Platforms B2B, Specialty Healthcare Software B2B, Female-Led Vertical SaaS B2B.

- **APPROVE: 10 SaaS sub-niches on WEEKLY REVIEW → Active - Long Term** (ranks 3, 4, 6-13). Finish existing outreach cadences, no new targets. Kept as tracker record per Kay: "we keep the record on our tracker."

- **APPROVE: Add 2 new services categories to Sam** —
  - `Specialty Commercial Equipment Services` (covers Specialty Coffee Equipment Service + commercial kitchen + wine cellar + specialty HVAC + dishwashing + refrigeration + craft bar + ice/water + combi-oven)
  - `Specialty Storage & Handling for High-Value Collections` (covers Art Storage + wine + classic auto + yacht + jewelry/watch vault + archives + museum loan + rare books + memorabilia + estate collections)

- **APPROVE: Broaden `Specialty Insurance Brokerage (Art & Collectibles)` → `Specialty Insurance Brokerage`** — drop Art & Collectibles from title, keep Fine Art + Collectibles + Jewelry + Wine + Classic Auto + Yacht + Aviation + Equine + Cyber UHNW + D&O family office + Museum + Auction in sub-industries. Kay rule: broader title, narrow subcategories. Target pool goes from ~3-5 to ~500-1,500.

- **APPROVE: Add Pest Management to Sam's DealsX sheet** — launch 5/7/2026 (corrected from 5/6). Title: `Specialty Pest & Environmental Management Services` (broadened per Sam's sheet rule). Sub-industries include luxury hospitality pest, HACCP-driven fine dining, museum/gallery, UHNW residential, Class-A commercial, historic building, yacht, wine cellar.

- **APPROVE: Delete the 3 retired SaaS rows from Sam's sheet.** Kay: "that is sam's sheet - you can delete, but we keep the record on our tracker."

### Infrastructure / governance

- **APPROVE: One-pager guardrail hook** — PreToolUse hook blocks writes to niche one-pager files (`*niche-onepager*.md`, `*one-pager*.md`, `*onepager*.md`) that contain personal/team references (Kay, Kay's network, analyst, CoS, Milanese, Wedgwood, Alain Wertheimer, JJ, G&B's right to win). Rationale: Kay corrected this pattern 3+ times in session; memory-only rule insufficient — tool-level enforcement needed.

- **APPROVE: tracker-manager skill + scope memory** — Claude owns day-to-day execution of tracker and operational-sheet updates; Kay owns strategic decisions. Auto-execute vs surface-for-approval matrix defined in `memory/feedback_tracker_manager_scope.md`. Skill scaffolded at `.claude/skills/tracker-manager/SKILL.md` with hard guardrails (snapshot before write, post-write verify, bash not zsh, trace log every material change).

- **APPROVE: JJ launchd timing 11pm → 6pm ET Sunday** — Kay wants to review prep before bed, not wake up to it Monday morning. Plist edited + reloaded. Next fire: Sunday 4/26 at 6pm ET.

### Personal context (corrected)

- **REJECT: Applying Wedgwood as niche-scoring lens** — Kay corrected: the Wedgwood chapter from *Creating Modern Capitalism* is personal aspirational context for who she wants to be as a leader. NOT a niche-evaluation heuristic. Do not surface "Wedgwood dimension" in one-pagers, scorecards, or niche analysis. Memory rewritten accordingly.

- **REJECT: Putting Chanel structural parallel + Milanese analyst right-to-win + "Kay's hospitality network" in the Specialty Coffee one-pager** — Kay: "I shared that information for your and my strategic perspective, not for the subagent to put in the one-pager." Artifacts are pure industry niche analysis. Memory rule saved + tool-level hook created.

## Actions Taken

### Vault

- CREATED: [[outputs/2026-04-19-specialty-coffee-equipment-service-niche-onepager]] (updated throughout session with revised disintermediation read + purity cleanup)
- CREATED: [[outputs/2026-04-19-validation-contacts-specialty-coffee-equipment-service]] (via niche-intelligence Step 5b)
- CREATED: `.claude/hooks/router/handlers/onepager_guardrail.py` (7 unit tests passing)
- CREATED: `.claude/skills/tracker-manager/SKILL.md`
- UPDATED: `.claude/hooks/router/pre_tool_use.py` (registered guardrail handler)
- UPDATED: `.claude/skills/jj-operations/SKILL.md` (generic Call Guide reference, removed per-niche lookup)
- UPDATED: [[context/continuation-2026-04-19-1]] (5/6 → 5/7 for Pest transition, 4 occurrences)

### Memory

- CREATED: `user_kay_wedgwood_archetype.md` (personal context only — NOT niche heuristic)
- CREATED: `feedback_artifacts_pure_industry_analysis.md` (artifacts = pure industry analysis; strategic context stays Kay ↔ Claude)
- CREATED: `feedback_tracker_manager_scope.md` (auto-execute vs surface-for-approval contract)
- UPDATED: `feedback_niches_drive_channels_not_reverse.md` (5/6 → 5/7 correction on Pest transition)
- UPDATED: `MEMORY.md` index (3 new entries)

### Drive

- CREATED: "Specialty Coffee Equipment Service" niche folder under WEEKLY REVIEW parent (ID `13_ZNe6kY-1EUYWPYzWmiGK6i5Jdxfdts`)
- CREATED: PPTX one-pager in Drive (ID `1VggLA7HHhXxNzOD4I8YPz1V_t5NbZ2_S`)
- CREATED: XLSX scorecard in Drive (ID `16Kgwp6y6wTLfsCyi0DOoVPopPDc4HAyR`), score 2.55/3.0
- UPDATED: Art Storage Drive folder moved from TABLED parent → WEEKLY REVIEW parent (ID `1yFRqoTgTXViZdk6Lg6gQzOgOd1PpYFjF`)

### Google Sheets

- UPDATED: Conference Pipeline — 48 conferences sorted by date with 15 week-divider rows preserved (notes carried on dividers per Kay's clarification)
- UPDATED: Industry Research Tracker / WEEKLY REVIEW —
  - Row 17 Rank 14: "Vertical Software" → "Vertical SaaS" for Luxury & High-Value Asset Service Industries
  - Rows 6-7, 9-16 (10 rows): Status Active-Outreach → Active-Long-Term
  - Row 19 Rank 16 Specialty Coffee: New → Active-Outreach / DealsX Email
  - Row 20 Rank 17 Art Storage & Related Services appended
- UPDATED: Industry Research Tracker / TABLED — Row 11 Art Storage cleared (moved to WEEKLY REVIEW)
- UPDATED: DealsX Industry Verticals sheet —
  - Rows 5-7 (3 retired SaaS categories) cleared, content shifted up (rows 5-9 now hold the 5 active kept categories contiguously)
  - Row 6 renamed: Vertical SaaS for Luxury & High-Value Asset Service Industries
  - Row 7 broadened: Specialty Insurance Brokerage (title + expanded sub-industries + keywords)
  - Rows 8-9: NEW Specialty Commercial Equipment Services + Specialty Storage & Handling
  - Row 10: NEW Specialty Pest & Environmental Management Services (launch 5/7)

### Infrastructure

- UPDATED: `~/Library/LaunchAgents/com.greenwich-barrow.jj-operations-sunday.plist` — Hour 23 → 18 (11pm → 6pm ET); launchd reloaded

## Deferred

- **Pest Management Sam launch: 5/7/2026** (trigger: date arrives; Kay flips G&B Filled Details flag to TRUE on Row 10 of DealsX sheet → Sam pulls lists)
- **DealsX sheet status flags** — all 6 rows currently at FALSE/FALSE/FALSE. Kay flips to TRUE when ready for each category's lists to be built.
- **JJ post-5/7 niche** — undecided. Current JJ niche (Premium Pest Management) has ~2.5 weeks remaining before Sam takes over. Need a new niche for JJ by ~5/4 at latest.
- **Mercury bank switch** — Kay to open application Monday 4/20 (explicit self-commitment in prior session)
- **Ping Sam to confirm 6-category book sufficient for 3,000-target 3-month sprint** — Kay can send Monday; draft on standby if needed.
- **Specialty Coffee PPTX Assessment score reconciliation** — placeholder 2.50 vs computed 2.55 (0.05 rounding delta); left as-is per agent recommendation.
- **Empty rows on DealsX sheet** — gog CLI limitation prevented true row-delete; rows shifted + trailing rows cleared (visual state is clean; no action needed unless Kay sees something off).

## Open Loops

- **JJ harvest-to-master-list write broken** — 19 targets called 4/9-4/10 had status captured on daily Call Log tabs but never written back to Full Target List Col T (JJ Call Status). They re-surfaced in this week's selection. Harvest workflow needs a fix before next week's prep. Flagged for Monday morning review.
- **Archive tabs not hidden on Premium Pest Management sheet** — gog CLI doesn't expose tab-hide. ARCHIVE-Call Log 4.08/4.09/4.10 tabs remain visible; ARCHIVE- prefix mitigates confusion but visual clutter remains. Acceptable as-is.
- **Call Guide for Pest Management** — clarified not needed; G&B Cold Call Guide (generic, Doc ID `12Hqfwxg4qJA3YdZh36ndd-flvYgWN`) applies across niches. Skill reference updated; no-niche-specific-guide is now the rule.
- **JJ post-5/7 niche decision** — carry to Monday or Tuesday analyst call.
- **Tracker-manager skill first acid test** — tomorrow. If any auto-execute step causes a problem, demote it back to surface-for-approval in the memory rule.

## Post-first-goodnight additions (late Sunday 4/19)

Kay kept working after the first /goodnight. Additional decisions captured:

### Sam's DealsX book additions + reshape

- **APPROVE: Add Premium Pest Management to Sam's DealsX sheet** — broader title `Specialty Pest & Environmental Management Services` (per Sam's "keep industries intentionally broad" rule). Date Added 4/19, Date Lists Due By 5/1, Launch 5/7 (corrected from 5/6). Written as Row 10 via tracker-manager guardrails (snapshot + post-write verify).
- **APPROVE: Delete 3 retired SaaS rows cleanly** — gog CLI doesn't support row-delete, so used content-shift approach: moved kept rows 8-12 up to rows 5-9, cleared trailing rows 10-12, then wrote Pest as new Row 10. Final state: 6 active categories in contiguous rows 5-10, no visual clutter for Sam.

### JJ operations

- **APPROVE: JJ launchd prep timing 11pm → 6pm ET Sunday** — Kay wants to review prep before bed, not wake to it Monday. Plist edited + launchd reloaded. Next fire Sunday 4/26 6pm ET.
- **APPROVE: Generic G&B Cold Call Guide (Doc `12Hqfwxg4qJA3YdZh36ndd-flvYgWN`)** is the reference, not per-niche guides. Skill reference updated to stop flagging missing per-niche variants.

### Strategic sprint — 11-day LOI goal reality-checked

- **REJECT: LOI in 11 days from 5 new niches** as structurally achievable. Kay set the aspirational goal; CIO reality-checked — cold-target-to-LOI is 3-6 months. Proposed realistic 11-day sprint goals: first CIM in hand, first Thumbs Up owner call scheduled, or 2 Thumbs Up calls + 1 NDA signed. Kay didn't select a specific goal but pivoted to building warm-intro activation across the 5 niches.

### Warm-intro sprint (Kay's per-niche asks)

- **APPROVE: Per-niche warm-intro activation**
  - INSURANCE: circle back with Sarah de Blasio (send G&B-letterhead'd Goodwin finder's fee); reply to Mark (existing not startup, platform review); respond to Amanda (RSVP or coffee)
  - COFFEE: walk into Frenchette + usuals, ask husband about restaurant equipment firms, ask Marriott luxury brand partnership director about hotel espresso equipment service
  - STORAGE (Art Storage): email Levi, text Paul, ask Karaugh for intros
  - PEST: Jason for Hamptons pest management contact
  - SaaS: research existing SaaS for yachting + jewelry independents landscape
- **APPROVE: Universal per-niche workstream** — warm LinkedIn searches, association listings, meetup attendance for every niche.

### Infrastructure / channel additions

- **APPROVE: Direct mail as 3rd outreach channel** — 3-channel stack (call + email + mail) beginning early May after Sam's target lists arrive. Handwrytten the CIO-recommended vendor (premium positioning, API-driven, robot-handwritten stationery aesthetic). Estimated cost $1,250/wave (250 pieces × $5) to $2,500/wave at scale. CFO budget check needed. **DEFER: planning to later this week** — Kay explicitly said not Monday.
- **APPROVE: Association-placeholder tab per niche target-list sheet** — while Sam builds Full Target Lists, we populate Associations tab from river-guide-builder output.
- **APPROVE: Industry Research Tracker → deal-aggregator sync** — deal-aggregator reads WEEKLY REVIEW at scan start so Coffee (Rank 16) + Art Storage reactivation (Rank 17) auto-roll into tomorrow's scan. Keyword expansion per niche flagged for `deal-aggregator-tuning-spec` — needs broker-friendly term translations.

### Operational ownership

- **APPROVE: Weekly tracker + dashboard as Friday agenda item.**
- **APPROVE: Monthly meeting with Megan Lawlor — last week of each month.** Last meeting on file: 4/1/2026. Schedule next 4/28-4/30 and establish recurring cadence.
- **APPROVE: Monthly reporting from Anthony (bookkeeper) — to be reviewed Friday 4/24.** No email from Anthony found in Gmail search; ping Anthony Monday to confirm delivery timing.

### Dropped ball recovered

- **REJECT: Previous Slack deep-link formatter for TheDealSheet** — my 4/13 Slack message sent `thedealsheet.co/pest-control` (category page) for the Palm Beach pest deal instead of a deal-specific URL. Kay couldn't open it. Deal details recovered from 4/13 scan (Palm Beach County, FL pest control — $5.8M rev / $1.6M EBITDA / $9.6M ask / 6.0x / Hot Deal flag). Queued for Monday: log into TheDealSheet, pull working deep-link, resend. Meta-fix: add to `deal-aggregator-tuning-spec` as hard issue.

## Post-goodnight actions taken

- CREATED: [[inbox/2026-04-20-monday-fire-plan]] — 7 priority workstreams + deferred items + Friday agenda + Megan cadence + Mercury reminder. /goodmorning will ingest automatically.
- UPDATED: DealsX Industry Verticals sheet — content-shifted rows 5-9 contiguous, Row 10 new Pest category written
- UPDATED: `~/Library/LaunchAgents/com.greenwich-barrow.jj-operations-sunday.plist` — Hour 23→18, launchd reloaded
- UPDATED: `.claude/skills/jj-operations/SKILL.md` — generic Call Guide reference (no per-niche search)
- UPDATED: `brain/context/continuation-2026-04-19-1.md` — 5/6→5/7 Pest transition (4 occurrences)
- UPDATED: `memory/feedback_niches_drive_channels_not_reverse.md` — 5/7 correction

## Tags

- niche/specialty-coffee-equipment-service
- niche/art-storage
- niche/premium-pest-management
- niche/specialty-insurance-brokerage
- niche/commercial-laundry-equipment (PASSED)
- topic/path-a-services-primary
- topic/international-oem-moat
- topic/pe-consolidation-risk
- topic/artifacts-pure-analysis
- topic/tracker-management
- topic/warm-intro-sprint
- topic/direct-mail-planning
- topic/monday-sprint

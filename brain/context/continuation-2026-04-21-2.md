---
date: 2026-04-21
type: context
title: "Continuation — 2026-04-21 #2"
saved_at: 2026-04-21T17:15:00-04:00
session_number: 2
tags: ["date/2026-04-21", "context", "topic/continuation", "topic/deal-aggregator-buildout", "topic/calibration"]
---

## Active Threads

**Deal Aggregator resource folder buildout — SUBSTANTIALLY COMPLETE.** All three buy-box Drive docs live (Services, Insurance, SaaS). Sourcing sheet created + populated + verified via 3 parallel audits. SKILL.md rewired to read from Drive + WEEKLY REVIEW + DEALSX foreign key. WEEKLY REVIEW tab has new "DealsX Niche" column; DEALSX tab rewritten with 7 DealsX-submitted niches (Niche Hypothesis, Quick notes, Keywords).

**Calibration thread — IN PROGRESS.** Kay confirmed midday-degradation pattern. Pre-flight checklist drafted (12 items) pending Kay's review next session. Kay added "am I filling with surface-level information?" as priority check.

**Verification audit — CORRECTIONS APPLIED.** 3 agents returned; Sica Fletcher restored to Active (was wrongly 404-labeled), 4 status upgrades, 4 URL fixes, 5 new niche sources, 2 reclassifications, 2 structural GAPs confirmed.

## Decisions Made This Session

### Buy-Box Architecture
- **Three-category split:** Services / Insurance / SaaS — each its own Drive doc (in Deal Aggregator folder)
- **Services:** $10-50M revenue, $1.5-5M EBITDA, 10%+ margin floor, B2B/B2B2C, 5+ yrs, 10-200 employees, 9 industry hard-excludes (franchises, consumer retail, restaurants, construction incl. NYC, capital-intensive mfg, physician, seasonal, lending, carve-outs), CA soft exclude
- **Insurance:** $3-40M COMMISSION revenue (not premium), $1.5-10M EBITDA, 15% margin floor, 5-100 employees, retail OR wholesale/E&S specialty brokerage only, commission-based revenue (not fee), 6 hard-excludes (PE-consolidator, captive carriers, MGA/MGU, TPA, lead-gen, lending)
- **SaaS:** ARR $3-20M, positive EBITDA required (auto-reject negative), 10%+ ARR growth, 85%+ GRR, 5-100 employees, vertical only (no horizontal/B2C/prosumer), no majority institutional, no VC board seats, <$2M total raised, 5+ yrs operating
- **Data Availability Rule:** missing data never auto-rejects — flags for review (applied to all three docs + scoring logic)
- **Stripped from buy-boxes:** thesis language, 5-moat framework, AI posture, owner profile, margin lessons, contact requirements, inline consolidator list, date parentheticals (go stale) — moved conceptually to separate Thesis docs (not yet built)
- **Date parentheticals** like "(founded 2021 or earlier)" stripped — calendar translations go stale in ~8 months

### Deal-Aggregator Skill Architecture
- **Scope locked:** prepped deals only (owner has decided to sell) — no target-seeding, no lists, no blacklists, no catalogs
- **Target-discovery PAUSED** (not sunsetted) — DealsX owns target list building end-to-end
- **SKILL.md reads buy-box from 3 Drive docs on every run** — never cached, never hardcoded
- **Step 0a** reads WEEKLY REVIEW for active niches (Active-Outreach + Active-Long Term) + DealsX Niche foreign-key
- **Step 0b** reads all 3 buy-box Drive docs freshly
- **Step 0c** niche corpus resolution: if DealsX Niche populated → pull Quick notes + Keywords from DEALSX (primary) + WR Quick notes (supplementary); if blank (Art Advisory) → WR row enrichment fallback (Niche Hypothesis + Quick notes + other populated fields)
- **Category routing:** Insurance→Insurance Buy Box; SaaS→SaaS Buy Box; everything else→Services Buy Box
- **Active-Diligence status** — Kay eliminating from data validation (never existed on tracker anyway)
- **Stop hooks added:** Step 0b completed (buy-boxes freshly read); Step 0c completed (corpus resolved for EVERY active niche); artifact logs corpus path per niche for calibration
- **All column-letter references** replaced with field names (no more "Col B / Col I" in SKILL.md)
- **All lists eliminated from skill scope** (no DNC, no Source Catalog, no Niche Coverage Map)

### Industry Research Tracker Updates
- **DEALSX tab rewritten:** rows 5-11 now show 7 DealsX-submitted niches from Greenwich & Barrow_DealsX Industry Verticals complete sheet
- **DEALSX field layout:** B=Niche Hypothesis, H=Quick notes (Industries/Types sub-verticals from Sam's sheet), I=Keywords (tokenized match corpus) — header renamed from "Red flags noted" → "Keywords"
- **WEEKLY REVIEW tab:** added "DealsX Niche" foreign-key column (header renamed from "Red flags noted")
- **7 niche mappings written** to WR DealsX Niche column; Private Art Advisory intentionally blank (no DealsX equivalent)
- **DealsX source file** aligned 3 months out; snapshot in Drive is authoritative for this period

### Sourcing Sheet (G&B Deal Aggregator - Sourcing List 4.21.26)
- **Created as discussion artifact** in Deal Aggregator folder (ID 1z8o2obq2mOG9drQ0umCmBk31K3OS2afMNGpVAlbLljw)
- **Two tabs:** General Sources (22 rows), Niche-Specific Sources (24 rows incl. 2 structural-GAP entries)
- **Column order:** Status, Source, Type, Access, URL, Notes (+Niche first on Niche tab)
- **Sorted by status priority** (Pending G&B registration at top)
- **Axial added** to General Sources (Pending G&B registration)
- **Three parallel verification audits completed:** Gmail registration (22+16 domains), URL accessibility (34 URLs), niche classification + GAP research
- **MAJOR correction:** Sica Fletcher is LIVE (was wrongly labeled 404 for days) — recovers ~35%+ of US insurance brokerage M&A deal flow visibility
- **4 status upgrades:** DealForce, IAG M&A, Viking Mergers → "Active - email alerts" (registered under alt sender domains: generational.deals, iag-service.com, vikingmergers.ccsend.com); Benchmark → "Registered - dormant" (no activity past 90 days)
- **4 URL fixes:** kumo.so (DNS dead) → withkumo.com; searchfunder.com/deals (404) → root; app.feinternational.com (login app) → feinternational.com/listings/; softwareequitygroup.com (301) → softwareequity.com
- **Quiet Light + Flippa reclassified:** "Active - email-only (web blocked)" — emails ARE active even though scraping is broken
- **Agency Checklists + IA Magazine reclassified** as Industry Publications (not deal sources) — intel-only tier
- **Keystone Business Advisors** flagged as multi-niche + California-based (NOT pest-specific) — 4th ask still pending Kay
- **5 new niche-specific sources added:** MidCap Advisors + Inside Self-Storage (Art Storage → GAP resolved); Green Bridge Advisors + Calder Capital + CMM Online (High-End Commercial Cleaning → GAP resolved)
- **2 structural GAPs confirmed:** Private Art Advisory + Specialty Coffee Equipment Service — no niche-specific source exists anywhere; flow can only come from outreach-manager/warm intros
- **Woodbridge Notes updated:** brand change — firm now operates as "Mariner"

### Process Rules — 10 Memories Saved
1. `feedback_test_before_concluding_channel_dead` — scan-coverage parity audit before any "channel dead" verdict
2. `feedback_signups_in_morning_brief` — standing line item in briefing with direct signup URLs
3. `feedback_all_channels_parallel` — never recommend dropping a channel; improve source quality within
4. `feedback_deal_aggregator_scope` — prepped deals only; target-seeding belongs in other skills
5. `feedback_target_discovery_paused` — paused not sunsetted; DealsX owns target list building
6. `feedback_missing_data_not_a_filter` — absence of disclosed field never auto-rejects
7. `feedback_deal_aggregator_no_lists` — no DNC, source catalog, coverage map — no maintained lists
8. `feedback_no_fabricated_status` — verify against authoritative source or spawn agent; narrative text ≠ verification
9. `feedback_no_name_in_deliverables` — STRENGTHENED — covers all artifacts (sheets, docs, decks), not just "formal" deliverables
10. `feedback_finish_step_before_next` — complete thoroughly before pivoting; never defer corrections

### Pre-Flight Checklist (NEW ARTIFACT)
- **Draft saved** at `brain/context/pre-flight-checklist-draft.md` — 12 items across Accuracy & Depth, Scope & Conventions, Step Completion, Decision Framing
- **Kay added** "am I filling with surface-level information?" as priority check (names the "eagerness to complete over accuracy" failure mode)
- **Pending next session:** Kay review + edit; decide whether to pin into CLAUDE.md root so it loads into every session's system prompt

## Next Steps

1. **Resume calibration review** — Kay edits the pre-flight checklist; decide pin-to-CLAUDE.md vs standalone
2. **Decide whether Private Art Advisory + Specialty Coffee Equipment graduate out of deal-aggregator scope** — both are confirmed STRUCTURAL GAPs, not coverage misses
3. **Keystone Business Advisors decision** — 4th ask carried since 4/17; now also flagged CA-based + multi-niche. Register / drop / move to General tab?
4. **Thesis companion docs** — the content extracted from old buy-boxes (must-haves, 5-moat framework, AI posture, margin lessons, owner profile) has not been landed in companion Thesis docs yet. Kay deferred this.
5. **Save-state format improvement** — Kay implicitly flagged that 200-300 words is too compressed for midstream saves. Consider updating the savestate skill to allow comprehensive mode when mid-project (like this one).

## Open Questions

- **Structural GAPs:** Do Private Art Advisory + Coffee Equipment stay in deal-aggregator scope (zero-yield forever) or graduate to outreach-only?
- **Keystone:** register, drop, or move to General tab?
- **Pre-flight checklist:** pin into CLAUDE.md root (default-loaded) or keep as standalone reference?
- **Save-state skill:** update to allow comprehensive mode for midstream session-ends?
- **Thesis docs:** when does Kay want these built (Services Thesis, Insurance Thesis, SaaS Thesis)?

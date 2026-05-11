---
name: Testing Day March 20 — Full Session Summary
description: Comprehensive summary of all testing, skill improvements, and system changes made during Friday 3/20 testing day
type: project
---

## Skills Tested

### 1. /start (today skill) — TESTED
- "Good morning" trigger wired into skill router (HIGH confidence)
- Skill updated: numbered items, "Proposed Action Items for Motion" header
- 3 sub-agents ran in parallel (previous-day, inbox, email)
- Email scanner processed 27 threads, created 6 inbox items
- 3 Motion tasks created from approved async items

### 2. pipeline-manager — TESTED
- 3 sub-agents ran in parallel (pipeline, relationships, Granola)
- 5-section format implemented: Active Deals, Intermediary, Investor, Relationship Building, Action Items
- "Pipeline Review" header added
- Eight Quarter Advisors added to Intermediary Pipeline
- Project Restoration added to Active Deals at NDA Executed (later moved to Financials Received)
- 5 People records updated, 3 Motion tasks created
- Active deal fast-path added: CIM/financials for active deals get same-day treatment with Slack ping + auto-trigger deal-evaluation

### 3. weekly-tracker — TESTED (major calibration)
- 4 sub-agents ran in parallel (Gmail, Calendar, Attio, Vault)
- Major metric definition corrections:
  - Delta vs snapshot distinction clarified (all metrics except Deals in Active Review, Qualified Opportunities, Top of Funnel)
  - Gmail queries tightened to use OUTREACH labels
  - Introductions = first-time "Kay, meet X" only
  - Deals in Active Review = First Conversation through LOI Signed (stages 3-9)
  - Top of Funnel renamed from Total Active Pipeline
- Historical quarterly data backfilled (Q1 2025 - Q1 2026) from:
  - SalesFlare archive (195 opportunities with timestamps)
  - Google Calendar (268 external meetings in Year 1)
  - Investor report PDFs (Q1-Q3 2025 exact numbers)
  - Google Drive ACTIVE DEALS folders (NDA/financials/LOI dates)
- Quarterly Summary restructured: 5 quarters + Year 1 Total + search fund benchmarks
- Validation stop hook built (weekly_tracker_validation.py)
- Calibration agent updated to read weekly tracker trends

### 4. niche-intelligence — TESTED (major restructuring)
- 6 gathering agents ran in parallel
- Significant pipeline changes:
  - Buy box removed from niche evaluation (buy box is for companies, not industries)
  - Initial Screen added: Margins 15%+, Recurring Revenue, Industry Growth >GDP, Growth TAM $500M+
  - Industry Scorecard separated from Company Scorecard
  - Target TAM = informational (like QSBS), determines sprint duration not go/no-go
  - No automated kills — Kay decides everything
  - Scorecard template updated with INITIAL SCREEN tab, uploaded to Drive
  - Target Pool column added to Industry Research Tracker (WEEKLY REVIEW + IDEATION tabs)

### 5. deal-evaluation — PARTIALLY TESTED (live deal: Project Restoration)
- Buy-Box Screen template created and added to Master Templates
- Buy-box screen run on Project Restoration CIM (FLAG — below size but exceptional margins)
- Quick Screen added: Margins, Recurring Revenue, Industry Growth (pre-scorecard)
- Size criteria changed from hard-fail to situational
- Active deal fast-path wired into pipeline-manager
- CIM downloaded from Gmail, filed to Drive
- Private deal folder created in DEALS IN REVIEW
- Cross-deal comparison feature planned (future, when volume justifies)

## System Infrastructure Built
- Google Docs brand formatter script (scripts/format-gdoc.py) — Avenir font, G&B full logo, Strictly Confidential footer, black text only
- All 7 Google Doc templates formatted
- Weekly tracker validation hook (PreToolUse)
- Remote control tested (Kay accessed session from phone)
- Call notes processed (AI in Search group call via Wispr Flow)

## Key Decisions Made
1. Size is situational, not a hard fail in buy-box
2. Industry scorecard ≠ company scorecard — different tools for different purposes
3. Target TAM determines sprint duration, not go/no-go (per investor feedback)
4. Growth TAM $500M floor (investor requirement)
5. Active deal signals get same-day treatment
6. No automated niche kills — Kay decides everything
7. Linkt has 2-3 weeks to prove value before considering alternatives

## Second Half: Niche Discovery Deep Dive

### The Pivot
Shifted from "advisory services for wealthy people" to "operationally critical B2B for luxury businesses." Every advisory niche Kay gravitates toward has beautiful economics but empty target pools (3-40), key person risk, and discretionary spend. The operational infrastructure niches may have hundreds of targets and value in contracts, not founders.

### 20+ Niches Evaluated (see project_niche_discovery_march20.md for full table)
Already on WEEKLY REVIEW: Trust Administration (tabled — empty pool), Estate Management (25-40, active), Trade Credit Insurance (8-15, active), IPLC (4-6, time-sensitive), Art Insurance Brokerage (3-5, wind-down).

New niches evaluated: Private Art Advisory (25-40 firms, 10-15 transferable — concerns re key person risk + discretionary spend), Collection Management (eliminated — not standalone), Concierge Medicine (eliminated — searchers + investor won't buy), Fine Art Logistics (interesting, moderate capital), Fire Protection ITM (likely PE-saturated), Kitchen Exhaust Cleaning (borderline — odd hours), Linen/Laundry (eliminated — capital intensive), Specialty Security (eliminated — PE rolled up), Visual Merchandising (eliminated — not a business), Luxury Packaging (borderline — manufacturing), AML/KYC for Art Market (watch — too early), Customs Brokerage luxury (eliminated — consolidated), Sustainability/ESG (eliminated — VC territory), UHNW Household Vetting (eliminated — bundled with staffing), Family Office IT/Cyber (possible — find MSP with FO clients), Trust Company Compliance (eliminated — too thin), Specialty Pest Mgmt Museums (small niche), Collection Documentation/Appraisal (fragmented, same small-pool problem), Workplace Compliance Training (parked), Cosmetics/CPG Compliance (eliminated — project-based).

### The Core Tension
Kay's thesis gravitates toward highly specialized, UHNW-adjacent, relationship-driven businesses. These are great to OWN but hard to BUY — small pools, founder-dependent, discretionary. The niches with big target pools tend to be commoditized, PE-saturated, or involve operating realities Kay doesn't want.

### The Chanel Parallel
Kay's approach: 3 parallel tracks, 10 targets each, first to convert wins. This mirrors how she got the Chanel job (9-month process, multiple interview tracks). Applied to the search: run insurance, estate management, and one other niche simultaneously. Whichever produces a signed LOI first wins.

### Insurance Conviction
- Team ready: insurance specialist available post-acquisition, Camilla as CFO
- August Felker (Oberle Risk Strategies) offered to help with DD — knows the landscape from the inside
- Richard Augustyn's "embedded/tightly integrated services" insight led to the whole compliance thesis
- Jeff Stevens (lead investor) connection to insurance through Anacapa portfolio

### Leads Mined from Calls and Emails
- Jeremy Black (Jasper+Black): 2 unfollowed leads — back-office insurance model + IMO/FMO aggregator
- Jonathan Crystal: contact from Hunter's network (insurance connections)
- August Felker: mentioned a specific target — women-led HNW insurance brokerage
- Richard Augustyn: recommended looking at "embedded/tightly integrated services" more broadly
- Hunter recommended the carve-out path (buy a division of a larger firm)
- Joe Vanore at E&K for monthly deal listings (intermediary pipeline)

### Fireflies Recovery
76 total transcripts found in Fireflies account. 26 missing transcripts that hadn't been synced were pulled and saved. All synced to vault. This was important — many of the insurance conversations were in these missing transcripts.

### OneNote MCP Integration
Installed mcp-server-onenote package. Needs configuration in settings.json and Microsoft authentication. Restricted to Search Fund notebook only. Purpose: mine Kay's handwritten call notes from Oct-Nov 2025 and earlier.

### Private Art Advisory Full Evaluation
25-40 firms total, 10-15 would be transferable acquisitions. Interesting platform vision but blocked by key person risk (client relationships follow the advisor) and discretionary spend (first thing cut in downturn). Same pattern as every advisory niche.

### Key Person Risk + Discretionary Spend
These two factors are the universal blockers on advisory niches. They make the target great to own (high margins, intellectual work) but terrible to buy (value walks out the door, revenue is fragile).

### Commercial Cleaning Backstop
Kay's fallback at 18 months (currently at 15): commercial cleaning. She knows it from inside Chanel — boring, necessary, recurring. She rejected it only because of operating reality, not economics. If nothing better materializes in 3 months, this becomes the play.

## Still To Test
- target-discovery (Linkt single cycle)
- outreach-manager (draft flow)
- Review existing top 5 niches + ideation against new initial screen criteria

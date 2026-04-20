---
name: river-guide-builder
description: "Build complete Niche Network per active niche: external ecosystem (associations + named individuals) + cross-check against Kay's network + industry-experience scan across her network. Outputs land in target-list sheet tabs. Attio writes default OFF."
user_invocable: true
context_budget:
  skill_md: 2500
  max_references: 3
  sub_agent_limit: 2000
---

<objective>
Build the complete **Niche Network** per active niche. For each niche, produce a bidirectional map:

- **External ecosystem** — associations + named individuals who touch deal flow (river guides)
- **Network cross-check** — which of those external contacts already intersect Kay's existing network?
- **Industry-experience scan** — who in Kay's existing network has industry-relevant work history, independent of the external ecosystem research?

This replaces the prior single-direction "Coffee Chat Menu" framing AND the niche-intelligence Step 5b validation-contacts output. Unified into one skill because the schemas are 90% overlapping.

**Proof of concept: Margot Romano.** She introduced Kay to Alexandra Kelly (UOVO), Sarah De Blasio (Chartwell Insurance), and Christopher Wise (Risk Strategies). Every conversation produced at least one high-quality introduction. This skill systematizes finding more Margots AND surfaces people like Margot already in Kay's network.

**This skill does NOT:**
- Scan broker platforms for posted deals (deal-aggregator)
- Draft outreach emails to business owners (outreach-manager)
- Create or manage target sheets (target-discovery)
- Track nurture cadences (relationship-manager)

**This skill DOES:**
- Research ecosystem contacts per niche across 6 categories (Phase 1)
- Cross-check each external contact against Kay's network via warm-intro-finder (Phase 2)
- Scan Kay's network for people with industry-relevant experience via Apollo employment history + LinkedIn CSV + Attio fields + vault + Gmail (Phase 3)
- Write results to three tabs on each niche's target-list sheet: Associations | River Guides | Network Matches

**Attio write behavior (config flags, default OFF):**
- `ATTIO_WRITE_RIVER_GUIDES: false` — if true, auto-create Attio People records for river guides with `relationship_type = "River Guide"`
- `ATTIO_TAG_NETWORK_MATCHES: false` — if true, tag existing Attio records with industry metadata when they hit on Phase 3 scan
- Both default OFF until Kay decides. Flipping to `true` is a one-line config change, no code rework.
</objective>

<ecosystem_categories>
## 6 Ecosystem Categories (Phase 1)

For each active niche, research and identify contacts in these categories:

### 1. Association Leaders
Officers, board members, committee chairs of industry associations. They know every member and see industry dynamics.

### 2. Industry CPAs
Accounting firms specializing in the industry. They see the financials. Example: PCO Bookkeepers (Dan Gordon, $1B+ in pest M&A transactions).

### 3. Industry M&A Lawyers / Advisors
Attorneys + boutique M&A advisors handling transactions in the niche. Know what's trading, at what multiples. Example: Sica Fletcher for specialty insurance ($19B+ since 2014).

### 4. Consultants & Advisors
Management consultants, valuation firms, industry advisors who work with owners on operational health, growth, succession. Example: Reagan Consulting (insurance), Potomac Pest Control Group.

### 5. Adjacent Operators
Owners of related businesses who know the competitive landscape and hear about deals through industry networks.

### 6. Validation Contacts *(lifted from niche-intelligence Step 5b — 2026-04-20)*
Industry analysts, former operators, trade press editors, conference speakers who can assess thesis viability. Historically underperformed as cold-call targets (Kay: "no one was answering"), but high-value when discovered via warm paths. Schema merges into River Guides output with a `category = "Validation"` tag rather than a separate file.
</ecosystem_categories>

<unified_schema>
## Unified Niche Network Schema

Each niche's target-list sheet has four tabs (created by target-discovery or jj-operations on niche activation):

| Tab | Owner | Purpose |
|---|---|---|
| Full Target List | Sam / DealsX / target-discovery | Acquisition targets |
| Do Not Call | target-discovery | Warm-intro reserves + PE-owned exclusions |
| Niche Context | niche-intelligence | Industry thesis summary |
| **Associations** | **river-guide-builder Phase 1** | Trade orgs, conferences, events |
| **River Guides** | **river-guide-builder Phase 1+2** | Named individuals who touch deal flow |
| **Network Matches** | **river-guide-builder Phase 3** | People in Kay's network with industry experience |

### Associations tab schema (7 cols)

`Association Name | Website | Events Page URL | Scope | Membership Cost | Member? | Notes`

### River Guides tab schema (11 cols — expanded for Phase 2)

`Name | Title | Firm | Email (if public) | LinkedIn | Category | Score (1-9) | Known Contact | Source | Evidence | Notes`

- **Category:** Association Leader / Industry CPA / M&A Lawyer / Consultant / Adjacent Operator / Validation Contact
- **Score:** 1-9 via 3-dimension scoring (Deal Flow Proximity × Accessibility × Niche Alignment)
- **Known Contact:** `WARM` / `INVESTOR INTRO` / `SHARED BACKGROUND` / `COLD` (populated by Phase 2)
- **Source:** `LinkedIn / Attio / Vault / Gmail / Investor` (populated by Phase 2)
- **Evidence:** short snippet (e.g., "LinkedIn 1st degree, connected 2019")

### Network Matches tab schema (8 cols — new)

`Name | Source | Current/Past Employer | Role/Position | Match Strength | Keywords Matched | Intro-Path Potential | Notes`

- **Source:** `LinkedIn CSV / Attio / Vault / Gmail`
- **Match Strength:** `H` (current C-suite or clean owner/founder past role), `M` (past role 3+ years), `L` (tangential keyword hit)
- **Keywords Matched:** list of niche keywords that triggered the match
</unified_schema>

<workflow>
## Workflow

### Phase 1 — Ecosystem Discovery

**Input:** niche name + target-list sheet ID

1. Read niche keyword file at `.claude/skills/river-guide-builder/references/niche-keywords/{niche-slug}.yaml`
2. Research 6 categories via web + Apollo + LinkedIn:
   - Association Leaders, Industry CPAs, M&A Lawyers, Consultants, Adjacent Operators, Validation Contacts
3. Cross-reference against Do Not Call tab to exclude DNC-flagged names (e.g., Acumen/Uovo/Hangman leadership for Art Storage)
4. Score each contact 1-9 on 3 dimensions (Deal Flow Proximity × Accessibility × Niche Alignment)
5. Write Associations tab (org-level) + River Guides tab Phase 1 columns (Name/Title/Firm/Email/LinkedIn/Category/Score/Notes)

### Phase 2 — Cross-Check Against Kay's Network

**Input:** River Guides tab from Phase 1

For each row, call warm-intro-finder's 5-source scan (reuse — don't rebuild):
1. LinkedIn CSV at `archives/linkedin/connections.csv`
2. Attio People search (`mcp__attio__search_records_by_content` by name, `search_records_by_relationship` by company)
3. Vault entities at `brain/entities/*.md`
4. Gmail history (`gog gmail search`)
5. Investor network

Populate 3 new columns per river guide: `Known Contact` (WARM/INVESTOR INTRO/SHARED BACKGROUND/COLD), `Source` (which of 5 sources hit), `Evidence` (short snippet).

**Association member cross-check:** for each association, attempt to pull public member directory / board roster / conference speaker list. Run each name through the same 5-source scan. Hits append to River Guides tab with `Notes = "found via {association} member roster"`.

### Phase 3 — Industry-Experience Network Scan

**Input:** niche keyword file + access to Kay's network data

Scan Kay's network for people with industry-relevant work history.

**Data sources (priority order):**

1. **Attio `nddl_apollo_employment_history`** (primary — post-enrichment of high-priority records, see Apollo Enrichment Dependency below)
   - For each Attio person: iterate past-role objects, match `organization_name` against niche keywords + `customer_segment_keywords`
   - Match strength: `H` if clean owner/founder/C-suite title + 3+ years tenure, `M` if 3+ years any role, `L` if < 3 years or tangential
2. **LinkedIn CSV** (`archives/linkedin/connections.csv` — 901 rows)
   - Grep `Company` + `Position` against niche keywords. Current-employer only; no past-role data.
3. **Attio standard fields** (`job_title`, `company`, `description`)
4. **Vault entities** (`brain/entities/*.md`) — grep for niche keywords
5. **Gmail** — email domain match against known industry customer/employer domains

Write results to Network Matches tab. Deduplicate across sources (Attio record wins; LinkedIn CSV second).

### Phase 4 — Optional Attio Writes (config-gated)

If `ATTIO_WRITE_RIVER_GUIDES=true`: auto-create Attio People records from River Guides tab with `relationship_type = "River Guide"`, `nurture_cadence = "Dormant"`, `how_introduced = "river-guide-builder 2026-04-20"`.

If `ATTIO_TAG_NETWORK_MATCHES=true`: tag existing Attio records (from Phase 3 hits) with a custom field or note — exact field name TBD by Kay.

Default: both OFF. Skill ships sheet-only until Kay decides.
</workflow>

<apollo_enrichment_dependency>
## Apollo Enrichment Dependency

Phase 3's primary source (`nddl_apollo_employment_history`) depends on Attio records being Apollo-enriched. Enrichment roadmap:

- **2026-04-20** — 5-record verification test (5 credits) → GO
- **2026-04-20 through 2026-05-02** — prioritized enrichment (~500 credit budget, highest-priority records: nurture_cadence populated → relationship_type populated → recent interactions → bulk)
- **2026-05-03 onward** — full remaining-population enrichment (fresh 2,520 credit month)

Reports:
- `brain/outputs/2026-04-20-apollo-enrichment-test.md` (Step 0)
- `brain/outputs/2026-04-21-apollo-prioritized-enrichment-report.md` (Step 1)
- `brain/outputs/2026-05-03-apollo-full-enrichment-report.md` (Step 1b)

**Degraded-mode behavior:** Before enrichment complete for a given Attio record, Phase 3 falls back to LinkedIn CSV + Attio standard fields + vault + Gmail. Re-running the skill on a niche after more records are enriched will produce richer Network Matches output automatically — no code change.
</apollo_enrichment_dependency>

<scoring>
## Phase 1 Scoring (retained from prior version)

| Dimension | 3 (High) | 2 (Medium) | 1 (Low) |
|-----------|----------|------------|---------|
| Deal Flow Proximity | Directly advises owners on exits/succession | Sees financials or industry data | Knows the industry generally |
| Accessibility | Warm intro path exists | Cold but likely to respond | Cold, unclear response |
| Niche Alignment | Works exclusively in this niche | Works in adjacent space | General practice |

**Total 7-9:** Priority coffee chat target
**Total 4-6:** Worth an intro email
**Total 1-3:** Monitor only
</scoring>

<finder_fee_program>
## Finder's Fee Program

**Template:** MANAGER DOCUMENTS / LEGAL / CONTRACTS (existing on Drive — needs Andy Lock review before use)

Open questions for Kay:
1. Fee amount ($5K? $10K? Percentage?)
2. Trigger — signed LOI or signed NDA?
3. Start offering immediately or wait until first organic referral?
4. Andy Lock review timeline?
</finder_fee_program>

<integrations>
## Integration Points

| Skill | Integration |
|---|---|
| **niche-intelligence** | Provides niche context. Step 5b validation-contacts **sunset 2026-04-20** — concept lifted into Phase 1 Category 6 (Validation Contacts). |
| **warm-intro-finder** | Phase 2 engine — reuse 5-source scan verbatim |
| **meeting-brief-manager** | Generates prep for coffee chats with river guides |
| **relationship-manager** | Tracks nurture cadence after Kay connects |
| **deal-aggregator** | When a river guide surfaces a deal, enters intermediary pipeline |
| **outreach-manager** | Initial outreach to new river guide targets (via Kay Email channel) |
| **target-discovery** | Owns target-list sheet creation; river-guide-builder writes to its Associations/River Guides/Network Matches tabs |
| **Apollo** | Phase 3 primary data via `nddl_apollo_employment_history` |
</integrations>

<schedule>
## Run Triggers

- New niche enters Active-Outreach on WEEKLY REVIEW — full 3-phase run
- Monthly refresh per active niche (for Phase 1 drift)
- Post-Apollo-enrichment-batch — Phase 3 re-run on niches to pick up newly-enriched records
- Ad-hoc on Kay's request

**Output location:** target-list sheet tabs (Associations + River Guides + Network Matches). No standalone `brain/context/river-guide-menu-*.md` file anymore — outputs live where Sam / JJ / Kay actually work.
</schedule>

<success_criteria>
## Success Criteria

- [ ] Niche keyword YAML exists at `references/niche-keywords/{niche-slug}.yaml`
- [ ] Phase 1: all 6 categories attempted, scored, populated on Associations + River Guides tabs
- [ ] Phase 2: every River Guide row has Known Contact populated
- [ ] Phase 3: Network Matches tab ≥ 5 rows (fewer is acceptable if niche is truly novel to Kay's network)
- [ ] Do Not Call cross-reference applied (no DNC-flagged leadership surfaced)
- [ ] False positives < 30% on Network Matches (spot-check 3 rows against actual signals)
- [ ] Zero Attio `create_record` calls unless config flags ON
- [ ] Only `update_record` calls against `nddl_apollo_*` fields permitted during enrichment runs
</success_criteria>

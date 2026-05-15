---
name: river-guide-builder
description: "Build complete Niche Network per active niche: external ecosystem (associations + named individuals) + cross-check against Kay's network + industry-experience scan across her network. Outputs land in target-list sheet tabs. Attio writes default OFF."
archetype: router
context_budget:
  skill_md: 200
  max_references: 12
  learnings_md: 40
  sub_agent_limit: 500
user_invocable: true
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

**Attio write behavior — Threshold Rule (event-driven, no config flags):**
- `river-guide-builder` **NEVER** auto-creates Attio records. Outputs live only in the target-list Google Sheet tabs.
- Attio records are created by `outreach-manager` at the moment Kay sends her **first outbound** (email / LinkedIn DM / intro ask) to a River Guides or Network Matches entry.
- Created record gets `relationship_type` per category (River Guide / Industry Expert / Advisor). **No `nurture_cadence` is set** — intermediaries are passively monitored via `relationship-manager`'s dormancy logic (100-day silence flag), not cadence-prompted.
- Rationale: match Attio's native inbound filter (no record until Kay engages). See `feedback_attio_threshold_rule.md` + `feedback_intermediary_dormancy_monitoring.md`.
- The retired `ATTIO_WRITE_RIVER_GUIDES` and `ATTIO_TAG_NETWORK_MATCHES` config flags are gone — threshold rule replaces them.
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
Industry analysts, former operators, trade press editors, conference speakers who can assess thesis viability. Historically underperformed as cold-call targets (Kay: "no one was answering"), but high-value when discovered via warm paths.

**Note:** These 6 categories are Phase 1 RESEARCH buckets (guides the agent on what types of contacts to identify). They are NOT sheet columns. The canonical River Guides tab uses `Industry` (vertical — e.g., "Wealth Management", "Art Insurance") instead of Category. `Title` implicitly carries role-in-ecosystem info. The ecosystem category is used as a research prompt only, not persisted on the sheet.
</ecosystem_categories>

<unified_schema>
## Unified Niche Network Schema

Each niche's target-list sheet has four tabs:

| Tab | Owner | Purpose |
|---|---|---|
| Full Target List | **Sam (DealsX pipeline) — NOT this skill** | Acquisition targets. Sam handles list building externally; when he delivers, rows are added to this tab. **Do not attempt to populate.** |
| Do Not Call | target-discovery | Warm-intro reserves + PE-owned exclusions |
| Niche Context | niche-intelligence | Industry thesis summary |
| **Associations** | **river-guide-builder Phase 1** | Trade orgs, conferences, events |
| **River Guides** | **river-guide-builder Phase 1+2** | Named individuals who touch deal flow |
| **Network Matches** | **river-guide-builder Phase 3** | People in Kay's network with industry experience |

**Scope of this skill:** Associations + River Guides + Network Matches only. The Full Target List tab is Sam's domain — this skill never writes to it and never triggers target-discovery to fill it.

### Canonical sheet location (Google Drive)

All niche target-list sheets live in **`OPERATIONS/TARGET LISTS/EMAIL OUTREACH/`** (folder ID `14MLYC9W-jTH-NXxZh_LN-Q_d5wCUKzn_`).

**Exception:** `Premium Pest Management - Target List` lives one level up at `OPERATIONS/TARGET LISTS/` (folder ID `1WfbzezRkD7Kr0FOA76y99x5wV8lwRkVc`) because JJ is actively running cold calls from it — do not move it.

When a new niche activates:
1. **Copy from the G&B Target List Template** (file ID `1wIK4Jv56QIZejcmpq-gGrCWAPe07eJWUbKsWTRwh778` in G&B MASTER TEMPLATES folder) — it has all canonical tabs pre-scaffolded
2. Place the new sheet inside `14MLYC9W-jTH-NXxZh_LN-Q_d5wCUKzn_` (EMAIL OUTREACH)
3. **Ship Associations tab first** (Phase 1 associations-only research). Do NOT populate River Guides or Network Matches on first ship.
4. Populate River Guides + Network Matches **only after** Apollo enrichment is complete AND Attio MCP is available. Running these phases degraded (missing sources) produces noisy output Kay then has to discard. See `feedback_step_by_step_interconnected_plans.md`.
5. Wait for Sam's target list to populate the Full Target List tab.

See `reference_target_list_canonical_folder.md` for the full folder-convention reference.

### Associations tab schema (7 cols)

`Association Name | Website | Events Page URL | Scope | Membership Cost | Member? | Notes`

### River Guides tab schema (7 cols — canonical, Kay-approved 2026-04-20)

`Name | Title | Firm | Location | LinkedIn | Industry | Why`

- **Name** = primary key, always first column
- **Title** = full title including division/group (e.g., "Vice President, Financial Advisor, Blue Rider Group")
- **Firm** = employer name
- **Location** = City, State
- **LinkedIn** = profile URL
- **Industry** = vertical tag (e.g., "Wealth Management", "Art Insurance", "Industry CPA") — used for sheet filtering/sorting. Replaces the old Category column.
- **Why** = free-text value/intro context (1-3 sentences — what they know, who they can intro to, why they matter for this niche). Mirrors the "Why" field from Kay's validation-call intake format.

**Population rule:** If a river guide is already a known contact (in Kay's Attio / direct network), **do not populate Location/LinkedIn** — Kay already has that data. Name + Title + Firm + Industry + Why are sufficient. Only fill full contact fields for new/cold river guides.

**Phase 2 output columns (NOT in base schema):** When Phase 2 runs (post-Apollo + Attio MCP), append three tracking columns to the right: `Known Contact` (WARM / INVESTOR INTRO / SHARED BACKGROUND / COLD) / `Source` (which of 5 scan sources hit) / `Evidence` (snippet). These are append-only additions, not part of the canonical intake schema.

### Network Matches tab schema (8 cols — Phase 3 output)

`Name | Source | Current/Past Employer | Role/Position | Match Strength | Keywords Matched | Intro-Path Potential | Notes`

- **Source:** `LinkedIn CSV / Attio / Vault / Gmail`
- **Match Strength:** `H` (current C-suite or clean owner/founder past role), `M` (past role 3+ years), `L` (tangential keyword hit)
- **Keywords Matched:** list of niche keywords that triggered the match
- **Note:** Populated by Phase 3 only — requires Apollo `nddl_apollo_employment_history` to produce quality output.
</unified_schema>

<workflow>
## Workflow

### Phase 1 — Ecosystem Discovery

**Input:** niche name + target-list sheet ID

**First-ship scope:** Associations tab only. River Guides + Network Matches do NOT populate on first ship — they wait for Apollo enrichment + Attio MCP. See `feedback_step_by_step_interconnected_plans.md`.

1. Read niche keyword file at `.claude/skills/river-guide-builder/references/niche-keywords/{niche-slug}.yaml`
2. Research associations (trade orgs, conferences, events) via web — populate Associations tab
3. Research river-guide candidates via the 6 ecosystem buckets (Association Leaders, Industry CPAs, M&A Lawyers, Consultants, Adjacent Operators, Validation Contacts) — **hold this output for Phase 2 run, do NOT write to River Guides tab yet**
4. Cross-reference against Do Not Call tab to exclude DNC-flagged names (e.g., Acumen/Uovo/Hangman leadership for Art Storage)

**River Guides tab population:** After Phase 2 (cross-check) runs with full source access, write Phase 1 candidates to the River Guides tab using the canonical 7-col schema (`Name | Title | Firm | Location | LinkedIn | Industry | Why`). Skip Location/LinkedIn for rows where the person is already a known contact in Kay's Attio/network.

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

**⚠️ Investigation open (2026-04-20):** Phase 3 calibration on 8 niches returned only 5 H-strength matches across 388 Apollo-enriched records, 6 niches at zero. Kay flagged that her lived network knowledge contradicts this — she has contacts in specialty-insurance, vertical-saas-luxury, and other niches the scan missed. Root cause under investigation. Suspected vectors: (a) subagent only hit `nddl_apollo_employment_history` despite spec requiring 4 sources; (b) keyword tokenization hits substring collisions; (c) H-criterion too strict (senior title + 3yr) excludes valid soft matches; (d) 21% Attio enrichment coverage means 79% of network unscannable until Step 1b lands 2026-05-03. **Do not run Phase 3 to completion until root cause resolved.** See [[brain/traces/2026-04-20-network-yield-vs-lived-knowledge]] for context.

**Mandatory: hit ALL 4 data sources.** Subagents running Phase 3 must scan every source, not just Apollo employment_history. Skipping any source silently is a defect — flag and halt if a source is unreachable.

**Two-sided cap check (pre-write gate):** Before any writes, compare per-niche count against Kay's expected range. Pause on `count > 10` OR `count == 0 when Kay expects signal`. Both are calibration signals, not green lights.

**Data sources (priority order — all MUST be scanned):**

1. **Attio `nddl_apollo_employment_history`** (primary — post-enrichment of high-priority records, see Apollo Enrichment Dependency below)
   - For each Attio person: iterate past-role objects, match `organization_name` against niche keywords + `customer_segment_keywords`
   - Match strength: `H` if clean owner/founder/C-suite title + 3+ years tenure, `M` if 3+ years any role, `L` if < 3 years or tangential
2. **LinkedIn CSV** (`archives/linkedin/connections.csv` — 901 rows)
   - Grep `Company` + `Position` against niche keywords. Current-employer only; no past-role data.
3. **Attio standard fields** (`job_title`, `company`, `description`)
4. **Vault entities** (`brain/entities/*.md`) — grep for niche keywords
5. **Gmail** — email domain match against known industry customer/employer domains

Write results to Network Matches tab. Deduplicate across sources (Attio record wins; LinkedIn CSV second).

### Phase 4 — Attio Writes (event-driven, not config)

**Threshold rule (replaces prior config flags):** river-guide-builder NEVER auto-creates Attio records. Attio records are created by `outreach-manager` at the moment Kay sends her first outbound to a River Guides entry. The retired `ATTIO_WRITE_RIVER_GUIDES` and `ATTIO_TAG_NETWORK_MATCHES` flags are gone. See `feedback_attio_threshold_rule.md` + `feedback_intermediary_dormancy_monitoring.md`.

Until Kay's first outbound: River Guides live only on the target-list sheet.
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

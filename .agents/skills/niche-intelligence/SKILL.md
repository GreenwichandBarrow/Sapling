---
name: niche-intelligence
description: "Niche Intelligence workflow. Full run Monday night: gathers data from newsletters, web, calls, email, and research; identifies new niches; runs initial screen; creates one-pagers; scores against G&B industry scorecard; updates Industry Research Tracker; feeds Tuesday Good Morning as Kay's thesis decision surface. Light thesis signal scan Thursday night feeds Friday Good Morning with urgent/queue/park signals."
# WARNING: 2.2x over archetype cap; refactor pending per item 2.
archetype: orchestrator
context_budget:
  skill_md: 450
  max_references: 12
  learnings_md: 40
  sub_agent_limit: 500
user-invocable: true
---

<credentials>
## Credentials (read first)

**1Password is the first rung — always.** Before any op://-backed CLI (this skill uses `gog sheets`/`gog drive`/`gog docs` to update the Industry Research Tracker):
```bash
source /home/ubuntu/projects/Sapling/scripts/op-env.sh
```
Exports `GOG_KEYRING_PASSWORD`, `SLACK_WEBHOOK_OPERATIONS`. **NEVER `source scripts/.env.launchd` raw** — hook-blocked; see `feedback_op_env_before_op_backed_cli`.

If a `gog` call fails with `aes.KeyUnwrap(): integrity check failed`, the cause is almost always that `op-env.sh` was not sourced — the keyring is fine. Re-source and retry, NEVER rotate credentials.

Gmail access is read-only in this workflow. Use `gog gmail search/read ... --gmail-no-send` when reading newsletters, broker/deal-flow mail, investor updates, or historical email. This skill never sends, draft-sends, forwards, or autoreplies to email.
</credentials>

<essential_principles>

## Architecture: 5-Step Pipeline with Parallel Sub-Agents

This skill implements a **sequential pipeline** where each step depends on the previous step's output. Within steps, sub-agents run in **parallel** where possible.

```
Step 1: GATHER (parallel)      → raw intelligence
Step 1b: SYNTHESIZE (sequential) → cross-source pattern recognition
Step 2: IDENTIFY (sequential)  → new niche candidates
Step 3: ONE-PAGER (parallel)   → pptx deliverables
Step 4: SCORE (sequential)     → scored niches + final report
Step 4b: VALIDATE (parallel)   → buy-box target count (gate before promotion)
Step 5: UPDATE (sequential)    → tracker updated + notification
Step 5b: VALIDATION CONTACTS (parallel) → key contacts + risk questions for Kay
```

### Chatroom Coordination

All sub-agents post findings to a shared chatroom at:
```
brain/traces/agents/{YYYY-MM-DD}-niche-intelligence.md
```

### Deliverable Verification (Stop Hooks)

After each step that produces a deliverable, verify before proceeding:
- **Step 1:** Chatroom has posts from both gathering agents (RECENT + HISTORICAL)
- **Step 3:** Each niche has a .pptx file created and uploaded to Drive
- **Step 4:** Output report exists at `brain/outputs/{date}-niche-intelligence-report.md`
- **Step 5:** Google Sheet updated with new rows
- **Step 5b:** Validation contacts page created for any niche flagged for activation

If verification fails, log the failure to chatroom and notify user — do NOT proceed to next step.

### Key References

| Reference | Path |
|-----------|------|
| Scorecard structure | `references/scorecard-structure.md` |
| One-pager template | `references/one-pager-template.md` |
| Learnings context | `brain/context/learnings.md` |
| Industry tracker | `references/tracker-access.md` |
| Sub-agent prompts | `references/sub-agents.md` |

### External Dependencies

| Tool | Purpose |
|------|---------|
| `gog` CLI | Gmail (newsletters), Google Sheets (tracker), Google Drive (one-pagers) |
| `last30days` skill | Web/social research via `/last30days` |
| Granola REST wrapper | Meeting transcript retrieval via `~/.local/bin/granola-api` |
| OneNote MCP | SEARCH FUND notebook — industry memos, deal convos, research notes |
| `python-pptx` | One-pager generation |
| `WebSearch` | Supplemental research for scoring |

**Headless gaps are evidence, not excuses.** If Granola MCP, OneNote MCP, ChatGPT export, or any other source is unavailable in the scheduled environment, document the gap in the report and sidecar. Use available fallbacks (`brain/calls/`, vault outputs, inbox signals) without pretending the missing source was covered.

### Schedule

Runs on two scheduled cycles:

- **Monday night full Niche Intelligence run.** Codex posts the Niche Intel Report link to #operations by 10am Tuesday. Tuesday Good Morning surfaces the CEO-level `Activate / Hold / Kill / Test` recommendations directly to Kay, including recommended conversion channel and owner. Kay makes the thesis call from the Good Morning brief; after Kay decides, Codex updates or routes an update to the Industry Research Tracker so status and channel ownership are captured. Camilla is pulled in only when Kay wants economics, modeling, or diligence support on an activated or uncertain thesis.
- **Thursday night light Thesis Signal Scan.** This is not a full one-pager/scorecard run. It scans fresh PE activity/news, call/email/inbox signals, deal-flow changes, conference signals, and active-thesis momentum. Friday Good Morning surfaces only status changes: urgent fast sprint, queue for Monday full run, park, or no meaningful signal.

**Deal 1 thesis gate:** For the first search entity, any thesis recommended for `Activate` or `Test` must include an explicit tailwind or growth trend. If no tailwind exists, recommend `Hold`, `Park`, or `Kill`; do not move it into active sourcing.

**Channel decision gate:** `Activate` / `Test` does not automatically mean target build or outreach. Every activated/test thesis must include a channel recommendation before execution: Tracker Channel, Execution Path, Secondary Channel if any, Do Not Use channels, owner split, and one-sentence rationale. The channel decision is made in Good Morning by Kay and must be written to the Industry Research Tracker `Outreach Channel` field before `target-discovery`, `outreach-manager`, DealsX, Camilla cold qualifiers, or Kay warm outreach starts.

**Scheduled-cycle failure escalation:** If the Monday full run or Thursday signal scan fails, times out, produces no verified report, or skips tracker validation, the next Good Morning must surface a red system decision item: `RECOMMEND: Investigate Niche Intelligence failure` with the latest log/artifact timestamp and YES / NO / DISCUSS framing.

</essential_principles>

<intake>

When `/niche-intelligence` is invoked:

1. Read `references/tracker-access.md` for current tracker state
2. Read `brain/context/learnings.md` for evaluation context
3. Create chatroom at `brain/traces/agents/{date}-niche-intelligence.md`
4. Execute the pipeline: `workflows/friday-pipeline.md`

No intake question needed — this is a fully automated workflow.

</intake>

<niche_inbox>

## Niche Inbox: How New Niche Ideas Enter the Pipeline

Niche ideas come from many places — not just the Monday night gathering agents. The pipeline must accept ideas from ANY source and route them through the full process (Identify → One-Pager → Score → Add to tracker). **Nothing skips steps. Nothing goes straight to WEEKLY REVIEW without a one-pager and score.**

### Sources that feed niche ideas into the pipeline:

| Source | How it arrives | Entry point |
|--------|---------------|-------------|
| Monday night gathering agents (RECENT + HISTORICAL) | Automated Step 1 run | Step 1b (Synthesize) → Step 2 (Identify) |
| Kay + Codex conversations | Kay mentions a niche idea, contact shares a list, brainstorming session | Written to `brain/inbox/` as niche signal → picked up at Step 2 |
| OneNote research notes | Kay's handwritten notes reference industries (e.g., Mike Horowitz's insurance back-end list) | Written to `brain/inbox/` as niche signal → picked up at Step 2 |
| Linkt data analysis | Patterns found across old or new Linkt exports (e.g., environmental compliance cluster) | Written to `brain/inbox/` as niche signal → picked up at Step 2 |
| Pipeline-manager | Niche signals detected in Granola calls or Gmail during daily ingestion | Written to `brain/inbox/` as `topic/niche-signal` → picked up at Step 1 (RECENT passive signals) |
| Contact referrals | Investor, operator, or advisor suggests a niche (e.g., Jeremy Black → TCI, Mike Horowitz → insurance back-end) | Written to `brain/inbox/` as niche signal → picked up at Step 2 |
| Conference attendee analysis | Conference-discovery surfaces an industry cluster | Written to `brain/inbox/` as niche signal → picked up at Step 2 |

### Writing a niche idea to the inbox:

When a niche idea surfaces outside of the full weekly run, write it to:
`brain/inbox/YYYY-MM-DD-niche-idea-{slug}.md`

```yaml
---
date: YYYY-MM-DD
type: inbox
status: pending
confidence: medium
source: conversation | onenote | linkt-analysis | contact-referral | conference | pipeline-manager
tags:
  - inbox
  - topic/niche-signal
  - source/{source}
---

## Niche Idea: {name}

**Source:** {who/what surfaced it}
**Context:** {why it came up, any data points}
**Initial fit assessment:** {quick gut check against buy box}
**Named companies (if any):** {list}
**Contacts who can help (if any):** {list}
```

### Processing niche ideas:

**Option A (queue for Monday full run):** Leave in inbox. The RECENT agent's passive signal source picks up `topic/niche-signal` items automatically during the next Monday full weekly run.

**Option B (run now):** Invoke `/niche-intelligence --from-inbox` to process all pending niche ideas through Steps 2-5 immediately. Useful for testing or when Kay wants results before the next Monday full cycle.

**Option C (organic intake chat):** Kay can flag a new niche idea in a dedicated CIO chat as it comes up from meetings, emails, deal leads, new websites, or brainstorming. The chat should create a lightweight `brain/inbox/` niche idea record, do only enough first-pass analysis to route it, and then choose:
- queue for Monday full run if normal priority,
- run `/niche-intelligence --from-inbox` if time-sensitive or tied to an active lead,
- tag as `watchlist` / `needs-more-signal` if the idea is too thin,
- tag as `do-not-resurface` only when there is clear prior killed/tabled rationale.

The intake chat is for capture and routing, not bypassing the pipeline. Anything that might become an active niche still goes through Identify → One-Pager → Score → Tracker.

### Dedicated CIO thesis brainstorming thread behavior

When Kay raises a niche, market, company type, contact insight, podcast idea, investor comment, conference, or deal-flow pattern in the canonical CIO Niche Intake and Thesis Discovery thread, do not jump straight to outreach execution. First clarify and route the signal.

Default first-pass questions to answer:
- What is the precise niche?
- Why now?
- What customer pain is intensifying?
- Is there recurring, reoccurring, repeat, or actuarial revenue?
- Are margins likely attractive?
- Is there enough target density in the U.S.?
- Is PE already too far into it?
- Does this fit G&B's luxury infrastructure / heritage / quality / community architecture?
- Is it suitable for Deal 1, a future HoldCo company, or just market intelligence?

For any promising or unresolved idea, produce a short `Niche Signal Capture` in the chat and, when the signal should persist, write it to `brain/inbox/` with `topic/niche-signal`.

Required chat format:
```
Niche Signal Capture
- Niche name:
- One-sentence thesis:
- Tailwind / growth driver:
- Why it may fit G&B:
- Main concern:
- Suggested action: Urgent Fast Sprint / Queue for Monday / Park / Kill
- Recommended Tracker Channel if Activate/Test: Kay Email / DealsX Email / Cold-Call-Only / No outreach yet
- Recommended Execution Path: Kay warm outreach / DealsX batch / call-first / conference / intermediary / no outreach yet
- Owner split: Kay / Codex / Camilla / DealsX
```

Routing rules:
- `Urgent Fast Sprint` = time-sensitive, tied to an active deal/contact, or likely to support an LOI sprint before Monday.
- `Queue for Monday` = promising but not time-sensitive; capture in inbox and let the Monday full run build the one-pager, scorecard, and tracker row.
- `Park` = interesting but missing a tailwind, target-density proof, or revenue-quality evidence.
- `Kill` = clear mismatch, prior killed rationale, no tailwind for Deal 1, too transactional, too retail/ecommerce/software/pure consulting, or no plausible target supply.
- `Owner: Kay` = thesis decision, relationship judgment, or direct founder/investor/customer signal.
- `Owner: Codex` = research, tracker routing, one-pager, scorecard, target-density proof, or Good Morning surfacing.
- `Owner: Camilla` = only after Kay asks for economics, modeling, diligence, or execution support.
- `Owner: DealsX` = outsourced outreach or market-list execution after Kay activates a thesis and approves the channel.

Channel recommendation rule:
- Recommend **Tracker Channel = Kay Email; Execution Path = Kay warm outreach** when trust, taste, luxury credibility, warm paths, or seller psychology materially change conversion odds.
- Recommend **Tracker Channel = DealsX Email; Execution Path = DealsX batch** only when the thesis has enough target density, messaging can be standardized without losing trust, and broad outbound is likely to convert.
- Recommend **Tracker Channel = Cold-Call-Only; Execution Path = call-first** only when phone responsiveness or local/service-market dynamics matter more than brand/taste credibility.
- Recommend **Tracker Channel = No outreach yet; Execution Path = Conference or Intermediary** when the fastest path is concentrated around a known event, association, estate/planning network, trade group, or industry connector. Route through conference-discovery or relationship/warm-intro work before target-discovery.
- Recommend **Tracker Channel = No outreach yet; Execution Path = no outreach yet** when the thesis is promising but ICP, target density, or tailwind evidence is not strong enough to risk burning the market.

Kay is the default thesis decision-maker. Camilla is not the default recipient of new thesis ideas.

### Robust niche discovery method

The recurring failure mode is re-surfacing already-discussed niches instead of discovering new ones, or stopping at visible end-markets instead of finding the picks-and-shovels vendors that benefit when those markets grow. Each full Monday run must include a source-led expansion pass before scoring. Do not start from prior favorite theses. Start from source systems, translate broad themes into growth trends, and only then map to G&B fit.

#### G&B umbrella themes for expansion

Use these themes as lenses, not as final niches:
1. **Luxury, Heritage & Personal Goods** — jewelry, watches, beauty, fragrance, art, design, private-client goods, and heritage brands.
2. **Asset Protection & Stewardship** — insurance, storage, appraisal, documentation, custody, repair, restoration, logistics, and risk management around valuable assets.
3. **Beauty, Wellness & Longevity Infrastructure** — services and vendors that support beauty, longevity, aesthetics, wellness, personal care, and premium consumer health categories.
4. **Family Wealth, Legacy & Life Infrastructure** — services supporting affluent families, children, education, estates, succession, elder/family transitions, and long-duration trust.
5. **Trust, Compliance & Verification** — testing, certification, regulatory, audit, claims, records, QA, provenance, safety, and outsourced administrative workflows where trust must be documented.

#### Picks-and-shovels expansion requirement

For every strong theme or growth trend, run this expansion before naming final candidate niches:

`Theme -> Growth Trend -> Operational Complexity Created -> Second-Order Beneficiaries -> Fragmented Service Niches -> Target-Density Proof -> Recommended Channel Path`

Required question: **Who makes money because this trend creates operational complexity?**

Each theme/trend must generate both mainline and edge candidates:
- **Obvious/mainline:** brands, retailers, direct service providers, visible operators.
- **Back-end infrastructure:** packaging, kitting, fulfillment, repair, storage, logistics, installation, maintenance, records, CRM/admin, billing, and workflow outsourcing.
- **Picks-and-shovels:** vendors that sell necessary inputs, services, QA, equipment, recurring maintenance, or labor to the growing category.
- **Compliance/risk:** testing, insurance, documentation, claims, safety, provenance, import/export, regulatory, and audit support.
- **Specialty networks:** associations, trade shows, certification bodies, local specialists, and intermediaries that reveal hidden target pools.

Example: If Korean skincare growth appears as a signal, do not stop at skincare brands, beauty retailers, or ecommerce. Also test beauty packaging 3PL, premium kitting and assembly, formulation/testing labs, import/regulatory compliance support, sampling and fulfillment vendors, QA/documentation workflows, and beauty conference exhibitor/service-provider lists. The same second-order logic should be applied to jewelry, watches, art, fragrance, hospitality, private-client insurance, wellness, and every other G&B theme.

Minimum discovery passes for a full run:
1. **Customer-environment map:** Pick 1-3 operating environments Kay knows or can credibly access, then list 50 recurring workflows/vendor touchpoints per environment before naming niches. Infer hidden third-party service categories only after the workflow map is complete.
2. **NAICS / taxonomy sweep:** Pull NAICS-adjacent categories touching the relevant luxury sectors, building health, education/child safety, hospitality infrastructure, or investor-surfaced operating environments. Use definitions to expand the candidate universe, not to force generic categories.
3. **Deal-flow artifact sweep:** Search SBA 7(a), broker marketplaces, Axial/DealsX artifacts, and CIM/teaser language for what is actually being financed or sold. Treat listings as saleability evidence, not thesis proof.
4. **Directory / target-density proof:** Use association directories, Apollo/Grata/SourceScrub-style counts, Google Maps/business directories, and trade groups to prove there are independent companies in the relevant geography or US market. No niche should be named as promising without target-density evidence.
5. **PE heat screen:** Check sponsor-backed platforms, add-on activity, and roll-up language. Flag crowded markets early; do not let PE-backed visibility masquerade as target supply.
6. **Negative-memory check:** Compare against tracker killed/tabled/skipped lanes and prior chat decisions. If a niche was previously killed, it can only re-enter with materially new evidence.

Discovery output before scoring must include:
- Candidate universe count reviewed
- Number killed for no tailwind
- Number killed for no target density
- Number killed for PE saturation
- Number killed for revenue quality / transactional model
- Number killed for weak Kay/searcher fit
- 3-10 candidates that survived to preliminary evidence review

Revenue-quality screen must distinguish: contractual recurring, non-contractual recurring, repeat revenue, actuarial revenue, and transactional revenue. Transactional-only businesses should not advance unless there is a clear path to repeat/reoccurring revenue with evidence.

### Searcher-fit and purchase-ability lens

Over the 2025-2026 search, the practical lesson is that purchase ability is often tied to searcher fit. A niche with good economics but no credible Kay-specific access, buyer empathy, operator-recruiting angle, or investor narrative may be theoretically attractive but weak for G&B. Conversely, a niche with moderate generic attractiveness can be more actionable if Kay has a real right to win.

Every candidate that survives initial discovery must be tested against these searcher-fit questions before it is recommended for `Activate` or `Test`:
- **Seller conversation credibility:** Would an owner believe Kay understands the customer, quality bar, and operating stakes of this business?
- **Access edge:** Does Kay have warm paths through luxury, fashion, jewelry, art, hospitality, family office, private club, NYC/Long Island, investor, women-owner, or community networks?
- **Customer fluency:** Can Kay credibly sell to or build relationships with the customer base without sounding like a financial buyer only?
- **Taste / trust / quality edge:** Does the business benefit from judgment, discretion, brand stewardship, service standards, or reputation-sensitive execution?
- **Operator recruiting edge:** Could Kay recruit and retain a credible operator or President for this category?
- **Investor believability:** Would disciplined search investors understand why this is Kay's deal to win, not just a random market?
- **Lifestyle / role fit:** Does the business avoid trapping Kay in day-to-day retail, founder-led craft, field-service dispatch, or pure consulting delivery?
- **Purchase path:** Are likely sellers independent, succession-oriented, reachable, and emotionally/logically open to Kay as buyer?

Use a three-point searcher-fit rating in discovery tables:
- `Strong`: Kay's background/network materially improves access, credibility, and post-close value creation.
- `Medium`: Some fit exists, but the sourcing or operating edge must be proven.
- `Weak`: Attractive market may exist, but Kay has no clear right to win; do not recommend unless target-density and deal-flow evidence is unusually strong.

For Deal 1, a niche should not be recommended for `Activate` unless both are true: (1) there is a clear tailwind or growth trend, and (2) searcher fit is `Strong` or clearly improvable to `Strong` through a named river guide, operator, customer channel, or proprietary target.

### Hair and J-curve resilience lens

Do not over-screen niches for being imperfect. Every acquirable SMB will have hair: founder dependence, messy systems, customer concentration, uneven margins, succession gaps, underbuilt sales, working-capital issues, or operational debt. The discovery question is not whether a niche is clean. The question is whether the business model has enough resilience to absorb the likely post-close J curve when Kay takes over.

For each candidate, identify the specific source of resilience that could carry the acquisition through transition:
- **Recurring / sticky revenue:** contractual renewals, required coverage, replenishment, installed-base service, reoccurring customer behavior, habit, or switching friction.
- **Margins / cash generation:** enough gross margin, EBITDA margin, or owner cash flow to fund management upgrades, systems, recruiting, and early mistakes.
- **Growth tailwind:** customer segment, regulation, compliance burden, infrastructure change, demographic shift, or category expansion that can offset execution drag.
- **Trust / brand / relationship moat:** customer reluctance to switch because failure is costly, embarrassing, risky, or emotionally sensitive.
- **Operational repeatability:** workflows that can be documented, delegated, trained, monitored, or centralized after acquisition.

When reviewing a niche or deal, name the likely hair and then answer: `What absorbs the J curve?` A niche can advance with hair if at least one resilience pillar is strong and there is a credible path for Kay to improve the business post-close. A niche should be held or killed when the hair directly attacks the only reason the business looked attractive.

### The rule:
**Every niche idea, regardless of source, must go through: Identify → One-Pager → Score → Tracker.** The only question is timing (now vs. Monday full run).

</niche_inbox>

<routing>

| Trigger | Workflow |
|---------|----------|
| `/niche-intelligence` | `workflows/friday-pipeline.md` (full pipeline) |
| `/niche-intelligence --step 1` | Run only Step 1 (gathering) |
| `/niche-intelligence --step 2` | Run Steps 1-2 (gather + identify) |
| `/niche-intelligence --from-inbox` | Process pending niche ideas from brain/inbox/ through Steps 2-5 (skip gathering, use inbox items as input) |
| `/niche-intelligence --dry-run` | Run Steps 1-4, skip Step 5 (no tracker writes) |

</routing>

<sub_agents>

## Sub-Agent Registry

### Step 1: Gathering (2 parallel tracks, HISTORICAL spawns sub-agents)

| Agent Name | Type | Description |
|------------|------|-------------|
| `niche-intel-recent` | general-purpose | Last 2 weeks: web research, newsletters, Granola calls, recent emails, vault outputs, passive signals |
| `niche-intel-historical` | general-purpose | Orchestrator that spawns 4 parallel sub-agents to mine the full search history |

**Architecture:** Two time-horizon tracks run in parallel. RECENT is a single agent covering 6 sources from the last 14 days. HISTORICAL is an orchestrator that spawns 4 sub-agents in parallel (one per source cluster), collects their findings, and posts a consolidated report to the chatroom.

#### RECENT agent (single agent, 6 sources):
1. **Web/social** — last30days skill (Reddit, HN, Polymarket) + WebSearch
2. **Newsletters** — `label:"auto/subscriptions & education"` (last 7 days) + `label:"auto/industry research"` (last 14 days). Covers all newsletters Kay subscribes to (Axios, HBR, Girdley, Sweaty Startup, Acquiring Minds, Buy Then Build, etc.) — pull the whole bucket, not per-publisher subject queries.
3. **Granola calls** — meeting transcripts from last 2 weeks
4. **Gmail deal flow** — `label:"auto/deal flow"` (last 14 days) + `label:"auto/investors"` (last 14 days). Broker teasers, CIMs, intermediary inbound, investor portfolio news, searcher cohort signal.
5. **Vault research** — brain/outputs/ and brain/calls/ from last 2 weeks
6. **Passive signals** — brain/inbox/ items tagged `topic/niche-signal` since last Tuesday

#### HISTORICAL orchestrator (spawns 4 parallel sub-agents):
| Sub-Agent | Source |
|-----------|--------|
| `hist-calls` | Fireflies (42 calls in brain/calls/) + Granola (all meetings beyond 14-day window) |
| `hist-email` | Gmail full history — brokers, operators, investors, intermediaries (older_than:14d) |
| `hist-onenote` | OneNote SEARCH FUND notebook — all 16 sections via MCP |
| `hist-chatgpt` | 16 ChatGPT conversations at ~/Downloads/031aafe3.../selected_business_conversations.json |

The HISTORICAL orchestrator:
1. Spawns all 4 sub-agents in parallel
2. Waits for all to complete
3. Cross-references findings (same niche from multiple sources = strong signal)
4. Posts consolidated report to chatroom

### Step 1b: Pattern Recognition & Synthesis

| Agent Name | Type | Description |
|------------|------|-------------|
| `niche-intel-synthesizer` | general-purpose | Cross-source pattern recognition, company extraction, contact mapping, lead lifecycle tracking |

**This agent runs AFTER both gathering tracks post to the chatroom and BEFORE the identifier agent.** It transforms raw intelligence into structured patterns.

**The synthesizer produces 5 outputs:**

1. **Cross-Source Signal Matrix** — Which niches appeared in which sources (RECENT vs HISTORICAL sub-agents). 2+ sources = STRONG, 3+ = VERY STRONG.

2. **Named Company Registry** — Every company mentioned across ALL sources, deduplicated, cross-referenced against Attio CRM and vault history. Each company gets an outreach routing flag: `ACTIVE_DEAL` (already being worked), `IN_CRM` (exists but not active), `WARM_INTRO` (Kay has a contact who can introduce), `VAULT_HISTORY` (mentioned in prior calls/outputs), or `NEW_TARGET` (eligible for cold outreach). Prevents cold-emailing someone Kay already knows.

3. **Contact-to-Niche Map** — Every person mentioned who could be a river guide, mapped to which niches they can help with and relationship warmth (met / emailed / referred / cold).

4. **Lead Lifecycle Tracker** — For every niche or strategy surfaced, track: who proposed it, when, who challenged/rejected it, outcome (live / dead / tabled). Prevents dead ideas from being resurfaced as live recommendations.

5. **Convergence Report** — Top 3-5 strongest signals ranked by: number of independent sources, named companies available, contacts available, alignment with buy box. This is what the Identifier agent reads first.

**Why this exists:** Pattern recognition is what separates good PE professionals from great ones. The same industry appearing in an operator call, a broker email, and a conference attendee list is a signal that no single source would reveal. The synthesizer is the "connect the dots" agent.

### Step 2: Identification + Industry Validation (FUSED)

| Agent Name | Type | Description |
|------------|------|-------------|
| `niche-intel-identifier` | general-purpose | Identify 1-5 new niches AND validate industry fundamentals for each |

**CRITICAL: The buy box is for evaluating COMPANIES, not INDUSTRIES. Do NOT apply company-level criteria (revenue range, EBITDA threshold, customer concentration) to niche evaluation.**

**Niche-level evaluation has two layers:**

**INITIAL SCREEN (pass/fail — must pass all 4 to proceed):**
1. **Margins** — Do companies in this industry typically have 15%+ EBITDA margins?
2. **Recurring / Reoccurring Revenue** — Is there existing recurring/contractual revenue, reoccurring/repeat revenue behavior, or a clear path to convert?
3. **Industry Growth** — Is the market growing above GDP?
4. **Growth TAM** — Is the total addressable market $500M+? (Investor floor — below $500M is a red flag)

**Kay calibration (2026-06-07):** recurring revenue, reoccurring/repeat revenue patterns, cohort/customer durability, and service criticality are the most important positive signals. The industry screen should elevate niches where customers repeat, renew, retain, or depend on the service even if individual company listings often fall below the old `$3M+` preference. Retail and restaurants remain hard-no categories. Do not apply company-level EBITDA thresholds as industry-level rejection gates.

**INDUSTRY SCORECARD (reference for ranking — does NOT gate decisions):**
- Full 7-category weighted evaluation (Growth, Size, Economics, Criticality, Risks, Porter's, Value Creation, Impact)

**TARGET TAM (informational — NOT scored, NOT in scorecard):**
- How many independently owned companies exist that could be acquisition candidates?
- Reported as an informational column on the Industry Research Tracker (like QSBS)
- Determines sprint duration: 50+ = long sprint, 20-50 = focused sprint, 10-20 = fast sprint, <10 = very fast
- Per investor feedback: target count determines how long you spend in an industry, not whether to enter it

**The identifier agent must, for each candidate niche:**
1. Identify the niche from gathered signals
2. Research industry margins and revenue model
3. Research market size and growth rate
4. Estimate how many independently owned firms exist (web search, association directories, industry databases)
5. Check PE consolidation activity (is the window closing?)

**Output per niche candidate (required — no exceptions):**
```
Niche: {name}
Thesis: {2-3 sentences}

QUICK SCREEN:
- Margins: {Strong/Moderate/Weak} — {typical industry margins}
- Recurring / Reoccurring Revenue: {High/Moderate/Low} — {contractual revenue, repeat purchasing, renewal/cohort durability, or conversion path}
- Industry Growth: {Strong/Moderate/Weak} — {CAGR}%, {key drivers}

TARGET TAM:
- Total firms in market: {n}
- Independently owned (potential targets): {n}
- Already PE-backed/acquired: {n}
- PE consolidation risk: High/Medium/Low
- Named examples: {top 5 with company name, location}

MARKET TAM:
- Market size: ${n} (year)
- Growth rate: {n}% CAGR
- Key demand drivers: {list}
```

**No automated rejection.** All niches proceed through the full pipeline. The data is for Kay's decision, not a gate. Flag thin target pools clearly but do NOT auto-kill or auto-table. Kay makes all niche decisions. Company-level constraints such as `$750K-$3M` review band, `$3M+` preferred EBITDA, and `<$750K` lower bound belong to deal/company screening; for niche evaluation they inform target availability and sourcing strategy, not automatic industry rejection.

### Step 3: One-Pager Creation

| Agent Name | Type | Description |
|------------|------|-------------|
| `niche-intel-onepager` | general-purpose | Create pptx one-pager (one per niche, parallel) |

### Step 4: Industry Scoring (NOT the company scorecard)

| Agent Name | Type | Description |
|------------|------|-------------|
| `niche-intel-scorer` | general-purpose | Score each niche using G&B **INDUSTRY** scorecard |

**CRITICAL: This is the INDUSTRY scorecard (7 categories: Growth & Catalyst, Size & Fragmentation, Industry Economics, Mission Criticality, Exogenous Risks, Porter's Forces, Value Creation, Impact). NOT the company scorecard (which evaluates a specific deal in deal-evaluation Phase 4). These are different tools for different purposes.**

The industry scorecard is for Kay's reference when ranking niches. It does NOT gate decisions — Kay decides what to advance, table, or kill.

### Step 4b: REMOVED — Target validation now fused into Step 2

Target validation was moved into the identification step (Step 2) so no niche is ever named without a target count and market TAM attached. This prevents wasted effort building one-pagers and scorecards for niches with empty target pools.

**History:** Trust Administration scored 2.88 (highest) but had almost no acquirable targets. IPLC had only 20-30 firms with half PE-acquired. This lesson drove the fusion.

### Step 5: Tracker Update

| Agent Name | Type | Description |
|------------|------|-------------|
| `niche-intel-tracker` | general-purpose | Update IDEATION + WEEKLY REVIEW tabs |

### Step 5b: SUNSET 2026-04-20 — Validation Contacts moved to river-guide-builder

Previously this step produced `brain/outputs/{date}-validation-contacts-{niche-slug}.md` identifying people who could validate a niche's risks. **Retired 2026-04-20** because (a) Kay's feedback: "no one was answering" the validation outreach, and (b) the output schema overlapped ~90% with river-guide-builder's River Guides output.

**New home:** `river-guide-builder` Phase 1 Category 6 ("Validation Contacts") — lifted concept, same discovery logic, merged into the unified Niche Network output on each target-list sheet. See `.agents/skills/river-guide-builder/SKILL.md`.

**Existing validation-contact outputs in `brain/outputs/2026-03-30-*` and `2026-04-19-*`** remain in place with `supersedes` frontmatter notes (historical record).

</sub_agents>

<reference_index>

## References

| File | Purpose |
|------|---------|
| `scorecard-structure.md` | G&B Industry & Company scorecard criteria, weights, scoring bands |
| `one-pager-template.md` | Template sections, Drive folder IDs, naming conventions |
| `tracker-access.md` | Sheet ID, tab columns, GOG commands for read/write |
| `sub-agents.md` | Complete prompt templates for all sub-agents |

</reference_index>

<workflows_index>

## Workflows

| Workflow | Purpose |
|----------|---------|
| `friday-pipeline.md` | Full 5-step orchestration with verification gates |

</workflows_index>

<niche_sprint_tracking>

## Niche Sprint Status Tracking (Moved from pipeline-manager)

This section monitors the WEEKLY REVIEW tab for status changes and executes transitions. It runs daily because Kay can change niche statuses from Good Morning decisions, decision review, or direct discussion at any time.

### Reading the Tracker

```bash
source scripts/op-env.sh
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "WEEKLY REVIEW" -a kay.s@greenwichandbarrow.com -j
```

Orange headers on WEEKLY REVIEW mark agent-trigger columns:
- **Current Status** — Active - Outreach, Active - Long Term, Under Review, etc.
- **Outreach Channel** — DealsX Email, Kay Email, Cold Call Only

When Kay sets values in these columns, agents act. But a "done" niche should NOT re-trigger work every Tuesday — that defeats the purpose of consolidation.

### SKIP LOGIC (runs BEFORE Detection Logic)

For each WEEKLY REVIEW row, skip the niche entirely if ALL four conditions are true:

1. **Current Status** = `Active - Outreach` or `Active - Long Term`
2. **Outreach Channel** = `DealsX Email`
3. **One-pager exists** — check Drive folder `ACTIVE SPRINTS / {Niche Name}` for a `.pptx` file
4. **Scorecard exists** — check same folder for a `.xlsx` file

If all four true → **SKIP**. Do not regenerate, re-score, or surface. Sam (DealsX) handles execution; Kay has no work here. The only trigger that brings this niche back into Kay's view is Sam surfacing specific targets post-May 6 — which routes through a different flow (target-review, not niche-intelligence).

If one-pager or scorecard is missing → niche needs initial work. Run Steps 3 (one-pager) and 4 (scoring) for that niche only.

If Status changes (e.g., Kay moves Active-Outreach → Tabled), the Status Change Handler below fires regardless of skip logic.

### Detection Logic (for rows NOT skipped above)

1. Read all WEEKLY REVIEW rows
2. For each row where Status starts with "Active" (matches Active - Outreach, Active - Long Term):
   - Check LINKT TARGET LISTS folder for a "{Niche} - Target List" sheet
   - If sheet exists with rows dated today → already running, skip
   - If no sheet or no recent rows → trigger target-discovery
3. Phase-specific behavior:
   - **Active - Outreach:** Target-discovery at full 4-6 targets/day with full outreach cadence.
   - **Active - Long Term:** Continue existing outreach sequences, no NEW targets.

### New Active Sprint Detection

**Active - Outreach detected:**
- Write to niche-sprint-status artifact: "New active sprint: {Niche Name} (Active - Outreach)"
- Target-discovery runs at full pace (4-6/day, Mon-Fri)
- Outreach-manager cadence starts

### Tabled/Killed Processing

When status = "Tabled" or "Killed":

1. Read the niche's full row from WEEKLY REVIEW by header names
2. Append to the target tab:
   - "Tabled" → append to TABLED tab with: Niche Hypothesis, Start Date, "Tabled", Quick notes, Red flags, Score, Why Tabled, What would need to change, Date tabled (today)
   - "Killed" → append to KILLED tab with: Niche Hypothesis, Start Date, "Killed", Quick notes, Red flags, Score, Primary reason, Pattern learned, Date killed (today)
3. Delete the row from WEEKLY REVIEW
4. Move the Drive folder:
   - Tabled: move niche folder to TABLED folder (1_k_c1F11ZNrv4MilATFrURLHdkNx0kRx)
   - Killed: move niche folder to KILLED folder (19xsNk5KTVHF2jb6m_li8IAGjcw34nlMX)
5. Stop target-discovery for that niche

### Status Dropdown Values (`Current Status` orange header)

- New — just added from pipeline, pending analyst review
- Under Review — analyst evaluating
- Active - Outreach — full target discovery with owner outreach cadence
- Active - Long Term — finishing in-flight outreach, no NEW targets but continue existing sequences
- Ideation — deprioritized, stays on WEEKLY REVIEW but sorted to bottom
- Tabled — moves to TABLED tab overnight
- Killed — moves to KILLED tab overnight

Convention: Orange column header = agent-trigger column.

### Sprint Status Artifact

After processing, write a lightweight artifact for pipeline-manager to read:

```
brain/context/niche-sprint-status-{date}.md
```

Contents: list of active niches with their phase (Outreach/Long Term) and any transitions detected. Pipeline-manager reads this for the morning briefing summary line.

### Nightly Audit Stop Hooks

**1. Tabled/Killed Move Validation:**
- Confirm niche row was appended to TABLED/KILLED tab
- Confirm row was removed from WEEKLY REVIEW
- Verify Drive folder was moved to correct status folder
- Verify target-discovery stopped for this niche

**2. Sort Validation:**
- Confirm sort order: Active - Outreach > Active - Long Term > Under Review > New > Ideation
- Confirm no data lost (row count before = row count after)

**3. Target List Template Validation (new Active sprints):**
- Active - Outreach: target list sheet exists, outreach cadence running
- Verify the `Kay Decision` orange header exists in target list sheets

**4. Kay Decision Column Validation (all active target lists):**
- Check for rows where `Kay Decision` = "Pass" not yet moved to Passed tab → move them
- Check for rows where `Kay Decision` = "Approve" not yet in Attio → flag for outreach-manager

</niche_sprint_tracking>

<success_criteria>

Niche Intelligence run is complete when:
- [ ] Both gathering agents (RECENT + HISTORICAL) posted to chatroom
- [ ] 1-5 new niches identified (or 0 with documented reasoning)
- [ ] One-pager .pptx created and uploaded for each new niche
- [ ] One-pager includes a Sources section citing every source used (external URLs, vault paths, chatroom traces, CRM pulls), each with a live hyperlink per `feedback_onepager_must_cite_sources`
- [ ] Each niche scored against detailed G&B scorecard
- [ ] Output report written to `brain/outputs/{date}-niche-intelligence-report.md`
- [ ] IDEATION tab updated with new niches + scores
- [ ] High-scoring niches promoted to WEEKLY REVIEW if warranted
- [ ] User notified that Niche Intelligence is complete
- [ ] For niches flagged for sprint activation: validation contacts page generated with 5+ contacts and key risks

</success_criteria>

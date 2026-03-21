---
name: niche-intelligence
description: "Niche Intelligence workflow. Gathers data from newsletters, web, calls, email, and research — identifies new niches — runs initial screen (margins, recurring revenue, growth, Growth TAM) — creates one-pagers — scores against G&B industry scorecard — updates Industry Research Tracker. Run every Tuesday night (ready Wednesday AM for analyst meeting) by 1pm EST."
user-invocable: true
---

<essential_principles>

## Architecture: 5-Step Pipeline with Parallel Sub-Agents

This skill implements a **sequential pipeline** where each step depends on the previous step's output. Within steps, sub-agents run in **parallel** where possible.

```
Step 1: GATHER (parallel)      → raw intelligence
Step 2: IDENTIFY (sequential)  → new niche candidates
Step 3: ONE-PAGER (parallel)   → pptx deliverables
Step 4: SCORE (sequential)     → scored niches + final report
Step 4b: VALIDATE (parallel)   → buy-box target count (gate before promotion)
Step 5: UPDATE (sequential)    → tracker updated + notification
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
| Granola MCP | Meeting transcript retrieval |
| OneNote MCP | SEARCH FUND notebook — industry memos, deal convos, research notes |
| `python-pptx` | One-pager generation |
| `WebSearch` | Supplemental research for scoring |

### Schedule

**Runs Tuesday night (automated).** Claude posts the Niche Intel Report link to #operations by 10am Wednesday for the analyst call. Kay reviews the report live on the call, not beforehand.

</essential_principles>

<intake>

When `/niche-intelligence` is invoked:

1. Read `references/tracker-access.md` for current tracker state
2. Read `brain/context/learnings.md` for evaluation context
3. Create chatroom at `brain/traces/agents/{date}-niche-intelligence.md`
4. Execute the pipeline: `workflows/friday-pipeline.md`

No intake question needed — this is a fully automated workflow.

</intake>

<routing>

| Trigger | Workflow |
|---------|----------|
| `/niche-intelligence` | `workflows/friday-pipeline.md` |
| `/niche-intelligence --step 1` | Run only Step 1 (gathering) |
| `/niche-intelligence --step 2` | Run Steps 1-2 (gather + identify) |
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
2. **Newsletters** — Axios + Axios Pro Rata from Gmail (last 7 days)
3. **Granola calls** — meeting transcripts from last 2 weeks
4. **Gmail deal flow** — broker teasers, CIMs, investor emails (last 14 days)
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

### Step 2: Identification + Industry Validation (FUSED)

| Agent Name | Type | Description |
|------------|------|-------------|
| `niche-intel-identifier` | general-purpose | Identify 1-5 new niches AND validate industry fundamentals for each |

**CRITICAL: The buy box is for evaluating COMPANIES, not INDUSTRIES. Do NOT apply company-level criteria (revenue range, EBITDA threshold, customer concentration) to niche evaluation.**

**Niche-level evaluation has two layers:**

**INITIAL SCREEN (pass/fail — must pass all 4 to proceed):**
1. **Margins** — Do companies in this industry typically have 15%+ EBITDA margins?
2. **Recurring Revenue** — Is there existing recurring/contractual revenue, or a clear path to convert?
3. **Industry Growth** — Is the market growing above GDP?
4. **Growth TAM** — Is the total addressable market $500M+? (Investor floor — below $500M is a red flag)

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
- Recurring Revenue: {High/Moderate/Low} — {revenue model description}
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

**No automated rejection.** All niches proceed through the full pipeline. The data is for Kay's decision, not a gate. Flag thin target pools clearly but do NOT auto-kill or auto-table. Kay makes all niche decisions.

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

<success_criteria>

Niche Intelligence run is complete when:
- [ ] Both gathering agents (RECENT + HISTORICAL) posted to chatroom
- [ ] 1-5 new niches identified (or 0 with documented reasoning)
- [ ] One-pager .pptx created and uploaded for each new niche
- [ ] Each niche scored against detailed G&B scorecard
- [ ] Output report written to `brain/outputs/{date}-niche-intelligence-report.md`
- [ ] IDEATION tab updated with new niches + scores
- [ ] High-scoring niches promoted to WEEKLY REVIEW if warranted
- [ ] User notified that Niche Intelligence is complete

</success_criteria>

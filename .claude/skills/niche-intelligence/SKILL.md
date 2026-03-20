---
name: niche-intelligence
description: "Niche Intelligence workflow. Gathers data from newsletters, web, calls, email, and research — identifies new niches — creates one-pagers — scores against G&B scorecard — updates Industry Research Tracker. Run every Tuesday night (ready Wednesday AM for analyst meeting) by 1pm EST."
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
- **Step 1:** Chatroom has posts from all gathering agents
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

### Step 1: Gathering (all run in parallel)

| Agent Name | Type | Description |
|------------|------|-------------|
| `niche-intel-news` | general-purpose | Web/social research via last30days skill |
| `niche-intel-newsletters` | general-purpose | Scan Axios + Axios Pro Rata from Gmail |
| `niche-intel-calls` | general-purpose | Pull niche-related meeting notes from Granola |
| `niche-intel-email` | general-purpose | Scan Gmail for deal flow / niche signals |
| `niche-intel-research` | general-purpose | Read recent brain/outputs/ research files |
| `niche-intel-passive-signals` | general-purpose | Pull queued niche signals from pipeline-manager |

#### Passive Signal Intake (niche-intel-passive-signals)

Pipeline-manager flags niche signals daily while processing Granola and Gmail. These accumulate in `brain/inbox/` tagged `topic/niche-signal` throughout the week.

**This agent:**
1. Glob for `brain/inbox/*niche-signal*` files created since last Tuesday
2. Read each signal: what was said, who said it, source, buy box alignment
3. Look for patterns: did multiple signals point to the same industry?
4. Cluster related signals into candidate niches
5. Post findings to chatroom alongside other gathering agents

**Pattern recognition priorities:**
- Same industry mentioned by 2+ unrelated sources = strong signal
- Broker mentioning deal flow in an industry = strong signal
- Single offhand mention = weak signal (include but don't weight heavily)
- Signal aligns with buy box characteristics (regulatory, recurring, fragmented) = boost

After niche-intelligence processes the signals, mark the inbox files as `status: processed` so they don't get re-scanned next week.

### Step 2: Identification + Target Validation (FUSED)

| Agent Name | Type | Description |
|------------|------|-------------|
| `niche-intel-identifier` | general-purpose | Identify 1-5 new niches AND validate target pool for each |

**CRITICAL: No niche gets named without answering the two investor questions:**

1. **Target TAM:** How many real, acquirable companies exist that fit the buy box? (Not total firms — specifically independently owned, $2-5M+ EBITDA, 10+ employees, 10+ year history, not PE-backed, owner-operator)
2. **Market TAM:** What is the total addressable market size for this niche? (Revenue of the industry segment, growth rate, what drives demand)

**The identifier agent must, for each candidate niche:**
1. Identify the niche from gathered signals
2. Immediately research target count (web search, association directories, industry databases, Linkt profile flow)
3. Research market size (industry reports, analyst estimates)
4. Filter targets for buy-box fit
5. Check PE consolidation activity (how many already acquired?)

**Output per niche candidate (required — no exceptions):**
```
Niche: {name}
Thesis: {2-3 sentences}

TARGET TAM:
- Total firms in market: {n}
- Firms fitting buy box: {n}
- Already PE-backed/acquired: {n}
- Net acquirable targets: {n}
- Named examples: {top 5 with company name, revenue, employees, location}
- PE consolidation risk: High/Medium/Low

MARKET TAM:
- Market size: ${n} (year)
- Growth rate: {n}% CAGR
- Key demand drivers: {list}

Verdict: Sufficient (20+ targets) / Thin (10-20) / Insufficient (<10)
```

**Gate rule:** Niches with <10 net acquirable targets are flagged "Thin Target Pool." Niches with <5 are rejected outright (Kay can override). This gate runs BEFORE one-pagers or scoring — no wasted effort on empty pools.

### Step 3: One-Pager Creation

| Agent Name | Type | Description |
|------------|------|-------------|
| `niche-intel-onepager` | general-purpose | Create pptx one-pager (one per niche, parallel) |

### Step 4: Scoring

| Agent Name | Type | Description |
|------------|------|-------------|
| `niche-intel-scorer` | general-purpose | Score each niche using G&B detailed scorecard |

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
- [ ] All 5 gathering agents posted to chatroom
- [ ] 1-5 new niches identified (or 0 with documented reasoning)
- [ ] One-pager .pptx created and uploaded for each new niche
- [ ] Each niche scored against detailed G&B scorecard
- [ ] Output report written to `brain/outputs/{date}-niche-intelligence-report.md`
- [ ] IDEATION tab updated with new niches + scores
- [ ] High-scoring niches promoted to WEEKLY REVIEW if warranted
- [ ] User notified that Niche Intelligence is complete

</success_criteria>

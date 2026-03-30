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
Step 1b: SYNTHESIZE (sequential) → cross-source pattern recognition
Step 2: IDENTIFY (sequential)  → new niche candidates
Step 3: ONE-PAGER (parallel)   → pptx deliverables
Step 4: SCORE (sequential)     → scored niches + final report
Step 4b: VALIDATE (parallel)   → buy-box target count (gate before promotion)
Step 5: UPDATE (sequential)    → tracker updated + notification
Step 5b: CUSTOMER CALL LIST (parallel) → validation call targets for JJ
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
- **Step 5b:** Customer call list doc created in Drive for any niche flagged for activation

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

<niche_inbox>

## Niche Inbox: How New Niche Ideas Enter the Pipeline

Niche ideas come from many places — not just the Tuesday night gathering agents. The pipeline must accept ideas from ANY source and route them through the full process (Identify → One-Pager → Score → Add to tracker). **Nothing skips steps. Nothing goes straight to WEEKLY REVIEW without a one-pager and score.**

### Sources that feed niche ideas into the pipeline:

| Source | How it arrives | Entry point |
|--------|---------------|-------------|
| Tuesday night gathering agents (RECENT + HISTORICAL) | Automated Step 1 run | Step 1b (Synthesize) → Step 2 (Identify) |
| Kay + Claude conversations | Kay mentions a niche idea, contact shares a list, brainstorming session | Written to `brain/inbox/` as niche signal → picked up at Step 2 |
| OneNote research notes | Kay's handwritten notes reference industries (e.g., Mike Horowitz's insurance back-end list) | Written to `brain/inbox/` as niche signal → picked up at Step 2 |
| Linkt data analysis | Patterns found across old or new Linkt exports (e.g., environmental compliance cluster) | Written to `brain/inbox/` as niche signal → picked up at Step 2 |
| Pipeline-manager | Niche signals detected in Granola calls or Gmail during daily ingestion | Written to `brain/inbox/` as `topic/niche-signal` → picked up at Step 1 (RECENT passive signals) |
| Contact referrals | Investor, operator, or advisor suggests a niche (e.g., Jeremy Black → TCI, Mike Horowitz → insurance back-end) | Written to `brain/inbox/` as niche signal → picked up at Step 2 |
| Conference attendee analysis | Conference-discovery surfaces an industry cluster | Written to `brain/inbox/` as niche signal → picked up at Step 2 |

### Writing a niche idea to the inbox:

When a niche idea surfaces outside of the Tuesday run, write it to:
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

**Option A (queue for Tuesday):** Leave in inbox. The RECENT agent's passive signal source picks up `topic/niche-signal` items automatically during the next Tuesday run.

**Option B (run now):** Invoke `/niche-intelligence --from-inbox` to process all pending niche ideas through Steps 2-5 immediately. Useful for testing or when Kay wants results before the next Tuesday cycle.

### The rule:
**Every niche idea, regardless of source, must go through: Identify → One-Pager → Score → Tracker.** The only question is timing (now vs. Tuesday).

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

### Step 5b: Customer Validation Call List

| Agent Name | Type | Description |
|------------|------|-------------|
| `niche-intel-customer-calls` | general-purpose | Generate customer/expert call list for niche validation |

**Purpose:** Before owner outreach begins on a new niche, JJ makes 5 customer/expert validation calls. These conversations surface red flags that desk research can't catch (e.g., weak demand, price-driven competition, declining relevance). This step generates the call list.

**When this runs:** Only for niches that pass all 4 initial screen gates AND are candidates for sprint activation (scored 2.5+ on industry scorecard or Kay requests activation).

**The agent:**
1. Read the niche one-pager, specifically the **Risks** section and **Mission Criticality** section
2. Generate 5-8 validation questions derived from the one-pager risks. Examples:
   - If risk says "price competition eroding margins" → "What drives your vendor selection — price, quality, relationships, or something else?"
   - If risk says "regulation may change" → "How dependent is your need for this service on current regulations?"
   - If risk says "PE consolidation" → "Have you noticed larger players entering your market? How has that changed the service?"
   - Always include: "How critical is {service} to your operations?" and "If your current provider disappeared, what would you do?"
3. Identify 5-10 potential call targets (customers/experts who USE the niche's service):
   - Search web for companies that are CUSTOMERS of this niche (not competitors)
   - Check industry association member directories for customer-side contacts
   - Search LinkedIn via WebSearch for titles like "VP Operations", "Procurement Director" at companies in the customer vertical
   - For each target: Name, Company, Title, Phone (if findable), LinkedIn URL, why they're relevant
4. Write the call list to Google Drive: `OPERATIONS / CALL LOGS / {Niche} - Customer Validation Calls.docx`
   - Include: niche name, the 5-8 questions, the 5-10 targets with contact info
   - Use the Customer Validation Call Log template (Doc ID: `1gw5qYUpBm6LMa-jtvKeY0rDYTxL9IOWE`, .docx format with G&B letterhead, in OPERATIONS / CALL LOGS)
   - Copy the template for each individual call target, pre-populate niche name and validation questions
5. Write a vault file: `brain/outputs/{date}-customer-validation-calllist-{niche-slug}.md`

**Output posted to chatroom:**
```
CUSTOMER VALIDATION CALL LIST: {Niche Name}
Status: Active - Diligence
Targets: {n} customers/experts identified
Questions: {n} derived from one-pager risks
Doc: {google_doc_link}
```

**Stop hook:** Call list doc exists in Drive AND contains at least 5 targets with at least one contact method each.

**HARD REQUIREMENT — Kay Approval Gate (before JJ receives anything):**

Customer validation call lists MUST be reviewed and approved by Kay before being sent to JJ. This is not optional.

1. After the call list doc is created in Drive, present the Google Doc link(s) to Kay for review.
2. Format the approval request clearly:
   ```
   CUSTOMER VALIDATION CALL LIST — APPROVAL NEEDED

   Niche: {Niche Name}
   Targets: {n} customers/experts
   Questions: {n} validation questions
   Doc: {google_doc_link}

   Please review the call list and approve before it goes to JJ.
   ```
3. Wait for Kay's explicit approval on each list. Do NOT proceed to Slack notification until approved.
4. If Kay requests changes, update the doc and re-present for approval.
5. Only after Kay approves should the list be shared with JJ via Slack.

This gate exists because JJ acts on these lists immediately. Bad targets or bad questions waste JJ's limited call time and can damage relationships. Kay reviews every list.

**After JJ completes 5 calls — Customer Validation Summary:**

Claude synthesizes JJ's 5 call log docs into a one-page **Customer Validation Summary** saved to `OPERATIONS / CALL LOGS / {Niche} - Customer Validation Summary.docx`:

```
CUSTOMER VALIDATION: {Niche Name}
Date: {date}
Calls Completed: 5 of 5

RISK VALIDATION:
1. "{Risk from one-pager}"
   - {n}/5 validated (customer quotes) ✓
   - {n}/5 contradicted (customer quotes) ✗
   - {n}/5 mixed
   → VERDICT: {Low risk / Moderate risk / High risk}

2. "{Next risk}"
   ...

OVERALL SIGNAL: [Strong / Mixed / Weak]
- Strong = 4-5 customers converge on the same answers → ready for Kay's decision
- Mixed = answers split, no clear pattern → recommend 3-5 more calls
- Weak = 4-5 customers raise concerns → recommend table or kill

KEY QUOTES: {2-3 verbatim quotes that capture the signal}

RECOMMENDATION: [Advance to Active-Outreach / More calls needed / Table]
```

Also saved to vault: `brain/outputs/{date}-customer-validation-summary-{niche-slug}.md`

**Decision gate:** Kay and analyst review the summary (typically at Wednesday analyst call). Kay decides: advance to Active-Outreach, request more calls, table, or kill. This is NOT an automatic promotion — Kay always decides.

**JJ's call volume during Active-Diligence:**
- Owner confirmation calls ALWAYS take priority (4-6/day)
- Customer validation calls fill remaining time (~3-4/day on a typical day)
- 5 completed customer conversations = ~2 days of JJ time
- JJ logs each customer call in a Call Log doc ("Customer Validation" variant) with structured answers to each question + overall sentiment

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
- [ ] For niches flagged for sprint activation: customer validation call list generated with 5+ targets

</success_criteria>

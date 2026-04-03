# Workflow: Friday Niche Intelligence Pipeline

<required_reading>
**Read these reference files NOW:**
1. `references/scorecard-structure.md`
2. `references/one-pager-template.md`
3. `references/tracker-access.md`
4. `references/sub-agents.md`
5. `brain/context/learnings.md`
</required_reading>

<process>

## Pre-Flight

1. Create chatroom at `brain/traces/agents/{YYYY-MM-DD}-niche-intelligence.md`
2. Read current tracker state:
   - WEEKLY REVIEW tab (all niches under active consideration — new niches go here directly)
   - KILLED tab (niche names to exclude)
   - TABLED tab (niches that could resurface with new data)
3. Store the killed/tabled/active niche lists — these feed into Step 2

## Step 1: GATHER (7 Parallel Tracks)

Spawn ALL SEVEN gathering agents in a **single message** for parallel execution.

### Sub-Agents to Spawn (parallel)

```
Agent("niche-intel-recent", prompt from references/sub-agents.md §1a)
  → Single agent covering 6 sources from last 14 days:
    web/social, newsletters, Granola calls, Gmail, vault research, passive signals

Agent("niche-intel-historical", prompt from references/sub-agents.md §1b)
  → Orchestrator that spawns 4 sub-agents in parallel:
    hist-calls (Fireflies + older Granola)
    hist-email (Gmail full history)
    hist-onenote (OneNote SEARCH FUND notebook)
    hist-chatgpt (ChatGPT conversations)
  → Collects, cross-references, and posts consolidated report

Agent("niche-intel-pe-trends", general-purpose)
  → PE trend scan: what industries are PE firms and search funds actively acquiring?
  → Uses WebSearch for:
    - "private equity lower middle market acquisition trends {current_year} services businesses"
    - "PE platform acquisitions fragmented industries roll-up {current_year}"
    - "search fund acquisitions {current_year} which industries"
    - "PE acquisitions {niche}" for each Active-Outreach and Under Review niche
  → Posts to chatroom:
    - Which industries PE is consolidating (with deal examples)
    - PE entry signals for niches Kay is watching (move faster or walk away)
    - New fragmented industries appearing in PE deal flow that match G&B buy box
    - Overlap alert: if PE saturation is high (>50% PE-driven deal volume), flag it

Agent("niche-intel-sba-heatmap", general-purpose)
  → SBA loan data mining: which industries have the most independently-owned businesses?
  → Process:
    1. Download SBA 7(a) FOIA dataset from data.sba.gov (FY2020-present CSV)
    2. Filter: most recent 2 fiscal years, loan amount $500K-$5M
    3. Filter to B2B services NAICS sectors (52-56, 61-62, 81)
    4. Group by 6-digit NAICS code, count loans, sum amounts
    5. Rank by loan count (high count = fragmented industry with many independents)
    6. Cross-reference top 30 against KILLED/TABLED niches (exclude known rejects)
    7. Cross-reference against current Active-Outreach niches (validate existing bets)
  → Posts to chatroom:
    - Top 20 NAICS codes by loan density with descriptions
    - Any NEW industries not previously considered (flag for Step 2)
    - Validation signals for current niches (e.g., "insurance agencies: 362 loans confirms thesis")
    - Industries where loan density is growing vs shrinking (compare FY2024 vs FY2025)

Agent("niche-intel-associations", general-purpose)
  → Trade association mining: discover niches through organized industry groups
  → Process:
    1. WebSearch ASAE Gateway to Associations directory for B2B services categories
    2. WebSearch for trade association directories in sectors matching G&B buy box:
       - "trade association" + "B2B services" / "professional services" / "compliance"
       - "industry association directory" + "small business" / "independent operators"
    3. For each association found, extract: industry served, member count (if available), 
       whether members are mostly independent/small businesses
    4. Cross-reference against KILLED/TABLED/IDEATION niches (skip known)
    5. Flag associations with 500+ members (indicates fragmented industry)
  → Posts to chatroom:
    - New associations discovered with member counts and industry descriptions
    - Associations that serve industries not on any tracker tab (true new signals)
    - Member directories that could feed target-discovery (direct target pool source)

Agent("niche-intel-regulation", general-purpose)
  → Regulation change scanning: new compliance requirements that create service demand
  → Process:
    1. WebSearch Wolters Kluwer regulatory compliance developments {current_year}
    2. WebSearch Paychex top regulatory issues {current_year}
    3. WebSearch "new regulation {current_year}" + "compliance requirements" + "small business"
    4. WebSearch Federal Register recent final rules affecting small businesses
    5. For each new regulation, identify: who must comply, what service they need to comply,
       whether independent service providers exist in that compliance space
  → Posts to chatroom:
    - New regulations creating compliance service demand
    - Existing regulations being tightened (expanded scope = expanded market)
    - Match to G&B compliance infrastructure thesis
    - Specific service categories spawned by each regulation

Agent("niche-intel-franchise-signal", general-purpose)
  → Franchise-as-niche-signal: identify industries where franchises prove the model is repeatable
  → Process:
    1. WebSearch FDD Exchange for B2B services franchise categories
    2. WebSearch "B2B services franchise" / "commercial services franchise" / "compliance franchise"
    3. For each franchise category found, identify:
       - The franchise model (what service they provide)
       - Number of franchise units (indicates market size)
       - Non-franchise independent competitors (the acquisition target pool)
    4. Filter: B2B only, not restaurants/retail/consumer
    5. Cross-reference against existing niches on tracker
  → Posts to chatroom:
    - Franchise categories with 100+ units (proven, repeatable model)
    - The non-franchise independent competitors in each category (target pool)
    - Any franchise categories serving luxury/HNW clients (G&B thesis overlap)
```

Each track posts a structured summary to the chatroom with:
- Source identifier and time horizon
- Key signals found (with relevance to M&A, PE activity, niche opportunities)
- Specific industries or companies mentioned
- Any data points useful for scoring (market size, growth rates, margins, etc.)
- Cross-source signals (same niche from multiple sources = strong signal)
- PE activity level (from PE trends track): none / early / active / saturated
- SBA density (from SBA heatmap track): loan count in G&B's size range

### Verification Gate 1

After all seven agents complete, read the chatroom. Verify:
- [ ] RECENT agent posted findings
- [ ] HISTORICAL agent posted consolidated findings (from all 4 sub-agents)
- [ ] PE TRENDS agent posted industry consolidation signals
- [ ] SBA HEATMAP agent posted NAICS density rankings
- [ ] ASSOCIATIONS agent posted new association discoveries
- [ ] REGULATION agent posted new compliance requirements
- [ ] FRANCHISE SIGNAL agent posted franchise category analysis

If any agent failed, log a warning but continue — Step 1b can work with partial input.

## Step 1b: SYNTHESIZE (Sequential — Pattern Recognition)

Spawn `niche-intel-synthesizer` agent AFTER all gathering agents complete.

This agent reads all chatroom posts (RECENT, HISTORICAL, PE TRENDS, SBA HEATMAP, ASSOCIATIONS, REGULATION, FRANCHISE SIGNAL) and produces 5 structured outputs:
1. **Cross-Source Signal Matrix** — which niches appeared in which sources, with strength ratings. A niche appearing in SBA data + association directory + PE trends = VERY STRONG signal.
2. **Named Company Registry** — every company mentioned, deduplicated, with independence status
3. **Contact-to-Niche Map** — every person who could help, mapped to niches and relationship warmth
4. **Lead Lifecycle Tracker** — proposed → challenged → outcome for every lead (prevents dead ideas from resurfacing)
5. **Convergence Report** — top 5 signals ranked by source count, named companies, contacts, buy box fit, and actionability

**Why this step exists:** Pattern recognition is what separates good PE professionals from great ones. The same industry appearing in an operator call, a broker email, and a conference attendee list is a signal no single source would reveal.

### Verification Gate 1b

- [ ] Synthesizer posted all 5 outputs to chatroom
- [ ] Lead Lifecycle Tracker flags any dead/killed leads

## Step 2: IDENTIFY + VALIDATE (Sequential — fused)

Spawn `niche-intel-identifier` agent with:
- The synthesizer's 5 outputs (NOT raw gathering posts — the synthesis is the input)
- The killed/tabled/active niche lists from pre-flight
- `brain/context/learnings.md` as evaluation context
- Buy box criteria and thesis context

This agent:
1. Synthesizes all Step 1 data
2. Identifies 1-5 niche candidates NOT already in the tracker (killed, tabled, ideation, or active)
3. **For each candidate, IMMEDIATELY validates target pool and market TAM** (web search, association directories, Linkt profile flow)
4. Checks if any tabled niches should resurface based on new data
5. Posts list to chatroom with full TAM data

**CRITICAL — Every niche must include (no exceptions):**
- **Target TAM:** Total firms → buy-box fit → PE-acquired → net acquirable targets + 5 named examples
- **Market TAM:** Market size ($), growth rate (CAGR%), key demand drivers
- **Verdict:** Sufficient (20+ targets) / Thin (10-20) / Insufficient (<10)

**Gate rule:** Niches with <10 net acquirable targets are flagged "Thin Target Pool." Niches with <5 are rejected — do NOT proceed to one-pager. Kay can override.

**Output:** A list of validated niches with target counts and market TAM. Only niches passing the gate proceed to Step 3.

If 0 new niches identified (or all fail the gate), document why and skip Steps 3-4. Proceed to Step 5 with status update only.

## Step 3: ONE-PAGER (Parallel per Niche)

For each niche from Step 2, spawn a `niche-intel-onepager` agent. If 3 niches identified, spawn 3 agents in parallel.

Each agent:
1. Checks if a one-pager already exists (pre-flight check in Drive + brain/outputs/)
2. Performs web research to fill all one-pager sections (Industry Overview, Thesis, Trends, Economics, Competition, Customers, Barriers, Key Success Factors, Exit)
3. Does NOT score or rate the niche — Assessment/Status is left as "Pending Scoring"
4. Uses `python-pptx` to create the pptx file following the template structure
5. Creates a Drive folder for the niche under WEEKLY REVIEW subfolder (`1eq7FjekjFhkV0RoBfgr9n6AXPtENEenT`)
6. Uploads the pptx to the new folder
7. Posts folder ID and file confirmation to chatroom

### Verification Gate 3 (STOP — must pass before Step 4)

After ALL one-pager agents complete, the orchestrator MUST verify each niche before proceeding:

For each niche:
1. Confirm .pptx file exists locally (`ls /tmp/{niche-slug}-onepager.pptx`)
2. Confirm Drive folder was created in WEEKLY REVIEW subfolder:
   `gog drive ls -a kay.s@greenwichandbarrow.com --parent 1eq7FjekjFhkV0RoBfgr9n6AXPtENEenT -j`
3. Confirm exactly ONE file exists in each new folder (no duplicates):
   `gog drive ls -a kay.s@greenwichandbarrow.com --parent {folder_id} -j`
4. Confirm Assessment/Status says "Pending Scoring" (no scores leaked into one-pager)

**If any niche fails:** Log the error in the chatroom, exclude that niche from Steps 4-5, and continue with passing niches.
**If ALL niches fail:** Stop pipeline, post error summary to chatroom, notify user.

## Step 4: ADD TO TRACKER (Sequential)

Spawn `niche-intel-tracker` agent to add new niches directly to WEEKLY REVIEW tab BEFORE scoring.

This agent:
1. Appends each new niche to WEEKLY REVIEW tab with columns populated (Score left blank, notes = "Pending scoring")
2. Posts confirmation of all sheet updates to chatroom

### Verification Gate 4 (STOP — must pass before Step 5)

After tracker update completes, verify:
1. Re-read WEEKLY REVIEW tab: `gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "WEEKLY REVIEW!A:I" -a kay.s@greenwichandbarrow.com -j`
2. Confirm each new niche appears as a row
3. Confirm Score column is blank or "Pending"

**If verification fails:** Retry the append once. If still fails, log error and continue to Step 5 (scorer can add rows itself as fallback).

## Step 5: SCORE (Sequential)

Spawn `niche-intel-scorer` agent with:
- All gathered intelligence from Step 1
- Niche list and one-pager content from Steps 2-3
- Scorecard structure from `references/scorecard-structure.md`
- `brain/context/learnings.md` for qualitative judgment

This agent:
1. For each niche, evaluates against the **detailed scorecard** (TEMPLATE tab structure — 7 categories, 20+ sub-criteria)
2. Performs additional web research where data gaps exist
3. Computes weighted scores
4. Normalizes to /3 scale for WEEKLY REVIEW tab compatibility
5. Also fills in WEEKLY REVIEW-specific columns: Margins, Recurring Revenue, AI Defensibility, Right to Win, Network Access
6. **Creates per-niche scorecard xlsx** — copies template from `brain/library/internal/scorecard/G&B Industry & Company Scorecard Template.xlsx`, fills INITIAL SCREEN + Industry Scorecard tabs with scored data using `openpyxl`, uploads to the niche's Drive folder (same folder as the one-pager)
7. Writes the final output report to `brain/outputs/{date}-niche-intelligence-report.md`
8. **Updates one-pagers** with final scores (downloads pptx, updates Assessment/Status, re-uploads)
9. **Updates tracker** with scores (writes score + WEEKLY REVIEW columns to the rows added in Step 4)

### Output Report Structure

```markdown
---
schema_version: 1.1.0
date: {YYYY-MM-DD}
type: research
status: draft
people: ["[[entities/kay-schneider]]"]
companies: ["[[entities/greenwich-and-barrow]]"]
projects: []
tags:
  - date/{YYYY-MM-DD}
  - output
  - output/research
  - status/draft
  - person/kay-schneider
  - company/greenwich-and-barrow
  - topic/niche-intelligence
  - topic/search-fund
---

# Friday Niche Intelligence Report — {date}

## Executive Summary
{2-3 sentences: how many niches identified, top signal, recommended actions}

## Data Sources This Week
| Track | Sources Covered | Key Signals |
|-------|----------------|-------------|
| RECENT (last 14 days) | Web/social, newsletters, Granola calls, Gmail, vault research, passive signals | {summary} |
| HISTORICAL (full search) | Fireflies calls, older Granola, Gmail full history, OneNote SEARCH FUND, ChatGPT conversations | {summary} |

## New Niches Identified

### {Niche 1 Name} — Score: {X.XX}/3
**Thesis:** {2-3 sentences}
**Detailed Scorecard:**
| Category | Score | Weight | Notes |
|----------|-------|--------|-------|
| Growth & Catalyst | {1-3} | 25% | {brief} |
| Size & Fragmentation | {1-3} | 10% | {brief} |
| Industry Economics | {1-3} | 10% | {brief} |
| Mission Criticality | {1-3} | 15% | {brief} |
| Exogenous Risks | {1-3} | 10% | {brief} |
| Porter's Forces | {1-3} | 15% | {brief} |
| Value Creation | {1-3} | 10% | {brief} |
| Impact | {1-3} | 5% | {brief} |
**WEEKLY REVIEW Columns:** Margins={}, Recurring={}, AI Defensibility={}, Right to Win={}, Network Access={}
**One-Pager:** [Drive link]
**Scorecard xlsx:** [Drive link]
**Recommendation:** Keep in WEEKLY REVIEW / Table / Kill

{Repeat for each niche}

## Tabled Niche Review
{Any tabled niches that should resurface based on new data? If none, state "No tabled niches warrant revisiting this week."}

## Recommended Actions for Monday Review
1. {action}
2. {action}
```

### Verification Gate 5

- [ ] Output report exists at `brain/outputs/{date}-niche-intelligence-report.md`
- [ ] Report has valid vault frontmatter
- [ ] Each niche has a complete scorecard
- [ ] Per-niche scorecard xlsx uploaded to each niche's Drive folder (same folder as one-pager)
- [ ] One-pagers updated with scores on Drive
- [ ] Tracker WEEKLY REVIEW rows updated with scores
- [ ] New niches appear in WEEKLY REVIEW tab with scores populated
- [ ] Each niche Drive folder in WEEKLY REVIEW subfolder (`1eq7FjekjFhkV0RoBfgr9n6AXPtENEenT`) contains both one-pager pptx and scorecard xlsx

## Completion

### Pre-Notification Stop Hook (MUST pass before Slack notification)

**CRITICAL: Slack notification is the LAST thing that happens. Never notify before deliverables are complete.** Kay and her analyst use the notification as a signal that everything is ready to review.

For EACH new niche, verify ALL deliverables exist in its Drive folder:
- [ ] One-pager .pptx uploaded to niche folder in WEEKLY REVIEW
- [ ] Scorecard .xlsx uploaded to SAME niche folder in WEEKLY REVIEW
- [ ] Tracker WEEKLY REVIEW row has score populated (not blank or "Pending")
- [ ] One-pager Assessment/Status updated with final score (not "Pending Scoring")

**Verification command (run for each niche):**
```bash
gog drive ls -a kay.s@greenwichandbarrow.com --parent {niche_folder_id} -p
# Must show exactly 2 files: one .pptx and one .xlsx
```

**If ANY niche fails this check:** Fix it before sending notification. Download, re-upload, or re-run the failed step. Do NOT send Slack with incomplete deliverables.

**If ALL niches pass:** Proceed to notification.

## Step 5b: CUSTOMER VALIDATION CALL LISTS (Conditional — Approval Required)

For any niche flagged for sprint activation (scored 2.5+ or Kay requests), spawn `niche-intel-customer-calls` agent to generate the customer validation call list.

### Kay Approval Gate (HARD REQUIREMENT)

Customer validation call lists MUST be reviewed and approved by Kay before being sent to JJ. This is not optional.

1. After the call list doc is created in Drive, present the Google Doc link(s) to Kay:
   ```
   CUSTOMER VALIDATION CALL LIST — APPROVAL NEEDED

   Niche: {Niche Name}
   Targets: {n} customers/experts
   Questions: {n} validation questions
   Doc: {google_doc_link}

   Please review the call list and approve before it goes to JJ.
   ```
2. Wait for Kay's explicit approval on each list. Do NOT send to JJ until approved.
3. If Kay requests changes, update the doc and re-present for approval.
4. Only after Kay approves should the list be shared with JJ via Slack.

### Verification Gate 5b

- [ ] Call list doc exists in Drive with 5+ targets
- [ ] Kay has explicitly approved the call list
- [ ] Only approved lists are sent to JJ via Slack

---

After all steps complete and stop hooks pass:

1. Read the full chatroom to compile final status
2. Send Slack notification:

```bash
curl -s -X POST "$SLACK_WEBHOOK_STRATEGY_OPS" \
  -H "Content-Type: application/json" \
  -d '{"text":"Niche Intelligence complete — {count} new niches identified.\n{For each: \"• {Niche Name} ({X.XX}/3)\"}\n\nOne-pagers: {count} | Promoted: {count or \"None\"}\nReport: brain/outputs/{date}-niche-intelligence-report.md\n\nReady for analyst call."}'
```

3. Output to user:

```
Friday Niche Intelligence Complete — {date}

Sources scanned: {list of sources that returned data}
New niches identified: {count}
{For each: "- {Niche Name} (Score: {X.XX}/3) — {1-line thesis}"}

One-pagers created: {count} (Drive links in report)
Promoted to Weekly Review: {count or "None"}

Output report: brain/outputs/{date}-niche-intelligence-report.md

Ready for analyst call — link posted to #operations.
```

</process>

<success_criteria>
This workflow is complete when:
- [ ] Both gathering tracks (RECENT + HISTORICAL) ran and posted to chatroom
- [ ] 0-5 new niches identified with documented reasoning
- [ ] One-pager .pptx created and uploaded (no scores — "Pending Scoring")
- [ ] Niches added to WEEKLY REVIEW tab in tracker (no scores yet)
- [ ] Each niche scored against detailed G&B scorecard
- [ ] Per-niche scorecard xlsx created and uploaded to niche Drive folder
- [ ] Scores written back to one-pagers (Assessment/Status updated)
- [ ] Scores written back to tracker (WEEKLY REVIEW rows updated)
- [ ] Output report written with valid vault frontmatter
- [ ] Slack notification sent with niche count, names, scores
- [ ] User notified with summary
- [ ] For niches flagged for activation: customer validation call lists created, approved by Kay, then sent to JJ
</success_criteria>

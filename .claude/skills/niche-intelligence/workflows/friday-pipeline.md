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
   - IDEATION tab (existing niches under consideration)
   - WEEKLY REVIEW tab (active niches — need current scores for promotion threshold)
   - KILLED tab (niche names to exclude)
   - TABLED tab (niches that could resurface with new data)
3. Store the killed/tabled/active niche lists — these feed into Step 2

## Step 1: GATHER (Parallel Sub-Agents)

Spawn ALL five gathering agents in a **single message** for parallel execution.

Each agent posts a structured summary to the chatroom with:
- Source identifier (newsletter / web / calls / email / research)
- Key signals found (with relevance to M&A, PE activity, niche opportunities)
- Specific industries or companies mentioned
- Any data points useful for scoring (market size, growth rates, margins, etc.)

### Sub-Agents to Spawn (parallel)

```
Agent("niche-intel-news", prompt from references/sub-agents.md §1a)
Agent("niche-intel-newsletters", prompt from references/sub-agents.md §1b)
Agent("niche-intel-calls", prompt from references/sub-agents.md §1c)
Agent("niche-intel-email", prompt from references/sub-agents.md §1d)
Agent("niche-intel-research", prompt from references/sub-agents.md §1e)
```

### Verification Gate 1

After all agents complete, read the chatroom. Verify:
- [ ] All 5 agents posted (some may post "no relevant data found" — that's OK)
- [ ] At least 2 agents returned substantive signals

If fewer than 2 agents returned data, log a warning but continue — Step 2 can still work with limited input by doing its own web research.

## Step 2: IDENTIFY + VALIDATE (Sequential — fused)

Spawn `niche-intel-identifier` agent with:
- All gathered intelligence from chatroom
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
5. Creates a Drive folder for the niche under IDEATION subfolder (`1fQNl6mogJW-6u5XJeE5uYQGsDPx495_O`)
6. Uploads the pptx to the new folder
7. Posts folder ID and file confirmation to chatroom

### Verification Gate 3 (STOP — must pass before Step 4)

After ALL one-pager agents complete, the orchestrator MUST verify each niche before proceeding:

For each niche:
1. Confirm .pptx file exists locally (`ls /tmp/{niche-slug}-onepager.pptx`)
2. Confirm Drive folder was created in IDEATION subfolder:
   `gog drive ls -a kay.s@greenwichandbarrow.com --parent 1fQNl6mogJW-6u5XJeE5uYQGsDPx495_O -j`
3. Confirm exactly ONE file exists in each new folder (no duplicates):
   `gog drive ls -a kay.s@greenwichandbarrow.com --parent {folder_id} -j`
4. Confirm Assessment/Status says "Pending Scoring" (no scores leaked into one-pager)

**If any niche fails:** Log the error in the chatroom, exclude that niche from Steps 4-5, and continue with passing niches.
**If ALL niches fail:** Stop pipeline, post error summary to chatroom, notify user.

## Step 4: ADD TO TRACKER (Sequential)

Spawn `niche-intel-tracker` agent to add new niches to IDEATION tab BEFORE scoring.

This agent:
1. Appends each new niche to IDEATION tab with columns populated (Score left blank, notes = "Pending scoring")
2. Posts confirmation of all sheet updates to chatroom

### Verification Gate 4 (STOP — must pass before Step 5)

After tracker update completes, verify:
1. Re-read IDEATION tab: `gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "IDEATION!A:J" -a kay.s@greenwichandbarrow.com -j`
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
4. Normalizes to /3 scale for IDEATION tab compatibility
5. Also fills in IDEATION-specific columns: Margins, Recurring Revenue, AI Defensibility, Right to Win, Network Access
6. Writes the final output report to `brain/outputs/{date}-niche-intelligence-report.md`
7. **Updates one-pagers** with final scores (downloads pptx, updates Assessment/Status, re-uploads)
8. **Updates tracker** with scores (writes score + IDEATION columns to the rows added in Step 4)
9. Checks if any scored niche warrants promotion to WEEKLY REVIEW (score > lowest WEEKLY REVIEW score AND >= 2.50)

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
| Source | Agent | Key Signals |
|--------|-------|-------------|
| Web/Social | niche-intel-news | {summary} |
| Newsletters | niche-intel-newsletters | {summary} |
| Calls | niche-intel-calls | {summary} |
| Email | niche-intel-email | {summary} |
| Prior Research | niche-intel-research | {summary} |

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
**IDEATION Columns:** Margins={}, Recurring={}, AI Defensibility={}, Right to Win={}, Network Access={}
**One-Pager:** [Drive link]
**Recommendation:** Add to IDEATION / Promote to WEEKLY REVIEW / Table / Kill

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
- [ ] One-pagers updated with scores on Drive
- [ ] Tracker IDEATION rows updated with scores
- [ ] Promoted niches appear in WEEKLY REVIEW tab (if applicable)

## Completion

After all steps complete:

1. Read the full chatroom to compile final status
2. Send Slack notification:

```bash
curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
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
- [ ] All 5 gathering agents ran and posted to chatroom
- [ ] 0-5 new niches identified with documented reasoning
- [ ] One-pager .pptx created and uploaded (no scores — "Pending Scoring")
- [ ] Niches added to IDEATION tab in tracker (no scores yet)
- [ ] Each niche scored against detailed G&B scorecard
- [ ] Scores written back to one-pagers (Assessment/Status updated)
- [ ] Scores written back to tracker (IDEATION rows updated)
- [ ] High-scoring niches promoted to WEEKLY REVIEW if warranted
- [ ] Output report written with valid vault frontmatter
- [ ] Slack notification sent with niche count, names, scores
- [ ] User notified with summary
</success_criteria>

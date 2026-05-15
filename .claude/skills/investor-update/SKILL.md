---
name: investor-update
description: "Investor communication — quarterly deck to all 12 investors, monthly call prep (Jeff Stevens), biweekly call prep (Guillermo Lavergne), post-LOI weekly DD. Four modes: quarterly, monthly, biweekly, weekly-dd."
archetype: orchestrator
context_budget:
  skill_md: 200
  max_references: 12
  learnings_md: 40
  sub_agent_limit: 500
user_invocable: true
---

<objective>
Keep investors informed and engaged across four cadences, using type-specific templates + Kay-approved golden examples as format references.

**Quarterly** — 3-slide deck summarizing the quarter, emailed to all 12 investors. Uses Start/Stop/Continue framework (investors love it). Triggers follow-up scheduling. Template: `templates/quarterly-deck.md`. Examples: `examples/quarterly/`.

**Monthly call prep** — Jeff Stevens (Anacapa Partners, lead investor). Terse bulleted call prep, forward-looking, max ~40 body lines. Template: `templates/monthly-call-prep.md`. Examples: `examples/monthly/`.

**Biweekly call prep** — Guillermo Lavergne (Ashford). Same terse bulleted format as monthly, biweekly window. Template: `templates/biweekly-call-prep.md`. Examples: `examples/biweekly/`.

**Weekly DD** (post-LOI only) — Deal-specific update materials for weekly investor group meetings during due diligence. Template: `templates/weekly-dd.md`. Examples: `examples/weekly-dd/` (populated once a deal reaches LOI).

**Core principle:** Investors want to hear about deals and progress, not feelings. Even when deal flow is light, frame operational improvements as competitive advantage.

**Template + example loading invariant:** Every call-prep subagent invocation MUST load `templates/{mode}.md` AND the most recent file in `examples/{mode}/` as the format reference BEFORE drafting. Do not fall through to a generic template. If the example folder is empty, stop and ask Kay for a golden.
</objective>

<mode_routing>
## Mode → Template + Example Mapping

| Invocation | Mode | Template | Examples folder | Save location |
|------------|------|----------|-----------------|---------------|
| `/investor-update monthly {name}` or `/investor-update call-prep {name}` (auto-detect monthly investor) | monthly | `templates/monthly-call-prep.md` | `examples/monthly/` | Drive `1FGxl4_q44sHK-Kv7t1hHfCMfYXA3H9YW` + `brain/briefs/` |
| `/investor-update biweekly {name}` or `/investor-update call-prep {name}` (auto-detect biweekly investor) | biweekly | `templates/biweekly-call-prep.md` | `examples/biweekly/` | Drive `1SFkrxnkBpyng6dWIcW3eDXqab9sf8wui` + `brain/briefs/` |
| `/investor-update quarterly` | quarterly | `templates/quarterly-deck.md` | `examples/quarterly/` | Drive DRAFTS `1mAOJgIy1_0QmfjtuHMDZQBg5_AIFsF5u`, then SENT `10xTxhVvuz8dmpwXvTV0j0NHF_ghW-GI5` |
| `/investor-update weekly-dd {company}` | weekly-dd | `templates/weekly-dd.md` | `examples/weekly-dd/` | Deal folder `ACTIVE DEALS / {Company} / NOTES /` |

**Cadence auto-detect from investor name:**
- Jeff Stevens → monthly
- Guillermo Lavergne → biweekly
- BK Growth, Saltoun Capital, Tom Jackson, Clayton Sachs, 6 others → quarterly only

**Invariant enforcement:** every subagent invocation MUST load `templates/{mode}.md` AND `examples/{mode}/{most-recent-file}.md` BEFORE drafting. Fail the run if either is unreadable. Do not fall through to a generic template.
</mode_routing>

<essential_principles>
## Investor Relationships

| Investor | Role | Cadence | Notes |
|----------|------|---------|-------|
| Jeff Stevens (Anacapa Partners) | Largest investor | Monthly call | Lead investor |
| Guillermo Lavergne | 2nd largest | Bi-weekly call | Office ~1x/quarter |
| BK Growth | Investor | Quarterly + office | Co-located |
| Saltoun Capital | Investor | Quarterly + office | Co-located |
| Tom Jackson | Investor | Quarterly + office | Co-located |
| Clayton Sachs | Investor | Quarterly + office | Co-located |
| 6 others | Investors | Quarterly | — |

**Attio:** Investor Engagement pipeline, list_id: `f9d58294-5fb2-4794-b796-5c9ffa066025`

## Drive Locations

- **Quarterly reports:** INVESTOR COMMUNICATION / QUARTERLY / QUARTERLIES SENT (folder ID: `10xTxhVvuz8dmpwXvTV0j0NHF_ghW-GI5`)
- **Quarterly drafts:** INVESTOR COMMUNICATION / QUARTERLY / DRAFTS (folder ID: `1mAOJgIy1_0QmfjtuHMDZQBg5_AIFsF5u`)
- **Monthly call notes:** INVESTOR COMMUNICATION / MONTHLY (folder ID: `1FGxl4_q44sHK-Kv7t1hHfCMfYXA3H9YW`)
- **Bi-weekly call notes:** INVESTOR COMMUNICATION / BI-WEEKLY (folder ID: `1SFkrxnkBpyng6dWIcW3eDXqab9sf8wui`)

## Format Rules

- Start/Stop/Continue framework on Slide 2 (mandatory, investors love it)
- Coded deal names for confidentiality (first 2-3 letters, e.g., ACU, HG, PR)
- "STRICTLY CONFIDENTIAL" watermark on every slide
- No em dashes
- Direct, confident, honest about progress
- Budget remaining always reported
- Investor Ask always included (intros, specific help)

## Email Rules

- Personalize per investor where relevant
- Reference shared office conversations for co-located investors
- Reference recent 1:1 topics for monthly/bi-weekly investors
- Sign off "Very best, Kay"
</essential_principles>

<modes>
## Mode 1: Quarterly Update

**Trigger:** End of quarter (Q1 ends May 7, Q2 ends Aug 7, etc.) or on-demand via `/investor-update quarterly`

### Sub-Agent 1: Data Collector
**Task:** Pull all data sources for the quarter.
**Tools:** gog sheets, Attio API, vault reads, gog gmail

**Data to collect:**
```json
{
  "weekly_tracker": "Pull all weekly columns for the quarter from Weekly Activity Tracker",
  "attio_pipeline": "Deals by stage, stage changes this quarter, new deals added, deals killed",
  "niche_activity": "Which niches explored, activated, killed this quarter (from Industry Research Tracker)",
  "conference_activity": "Conferences attended, contacts made, conversations (from conference pipeline sheet)",
  "deal_activity": "Deals evaluated, NDAs signed, financials received, LOIs (from Attio + vault)",
  "outreach_volume": "Emails sent, calls made, response rates (from weekly tracker)",
  "budget": "Current fund balance, burn rate, runway",
  "key_calls": "Significant calls/meetings from vault brain/calls/ this quarter",
  "granola_investor_calls": "Transcripts from monthly/bi-weekly investor calls for context continuity"
}
```

**Queries:**
```bash
# Weekly tracker data
gog sheets get "1NGGZY_iq9h8cNzLAXSJ1vTcsfXWNU9oin2RiOMtl9NE" "'Weekly Topline'!A:Z" --json

# Attio pipeline snapshot
curl -s -X POST "https://api.attio.com/v2/lists/0cf5dd92-4a97-4c6b-9f6c-1e64c81bfc7b/entries/query" \
  -H "Authorization: Bearer $ATTIO_API_KEY" -H "Content-Type: application/json" -d '{}'

# Vault calls this quarter
Glob: brain/calls/{QUARTER_START_YYYY-MM}* through brain/calls/{QUARTER_END_YYYY-MM}*

# Niche tracker
gog sheets get "1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins" "'WEEKLY REVIEW'!A:Z" --json
```

**Returns:**
```json
{
  "metrics": {
    "ndas_signed": 0,
    "financials_received": 0,
    "lois_submitted": 0,
    "lois_signed": 0,
    "meaningful_conversations": 0,
    "outreach_sent": 0,
    "response_rate": 0,
    "conferences_attended": 0,
    "deals_added": 0,
    "deals_killed": 0
  },
  "deals": [{"code": "", "source": "", "status": "", "summary": ""}],
  "niches": [{"name": "", "status": "active|killed|tabled"}],
  "budget_remaining": "",
  "budget_pct": ""
}
```

**Stop Hook:**
- [ ] Weekly tracker data retrieved
- [ ] Attio pipeline data retrieved
- [ ] At least one data source per section populated

### Sub-Agent 2: Narrative Drafter
**Task:** Draft the 3-slide quarterly update.
**Tools:** Data from Agent 1, previous quarterly reports for tone

**Slide 1: Executive Summary**
- 3-4 bullet highlights for the quarter
- Investor Ask (specific, actionable — intros, industries, connections)
- Quarter label and "STRICTLY CONFIDENTIAL"

**Slide 2: Start / Stop / Continue / Pause**
- PROGRESS: Key metric or milestone + budget remaining
- START: New approaches or initiatives this quarter
- STOP: What was deprioritized and why
- PAUSE: What's on hold and why
- CONTINUE: What's working and will keep doing

**Slide 3: Key Learnings + Opportunity Highlights + Strategic Planning**
- CONTINUE: 3-4 operational learnings
- Opportunity Highlights: Active deals with coded names, source, status (1-2 lines each)
- Strategic Planning: Next quarter focus (2-3 sentences)

**Voice guidance:**
- Direct and confident, even when reporting challenges
- Frame pivots as strategic decisions, not failures
- Operational improvements (AI tooling) are competitive advantage, not gap-filling
- Honest about what didn't work without being self-deprecating
- Read previous quarters for tone continuity

**Returns:** Full text for all 3 slides

**Stop Hook:**
- [ ] All 3 slides have content
- [ ] Start/Stop/Continue/Pause framework present on Slide 2
- [ ] Investor Ask is specific and actionable
- [ ] Budget remaining reported
- [ ] Deal names are coded
- [ ] No em dashes

### Sub-Agent 3: Deck Builder
**Task:** Create the deck from template or previous quarter's deck.
**Tools:** gog slides or gog drive copy + edit

**Steps:**
1. Create from template using `gog slides create-from-template`:
   - Template ID: `16LUAOazJEufkncRS2E_VvYH9HRGw7x5GlSZovvUq9r0`
   - Use `--exact` mode with replacements JSON
2. All placeholder tags ({{QUARTER}}, {{EXECUTIVE_SUMMARY}}, etc.) populated with new narrative
3. Update quarter label
4. Save to DRAFTS folder first
5. Present to Kay for review

**Returns:**
```json
{
  "deck_id": "",
  "deck_url": "",
  "location": "DRAFTS"
}
```

**Stop Hook:**
- [ ] Deck exists in DRAFTS folder
- [ ] Quarter label is correct
- [ ] All 3 slides updated with new content
- [ ] STRICTLY CONFIDENTIAL on every slide

### Sub-Agent 4: Email Drafter
**Task:** Draft personalized emails to each of the 12 investors.
**Tools:** gog gmail (read recent threads), Attio (investor list), vault entities

**Steps:**
1. Pull investor list from Attio Investor Engagement pipeline
2. For each investor, draft email:
   - Warm opening (personalized)
   - "Attached is our Q{X} update"
   - 1-2 sentence highlight most relevant to that investor
   - Investor Ask repeated
   - Sign off "Very best, Kay"
3. Personalization rules:
   - **Co-located investors** (BK Growth, Saltoun, Tom Jackson, Clayton Sachs): Reference recent office conversation if available
   - **Jeff Stevens**: Reference recent monthly call topic
   - **Guillermo**: Reference recent bi-weekly call topic
   - **Others**: General but warm
4. Create drafts via Gmail using `gog gmail draft create` (do NOT send) — per `feedback_gmail_only_no_superhuman` (Superhuman sunset 4/29)

**Returns:** List of 12 draft emails with investor name, personalization note

**Stop Hook:**
- [ ] 12 email drafts created
- [ ] Each has personalized opening
- [ ] Deck attached or linked
- [ ] No em dashes
- [ ] Sign off "Very best, Kay"

### Phase: Post-Send Follow-Up
After Kay sends the quarterly update:
1. Create Motion tasks: "Follow-up call with {investor}" for each investor, due 2 weeks out
2. Track responses in Attio
3. Surface in pipeline-manager morning briefing: "3 investors responded to Q{X} update — {names}. 9 haven't replied."

### Quarterly Deliverables
1. Draft deck in DRAFTS folder → Kay reviews → moves to QUARTERLIES SENT
2. 12 personalized email drafts
3. Motion follow-up tasks created
4. Slack notification to #operations: "Q{X} investor update ready for review. Deck: {url}"

---

## Mode 2: Weekly DD (Post-LOI)

**Trigger:** Active deal in LOI Signed stage in Attio, or on-demand via `/investor-update weekly-dd`

### Sub-Agent 5: DD Update Builder
**Task:** Prepare weekly due diligence update for investor group meeting.
**Tools:** gog drive (deal folder), vault reads, Attio

**Steps:**
1. Pull current DD status:
   - What was reviewed this week
   - Key findings (positive and concerning)
   - Open items / blockers
   - Financial model updates
   - Legal/accounting status
2. Pull from deal folder:
   - New documents received
   - Scorecard updates
   - Any revised financials
3. Build update:

**Weekly DD Update Structure:**
```
DD UPDATE: {Company} — Week {N}
Week ending: {date}

STATUS: {On track / Flagged / Considering kill}

THIS WEEK:
- Reviewed: {list of items}
- Key findings: {bullets}
- Concerns: {bullets}

FINANCIAL MODEL:
- Revenue: ${X}M → {any revision}
- EBITDA: ${X}M → {any revision}
- Key assumption changes: {if any}

OPEN ITEMS:
- [ ] {item} — owner: {who} — due: {when}
- [ ] {item}

NEXT WEEK:
- {planned activities}

DECISION POINT:
- {If approaching kill/go decision, flag it}
```

4. Save to deal folder NOTES/
5. Notify via Slack

**Returns:** Formatted DD update

**Stop Hook:**
- [ ] Update covers what was reviewed
- [ ] Financial model status included
- [ ] Open items have owners and dates
- [ ] Saved to deal folder
</modes>

<execution_flow>
## Invocation

```
/investor-update quarterly          → Mode 1: Full quarterly deck + emails
/investor-update weekly-dd          → Mode 2: Weekly DD update (post-LOI only)
```

## Sub-Agent Summary

| Agent | Mode | Task | Parallel? |
|-------|------|------|-----------|
| 1: Data Collector | Quarterly | Pull all data sources | Solo (first) |
| 2: Narrative Drafter | Quarterly | Write 3-slide content | Solo (after Agent 1) |
| 3: Deck Builder | Quarterly | Create/update PowerPoint | Solo (after Agent 2) |
| 4: Email Drafter | Quarterly | 12 personalized email drafts | Solo (after Agent 3) |
| 5: DD Update | Weekly DD | Due diligence progress update | Solo |

Quarterly mode runs sequentially (each agent depends on the previous).
Weekly DD is a standalone single-agent mode.

**Note:** Investor call prep (Jeff monthly, Guillermo bi-weekly) is handled by meeting-brief-manager (Subagent 2), which auto-detects investor meetings on the calendar and routes them to the appropriate prep template.

## Pipeline-Manager Integration

Pipeline-manager should:
- After quarterly update sent → track investor responses, surface non-responders
- During DD → remind Kay to run weekly-dd before investor meetings
</execution_flow>

<success_criteria>
## Success Criteria

### Quarterly Mode
- [ ] Data collected from all sources (weekly tracker, Attio, vault, niche tracker)
- [ ] 3-slide deck in correct format with Start/Stop/Continue
- [ ] All deals coded for confidentiality
- [ ] Budget remaining reported
- [ ] Investor Ask is specific
- [ ] Deck saved to DRAFTS → Kay reviews → moves to QUARTERLIES SENT
- [ ] 12 personalized email drafts created
- [ ] Motion follow-up tasks created for all 12 investors
- [ ] Slack notification sent to #operations

### Weekly DD Mode
- [ ] DD progress summarized
- [ ] Financial model status included
- [ ] Open items with owners and dates
- [ ] Saved to deal folder NOTES/
- [ ] Slack notification sent

### Validation (all modes)
```python
checks = {
    "deliverable_exists": file_or_message_created(),
    "no_em_dashes": no_em_dashes_in_output(),
    "confidential_watermark": deck_has_watermark() if quarterly else True,
    "deal_names_coded": no_real_deal_names() if quarterly else True,
}
```
</success_criteria>

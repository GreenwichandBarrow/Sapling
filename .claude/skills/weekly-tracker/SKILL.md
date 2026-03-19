---
name: weekly-tracker
description: "Weekly activity tracker — sub-agents pull data from Gmail, Calendar, Attio, and vault in parallel, populate Google Sheet + vault snapshot, Slack notify on completion. Run every Friday."
user_invocable: true
---

<objective>
Populate the G&B Weekly Activity Tracker with the current week's data.

This is **Stage 7: Model Updating** of the G&B acquisition methodology. It answers two questions:
- **Signal Quality** — Are we reaching the right people? Are conversations converting?
- **System Throughput** — Is the machine producing enough volume to hit the goal?

Goal: 1 interesting deal reviewed per week, fed by 2–5 owner conversations per week.

The Google Sheet already exists (one-time creation done). Each run adds a new weekly column to the existing sheet.
</objective>

<essential_principles>
## What Kay Cares About

These metrics are what matter, in priority order. They go at the top of the sheet, visually distinct:

**Deal Progress (the scoreboard):**
1. **LOIs Signed** — committed deal
2. **LOIs Submitted** — active pursuit
3. **Financials Received** — real diligence happening
4. **NDAs Signed** — deals progressing past intro

**Conversation Quality (the leading indicator):**
5. **Meaningful Owner Conversations** — owner discussed selling, shared business details, or agreed to next steps. Captured via `meaningful_conversation` checkbox on Active Deals list entries in Attio. Includes calls, in-person meetings, and Zoom. This is the #3 most tracked metric by experienced searchers (2025 investor survey).
6. **Calls 15+ minutes** — quality signal separating real conversations from quick intros
7. **Owner Response Rate (%)** — responses received / outreach sent. Experienced searchers track this over raw email count.

**Source Attribution (where conversations come from):**
8. **Conversations by source** — conference, email outreach, broker, network intro, cold call. Tracks which channels are actually converting.

Everything else is diagnostic — it shows whether the activity machine is converting into those numbers. The core question the supporting data answers: **Are we getting 2-5 meaningful owner conversations per week that turn into 1 interesting deal per week?** If key metrics are low, the source attribution and supporting data show where the funnel is leaking.

**Context:** 2025 investor survey of 54 searchers showed experienced searchers (24+ months) shift from tracking top-of-funnel (emails sent, open rates) to tracking direct connections (meetings, meaningful conversations, response rates, LOIs). Emails sent is a vanity metric. Meaningful conversations is the leading indicator.

## Locations

- **Google Sheet:** `OPERATIONS / WEEKLY ACTIVITY TRACKER` (folder ID: `1-TcRl74G0Ezc0lEJC9__BiBPwnG7gwfR`)
  - Sheet ID: `1NGGZY_iq9h8cNzLAXSJ1vTcsfXWNU9oin2RiOMtl9NE`
  - Tabs: `Weekly Topline`, `Weekly Detail`, `Quarterly Summary`
- **Vault:** `brain/trackers/weekly/{YYYY-MM-DD}-weekly-tracker.md` (week-ending date)

## Schedule

Run Friday night (automated, ready Friday morning review). Or on demand via `/weekly-tracker`. The sheet is cumulative — each run adds a new column for the current week.
</essential_principles>

<sub_agents>
## Sub-Agent Architecture

Spawn 4 specialized sub-agents in parallel to collect data. Each returns a structured JSON summary. Use `agent-chatroom` if 3+ agents are needed concurrently.

### Agent 1: Gmail Collector
**Task:** Count outreach volume and responses for the week.
**Tools:** gog gmail search
**Returns:**
```json
{
  "outreach_emails_sent": 0,
  "cold_calls_logged": 0,
  "responses_received": 0,
  "owner_response_rate_pct": 0,
  "intro_threads": [],
  "outreach_by_source": {"email": 0, "cold_call": 0, "conference_followup": 0, "broker": 0, "network": 0}
}
```
**Queries:**
```bash
# Outreach sent (from Kay or JJ)
gog gmail search "from:me subject:(introduction OR intro OR regarding OR reaching out) after:{WEEK_START} before:{WEEK_END}" --json
# Responses received
gog gmail search "to:me subject:(re: introduction OR re: intro OR re: regarding) after:{WEEK_START} before:{WEEK_END}" --json
```
Count unique threads, not individual messages. Look for cold call confirmation/follow-up emails to estimate call volume.

### Agent 2: Calendar & Meetings Collector
**Task:** Classify all meetings for the week.
**Tools:** gog calendar list, Granola MCP, vault reads
**Returns:**
```json
{
  "stage_1_calls": 0,
  "stage_2_calls": 0,
  "networking_meetings": 0,
  "introductions_received": 0,
  "meeting_details": []
}
```
**Queries:**
```bash
gog calendar list --from {WEEK_START} --to {WEEK_END} --json
```
Classify each event:
- **Stage 1 call** — first call with a deal contact / broker / owner
- **Stage 2 call** — follow-up / deep dive on a specific deal
- **Networking** — river guides, advisors, fellow searchers, introductions
- **Internal** — skip (team calls, recurring standups)

Cross-reference with `brain/calls/` for logged call notes. Use Granola MCP to verify meeting counts if available.

### Agent 3: Attio Pipeline Collector
**Task:** Pull pipeline movements and deal stage data from all 4 Lists.
**Tools:** Attio API (curl)
**API:** Bearer token from `.env` (`ATTIO_API_KEY`), base URL `https://api.attio.com/v2`

**CRITICAL:** All pipelines are Attio **Lists**. Query the Lists API, not the Deals object.

**Lists to query:**
- Active Deals – Owners: `0cf5dd92-4a97-4c6b-9f6c-1e64c81bfc7b`
- Outreach: Network Pipeline: `94ccb017-2b86-4e12-b674-e27de8e146c9`
- Outreach: Intermediary Pipeline: `7faac55b-a183-4afe-b7ea-fc8a4ccace10`

**Active Deals stage mapping (report ALL stages, even if 0 deals):**

| Attio Stage | Tracker Metric |
|---|---|
| Identified | (sourcing) |
| Contacted | (sourcing) |
| First Conversation | Stage 1 Calls |
| Second Conversation | Stage 2 Calls |
| NDA Executed | NDAs Signed |
| Financials Received | Financials Received |
| Active Diligence | Deals in Active Review |
| LOI / Offer Submitted | LOIs Submitted |
| LOI Signed | LOIs Signed |
| Closed / Not Proceeding | Deals Killed |

**To get all stage names:** `GET /v2/lists/{list_id}/attributes/stage/statuses`
**To get entries:** `POST /v2/lists/{list_id}/entries/query` with `{}`

**Also query `meaningful_conversation` checkbox on Active Deals entries:**
```
For each entry, check if meaningful_conversation is checked.
Count total meaningful conversations this week (by comparing timestamps).
```

**Returns:**
```json
{
  "ndas_signed": 0,
  "financials_received": 0,
  "lois_submitted": 0,
  "lois_signed": 0,
  "meaningful_conversations": 0,
  "total_active_pipeline": 0,
  "deals_added": 0,
  "deals_killed": 0,
  "qualified_a_count": 0,
  "deals_in_review": 0,
  "stage_counts": {"Identified": 0, "Contacted": 0, ...}
}
```
Count deals per stage. For weekly changes, compare `created_at` timestamps against the week window for new deals. For killed deals, count entries at "Closed / Not Proceeding".

### Agent 4: Vault Activity Collector
**Task:** Count vault activity for the week.
**Tools:** Glob, Grep, git log
**Returns:**
```json
{
  "new_contacts_added": 0,
  "call_notes_logged": 0,
  "entities_created": []
}
```
**Queries:**
```bash
# Call notes in date range
Glob: brain/calls/{YYYY-MM-DD}*  (for each day in the week)

# New entities created this week
git log --after={WEEK_START} --before={WEEK_END} --name-only --diff-filter=A -- brain/entities/
```
### Agent 5: Linkt Credit & ICP Collector
**Task:** Pull Linkt credit usage, list quality metrics, and ICP accuracy from the master sheet.
**Tools:** Linkt API (curl), gog sheets
**Returns:**
```json
{
  "credits_used_this_week": 0,
  "credits_used_this_month": 0,
  "credits_remaining": 150,
  "entities_returned": 0,
  "search_runs": 0,
  "avg_entities_per_run": 0,
  "kay_accept_rate": 0,
  "kay_reject_rate": 0,
  "top_reject_reason": "",
  "jj_connection_rate": 0,
  "positive_sentiment_rate": 0,
  "credits_per_approved_target": 0,
  "credits_per_conversation": 0,
  "active_icp_name": "",
  "requested_list_size": 0,
  "icp_changed_this_week": false
}
```
**Queries:**
```bash
# Linkt credit usage
curl -s -X GET "https://api.linkt.ai/v1/run" -H "x-api-key: {API_KEY}" | # filter runs by date range

# Master sheet ICP data (Kay + JJ columns)
gog sheets get "{MASTER_SHEET_ID}" "'Active'!N:T" --json  # Kay Decision, Reject Reason, Call Status, Sentiment
```
</sub_agents>

<execution_flow>
## Execution Flow

### Step 1: Define the Week
```
WEEK_START = Monday 00:00 of current week
WEEK_END = Friday (today) or Sunday if running retroactively
WEEK_ENDING_DATE = Friday date in YYYY-MM-DD format
```

### Step 2: Spawn Data Collection Sub-Agents
Launch all 5 agents in parallel:
```
Agent 1: Gmail Collector (background)
Agent 2: Calendar & Meetings Collector (background)
Agent 3: Attio Pipeline Collector (background)
Agent 4: Vault Activity Collector (background)
Agent 5: Linkt Credit & ICP Collector (background)
```
Wait for all to return.

### Step 3: Aggregate & Calculate
Merge all agent results into a single data object. Calculate derived metrics:
- **Response Rate** = responses_received / outreach_emails_sent
- **Outreach → Owner Conversation** = stage_1_calls / outreach_emails_sent
- **Owner Conversation → NDA** = ndas_signed / stage_1_calls

### Step 4: Write to Google Sheet
Read current sheet to find next empty column, then write data to all 3 tabs:

**Weekly Topline tab** — write new column with:
- Week ending date (header)
- NDAs Signed
- Financials Received
- LOIs Submitted
- LOIs Signed

**Weekly Detail tab** — write new column with all metrics:
- System Throughput: outreach, calls, responses, contacts, networking, intros
- Signal Quality: response rate, Stage 1 calls, A count, Stage 2 calls, deals in review, conversion rates
- Pipeline Health: total active, added, killed

**Quarterly Summary tab** — update current quarter column with cumulative totals (SUM formulas referencing Weekly Detail)

```bash
SHEET_ID="1NGGZY_iq9h8cNzLAXSJ1vTcsfXWNU9oin2RiOMtl9NE"

# Find next empty column
gog sheets get "$SHEET_ID" "'Weekly Topline'!1:1" --json

# Write to all 3 tabs
gog sheets update "$SHEET_ID" "'Weekly Topline'!{COL}1:{COL}9" --values-json '{...}'
gog sheets update "$SHEET_ID" "'Weekly Detail'!{COL}1:{COL}23" --values-json '{...}'
gog sheets update "$SHEET_ID" "'Quarterly Summary'!{QCOL}3:{QCOL}31" --values-json '{...}'
```

### Step 5: Save Vault Snapshot
Write `brain/trackers/weekly/{YYYY-MM-DD}-weekly-tracker.md` with frontmatter and diagnostic narrative.

### Step 6: Validation (Stop Hook)
Before notifying, validate all deliverables exist:

```python
# Validation checks (stop hook logic)
checks = {
    "sheet_updated": verify_sheet_column_exists(SHEET_ID, WEEK_ENDING_DATE),
    "vault_file": file_exists(f"brain/trackers/weekly/{WEEK_ENDING_DATE}-weekly-tracker.md"),
    "topline_populated": verify_tab_has_data("Weekly Topline", COL),
    "detail_populated": verify_tab_has_data("Weekly Detail", COL),
}

# If any check fails, halt and report — do NOT send Slack notification
for check, passed in checks.items():
    if not passed:
        raise ValidationError(f"STOP: {check} failed. Fix before notifying.")
```

**Validation rules:**
1. Google Sheet has a new column with the correct week-ending date in all 3 tabs
2. Key metrics (NDAs, financials, LOIs submitted, LOIs signed) are populated (even if 0)
3. Vault snapshot file exists at the expected path with valid frontmatter
4. Vault snapshot contains all 4 key metrics in the body

**If validation fails:** Do NOT send Slack. Report the failure and what's missing. Fix and re-validate.

### Step 7: Notify
Only after validation passes:
```bash
curl -s -X POST "SLACK_WEBHOOK_REDACTED" \
  -H "Content-Type: application/json" \
  -d '{"text":"Weekly Activity Tracker updated for week ending {date}.\nNDAs: {n} | Financials: {n} | LOIs submitted: {n} | LOIs signed: {n}\nhttps://docs.google.com/spreadsheets/d/1NGGZY_iq9h8cNzLAXSJ1vTcsfXWNU9oin2RiOMtl9NE/edit"}'
```
The Slack message must always include the 4 key metrics and the Sheet link.
</execution_flow>

<sheet_structure>
## Google Sheet Structure

### Tab 1: Weekly Topline
Kay's glanceable view. 4 key metrics only.

| Row | Metric | Target | {Week Col} |
|-----|--------|--------|------------|
| 1 | Header | | Week ending {date} |
| 2 | | | |
| 3 | KEY METRICS | Target | |
| 4 | NDAs Signed | 1/wk | {n} |
| 5 | Financials Received | 1/wk | {n} |
| 6 | LOIs Submitted | — | {n} |
| 7 | LOIs Signed | — | {n} |
| 8 | | | |
| 9 | Goal: 1 interesting deal reviewed per week | | |

### Tab 2: Weekly Detail
Diagnostic view organized by Stage 7 questions.

| Row | Metric | Target | {Week Col} |
|-----|--------|--------|------------|
| 1 | Header | | Week ending {date} |
| 2 | | | |
| 3 | SYSTEM THROUGHPUT | Target | |
| 4 | Outreach Emails Sent | — | {n} |
| 5 | Cold Calls Made | — | {n} |
| 6 | Responses Received | — | {n} |
| 7 | New Contacts Added | — | {n} |
| 8 | Networking Meetings | — | {n} |
| 9 | Introductions Received | — | {n} |
| 10 | | | |
| 11 | SIGNAL QUALITY | Target | |
| 12 | Response Rate | — | {calculated} |
| 13 | Stage 1 Calls (Owner Conversations) | 2–5/wk | {n} |
| 14 | Qualified Opportunities (A count) | — | {n} |
| 15 | Stage 2 Calls (Deep Dives) | — | {n} |
| 16 | Deals in Active Review | — | {n} |
| 17 | Conversion: Outreach to Owner Conversation | — | {calculated} |
| 18 | Conversion: Owner Conversation to NDA | — | {calculated} |
| 19 | | | |
| 20 | PIPELINE HEALTH | Target | |
| 21 | Total Active Pipeline | — | {n} |
| 22 | Deals Added This Week | — | {n} |
| 23 | Deals Killed/Passed | — | {n} |

### Tab 3: Quarterly Summary
Investor-grade rollup. Cumulative totals and conversion funnels.

| Row | Metric | Q1 2026 | Q2 2026 | ... |
|-----|--------|---------|---------|-----|
| DEAL FLOW | | | | |
| Total Owner Conversations | =SUM(weekly) | | | |
| Total Deals Reviewed | =SUM(weekly) | | | |
| NDAs Signed (cumulative) | =SUM(weekly) | | | |
| Financials Received (cumulative) | =SUM(weekly) | | | |
| LOIs Submitted (cumulative) | =SUM(weekly) | | | |
| LOIs Signed (cumulative) | =SUM(weekly) | | | |
| CONVERSION RATES | | | | |
| Outreach to Response | =responses/outreach | | | |
| Response to Owner Conversation | =stage1/responses | | | |
| Owner Conversation to NDA | =NDAs/stage1 | | | |
| NDA to Financials | =financials/NDAs | | | |
| Financials to LOI | =LOIs/financials | | | |
| PIPELINE HEALTH | | | | |
| Active Pipeline (end of quarter) | {snapshot} | | | |
| Deals Killed/Passed | =SUM(weekly) | | | |
| Net Pipeline Growth | =added-killed | | | |
| ACTIVITY VOLUME | | | | |
| Total Outreach Sent | =SUM(emails+calls) | | | |
| Networking Meetings | =SUM(weekly) | | | |
| Introductions Received | =SUM(weekly) | | | |
| THESIS | | | | |
| Active Niches | {list} | | | |
| Niches Activated This Quarter | {count} | | | |
| Niches Killed This Quarter | {count} | | | |

### Tab 4: Linkt Credit Tracker
Tracks credit consumption, list quality, and ICP efficiency week over week.

| Row | Metric | Target | {Week Col} |
|-----|--------|--------|------------|
| 1 | Header | | Week ending {date} |
| 2 | | | |
| 3 | CREDIT USAGE | | |
| 4 | Credits Used This Week | — | {n} |
| 5 | Credits Used This Month (cumulative) | 150/mo | {n} |
| 6 | Credits Remaining This Month | — | {n} |
| 7 | | | |
| 8 | LIST QUALITY | | |
| 9 | Entities Returned | — | {n} |
| 10 | Entities per Credit | — | {calculated} |
| 11 | Search Runs This Week | — | {n} |
| 12 | Avg Entities per Run | — | {calculated} |
| 13 | | | |
| 14 | ICP ACCURACY | | |
| 15 | Kay Accept Rate | 70%+ | {%} |
| 16 | Kay Reject Rate | — | {%} |
| 17 | Top Reject Reason | — | {reason} |
| 18 | | | |
| 19 | OUTREACH CONVERSION | | |
| 20 | JJ Connection Rate | — | {%} |
| 21 | Positive Sentiment Rate | — | {%} |
| 22 | Credits per Approved Target | — | {calculated} |
| 23 | Credits per Conversation | — | {calculated} |
| 24 | | | |
| 25 | ICP CONFIGURATION | | |
| 26 | Active ICP Name | — | {name} |
| 27 | Requested List Size | — | {n} |
| 28 | ICP Change This Week? | — | Y/N |

**Data sources:**
- Credits used: Linkt API (`/v1/run` endpoint, sum credits per run this week)
- Entities returned: Linkt API (`/v1/entity/search` count) or from master sheet row count
- Kay accept/reject: Master sheet Col N (Kay Decision)
- JJ rates: Master sheet Col Q (Call Status) and Col T (Owner Sentiment)

**What this tab tells you:**
- Are we burning credits too fast? (Credits remaining vs days left in month)
- Are the lists good quality? (Accept rate, entities per credit)
- Should we change the list size request? (If 20 entities/run and 50% rejected, try 10 tighter ones)
- Should we upgrade the subscription? (If consistently hitting 150 by week 3)
- Is the ICP working? (Credits per conversation is the ultimate efficiency metric)

### Why These Supporting Metrics

Every supporting metric maps to one of the two Stage 7 diagnostic questions:

**System Throughput** — Is the machine producing enough?
| Metric | Diagnoses |
|--------|-----------|
| Outreach emails sent | Is outbound volume sufficient? |
| Cold calls made | Is phone activity consistent? |
| Responses received | Is outreach generating engagement? |
| New contacts added | Is the network growing? |
| Networking meetings | Is the relationship engine active? |
| Introductions received | Are relationships producing warm leads? |

**Signal Quality** — Are we reaching the right people?
| Metric | Diagnoses |
|--------|-----------|
| Response rate | Is our messaging resonating? |
| Stage 1 calls (owner conversations) | Are we hitting 2–5/wk? The critical conversion point. |
| Qualified "A" count | Are conversations with the right type of owner? |
| Stage 2 calls (deep dives) | Are qualified leads progressing? |
| Deals in active review | Are we modeling enough financials? |
| Outreach to owner conversation rate | Is volume converting to real conversations? |
| Owner conversation to NDA rate | Are conversations converting to deals? |

### Trend Analysis (Monthly)

On the **4th week of each month** (or on demand), include a trend analysis in the vault snapshot:
- **Conversion rates over time:** outreach → response → Stage 1 → qualified → NDA → financials → LOI
- **Velocity:** avg time between stages (are deals speeding up or stalling?)
- **Volume vs. conversion:** is the problem not enough activity, or poor conversion at a specific stage?
- **Month-over-month comparison** of key metrics
- **Recommendation:** 1–2 specific process changes based on the data
</sheet_structure>

<vault_save>
## Vault Snapshot

Save to `brain/trackers/weekly/{YYYY-MM-DD}-weekly-tracker.md`:

```yaml
---
schema_version: "1.0.0"
date: {YYYY-MM-DD}
type: tracker
title: "Weekly Activity Tracker — Week Ending {date}"
tags:
  - date/{YYYY-MM-DD}
  - output
  - output/tracker
  - status/published
  - topic/weekly-tracker
  - source/claude
---
```

Body contains the week's numbers in readable markdown format, plus a short diagnostic narrative structured around Stage 7:
- **Key metrics vs. goal** — Are we hitting 1 interesting deal/week?
- **System Throughput** — Is outbound volume sufficient? Are enough conversations being generated?
- **Signal Quality** — Are we reaching the right people? Where is conversion breaking down?
- **Notable pipeline movements** — deals advancing, stalling, or killed
- **Flags** — anything that needs attention next week
</vault_save>

<success_criteria>
## Success Criteria

Tracker update is complete when ALL checks pass:

### Data Collection
- [ ] All 4 sub-agents returned data (Gmail, Calendar, Attio, Vault)
- [ ] No sub-agent errored silently (check for empty/null returns)

### Google Sheet
- [ ] New column added to Weekly Topline with week-ending date
- [ ] New column added to Weekly Detail with week-ending date
- [ ] Key metrics populated in Topline (even if 0)
- [ ] All metrics populated in Detail (even if 0)
- [ ] Quarterly Summary updated with current quarter cumulative totals

### Vault
- [ ] Snapshot file exists at `brain/trackers/weekly/{date}-weekly-tracker.md`
- [ ] Frontmatter passes schema validation
- [ ] Body contains all 4 key metrics
- [ ] Diagnostic narrative present (throughput + signal quality)

### Notification
- [ ] Validation stop hook passed (all above checks green)
- [ ] Slack notification sent with 4 key metrics and Sheet link
- [ ] Google Sheet link shared with user
</success_criteria>

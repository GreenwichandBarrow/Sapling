---
name: weekly-tracker
description: "Weekly activity tracker — sub-agents pull data from Gmail, Calendar, Attio, and vault in parallel, populate Google Sheet + vault snapshot, Slack notify on completion. Run every Friday."
# WARNING: 3.7x over archetype cap; refactor pending per item 2.
archetype: orchestrator
context_budget:
  skill_md: 750
  max_references: 12
  learnings_md: 40
  sub_agent_limit: 500
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
6. **Owner Calls 15+ minutes** — quality signal separating real owner conversations from quick intros. Only counts calls with business owners, not investor calls, networking, or internal meetings.
7. **Owner Response Rate (%)** — responses received / outreach sent. Experienced searchers track this over raw email count.

**Source Attribution (where conversations come from):**
8. **Conversations by source** — conference, email outreach, broker, network intro, cold call. Tracks which channels are actually converting.

Everything else is diagnostic — it shows whether the activity machine is converting into those numbers. The core question the supporting data answers: **Are we getting 2-5 meaningful owner conversations per week that turn into 1 interesting deal per week?** If key metrics are low, the source attribution and supporting data show where the funnel is leaking.

**Context:** 2025 investor survey of 54 searchers showed experienced searchers (24+ months) shift from tracking top-of-funnel (emails sent, open rates) to tracking direct connections (meetings, meaningful conversations, response rates, LOIs). Emails sent is a vanity metric. Meaningful conversations is the leading indicator.

## Locations

- **Google Sheet:** `OPERATIONS / WEEKLY ACTIVITY TRACKER` (folder ID: `1-TcRl74G0Ezc0lEJC9__BiBPwnG7gwfR`)
  - Sheet ID: `1NGGZY_iq9h8cNzLAXSJ1vTcsfXWNU9oin2RiOMtl9NE`
  - Tabs: `Weekly Topline`, `Weekly Detail`, `Quarterly Summary`, `Apollo Credit Tracker`
  - Weekly snapshots: `OPERATIONS/WEEKLY ACTIVITY TRACKER/WEEKLY SNAPSHOTS/` (Drive)
- **Vault:** `brain/trackers/weekly/{YYYY-MM-DD}-weekly-tracker.md` (week-ending date)

## Schedule

Run Friday night (automated, ready Friday morning review). Or on demand via `/weekly-tracker`. The sheet is cumulative — each run adds a new column for the current week.
</essential_principles>

<sub_agents>
## Sub-Agent Architecture

Spawn 6 specialized sub-agents in parallel to collect data. Each returns a structured JSON summary. Use `agent-chatroom` if 3+ agents are needed concurrently.

### Agent 1: Gmail Collector
**Task:** Count outreach volume, responses, and introductions for the week.
**Tools:** gog gmail search

**Metric definitions:**
- **Outreach Emails Sent:** All acquisition-related outreach — cold emails to owners, broker intros, intermediary emails, network intro emails. NOT internal ops, personal, or support emails.
- **Responses Received:** Replies to outreach from owners, brokers, intermediaries, or network contacts on acquisition-related threads. NOT automated/support/promo emails.
- **Introductions Received:** A **first-time personal introduction** where someone connects Kay to a new person she hasn't met before — NOT forwarded deal flow (teasers/CIMs are inbound deals, not intros). An introduction means: "Kay, meet {person}. {Person}, meet Kay." Look for: 3+ recipients, subject lines with "intro/introduction/meet/connecting you with." Do NOT count: ongoing threads from prior-week intros that just had activity this week, forwarded deal documents, or deal flow from intermediaries.

**Returns:**
```json
{
  "outreach_emails_sent": 0,
  "cold_calls_logged": 0,
  "responses_received": 0,
  "introductions_received": 0,
  "owner_response_rate_pct": 0,
  "intro_threads": [],
  "outreach_by_source": {"email": 0, "cold_call": 0, "conference_followup": 0, "broker": 0, "network": 0, "linkedin_dm": 0}
}
```
**Queries:**
```bash
# Outreach sent — use specific OUTREACH sublabels (parent label doesn't work in Gmail search)
gog gmail search "(label:OUTREACH/INTERMEDIARIES OR label:OUTREACH/NETWORK) from:me after:{WEEK_START} before:{WEEK_END}" --json
# Manually filter out non-outreach (invoices, receipts, consultant payments that happen to have outreach labels)
# Only count threads where Kay initiated or continued acquisition-related correspondence

# Responses — same label query, filter to threads with messageCount > 1
gog gmail search "(label:OUTREACH/INTERMEDIARIES OR label:OUTREACH/NETWORK) after:{WEEK_START} before:{WEEK_END}" --json
# Thread with messageCount > 1 where the other party replied = 1 response

# Introductions received — someone introducing Kay to a new person
gog gmail search "to:me (subject:intro OR subject:introduction OR subject:meet OR subject:connecting) after:{WEEK_START} before:{WEEK_END}" --json
gog gmail search "to:me (subject:FW: OR subject:Fwd:) (subject:acquisition OR subject:opportunity OR subject:restoration OR subject:teaser) after:{WEEK_START} before:{WEEK_END}" --json
# Count: any thread where a third party introduced Kay to someone new (broker forwarding a deal, investor making a connection, etc.)
```
Count unique threads, not individual messages. For each thread, verify it's acquisition-relevant before counting. Exclude: automated emails, support threads, internal ops, personal correspondence, newsletters, consultant invoices.

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
**Task:** Pull pipeline movements and deal stage data from Attio Lists.
**Tools:** Attio API (curl)
**API:** Bearer token from `.env` (`ATTIO_API_KEY`), base URL `https://api.attio.com/v2`

**CRITICAL:** All pipelines are Attio **Lists**. Query the Lists API, not the Deals object.

**Lists to query:**
- Active Deals – Owners: `0cf5dd92-4a97-4c6b-9f6c-1e64c81bfc7b`
- Outreach: Network Pipeline: `94ccb017-2b86-4e12-b674-e27de8e146c9`

**Active Deals stage mapping (report ALL stages, even if 0 deals):**

| Attio Stage | Tracker Metric |
|---|---|
| Identified | (sourcing) |
| Contacted | (sourcing) |
| First Conversation | Stage 1 Calls |
| Second Conversation | Stage 2 Calls |
| NDA Executed | NDAs Signed |
| Financials Received | Financials Received |
| Active Diligence | (part of Deals in Active Review) |
| LOI / Offer Submitted | LOIs Submitted |
| LOI Signed | LOIs Signed |
| Closed / Not Proceeding | Deals Killed |

**Deals in Active Review** = Entries from **Financials Received through LOI Signed** (stages 6-9). A deal is "in active review" once Kay has a CIM or financials and is evaluating whether to proceed. Earlier stages (Identified, Contacted, First Conversation, NDA Executed) are sourcing/top-of-funnel. Closed/Not Proceeding are resolved. This is a weekly delta — count deals that were in these stages at any point during the week, including deals that entered and were killed within the same week.

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
Count deals per stage. **CRITICAL: Key metrics (NDAs, Financials, LOIs) must be WEEKLY DELTAS, not total snapshot counts.** Compare each entry's stage `active_from` timestamp against the week window to determine which entries *moved into* that stage this week. For example, if 2 entries are at "NDA Executed" but only 1 moved there this week, report ndas_signed=1. For deals added, compare `created_at` timestamps against the week window. For deals killed, count entries that moved to "Closed / Not Proceeding" this week (not total at that stage).

### Agent 4: Vault & Attio Activity Collector
**Task:** Count new contacts added across both vault AND Attio this week.
**Tools:** Glob, Grep, git log, Attio API (curl)

**"New Contacts Added" includes:**
- New vault entities created in `brain/entities/`
- New Company records created in Attio (by `created_at` timestamp this week)
- New People records created in Attio (by `created_at` timestamp this week)
- New list entries added to any pipeline (by `created_at` timestamp this week)

Deduplicate: if a company appears in both vault and Attio, count once.

**Returns:**
```json
{
  "new_contacts_added": 0,
  "call_notes_logged": 0,
  "entities_created": [],
  "attio_companies_created": 0,
  "attio_people_created": 0
}
```
**Queries:**
```bash
# Call notes in date range
Glob: brain/calls/{YYYY-MM-DD}*  (for each day in the week)

# New vault entities created this week
git log --after={WEEK_START} --before={WEEK_END} --name-only --diff-filter=A -- brain/entities/

# New Attio companies created this week
curl -s -X POST "https://api.attio.com/v2/objects/companies/records/query" \
  -H "Authorization: Bearer {API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"filter":{"created_at":{"$gte":"{WEEK_START}T00:00:00Z"}}}'

# New Attio list entries created this week (check each pipeline)
# Filter entries by created_at >= WEEK_START
```
### Agent 5: Tool & Integration Monitor
**Task:** Check parked/pending tool integrations for new features that would be valuable to G&B.
**Tools:** WebFetch
**Checks:**
- **Happenstance:** Fetch `https://developer.happenstance.ai/llms.txt` and `https://happenstance.ai` — look for LinkedIn integration, Chrome extension, or any new data source beyond Gmail/Calendar/Instagram/Twitter. If found, flag as high-priority in report.
- *(Add future tools to monitor here)*

**Returns:**
```json
{
  "tools_checked": ["happenstance"],
  "changes_detected": [],
  "flags": []
}
```
If no changes, return empty arrays. Only flag meaningful integration additions, not minor UI/docs changes.

### Agent 6: Apollo Credit & ICP Collector
**Task:** Pull Apollo credit usage, list quality metrics, and ICP accuracy from the master sheet.
**Tools:** Apollo API (curl), gog sheets
**Returns:**
```json
{
  "credits_used_this_week": 0,
  "credits_used_this_month": 0,
  "credits_remaining": 0,
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
# Apollo credit usage — check account credit consumption via API:
# GET https://api.apollo.io/api/v1/auth/health (returns credit balance and usage)
# Count email reveals logged this week by querying Apollo people/search with reveal dates
# or by counting new email reveals on the master sheet (Col with Apollo-sourced emails)
curl -s -X GET "https://api.apollo.io/api/v1/auth/health" \
  -H "X-Api-Key: ${APOLLO_API_KEY}" \
  -H "Content-Type: application/json"

# Master sheet ICP data (Kay + JJ columns)
gog sheets get "{MASTER_SHEET_ID}" "'Active'!O:U" --json  # Kay Decision, Pass Reason, Call Status, Sentiment
```
### Agent 6 (extended): Outreach Channel Collector
**Additional task for Agent 6:** Pull outreach metrics by channel.

Outreach tracking varies by niche channel type:
- **DealsX Email niches:** Metrics come from Sam's shared Google Sheet (company, owner, email, date contacted, response status, meetings booked). Read the shared sheet for emails sent, responses, and meetings.
- **Kay Email niches:** Metrics come from Gmail (existing tracking via Agent 1). Superhuman sunset 4/29 — no longer a source.
- **JJ-Call-Only niches:** Metrics come from target sheet call columns (existing tracking via Agent 3).

**Queries:**
```bash
# DealsX shared sheet — read Sam's report for outreach metrics
# Sheet contains: company, owner, email, date contacted, response status, meetings booked
gog sheets get "{DEALSX_SHARED_SHEET_ID}" "'Sheet1'!A:F" --json
# Filter rows by date range for this week

# LinkedIn DMs — track manually from Gmail notification emails
gog gmail search "from:linkedin.com subject:accepted subject:invitation after:{WEEK_START} before:{WEEK_END}" --json
```

**Counts:**
- DealsX Emails Sent (from Sam's shared sheet: rows with date contacted this week)
- DealsX Responses (from Sam's shared sheet: rows with response status this week)
- DealsX Meetings Booked (from Sam's shared sheet: rows with meetings booked this week)
- Kay Emails Sent (from Gmail Agent 1 data, filtered to Kay Email niches)
- LinkedIn DMs Sent (from Gmail notification scan)
- LinkedIn DMs Responded (from Gmail LinkedIn reply notifications)

Include in Agent 6 returns:
```json
{
  "dealsx_emails_sent": 0,
  "dealsx_responses": 0,
  "dealsx_meetings_booked": 0,
  "kay_emails_sent": 0,
  "linkedin_dms_sent": 0,
  "linkedin_dms_responded": 0,
  "linkedin_dm_response_rate": 0
}
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

**Weekend rollover rule:** Saturday and Sunday activity counts toward the FOLLOWING week (Monday-Friday). When scanning for signals, include the prior Saturday and Sunday in the current week's window:
```
EFFECTIVE_WEEK_START = Saturday 00:00 before WEEK_START (i.e., 2 days before Monday)
```
This ensures that weekend NDAs, emails, or CIM receipts land in the next week's tracker, not the prior week's.

### Step 2: Spawn Data Collection Sub-Agents
Launch all 6 agents in parallel:
```
Agent 1: Gmail Collector (background)
Agent 2: Calendar & Meetings Collector (background)
Agent 3: Attio Pipeline Collector (background)
Agent 4: Vault Activity Collector (background)
Agent 5: Tool & Integration Monitor (background)
Agent 6: Apollo Credit & ICP Collector (background)
```
Wait for all to return.

### Step 3: Aggregate & Calculate
Merge all agent results into a single data object. Calculate derived metrics:
- **Response Rate** = responses_received / outreach_emails_sent
- **Outreach → Owner Conversation** = stage_1_calls / outreach_emails_sent
- **Owner Conversation → NDA** = ndas_signed / stage_1_calls
- **Daily Outreach Average** = outreach_emails_sent / business_days_this_week (target: 4-6/day)
- **Daily Call Average** = cold_calls_made / business_days_this_week (should match email volume)
- **Volume Flag:** If daily outreach average exceeds 6/day, flag in the weekly summary: "Outreach volume above target (X/day vs 4-6 target). Review quality vs quantity." If below 3/day when a sprint is active, flag: "Outreach volume below target. Check target-discovery pipeline."

### Step 4: Write to Google Sheet
Read current sheet to find next empty column, then write data to all 3 tabs:

**Weekly Topline tab** — write new column with:
- Week ending date (header)
- NDAs Signed
- Financials Received
- LOIs Submitted
- LOIs Signed

**Weekly Detail tab** — write new column with all metrics. **CRITICAL: distinguish delta vs snapshot.**

**WEEKLY DELTAS (what happened this week):**
- Outreach Emails Sent, Cold Calls Made, Responses Received, New Contacts Added, Networking Meetings, Introductions Received
- Stage 1 Calls, Qualified Opportunities (newly qualified this week), Stage 2 Calls
- NDAs Signed (moved to NDA Executed THIS week), Financials Received (THIS week), LOIs Submitted (THIS week), LOIs Signed (THIS week)
- Deals Added This Week, Deals Killed/Passed (moved to Closed THIS week)
- Response Rate, Conversion rates (calculated from this week's deltas)

**SNAPSHOTS (current state, not delta):**
- Qualified Opportunities / A count (current count: deals Kay is actively pursuing — requested financials, initiated diligence, etc.)
- Deals in Active Review (weekly delta: deals at Financials Received through LOI Signed at any point this week, including deals that entered and exited within the week)
- Top of Funnel / Total Pipeline (current count: all except Closed/Not Proceeding — includes Identified and Contacted not yet engaged)

To compute deltas: check each entry's stage `active_from` timestamp. Only count entries that moved INTO a stage during the week window.

**Quarterly Summary tab** — update current quarter column with cumulative totals (SUM formulas referencing Weekly Detail)

```bash
SHEET_ID="1NGGZY_iq9h8cNzLAXSJ1vTcsfXWNU9oin2RiOMtl9NE"

# Find next empty column
gog sheets get "$SHEET_ID" "'Weekly Topline'!1:1" --json

# Write to all 4 tabs
gog sheets update "$SHEET_ID" "'Weekly Topline'!{COL}1:{COL}9" --values-json '{...}'
# Weekly Detail: write aggregate total to next historical column (left), then overwrite niche breakdown columns (right)
gog sheets update "$SHEET_ID" "'Weekly Detail'!{COL}1:{COL}27" --values-json '{...}'
gog sheets update "$SHEET_ID" "'Quarterly Summary'!{QCOL}3:{QCOL}31" --values-json '{...}'
gog sheets update "$SHEET_ID" "'Apollo Credit Tracker'!{COL}1:{COL}28" --values-json '{...}'
```

### Step 4.5: Save Weekly Detail Snapshot to Drive
After writing to the sheet, export the Weekly Detail tab as an xlsx file to preserve the niche breakdown before it gets overwritten next week.

```bash
SNAPSHOT_FOLDER="OPERATIONS/WEEKLY ACTIVITY TRACKER/WEEKLY SNAPSHOTS"
SNAPSHOT_FILENAME="Weekly Detail - {WEEK_ENDING_DATE}.xlsx"

# Export Weekly Detail tab as xlsx and upload to Drive snapshots folder
# 1. Use gog to export the sheet tab as xlsx
gog sheets export "$SHEET_ID" --tab "Weekly Detail" --format xlsx --output "/tmp/${SNAPSHOT_FILENAME}"

# 2. Upload to Drive
gog drive upload "/tmp/${SNAPSHOT_FILENAME}" --folder "$SNAPSHOT_FOLDER"
```

**Purpose:** The niche breakdown (right section of Weekly Detail) is overwritten each week with the current sprint's data. This snapshot preserves the full niche breakdown for historical reference. Drive folder: `OPERATIONS/WEEKLY ACTIVITY TRACKER/WEEKLY SNAPSHOTS/`.

### Step 5: Save Vault Snapshot
Write `brain/trackers/weekly/{YYYY-MM-DD}-weekly-tracker.md` with frontmatter and diagnostic narrative.

### Step 6: Validation (Stop Hook) — MANDATORY

**Two-layer enforcement:**

1. **PreToolUse hook (skill-internal):** `.claude/hooks/router/handlers/weekly_tracker_validation.py` — blocks Slack webhook from firing if validation fails. First line of defense; runs inside the agent's tool-call loop.

2. **POST_RUN_CHECK validator (wrapper-level):** `scripts/validate_weekly_tracker_integrity.py` — runs AFTER `claude -p` exits, regardless of internal hook state. Catches the silent-success failure mode where the agent exits 0 but artifacts are missing (e.g. 4/24 partial-write where vault snapshot landed but sheet column did not).

**Wrapper validator copyable invocation (manual run):**
```bash
python3 "/Users/kaycschneider/Documents/AI Operations/scripts/validate_weekly_tracker_integrity.py"
# Pass --week-ending YYYY-MM-DD to override auto-Friday computation
```

The validator returns exit 2 on failure. The launchd wrapper (`scripts/run-skill.sh`) overrides EXIT_CODE on POST_RUN_CHECK failure and emits a Slack alert prefixed `VALIDATOR FAILED`. Pattern: `memory/feedback_mutating_skill_hardening_pattern.md`. Bead: `ai-ops-jrj.3`.

Before notifying, validate all deliverables exist:

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
curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
  -H "Content-Type: application/json" \
  -d '{"text":"Weekly Activity Tracker updated for week ending {date}.\nNDAs: {n} | Financials: {n} | LOIs submitted: {n} | LOIs signed: {n}\nhttps://docs.google.com/spreadsheets/d/1NGGZY_iq9h8cNzLAXSJ1vTcsfXWNU9oin2RiOMtl9NE/edit"}'
```
The Slack message must always include the 4 key metrics and the Sheet link.
</execution_flow>

<sheet_structure>
## Google Sheet Structure

### Tab 0: Dashboard
Kay's process optimization view. Presents 10 high-level questions that surface where the pipeline needs tuning. This is NOT system health (that's health-monitor's job) — it's about **process optimization decisions** through two lenses:

- **Signal Quality** — Are we reaching the right people with the right message?
- **System Throughput** — Is the pipeline flowing or stuck?

**Current questions (populated):**

| # | Question | Lens | Data Source | Decision Trigger |
|---|----------|------|-------------|-----------------|
| 1 | Do any niches need more targets? | System Throughput | Read each niche's target sheet — count rows by Col O status (Identified, Contacted, etc.) and outreach status. Flag any niche where remaining uncontacted targets < 10. | "Fractional CFO needs refill" → triggers target-discovery for that niche |
| 2 | Which email variant is winning per niche? | Signal Quality | A/B testing for DealsX niches managed by Sam. Kay Email niches track variants on target sheet. Pull open rate, reply rate, meeting rate per variant (A vs B) from channel-appropriate source. | "Variant A outperforming in Art Advisory" → shift more targets to Variant A |

**Placeholder questions (3-10):**

| # | Question | Lens |
|---|----------|------|
| 3 | [Placeholder — to be added as process matures] | — |
| 4 | [Placeholder — to be added as process matures] | — |
| 5 | [Placeholder — to be added as process matures] | — |
| 6 | [Placeholder — to be added as process matures] | — |
| 7 | [Placeholder — to be added as process matures] | — |
| 8 | [Placeholder — to be added as process matures] | — |
| 9 | [Placeholder — to be added as process matures] | — |
| 10 | [Placeholder — to be added as process matures] | — |

**Data collection for active questions:**
- **Q1 (target refill):** For each active niche sprint, read the niche's target sheet. Count total rows, rows where Col O = any contacted/outreached status, and rows where Col O = Identified (uncontacted). If uncontacted < 10, flag the niche name and remaining count.
- **Q2 (variant performance):** For DealsX niches, request A/B variant data from Sam's shared sheet or weekly report. For Kay Email niches, check target sheet variant column for open rate, reply rate, and meeting-booked rate per variant. Present side-by-side comparison.

**How dashboard feeds decisions:**
- Dashboard presents data and recommendations. Kay decides. Do NOT auto-act on dashboard findings.
- Q1 refill recommendation → Kay approves → target-discovery runs for that niche.
- Q2 variant recommendation → Kay approves → variant mix adjusted (DealsX: Sam updates; Kay Email: target sheet updated).

**Sheet layout:** One row per question. Columns: Question #, Question, Lens, Current Answer, Recommendation, Last Updated. Answers and recommendations are overwritten each week.

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
Diagnostic view organized by Stage 7 questions. **This tab serves dual purpose: historical totals on the left (one column per week), niche breakdown on the right (current week only), Description column at the far right.**

**Left section (historical):** Each week adds a new Total column. Metrics are aggregate weekly deltas — one column per week ending date.

**Right section (current week niche breakdown):** Per-niche columns for the current week only. Each active niche sprint gets its own column showing outreach, calls, and conversations broken down by niche. This section is overwritten each week — history is preserved via Drive snapshot (see Step 4.5).

**Description column (far right):** Static labels/row headers for human readability.

When writing to the sheet, write aggregate totals to the left historical column, then write per-niche breakdown to the right niche columns. For metrics that don't break down by niche (e.g., New Contacts Added, Networking Meetings), populate in aggregate total only.

| Row | Metric | Target | {Week Col} |
|-----|--------|--------|------------|
| 1 | Header | | Week ending {date} |
| 2 | | | |
| 3 | SYSTEM THROUGHPUT | Target | |
| 4 | Outreach Emails Sent | — | {n} |
| 5 | Cold Calls Made | — | {n} |
| 6 | JJ Dials (total) | 8-12/day | {n} |
| 7 | LinkedIn DMs Drafted | — | {n} |
| 8 | LinkedIn DMs Sent | — | {n} |
| 9 | Responses Received | — | {n} |
| 10 | New Contacts Added | — | {n} |
| 11 | Networking Meetings | — | {n} |
| 12 | Introductions Received | — | {n} |
| 13 | | | |
| 14 | SIGNAL QUALITY | Target | |
| 15 | Response Rate | — | {calculated} |
| 16 | Stage 1 Calls (Owner Conversations) | 2–5/wk | {n} |
| 17 | Qualified Opportunities (A count) | — | {n} |
| 18 | Stage 2 Calls (Deep Dives) | — | {n} |
| 19 | Deals in Active Review | — | {n} |
| 20 | Conversion: Outreach to Owner Conversation | — | {calculated} |
| 21 | Conversion: Owner Conversation to NDA | — | {calculated} |
| 22 | LinkedIn DM Response Rate | — | {calculated} |
| 23 | | | |
| 24 | PIPELINE HEALTH | Target | |
| 25 | Top of Funnel (Total Pipeline) | — | {n} |
| 26 | Deals Added This Week | — | {n} |
| 27 | Deals Killed/Passed | — | {n} |

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

### Tab 4: Apollo Credit Tracker
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
| 16 | Kay Pass Rate | — | {%} |
| 17 | Top Pass Reason | — | {reason} |
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
- Credits used: Apollo API (`/api/v1/auth/health` endpoint for balance, count email reveals this week)
- Entities returned: Apollo API (people/search results count) or from master sheet row count
- Kay accept/reject: Master sheet Col N (Kay Decision)
- JJ rates: Master sheet Call Status field and Owner Sentiment field.

**CRITICAL — JJ dial counting rule (per `feedback_jj_call_date_from_field_not_tab`):**

- Tab names like `Call Log 4.21.26` are **estimated** batch dates — the date the row was staged, not the date JJ called.
- JJ's actual dial date is the value he types into the `JJ: 1st Call Date` or `JJ: 2nd Call Date` field (post-4/21 NEW schema), or the `JJ: Call Date` field on pre-4/21 OLD-schema tabs.
- JJ routinely logs today's calls onto older prep tabs (confirmed 4/24: today's 9 dials landed on the 4.21.26 tab). Grouping by tab name **misses these entirely** and under-reports the true count.
- **Always count by populated `Call Date` value across ALL tabs + Full Target List, grouped by the actual date value — never by tab name.**
- Normalize date formats before counting: JJ mixes `4/20/26`, `4.24.26`, `4/13/2026`, and occasionally malformed entries like `4/8//2026`. Treat any value containing digits + `/` or `.` + digits as a candidate date; strip punctuation variants before grouping.
- Pre-4/21 OLD-schema tabs have header-vs-data drift: dates may sit under the field header `JJ: Call Notes` instead of `JJ: Call Date` on rows written before the 4/23 migration. Sample-inspect before counting; when in doubt, scan all four JJ fields for date-shaped values.

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
- **Niche breakdown** — per-niche outreach, calls, and conversations for the current week (mirrors the right section of Weekly Detail). Include a table with one row per active niche sprint.
- **Notable pipeline movements** — deals advancing, stalling, or killed
- **Flags** — anything that needs attention next week
</vault_save>

<success_criteria>
## Success Criteria

Tracker update is complete when ALL checks pass:

### Data Collection
- [ ] All 5 data sub-agents returned data (Gmail, Calendar, Attio, Vault, Apollo)
- [ ] No sub-agent errored silently (check for empty/null returns)

### Google Sheet
- [ ] New column added to Weekly Topline with week-ending date
- [ ] New column added to Weekly Detail (historical left section) with week-ending date
- [ ] Weekly Detail niche breakdown (right section) updated for current week
- [ ] Key metrics populated in Topline (even if 0)
- [ ] All metrics populated in Detail (even if 0)
- [ ] Quarterly Summary updated with current quarter cumulative totals
- [ ] Apollo Credit Tracker tab updated
- [ ] LinkedIn DM metrics populated (even if 0)
- [ ] JJ dial count populated
- [ ] Weekly Detail snapshot exported as xlsx to Drive (`OPERATIONS/WEEKLY ACTIVITY TRACKER/WEEKLY SNAPSHOTS/Weekly Detail - {date}.xlsx`)

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

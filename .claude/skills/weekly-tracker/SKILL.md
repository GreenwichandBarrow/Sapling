---
name: weekly-tracker
description: "Generate the weekly activity tracker — pulls data from Gmail, Calendar, Attio, and vault, writes to Google Sheet + vault. Run every Friday or on demand."
user_invocable: true
---

<objective>
Populate the G&B Weekly Activity Tracker with the current week's data. The tracker is a cumulative Google Sheet spanning the full search, with one column per week. Key metrics (NDAs signed, financials received, LOIs submitted, LOIs signed) are featured prominently at the top. Supporting activity metrics fill in below.

Goal: 1 interesting deal per week.
</objective>

<essential_principles>
## What Kay Cares About

These 4 metrics are the only ones that matter. They go at the top of the sheet, visually distinct:

1. **NDAs Signed** — deals progressing past intro
2. **Financials Received** — real diligence happening
3. **LOIs Submitted** — active pursuit
4. **LOIs Signed** — committed deal

Everything else is diagnostic — it shows whether the activity machine is converting into those numbers. The core question the supporting data answers: **Are we getting 2–5 owner conversations per week that turn into 1 interesting deal per week?** If key metrics are low, the supporting data shows where the funnel is leaking.

## Locations

- **Google Sheet:** `OPERATIONS / WEEKLY ACTIVITY TRACKER` (folder ID: `1-TcRl74G0Ezc0lEJC9__BiBPwnG7gwfR`)
- **Vault:** `brain/trackers/weekly/{YYYY-MM-DD}-weekly-tracker.md` (week-ending date)

## Schedule

Run every Friday (or on demand via `/weekly-tracker`). The sheet is cumulative — each run adds a new column for the current week.
</essential_principles>

<sheet_structure>
## Google Sheet Layout

The sheet has a single tab: **Weekly Tracker**

### Row Structure

| Row | Metric | Target | Week 1 | Week 2 | ... |
|-----|--------|--------|--------|--------|-----|
| **Header** | | | Week ending {date} | Week ending {date} | |
| | | | | | |
| **KEY METRICS** | | | | | |
| 1 | NDAs Signed | 1/wk | {n} | {n} | |
| 2 | Financials Received | 1/wk | {n} | {n} | |
| 3 | LOIs Submitted | — | {n} | {n} | |
| 4 | LOIs Signed | — | {n} | {n} | |
| | | | | | |
| **SOURCING** | | | | | |
| 5 | Outreach Emails Sent | — | {n} | {n} | |
| 6 | Cold Calls Made | — | {n} | {n} | |
| 7 | Responses Received | — | {n} | {n} | |
| 8 | Response Rate | — | =(R7/R5) | | |
| 9 | New Contacts Added | — | {n} | {n} | |
| | | | | | |
| **QUALIFICATION** | | | | | |
| 10 | Stage 1 Calls Completed | — | {n} | {n} | |
| 11 | Qualified Opportunities ("A" count) | — | {n} | {n} | |
| | | | | | |
| **CONVERSION** | | | | | |
| 12 | Stage 2 Calls Completed | — | {n} | {n} | |
| 13 | Deals in Active Review | — | {n} | {n} | |
| | | | | | |
| **PIPELINE HEALTH** | | | | | |
| 14 | Total Active Pipeline | — | {n} | {n} | |
| 15 | Deals Added This Week | — | {n} | {n} | |
| 16 | Deals Killed/Passed | — | {n} | {n} | |
| | | | | | |
| **RELATIONSHIPS** | | | | | |
| 17 | Networking Meetings | — | {n} | {n} | |
| 18 | Introductions Received | — | {n} | {n} | |

Key metrics rows (1–4) should be **bold** with a distinct background color to stand out visually.

### Why These Supporting Metrics

Every supporting metric exists to answer a diagnostic question when key metrics underperform:

| Metric | Diagnoses |
|--------|-----------|
| Outreach emails sent | Are we generating enough top-of-funnel volume? |
| Cold calls made | Is JJ's call activity consistent? |
| Responses received + rate | Is our messaging working? |
| New contacts added | Is the network growing? |
| Stage 1 calls | Are responses converting to conversations? |
| Qualified "A" count | Are we talking to the right people? |
| Stage 2 calls | Are qualified leads progressing to deep dives? |
| Deals in active review | Are we modeling enough financials? |
| Pipeline totals / adds / kills | Is the pipeline growing, flat, or shrinking? |
| Networking + intros | Is the relationship engine feeding the deal engine? |

### Trend Analysis

On the **4th week of each month** (or on demand), include a trend analysis in the vault snapshot:
- **Conversion rates over time:** outreach → response → Stage 1 → qualified → NDA → financials → LOI
- **Velocity:** avg time between stages (are deals speeding up or stalling?)
- **Volume vs. conversion:** is the problem not enough activity, or poor conversion at a specific stage?
- **Month-over-month comparison** of key metrics
- **Recommendation:** 1–2 specific process changes based on the data
</sheet_structure>

<data_sources>
## Phase 1: Data Collection

Run these queries in parallel to gather the week's numbers.

### Define the Week
Week = Monday 00:00 to Sunday 23:59 of the current week (or specified week).
```
WEEK_START={Monday date}
WEEK_END={Sunday date}
```

### Gmail — Outreach & Responses
```bash
# Outreach sent (from Kay or JJ)
gog gmail search "from:me subject:(introduction OR intro OR regarding OR reaching out) after:{WEEK_START} before:{WEEK_END}" --json

# Responses received
gog gmail search "to:me subject:(re: introduction OR re: intro OR re: regarding) after:{WEEK_START} before:{WEEK_END}" --json
```
Count unique threads, not individual messages.

### Calendar — Meetings & Calls
```bash
gog calendar list --from {WEEK_START} --to {WEEK_END} --json
```
Classify each event:
- **Stage 1 call** — first call with a deal contact / broker
- **Stage 2 call** — follow-up / deep dive on a specific deal
- **Networking** — river guides, advisors, fellow searchers, introductions
- **Internal** — skip (team calls, recurring standups)

Cross-reference with `brain/calls/` for any logged call notes in the date range.

### Attio — Pipeline Data
```bash
# Query Attio API for deal pipeline movements this week
# NDAs, financials, LOIs from pipeline stage changes
```
Check Attio pipeline for:
- Deals that moved to NDA stage → NDAs Signed count
- Deals that moved to Financials stage → Financials Received count
- Deals that moved to LOI stage → LOIs Submitted count
- Signed LOIs → LOIs Signed count
- Total active deals, new deals added, deals killed/passed

### Vault — Activity Counts
```bash
# Call notes logged this week
ls brain/calls/{WEEK_START}* through brain/calls/{WEEK_END}*

# New contacts/entities created
git log --after={WEEK_START} --before={WEEK_END} --name-only -- brain/entities/
```

### Granola — Meeting Cross-Reference
Use Granola MCP to verify meeting counts against calendar data if needed.
</data_sources>

<write_phase>
## Phase 2: Write to Google Sheet

### First Run (Sheet Creation)
If no sheet exists yet in the tracker folder, create one:
```bash
# Create a new Google Sheet
gog sheets create "G&B Weekly Activity Tracker" --parent "1-TcRl74G0Ezc0lEJC9__BiBPwnG7gwfR"
```
Then populate the row labels (column A), targets (column B), and first week's data (column C).

### Subsequent Runs (Add Column)
1. Read the existing sheet to find the next empty column
2. Write the week-ending date in the header row
3. Write all metric values down the column
4. Formulas (response rate, ratios) should be cell formulas, not pre-calculated

```bash
# Read current sheet to find next column
gog sheets read {SHEET_ID} --range "A1:ZZ1" --json

# Write new column
gog sheets write {SHEET_ID} --range "{COL}1:{COL}20" --values '{json_array}'
```

### Formatting
Apply on first run:
- Key metrics rows (1–4): bold text, light blue background
- Section headers: bold, grey background
- Target column: italic
</write_phase>

<vault_save>
## Phase 3: Save to Vault

Save a markdown snapshot to `brain/trackers/weekly/{YYYY-MM-DD}-weekly-tracker.md`:

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

Body contains the week's numbers in readable markdown format, plus a short diagnostic narrative:
- **Key metrics vs. goal** — Are we hitting 1 interesting deal/week?
- **Funnel diagnosis** — Are we getting 2–5 owner conversations/week? If not, where is the funnel leaking? (volume? response rate? qualification?)
- **Notable pipeline movements** — deals advancing, stalling, or killed
- **Flags** — anything that needs attention next week
</vault_save>

<notify>
## Phase 4: Notify

Send Slack notification with the Google Sheet link:
```bash
curl -s -X POST "SLACK_WEBHOOK_REDACTED" \
  -H "Content-Type: application/json" \
  -d '{"text":"Weekly Activity Tracker updated for week ending {date}.\nNDAs: {n} | Financials: {n} | LOIs submitted: {n} | LOIs signed: {n}\n{Google Sheet link}"}'
```
The Slack message must always include the 4 key metrics and the Sheet link.
</notify>

<success_criteria>
Tracker update is complete when:
- [ ] All data sources queried (Gmail, Calendar, Attio, vault)
- [ ] Key metrics (NDAs, financials, LOIs submitted, LOIs signed) populated
- [ ] Supporting metrics populated
- [ ] New column added to Google Sheet (or sheet created on first run)
- [ ] Vault snapshot saved to brain/trackers/weekly/
- [ ] Slack notification sent with key metrics and Sheet link
- [ ] Google Sheet link shared with user
</success_criteria>

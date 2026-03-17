---
name: weekly-tracker
description: "Generate the weekly activity tracker — pulls data from Gmail, Calendar, Attio, and vault, writes to Google Sheet + vault. Run every Friday or on demand."
user_invocable: true
---

<objective>
Populate the G&B Weekly Activity Tracker with the current week's data. The tracker is a cumulative Google Sheet spanning the full search, with one column per week.

This is **Stage 7: Model Updating** of the G&B acquisition methodology. It answers two questions:
- **Signal Quality** — Are we reaching the right people? Are conversations converting?
- **System Throughput** — Is the machine producing enough volume to hit the goal?

Goal: 1 interesting deal reviewed per week, fed by 2–5 owner conversations per week.
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
  - Sheet ID: `1NGGZY_iq9h8cNzLAXSJ1vTcsfXWNU9oin2RiOMtl9NE`
  - Tabs: `Weekly Topline`, `Weekly Detail`, `Quarterly Summary`
- **Vault:** `brain/trackers/weekly/{YYYY-MM-DD}-weekly-tracker.md` (week-ending date)

## Schedule

Run every Friday (or on demand via `/weekly-tracker`). The sheet is cumulative — each run adds a new column for the current week.
</essential_principles>

<sheet_structure>
## Google Sheet Layout

The sheet has three tabs:
1. **Weekly Topline** — Kay's 4 key metrics only. Clean, glanceable.
2. **Weekly Detail** — System Throughput + Signal Quality diagnostics. Analyzed weekly/monthly to see if the process is improving toward the goal.
3. **Quarterly Summary** — Cumulative investor-grade metrics rolled up from weekly data.

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
| **SYSTEM THROUGHPUT** *(is the machine producing enough?)* | | | | | |
| 5 | Outreach Emails Sent | — | {n} | {n} | |
| 6 | Cold Calls Made | — | {n} | {n} | |
| 7 | Responses Received | — | {n} | {n} | |
| 8 | New Contacts Added | — | {n} | {n} | |
| 9 | Networking Meetings | — | {n} | {n} | |
| 10 | Introductions Received | — | {n} | {n} | |
| | | | | | |
| **SIGNAL QUALITY** *(are we reaching the right people?)* | | | | | |
| 11 | Response Rate | — | =(responses/outreach) | | |
| 12 | Stage 1 Calls (Owner Conversations) | 2–5/wk | {n} | {n} | |
| 13 | Qualified Opportunities ("A" count) | — | {n} | {n} | |
| 14 | Stage 2 Calls (Deep Dives) | — | {n} | {n} | |
| 15 | Deals in Active Review | — | {n} | {n} | |
| 16 | Conversion: Outreach → Owner Conversation | — | =(R12/R5) | | |
| 17 | Conversion: Owner Conversation → NDA | — | =(R1/R12) | | |
| | | | | | |
| **PIPELINE HEALTH** | | | | | |
| 18 | Total Active Pipeline | — | {n} | {n} | |
| 19 | Deals Added This Week | — | {n} | {n} | |
| 20 | Deals Killed/Passed | — | {n} | {n} | |

Key metrics rows (1–4) should be **bold** with a distinct background color to stand out visually.

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
| Outreach → owner conversation rate | Is volume converting to real conversations? |
| Owner conversation → NDA rate | Are conversations converting to deals? |

### Trend Analysis (Monthly)

On the **4th week of each month** (or on demand), include a trend analysis in the vault snapshot:
- **Conversion rates over time:** outreach → response → Stage 1 → qualified → NDA → financials → LOI
- **Velocity:** avg time between stages (are deals speeding up or stalling?)
- **Volume vs. conversion:** is the problem not enough activity, or poor conversion at a specific stage?
- **Month-over-month comparison** of key metrics
- **Recommendation:** 1–2 specific process changes based on the data

### Investor Quarterly View

The weekly data rolls up into quarterly investor metrics. Add a **second tab** to the Google Sheet: **Quarterly Summary**

This tab auto-calculates from the weekly data and is designed to feed directly into quarterly investor updates.

| Metric | Q1 | Q2 | Q3 | Q4 |
|--------|----|----|----|----|
| **Deal Flow** | | | | |
| Total Owner Conversations | =SUM(weekly Stage 1 calls) | | | |
| Total Deals Reviewed | =SUM(weekly deals added) | | | |
| NDAs Signed (cumulative) | =SUM(weekly NDAs) | | | |
| Financials Received (cumulative) | =SUM(weekly financials) | | | |
| LOIs Submitted (cumulative) | =SUM(weekly LOIs submitted) | | | |
| LOIs Signed (cumulative) | =SUM(weekly LOIs signed) | | | |
| **Conversion Rates** | | | | |
| Outreach → Response | =total responses / total outreach | | | |
| Response → Owner Conversation | =total Stage 1 / total responses | | | |
| Owner Conversation → NDA | =total NDAs / total Stage 1 | | | |
| NDA → Financials | =total financials / total NDAs | | | |
| Financials → LOI | =total LOIs / total financials | | | |
| **Pipeline Health** | | | | |
| Active Pipeline (end of quarter) | {snapshot} | | | |
| Deals Killed/Passed | =SUM(weekly kills) | | | |
| Net Pipeline Growth | =added - killed | | | |
| **Activity Volume** | | | | |
| Total Outreach Sent | =SUM(emails + calls) | | | |
| Networking Meetings | =SUM(weekly networking) | | | |
| Introductions Received | =SUM(weekly intros) | | | |
| **Thesis** | | | | |
| Active Niches | {list} | | | |
| Niches Activated This Quarter | {count} | | | |
| Niches Killed This Quarter | {count} | | | |

**Why this differs from weekly:** Investors want cumulative totals, conversion funnels, and thesis evolution — not weekly operational noise. This tab tells the story: "We're running a disciplined process, here's the proof."

**How to use:** When generating quarterly investor updates, pull directly from this tab. The data is already structured to drop into a narrative report.
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

Body contains the week's numbers in readable markdown format, plus a short diagnostic narrative structured around Stage 7:
- **Key metrics vs. goal** — Are we hitting 1 interesting deal/week?
- **System Throughput** — Is outbound volume sufficient? Are enough conversations being generated?
- **Signal Quality** — Are we reaching the right people? Where is conversion breaking down?
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

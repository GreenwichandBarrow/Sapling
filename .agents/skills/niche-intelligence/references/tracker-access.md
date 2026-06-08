# Industry Research Tracker Access

## Google Sheet
- **Sheet ID:** `1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins`
- **Account:** `kay.s@greenwichandbarrow.com`

## Reading Tabs

```bash
# Load 1Password-backed credentials first.
source scripts/op-env.sh

# Read whole tabs as transport, then resolve all business fields by header.
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "IDEATION" -a kay.s@greenwichandbarrow.com -j
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "WEEKLY REVIEW" -a kay.s@greenwichandbarrow.com -j
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "KILLED" -a kay.s@greenwichandbarrow.com -j
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "TABLED" -a kay.s@greenwichandbarrow.com -j
```

## Header Resolution Rules

Never use column letters or fixed column numbers as business logic. A range may be used only as a transport envelope when the CLI requires it. After reading a tab:

1. Find the header row by matching expected header names.
2. Normalize headers with lower-case, trimmed whitespace, and collapsed spaces.
3. Build a `header -> index` map.
4. Read and write values by header name.
5. If a required header is missing, stop with:
   `NICHE-INTELLIGENCE STOP: tracker missing header "{Header Name}" on "{Tab Name}"`

## Tab Column Structures

### WEEKLY REVIEW
| Header | Agent-Trigger? |
|--------|----------------|
| Rank | |
| Niche Hypothesis | |
| Current Status | ORANGE - triggers pipeline-manager, target-discovery |
| Outreach Channel | ORANGE - gates target routing (DealsX Email / Kay Email / Cold Call Only) |
| Score | |
| QSBS | |
| Target Pool | |
| Quick notes | |
| Red flags noted | |
| Start Date | |
| Days in Review | |

### IDEATION
| Header |
|--------|
| Section |
| Rank |
| Niche |
| Score (/3) |
| Margins |
| Recurring Revenue |
| AI Defensibility |
| Right to Win (Kay) |
| Network Access |
| Target Pool |
| Notes |
| QSBS |

### TABLED
| Header |
|--------|
| Niche Hypothesis |
| Start Date |
| Current Status |
| Quick notes |
| Red flags |
| Score |
| Why Tabled |
| What would need to change |
| Date tabled |

### KILLED
| Header |
|--------|
| Niche Hypothesis |
| Start Date |
| Current Status |
| Quick notes |
| Red flags |
| Score |
| Primary reason |
| Pattern learned |
| Date Killed |

## Writing to Tabs

**CRITICAL: IDEATION tab has section headers.** Do NOT blindly append — new niches must go in the correct section.

IDEATION section headers (separator rows under the `Section` header):
- `— INTERSECTION (Luxury + Compliance) —`
- `— LUXURY INFRASTRUCTURE —`
- `— COMPLIANCE INFRASTRUCTURE —`
- `— OTHER / WATCH LIST —`
- `— REVISIT (From Tabled/Killed — New Insights) —`

**Process for adding to IDEATION:**
1. First READ the full tab to find the correct section and its row range
2. Determine which section the niche belongs to (Intersection, Luxury, Compliance, Other)
3. Find the last row of that section (the row before the NEXT section header)
4. INSERT a new row at that position: `gog sheets insert {sheetId} "IDEATION" rows {row} -a {account} --count 1 -j`
5. WRITE the niche data by ordering values according to the current header map. Do not hard-code a write range that assumes fixed columns.

**Process for adding to WEEKLY REVIEW:**
1. Read the full WEEKLY REVIEW tab.
2. Build the header map from the current header row.
3. Create a row object keyed by headers, for example:
   `{"Rank": "6", "Niche Hypothesis": "Niche Name", "Current Status": "New", "Start Date": "{today}", "Score": "2.75", "Target Pool": "TBD", "Quick notes": "Promoted from Niche Intelligence"}`
4. Convert the row object to an ordered list using the current header map.
5. Append the ordered row.
6. Re-read the tab and verify the niche appears once.

## Drive Folder Operations

Drive is organized by status subfolders (mirrors tracker tabs):

| Status | Folder ID |
|--------|-----------|
| WEEKLY REVIEW | `1eq7FjekjFhkV0RoBfgr9n6AXPtENEenT` |
| IDEATION | `1fQNl6mogJW-6u5XJeE5uYQGsDPx495_O` |
| TABLED | `1_k_c1F11ZNrv4MilATFrURLHdkNx0kRx` |
| KILLED | `19xsNk5KTVHF2jb6m_li8IAGjcw34nlMX` |

```bash
# Create new niche folder under IDEATION (default for new niches)
gog drive mkdir "NICHE NAME" -a kay.s@greenwichandbarrow.com --parent 1fQNl6mogJW-6u5XJeE5uYQGsDPx495_O -j

# Upload one-pager to niche folder
gog drive upload "/path/to/file.pptx" -a kay.s@greenwichandbarrow.com --parent {folder_id}

# Move niche folder when promoted/tabled/killed
gog drive move {folder_id} --parent {target_status_folder_id} -a kay.s@greenwichandbarrow.com -j
```

## Promotion Logic

## Placement Logic

**ALL scored niches go to WEEKLY REVIEW with status "New".** There is no separate staging area. WEEKLY REVIEW is the single working list for the analyst call. Kay and her analyst decide what to pursue, table, or kill during the call. The nightly audit (pipeline-manager) moves Tabled/Killed niches to their respective tabs and re-sorts the list.

**IDEATION tab is archived.** It contains historical data but nothing new gets added there. All pipeline output goes to WEEKLY REVIEW.

**Nightly audit sort order (pipeline-manager):**
1. Active - Outreach
2. Active - Long Term
3. Under Review
4. New
(Tabled and Killed get moved to their own tabs overnight — never appear in sorted list)

**Status dropdown values (`Current Status` orange header):**
- New — just came through pipeline
- Under Review — analyst evaluating
- Active - Outreach — full target discovery (4-6/day) with owner outreach cadence (agent trigger)
- Active - Long Term — finishing in-flight outreach, no NEW targets but continue existing outreach sequences
- Tabled — moved to TABLED tab overnight
- Killed — moved to KILLED tab overnight

When adding to WEEKLY REVIEW:
1. Append row with Status = "New", Start Date = today, Score, Target Pool, Quick notes
2. Create Drive folder if one-pager exists
3. Upload one-pager to the folder

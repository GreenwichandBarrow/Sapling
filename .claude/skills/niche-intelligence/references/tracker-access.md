# Industry Research Tracker Access

## Google Sheet
- **Sheet ID:** `1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins`
- **Account:** `kay.s@greenwichandbarrow.com`

## Reading Tabs

```bash
# Read IDEATION tab (all rows)
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins -a kay.s@greenwichandbarrow.com --range "IDEATION!A:K" -j

# Read WEEKLY REVIEW tab
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins -a kay.s@greenwichandbarrow.com --range "WEEKLY REVIEW!A:J" -j

# Read KILLED tab (to exclude)
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins -a kay.s@greenwichandbarrow.com --range "KILLED!A:I" -j

# Read TABLED tab (can resurface if new data warrants)
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins -a kay.s@greenwichandbarrow.com --range "TABLED!A:I" -j
```

## Tab Column Structures

### WEEKLY REVIEW
| Col | Field | Agent-Trigger? |
|-----|-------|----------------|
| A | Rank | |
| B | Niche Hypothesis | |
| C | Current Status | ORANGE — triggers pipeline-manager, target-discovery |
| D | Outreach Channel | ORANGE — gates target routing (Salesforge / JJ-Call-Only / Salesforge+JJ / TBD) |
| E | Score | |
| F | QSBS | |
| G | Target Pool | |
| H | Quick notes | |
| I | Red flags noted | |
| J | Start Date | |
| K | Days in Review | |

### IDEATION
| Col | Field |
|-----|-------|
| A | Section |
| B | Rank |
| C | Niche |
| D | Score (/3) |
| E | Margins |
| F | Recurring Revenue |
| G | AI Defensibility |
| H | Right to Win (Kay) |
| I | Network Access |
| J | Target Pool |
| K | Notes |
| L | QSBS |

### TABLED
| Col | Field |
|-----|-------|
| A | Niche Hypothesis |
| B | Start Date |
| C | Current Status |
| D | Quick notes |
| E | Red flags |
| F | Score |
| G | Why Tabled |
| H | What would need to change |
| I | Date tabled |

### KILLED
| Col | Field |
|-----|-------|
| A | Niche Hypothesis |
| B | Start Date |
| C | Current Status |
| D | Quick notes |
| E | Red flags |
| F | Score |
| G | Primary reason |
| H | Pattern learned |
| I | Date Killed |

## Writing to Tabs

**CRITICAL: IDEATION tab has section headers.** Do NOT blindly append — new niches must go in the correct section.

IDEATION section headers (separator rows in column A):
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
5. WRITE the niche data to the newly inserted row: `gog sheets update {sheetId} "IDEATION!A{row}:K{row}" -a {account} --values-json '[["Section","Rank","Niche","Score","Margins","Recurring","AI","RTW","Network","Target Pool","Notes"]]' -j

```bash
# Append row to WEEKLY REVIEW (no sections — append is fine)
gog sheets append 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins -a kay.s@greenwichandbarrow.com --range "WEEKLY REVIEW!A:J" --values-json '[["6","Niche Name","2026-03-21","New - Pending Review","2.75","0","TBD","TBD","None identified","Promoted from IDEATION via Niche Intelligence"]]'
```

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
2. Active - Wind Down
3. Under Review
4. New
(Tabled and Killed get moved to their own tabs overnight — never appear in sorted list)

**Status dropdown values (orange header, column D):**
- New — just came through pipeline
- Under Review — analyst evaluating
- Active - Outreach — full target discovery (4-6/day) with owner outreach cadence (agent trigger)
- Active - Wind Down — finishing in-flight outreach, no NEW targets but continue existing outreach sequences
- Tabled — moved to TABLED tab overnight
- Killed — moved to KILLED tab overnight

When adding to WEEKLY REVIEW:
1. Append row with Status = "New", Start Date = today, Score, Target Pool, Quick notes
2. Create Drive folder if one-pager exists
3. Upload one-pager to the folder

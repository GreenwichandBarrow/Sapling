# Industry Research Tracker Access

## Google Sheet
- **Sheet ID:** `1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins`
- **Account:** `kay.s@greenwichandbarrow.com`

## Reading Tabs

```bash
# Read IDEATION tab (all rows)
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins -a kay.s@greenwichandbarrow.com --range "IDEATION!A:J" -j

# Read WEEKLY REVIEW tab
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins -a kay.s@greenwichandbarrow.com --range "WEEKLY REVIEW!A:I" -j

# Read KILLED tab (to exclude)
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins -a kay.s@greenwichandbarrow.com --range "KILLED!A:I" -j

# Read TABLED tab (can resurface if new data warrants)
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins -a kay.s@greenwichandbarrow.com --range "TABLED!A:I" -j
```

## Tab Column Structures

### WEEKLY REVIEW
| Col | Field |
|-----|-------|
| A | Rank |
| B | Niche Hypothesis |
| C | Start Date |
| D | Current Status |
| E | Score |
| F | Days in Review |
| G | QSBS |
| H | Red flags |
| I | Quick notes |

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
| J | Notes |

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

```bash
# Append row to IDEATION
gog sheets append 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins -a kay.s@greenwichandbarrow.com --range "IDEATION!A:J" --values '[["Section","Rank","Niche Name","2.50","High","High","Medium","Strong","Medium","Notes here"]]'

# Append row to WEEKLY REVIEW
gog sheets append 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins -a kay.s@greenwichandbarrow.com --range "WEEKLY REVIEW!A:I" --values '[["6","Niche Name","2026-03-21","New - Pending Review","2.75","0","TBD","None identified","Promoted from IDEATION via Niche Intelligence"]]'
```

## Drive Folder Operations

```bash
# Create new niche folder under Industry Research parent
gog drive mkdir "NICHE NAME" -a kay.s@greenwichandbarrow.com --parent 1tiAc7lVveBwi_DlYcFUX2tFP6FVwYKmQ

# Upload one-pager to niche folder
gog drive upload "/path/to/file.pptx" -a kay.s@greenwichandbarrow.com --parent {folder_id}
```

## Promotion Logic

A niche should be promoted from IDEATION to WEEKLY REVIEW when:
1. Its score exceeds the lowest score currently in WEEKLY REVIEW, OR
2. It scores 2.50+ (/3 normalized) on the quick scorecard AND has strong Right to Win + Network Access

When promoted:
1. Add row to WEEKLY REVIEW with Start Date = today, Status = "New - Pending Review"
2. Remove from IDEATION tab (or mark as promoted)
3. Create Drive folder under parent
4. Upload one-pager to the new folder

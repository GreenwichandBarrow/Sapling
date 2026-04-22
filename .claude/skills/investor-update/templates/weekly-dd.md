# Weekly DD Update — Template

**Purpose:** Deal-specific weekly update materials for investor group meetings during post-LOI due diligence. Triggered by any deal in the Attio Active Deals pipeline at "LOI Signed" stage.

**Golden reference:** load most recent file in `../examples/weekly-dd/` as anchor. Folder will be empty until G&B closes a first LOI.

**Save location:** inside the deal's Drive folder at `ACTIVE DEALS / {Company} / NOTES / Week {N} DD Update {M.DD.YY}`.

---

## Structure

```
DD UPDATE: {Coded Company Name} — Week {N}
Week ending: {YYYY-MM-DD}

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
- {If approaching kill/go decision, flag it explicitly}
```

## Voice + Content Rules

- Direct, factual, concern-first when concerns exist
- Use coded company names (first 2-3 letters) consistent with quarterly-deck coding
- No em dashes
- Every OPEN ITEM has an owner + due date, no naked bullets
- DECISION POINT section MUST be present every week — either says "no decision needed this week" or flags the specific kill/go moment

## Data Sources

- Deal folder: `ACTIVE DEALS / {Company} /` all subfolders (CIM, FINANCIALS, LEGAL, DILIGENCE, CORRESPONDENCE)
- Attio Active Deals entry: current stage + all custom attributes
- Financial model: latest `.xlsx` in FINANCIALS subfolder
- Scorecard: latest in `brain/outputs/` for this company
- Prior week's DD update: last file in deal folder's NOTES/

## Validation Gates

- [ ] All 6 sections populated (Status, This Week, Financial Model, Open Items, Next Week, Decision Point)
- [ ] Every open item has owner + due date
- [ ] Coded company name (not real name) in the title
- [ ] Revenue/EBITDA numbers consistent with latest model
- [ ] File saved to deal folder's NOTES/ subfolder
- [ ] Slack notification to investor group channel after save

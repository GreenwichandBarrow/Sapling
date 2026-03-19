# Target Discovery — Drive Locations

## LINKT TARGET LISTS folder
- **Folder ID:** 1WfbzezRkD7Kr0FOA76y99x5wV8lwRkVc
- **Path:** G&B Shared Drive > OPERATIONS > LINKT TARGET LISTS
- **URL:** https://drive.google.com/drive/folders/1WfbzezRkD7Kr0FOA76y99x5wV8lwRkVc

## Master Sheet (one per niche sprint)

**Naming:** "{Niche} - Target List"
**Created once** at niche sprint activation. All Linkt runs append to the same sheet. Do NOT create new sheets per run.

### Tab 1: Active
Targets being outreached. Kay approved, JJ calling, emails going out. New Linkt results append here.

### Tab 2: Passed
Targets Kay passed on. Rows move here when Kay marks "Pass" in Col O. Pass reason preserved. Not deleted — may revisit if ICP shifts. This tab is the dataset for "why did we pass" analysis during ICP calibration.

## Column Layout (both tabs, same structure)

### Linkt Data (Claude populates)
A: **Source** — dropdown: Linkt, Association Directory, Conference List, Web Research, Intermediary Referral, Broker
B: Company | C: Website | D: Headquarters | E: Industry | F: Employees | G: Revenue | H: Ownership | I: Owner Name | J: Owner Title | K: Email | L: Phone | M: LinkedIn (Owner) | N: LinkedIn (Company)

### Kay's Review (Kay populates)
O: **Kay Decision** — dropdown: Approve, Pass, Maybe
P: **Pass Reason** — dropdown: Wrong Size, PE-Backed, Wrong Industry, Wrong Geography, Already Contacted, Not a Fit, Other
Q: **Kay Notes** — freeform

### JJ's Calls (JJ populates)
R: **Call Status** — dropdown: Not Called, Connected, Voicemail, Callback Requested, Not Interested, Wrong Number
S: **Call Date**
T: **Call Notes** — freeform
U: **Owner Sentiment** — dropdown: Interested, Neutral, Not Selling, Hostile

### ICP Calibration (Claude auto-calculates)
V: **ICP Match** — TRUE if Kay=Approve AND JJ call was positive (Connected + Interested/Neutral)
W: **ICP Miss Reason** — auto-populated from Kay's Pass Reason or JJ's negative outcomes

## Row Lifecycle

1. **Claude** appends new target to **Active** tab (cols A-N)
2. **Kay** reviews → marks Approve, Pass, or Maybe in Col O, reason in Col P, notes in Col Q
3. If Pass → **Claude** moves row to **Passed** tab (with all data preserved)
4. If Approve → row stays in Active, outreach-manager picks it up for Day 1 email
5. **JJ** fills in call columns (R-U) as he calls
6. **Claude** calculates ICP Match (Col V) and ICP Miss Reason (Col W) from Kay + JJ data

## Column Ownership (who writes what)

| Owner | Columns | Description |
|-------|---------|-------------|
| **Claude** | A-N | Source + all Linkt enrichment data |
| **Kay** | O-Q | Decision, reject reason, notes |
| **JJ** | R-U | Call status, date, notes, sentiment |
| **Claude** | V-W | ICP calibration (auto-calculated) |

**Rule:** Never write to another owner's columns. Claude does not fill Kay's or JJ's columns. Kay does not fill JJ's columns. JJ does not fill Kay's columns.

## Dropdown Data Validation

Set on sheet creation:
- Col A (Source): Linkt, Association Directory, Conference List, Web Research, Intermediary Referral, Broker
- Col O (Kay Decision): Approve, Pass, Maybe
- Col P (Pass Reason): Wrong Size, PE Backed, Wrong Industry, Wrong Geography, Already Contacted, Not a Fit, Other
- Col R (Call Status): Not Called, Connected, Voicemail, Callback Requested, Not Interested, Wrong Number
- Col U (Owner Sentiment): Interested, Neutral, Not Selling, Hostile

## ICP Calibration Metrics (every 2 weeks, from weekly-tracker)

Calculated from Active + Passed tabs combined:
- **Kay Accept Rate:** Approve / (Approve + Pass) — target: 70%+
- **JJ Connection Rate:** Connected / total called
- **Positive Sentiment Rate:** (Interested + Neutral) / Connected
- **ICP Accuracy:** ICP Match TRUE / total targets
- **Top Pass Reasons:** ranked frequency of Pass Reason values
- **Credit Efficiency:** credits spent / Kay-approved targets

Output: Google Doc in LINKT TARGET LISTS folder + vault file + Slack notification with key metrics.

## Archived Raw Exports (pre-sprint format)

These are older Linkt exports from before the master sheet format. Kept for reference:
- Specialty Insurance Compliance: 1fsHYA8ljX6rXT-HIb69ZelJZiW3h38C925ci3i8E3cg
- NYC Tri-State Private OpCo: 1_FB15QIRNb23ASPjv-0YsJprdYXufy1x0lo5UNiYg8Y
- NYC Tri-State Private Business: 12Ty5T1V6JqnTI744JvxiN5Bjp7Pwr_-KUJJjEDXnNjE
- NYC Area M&A Targets - Succession: 1D84V1Oiiwqhxug27BXUQ_TjMnLKVuygZhgq6un4fuFQ
- Tri-State M&A Targets: 1vde_LKe44IcDhdmWq96sfo8TnX53_EjQZfnC0hRkRf4
- NYC Radius - Private B2B Owner: 1jVF7aX06boU--D-xXV4YXjO4Ztt3nPwqAyMYuN2W9CA
- Linkt ICP Configurations: 1w88mO5Mgtt0a-1rb7488RcUIzE1scD-jgrdwL_gm9ck

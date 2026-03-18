# Target Discovery — Drive Locations

## LINKT TARGET LISTS folder
- **Folder ID:** 1WfbzezRkD7Kr0FOA76y99x5wV8lwRkVc
- **Path:** G&B Shared Drive > OPERATIONS > LINKT TARGET LISTS
- **URL:** https://drive.google.com/drive/folders/1WfbzezRkD7Kr0FOA76y99x5wV8lwRkVc

All Linkt exports and target lists live here. One sheet per ICP/niche run.

## Sheet Format (single "Targets" tab per sheet)

### Linkt Data Columns (Claude populates)
A: Company | B: Website | C: Headquarters | D: Industry | E: Employees | F: Revenue | G: Ownership | H: Owner Name | I: Owner Title | J: Email | K: Phone | L: LinkedIn (Owner) | M: LinkedIn (Company)

### Kay's Review Columns (Kay populates)
N: **Kay Decision** — dropdown: Approve, Reject, Maybe
O: **Reject Reason** — dropdown: Wrong Size, PE-Backed, Wrong Industry, Wrong Geography, Already Contacted, Not a Fit, Other
P: **Kay Notes** — freeform

### JJ's Call Columns (JJ populates)
Q: **Call Status** — dropdown: Not Called, Connected, Voicemail, Callback Requested, Not Interested, Wrong Number
R: **Call Date**
S: **Call Notes** — freeform
T: **Owner Sentiment** — dropdown: Interested, Neutral, Not Selling, Hostile

### ICP Calibration Columns (Claude calculates from Kay + JJ data)
U: **ICP Match** — auto-calculated: TRUE if Kay=Approve AND JJ call was positive (Connected + Interested/Neutral)
V: **ICP Miss Reason** — auto-populated from Kay's Reject Reason or JJ's negative outcomes

No separate tabs for companies and people. Always combined on one row.
No separate JJ call list sheet — JJ works directly from this same sheet.

## Dropdown Data Validation

When creating a new sheet, set data validation on these columns:
- Col N (Kay Decision): Approve, Reject, Maybe
- Col O (Reject Reason): Wrong Size, PE-Backed, Wrong Industry, Wrong Geography, Already Contacted, Not a Fit, Other
- Col Q (Call Status): Not Called, Connected, Voicemail, Callback Requested, Not Interested, Wrong Number
- Col T (Owner Sentiment): Interested, Neutral, Not Selling, Hostile

## ICP Calibration Metrics (calculated at sprint check-in)

From these columns, Claude calculates:
- **Kay Accept Rate:** Approve / (Approve + Reject) — target: 70%+
- **JJ Connection Rate:** Connected / total called
- **Positive Sentiment Rate:** (Interested + Neutral) / Connected
- **ICP Accuracy:** ICP Match TRUE / total targets
- **Top Reject Reasons:** ranked frequency of Reject Reason values
- **Credit Efficiency:** credits spent / Kay-approved targets

These metrics feed the sprint check-in and drive ICP adjustments.

## Existing Linkt Export Sheets
- Specialty Insurance Compliance: 1fsHYA8ljX6rXT-HIb69ZelJZiW3h38C925ci3i8E3cg
- NYC Tri-State Private OpCo: 1_FB15QIRNb23ASPjv-0YsJprdYXufy1x0lo5UNiYg8Y
- NYC Tri-State Private Business: 12Ty5T1V6JqnTI744JvxiN5Bjp7Pwr_-KUJJjEDXnNjE
- NYC Area M&A Targets - Succession: 1D84V1Oiiwqhxug27BXUQ_TjMnLKVuygZhgq6un4fuFQ
- Tri-State M&A Targets: 1vde_LKe44IcDhdmWq96sfo8TnX53_EjQZfnC0hRkRf4
- NYC Radius - Private B2B Owner: 1jVF7aX06boU--D-xXV4YXjO4Ztt3nPwqAyMYuN2W9CA
- Linkt ICP Configurations: 1w88mO5Mgtt0a-1rb7488RcUIzE1scD-jgrdwL_gm9ck

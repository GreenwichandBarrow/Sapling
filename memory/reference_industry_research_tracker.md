---
name: Industry Research Tracker & One-Pager System
description: Google Sheets tracker ID, Drive folder IDs, one-pager template, and scoring methodology for the Friday Niche Intelligence workflow
type: reference
---

## Industry Research Tracker (Google Sheets)
- **Sheet ID:** `1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins`
- **Tabs:** WEEKLY REVIEW, IDEATION, TABLED, KILLED
- **Link:** https://docs.google.com/spreadsheets/d/1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins

### WEEKLY REVIEW Tab Columns
A=Rank, B=Niche Hypothesis, C=Start Date, D=Current Status, E=Score, F=Days in Review, G=QSBS, H=Red flags, I=Quick notes

### IDEATION Tab Columns
A=Section, B=Rank, C=Niche, D=Score (/3), E=Margins, F=Recurring Revenue, G=AI Defensibility, H=Right to Win (Kay), I=Network Access, J=Notes

### TABLED Tab Columns
A=Niche Hypothesis, B=Start Date, C=Current Status, D=Quick notes, E=Red flags, F=Score, G=Why Tabled, H=What would need to change, I=Date tabled

### KILLED Tab Columns
A=Niche Hypothesis, B=Start Date, C=Current Status, D=Quick notes, E=Red flags, F=Score, G=Primary reason, H=Pattern learned, I=Date Killed

## Industry Research Drive Folder
- **Parent folder ID:** `1tiAc7lVveBwi_DlYcFUX2tFP6FVwYKmQ`
- **KILLED subfolder:** `19xsNk5KTVHF2jb6m_li8IAGjcw34nlMX`

### Active Niche Folders (Top 5)
| Niche | Folder ID | One-Pager |
|-------|-----------|-----------|
| Trust Administration | `1kStCWA4JQ31tzsOMqume2XEeeoaT0fWi` | Trust Administration March 2026.pptx |
| Estate Management | `1mGXkPKF98KsNIR5vRrEl4SZaOqGUrCPa` | Estate Management March 2026.pptx |
| Trade Credit Insurance | `1WDy3v08zPxR7oGpTQ0B3rUdrgCV5qy7V` | Trade Credit Insurance March 2026.pptx |
| Insurance Producer License Compliance | `1pjOHPBLxly2PsUnd8hmxVZOsfboRB7hH` | Insurance Producer License Compliance March 2026.pptx |
| Art Insurance Brokerage (in SPECIALTY INSURANCE) | `18Rv_m76SPsVZgUv6-yHCKH-sv1Cnwmm7` | Art Insurance Brokerage March 2026.pptx |

### Other Active Folders
| Folder | ID | Status |
|--------|----|--------|
| ESTATE PLANNING | `1-upIdD7QrGZUQIcqq1jrHsCJ7s-KiVO0` | Active (trust admin related) |
| ART STORAGE | `1yFRqoTgTXViZdk6Lg6gQzOgOd1PpYFjF` | Tabled |

## G&B Scorecard File
- **Drive ID:** `1Zen-snMZKmKUjnihrn9O6AdIYMb2B_Zm`
- **Local copy:** `brain/library/internal/scorecard/G&B Scorecard Industry & Company 7.24.25.xlsx`
- **Tabs:** G&B INITIAL SCREEN, G&B TARGET LIST, TEMPLATE (industry scorecard template), G&B INDUSTRY SCORECARD (summary), G&B OPPTY SCORECARD (company), plus completed scorecards for Home Services, Estate Planning, B2B Licensing, Spec Insurance, PostOp SaaS, Art Platform, Art Storage, Escrow SaaS
- **Full structure:** `.claude/skills/niche-intelligence/references/scorecard-structure.md`

## One-Pager Template
- **Template file:** Customs Bonds pptx format (single slide, table-based)
- **Drive ID:** `1FfZ_r3IJAnd0AMqAcKCGd3anGyGGFV-6`
- **Local copy:** `brain/library/internal/one-pager-template/customs-bonds-template.pptx`
- **Sections:** Title, Assessment/Status, Industry Overview, Industry Thesis, Macro Trends & Growth Drivers | Risks & Concerns, Economics & Pricing | Competitive Landscape, Customers | Barriers to Entry, Key Success Factors, Exit
- **Built with:** python-pptx library
- **Full reference:** `.claude/skills/niche-intelligence/references/one-pager-template.md`

## Scorecard Methodology (8 criteria, 1-3 each, max 24, normalized to /3)
1. **Growth** — Market CAGR vs GDP. 1=below, 2=GDP-2x, 3=2x+
2. **Margins** — EBITDA. 1=<15%, 2=15-25%, 3=25%+
3. **Recurring Revenue** — 1=project-based, 2=moderate, 3=80%+ recurring
4. **Fragmentation** — 1=consolidated, 2=moderate, 3=highly fragmented
5. **Mission Criticality** — 1=nice-to-have, 2=important, 3=mission-critical/regulatory
6. **Tech Disruption Risk** — (3=LOW risk) 1=high disruption, 2=moderate, 3=protected
7. **Right to Win** — Kay's specific advantage. 1=none, 2=moderate, 3=strong
8. **Acquirability** — Retirement-age founders in $2-10M range. 1=unlikely, 2=some, 3=many

## Friday Niche Intelligence Workflow
Every Friday, use this system to:
1. Scan IDEATION tab for niches ready for promotion/demotion
2. Check TABLED tab for niches with new information that warrants revisiting
3. Score any new niches added during the week
4. Recommend promote/table/kill decisions for Monday review
5. If a niche is promoted: create one-pager, create Drive folder, move to WEEKLY REVIEW
6. If killed/tabled: move from IDEATION to appropriate tab, move Drive folder if exists

**Why:** This is the system that feeds Kay's acquisition pipeline. Without weekly niche intelligence, the top 5 stagnates and opportunities are missed.

**How to apply:** The Niche Intelligence skill should read the tracker, cross-reference with market signals, and produce a concise Friday briefing with recommended actions.

# Conference Prep — Drive Locations

## Conference Pipeline Spreadsheet
- **Sheet ID:** 1bdf7xlcRjOTlVkuXA-HNGOQgjtDRmVN2RfDf9aUsDpY
- **URL:** https://docs.google.com/spreadsheets/d/1bdf7xlcRjOTlVkuXA-HNGOQgjtDRmVN2RfDf9aUsDpY/edit
- **Tabs:**
  - `Pipeline` — All active conferences: Discovered through Attended, including Register Only. Single view.
  - `Skipped` — Archive for conferences Kay passes on. Same columns.
- **Columns:** Date of Conference (A), Event Name (B), Location (C), Travel (D), Niche (E), Registration Cost (F), Reg Deadline (G), Est. Attendees (H), Attendee List (I), Website (J), Status (K), Agent Rec (L), Decision (M), Notes (N), Agent Notes (O)
- **Dropdowns:** Status (K), Agent Rec (L), Decision (M) all have data validation dropdowns
- **Claude fills:** A-L, O. **Kay fills:** M, N.

## Drive Folders

### CONFERENCES (parent folder)
- **Folder ID:** 18H0L-5UgHObt_0Reb6YlRshbWakEozk5
- **Path:** G&B Shared Drive > RESEARCH > CONFERENCES
- **URL:** https://drive.google.com/drive/folders/18H0L-5UgHObt_0Reb6YlRshbWakEozk5

### Existing Conference Subfolders
- FRIEZE LA: 1aDP7GjLDDoblQnPYK690z2ag6QAZnbim
- DELOITTE: 1B9G5wX4aIrsfCDDHkY1XbE4O1GTUcsfa
- ARCS: 1BberBHsqob5RNLkzDMe0pO61bh7VOHXK
- ESTATE PLANNING - NAEDC: 18Ju8lNrUB2K3zNkzvk2TZxo2SjNzwwTL

### Creating New Conference Folders
For each conference Kay registers for, create a subfolder:
```bash
gog drive mkdir "{CONFERENCE NAME}" --parent "18H0L-5UgHObt_0Reb6YlRshbWakEozk5" --json
```

Store in the folder:
- Attendee/exhibitor lists
- Conference slides and presentations
- Industry reports shared at the conference
- Pre-conference target list
- Post-conference debrief notes

### Conference Materials as Niche Research
Conference materials (slides, reports, whitepapers) are valuable niche research. Example: Deloitte conference provided a 500+ page art & finance report relevant to multiple niches. When ingesting conference materials:
1. Save to the conference folder
2. Cross-reference with Industry Research Tracker niches
3. Flag relevant findings for niche intelligence

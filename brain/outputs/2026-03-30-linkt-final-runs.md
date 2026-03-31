---
schema_version: 1.1.0
date: 2026-03-30
type: research
status: published
tags: ["date/2026-03-30", "output", "output/research", "status/published", "topic/target-discovery", "topic/linkt"]
---

# Linkt Final Runs - 5 Niche Search Results

## Summary

Ran 5 Linkt search tasks across all active niches on 2026-03-30. Only Art Insurance completed successfully. The other 4 niches (IPLC, Art Advisory, Art Storage, TCI) hit a Linkt platform bug where the ICP ID is not populated on the run document, causing all runs to fail with "ValueError: ICP ID not present on run the document".

## Art Insurance (COMPLETED)

- ICP: 69cb1a2d7b20beb08475ec21 (Art Insurance Brokerage Acquisition Target)
- Runs: 2 batches, both COMPLETED
- Batch 1 run ID: 69cb1da87b20beb08475ec43 -- 45.5 credits, 41 entities, 163 min
- Batch 2 run ID: 69cb1da97b20beb08475ec44 -- 50.5 credits, 43 entities, 114 min
- Total credits: 96.0
- Results: 26 companies, 24 people
- Sheet: Art Insurance - Target List (15M76-gpcklwc47HDXIwyFC9Tj8K4wDOor4i0uxCYyHQ) -- new sheet created from template
- All 26 companies written to Active tab with owner contact info where available

### Notable companies found

- Bruce Gendelman Company ($11.3M, West Palm Beach FL)
- Century Risk Advisors ($11M, Boca Raton FL)
- Ross and Yerger ($18-22M, Jackson MS) -- may exceed buy box
- Webb Insurance Agency ($8.4M, St. Charles MO)
- Felton Berlin and Erdmann ($7M, Wakefield MA)
- Personal Risk Management Solutions ($6M, New York NY)
- Cambridge Insurance Advisors ($5.25M, Shelton CT)
- Butwin Insurance Group ($5.4M, Great Neck NY)

## IPLC v3 (FAILED - Platform Bug)

- ICP: 69cb26e07b20beb08475ec6c
- Task: 69cb26e17b20beb08475ec6f
- Error: ValueError: ICP ID not present on run the document
- Attempts: 4 separate execution attempts, all failed with same error
- Credits consumed: 0
- Existing sheet data: 28 companies from web research already on sheet

## Art Advisory v3 (FAILED - Platform Bug)

- ICP: 69cb26e27b20beb08475ec71
- Task: 69cb26e27b20beb08475ec74
- Error: ValueError: ICP ID not present on run the document
- Attempts: 3 separate execution attempts, all failed
- Credits consumed: 0
- Existing sheet data: 29 companies from web research already on sheet

## Art Storage v3 (FAILED - Platform Bug)

- ICP: 69cb26e47b20beb08475ec76
- Task: 69cb26e57b20beb08475ec79
- Error: ValueError: ICP ID not present on run the document
- Attempts: 3 separate execution attempts, all failed
- Credits consumed: 0
- Existing sheet data: 29 companies (Attio + enrichment) already on sheet

## TCI v3 (FAILED - Platform Bug)

- ICP: 69cb26e67b20beb08475ec7b
- Task: 69cb26e67b20beb08475ec7e
- Error: ValueError: ICP ID not present on run the document
- Attempts: 3 separate execution attempts, all failed
- Credits consumed: 0
- Existing sheet data: 29 companies from association/FCIA/EXIM directories already on sheet

## Credits Summary

- Art Insurance: 96.0 credits
- IPLC: 0
- Art Advisory: 0
- Art Storage: 0
- TCI: 0
- Total: 96.0 credits

## Linkt Platform Bug Details

When executing tasks linked to ICPs created on 2026-03-31, the Linkt platform does not copy the icp_id from the task document to the run document. The run starts with icp_id null, and when the search flow tries to read the ICP configuration, it fails.

Evidence:
- Art Insurance ICP (69cb1a2d, created 2026-03-31 00:49) works -- runs have icp_id populated
- All v3 ICPs (69cb26e0 through 69cb26e6, created 2026-03-31 01:44) fail -- runs always have icp_id null
- Tried: empty body, with prompt, with task_config, creating fresh ICPs from scratch -- all fail identically
- The ICP, task, and sheet documents are all correctly created and linked; the bug is in the run creation pipeline

## Next Steps

1. Try running the 4 failed searches from the Linkt web dashboard at app.linkt.ai
2. If that fails, contact Linkt support about the ICP ID bug
3. Art Insurance results are ready for review on the new target list sheet
4. IPLC, Art Advisory, Art Storage, and TCI sheets still have web research data that can be used for outreach while Linkt is down

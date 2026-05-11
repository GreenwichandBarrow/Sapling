---
name: Always test integrations end-to-end before relying on them
description: Linkt API was never properly validated - ICPs created but search runs never confirmed to return results
type: feedback
---

Never mark an integration as "tested" until a full end-to-end test proves it works: input → processing → output verified.

**Why:** Linkt API was listed as tested on March 20 but the ICP-to-search-run flow was never validated. When we tried to burn 263 credits across 5 niches, every single run failed with "ICP ID not present" and "company sheet not found" errors. Zero credits consumed. Zero results. The skill was built on an untested foundation.

**How to apply:**
- For any API integration: create a test record, run the full workflow, verify output, delete the test record
- "I created the ICP" is not a test. "I created the ICP, ran a search, got 10 companies back, verified they match the criteria" is a test.
- Health-monitor should check that integrations produce actual results, not just that API keys authenticate
- Before building a skill around a tool, prove the tool works first
- Add to health-monitor: Linkt search run validation (submit test search, verify entities returned)

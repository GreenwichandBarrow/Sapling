---
name: Claude plans, Kay executes — default collaboration split
description: For sensitive-access tasks Kay prefers planning from Claude + manual execution by herself rather than granting backend access
type: feedback
originSessionId: 4bdde090-de44-4ba3-971a-ad1a0b83d208
---
For tasks involving new access grants, OAuth scope expansion, third-party integrations, or anything touching personal account security, default to a split-workflow pattern:

- **Claude owns:** planning, analysis, taxonomy design, click-by-click recipe writing, tracking progress, cross-account cross-reference tables
- **Kay owns:** the actual clicks — OAuth consent, settings changes, bulk operations in native UIs

**Why:** Post-Salesforge spam incident (April 5, 2026), Kay is rightly conservative about expanding access surface. Her rule: "When Google says no, I listen." The cost of granting access is asymmetric — easy to grant, hard to fully unwind if compromised. Whereas manual execution with a written recipe is slightly slower but fully reversible at every step.

**How to apply:**
- Before proposing OAuth/API/credential access expansion, first check whether the task can be decomposed into Claude-plan + Kay-execute
- When Kay surfaces "I'm worried about overexposing accounts," pivot immediately — don't argue, don't lobby for access
- Honestly distinguish risk profiles (e.g., "gog is your own OAuth, not a third party") so Kay decides with full info, but respect her call without pressure
- Default deliverable when in split mode: cross-reference chart/table + step-by-step recipe Kay can execute in native UIs
- Exception: if backend access has already been granted and proven safe, continue using it — this rule is for NEW access requests

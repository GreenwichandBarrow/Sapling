---
name: When skill output contradicts Kay's lived knowledge, instrument is suspect
description: If a scan-skill returns thin/empty results in a domain Kay knows well, default prior is "instrument is broken" not "reality is thin." Investigate the skill before accepting the output.
type: feedback
originSessionId: 4d4166cd-0bb3-4a20-887c-1f29801ff285
---
When a network-scan, relationship-scan, or domain-scan skill produces output that contradicts Kay's direct knowledge of the domain, the default prior is that the instrument (skill, data, matcher, tokenization) is broken — NOT that reality is thin.

**Why:** On 2026-04-20, river-guide-builder Phase 3 calibration across 8 niches returned 5 total H-strength matches with 6 niches at zero. The subagent's recommendation was "criterion holds, proceed with writes." Kay rejected on lived-knowledge grounds: she has named network contacts in specialty-insurance, vertical-saas-luxury, and other niches that the scan missed. Suspected causes: substring-collision tokenization, H-criterion too strict (3yr + senior title), Attio enrichment coverage at 21% (388/1,825 records), and data spread across 4 sources (Apollo employment history, LinkedIn CSV, Attio fields, vault, Gmail) when the subagent only hit one.

**How to apply:**
- When presenting scan results to Kay, flag the gap explicitly: "This is what the scan returned. Does this match your expectation for the domain?" — don't just present the output and ask for a write greenlight.
- If Kay pushes back with "I know more people in this niche," TREAT THAT AS A DEFECT SIGNAL. Do not defend the scan. Investigation vectors to offer:
  1. Keyword matching precision (substring collisions, whole-word matching)
  2. Strength criterion (is it too strict? should include softer matches?)
  3. Data coverage (what % of the population has been indexed?)
  4. Source coverage (are all data sources being hit? e.g., LinkedIn CSV, Gmail, vault)
- Do not propose writes or ship output until the investigation resolves.
- **Corollary:** when scan output MATCHES Kay's expectation, that's a weak signal that instrument is healthy; still sanity-check false positives.

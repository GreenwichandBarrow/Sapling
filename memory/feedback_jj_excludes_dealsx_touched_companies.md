---
name: JJ weekly call-list excludes DealsX-touched companies (no double-touch)
description: 2026-05-11 operational rule. When building JJ Mon-Fri Call Log tabs (jj-operations-sunday), exclude companies flagged "Receiving DealsX outreach" in Agent Notes (col 18) on the Full Target List. Multi-channel touch is OK if sequenced; uncoordinated parallel phone+email is what is risky.
type: feedback
---

When building JJ weekly Mon-Fri Call Log tabs for any niche where DealsX is also active, **exclude companies whose Agent Notes (col 18) on the Full Target List contain "Receiving DealsX outreach"**.

**Why:** Uncoordinated phone+email touch from G&B + DealsX in the same week reads as spam. Per Kay 2026-05-11: "multi-touch can actually outperform single-channel if sequenced; uncoordinated touch is what is risky." Coordination requires visibility. 2026-05-11 baseline: 87 of JJ 182-company week pool overlapped DealsX 4 pest tabs (Specialty Pest & Environmental Service Good/Probable Fit + Valid variants). All 87 removed from JJ Mon-Fri 5/11-5/15 Call Logs and annotated on Full Target List.

**How to apply:**
- jj-operations-sunday must pre-filter Full Target List query to exclude rows where Agent Notes col 18 contains "Receiving DealsX outreach"
- Companies stay on Full Target List (do NOT delete the row); only the per-week Call Log tabs exclude them
- Annotation format: "Receiving DealsX outreach {YYYY-MM-DD}" written into Agent Notes col 18
- Rule only applies when DealsX is firing the same niche as JJ. As of 2026-05-11: Premium Pest Management (DealsX taxonomy: Specialty Pest & Environmental Service)
- **DO NOT send Sam an exclusion list.** Kay choice: pull from JJ side, not push to DealsX side
- Multi-touch sequencing (phone → email or email → phone with delay) is fine; only uncoordinated parallel touch is the failure mode

**Structural fix queued:** Bake the exclusion filter into `jj-operations-sunday/SKILL.md` so this does not require manual dedup every Sunday rollover. Until then, dedup runs as a Monday-morning subagent task after fresh tabs land.

**Related:**
- project_conference_platform_comms_via_intermediary_list.md — channel signal capture pattern
- feedback_brokers_stay_in_sheet_until_reply.md — sheet vs Attio promotion rule

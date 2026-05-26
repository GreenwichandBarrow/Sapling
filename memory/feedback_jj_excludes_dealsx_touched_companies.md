---
name: jj-weekly-call-list-excludes-dealsx-touched-companies-no-double-touch
description: "2026-05-11 operational rule. When building JJ Mon-Fri Call Log tabs (jj-operations-sunday), exclude companies flagged \"Receiving DealsX outreach\" in Agent Notes (col 18) on the Full Target List. Multi-channel touch is OK if sequenced; uncoordinated parallel phone+email is what is risky."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 37de3c90-d2d0-44f1-9b4b-ddb0727158c9
---

When building JJ weekly Mon-Fri Call Log tabs for any niche where DealsX is also active, **exclude companies whose Agent Notes (col 18) on the Full Target List contain "Receiving DealsX outreach"**.

**Why:** Uncoordinated phone+email touch from G&B + DealsX in the same week reads as spam. Per Kay 2026-05-11: "multi-touch can actually outperform single-channel if sequenced; uncoordinated touch is what is risky." Coordination requires visibility. 2026-05-11 baseline: 87 of JJ 182-company week pool overlapped DealsX 4 pest tabs (Specialty Pest & Environmental Service Good/Probable Fit + Valid variants). All 87 removed from JJ Mon-Fri 5/11-5/15 Call Logs and annotated on Full Target List.

**How to apply (2026-05-26 calibration — removal pattern replaces annotation-and-keep):**
- jj-operations-sunday must cross-reference the DealsX Drive Verticals sheet at BUILD TIME and **DELETE rows** from the per-week Call Log tabs that match DealsX-active companies. Annotation-and-skip is the OLD pattern, retired.
- Apollo enrichment of JJ rows happens AFTER dedup, never before — see [[feedback-outreach-channel-universes-separate]] item 5.
- Companies stay on Full Target List (do NOT delete the row from the Full Target List); only per-week Call Log tabs have rows removed.
- Annotation on Full Target List Col 18 = "Receiving DealsX outreach {YYYY-MM-DD}" is still maintained for audit; the per-week Call Log dedup uses the annotation as a fast-path signal (any annotated row never appears in a Call Log build) PLUS a fresh DealsX vertical-sheet cross-reference catches new additions.
- Match logic: lowercase, strip Inc/LLC/Corp/Co/Ltd, collapse punctuation. Strict-on-match (avoid false positives like `Pest Management Services Inc` vs `Pest Management Inc` which are different firms). If uncertain → KEEP + flag, never auto-delete.
- Rule applies when DealsX is firing the same niche as JJ. As of 2026-05-11+: Premium Pest Management (DealsX taxonomy: Specialty Pest & Environmental Service).
- **DO NOT send Sam an exclusion list.** Kay choice: pull from JJ side, not push to DealsX side.
- Multi-touch sequencing (phone → email or email → phone with delay) is fine; only uncoordinated parallel touch is the failure mode.
- **Snapshot before deletion:** `brain/context/rollback-snapshots/jj-dealsx-dedup-{ISO timestamp}.json` with full pre-deletion row dumps + match metadata.
- **Tab-floor flag:** if dedup drops a daily Call Log tab below 20 rows, surface to Kay loudly; do NOT auto-backfill (risks reintroducing overlap).

**Structural fix queued:** Bake the cross-reference + remove (not annotate-and-skip) filter into `jj-operations` Sunday rollover SKILL.md so this does not require a manual cleanup pass. Until then, dedup runs as an immediately-after-build subagent task.

**2026-05-26 cleanup precedent:** Tue/Wed/Thu/Fri Call Log tabs for week 5/24-5/30 were built without the cross-reference. A manual dedup pass removed 43 rows total (Tue 7, Wed 10, Thu 11, Fri 15). Fri dropped to 22 rows, 2 above the 20-floor — kept, not backfilled. Snapshot `jj-dealsx-dedup-2026-05-26T17-23-52Z.json`.

**Related:**
- project_conference_platform_comms_via_intermediary_list.md — channel signal capture pattern
- feedback_brokers_stay_in_sheet_until_reply.md — sheet vs Attio promotion rule

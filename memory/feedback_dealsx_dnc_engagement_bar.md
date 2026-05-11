---
name: DealsX DNC engagement-bar policy
description: For DealsX target-list dedup, DNC threshold = material engagement OR LinkedIn 1st connection. Attio stub-only records (zero email/call/meeting/LI tie) go to Sam.
type: feedback
originSessionId: cece2f47-c8d7-4430-af72-e9cfb7942006
---
**Rule:** When dedup'ing any DealsX target list against Kay's network, mark a row "DO NOT CALL" only if ANY of these signals are true:

1. **Material engagement** — at least 1 of:
   - Gmail thread (sent OR received) within last 24 months
   - Vault call note (`brain/calls/`) referencing the company or person
   - Granola transcript with anyone @ the company
   - Attio Person record with `status` ≠ `prospect` (anything past stub state)
   - Attio Company record with linked notes / interactions / pipeline membership

2. **LinkedIn 1st-degree connection** with anyone @ the company (parse from `Complete_LinkedInDataExport_03-23-2026.zip` or latest LI export in Drive).

**Stub-only Attio records** (record exists, but zero engagement signals + no LI connection) → **GO for DealsX, no DNC tag.**

**Why:** Sam @ DealsX collects success fees only on engaging "new" targets. Material engagement contaminates that claim AND risks brand damage if Sam touches a contact Kay was warming. But Attio stubs Kay was never going to chase herself are free intelligence — let Sam test the universe.

**How to apply:**
- Every DealsX target-list dedup pass uses this exact bar — not "any Attio record" (too strict; over-restricts Sam) and not "engagement only" (too loose; misses LI ties).
- Targets Kay explicitly handed Sam (in `operations/Target list/Deals X/...` folder) are pre-approved — dedup logic ignores them, no DNC tag regardless of engagement.
- **Marking convention on DealsX-owned sheets:** VISUAL-ONLY (red row background highlight, RGB ~0.96/0.65/0.65 across all populated columns). Do NOT write text into Sam's sheet's columns — Sam's team prefers non-destructive marking. The text reasoning lives in Kay's separate G&B-owned reference sheet (e.g. `G&B DealsX New Verticals (May) — DO NOT CALL list 5.5.26`, file id `1zxi7G-1oYBKv1yKzmqJaTzC5oGgkNV7iPfL1nMgEtkQ`) which mirrors the DNC list with full DNC reasoning per row. Sam's sheet just gets the visual highlight; Kay's mirror sheet gets the audit trail.
- For each dedup pass, also run a heuristic exclusion screen (PE/VC/captive/franchise/etc.) per Services Buy Box + Insurance Buy Box — separate from the engagement-bar check, additive in the same scratch field with `EXCLUDE — {reason}` prefix.

**Source:** Kay confirmed 2026-05-05 morning during DealsX New Verticals (May) dedup. Initial subagent pass over-flagged (65 matches via Attio existence alone); Kay refined to engagement-bar.

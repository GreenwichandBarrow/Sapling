---
name: Niche Network is bidirectional — river-guide-builder 3-phase
description: river-guide-builder is the single skill for Niche Network. 3 phases: ecosystem discovery + network cross-check + industry-experience scan. Attio writes OFF by default. Apollo-enriched Attio is the Phase 3 primary source.
type: feedback
originSessionId: c9463652-c8f2-4d3d-b096-737d00fef818
---
## Rule

river-guide-builder is the canonical skill for building Kay's "Niche Network" per active niche. Single unified skill with 3 phases, writing to three tabs on each target-list sheet:
1. **Associations** (orgs + events) — Phase 1
2. **River Guides** (named external contacts + network cross-check columns) — Phase 1 + Phase 2
3. **Network Matches** (people in Kay's network with industry-relevant work history) — Phase 3

**Why:** Kay's insight 2026-04-20 — the skill becomes robust only when bidirectional. External discovery alone produces research lists; adding network cross-check (who does Kay already know?) + industry-experience scan (who in her network has industry work history?) turns research into warm-path maps.

## How to apply

- **Phase 1 categories (6 total):** Association Leaders, Industry CPAs, M&A Lawyers, Consultants, Adjacent Operators, Validation Contacts (lifted from retired niche-intelligence Step 5b on 2026-04-20)
- **Phase 2 engine:** reuse `warm-intro-finder` 5-source scan (LinkedIn CSV / Attio / Vault / Gmail / Investor network) verbatim per row
- **Phase 3 primary source:** Attio `nddl_apollo_employment_history` (Apollo-enriched). Fallback to LinkedIn CSV + Attio standard fields + vault + Gmail for un-enriched records
- **Apollo enrichment cadence:** ~500 credits before May 2 reset on highest-priority records (nurture_cadence → relationship_type → recent interactions → bulk), remaining records enriched post-May 2 reset
- **Niche keywords:** `.claude/skills/river-guide-builder/references/niche-keywords/{niche-slug}.yaml` — one file per active niche, manually curated, contains `keywords`, `negative_keywords`, `customer_segment_keywords`, `pe_platforms_to_exclude`, `sub_niches` where applicable
- **Attio writes OFF by default:** `ATTIO_WRITE_RIVER_GUIDES: false` + `ATTIO_TAG_NETWORK_MATCHES: false`. Flipping to true is a one-line config change. Kay decides when ready.
- **Existing Attio relationships are not surfaced as river guides** — the skill checks before appending, flags as "existing G&B relationship" in notes

## Related memory

- Associations-vs-people Attio distinction: associations don't feed Attio; named people COULD feed Attio (decision deferred).
- Retired validation-calls memory: niche-intelligence Step 5b sunset 2026-04-20. Historical `brain/outputs/*validation-contacts-*.md` files remain with `supersedes` frontmatter for record.

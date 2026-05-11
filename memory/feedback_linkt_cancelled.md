---
name: Linkt Subscription — active through 2026-05-30
description: Linkt subscription paid through 2026-05-30. Key at /tmp/linkt-key.txt. After 5/30, Apollo + web research takes over per target-discovery Phase 2.
type: feedback
originSessionId: c9463652-c8f2-4d3d-b096-737d00fef818
---
## Linkt Subscription Status (corrected 2026-04-20)

Linkt subscription is **paid through 2026-05-30**. NOT cancelled, NOT downgraded to Starter. Prior memory claiming Starter/invalidated was wrong — Kay clarified 2026-04-20.

**API key location:** `/tmp/linkt-key.txt` (as of 4/20). Should also be written to `scripts/.env.launchd` as `LINKT_API_KEY` for launchd runs. MCP block in `.mcp.json` pointed at `https://api.linkt.ai/mcp` with `x-api-key: ${LINKT_API_KEY}` header.

## Usage Note — Linkt is List-Building, Not Per-Domain Enrichment

Linkt's primary value is the **Search flow**: give it an ICP ("find NY-area pest businesses with $2M+ rev, owner-operated") and it discovers + enriches new companies. 1 credit per entity created.

Linkt is NOT well-suited for "here are 184 companies I already have — give me their owners." Tested 2026-04-20 with pest businesses: hit rate was 0% (fuzzy matches returned unrelated companies from Kay's prior Insurance ICP). **For per-domain owner enrichment, use Apollo `/people/match`** (list-builder skill).

**How to apply:**
- Active niche SPRINT → Linkt for list generation. Create ICP → sheets → task → execute → export enriched entities.
- Weekly owner enrichment on existing target list → Apollo (via list-builder skill), not Linkt.
- After 2026-05-30 → if Kay doesn't renew, Phase 2 falls back to Apollo primary + web research. Target-discovery SKILL.md already documents this fallback. Update the "through 2026-05-30" references when subscription changes.

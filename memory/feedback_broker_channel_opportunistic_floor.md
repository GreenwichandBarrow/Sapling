---
name: Broker channel needs separate buy-box (Kay 5/3 + Megan Lawlor pattern)
description: For broker/intermediary-curated deal-flow channels, build a SEPARATE Broker-Channel Buy Box — short criteria, geographic, industry-agnostic. Do NOT relax the financial floor on the existing buy-box. Geography window pending Kay's lock.
type: feedback
originSessionId: e8a79c7a-dbe3-484f-a6ad-c576b0b6d195
---
For deal-aggregator and any future deal-screen logic on broker/intermediary channels:

**Rule:** Broker-channel deals (sources where `Type` is `Email-only broker`, `Newsletter blast`, `Advisory + Deal Platform`, `Marketplace + Email`, `Email-only broker + Buyer Portal`) need a SEPARATE buy-box document with a SHORT list of criteria — geographic but industry-agnostic.

**Why:** Per Megan Lawlor 4/1 call (`brain/calls/2026-04-01-megan-lawlor.md`): "Broker deals reviewed opportunistically. Filters for 2-3 industries but scans broadly." Megan's actual LOI was a Marble & Granite Fabrication business — totally outside her thesis, came through a Twitter-broker intro, geographic + financial fit was the whole gate. Kay's 5/3 framing: separate buy-box for brokered search with shorter criteria — geographic but industry agnostic.

**How to apply (when Broker-Channel Buy Box doc is built):**
- Geography is a HARD gate (Kay's commute radius for Deal 1 CEO role — geography window pending Kay's lock; baseline NY/NJ/CT/PA from existing Axial filter)
- Industry is AGNOSTIC — any industry passing the financial + geographic + hard-exclude gates qualifies for review
- Financial floor stays at $2M EBITDA practical floor (supports $300K salary + debt service per `feedback_deal_screen_300k_salary_15pct_margin`) — NOT relaxed
- Hard-excludes intact: California (`feedback_no_california`), lending (`feedback_no_lending`), carve-outs (`feedback_no_carveouts`), fashion (per 1/15 Guillermo call)
- Margin floor 15% (no change)
- Owner-transition viable (30-90 day handover, no irreplaceable founder dependency)
- Revenue band relaxed from $5-50M strict to informational-only

**REJECTED approach (Kay 5/3):** Lowering EBITDA floor to $1M with relaxed margin gate (12%) on broker channel. Reason: financial floor is a hard constraint driven by $300K salary + debt service math. It doesn't change by source. A $1M EBITDA broker-channel deal still doesn't pencil. Surfacing sub-floor deals as "opportunistic matches" creates noise, not signal.

**STATUS (as of 2026-05-03):** Concept locked. Geography window NOT YET locked. Broker-Channel Buy Box doc NOT YET built. Until built, broker-channel listings still route to the matching Services/Insurance/SaaS niche buy-box.

**Codified in:** `.claude/skills/deal-aggregator/SKILL.md` channel-type routing section (notes Type for each match, `OPPORTUNISTIC` channels marked for future routing once broker buy-box doc exists).

**Open loop:** Kay to lock geography window (NY/NJ/CT/PA baseline + maybe MA, FL?) before broker buy-box build can proceed.

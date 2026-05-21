---
name: teaser-silent-review-industry-scoped
description: "Confidential teasers/CIMs are silent input only. Never echo specifics in chat. Industry-level deliverables (one-pagers, scorecards) must contain only public/general industry data, not company-specific figures from a private teaser."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f96a6428-58cf-4329-bea3-44eaf20df596
---

Rule: When Kay points me at a confidential teaser, CIM, NDA-protected doc, or any private deal file, **review it silently**. Use it ONLY to calibrate broader industry analysis — never to populate company-specific data into industry-level deliverables, and never to echo specifics in chat.

**Why:** Two independent failures on 2026-05-19 with the Project Drone teaser:
1. I quoted teaser specifics (revenue, EBITDA, customer concentration, advisor names) directly in the chat transcript. Kay's correction: "Do not publish this information here. this is a secret teaser. you should have reviewed silently."
2. I was about to weave teaser-specific facts (90% renewal rate, 32% EBITDA, 80% of Colombia's sugarcane belt) into the niche one-pager body. Kay's correction: "this is a specific company, please make sure the information in the one pager is the broader industry and not related to this one pager specifically."

Teasers/CIMs operate under NDA-equivalent norms. Echoing specifics into the chat leaks them into the conversation transcript (which lives in `~/.claude/projects/...`, git-syncable). Embedding them in non-deal-specific files conflates company analysis with industry analysis and corrupts the niche-level deliverable.

**How to apply:**
- When given a confidential teaser/CIM/private deal doc → download, read silently, do not paste specifics back in chat. State only generic confirmations: "teaser reviewed, integrating into analysis."
- For industry-level outputs (niche one-pagers, scorecards, industry-research-tracker entries): use ONLY public/general industry data from web research, USDA/industry reports, association data. Never insert company-specific revenue, EBITDA, customer concentration, advisor names, founder names, or hectare figures from a private teaser.
- Allowable: use the teaser as silent calibration to TIGHTEN the niche framing. Generic category signals like "specialty crops support per-hectare SaaS with multi-year contracts" are fine; the same statement with named company / specific %s is not.
- For deal-specific deliverables (company scorecard, deal one-pager, post-call notes for the SPECIFIC company): teaser specifics may appear, but the file must live in the deal's own private folder (e.g., `ANALYST / Active Deals / Project {Name}/`), not in industry-level locations.
- If unsure whether a fact is "industry-broad" or "teaser-specific": treat it as teaser-specific. The cost of over-redacting is far lower than the cost of leaking.

Related: [[feedback_strip_user_context_from_public_copy]] (LENS vs CONTENT distinction), [[feedback_outreach_no_strategy_leaks]] (no thesis leaks in outreach).

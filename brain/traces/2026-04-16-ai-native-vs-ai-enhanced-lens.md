---
schema_version: 1.2.0
date: 2026-04-16
type: trace
task: Evaluate whether Kovr.ai invalidates G&B's vertical SaaS thesis
had_human_override: true
importance: critical
target: process
tags: ["date/2026-04-16", "trace", "pattern/ai-native-vs-enhanced", "domain/thesis"]
---

# Decision Trace: AI-Native vs AI-Enhanced as Disruption Lens

## Context

Kay shared Kovr.ai (AI-native cyber compliance automation platform, $3.6M seed). She asked whether it invalidated G&B's vertical SaaS thesis. My first answer: "Healthcare Regulatory Compliance SaaS faces existential pressure within 24-36 months; acquire + modernize is the answer." Kay pushed back, citing her own experience ripping out her tech stack and rebuilding AI-native on Claude Code.

## Decisions

### Disruption Lens Framing

**AI proposed:** Buy legacy compliance SaaS and "layer AI on top" — an acquire-and-modernize play that captures the AI-productivity upside inside the acquired business.

**Chosen (by Kay's override):** The "buy + bolt AI on" playbook produces **AI-enhanced**, not **AI-native**. Customers who experience AI-native products (the gap is 10x, not 1.5x) migrate away from AI-enhanced regardless of the acquirer's modernization effort. The structural difference is architectural, not feature-level.

**Reasoning:** Kay's lived experience is the authority here. She didn't incrementally add Claude to Asana/Notion/Linear — she tore them out and rebuilt from scratch on Claude Code + skills + vault. She knows experientially that bolting AI onto legacy code is fundamentally different from rebuilding architecture with AI as the primary interface. The pattern is the same as cloud-native beating cloud-enhanced (SaaS beating hosted legacy), and mobile-native beating mobile-responsive.

**Pattern:** #pattern/ai-native-vs-enhanced

### Thesis Portfolio Implication

**AI proposed (corrected in same turn):** Downgrade all documentation-heavy compliance niches uniformly.

**Chosen:** Split the thesis portfolio by workflow type:
- **Physical-workflow verticals (MORE conviction):** vet, funeral, childcare, estate mgmt, PT, fertility, senior living, premium pest. Software is connective tissue for humans doing bodily/operational tasks. AI can't do the actual work. Structurally protected from AI-native disruption.
- **Documentation/rules-heavy verticals (stress-test required):** Healthcare Regulatory Compliance SaaS, Digital Accessibility Compliance, Behavioral Health Practice Mgmt (documentation layer), Home Health Agency Software (documentation layer). AI-native entrants can eat these.

**Reasoning:** The disruption lens doesn't just remove conviction from some niches — it *adds* conviction to others. The split isn't "all SaaS is exposed" but "workflow type determines exposure." Kay's earlier principle (conviction from structure, per [[feedback_conviction_from_structure]]) is preserved and extended.

### Thesis Survival

**AI proposed:** The thesis is at risk; rethink.

**Chosen:** The thesis stands broadly. ~10-11 of 15 active niches are structurally defended. Only ~4 need AI-disruption stress tests before acquisition. This is a portfolio-strengthening insight, not a thesis-killing one.

## Learnings

- **Distinguish AI-enhanced vs AI-native** as the primary lens when evaluating any software acquisition target. They are architecturally different products, not feature-set variants.
- **Physical-workflow vs documentation-workflow** is the split that determines AI-native disruption exposure in vertical SaaS. Apply this filter to every niche evaluation.
- **Kay's lived experience is authoritative on disruption patterns.** She rebuilt her stack AI-native and knows the migration economics firsthand. When she pushes back on "acquire + modernize" framings, trust her.
- **"Conviction from structure" now includes workflow-physicality as a sub-dimension.** Not just "labor-intensive + fragmented + aging-owner" but also "does the work happen in the physical world or in documents/rules?"
- **Future agents evaluating niches must apply the physical-vs-documentation split explicitly.** Do not treat all vertical SaaS niches as equally exposed to AI-native entrants.

## Targets for Calibration

- **CLAUDE.md or niche-intelligence skill:** Add AI-native disruption screen to niche evaluation criteria (physical vs documentation workflow)
- **deal-evaluation skill:** When evaluating a software target, add "AI-enhanced vs AI-native" screen on the incumbent product
- **Memory:** Add `feedback_ai_native_vs_enhanced_lens` to MEMORY.md so this distinction is surfaced in future thesis conversations

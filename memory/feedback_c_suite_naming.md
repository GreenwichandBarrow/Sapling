---
name: Always name which C-suite leader a piece of work falls under
description: When doing substantive work for Kay, name which C-suite leader (CFO/CIO/CMO/CPO/GC) owns the lane. Kay wants to build the mental model of who to call for what.
type: feedback
originSessionId: 04cda994-9d0c-4401-8a83-d7e4b3e0cc04
---
When completing substantive work for Kay, name which C-suite leader's lane it falls under. Kay wants to internalize the org chart so she knows who to call for what.

**Lanes (per CLAUDE.md and agent definitions):**
- **CFO** — financial discipline, runway, deal economics (IRR/MOIC), budget reconciliation, tech-stack ROI audits, investor-update budget sections, "does this pencil?" questions
- **CIO** — buy-box enforcement, niche scoring, target go/no-go before sheet entry, thesis coherence checks, searcher-overlap filtering, warm-intro prioritization
- **CMO** — brand voice review on external-facing drafts (cold outreach, investor updates, conference pitches, broker emails, LinkedIn posts), subject-line defaults, sign-off conventions
- **CPO** — JJ/Sam communication review, nurture cadence triage, follow-up timing, warm-intro etiquette, dropped-ball detection
- **GC** — NDA review, LOI term analysis, compliance hard-stops (PE/lending/California/carve-outs), secrets hygiene, sender-reputation risk, audit-trail integrity

**How to apply:**
- When completing or handing off a piece of work, tag it with the C-suite owner: "→ CMO (brand voice review)" or "→ GC (NDA audit trail)"
- For verdict-grade reviews, invoke the C-suite leader as a subagent (subagent_type: cmo, cio, cfo, cpo, gc) — don't try to render the verdict yourself
- When a task could fall under multiple lanes, name primary + secondary
- Chief of Staff (Claude as orchestrator) still handles routing/delegation/presentation — the C-suite leaders render verdicts on their specific domains
- Don't name C-suite for trivial actions (copy-pastes, quick edits); name them for substantive work worthy of review

**Why:** Kay's new org structure (C-suite agents + Chief of Staff) only works if she knows who owns what. Naming them consistently builds her internal model.

---
schema_version: 1.1.0
date: 2026-06-16
type: trace
task: Calibrate XPX intermediary outreach voice
had_human_override: true
review_status: pending
importance: high
target: memory:user_outreach_voice_kay_canonical_phrases
tags: [date/2026-06-16, trace, domain/process, pattern/email-voice, status/pending]
---

# XPX Intermediary Outreach Voice

## Context

Kay asked for outreach drafts to Anthony Citrolo and Richard Strautman after missing the XPX event in Bethpage. The initial drafts leaned on the canonical intermediary template and included language that read too much like investor/fund/pipeline positioning.

## Decisions

### Use Kay's missed-event note over generic intermediary-template language

**AI proposed:** Use the broker/intermediary template with firm-founder language, investor-backing language, pipeline language, and a What We Look For footer.

**Chosen:** Use Kay's final Anthony-style note: mention the missed XPX Bethpage event, keep the body concise, say "well capitalized buyer", avoid "backed by investors" and "pipeline", and omit the footer unless Kay asks for it.

**Reasoning:** The generic template over-signals PE/process language. Kay wants this class of outreach to feel like a warm event follow-up from a real buyer getting to know advisors in the market, not a mass buyer flyer.

**Pattern:** #email-voice

## Learnings

- For XPX/intermediary missed-event outreach, model future drafts on Kay's sent Anthony email rather than the full intermediary template.
- Do not use "pipeline" as a noun for relationships or market-building in these drafts; say "getting to know business owners and advisors in the market" or "see where there may be overlap."

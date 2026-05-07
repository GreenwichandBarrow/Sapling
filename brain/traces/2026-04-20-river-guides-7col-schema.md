---
schema_version: 1.1.0
date: 2026-04-20
type: trace
title: "River Guides tab schema: 7-col validation-call-intake format"
had_human_override: true
importance: medium
target: "skill:river-guide-builder"
tags: ["date/2026-04-20", "trace", "topic/river-guide-builder", "topic/schema", "pattern/match-real-intake-format"]
---

# River Guides Tab Canonical Schema

## Context

River-guide-builder Phase 1 produced hundreds of individual river-guide contacts across 8 niches. Different agents produced different schemas:
- 6 niches: 11 columns (Name / Title / Firm / Email / LinkedIn / Category / Score / Notes / + 3 Phase 2 cols)
- Coffee: 14 cols with numeric 1-3 scoring + Suggested Approach
- Estate Mgmt: 16 cols
- Art Storage: 18 cols with Category in column A
- Commercial Cleaning: 16 cols with Category in column A

Kay needed a single canonical schema, Name-first, that matched her actual validation-call intake format.

## Decisions

### Schema selection
**AI proposed sequence:**
- First: 13 columns including Priority + Known Contact + Source + Evidence + Outreach Status + Outreach Notes (JJ-call-log-adjacent)
- Second: 8 columns after Kay pointed to her validation-call format — Name / Title / Firm / Category / Phone / LinkedIn / Location / Why
- Third: iterate on Kay's feedback

**Chosen (Kay-proposed):** 7 columns — `Name | Title | Firm | Location | LinkedIn | Industry | Why`.

**Reasoning:** Kay showed me an example of how she laid out validation-call contacts:
> Morgan Stanley Private Wealth Management
> Contact: Anna Raginskaya
> Title: Vice President, Financial Advisor, Blue Rider Group
> Phone: N/A
> LinkedIn: linkedin.com/in/raginskaya
> Location: New York, NY
> Why: Art-focused wealth advisor at Morgan Stanley's Blue Rider Group...

Kay's refinement:
- Name must be first column (her explicit requirement)
- Industry instead of Category (Industry = vertical tag like "Wealth Management" for filtering; Title implicitly carries role-in-ecosystem)
- Drop Phone (most river guides don't have public phone)
- Drop Email at the intake stage (public email often isn't available; add when engaging)
- Drop Score / Priority / Phase 2 tracking columns (these are internal heuristics, not intake data)

**Pattern:** #pattern/match-real-intake-format — when a user has an existing intake format for a type of record, mirror it in the system schema. Don't invent a research-centric schema when a human-use-centric one exists.

### Population rule for known contacts
**Chosen:** If a river guide is already a known contact (in Kay's Attio / direct network), **don't populate Location/LinkedIn** — Kay has that data. Fill only Name + Title + Firm + Industry + Why.

**Reasoning:** Kay: "If there are already a contact or river guide — I don't need contact info, I have it." Avoids duplicating effort and reminds future agents that the sheet is a working surface, not a contact database.

### Category dropped, kept as Phase 1 research bucket only
**Chosen:** The 6 ecosystem categories (Association Leader / Industry CPA / M&A Lawyer / Consultant / Adjacent Operator / Validation Contact) remain as PHASE 1 RESEARCH BUCKETS — used to guide what types of people to find — but are NOT persisted as a sheet column. Industry column covers the sortable dimension.

**Reasoning:** Kay: "We have Title and Industry. I think we are covered." Title + Industry together encode the ecosystem position implicitly.

### Template propagation
**Chosen:** Add River Guides tab (7-col schema) to G&B Target List Template (Drive ID `1wIK4Jv56QIZejcmpq-gGrCWAPe07eJWUbKsWTRwh778`) so new niches inherit it on creation.

## Learnings

- When a user has an existing intake format (narrative-style in their calls), the sheet schema should match it column-for-field. This preserves workflow continuity — Kay can paste call notes into rows without reformatting.
- Don't encode research-centric metadata (Score, Priority, Category) as columns unless the user sorts/filters by them. These are internal heuristics; keep them in prompts/code, not sheet schemas.
- Schema iterations cost cleanup time. Ask for the target intake format BEFORE drafting any column layout.

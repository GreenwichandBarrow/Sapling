---
schema_version: 1.1.0
date: 2026-04-23
type: trace
title: "Buy-Box Paragraph — Kay-Authored Replaces Claude-Drafted Version"
tags: ["date/2026-04-23", "trace", "topic/buy-box-paragraph", "topic/outreach-voice", "topic/seller-psychology", "topic/conference-engagement-skill", "topic/messaging-encoding"]
had_human_override: true
importance: high
target: outreach
people: ["[[entities/kay-schneider]]"]
companies: []
---

# Trace: Buy-Box Paragraph — Kay-Authored Version Replaces Claude Draft

## Context

While building the `conference-engagement` skill, Claude drafted a buy-box reference paragraph for the intermediary post-conference template. The draft used third-person institutional voice ("Greenwich & Barrow is a single-family private investment office acquiring..."), followed standard buy-box structure (EBITDA band, sector, hold orientation, seller fit), and closed with "we are often a good home for sellers who want to pick their buyer."

Kay reviewed the rendered template in a Google Doc, then wrote her own version mid-session and asked Claude to use it "for future reference." The new paragraph differs in several non-obvious ways.

## Decisions

### Kay's version replaces Claude's across skill Snippets tab, review doc, and local markdown
**Claude proposed:**
> For context on what we are looking for: Greenwich & Barrow is a single-family private investment office acquiring founder-led or family-owned businesses in the US, typically $2-5M EBITDA, with a long-term hold orientation. We focus on operationally critical B2B services businesses where the current owner is thinking about succession, legacy, or stepping back. We move quickly, hold indefinitely, and care more about fit with the owner than maximizing multiples, so we are often a good home for sellers who want to pick their buyer.

**Kay wrote (and locked):**
> For context on what we are looking for: I am looking to acquire a founder-led or family-owned business in the US (NY Metro would be a plus), ~$2-5M EBITDA, with a long-term orientation. Currently looking at operationally critical B2B services where the current owner is thinking about succession. We move quickly, aim to retain existing employees, and are able to partner with a seller on terms in a customized way.

## Alternatives Considered

- **Keep Claude's third-person institutional voice.** Rejected — sounds fund-like even though the word "fund" was avoided. Violates `feedback_never_say_fund_or_lead` in spirit if not letter.
- **Hybrid (Kay's first person + Claude's closing line about "good home for sellers who want to pick their buyer").** Not explicitly considered by Kay, but the closing was dropped — likely too salesy for a first-touch post-conference email.
- **Geography as hard filter (not "a plus").** Rejected by Kay's phrasing "NY Metro would be a plus." Soft-signal preserves optionality to engage targets outside tri-state without appearing inconsistent.

## Reasoning

Kay's version encodes several strategic choices that a future agent could easily undo:

1. **First-person voice ("I am looking to acquire...").** This shifts G&B from an institutional buyer to a personal one. Matches the Alain Wertheimer / Wedgwood archetype in `project_gb_charter`. Legacy-motivated sellers want to pick a *person*, not a fund — so the outreach must sound like a person.

2. **"NY Metro would be a plus."** Soft preference, not hard filter. Signals geographic focus without excluding off-thesis deal flow that intermediaries might still send. Also resonates with NY Metro intermediaries who feel the preference is in their favor (this applies to XPX's entire audience).

3. **"Currently looking at."** Time-bounded framing. Signals active search without locking G&B into a permanent sector definition. Lets Kay pivot thesis without the paragraph going stale.

4. **"Aim to retain existing employees."** Employee-retention line addresses a founder-seller anxiety that Claude's version missed entirely. Founders care about their team; surfacing retention directly signals Kay is a responsible steward.

5. **"Able to partner with a seller on terms in a customized way."** This is the load-bearing sentence. It encodes flexibility on post-close transition obligations (the seller psychology insight surfaced at XPX — see [[traces/2026-04-23-seller-short-transition-matters]]) WITHOUT quoting the anxiety back at sellers. A founder reading this hears "short transition if I want it, longer if I want it" — but the paragraph never mentions transitions explicitly. This is the craft.

6. **Dropped "fit with the owner" + "pick their buyer" closing.** Kay's version ends on a fact (capability) rather than a pitch (benefit). Sellers reading this feel less marketed-at.

## Why This Trace Matters

A future agent running `conference-engagement` (or any outreach skill) will encounter the Snippets tab with this paragraph. Without this context, a well-meaning agent could:
- "Improve" the paragraph by adding a closer ("...and we'd love to be the home for your business").
- "Modernize" by switching to "we" throughout for consistency.
- "Clarify" by naming the transition-flexibility point explicitly.
- "Scope down" by removing the NY Metro soft preference because it seems limiting.

Each of those changes would degrade the paragraph. This trace exists so agents understand the encoding BEFORE they edit.

## Key Insight

**The buy-box paragraph is not descriptive copy — it is a strategic signaling document.** Every sentence does work. "A plus" (not "required"), "currently looking" (not "focused on"), "customized terms" (not "flexible on transition"), first-person "I" (not institutional "we"). Kay wrote this deliberately. Do not regenerate it without explicit re-authorization.

This also establishes a precedent: when Kay authors language directly, it supersedes Claude's draft across all artifacts, and the language itself becomes part of the institutional knowledge — not just the fact that Kay approved it.

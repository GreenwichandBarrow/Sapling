---
schema_version: 1.1.0
date: 2026-04-21
type: trace
had_human_override: true
importance: high
target: process
tags: ["date/2026-04-21", "trace", "pattern/ask-before-drafting-felt-content", "topic/peer-group-brief-prep", "topic/wsn", "topic/disclosure-calibration"]
---

# Decision Trace: Felt, Not Framed — H/L/L Methodology for Peer-Group Briefs

## Context

Prepping Kay's High/Low/Lesson content for the WSN Month 2 group call. Claude's first-pass drafts consistently failed and required multiple rewrites across all three sections:

- **HIGH** — First draft "tools-for-walls framework from Guillermo" rejected ("feels not as much of an eye opener as you feel"). Second version landed only after Claude asked "what's the moment you've replayed in your head?" — Kay dictated the answer; Claude reshaped into speakable form.
- **LOW** — First draft "still no LOI at month 14, 'more no than yes' in my system" rejected as oversharing. Second draft with "not sleeping" + investor-pang rejected ("feels like oversharing with a group I've only met once"). Final landed as two composed sentences — macro niche spin + engine warm-up lag. Each iteration Claude went too raw; Kay pulled back.
- **LESSON** — Went through five rejected drafts (rank-on-external-criteria, portfolio-thinking, operator-identity, act-on-peer-advice-faster, network-was-the-asset) before landing on "don't pause pipeline to build systems." Each rejection flagged a distinct failure mode: not fresh to the 3-week window, oversharing, factually wrong, not actually a lesson Kay learned.

## Decisions

### Asking open questions before drafting felt content
**AI proposed (implicitly, multiple times):** Infer Kay's High/Low/Lesson from session history — strategic wins, operational setbacks, framework unlocks. Draft speakable versions from that inferred content.
**Kay's response (across multiple turns):** "High — feels not as much of an eye opener as you feel." ... "I didn't feel like the lesson is indicative about the 3 weeks since the last meeting." ... "Option B is not a lesson I have learned."
**Chosen:** When Claude finally switched to asking one open question ("What's a moment you've replayed in your head?" / "What's the thing you learned this month you'd want another searcher six months behind you to hear?"), Kay dictated rich, specific, felt content that Claude then reshaped. Every successful H/L/L landing used this flow.
**Reasoning:** Strategic content (what Claude can infer from session state) and felt content (what Kay actually carries into a peer conversation) are not the same. Strategic wins may be already-internalized by the time Kay speaks them — they don't feel like "eye-openers" in the moment, even if they were important decisions. Felt content requires Kay to surface what's emotionally weighted, and the only reliable way to extract that is to ask.
**Pattern:** #pattern/ask-before-drafting-felt-content

### Calibrating vulnerability to group maturity and Kay's relative position
**AI proposed:** Drafts trending toward full disclosure — "not sleeping," investor-update pang, self-referential LOI gap ("three of you have LOIs in motion — I don't").
**Kay's response:** "It feels like I'm oversharing with a group I have only met once. Everyone else has deals in the pipeline except me."
**Chosen:** Strip all emotional disclosure from the LOW. Keep it strategic and composed. Rewrite the question to lead generously with the group's progress instead of Kay's personal lack.
**Reasoning:** Two factors drive the disclosure ceiling: (1) meeting cadence — month-two peer groups ≠ established advisors. The group hasn't yet earned the right to the rawest material. (2) Relative position — when Kay is the only person in the room without a visible LOI, leading with lack costs dignity without buying help. Composed-but-honest > vulnerable-and-exposed when the audience is peers who are outpacing you.
**Pattern:** #pattern/disclosure-ceiling-by-group-maturity-and-relative-position

### Question framing — lead generously, not with self-lack
**AI proposed:** "Last time we all admitted to being 'more no than yes.' Since then, three of you have LOIs in motion — I don't. What actually moved you from analysis to action on the LOIs you've submitted?"
**Kay's rewrite:** "As many of you have LOIs in motion, I'd love to ask you to share what actually moved you from analysis to action on the LOIs you've submitted? Was it a specific seller moment, an investor pushing you, or a deliberate rule you set for yourselves?"
**Chosen:** Kay's wording. Opens with their progress, invites them to teach, strips the self-referential gap.
**Reasoning:** Same pattern as the LOW — when you're the one without the thing, the generous question earns help; the self-referential question earns pity. Same content, different positioning, radically different room response.

## Alternatives Considered

1. **Keep inferring from session state, iterate via Kay corrections** — what Claude defaulted to for the first several rounds. High token cost, high correction volume, low success rate on first-pass.
2. **Ask a single open question, draft from Kay's dictation** — switched to this mid-session and it worked immediately on every section.
3. **Pre-generate 3-4 options per section and let Kay pick** — tried this on the LESSON, still produced rejected drafts because the options were built from Claude's inference, not Kay's felt experience.

## Reasoning

Peer-group H/L/L and personal-reflection content differ structurally from operational content. For operational content (drafts, emails, analyses), Claude can infer from session state and produce strong first-passes — the relevant facts are in the vault. For reflective content, the content Kay needs is in her head and her body, not the session log. Inference substitutes for dictation at the cost of accuracy.

The three failure modes observed tonight — strategic-framing-as-eye-opener, vulnerability-too-raw-for-room, lessons-not-fresh-to-window — all trace to the same root cause: Claude drafting before asking.

## Why This Trace Matters

For any future brief prep involving personal reflection, peer-group content, or emotionally-weighted material, default to this flow:

1. **Ask first.** One open question per section: "What's the moment you've replayed? / What sat on your chest? / What would you tell a searcher behind you?"
2. **Listen for Kay's own words.** The phrases she dictates are the raw material.
3. **Reshape, don't rewrite.** Preserve her phrasing. Tighten for time. Strip vendor names by default unless explicitly approved.
4. **Apply the disclosure filter before presenting.** Check meeting cadence, Kay's relative position in the room, audience model (traditional searcher vs. HoldCo-aware advisor), and any fund-structure constraints. When in doubt, pull back.
5. **For questions Kay will ask the group:** lead generously with their progress/expertise, never with Kay's gap.

Applicable skills: `meeting-brief`, any future `peer-group-brief` skill, `investor-update` (for reflection sections), WSN-specific prep.

## Key Insight

Inference produces strategic content. Dictation produces felt content. Peer-group briefs require felt content. One open question before drafting beats five iterations of corrected drafts — every time.

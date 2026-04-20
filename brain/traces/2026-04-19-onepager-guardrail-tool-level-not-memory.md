---
schema_version: 1.1.0
date: 2026-04-19
type: trace
title: "One-pager purity rule enforced at tool level, not memory level"
tags: ["date/2026-04-19", "trace", "topic/artifact-purity", "topic/guardrails", "pattern/memory-vs-hook"]
had_human_override: true
importance: high
---

## Trigger

Kay corrected Claude for inserting personal/team-centric content (Kay's Milanese analyst right-to-win, Chanel structural parallel, Kay's hospitality network names) into the Specialty Coffee Equipment Service one-pager. Kay: "this is not the first time I have called that out so there needs to be a stop hook or guardrails set up to prevent this on the one pager in the future."

Critical phrase: "not the first time." Pattern repeated ≥3x, memory-only enforcement demonstrably insufficient.

## Decision

**Tool-level PreToolUse hook (via existing router framework), not memory alone.**

Implemented at `.claude/hooks/router/handlers/onepager_guardrail.py`. Blocks Write/Edit/MultiEdit tool calls on files matching niche-onepager path patterns when the content contains Kay-specific, team-specific, or Kay's-personal-framing patterns (Kay, Kay's network, analyst, CoS, Milanese, Wedgwood, Alain Wertheimer, JJ, G&B's right-to-win). Registered in the router's HANDLERS list so it fires on every Write/Edit.

## Alternatives Considered

- **Memory rule only** (`feedback_artifacts_pure_industry_analysis.md`). Rejected — Kay explicitly said memory alone insufficient ("not the first time"). A memory rule still depends on Claude remembering to check it on each write. The hook doesn't.
- **Prompt-level instructions** (CLAUDE.md addition). Same failure mode as memory — subject to Claude's self-discipline.
- **PostToolUse cleanup hook** (write then sanitize). Rejected — the purity violation is already in the git diff and vault snapshot by then.
- **Human review gate on every one-pager write.** Rejected — adds Kay friction on legitimate edits, violates `feedback_remove_kay_from_loop`.

## Reasoning

Memory rules work for behaviors Claude can self-enforce reliably. This pattern failed that test repeatedly (3+ corrections in a week). The governance principle:

> **When a correction has been given 3+ times on the same pattern, graduate the enforcement from memory to tool-level.**

The hook mechanism:
- Matches Write/Edit/MultiEdit tool calls
- Filters by file path (`brain/outputs/**/*(niche-onepager|one-pager|onepager)*.md`)
- Strips frontmatter + wiki-links before pattern matching (avoids false positives on auto-generated `people: [[entities/kay-schneider]]`)
- Returns `Decision.BLOCK` with a detailed reason citing the feedback memory file and the litmus test
- 7 unit tests pass (clean content passes; banned patterns blocked; wiki-link frontmatter safe; non-onepager paths skipped)

## Why This Trace Matters

Three-fold:

1. **Pattern-recognition precedent.** This is the first time in the G&B system that a repeated-correction pattern was escalated from memory to tool-level enforcement. Future agents observing similar repeated corrections should propose the same escalation (with Kay's approval) rather than accepting that "Claude will remember this time."

2. **Hook scope discipline.** The hook only fires on niche-one-pager files, not on validation-contacts files (which are legitimately Kay-specific) or strategic conversation transcripts. Enforcement matches the artifact type, not the topic. Future hooks should follow this narrow-scoping discipline to avoid over-blocking legitimate work.

3. **The strategic-context vs artifact-content distinction is load-bearing.** Kay's second correction in the same conversation sharpened the rule: strategic context (Chanel parallel, Milanese analyst) stays between Kay and Claude; artifacts are generic-acquirer-voice. The hook encodes this distinction in enforcement.

## Key Insight

**Memory rules are necessary but not sufficient for repeated violations. The 3x-correction threshold is the graduation criterion to tool-level enforcement.**

Future agents: if a correction has been given 3 or more times on the same pattern and memory is already in place, propose a hook rather than another memory entry. Otherwise the next occurrence will be the 4th correction.

## Related

- [[context/session-decisions-2026-04-19]]
- `memory/feedback_artifacts_pure_industry_analysis.md` (companion rule)
- `.claude/hooks/router/handlers/onepager_guardrail.py` (implementation)
- `.claude/skills/tracker-manager/SKILL.md` (applies same discipline to tracker operations)

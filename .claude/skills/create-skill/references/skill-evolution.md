# Skill Evolution Patterns

Skills are living systems, not static documents. They drift out of alignment with user preferences over 3-4 months unless designed for iterative change. This reference covers three patterns that prevent full rebuilds.

## Design Principle: Stable Core + Evolving Periphery

```
skill-name/
├── SKILL.md              ← STABLE (changes ~2x/year)
├── workflows/            ← STABLE (changes when new capability added)
├── references/           ← STABLE (domain knowledge, rarely shifts)
├── scripts/              ← STABLE (pure I/O, no business logic)
└── learnings.md          ← EVOLVES (every run can update this)
```

The SKILL.md and workflows define *what* the skill does. Every generated skill includes `learnings.md`, which captures execution knowledge that prevents repeating mistakes.

## Pattern 1: Skill-Level Learnings (`learnings.md`)

A file at the skill root that Claude reads before acting and updates after discovering an actionable execution learning.

### Structure

```markdown
# Learnings

Append entries in this parseable shape:

- date: YYYY-MM-DD
  trigger: What happened during execution
  issue: What failed, changed, surprised the agent, or upset the user
  resolution: What worked
  future_rule: What to do differently next time
```

### How It Works

1. Skill triggers → Claude reads `learnings.md` (if exists)
2. Learnings inform execution (preferences override defaults, gotchas prevent known failures)
3. During execution, Claude hits friction: repeated failed searches, changed data/tool structure, unexpected behavior, resolved errors, or a user correction/preference signal
4. After task completes → Claude appends one atomic, parseable entry
5. Next invocation → Claude reads updated learnings, is immediately smarter

### Rules for Healthy Learnings

- **Atomic entries**: One insight per entry. Specific enough to act on.
- **Date everything**: Learnings age. A preference from 6 months ago may be stale.
- **Structured fields**: Include `date`, `trigger`, `issue`, `resolution`, and `future_rule`.
- **Prune quarterly**: When re-reading, delete entries contradicted by newer ones.
- **40 lines max by default**: If it's growing past budget, some entries belong in references instead.
- **Never duplicate SKILL.md**: Learnings capture *discovered* knowledge, not *designed* behavior.
- **No task facts**: Do not save project facts, transient task details, or output content.

### When to Write a Learning

Write a learning when future runs should behave differently because the agent:
- Had to make many searches before finding the right path/query
- Realized a data, API, file, or tool structure changed
- Found unexpected behavior and resolved it
- Hit a repeatable command/tool failure
- Realized the user was frustrated or prefers a different execution style

Skip when the information is merely:
- A fact about the current project or client
- A temporary task decision
- A deliverable that belongs in the output
- Core behavior that belongs in SKILL.md or a reference

## Pattern 2: Living Knowledge Files

For skills with scripts that parse external data (APIs, exports, file formats), separate the knowledge from the code.

### The Problem

```python
# BAD: Business logic encoded in script
EXPECTED_COLUMNS = ["Company Name", "Revenue", "Employees"]
# When Grata renames "Company Name" to "Name" → script breaks
```

### The Solution

```
scripts/discover.py      ← Pure I/O: discovers structure, outputs JSON
references/schema.md     ← Living knowledge: what structure looks like
```

The script discovers reality. The knowledge file interprets it. Claude bridges the gap.

### Living Knowledge File Structure

```markdown
# [Format] Schema Knowledge

## Expected Structure
- Tab "Companies": columns A-Z (headers in row 1)
- Key columns: Name (A), Revenue (F), Employees (G), Founded (H)

## Known Variants
- "Company Name" → renamed to "Name" as of 2026-03
- "Annual Revenue" → sometimes "Revenue (USD)"

## Change History
- 2026-04-15: New column "AI Readiness Score" added at position AA
- 2026-03-01: "Company Name" renamed to "Name"

## Mapping Rules
- Match columns by position + sample values, not just header name
- If header unknown but position/data matches → add as variant
- If structure unrecognizable → STOP and ask user
```

### Self-Healing Flow

```
Normal:     discover.py → compare to schema.md → match → proceed
Changed:    discover.py → compare to schema.md → diff found →
            Claude identifies what changed → adapts mapping →
            UPDATES schema.md → proceeds
Unknown:    discover.py → compare to schema.md → unrecognizable →
            STOP → ask user → human confirms → update schema.md
```

The script never changes. The knowledge file evolves. Each run makes the next run more resilient.

## Pattern 3: When to Use Which

| Signal | Pattern | Example |
|--------|---------|---------|
| User corrects execution style | learnings.md | "Do not store task facts in learnings" |
| External format changes | Living knowledge file | API response adds new field |
| Script hits new error | learnings.md (Gotchas) | "openpyxl fails on chart sheets" |
| Search path finally found | learnings.md | "Repo logs actually live under orchestration workspace" |
| Entire tab structure changes | Living knowledge + escalation | Grata redesigns export |
| User wants different sources for this task only | Output/task plan, not learnings | "Use Salesforce for this mapping run" |

## Integrating Into Skill Design

When building a new skill, ask:
1. Every generated skill gets `learnings.md`
2. Does it parse external data? → Consider living knowledge file
3. Are user preferences likely to drift? → Capture execution preferences in `learnings.md`
4. Does it use scripts? → Scripts stay dumb; knowledge stays in `.md` files

### SKILL.md Integration

Add to your skill's process steps:

```xml
<process>
## Step 0: Load Context [LOW]
1. Read `learnings.md` if it exists
2. Apply any relevant preferences or gotchas to this run
...
## Step N+1: Capture Learnings [LOW]
Append one structured entry to `learnings.md` only when execution friction should change future runs. Include date, trigger, issue, resolution, and future_rule.
</process>
```

## Anti-Patterns

- **Bloated learnings**: exceeding the declared budget means some entries should be promoted to references or deleted
- **Learnings duplicating SKILL.md**: If it's core behavior, put it in the skill. Learnings are *discovered*, not *designed*
- **Learnings as task memory**: Project facts, client facts, and temporary task requirements belong in outputs or task plans, not learnings.
- **Script with embedded knowledge**: If the script "knows" what columns to expect, that knowledge belongs in a `.md` file
- **Never pruning**: Old entries contradict new ones. Date entries and prune when re-reading.
- **Learnings as a log**: Not a diary. Only actionable insights that change future behavior.

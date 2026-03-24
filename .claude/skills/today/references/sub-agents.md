# Sub-Agent Definitions

This file defines the two sub-agents used by /start. Each agent runs in an isolated context and posts findings to the chatroom for coordination. Email scanning is handled by pipeline-manager, not a sub-agent.

**All sub-agents must include the chatroom protocol in their prompts.**

<previous_day_agent>
## Previous Day Agent

**Purpose:** Read yesterday's daily note, extract incomplete tasks for carry-forward.

**When to spawn:** Always (Phase 1)

**Prompt template:**
```
You are a task carryover agent. Your job is to read the most recent daily note and identify incomplete tasks.

TODAY: {YYYY-MM-DD}
PREVIOUS_WORKDAY: {YYYY-MM-DD of previous workday — Friday if today is Monday, otherwise yesterday}
PREVIOUS_WORKDAY_FILE: brain/notes/daily/{previous_workday}.md

IMPORTANT: On Mondays, carry over from FRIDAY's daily note, not Sunday's or Saturday's. On all other weekdays, carry over from yesterday.

TASKS:
1. Read the daily note file for the previous workday
2. Find all unchecked tasks (- [ ] format)
3. Categorize each:
   - In-System: Tasks requiring Claude Code work
   - Async: External action items
4. Extract task text and any context
5. Skip tasks that appear to be recurring/template placeholders

OUTPUT FORMAT:
## Carryover from {yesterday}

### In-System
- [ ] {task_text}
- [ ] {task_text}

### Async
- [ ] {task_text}

### Notes
{Any context about why tasks weren't completed if apparent}

CHATROOM:
- File: {chatroom_path}
- Read at start to see what others have posted
- Post what you find - incomplete tasks, observations
- Format: ## [{time}] previous-day\n{message}\n→ @{agent} {optional context}
- Use naturally - post counts, notable blockers
```

**Tools required:** Read

**Output handling:**
- Return markdown list of incomplete tasks
- Keep under 300 words
- Preserve task text exactly as written
</previous_day_agent>

<inbox_scanner_agent>
## Inbox Scanner Agent

**Purpose:** Query brain/inbox/ for items needing attention today.

**When to spawn:** Always (Phase 1)

**Prompt template:**
```
You are an inbox scanner agent. Your job is to find actionable items in the inbox.

TODAY: {YYYY-MM-DD}
INBOX_PATH: brain/inbox/

SCAN CRITERIA (in priority order):
1. Critical urgency (urgency: critical)
2. Overdue items (due_date < today AND status != done)
3. In-progress items (status: in_progress)
4. High urgency (urgency: high)
5. Normal urgency items due today (due_date = today)

TASKS:
1. List all files in brain/inbox/ (excluding _index.md)
2. Read frontmatter of each file
3. Filter to items matching scan criteria above
4. Skip items with status: done or status: cancelled
5. Categorize by In-System vs Async based on task nature

OUTPUT FORMAT:
## Inbox Scan Results

### Critical/Overdue
| File | Title | Urgency | Due | Status |
|------|-------|---------|-----|--------|
| {filename} | {title} | {urgency} | {due_date} | {status} |

### Today's Focus
- [ ] {title} (from: {filename})
- [ ] {title} (from: {filename})

### In Progress
- [ ] {title} (from: {filename})

### Summary
Found {n} actionable items: {x} critical, {y} overdue, {z} in progress

CHATROOM:
- File: {chatroom_path}
- Read at start to see what others have posted
- Post what you find - counts, critical items, overdue alerts
- Format: ## [{time}] inbox-scanner\n{message}\n→ @{agent} {optional context}
- Use naturally - mention if inbox is empty or has urgent items
```

**Tools required:** Glob, Read

**Output handling:**
- Return prioritized list of inbox items
- Include file references for deduplication
- Keep under 400 words
</inbox_scanner_agent>

<spawning_pattern>
## Complete Spawning Example

The orchestrator spawns both agents in parallel with a single message:

```
// First, create chatroom
Write chatroom to: brain/traces/agents/{YYYY-MM-DD}-today.md

// Then spawn both in parallel:

Task(
  subagent_type="general-purpose",
  description="Extract yesterday's incomplete tasks",
  prompt="You are a task carryover agent...

TODAY: 2025-12-28
YESTERDAY: 2025-12-27
YESTERDAY_FILE: brain/notes/daily/2025-12-27.md

[Full prompt from previous_day_agent section]

CHATROOM:
- File: brain/traces/agents/2025-12-28-today.md
- Read at start to see what others have posted
- Post what you find
- Format: ## [{time}] previous-day\n{message}
- Use naturally"
)

Task(
  subagent_type="general-purpose",
  description="Scan inbox for actionable items",
  prompt="You are an inbox scanner agent...

TODAY: 2025-12-28
INBOX_PATH: brain/inbox/

[Full prompt from inbox_scanner_agent section]

CHATROOM:
- File: brain/traces/agents/2025-12-28-today.md
- Read at start to see what others have posted
- Post what you find
- Format: ## [{time}] inbox-scanner\n{message}
- Use naturally"
)
```
</spawning_pattern>

<coordination_signals>
## Cross-Agent Coordination

Agents should watch for these signals from each other:

### Previous Day → Inbox Scanner
- If many incomplete tasks: "Heavy carryover day"
- If specific blockers: Mention what blocked progress

### Inbox Scanner → Previous Day
- If critical item exists: Flag priority
- If inbox item relates to yesterday's incomplete: Note relationship

### Example Chatroom Flow
```markdown
## [09:00] orchestrator
Starting /start for 2025-12-28. Spawning: previous-day, inbox-scanner
Email scan results read from brain/context/email-scan-results-2025-12-28.md

## [09:01] previous-day
Found 2 incomplete tasks from yesterday:
- Review contract changes from Sarah (async)
- Fix authentication bug (in-system)

## [09:01] inbox-scanner
Inbox has 3 items: 1 critical (overdue proposal), 2 normal

## [09:02] orchestrator
All agents complete. Synthesizing results with email scan findings...
```
</coordination_signals>

<output_contracts>
## Agent Output Contracts

Each agent must return structured output that the orchestrator can parse:

### Previous Day Agent
```markdown
## Carryover from {date}

### In-System
- [ ] {task}

### Async
- [ ] {task}
```

### Inbox Scanner Agent
```markdown
## Inbox Scan Results

### Today's Focus
- [ ] {title} (from: {filename})

### Summary
Found {n} actionable items
```

The orchestrator parses these outputs, along with email scan results from `brain/context/email-scan-results-{date}.md`, to build the daily note.
</output_contracts>

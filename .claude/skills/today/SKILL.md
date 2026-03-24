---
name: today
description: "/start Command"
---

<objective>
Aggregate tasks from multiple sources (yesterday's incomplete and inbox) using parallel sub-agents, then synthesize into today's daily note automatically. Reads email findings from pipeline-manager's scan results. Routes high-confidence items to Tasks section, defers medium/low to /triage.
</objective>

<essential_principles>
## Orchestrator Architecture

This skill implements a **three-phase orchestrator pattern**:

**Phase 1 - Parallel Gathering:**
Spawn two sub-agents with chatroom coordination:
- Previous Day Agent: Reads yesterday's daily note, extracts incomplete tasks
- Inbox Scanner Agent: Queries brain/inbox/ for critical/overdue/in-progress items

Read `brain/context/email-scan-results-{date}.md` for email findings (pipeline-manager scans Gmail, /start reads results).

**Phase 2 - Synthesis:**
Orchestrator reads chatroom, deduplicates findings, writes directly to daily note without confirmation.

**Phase 3 - Handoff:**
Present async items as a **numbered list** for Kay to confirm which become Motion tasks. Then invoke /triage for medium/low confidence items.

### Key Behaviors

**Fully automatic:** No user confirmation before writing daily note. This is a morning workflow that should just work.

**Monday carry-over:** On Mondays, the Previous Day Agent reads FRIDAY's daily note (not Sunday's). Weekend days don't have daily notes.

**Confidence routing:**
- `confidence: high` → Goes directly to Tasks section
- `confidence: medium/low` → Deferred to Triage section (handled by /triage)

### Email Findings

Pipeline-manager scans Gmail overnight and writes results to `brain/context/email-scan-results-{YYYY-MM-DD}.md`. The /start command reads this file during Phase 2 synthesis instead of scanning Gmail directly. This eliminates redundant Gmail scanning.
</essential_principles>

<quick_start>
## Execution Flow

When /start is invoked:

1. **Read email scan results** from `brain/context/email-scan-results-{date}.md` (written by pipeline-manager)
2. **Create chatroom** at `brain/traces/agents/{date}-start.md`
3. **Spawn sub-agents in parallel:**
   - Previous Day Agent
   - Inbox Scanner Agent
4. **Wait for all agents** to complete
5. **Synthesize results:**
   - Merge sub-agent findings with email scan results
   - Deduplicate items (by source_ref, title similarity)
   - Separate high-confidence from medium/low
6. **Write daily note:**
   - Create/update `brain/notes/daily/{date}.md`
   - High-confidence → Tasks sections
   - Medium/low → Triage section
7. **Hand off to /triage** if triage items exist
</quick_start>

<phase_1_parallel>
## Phase 1: Parallel Sub-Agent Spawning

Spawn both agents in a **single message** for parallel execution. Each agent posts findings to the chatroom.

### Chatroom Setup

Before spawning, create chatroom:
```markdown
brain/traces/agents/{YYYY-MM-DD}-start.md
```

### Spawning Pattern

```
Task(
  subagent_type="general-purpose",
  description="Extract yesterday's incomplete tasks",
  prompt="[Previous Day Agent prompt with chatroom protocol]"
)

Task(
  subagent_type="general-purpose",
  description="Scan inbox for actionable items",
  prompt="[Inbox Scanner Agent prompt with chatroom protocol]"
)
```

### Email Scan Results (no sub-agent needed)

Read `brain/context/email-scan-results-{date}.md` directly in the orchestrator. This file is written by pipeline-manager during its overnight/morning run and contains all actionable email items, deal flow classification, draft status, introductions, and niche signals. No Gmail scanning sub-agent needed.

See `references/sub-agents.md` for complete prompt templates.
</phase_1_parallel>

<phase_2_synthesis>
## Phase 2: Synthesis

After all sub-agents complete:

### Read Chatroom

Read the full chatroom at `brain/traces/agents/{date}-start.md` to see:
- What each agent found
- Blockers or empty results

Also read `brain/context/email-scan-results-{date}.md` for email findings from pipeline-manager's scan.

### Deduplicate

Items may appear in multiple sources. Deduplicate by:

1. **source_ref match:** Same Gmail message ID or inbox file path
2. **Title similarity:** Fuzzy match on task titles (same client + similar action)
3. **Entity overlap:** Same person/company + same topic within 48 hours

When duplicates found, keep the most complete version.

### Categorize

**In-System tasks:** Tasks that require Claude Code work (code changes, content creation, system tasks)

**Async tasks:** Tasks requiring external action (calls, emails to send, meetings)

**Triage items:** Medium/low confidence items that need human review

### Write Daily Note

Read `templates/daily-note.md` for merge behavior and section mapping, then read `schemas/vault/daily-note.yaml` for the `example:` block structure. Write directly without confirmation:

```markdown
## Tasks

### In-System
- [ ] {high-confidence task from email/inbox}
- [ ] {incomplete task from yesterday}

### Async
- [ ] {external action item}

### Triage
- [ ] {medium confidence: title} (source: {email|inbox})
- [ ] {low confidence: title} (source: {email|inbox})
```

For triage items, include source to help user understand origin.
</phase_2_synthesis>

<phase_3_handoff>
## Phase 3: Review & Handoff

### Async Item Review (always numbered)

After writing the daily note, present all async (external action) items as a **numbered list** with the title **"Proposed Action Items for Motion"**:

```
**Proposed Action Items for Motion**

1. {title} — {one-line context}
2. {title} — {one-line context}
3. {title} — {one-line context}
```

**Always use numbered lists when presenting items for Kay's review.** This lets Kay respond with just numbers (e.g., "1, 3 yes, 2 no").

After confirmation:
- Create Motion tasks for approved items (status: "Todo", workspace: ws_fnSjxkfnWpcCPke4cknr9r)
- Mark declined inbox items as done if already complete

### Triage Handoff

If any items were placed in the Triage section:

1. **Summarize triage queue** as a numbered list with confidence levels
2. **Invoke /triage skill** for human decisions

If no triage items, skip triage and complete the command.
</phase_3_handoff>

<email_scan_results>
## Email Scan Results (from pipeline-manager)

Pipeline-manager scans Gmail and writes results to `brain/context/email-scan-results-{YYYY-MM-DD}.md`. The /start command reads this file during Phase 2 synthesis.

The file contains:
- **Actionable Items Created** — inbox items created from emails (with source_ref)
- **Deal Flow Classified** — DIRECT/BLAST/NEWSLETTER counts
- **Draft Status** — sent vs unsent drafts with age
- **Introductions Detected** — new intros found in email
- **Niche Signals** — passive niche observations from email content

If the file doesn't exist (pipeline-manager hasn't run yet), log a warning in the chatroom and proceed with sub-agent findings only. The daily note will be updated when pipeline-manager runs.
</email_scan_results>

<references_index>
## References

| Reference | Purpose |
|-----------|---------|
| `sub-agents.md` | Complete prompt templates for both sub-agents |
</references_index>

<templates_index>
## Templates

Templates point to schemas and add skill-specific context:

| Template | Schema | Skill-Specific |
|----------|--------|----------------|
| `daily-note.md` | `schemas/vault/daily-note.yaml` | Merge behavior, section mapping |
| `chatroom.md` | `schemas/vault/chatroom.yaml` | /start agent list, closing format |

**Usage:** Read the template, then read the schema's `example:` block for structure.
</templates_index>

<success_criteria>
Command execution is complete when:
- [ ] Chatroom created for agent coordination
- [ ] All three sub-agents spawned in parallel
- [ ] Sub-agents posted findings to chatroom
- [ ] Results synthesized and deduplicated
- [ ] Daily note written/updated automatically
- [ ] High-confidence items in Tasks sections
- [ ] Medium/low items in Triage section
- [ ] Processing state updated with new timestamp
- [ ] /triage invoked if triage items exist
- [ ] No user confirmation required for daily note writes
</success_criteria>

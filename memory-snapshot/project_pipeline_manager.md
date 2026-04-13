---
name: Pipeline Manager Skill
description: Daily pipeline management skill — auto-triggers on session start, scans activity signals, recommends Attio stage changes for Kay to approve/reject
type: project
---

## Pipeline Manager — Built 2026-03-17

**Skill:** `.claude/skills/pipeline-manager/SKILL.md`
**Hook:** Fires on SessionStart via `pipeline_pulse` handler in `.claude/hooks/router/handlers/pipeline.py`
**Reference:** All 4 pipeline stage IDs in `.claude/skills/pipeline-manager/references/attio-stages.md`

### What It Does
1. Scans yesterday's calendar, email, and vault for activity signals
2. Matches signals to Attio pipeline entries across all 4 Lists
3. Presents recommended stage changes — Kay says yes/no
4. Executes approved changes via Attio API
5. Flags stale deals (same stage 2+ weeks)
6. Sends Slack nudge: "{n} pipeline updates waiting"

### Why It Exists
Kay identified herself as the bottleneck on pipeline management. Never consistently updated SalesFlare either. This removes the friction — pipeline updates become a 30-second yes/no review instead of remembering to drag cards.

### Key Design Decision
Pipeline updates come as recommendations, not auto-applied. Kay approves each one. This keeps her in the loop without requiring her to initiate.

### The 4 Pipelines
1. **Network** (most active) — relationship building, nurture cadence
2. **Intermediary** (ramping up) — brokers, CPAs, lawyers sending deal flow
3. **Active Deals** (where growth is needed) — the deal funnel, feeds the weekly tracker
4. **Investor Engagement** (quarterly) — low-touch, quarterly updates

### Example: Dan Tanzilli (2026-03-17)
Kay met Dan for coffee. System should have detected the calendar event, matched Dan in the Network Pipeline, and recommended: "Move Dan Tanzilli → Need to Send Thank You" + "Draft thank you email?" + "Who is Dan introducing you to?"

### Architecture Update (2026-03-17 evening)
- Network relationships moved from List entries to **People records with custom attributes**
- 5 custom attributes created on People: relationship_type, nurture_cadence, value_to_search, next_action, how_introduced
- Dan Tanzilli record fully populated as template, confirmed by Kay
- Migration agent launched overnight to populate all 111 network contacts
- Migration log will be at: brain/trackers/network-migration-log.md
- Network List will be retired after migration is confirmed
- Attio API key now has object_configuration:read-write and list_configuration:read-write scopes

### Architecture: Manager + 3 Sub-Agents (designed 2026-03-17 evening)
Claude acts as manager overseeing 3 specialized sub-agents that run in parallel:
1. **Pipeline Agent** — all 3 Lists (Intermediary, Active Deals, Investor), scans for deal signals, recommends stage moves
2. **Relationships Agent** — People records, scans ALL sources for enrichment: Attio records, Gmail (gog), vault calls (brain/calls/ — single source of truth for all transcripts, Fireflies + Granola). Flags overdue nurture, recommends attribute updates
3. **Granola Agent** — meeting transcripts, extracts action items, proposes Motion tasks

Manager responsibilities:
- Launch agents in parallel
- Review outputs for quality, flag red flags (conflicts, missing data, unusual patterns)
- Present recommendations sequentially: pipelines → relationships → tasks
- Execute approved changes
- Run stop hooks to validate (pipeline stages confirmed, People attributes confirmed)

Kay explicitly requested: "I would like you to function as the manager to oversee these agents and make sure everything functions accordingly and raise to me any red flags to review."

### Daily Review Structure
Part 1: Pipeline stages (Intermediary, Active Deals, Investor) — stage change recommendations
Part 2: Nurture reminders — compare each person's nurture_cadence against last_interaction date in Attio. Surface anyone overdue: "Consider following up with {name} ({cadence}, last contact {date})". Approved → creates Motion task automatically.
Part 3: Granola action items → Motion tasks
Part 4: Follow-ups — draft emails, create entities for intros

### Nurture Reminder Logic
- Weekly: overdue after 10 days
- Monthly: overdue after 5 weeks
- Quarterly: overdue after 14 weeks
- Occasionally: overdue after 7 months
- Bi-Annually: overdue after 7 months (uses "Occasionally" cadence option)
- Dormant: never surfaced
- Source: Attio last_interaction field (auto-populated by Attio from email/calendar)
- Output: "Consider following up with {name} ({relationship_type}, last contact {date})" → approve → Motion task created

### Superhuman MCP Server
Gmail API drafts don't sync to Superhuman. Investigating Superhuman MCP Server (OAuth-based, no API key needed).
Command to add: `claude mcp add --transport http superhuman-mail https://mcp.mail.superhuman.com/mcp`
Kay will try this on next session restart.

**How to apply:** This skill runs automatically on every session start. It's the first thing Kay sees. Follow-up actions (draft emails, create entities for introductions, Motion tasks) flow naturally from the pipeline recommendations. Ask questions one at a time. No em dashes in emails.

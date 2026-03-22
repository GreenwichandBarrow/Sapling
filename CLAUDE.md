# Sapling OS

Personal knowledge system: Obsidian vault + Claude Code + learning loop.
You manage `brain/`, skills, hooks. Execute tasks; capture decisions; system gets smarter.

**Core loop:** Request → Execute → Trace decisions → Skills improve → Better next time.

## Vault Writing Rules (CRITICAL)

Every file in `brain/` builds an Obsidian knowledge graph. **Wiki-links and tags are mandatory** — without them, files are isolated and useless.

### Wiki-Links

**Always link.** Every person, company, call, output, or trace you reference MUST be a wiki-link.

```markdown
# Good
people: ["[[entities/jane-smith]]"]
Follow up from [[calls/2025-12-27-strategy-update]].
Send deliverable to [[entities/jane-smith|Jane]].

# Bad — broken graph, no connections
people: ["jane-smith"]
Follow up from strategy call.
Send deliverable to Jane.
```

**Format:** `[[entities/{slug}]]` or `[[entities/{slug}|Display Name]]` for inline.
**Entities are flat:** `entities/{slug}` — never `entities/people/` or `entities/companies/`.

**Cross-reference rule:** If file A mentions entity/file B, file A MUST wiki-link to B.
- Mention a person → `[[entities/{slug}]]`
- Reference a call → `[[calls/{date}-{slug}]]`
- Cite an output → `[[outputs/{date}-{slug}]]`
- Link to daily note → `[[notes/daily/{date}]]`

**Entity creation:** If you reference an entity that doesn't exist yet, create it in `brain/entities/{slug}.md` with proper schema. Don't leave broken links.

### Tags

**Every `brain/` file needs tags.** Tags are how Obsidian queries work — no tags = invisible file.

Required tag namespaces (per schema `required_patterns`):
- `date/YYYY-MM-DD` — always
- Type literal — `call`, `entity`, `output`, `trace`, `inbox`, `library`, `daily`, `weekly`
- Context tags — `person/{slug}`, `company/{slug}`, `client/{slug}`, `source/{source}`, `output/{type}`, `status/{status}`

**Derive tags from frontmatter:**
```yaml
# If frontmatter has:
people: ["[[entities/jane-smith]]"]
companies: ["[[entities/acme-corp]]"]

# Then tags MUST include:
tags:
  - person/jane-smith
  - company/acme-corp
```

**Topic tags:** Use `topic/{slug}`. Check existing files for prior topics before inventing new ones.

### Frontmatter

Every `brain/` file needs YAML frontmatter. Hook `validate-edits.py` enforces required fields per schema — if it rejects a write, read the error + schema example, fix in one retry.

Schema mapping:
| Path | Schema |
|------|--------|
| `brain/calls/` | `schemas/vault/call.yaml` |
| `brain/entities/` | `schemas/vault/entity.yaml` |
| `brain/inbox/` | `schemas/vault/inbox.yaml` |
| `brain/library/` | `schemas/vault/library.yaml` |
| `brain/outputs/` | `schemas/vault/output.yaml` |
| `brain/traces/` | `schemas/vault/trace.yaml` |
| `brain/notes/daily/` | `schemas/vault/daily-note.yaml` |
| `brain/notes/weekly/` | `schemas/vault/weekly-note.yaml` |

**Before creating a file:** Read the schema's `example:` block. Match it exactly.

### Knowledge Graph Checklist

Before finishing any `brain/` write, verify:
- [ ] Frontmatter has all required fields per schema
- [ ] All people/companies in frontmatter are wiki-links to `entities/`
- [ ] Tags include namespaces for every linked entity (`person/`, `company/`, `client/`)
- [ ] Body text uses wiki-links for any entity, call, output, or trace mentioned
- [ ] Referenced entities exist — if not, create them

## Querying

**By Path:**
- `brain/entities/` → People + companies
- `brain/calls/` → Call notes
- `brain/outputs/` → Deliverables
- `brain/traces/` → Decision traces
- `brain/inbox/` → Pending tasks
- `brain/context/` → Identity, business, voice

**By Tag:**
- `client/{slug}` — all content for a client
- `person/{slug}` — all content involving a person
- `company/{slug}` — all content involving a company
- `topic/{topic}` — subject matter
- `status/{status}` — state (draft, published, done)
- `output/{type}` — output type (linkedin-post, prd, email)

**Find everything about someone:**
```bash
grep -r "person/jane-smith" brain/
grep -r "\[\[entities/jane-smith\]\]" brain/
```

**Source of Truth:**
- **Beads** owns: tasks, dependencies, work status
- **Obsidian (brain/)** owns: knowledge — entities, calls, outputs, traces, context

## Tools

**Beads (`bd`):** File-based issue tracking. `bd ready`, `bd create`, `bd close`, `bd sync`.
**GOG (`gog`):** CLI for Google Workspace. Gmail, Calendar, Drive, Docs, Sheets, Slides, Tasks, Contacts, Forms, Chat, and more.
- Account: `kay.s@greenwichandbarrow.com` (OAuth). Invoke via `/gogcli` skill.
- Use `--json` when parsing output. Use `--dry-run` before destructive ops.
- Prefer `--readonly` scopes when full access isn't needed.
- Never expose OAuth tokens or credentials in logs/commits.
- Skill references: `.claude/skills/gogcli/references/commands.md` (full command ref), `auth-setup.md`.
- Env vars: `$GOG_ACCOUNT`, `$GOG_TIMEZONE`, `$GOG_ENABLE_COMMANDS` (sandbox for automation).
- Supports batch ops, cross-service workflows (email → sheet → calendar), and pub/sub watches.

**Skills:** `.claude/skills/` — reusable workflows. Invoked via `/task`, `/onboard`, `/calibrate`.
**Commands:** `.claude/commands/` — slash command wrappers.
**Hooks:** `.claude/hooks/` — event handlers (schema validation, session start).

## Context Engineering

Context window = public good. Every token competes.

- Progressive disclosure: metadata first (~50 tok), skill content on trigger (~1,500 tok), references only when needed.
- Sub-agents when reading/editing 3+ files — for context isolation, not complexity.
- Sub-agent output: max 2,000 words. Summaries, not prose. Analysis stays in sub-agent.
- Context resumption: verify `git status` + read files before trusting summaries.
- 2+ parallel sub-agents → invoke `agent-chatroom` skill first.

## Task Management

**Beads (`bd`)** is the single task system.

```bash
bd ready                    # What can I work on?
bd update <id> --status=in_progress
bd close <id>
bd sync                     # Push to git
```

Rules: create beads for multi-step/multi-session work. `--assignee=agent` for agent, `--assignee=human` for human. Dependencies: `bd dep add <blocker> <blocked-by>`.

## Commands

| Command | Purpose |
|---------|---------|
| `/task` | Task + decision tracing |
| `/today` | Daily note workflow |
| `/weekly` | Weekly review |
| `/commit` | Git commit |
| `/migrate` | Schema migrations |

## Evolution

System learns from decisions. `/task` completes → `decision-traces` skill captures choices → traces identify improvement targets → skills upgrade.

Litmus: only trace choices between alternatives that change future behavior with non-obvious reasoning.

## Scheduled Skills (launchd)

Three skills run on a schedule via macOS launchd, independent of active sessions:

| Skill | Schedule | Purpose |
|-------|----------|---------|
| `intermediary-manager` | Mon-Fri 6am ET | Platform scanning + email screening |
| `niche-intelligence` | Tuesday 11pm ET | Newsletter scrape, niche identification, one-pagers, scorecards |
| `weekly-tracker` | Friday 8pm ET | Weekly activity data compilation |

**Infrastructure:**
- Wrapper: `scripts/run-skill.sh` (shared by all jobs)
- Env: `scripts/.env.launchd` (secrets for headless runs, not committed)
- Logs: `logs/scheduled/{skill}-{date}.log` (14-day rotation)
- Plists: `~/Library/LaunchAgents/com.greenwich-barrow.{skill}.plist`

**Status check:** `launchctl list | grep greenwich`
**Manual trigger:** `launchctl start com.greenwich-barrow.{skill}`
**Mac must be in sleep mode (not shut down) for scheduled runs to fire.**

## Behaviors

- Start simple. Sharp knife first. Complexity only after simpler approach fails.
- Before acting: query system for context (entities, calls, prior outputs).
- Use skills; don't reinvent workflows.
- Parallel over sequential for independent work.
- Beads for persistence on multi-step/multi-session tasks.

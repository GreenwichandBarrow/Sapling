# Sapling OS

A personal operating system built on Claude Code + Obsidian that learns your preferences over time.

**Core idea:** Every task builds a knowledge graph. Wiki-links and tags wire files together automatically. Run `/calibrate` to review decisions and improve the system. The more you use it, the smarter it gets.

## Quick Start

**Prerequisites:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Beads](https://github.com/steveyegge/beads), Python 3.8+

**Optional:** [fzf](https://github.com/junegunn/fzf) for fuzzy file matching (`brew install fzf`)

```bash
brew tap steveyegge/beads && brew install bd

git clone https://github.com/hwells4/Sapling.git
cd Sapling
bd onboard

claude
/onboard  # First-time setup (~5 min)
```

## What You Get

### Commands

| Command | What it does |
|---------|-------------|
| `/task` | Execute work with automatic decision tracing |
| `/today` | Aggregate tasks from yesterday, inbox, and email into daily note |
| `/calibrate` | Review decision traces and improve skills |
| `/onboard` | First-time setup — populate your context files |
| `/commit` | Git commit with Linear issue sync |
| `/push` | Push to remote |

### Skills (built-in)

| Skill | Purpose |
|-------|---------|
| `decision-traces` | Capture meaningful choices that change future behavior |
| `today` | Multi-agent daily note synthesis (parallel sub-agents) |
| `calibration-workflow` | Review traces, propose skill improvements |
| `triage` | Route medium/low confidence items for human decision |
| `agent-chatroom` | Coordinate 2+ parallel sub-agents |
| `obsidian-vault-ops` | Read/write vault files with proper wiki-links |
| `onboard` | Interactive context population |
| `generate-prd` | Generate product requirement docs |
| `generate-stories` | Break PRDs into stories |
| `generate-visuals` | Image generation (requires Gemini API key) |
| `plan-refinery` | Iterative plan improvement |
| `create-hook` | Scaffold new hooks |
| `migration-workflow` | Schema version migrations |
| `github` | GitHub operations |

### Hook Router

All hooks route through a Python framework (`.claude/hooks/router/`) that dispatches to handler functions per event:

| Event | What fires |
|-------|-----------|
| `SessionStart` | Git sync, session initialization |
| `PreToolUse` | Schema validation on `brain/` writes, skill context injection |
| `PostToolUse` | Post-write processing |
| `Stop` | Auto-commit, orchestrator gates |
| `PreCompact` | Context preservation before compaction |
| `UserPromptSubmit` | Input processing |

**Schema validation:** Every file written to `brain/` is validated against its schema (`schemas/vault/*.yaml`). Missing frontmatter or required tags → rejected with a copy-paste template.

### Knowledge Graph

Files in `brain/` are an Obsidian vault. Wiki-links (`[[entities/slug]]`) and tags (`person/slug`, `client/slug`) connect everything into a queryable graph.

CLAUDE.md enforces writing rules so the graph builds automatically as you work:
- Every entity reference becomes a wiki-link
- Tags are derived from frontmatter (people → `person/` tags, companies → `company/` tags)
- Missing entities are created on the fly
- Schema validation hook rejects files that break the structure

## Directory Structure

```
Sapling/
├── CLAUDE.md              # System instructions (always in context)
├── brain/                 # Obsidian vault
│   ├── calls/             # Meeting notes
│   ├── context/           # About you, your business, your voice
│   ├── entities/          # People + companies (flat)
│   ├── inbox/             # Task capture (calls, email, manual)
│   ├── library/           # Reference material (external + internal)
│   ├── notes/daily/       # Daily notes
│   ├── notes/weekly/      # Weekly reviews
│   ├── outputs/           # Deliverables (posts, PRDs, emails)
│   ├── traces/            # Decision traces + hypotheses
│   └── triage/            # Unclassified items
├── schemas/
│   ├── vault/             # YAML schemas per file type (10 schemas)
│   └── tags/taxonomy.yaml # All valid tag namespaces
├── .claude/
│   ├── commands/          # Slash commands
│   ├── skills/            # Reusable workflows (16 skills)
│   └── hooks/router/      # Event-driven hook framework
└── .beads/                # File-based issue tracking
```

## Configuration

Copy `.env.example` to `.env` for optional features:

| Variable | Purpose |
|----------|---------|
| `GEMINI_API_KEY` | Image generation via `/generate-visuals` |
| `GITHUB_TOKEN` | GitHub CLI auth (if not using `gh auth login`) |

## How It Learns

1. `/task` executes work and captures decisions (choices between alternatives with non-obvious reasoning)
2. Decision traces land in `brain/traces/`
3. `/calibrate` reviews traces and proposes skill improvements
4. Skills get better → future tasks execute better

**Litmus test for tracing:** Is it a choice between alternatives? Does it change future behavior? Is the reasoning non-obvious? All three must be yes.

## License

MIT License — see [LICENSE](LICENSE)

---

Built on [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Obsidian](https://obsidian.md), and [Beads](https://github.com/steveyegge/beads).

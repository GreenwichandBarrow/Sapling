---
description: Atomic commit of task-related changes
argument-hint: [optional context about what was done]
---

# /commit Command

Create atomic commits that capture complete units of work. NO Claude Code authorship.

## Core Principle

One task = one commit. Intelligently detect ALL files related to the current work and commit them together.

## Process

**Before committing, always run the session wrap-up checklist:**

### Session Wrap-Up (runs every /commit)
1. **Memory** — Save any new memories from this session (user preferences, feedback, project updates). Check if existing memories need updating.
2. **Skills** — Update any skills that were discussed, modified, or need fixes identified during the session. Apply feedback to skill instructions.
3. **Stop hooks** — Add any sub-agent stop hooks or verification gates that came up during the session.
4. **Context** — Update daily note, processing state, or any context files that changed.
5. **Then commit** — proceed with the git workflow below.

### Git Workflow
1. **Identify the task** - What was the user trying to accomplish?
2. **Detect related files** - Scan for all changes connected to this task (see detection below)
3. **Verify completeness** - Would someone checking out this commit have everything they need?
4. **Stage atomically** - All related files in one commit, nothing more, nothing less
5. **Write message** - Describe what was accomplished, not just what files changed
6. **Push to remote** - `git push origin main` so the other machine can pull

## Message Format

```
[verb]: [what was accomplished]
```

Common verbs: `add`, `fix`, `update`, `refactor`, `implement`, `configure`

## Examples

- `add: user onboarding flow with creature selection`
- `fix: date parsing in call transcript processor`
- `implement: skill healing workflow with approval gates`
- `update: voice examples with 10 new LinkedIn posts`
- `configure: playwright for headed browser testing`

## Rules

1. **NO Claude Code footer** - Never add co-author or generated-by lines
2. **Atomic = complete** - Commit must be self-contained; nothing missing, nothing extra
3. **Task coherence** - All files serve the same purpose
4. **Present tense** - "add" not "added"
5. **Ask if unclear** - When multiple tasks are mixed in changes, ask user which to commit

## Intelligent File Detection

Before committing, intelligently detect all task-related changes:

```bash
# 1. See everything that changed
git status --short

# 2. Check for files modified in same time window (last 2 hours)
find . -type f -mmin -120 -not -path './.git/*' | head -30
```

### Detection Heuristics

**Code changes** → Look for:
- Test files for modified code
- Type definitions if interfaces changed
- Config files if behavior changed (e.g., new env vars)

**Content/output changes** → Look for:
- Associated traces in `brain/traces/`
- Source files referenced in output
- Template files if output format is new

**Skill/command changes** → Look for:
- Related reference files in same skill folder
- Updated templates
- Hook modifications

### Cross-Reference Checks

```bash
# Check frontmatter for linked files
grep -l "linked_trace\|related_chatroom\|source:" brain/**/*.md 2>/dev/null
```

**When uncertain:** Show user the candidate files and ask which belong together.

$ARGUMENTS

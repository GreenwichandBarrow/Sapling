---
name: github
description: GitHub repository management via gh CLI. Use for creating repos, cloning, changing visibility, or scaffolding new projects from boilerplates.
archetype: simple
context_budget:
  skill_md: 100
  max_references: 12
  learnings_md: 40
  sub_agent_limit: 500
invocation: user
---

<objective>
Manage GitHub repositories through the gh CLI with sane defaults (private repos, proper error handling).
</objective>

<essential_principles>
- All repos created are **private by default**
- Check authentication before operations: `gh auth status`
- Use `gh repo` commands, not raw git for GitHub operations
</essential_principles>

<intake>
**Commands:**
1. `/github list` - List your repositories
2. `/github create <name>` - Create new private repo
3. `/github clone <repo>` - Clone a repo locally
4. `/github visibility <repo> <public|private>` - Change visibility
5. `/github new-project <name> --from <boilerplate>` - Create from template

What would you like to do?
</intake>

<routing>
| Command Pattern | Workflow |
|-----------------|----------|
| `list` | workflows/list.md |
| `create <name>` | workflows/create.md |
| `clone <repo>` | workflows/clone.md |
| `visibility <repo> <visibility>` | workflows/visibility.md |
| `new-project <name> --from <boilerplate>` | workflows/new-project.md |
</routing>

<references_index>
| Reference | Purpose |
|-----------|---------|
| references/gh-commands.md | gh CLI command syntax and flags |
</references_index>

<error_handling>
Common errors and resolutions:
- **Not authenticated**: Run `gh auth login`
- **Repo already exists**: Check with `gh repo view <name>` first
- **Permission denied**: Verify you own the repo or have admin access
- **Rate limited**: Wait and retry, or use authenticated requests
</error_handling>

<success_criteria>
- [ ] Operation completes without error
- [ ] User informed of result (repo URL, local path, etc.)
</success_criteria>

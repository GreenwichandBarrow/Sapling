# gh CLI Command Reference

Quick reference for GitHub CLI commands used by this skill.

## Authentication

```bash
# Check auth status
gh auth status

# Login interactively
gh auth login

# Login with token
gh auth login --with-token < token.txt
```

## Repository Creation

```bash
# Create private repo (default)
gh repo create <name> --private

# Create with description
gh repo create <name> --private --description "My project"

# Create in organization
gh repo create <org>/<name> --private

# Create and clone
gh repo create <name> --private --clone
```

## Repository Cloning

```bash
# Clone by owner/repo
gh repo clone <owner>/<repo>

# Clone to specific directory
gh repo clone <owner>/<repo> <directory>

# Clone with git flags
gh repo clone <owner>/<repo> -- --depth=1
```

## Listing Repositories

```bash
# List your repos (default 30)
gh repo list

# List more repos
gh repo list --limit 100

# List specific owner/org
gh repo list <owner>

# Filter by visibility
gh repo list --visibility private
gh repo list --visibility public

# Exclude forks
gh repo list --source

# JSON output
gh repo list --json name,visibility,updatedAt,description

# Filter by language
gh repo list --language python
```

## Repository Info

```bash
# View repo details
gh repo view <repo>

# View as JSON
gh repo view <repo> --json visibility,name,url
```

## Repository Settings

```bash
# Change visibility
gh repo edit <repo> --visibility public
gh repo edit <repo> --visibility private

# Accept visibility change consequences (required for API)
gh repo edit <repo> --visibility public --accept-visibility-change-consequences

# Update description
gh repo edit <repo> --description "New description"
```

## Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| `gh: command not found` | gh not installed | `brew install gh` |
| `not logged in` | No auth token | `gh auth login` |
| `repository already exists` | Name taken | Choose different name |
| `permission denied` | No admin access | Check repo ownership |
| `Could not resolve` | Repo not found | Verify owner/repo format |

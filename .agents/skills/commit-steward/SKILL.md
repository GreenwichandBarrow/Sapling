---
name: commit-steward
description: Commit and push steward for Kay's operating system. Use when Kay invokes /commit, /push, asks to save changes, close a work session, commit work, or explain why commits are lingering. Preserves the Claude-era wrap-up checklist: memory, skills, hooks, context, decisions, atomic commits, dirty-tree classification, and explicit push handling.
---

# Commit Steward

This skill preserves the Claude-era `/commit` and `/push` intent while respecting the Codex migration policy.

## Core Contract

One logical task equals one commit. Do not make a giant cleanup commit unless Kay explicitly asks.

Before committing:
1. Inspect `git status --short`.
2. Classify changes:
   - current task
   - unrelated user/workstream changes
   - generated artifacts
   - sensitive files
   - temporary/debug files
3. Review diffs for the files you intend to stage.
4. Confirm no secrets are being committed.
5. Update required migration/operations docs when the work changed the operating model.

Never use broad staging unless the file set has been reviewed. Prefer explicit paths.

## Session Wrap-Up Checklist

Before a closeout commit, check whether the session created:
- new durable user preferences
- skill improvements or learnings
- stop hooks or safety rules
- workflow decisions that belong in `brain/session-decisions/`
- migration notes or Phase 3 cleanup items
- dashboard / scheduled-job changes that need validation notes

If there are no updates in a category, report zero explicitly rather than silently skipping it.

## Push Policy

Default during migration fidelity repair:
- Commit scoped fixes locally.
- Do not push until Kay approves or the final fidelity pass explicitly asks for it.

If Kay explicitly asks to push:
1. Confirm branch.
2. Confirm no sensitive/unrelated files are included.
3. Push only the intended branch.
4. Report the pushed commit range.

## Commit Message

Use clear value-oriented messages:

`skills: migrate goodmorning command contract`

`docs: record migration fidelity gate`

## Success Criteria

The repo has small, reviewable commits; dirty-tree leftovers are explained; push state is explicit; and Good Night can rely on the commit ledger instead of leaving unowned changes behind.

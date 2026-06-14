# Runtime Artifact Classification - 2026-06-14

This note classifies the remaining dirty artifacts observed during Phase 2.5 of
the Claude Code to Codex migration. It is intentionally conservative: uncertain
business records and generated runtime outputs should be preserved in place until
Kay explicitly reviews or a durable artifact policy is adopted.

## Commit Now

The following categories are durable Phase 2.5 source or operating-system
changes and are safe to preserve in git:

- Dashboard command-center source and operator-maintained static data.
- Codex runner/readiness scripts and non-secret scheduled-job wrappers.
- Task tracker builder logic and skill instructions.
- Workstation/workspace setup documentation.
- Codex/Claude usage refresh scripts and systemd templates used for monitoring
  the transition away from Claude Code.
- One-off repair scripts that document and preserve a known migration incident.

## Runtime Snapshot Artifacts

These are generated status snapshots, dated scan outputs, logs, and rollback
captures. They may be useful for auditability, but should not be committed
blindly without a policy for retention and redaction:

- `brain/context/*-snapshot.json`
- `brain/context/*scan*.md`
- `brain/context/email-intelligence-input-*.json`
- `brain/context/email-scan-results-*.md`
- `brain/context/relationship-status-*.md`
- `brain/context/rollback-snapshots/*`
- `brain/context/verb-logs/*`
- `brain/trackers/health/*`
- `brain/trackers/niches/*`
- `brain/trackers/weekly/*`

## Business Records / Needs Kay

These files may be legitimate CRM, call, relationship, inbox, brief, or entity
records. They should remain uncommitted until Kay confirms whether the repo is
the intended durable home for these records:

- `brain/briefs/*`
- `brain/calls/*`
- `brain/entities/*`
- `brain/inbox/*`
- `brain/outputs/*`
- `brain/traces/agents/*`
- `brain/trackers/post-call-analyzer/*`
- `memory/*`

## Phase 3 Cleanup Candidates

Do not remove these during Phase 2.5. They belong in Phase 3 after the monitoring
week confirms Codex is stable:

- Claude usage compatibility scripts/templates, if no longer needed.
- `jj-*` compatibility names after dashboard and downstream references are
  renamed to Cold Call Operations.
- Symlink aliases and duplicate lowercase/uppercase operating-area paths.
- Old rollback snapshots after Kay approves retention/deletion policy.

## Sensitive / Do Not Inspect Values

- `scripts/.env.codex` may be checked for presence or metadata only.
- Do not print or commit secrets.

## Recommended Policy Follow-up

Create an artifact-retention policy that explicitly decides which generated
records belong in git, which belong in Google Drive or another data store, and
which should be ignored after a short retention window.

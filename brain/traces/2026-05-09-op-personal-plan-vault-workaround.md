---
schema_version: 1.1.0
date: 2026-05-09
type: trace
importance: medium
target: "skill:1password-setup"
tags: ["date/2026-05-09", "trace", "domain/infrastructure", "topic/1password", "topic/service-account", "pattern/plan-limitation", "status/applied"]
---

# 1Password Personal/Individual plan: Service Accounts can't access Personal vault directly

## Trigger

Tried to create a Service Account at `https://my.1password.com/developer-tools/infrastructure-secrets/serviceaccount` to give the Hetzner server programmatic op:// resolution access. The vault-access step showed only one option: a "Allow creation of new vaults" checkbox. No vault picker, no list of existing vaults to grant access to. The Personal vault was not listed as a sharing target.

## Decision

Workaround: create a custom vault named `GB Server` in 1Password (Personal plan does support custom vaults via desktop app File menu / `cmd+option+N`). Move the Attio + Apollo API key items from Personal → GB Server vault. Then restart Service Account creation; the GB Server vault appears in the picker because it's a non-Personal vault (Personal plan SAs CAN access custom vaults Kay creates).

## Alternatives Considered

- **Upgrade to 1Password Families plan** (~$5/mo). Would unlock Personal-vault sharing with SAs. Rejected: cost + multi-day timing for plan change to propagate. Workaround is free + works immediately.
- **Skip Service Account, use op CLI with master-password sign-in on server.** Rejected: requires Kay's master password live on server (worse than SA token). Also brittle — sign-in expires periodically.
- **Skip op:// migration on server entirely; keep raw values in `scripts/.env.launchd`.** Rejected: server is the runtime where most timers fire; raw values on server defeats the purpose of the migration.

## Reasoning

The Personal plan limitation is undocumented in the SA creation flow — the empty-state UI just shows "This service account cannot access any vaults" with no explanation. If you don't know about custom vaults, you'd assume the workflow is broken and either upgrade or abandon.

The custom vault workaround works because:
1. Personal plan supports user-created vaults (via desktop File → New Vault).
2. SAs on Personal plan CAN be granted access to user-created vaults.
3. Items can be moved between vaults trivially (right-click → Move).

The cost: one additional vault + ongoing convention to put server-needed items in `GB Server` rather than `Personal`. Items not consumed by `.env.launchd` (like Tailscale auth key, ANTHROPIC_API_KEY for Claude Code app) stay in Personal because they're accessed via Touch ID locally, not via SA.

## Outcome

- `GB Server` vault created in 1Password.
- Attio + Apollo API key items moved Personal → GB Server.
- Service Account `GB-Server` created with Read-only access to GB Server vault.
- SA token deployed to Hetzner server at `~/.config/op-sa-token.env`.
- Server-side `op vault list` returns `GB Server`. Both API keys resolve to correct lengths (64 + 22).
- iMac references updated from `op://Personal/...` to `op://GB Server/...` via sed.

## Learnings

- 1Password Personal plan: SA can ONLY access vaults Kay creates manually. Personal vault is NOT shareable with SA on Personal plan.
- For any future secret that the server (or other non-Touch-ID environment) needs: store in `GB Server` vault, not Personal. Personal vault items are for human-Touch-ID use only.
- When a 1Password UI shows an empty-state with no actionable explanation, the answer often lies in a related-but-not-mentioned feature (in this case, custom vaults). Check the desktop app's vault picker, not just the web admin.
- This pattern generalizes: any SaaS Service Account flow where the empty state shows "no access" likely has a workaround via the customer's own resource creation (not a plan upgrade).

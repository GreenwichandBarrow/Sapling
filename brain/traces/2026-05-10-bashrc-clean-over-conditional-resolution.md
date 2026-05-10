---
schema_version: 1.1.0
date: 2026-05-10
type: trace
importance: medium
target: "doctrine:secrets-management"
tags: ["date/2026-05-10", "trace", "domain/security", "topic/secrets-management", "topic/1password-migration", "topic/shell-config", "pattern/clean-over-convenient", "status/applied"]
---

# Clean .bashrc over conditional op:// resolution — convenience cost vs hidden behavior

## Trigger

After migrating `GOG_KEYRING_PASSWORD` to `op://` reference in `scripts/.env.launchd`, server claude proposed three options for the now-redundant plaintext line in `~/.bashrc`:

- **A** — Remove line entirely. Cleanest. Interactive `gog` from raw shell sessions won't work unless user manually sources `~/.config/op-sa-token.env` first.
- **B (server claude's recommendation)** — Replace plaintext line with conditional block that fires `op read` on shell open when `OP_SERVICE_ACCOUNT_TOKEN` is in env. Resolves automatically for interactive shells.
- **C** — Leave plaintext line. Functionally redundant; defeats migration purpose.

Decision needed: A, B, or C.

## Decision

**A — remove the line entirely.** Reject server claude's recommended B.

## Alternatives Considered

- **Option B (conditional `op read` block in `.bashrc`).** Tempting because it preserves interactive-shell convenience for ad-hoc `gog` invocations. Rejected: every `op read` is a network call to 1Password's API. Adding it to shell init means EVERY interactive shell open hits the network — adds ~100-200ms latency, hidden from anyone debugging shell startup performance, and creates a dependency on 1P API availability for opening a terminal. Six lines of conditional shell logic that runs on every login, when the actual production path (systemd-scheduled jobs) doesn't use `.bashrc` at all. The convenience benefit is small (server claude running ad-hoc `gog` via Bash tool); the cost is recurring and broadly distributed.
- **Option C (leave plaintext).** Rejected: this is the state we're explicitly migrating away from. The whole point of the migration is to eliminate plaintext-secret-on-disk risk. Keeping the line because "the systemd path doesn't use it anyway" misses the point — anyone with shell access can still `cat ~/.bashrc` and see the value.
- **Option D (helper script/alias for ad-hoc `gog`).** Considered as middle path. Wrap the env-loading in a single command (`source ~/.config/op-sa-token.env && export GOG_KEYRING_PASSWORD=$(op read ...) && gog $@`) accessible as `gog-secure` alias or wrapper script. Cleaner than B because it's invoked on demand, not on every shell open. Mentioned to server claude as the right path if interactive ad-hoc need recurs more than 2-3 times.

## Reasoning

The framework: **separate the production path from the convenience path, optimize each independently.**

- **Production path** (launchd-scheduled jobs, systemd timers): runs through `scripts/run-skill.sh`, which sources `load-env.sh` which resolves `op://` references via `op inject`. Doesn't touch `.bashrc` at all. This path is what generates real revenue/value.
- **Convenience path** (server claude running ad-hoc `gog` via Bash tool, future debugging): rare, predictable surface area. Should be solved at the call site (prefix env-loading) or via a helper alias, not by polluting shell init.

When the convenience path's solution adds cost to the production path's surroundings (every shell open, every debug session, every future engineer trying to understand startup), that's a misallocation. Move the cost to where the convenience is actually needed.

The other framing: **`.bashrc` should not contain logic that runs unconditionally for behaviors that fire conditionally.** The conditional block in B has a guard (`if SA token present`), but the cost of EVALUATING the guard runs on every shell open. The actual op-reading only fires when SA token is set, but the guard check is universal. Better to have zero `.bashrc` magic and reach for the convenience explicitly when needed.

Server claude's instinct toward B is reasonable from a "my own ad-hoc workflow is now harder" perspective. But agent-side ergonomics shouldn't dictate user-side shell config. The right separation: agent learns to prefix env-loading in its own Bash tool calls when needed; user's `.bashrc` stays clean.

## Outcome

- `.bashrc` plaintext `GOG_KEYRING_PASSWORD` line removed.
- Stale `.env.launchd.bak` files deleted (rotated-out values, no recovery use).
- Smoke tests passed: `op inject` resolves all 7 vars, `gog gmail draft list` returns drafts (proves keyring decrypt under op://), Attio API curl returns 200 OK.
- Server claude given the helper-pattern instruction: `source ~/.config/op-sa-token.env && export GOG_KEYRING_PASSWORD=$(op read 'op://GB Server/GOG Keyring Password/password') && gog <command>` for ad-hoc invocations. If used 3+ times, graduate to alias/wrapper.

## Why This Trace Matters

Future agents and humans debugging this server will see a clean `.bashrc` and may wonder "why isn't `gog` working when I just `ssh ubuntu@server`?" The answer is intentional — this trace records the choice and the cost reasoning so the question doesn't get answered by adding the conditional block back later.

It also establishes the doctrine: **convenience-path costs go to the call site, not into shared config.** Applies broadly: any time an agent proposes "let me make this easier by adding logic to a universally-loaded file" — challenge the universality of the cost.

## Key Insight

When a recommendation adds always-on cost for sometimes-on benefit, the right fix is usually at the sometimes-on side, not the always-on side. Shell init, CI configs, dotfiles, and root-level configuration are universally-loaded — anything you put there pays cost on every load. Reserve them for things that are also universally needed.

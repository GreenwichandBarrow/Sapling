---
schema_version: 1.1.0
date: 2026-05-09
type: trace
importance: high
target: "skill:secrets-management"
tags: ["date/2026-05-09", "trace", "domain/security", "topic/secrets-management", "topic/incident-response", "pattern/severity-tiering", "status/applied"]
---

# Rotation urgency tiering — same-session for high-impact, deferred for low-impact

## Trigger

Two security leak events tonight exposed live secrets to conversation transcript:

1. **8:00 PM:** `grep -rE PATTERN .env.launchd*` exposed ATTIO_API_KEY (64 chars) + APOLLO_API_KEY (22 chars). Violation of CLAUDE.md "Before handling secrets" preflight rule (use value-suppressing patterns only).
2. **8:13 PM:** `bash -x` debug trace of `load_env` exposed 4 SLACK_WEBHOOK_* URLs (with secret tokens) + GOG_KEYRING_PASSWORD (32-char keyring password).

Question: rotate everything immediately, or tier by impact?

## Decision

Tier by leak vector + weaponization cost:

- **Same-session (within 5 min):** ATTIO_API_KEY + APOLLO_API_KEY. These are direct API authentication credentials — any third party with the key can immediately authenticate as Kay against Attio/Apollo. Highest impact, instant weaponization. Kay rotated both at the respective admin panels, added new keys to 1Password GB Server vault.
- **Defer to next morning (Sunday):** 4 SLACK_WEBHOOK_* URLs + GOG_KEYRING_PASSWORD. Lower weaponization potential:
  - Slack webhooks: attacker can post messages to specific Slack channels. Annoying, not catastrophic. Worst case = team confusion / phishing-via-pretend-system-message.
  - GOG_KEYRING_PASSWORD: decrypts the gog keyring on Hetzner server. Attacker would need shell access to the server to use it. Defense-in-depth, not first-line.

## Alternatives Considered

- **Rotate everything immediately tonight.** Rejected: Kay was already 8 hours into a major infrastructure session and getting tired. Slack webhook rotation requires going to each channel's webhook config + pasting new value into server `.env.launchd` + restarting affected services. ~30 min of additional work for low marginal security gain.
- **Defer everything (including Attio/Apollo) to Sunday.** Rejected: Attio/Apollo keys are direct authn — leaving them live means anyone scraping the transcript window has working credentials. Same-session rotation is non-negotiable for direct-API-credential leaks.
- **Treat Slack webhooks as same-tier as API keys.** Rejected: webhooks are write-only-to-channel, not authentication for reads. Different weaponization profile.

## Reasoning

The framework that worked: classify each leaked secret by:

1. **Authentication scope.** Does the secret authenticate as a user/principal (high), or grant a specific narrow capability (medium), or require additional access to weaponize (low)?
2. **Time-to-weaponization.** How long does it take an attacker who reads the transcript to actually use the secret? Direct API keys = seconds. Webhooks = minutes (need to craft message). Server-only secrets = requires server access first (often days/never).
3. **Blast radius if weaponized.** Full account access (high), specific channel access (medium), local-only operations (low).

Tiering matters because rotation has its own cost — it consumes attention, time, and creates risk of misconfiguration during the rotation. For high-tier leaks, that cost is justified by the severity. For low-tier, it can wait.

CLAUDE.md preflight already says "use value-suppressing patterns" to PREVENT leaks. Once a leak happens, this trace establishes the response framework: tier the rotation, do the high-tier same-session, queue the rest as a task with clear instructions.

## Outcome

- ATTIO + APOLLO rotated within 5 min of leak detection. New keys in 1Password GB Server vault. iMac + server `.env.launchd` updated to op:// references in same session. Old keys revoked at admin panels.
- Task #4 created for Slack webhooks + GOG_KEYRING_PASSWORD rotation Sunday morning.
- 1Password migration architecture (load-env.sh + GB Server vault) means future leaks of these specific secrets become impossible: op:// references can't be grep'd to reveal values; the token is in 1Password, not on disk in plaintext.

## Learnings

- **Direct API credentials → same-session rotation, no exceptions.** If a key authenticates as the user/account against an external API, treat as fire alarm.
- **Channel/scoped secrets → same-day or next-morning rotation.** Slack webhooks, monitoring tokens, etc.
- **Server-only secrets → defer if attacker would need additional access to weaponize.** Document for cleanup, but don't burn the night on it.
- **Future-proof during rotation.** Don't just rotate — also migrate to a secret store (1Password, AWS Secrets Manager, etc.) so the next leak can't expose values. Each rotation is an opportunity to upgrade the storage pattern.
- **Leak vectors to watch for in this codebase:**
  - `grep PATTERN $secret_file` (direct value print) — addressed by secret-file-guard hook
  - `bash -x` debug traces (env vars printed during script execution) — no current hook
  - MCP server error formatters (e.g., axios 401 errors leak Authorization header) — documented in CLAUDE.md
  - `git diff` showing `.env.launchd` changes — addressed by .gitignore
  - Process list (`ps -ef`) showing env vars — only relevant if secrets are passed as CLI args, not env vars

# gogcli Auth Setup Guide

## First-Time Setup

### 1. Get OAuth2 Credentials

1. Open [Google Cloud Console Credentials](https://console.cloud.google.com/apis/credentials)
2. Create or select a project
3. Enable the APIs you need:
   - Gmail API, Calendar API, Drive API, Docs API, Sheets API, Slides API
   - People API (Contacts), Tasks API, Forms API
   - Chat API, Classroom API, Apps Script API (if needed)
   - Cloud Identity API (Groups), Keep API, Admin SDK API (Workspace only)
4. Configure [OAuth consent screen](https://console.cloud.google.com/auth/branding)
5. If app is in "Testing", [add test users](https://console.cloud.google.com/auth/audience)
6. Create OAuth client → Application type: "Desktop app" → Download JSON

### 2. Store Credentials

```bash
gog auth credentials ~/Downloads/client_secret_....json
```

For multiple OAuth clients:
```bash
gog --client work auth credentials ~/Downloads/work-client.json
gog auth credentials list
```

### 3. Authorize Account

```bash
# Browser flow (default)
gog auth add you@gmail.com

# Headless / remote server
gog auth add you@gmail.com --services user --manual

# Specific services only
gog auth add you@gmail.com --services gmail,calendar,drive

# Read-only
gog auth add you@gmail.com --services drive,calendar --readonly
```

### 4. Verify

```bash
gog auth status
gog gmail labels list
```

## Multiple Accounts

```bash
gog auth add personal@gmail.com
gog auth add work@company.com
gog auth alias set personal personal@gmail.com
gog auth alias set work work@company.com

# Use via flag or env
gog --account work gmail search 'newer_than:1d'
export GOG_ACCOUNT=work
```

## Multiple OAuth Clients

```bash
gog --client work auth credentials ~/Downloads/work.json --domain company.com
gog --client personal auth credentials ~/Downloads/personal.json
```

Client selection priority:
1. `--client` flag / `GOG_CLIENT` env
2. `account_clients` config (email -> client)
3. `client_domains` config (domain -> client)
4. Credentials file named after domain (`credentials-company.com.json`)
5. `default`

## Service Account (Workspace Only)

For Keep, Admin, and domain-wide delegation:

1. Create service account in Google Cloud Console
2. Enable domain-wide delegation
3. Download JSON key
4. Allowlist scopes in Workspace Admin Console → Security → API Controls → Domain-wide Delegation

```bash
gog auth service-account set you@domain.com --key ~/Downloads/sa.json
gog auth service-account status you@domain.com
```

## Keyring Backend

```bash
gog auth keyring              # Show current backend
gog auth keyring file         # Use encrypted file (avoids Keychain prompts)
gog auth keyring keychain     # Use macOS Keychain
gog auth keyring auto         # Auto-detect best
```

For CI/non-interactive:
```bash
export GOG_KEYRING_BACKEND=file
export GOG_KEYRING_PASSWORD='...'
gog --no-input auth status
```

## Scope Control

```bash
# Gmail scope levels
--gmail-scope full              # Default: modify + settings
--gmail-scope readonly          # Read-only

# Drive scope levels
--drive-scope full              # Default: full access
--drive-scope readonly          # Read-only
--drive-scope file              # Only files created by this app

# Extra scopes
--extra-scopes https://www.googleapis.com/auth/gmail.labels

# Re-authorize with new scopes
gog auth add you@gmail.com --services user --force-consent
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `403 insufficient scopes` | `gog auth add <email> --services <svc> --force-consent` |
| Token revoked/expired | `gog auth list --check` then re-add |
| Keychain keeps prompting | `gog auth keyring file` or use stable binary path |
| Service account 403 | Check domain-wide delegation allowlist in Workspace Admin |
| Remote/headless server | Use `--manual` or `--remote --step 1` / `--step 2` |

## Command Sandboxing

Restrict available commands (useful for agent/automated runs):

```bash
export GOG_ENABLE_COMMANDS=calendar,tasks,gmail
gog calendar events primary --today    # Works
gog drive ls                           # Blocked
```

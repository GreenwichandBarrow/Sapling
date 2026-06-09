# MacBook Codex VPS Setup

Paste these instructions into Codex on the MacBook.

## Goal

Make the MacBook point at the same canonical Sapling workspace used by the iMac and iPhone workflow:

```text
vps:/home/ubuntu/projects/Sapling
```

The MacBook should not recreate separate local Codex project folders for Chief of Staff, CFO, CIO, or family-office areas. Those role separations now live inside Sapling at:

```text
brain/operating-areas
```

## SSH Host

Create or update `~/.ssh/config` on the MacBook:

```sshconfig
Host vps
  HostName 100.67.36.25
  User ubuntu
  IdentityFile ~/.ssh/dodo-vps_ed25519
  IdentitiesOnly yes
```

Make sure the private key exists:

```bash
ls -l ~/.ssh/dodo-vps_ed25519
chmod 600 ~/.ssh/dodo-vps_ed25519
chmod 700 ~/.ssh
```

Verify SSH:

```bash
ssh vps 'whoami; echo $HOME; hostname; command -v codex; codex --version; ls -la /home/ubuntu/projects/Sapling'
```

Expected basics:

```text
ubuntu
/home/ubuntu
agent-vps-7731c88b
```

## Codex Auth On VPS

Verify Codex auth works on the VPS:

```bash
ssh vps 'codex login status'
```

Then run a real smoke test:

```bash
ssh vps 'cd /home/ubuntu/projects/Sapling && codex exec --sandbox read-only --ephemeral "Reply with exactly: remote-auth-ok"'
```

Expected final response:

```text
remote-auth-ok
```

If the smoke test fails with `token_invalidated`, `app_session_terminated`, or `Your session has ended`, replace the VPS auth cache from a Mac where Codex is logged in:

```bash
scp ~/.codex/auth.json vps:/home/ubuntu/.codex/auth.json
ssh vps 'chmod 600 ~/.codex/auth.json; codex login status'
```

## Codex App

In the MacBook Codex desktop app:

1. Open Settings > Connections.
2. Add or refresh SSH host `vps`.
3. Add/select this remote project folder:

```text
/home/ubuntu/projects/Sapling
```

Optional parent if the app needs to browse first:

```text
/home/ubuntu/projects
```

## Workspace Rule

Use this as the daily rule:

```text
If work should be available on iMac, MacBook, and iPhone, start it in vps:/home/ubuntu/projects/Sapling.
```

Role-specific material should be filed under:

```text
brain/operating-areas/c-suite/chief-of-staff
brain/operating-areas/c-suite/cfo
brain/operating-areas/c-suite/cio
brain/operating-areas/family-office
```

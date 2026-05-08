#!/bin/bash
# install_systemd_units.sh — install Phase 3 systemd unit templates on the server.
#
# Idempotent. Run on the Hetzner server from inside ~/projects/Sapling:
#   bash scripts/install_systemd_units.sh
#
# What it does:
#   1. Sets system timezone to America/New_York (so OnCalendar fires at ET)
#   2. Enables user-lingering for the current user (so timers fire even when
#      no SSH session is open)
#   3. Copies systemd/*.service and systemd/*.timer to ~/.config/systemd/user/
#   4. Runs `systemctl --user daemon-reload`
#   5. Lists installed timers and prints how to enable selectively
#
# What it does NOT do:
#   - Enable any timer (you enable per-skill after verifying secrets are set up).
#   - Touch the macOS launchd plists on your iMac.
#   - Modify .env.launchd or any other secrets.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SYSTEMD_SRC="$REPO_ROOT/systemd"
SYSTEMD_DST="$HOME/.config/systemd/user"
USERNAME="$(whoami)"

# ─── Sanity checks ────────────────────────────────────────────────────

if [[ "$(uname)" != "Linux" ]]; then
  echo "ERROR: this installer is for Linux only — current OS: $(uname)" >&2
  echo "       (the macOS host keeps running launchd jobs unchanged)" >&2
  exit 1
fi

if ! command -v systemctl >/dev/null 2>&1; then
  echo "ERROR: systemctl not found — this script requires systemd" >&2
  exit 1
fi

if [[ ! -d "$SYSTEMD_SRC" ]]; then
  echo "ERROR: $SYSTEMD_SRC not found — repo may not be in expected location" >&2
  exit 1
fi

# ─── 1. Set system timezone ───────────────────────────────────────────

CURRENT_TZ="$(timedatectl show --property=Timezone --value 2>/dev/null || echo unknown)"
if [[ "$CURRENT_TZ" != "America/New_York" ]]; then
  echo "[1/5] Setting timezone to America/New_York (was: $CURRENT_TZ)..."
  sudo timedatectl set-timezone America/New_York
else
  echo "[1/5] Timezone already America/New_York — skipping"
fi

# ─── 2. Enable user lingering ─────────────────────────────────────────

LINGER_STATUS="$(loginctl show-user "$USERNAME" -p Linger --value 2>/dev/null || echo no)"
if [[ "$LINGER_STATUS" != "yes" ]]; then
  echo "[2/5] Enabling user lingering for $USERNAME so timers fire without SSH..."
  sudo loginctl enable-linger "$USERNAME"
else
  echo "[2/5] User lingering already enabled — skipping"
fi

# ─── 3. Copy unit files ───────────────────────────────────────────────

mkdir -p "$SYSTEMD_DST"
echo "[3/5] Copying unit files from $SYSTEMD_SRC → $SYSTEMD_DST..."
unit_count=0
for f in "$SYSTEMD_SRC"/*.service "$SYSTEMD_SRC"/*.timer; do
  [[ -f "$f" ]] || continue
  cp "$f" "$SYSTEMD_DST/"
  unit_count=$((unit_count + 1))
done
echo "      copied $unit_count unit files"

# ─── 4. Reload systemd ────────────────────────────────────────────────

echo "[4/5] Reloading systemd user manager..."
systemctl --user daemon-reload

# ─── 5. Summary ───────────────────────────────────────────────────────

echo "[5/5] Installed but NOT enabled. To enable a single timer:"
echo "      systemctl --user enable --now <skill>.timer"
echo
echo "      Example:"
echo "      systemctl --user enable --now attio-snapshot-refresh.timer"
echo
echo "      To verify a timer is loaded:"
echo "      systemctl --user list-unit-files --type=timer | grep <skill>"
echo
echo "      To watch a timer fire:"
echo "      journalctl --user -u <skill>.service -f"
echo
echo "Available timers (currently disabled):"
ls "$SYSTEMD_DST"/*.timer 2>/dev/null | xargs -n1 basename | sed 's/^/      /'
echo
echo "Done. Total units installed: $unit_count"
echo "Excluded from server: post-call-analyzer (Granola sidecar — stays on iMac)"

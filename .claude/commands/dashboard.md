---
description: Open the G&B Command Center dashboard (Streamlit, server-hosted via systemd at https://agent-vps-7731c88b.tail868ef9.ts.net)
---

Open the Command Center dashboard.

**The dashboard runs persistently on the Sapling server** as a user-level systemd service (`dashboard.service`, `Restart=always`). It does not need to be "started" each session — it stays up across reboots. This skill verifies health and surfaces the URL Kay should open in her browser.

**Steps:**
1. Verify the service is active:
   ```bash
   ssh ubuntu@agent-vps-7731c88b "systemctl --user is-active dashboard.service"
   ```
2. If output is `active`, tell Kay it's live at **[https://agent-vps-7731c88b.tail868ef9.ts.net](https://agent-vps-7731c88b.tail868ef9.ts.net)** and stop. Note that refresh polling is every 60s. Magic DNS resolves the hostname over Tailscale — bookmarkable, works from any tailnet device (iMac, MacBook, iPhone with Tailscale connected).
3. If output is `inactive` or `failed`, attempt one restart:
   ```bash
   ssh ubuntu@agent-vps-7731c88b "systemctl --user restart dashboard.service"
   sleep 5
   ssh ubuntu@agent-vps-7731c88b "systemctl --user is-active dashboard.service"
   ```
4. If still not active after restart, surface recent logs without attempting further fixes:
   ```bash
   ssh ubuntu@agent-vps-7731c88b "journalctl --user -u dashboard.service -n 50 --no-pager"
   ```
   Tell Kay the service is down and show the log tail. Don't reinstall dependencies or recreate the venv (`/home/ubuntu/projects/Sapling/dashboard/.venv`) without asking — the venv was set up in Session 1 and should not be recreated casually.

**HTTP smoke-test (optional, after step 2 or 3):**
```bash
ssh ubuntu@agent-vps-7731c88b 'curl -s -o /dev/null -w "%{http_code}" http://localhost:8501'
```
Expect `200`. Use `localhost:8501` here because the curl runs ON the server; from Kay's browser the URL is the Magic DNS one.

**Scope & visual reference:**
- Scope doc: `brain/context/continuation-2026-04-24-dashboard-scope-locked.md`
- Visual language memory: `memory/feedback_dashboard_visual_language_locked.md`
- Mockups: `dashboard/mockup-landing.html`, `dashboard/mockup-deal-aggregator.html`

**Background:** Migrated from Mac-local Streamlit (former `localhost:8501` on Kay's iMac) to server-hosted Streamlit (systemd-managed, bound to `0.0.0.0:8501`, reachable via Tailscale Magic DNS) in early May 2026. See `~/.config/systemd/user/dashboard.service` for the unit definition.

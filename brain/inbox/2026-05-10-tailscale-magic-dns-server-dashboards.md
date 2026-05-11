---
schema_version: 1.2.0
date: 2026-05-10
title: Configure Tailscale Magic DNS for server dashboards
status: backlog
source: email
urgency: normal
confidence: high
automated: true
entity: "[[entities/harrison-wells]]"
source_ref: "msg:19de009cf5b8c59f"
source_url: "https://mail.google.com/mail/u/0/#inbox/19de009cf5b8c59f"
tags:
  - date/2026-05-10
  - inbox
  - source/email
  - urgency/normal
  - status/backlog
  - person/harrison-wells
  - topic/server
  - topic/security
---

# Configure Tailscale Magic DNS for server dashboards

## Description
Harrison Wells (msg 8 in the server-setup thread, 2026-05-08 20:29 CT) recommends enabling Tailscale Magic DNS so the Streamlit dashboard + any future server-hosted UIs are reachable only from devices on Kay's tailnet (MacBook + iMac + iPhone + server) instead of the open internet.

Action: ask Claude on the server to enable Magic DNS via `tailscale set --accept-dns` (or the Tailscale admin console toggle), then update the dashboard URL Kay opens each morning from `http://localhost:8501` / public IP to the Magic-DNS hostname (e.g. `http://agent-vps-7731c88b:8501`).

Final loop on Phase 1 of the dodo-vps server build. Not blocking pipeline work.

## Notes
*Not started*

## Outcome
*Pending*

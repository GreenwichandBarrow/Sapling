---
schema_version: 1.2.0
date: 2026-05-01
title: Harrison Wells — watch for Server Setup + Tailscale email
status: done
source: call
urgency: medium
source_ref: "[[calls/2026-04-30-harrison-wells-coaching-session]]"
confidence: high
tags: [date/2026-05-01, inbox, source/call, person/harrison-wells, company/dodo-digital, topic/server-migration, topic/tailscale, topic/claude-infrastructure, urgency/medium, status/done]
---

# Harrison Wells — watch for Server Setup + Tailscale email

## Description

Per the 4/30 coaching session, Harrison committed to sending a Server Setup + Tailscale walkthrough email — Hetzner repo + how-to for migrating Kay's scheduled jobs off Mac-dependent launchd to a proper server with Tailscale for secure access.

## Action

- Watch inbox for Harrison's email (subject likely contains "Hetzner", "Server Setup", or "Tailscale").
- When it arrives, route to Hetzner-migration umbrella project for review and beads breakdown.
- If not received within 5 business days, send Harrison a soft nudge.

## Context

- Source: [[calls/2026-04-30-harrison-wells-coaching-session]] section B.1.
- Hetzner migration is the umbrella project — single source of truth replacing local-dual-machine setup ($12/mo tier). Kay confirmed *"I'm definitely going to do that."*
- Walkthrough is the prerequisite reading before Kay or any agent starts the migration work.
- Related: [[entities/harrison-wells]], [[entities/dodo-digital]].

## Resolution

Closed 2026-05-10. Harrison did send the Server Setup + Tailscale email (4/30). Migration is complete: Hetzner cpx21 cutover finished 5/8, Tailscale SSH wired, 1Password vault migrated 5/10. No further action — superseded by completed work.

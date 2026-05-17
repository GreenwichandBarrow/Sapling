---
name: reference-vps-broken-pipe-use-agent-tmux
description: "Kay's recurring \"VPS disconnects / broken pipe\" is an SSH idle timeout — launch via agent/tmux to survive it"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 7b223302-fb2c-4eb1-b17a-bf9f0dcd0466
---

Kay's repeated "the VPS disconnects and tells me the pipe is broken, I have to login again" is **not a server failure** (8+ days uptime, no reboot/OOM confirmed 2026-05-16). It is an **SSH broken pipe from idle timeout**: server `ClientAliveInterval 300 / ClientAliveCountMax 2` vs ~60–120s home/office NAT idle drop. During long agent runs no terminal traffic flows, the NAT mapping dies before the server's first keepalive probe, and foreground `claude` dies with the tunnel — taking uncaptured session-decisions with it.

**How to apply:** Tell Kay to launch Claude via the `agent` alias (detached tmux on the VPS), then `tmux attach -t agent` to resume after any pipe break — Claude keeps running server-side, nothing lost. NOT a Harrison server-stability topic. Two open follow-ups: (1) optional sshd hardening `ClientAliveInterval 60 / CountMax 15` (pending Kay YES/NO — edits sshd_config, validate with `sshd -t`, reload not restart); (2) decision-capture fragility is a real resilience design item for Harrison infra batch (auto-checkpoint session-decisions / scheduled fallback so a dropped pipe never costs the record). Related: [[feedback-test-op-resolution-before-declaring-auth-down]]

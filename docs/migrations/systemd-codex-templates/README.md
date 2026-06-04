# Codex Systemd Cutover Templates

These are non-live cutover notes for Phase 1. Do not copy them into
`~/.config/systemd/user` until the matching workflow or workflow cluster has
passed manual Codex validation.

## Standard Service Swap

For generated agent-backed services, the Phase 1 cutover is a one-line
`ExecStart` change:

```ini
ExecStart=/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh <skill> [args]
```

Keep existing timer schedules, `WorkingDirectory`, `EnvironmentFile`, `PATH`,
and install targets unchanged.

## Workflow Mapping

| Service | Codex ExecStart | Cutover group |
| --- | --- | --- |
| `calibration-workflow.service` | `/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh calibration-workflow` | calibration |
| `conference-discovery.service` | `/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh conference-discovery sunday` | conference |
| `deal-aggregator.service` | `/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh deal-aggregator` | deal-aggregator |
| `deal-aggregator-afternoon.service` | `/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh deal-aggregator --afternoon` | deal-aggregator |
| `deal-aggregator-friday.service` | `/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh deal-aggregator --digest-mode` | deal-aggregator |
| `email-intelligence.service` | `/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh email-intelligence` | email-intelligence |
| `health-monitor.service` | `/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh health-monitor` | health-monitor pilot |
| `jj-operations-sunday.service` | `/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh jj-operations:sunday-prep` | jj-operations |
| `launchd-debugger.service` | `/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh launchd-debugger daily` | launchd-debugger |
| `niche-intelligence.service` | `/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh niche-intelligence tuesday` | niche-intelligence |
| `nightly-tracker-audit.service` | `/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh nightly-tracker-audit nightly` | tracker-audit |
| `relationship-manager.service` | `/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh relationship-manager daily` | relationship-manager |
| `target-discovery-sunday.service` | `/bin/bash %h/projects/Sapling/scripts/run-agent-skill.sh target-discovery phase2-sunday` | target-discovery |

## Special Case: Post-Call Analyzer

`post-call-analyzer-poll.service` calls `scripts/post_call_analyzer_poll.sh`,
which internally launches the old runner. Cutover should change the service to:

```ini
ExecStart=/bin/bash %h/projects/Sapling/scripts/post_call_analyzer_poll.codex.sh
```

Keep `KillMode=process` because the poller deliberately detaches the analyzer
child process.

## Agent-Free Direct Scripts

The following services appeared agent-free during the Phase 1 scan and should
remain unchanged unless later validation proves otherwise:

- `apollo-credits-refresh.service`
- `attio-snapshot-refresh.service`
- `external-services-probe.service`
- `jj-snapshot-refresh.service`
- `weekly-archive-export.service`
- `weekly-snapshot.service`

`external-services-probe` still probes Claude/Anthropic as an external service
health check. That is not a Codex runtime dependency, but it is a Phase 2 cleanup
candidate.

## Controlled Cutover Procedure

1. Confirm `scripts/check-codex-migration-readiness.sh` passes.
2. Run the workflow manually through `scripts/run-agent-skill.sh`.
3. Inspect `logs/scheduled/` and the workflow output artifacts.
4. Update the relevant service file in `~/.config/systemd/user`.
5. Run `systemctl --user daemon-reload`.
6. Run `systemctl --user start <service>`.
7. If validation fails, restore that service from
   `/home/ubuntu/backups/claude-to-codex-20260604-161906/systemd-user/`.

#!/usr/bin/env python3
"""Probe external services for the Infrastructure Zone 2 dashboard tile.

Each probe returns (status, latency_ms, message). Snapshot lands at
brain/context/external-services-snapshot.json. Loader merges this over the
hand-curated YAML — YAML stays source of truth for labels/order/descriptions,
snapshot overrides the live-probable fields (health + status text + latency).

Probes are wrapped in try/except + per-probe timeout so one slow service
can't drag the whole run past the 60s budget. All probes execute in
parallel via a thread pool.

Secrets discipline: API keys are read from os.environ — never logged,
never echoed. Errors surface only the failure category, not the key value.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

REPO_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT_PATH = REPO_ROOT / "brain" / "context" / "external-services-snapshot.json"

PROBE_TIMEOUT_SEC = 15      # per-probe network ceiling
TOTAL_BUDGET_SEC = 55       # leave headroom under launchd's 60s expectation


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------


def _result(status: str, latency_ms: int | None, message: str,
            skip_reason: str | None = None) -> dict:
    return {
        "status": status,            # ok | warn | error | skip
        "latency_ms": latency_ms,
        "message": message,
        "skip_reason": skip_reason,
    }


def _skip(reason: str) -> dict:
    return _result("skip", None, "", skip_reason=reason)


def _run(cmd: list[str], timeout: int = PROBE_TIMEOUT_SEC) -> tuple[int, str, str, int]:
    """subprocess.run wrapper that returns (returncode, stdout, stderr, elapsed_ms)."""
    start = time.monotonic()
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )
    elapsed = int((time.monotonic() - start) * 1000)
    return proc.returncode, proc.stdout, proc.stderr, elapsed


def _http_status_and_time(url: str, method: str = "GET",
                          headers: list[str] | None = None,
                          data: str | None = None,
                          timeout: int = PROBE_TIMEOUT_SEC) -> tuple[int, float] | None:
    """curl-based HTTP probe. Returns (http_code, time_total_sec) or None on hard fail."""
    cmd = ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}|%{time_total}",
           "--max-time", str(timeout), "-X", method]
    for h in headers or []:
        cmd.extend(["-H", h])
    if data is not None:
        cmd.extend(["-d", data])
    cmd.append(url)
    try:
        rc, out, _err, _ms = _run(cmd, timeout=timeout + 2)
    except subprocess.TimeoutExpired:
        return None
    if rc != 0 or "|" not in out:
        return None
    code_str, time_str = out.strip().split("|", 1)
    try:
        return int(code_str), float(time_str)
    except ValueError:
        return None


# -----------------------------------------------------------------------------
# Individual probes
# -----------------------------------------------------------------------------


def probe_gog() -> dict:
    if not shutil.which("gog"):
        return _result("error", None, "gog CLI not on PATH")
    try:
        rc, out, err, ms = _run(["gog", "auth", "status", "--json"])
    except subprocess.TimeoutExpired:
        return _result("error", PROBE_TIMEOUT_SEC * 1000, "timed out")
    if rc != 0:
        return _result("error", ms, f"exit {rc}")
    # gog --json may return either an authenticated payload or an envelope;
    # treat any successful JSON parse with non-empty stdout as healthy.
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        return _result("warn", ms, "non-JSON response")
    # Look for any common authenticated marker; fall back to "exit 0 = healthy"
    authed = False
    if isinstance(data, dict):
        for k in ("authenticated", "ok", "valid"):
            if data.get(k) is True:
                authed = True
                break
        if not authed and (data.get("account") or data.get("email") or data.get("status")):
            authed = True
    if authed or rc == 0:
        return _result("ok", ms, "authenticated")
    return _result("warn", ms, "auth state unclear")


def probe_github() -> dict:
    if not shutil.which("gh"):
        return _result("error", None, "gh CLI not on PATH")
    try:
        rc, _out, _err, ms = _run(["gh", "auth", "status"])
    except subprocess.TimeoutExpired:
        return _result("error", PROBE_TIMEOUT_SEC * 1000, "timed out")
    if rc == 0:
        return _result("ok", ms, "gh authenticated")
    return _result("error", ms, f"gh auth status exit {rc}")


def probe_apollo() -> dict:
    key = os.environ.get("APOLLO_API_KEY")
    if not key:
        return _result("error", None, "APOLLO_API_KEY not set")
    res = _http_status_and_time(
        "https://api.apollo.io/v1/auth/health",
        headers=[f"X-Api-Key: {key}"],
    )
    if res is None:
        return _result("error", None, "request failed")
    code, secs = res
    ms = int(secs * 1000)
    if code == 200:
        return _result("ok", ms, "200 OK")
    if code == 401:
        return _result("error", ms, "401 unauthorized")
    return _result("warn", ms, f"HTTP {code}")


def probe_anthropic() -> dict:
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        return _skip("ANTHROPIC_API_KEY not in env")
    body = json.dumps({
        "model": "claude-haiku-4-5-20251001",
        "max_tokens": 1,
        "messages": [{"role": "user", "content": "hi"}],
    })
    res = _http_status_and_time(
        "https://api.anthropic.com/v1/messages",
        method="POST",
        headers=[
            f"x-api-key: {key}",
            "anthropic-version: 2023-06-01",
            "content-type: application/json",
        ],
        data=body,
    )
    if res is None:
        return _result("error", None, "request failed")
    code, secs = res
    ms = int(secs * 1000)
    if code == 200:
        return _result("ok", ms, "200 OK")
    if code in (401, 403):
        return _result("error", ms, f"HTTP {code} (key issue)")
    return _result("warn", ms, f"HTTP {code}")


def probe_slack_webhooks() -> dict:
    """Per feedback_one_webhook_test: don't ping live, just confirm vars exist."""
    expected = [
        "SLACK_WEBHOOK_AI_OPERATIONS",
        "SLACK_WEBHOOK_SVA",
        "SLACK_WEBHOOK_OPERATIONS",
        "SLACK_WEBHOOK_ACTIVE_DEALS",
        "SLACK_WEBHOOK_STRATEGY_OPS",
    ]
    present = [name for name in expected if os.environ.get(name, "").strip()]
    if not present:
        return _result("error", None, "no webhooks in env")
    if len(present) < 2:
        return _result("warn", None, f"only {len(present)} webhook(s) configured")
    return _result("ok", None, f"{len(present)} webhooks configured")


def probe_granola_mcp() -> dict:
    res = _http_status_and_time(
        "https://mcp.granola.ai/mcp",
        method="HEAD",
    )
    if res is None:
        return _result("error", None, "request failed")
    code, secs = res
    ms = int(secs * 1000)
    if code in (200, 204, 405):  # 405 is acceptable for HEAD on a POST endpoint
        return _result("ok", ms, f"HTTP {code}")
    if code in (401, 403):
        # Endpoint reachable but requires auth — that's still "service is up"
        return _result("ok", ms, f"HTTP {code} (auth-gated, service up)")
    return _result("warn", ms, f"HTTP {code}")


def probe_launchd() -> dict:
    try:
        rc, out, _err, ms = _run(["launchctl", "list"])
    except subprocess.TimeoutExpired:
        return _result("error", PROBE_TIMEOUT_SEC * 1000, "timed out")
    if rc != 0:
        return _result("error", ms, f"launchctl list exit {rc}")
    count = sum(1 for line in out.splitlines() if "greenwich" in line)
    msg = f"{count} jobs registered"
    if count >= 10:
        return _result("ok", ms, msg)
    if count >= 5:
        return _result("warn", ms, msg)
    return _result("error", ms, msg)


def probe_vault() -> dict:
    start = time.monotonic()
    try:
        brain_dir = REPO_ROOT / "brain"
        if not brain_dir.is_dir():
            return _result("error", 0, "brain/ missing")
        count = sum(1 for _ in brain_dir.rglob("*.md"))
    except OSError as e:
        return _result("error", None, f"scan failed: {e}")
    ms = int((time.monotonic() - start) * 1000)
    if count > 100:
        return _result("ok", ms, f"{count} markdown files")
    if count > 0:
        return _result("warn", ms, f"only {count} markdown files")
    return _result("error", ms, "no markdown files")


def probe_mcp_processes() -> dict:
    """Liveness check for attio-mcp / superhuman MCP processes."""
    try:
        rc, out, _err, ms = _run(["ps", "ax"])
    except subprocess.TimeoutExpired:
        return _result("error", PROBE_TIMEOUT_SEC * 1000, "timed out")
    if rc != 0:
        return _result("error", ms, f"ps exit {rc}")
    attio = sum(1 for ln in out.splitlines() if "attio-mcp" in ln and "grep" not in ln)
    superhuman = sum(1 for ln in out.splitlines()
                     if "superhuman" in ln.lower() and "grep" not in ln)
    total = attio + superhuman
    msg = f"attio-mcp={attio} superhuman={superhuman}"
    if total >= 2:
        return _result("ok", ms, msg)
    if total >= 1:
        return _result("warn", ms, msg)
    return _result("error", ms, msg)


# -----------------------------------------------------------------------------
# Skipped (OAuth-gated, Kay handles in browser)
# -----------------------------------------------------------------------------


def probe_attio_mcp() -> dict:
    return _skip("OAuth re-flow required (Smithery UI)")


def probe_superhuman() -> dict:
    return _skip("OAuth refresh required (manual)")


def probe_linkt() -> dict:
    return _skip("Browser session required (no API)")


# -----------------------------------------------------------------------------
# Probe registry — keys MUST match dashboard/data/external_services.yaml `name` field
# -----------------------------------------------------------------------------


PROBES: dict[str, Callable[[], dict]] = {
    "gog": probe_gog,
    "github": probe_github,
    "apollo": probe_apollo,
    "claude-api": probe_anthropic,
    "slack-webhooks": probe_slack_webhooks,
    "granola": probe_granola_mcp,
    "launchd": probe_launchd,
    "vault": probe_vault,
    "attio-mcp": probe_attio_mcp,
    "superhuman": probe_superhuman,
    "linkt": probe_linkt,
    # MCP-process liveness is informational; not a yaml row, but useful for ops
    "mcp-processes": probe_mcp_processes,
}


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


def run_all() -> dict[str, dict]:
    """Run every probe in parallel with a global wall-clock budget."""
    results: dict[str, dict] = {}
    deadline = time.monotonic() + TOTAL_BUDGET_SEC

    with ThreadPoolExecutor(max_workers=len(PROBES)) as ex:
        futures = {ex.submit(_safe_probe, name, fn): name for name, fn in PROBES.items()}
        for fut in as_completed(futures):
            name = futures[fut]
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                results[name] = _result("error", None, "global budget exceeded")
                continue
            try:
                results[name] = fut.result(timeout=max(remaining, 1))
            except Exception as e:                       # noqa: BLE001
                results[name] = _result("error", None, f"probe crashed: {type(e).__name__}")
    # Fill in any names that didn't return (shouldn't happen, but defensive)
    for name in PROBES:
        results.setdefault(name, _result("error", None, "no result"))
    return results


def _safe_probe(name: str, fn: Callable[[], dict]) -> dict:
    try:
        return fn()
    except subprocess.TimeoutExpired:
        return _result("error", PROBE_TIMEOUT_SEC * 1000, "timed out")
    except Exception as e:                              # noqa: BLE001
        # Never let one probe leak details that might include a header value
        return _result("error", None, f"{type(e).__name__}")


def main() -> int:
    services = run_all()
    snapshot = {
        "fetched_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "services": services,
    }
    SNAPSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    SNAPSHOT_PATH.write_text(json.dumps(snapshot, indent=2))
    # Summary to stderr — never include key values
    ok = sum(1 for r in services.values() if r["status"] == "ok")
    warn = sum(1 for r in services.values() if r["status"] == "warn")
    err = sum(1 for r in services.values() if r["status"] == "error")
    skip = sum(1 for r in services.values() if r["status"] == "skip")
    print(f"[probe] wrote {SNAPSHOT_PATH} — ok={ok} warn={warn} error={err} skip={skip}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

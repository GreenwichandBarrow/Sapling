"""Infrastructure page — system health, external connectivity, credits, calibration, tech stack.

Five zones per the locked scope (`continuation-2026-04-24-dashboard-scope-locked.md`,
Section 5). This v1 ships **Zones 1 + 5 only** — those are pure local data with
no external auth. Zones 2 (External Connectivity), 3 (Credits & Spend), and 4
(Calibration & Learning) require auth probes / billing API access / calibration-
workflow output and are deferred to Session 5 part 2 (supervised work).

Zone 1 (System Health) renders 8 tiles built from local probes:
- launchctl list count
- launchctl spec vs registered (catches health-monitor's missing plist)
- log files writing today
- hooks configured (parses settings.json)
- disk space (statvfs on the volume holding the repo)
- vault frontmatter validation count
- last commit age
- briefing pipeline (proxy via pipeline-manager log)

Zone 5 (Tech Stack Inventory) renders the 28-service / 13-category catalog
from `dashboard/data/tech_stack.yaml`, validated against Kay's actual stack
on 2026-04-24.
"""

from __future__ import annotations

from html import escape
from textwrap import dedent

import sys
from pathlib import Path

_DASHBOARD_DIR = Path(__file__).resolve().parent.parent
if str(_DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(_DASHBOARD_DIR))

from data_sources import (  # noqa: E402
    CalibrationEntry,
    CalibrationLog,
    CreditTile,
    ExternalService,
    HealthTile,
    StackCategory,
    StackService,
    external_services_summary,
    load_calibration_log,
    load_credit_tiles,
    load_external_services,
    load_system_health,
    load_tech_stack,
    system_health_summary,
    tech_stack_count,
)


_HEALTH_DOT_CLASS = {
    "ok": "green",
    "warn": "yellow",
    "alert": "red",
    "unknown": "grey",
}

_HEALTH_TILE_CLASS = {
    "ok": "",
    "warn": " warn",
    "alert": " alert",
    "unknown": "",
}


def _render_health_tile(tile: HealthTile) -> str:
    dot = _HEALTH_DOT_CLASS.get(tile.status, "grey")
    extra = _HEALTH_TILE_CLASS.get(tile.status, "")
    return dedent(
        f"""
        <div class="gb-health-tile{extra}">
        <div class="gb-health-tile-label">{escape(tile.label)}</div>
        <div class="gb-health-tile-value">
        <span class="gb-status-dot {dot}"></span>
        {escape(tile.value)}
        </div>
        <div class="gb-health-tile-detail">{escape(tile.detail)}</div>
        </div>
        """
    ).strip()


def _render_zone_1(tiles: list[HealthTile]) -> str:
    summary = system_health_summary(tiles)
    pills = []
    if summary["healthy"]:
        pills.append(f'<span class="pill">{summary["healthy"]} healthy</span>')
    if summary["warn"]:
        pills.append(f'<span class="pill yellow">{summary["warn"]} warn</span>')
    if summary["alert"]:
        pills.append(f'<span class="pill red">{summary["alert"]} alert</span>')
    if summary["unknown"]:
        pills.append(f'<span class="pill neutral">{summary["unknown"]} unknown</span>')
    head = dedent(
        f"""
        <div class="gb-zone-head">
        <div>
        <div class="gb-zone-label">System Health</div>
        <div class="gb-zone-sublabel">Dashboard, VPS access, AI runtimes, git sync, and disk</div>
        </div>
        <div class="gb-zone-meta">{''.join(pills)}</div>
        </div>
        """
    ).strip()
    grid = '<div class="gb-health-grid">'
    grid += "".join(_render_health_tile(t) for t in tiles)
    grid += "</div>"
    return f'<section class="gb-zone">{head}{grid}</section>'



def _render_usage_tile(tile: CreditTile) -> str:
    status = {"green": "ok", "yellow": "warn", "red": "alert"}.get(tile.runway_color, "unknown")
    dot = _HEALTH_DOT_CLASS.get(status, "grey")
    extra = _HEALTH_TILE_CLASS.get(status, "")
    runway = tile.runway_text.split(" · ")[0] if tile.runway_text else ""
    trend = tile.trend or ""
    trend_html = f'<span class="gb-usage-trend">{escape(trend)}</span>' if trend else ""
    return dedent(
        f"""
        <div class="gb-health-tile gb-usage-tile{extra}">
        <div class="gb-health-tile-label">{escape(tile.label)}</div>
        <div class="gb-health-tile-value">
        <span class="gb-status-dot {dot}"></span>
        {escape(tile.value)} <span class="unit">{escape(tile.unit)}</span>
        </div>
        <div class="gb-health-tile-detail">{escape(runway)}{trend_html}</div>
        </div>
        """
    ).strip()


def _render_zone_system_usage(health_tiles: list[HealthTile], credits: list[CreditTile]) -> str:
    health = system_health_summary(health_tiles)
    in_range = sum(1 for t in credits if t.runway_color == "green")
    pending = sum(1 for t in credits if t.runway_color == "none")
    monitor = sum(1 for t in credits if t.runway_color == "yellow")
    alert = sum(1 for t in credits if t.runway_color == "red")
    pills = []
    if health["healthy"]:
        pills.append(f'<span class="pill">{health["healthy"]} healthy</span>')
    if health["warn"]:
        pills.append(f'<span class="pill yellow">{health["warn"]} warn</span>')
    if health["alert"]:
        pills.append(f'<span class="pill red">{health["alert"]} alert</span>')
    if in_range:
        pills.append(f'<span class="pill">{in_range} usage in range</span>')
    if monitor:
        pills.append(f'<span class="pill yellow">{monitor} usage monitor</span>')
    if alert:
        pills.append(f'<span class="pill red">{alert} usage alert</span>')
    if pending:
        pills.append(f'<span class="pill neutral">{pending} usage pending</span>')
    head = dedent(
        f"""
        <div class="gb-zone-head">
        <div>
        <div class="gb-zone-label">System Health &amp; Usage</div>
        <div class="gb-zone-sublabel">Dashboard runtime, VPS access, AI runtimes, git sync, disk, Apollo, Anthropic, and OpenAI usage</div>
        </div>
        <div class="gb-zone-meta">{''.join(pills)}</div>
        </div>
        """
    ).strip()
    tiles = "".join(_render_health_tile(t) for t in health_tiles) + "".join(_render_usage_tile(t) for t in credits)
    return f'<section class="gb-zone gb-system-usage-zone">{head}<div class="gb-health-grid">{tiles}</div></section>'

def _render_stack_chip(service: StackService) -> str:
    health = service.health if service.health in ("ok", "warn", "alert", "retired") else "ok"
    dot_class = {
        "ok": "",
        "warn": " yellow",
        "alert": " red",
        "retired": " dim",
    }.get(health, "")
    note_html = (
        f'<span class="note">{escape(service.note)}</span>' if service.note else ""
    )
    return (
        f'<span class="gb-stack-chip">'
        f'<span class="gb-stack-dot{dot_class}"></span>{escape(service.name)}{note_html}'
        f"</span>"
    )


def _render_stack_row(category: StackCategory) -> str:
    chips = "".join(_render_stack_chip(s) for s in category.services)
    return dedent(
        f"""
        <div class="gb-stack-row">
        <div class="gb-stack-cat">{escape(category.label)}</div>
        <div class="gb-stack-chips">{chips}</div>
        </div>
        """
    ).strip()


def _stack_health_summary(categories: list[StackCategory]) -> dict[str, int]:
    counts = {"total": 0, "healthy": 0, "warn": 0, "alert": 0, "retired": 0}
    for category in categories:
        for service in category.services:
            counts["total"] += 1
            if service.health == "warn":
                counts["warn"] += 1
            elif service.health == "alert":
                counts["alert"] += 1
            elif service.health == "retired":
                counts["retired"] += 1
            else:
                counts["healthy"] += 1
    return counts


def _render_stack_inventory(categories: list[StackCategory]) -> str:
    rows = "".join(_render_stack_row(c) for c in categories)
    return f'<div class="gb-stack-list gb-stack-list-compact">{rows}</div>'


def _render_zone_5(categories: list[StackCategory]) -> str:
    n = tech_stack_count(categories)
    head = dedent(
        f"""
        <div class="gb-zone-head">
        <div>
        <div class="gb-zone-label">Tech Stack · Full Inventory</div>
        <div class="gb-zone-sublabel">Every service in active use · validated against operator stack 2026-04-24</div>
        </div>
        <div class="gb-zone-meta">{n} services · {len(categories)} categories</div>
        </div>
        """
    ).strip()
    rows = "".join(_render_stack_row(c) for c in categories)
    return f'<section class="gb-zone">{head}<div class="gb-stack-list">{rows}</div></section>'


_HEALTH_TO_DOT = {"ok": "green", "warn": "yellow", "alert": "red"}


def _render_service_row(svc: ExternalService) -> str:
    dot = _HEALTH_TO_DOT.get(svc.health, "grey")
    status_class = "gb-svc-status"
    if svc.health == "ok":
        status_class += " healthy"
    elif svc.health == "warn":
        status_class += " warn"
    elif svc.health == "alert":
        status_class += " alert"
    kind_class = "svc" if svc.kind == "service" else "local"
    return dedent(
        f"""
        <div class="gb-svc-row">
        <span class="gb-status-dot {dot}"></span>
        <div class="gb-svc-cell">
        <div class="gb-svc-name">{escape(svc.name)}<span class="kind {kind_class}">{escape(svc.kind)}</span></div>
        <div class="gb-svc-desc">{escape(svc.description)}</div>
        </div>
        <div class="{status_class}">{escape(svc.status_text)}</div>
        <div class="gb-svc-action {escape(svc.action)}">{escape(svc.action_text)}</div>
        <div class="gb-svc-chevron">›</div>
        </div>
        """
    ).strip()


def _render_zone_2(services: list[ExternalService]) -> str:
    summary = external_services_summary(services)
    pills = []
    if summary["healthy"]:
        pills.append(f'<span class="pill">{summary["healthy"]} healthy</span>')
    if summary["warn"]:
        pills.append(f'<span class="pill yellow">{summary["warn"]} warn</span>')
    if summary["alert"]:
        pills.append(f'<span class="pill red">{summary["alert"]} needs key</span>')
    head = dedent(
        f"""
        <div class="gb-zone-head">
        <div>
        <div class="gb-zone-label">External Connectivity &amp; Tooling</div>
        <div class="gb-zone-sublabel">Auth, API keys, MCP servers, local tools · status is the headline, action is one click</div>
        </div>
        <div class="gb-zone-meta">{summary["total"]} services {''.join(pills)}</div>
        </div>
        """
    ).strip()
    # Sort: alerts first, then warns, then healthy — surfaces what needs action
    order = {"alert": 0, "warn": 1, "ok": 2}
    sorted_services = sorted(services, key=lambda s: order.get(s.health, 3))
    body = "".join(_render_service_row(s) for s in sorted_services)
    return f'<section class="gb-zone">{head}<div>{body}</div></section>'


def _render_zone_tooling(services: list[ExternalService], categories: list[StackCategory]) -> str:
    service_summary = external_services_summary(services)
    stack_summary = _stack_health_summary(categories)
    pills = []
    if service_summary["healthy"]:
        pills.append(f'<span class="pill">{service_summary["healthy"]} healthy</span>')
    if service_summary["warn"]:
        pills.append(f'<span class="pill yellow">{service_summary["warn"]} warn</span>')
    if service_summary["alert"]:
        pills.append(f'<span class="pill red">{service_summary["alert"]} needs action</span>')

    head = dedent(
        f"""
        <div class="gb-zone-head">
        <div>
        <div class="gb-zone-label">Tooling &amp; Integrations</div>
        <div class="gb-zone-sublabel">Connected services, local tools, and stack inventory · issues first, inventory below</div>
        </div>
        <div class="gb-zone-meta">{service_summary["total"]} monitored · {stack_summary["total"]} inventory {''.join(pills)}</div>
        </div>
        """
    ).strip()

    action_services = [s for s in services if s.health in ("alert", "warn")]
    order = {"alert": 0, "warn": 1, "ok": 2}
    action_services.sort(key=lambda s: order.get(s.health, 3))
    if action_services:
        action_rows = "".join(_render_service_row(s) for s in action_services)
    else:
        action_rows = '<div class="gb-zone-empty">No integration issues.</div>'

    inventory_head = dedent(
        f"""
        <div class="gb-tooling-subhead">
        <span>Full stack inventory</span>
        <span>{stack_summary["total"]} tools · {len(categories)} categories</span>
        </div>
        """
    ).strip()
    return (
        f'<section class="gb-zone gb-tooling-zone">{head}'
        f'<div class="gb-tooling-actions">{action_rows}</div>'
        f'{inventory_head}{_render_stack_inventory(categories)}</section>'
    )



def _render_zone_tooling_inventory(categories: list[StackCategory]) -> str:
    stack_summary = _stack_health_summary(categories)
    pills = []
    if stack_summary["healthy"]:
        pills.append(f'<span class="pill">{stack_summary["healthy"]} healthy</span>')
    if stack_summary["warn"]:
        pills.append(f'<span class="pill yellow">{stack_summary["warn"]} watch</span>')
    if stack_summary["alert"]:
        pills.append(f'<span class="pill red">{stack_summary["alert"]} issue</span>')
    head = dedent(
        f"""
        <div class="gb-zone-head">
        <div>
        <div class="gb-zone-label">Tech Stack &amp; Tooling</div>
        <div class="gb-zone-sublabel">Reference inventory only · operational issues surface above or on the relevant page</div>
        </div>
        <div class="gb-zone-meta">{stack_summary["total"]} tools · {len(categories)} categories {''.join(pills)}</div>
        </div>
        """
    ).strip()
    return f'<section class="gb-zone">{head}{_render_stack_inventory(categories)}</section>'

def _render_credit_tile(tile: CreditTile) -> str:
    arrow_glyph = {"up": "↑", "down": "↓", "flat": "→"}.get(tile.trend_arrow, "→")
    runway_color_class = (
        f' class="{tile.runway_color}"'
        if tile.runway_color in ("green", "yellow", "red")
        else ""
    )
    if tile.runway_color in ("green", "yellow", "red"):
        runway_html = (
            f'<span{runway_color_class}>{escape(tile.runway_text.split(" · ")[0])}</span>'
            f'{escape(" · " + " · ".join(tile.runway_text.split(" · ")[1:])) if " · " in tile.runway_text else ""}'
        )
    else:
        runway_html = escape(tile.runway_text)
    return dedent(
        f"""
        <div class="gb-credit-tile">
        <div class="gb-credit-label">{escape(tile.label)}</div>
        <div class="gb-credit-value">{escape(tile.value)} <span class="unit">{escape(tile.unit)}</span></div>
        <div class="gb-credit-runway">{runway_html}</div>
        <div class="gb-credit-trend"><span class="arrow {tile.trend_arrow}">{arrow_glyph}</span><span>{escape(tile.trend)}</span></div>
        </div>
        """
    ).strip()


def _render_zone_3(tiles: list[CreditTile]) -> str:
    in_range = sum(1 for t in tiles if t.runway_color == "green")
    monitor = sum(1 for t in tiles if t.runway_color == "yellow")
    alert = sum(1 for t in tiles if t.runway_color == "red")
    pills = []
    if in_range:
        pills.append(f'<span class="pill">{in_range} in range</span>')
    if monitor:
        pills.append(f'<span class="pill yellow">{monitor} monitor</span>')
    if alert:
        pills.append(f'<span class="pill red">{alert} renewal</span>')
    head = dedent(
        f"""
        <div class="gb-zone-head">
        <div>
        <div class="gb-zone-label">Credits &amp; Subscription Spend</div>
        <div class="gb-zone-sublabel">Operational runway · what depletes, when, at current burn</div>
        </div>
        <div class="gb-zone-meta">{''.join(pills)}</div>
        </div>
        """
    ).strip()
    body = "".join(_render_credit_tile(t) for t in tiles)
    return f'<section class="gb-zone">{head}<div class="gb-credits-grid">{body}</div></section>'


def _render_calibration_entry(e: CalibrationEntry) -> str:
    return dedent(
        f"""
        <div class="gb-calib-entry">
        <div class="gb-calib-icon {escape(e.icon_color)}">{escape(e.icon)}</div>
        <div>
        <div class="gb-calib-headline">{escape(e.headline)}</div>
        <div class="gb-calib-detail">{e.detail}</div>
        </div>
        <div class="gb-calib-when">{escape(e.when)}</div>
        </div>
        """
    ).strip()


def _render_zone_4(log: CalibrationLog) -> str:
    head = dedent(
        f"""
        <div class="gb-zone-head">
        <div>
        <div class="gb-zone-label">Calibration &amp; Learning · This Week</div>
        <div class="gb-zone-sublabel">What the system codified, retired, or refreshed since last Friday</div>
        </div>
        <div class="gb-zone-meta">{len(log.entries)} updates · last run {escape(log.last_run)}</div>
        </div>
        """
    ).strip()
    if not log.entries:
        body = '<div class="gb-zone-empty">No calibration entries this week.</div>'
    else:
        body = "".join(_render_calibration_entry(e) for e in log.entries)
    return f'<section class="gb-zone">{head}<div>{body}</div></section>'


def _render_subtitle() -> str:
    return (
        '<div class="gb-subtitle">'
        "System health, external connectivity, credits &amp; spend."
        "</div>"
    )


def _render_summary(health_tiles: list[HealthTile], credits: list[CreditTile], stack: list[StackCategory]) -> str:
    """Top operating status across system health, usage freshness, and tooling inventory."""
    health = system_health_summary(health_tiles)
    credits_in_range = sum(1 for t in credits if t.runway_color == "green")
    credits_monitor = sum(1 for t in credits if t.runway_color == "yellow")
    credits_alert = sum(1 for t in credits if t.runway_color == "red")
    credits_pending = sum(1 for t in credits if t.runway_color in {"none", "grey"})
    stack_count = tech_stack_count(stack)
    system_color = "var(--green)" if health["alert"] == 0 and health["warn"] == 0 else "var(--yellow)"
    usage_issue_count = credits_monitor + credits_alert + credits_pending
    usage_issue_label = "usage needs review" if credits_monitor or credits_alert else "usage pending data"
    usage_issue_color = "var(--yellow)" if credits_monitor else "var(--red)" if credits_alert else "var(--text-muted)"
    return (
        '<div class="gb-summary">'
        f'<div><span class="num" style="color:{system_color};">{health["healthy"]} / {sum(health.values())}</span>system healthy</div>'
        f'<div><span class="num" style="color:var(--green);">{credits_in_range}</span>usage in range</div>'
        f'<div><span class="num" style="color:{usage_issue_color};">{usage_issue_count}</span>{usage_issue_label}</div>'
        f'<div><span class="num">{stack_count}</span>tools inventoried</div>'
        "</div>"
    )


def render() -> None:
    import streamlit as st

    health_tiles = load_system_health()
    stack = load_tech_stack()
    credits = load_credit_tiles()
    st.markdown(_render_subtitle(), unsafe_allow_html=True)
    st.markdown(_render_summary(health_tiles, credits, stack), unsafe_allow_html=True)
    st.markdown(_render_zone_system_usage(health_tiles, credits), unsafe_allow_html=True)
    st.markdown(_render_zone_tooling_inventory(stack), unsafe_allow_html=True)

    st.markdown(
        '<div class="gb-page-note">Infrastructure focuses on runtime health and usage. '
        "Tooling is kept as reference inventory; credentials are managed through 1Password and the VPS operating layer."
        "</div>",
        unsafe_allow_html=True,
    )

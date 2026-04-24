"""Visual tokens and CSS for G&B Command Center.

Palette and type scale mirror dashboard/mockup-landing.html — validated 2026-04-24.
Do not diverge without Kay's sign-off (see memory/feedback_dashboard_visual_language_locked.md).
"""

REFRESH_SECONDS = 60

PALETTE = {
    "bg": "#0B0D12",
    "panel": "#141821",
    "panel_hover": "#1A1F2A",
    "row_hover": "#181C26",
    "border": "#242A36",
    "border_bright": "#2E3647",
    "border_soft": "#1C212C",
    "divider": "#1C212C",
    "text": "#E8ECF3",
    "text_muted": "#8B93A7",
    "text_dim": "#5B6378",
    "accent": "#4A9EFF",
    "green": "#3FD17F",
    "yellow": "#F5C451",
    "red": "#FF5A5A",
    "neutral": "#6B7280",
    "purple": "#B084F0",
}

# (label, url_path, implemented) — st.navigation uses implemented==True pages;
# unimplemented items render as disabled sidebar entries.
NAV_ITEMS = [
    ("Dashboard", "dashboard", True),
    ("Deal Aggregator", "deal-aggregator", True),
    ("Deal Pipeline", "deal-pipeline", False),
    ("C-Suite & Skills", "c-suite-skills", False),
    ("Infrastructure", "infrastructure", False),
    ("M&A Analytics", "ma-analytics", False),
    ("Tech Stack", "tech-stack", False),
]


GLOBAL_CSS = f"""
<style>
  :root {{
    --bg: {PALETTE["bg"]};
    --panel: {PALETTE["panel"]};
    --panel-hover: {PALETTE["panel_hover"]};
    --row-hover: {PALETTE["row_hover"]};
    --border: {PALETTE["border"]};
    --border-bright: {PALETTE["border_bright"]};
    --border-soft: {PALETTE["border_soft"]};
    --divider: {PALETTE["divider"]};
    --text: {PALETTE["text"]};
    --text-muted: {PALETTE["text_muted"]};
    --text-dim: {PALETTE["text_dim"]};
    --accent: {PALETTE["accent"]};
    --green: {PALETTE["green"]};
    --yellow: {PALETTE["yellow"]};
    --red: {PALETTE["red"]};
    --neutral: {PALETTE["neutral"]};
    --purple: {PALETTE["purple"]};
  }}

  /* Hide Streamlit chrome that fights our design */
  header[data-testid="stHeader"] {{ display: none; }}
  div[data-testid="stToolbar"] {{ display: none; }}
  #MainMenu {{ visibility: hidden; }}
  footer {{ visibility: hidden; }}
  div[data-testid="stDecoration"] {{ display: none; }}
  div[data-testid="stStatusWidget"] {{ display: none; }}

  html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {{
    background: var(--bg) !important;
    color: var(--text);
    font-family: "Avenir Next", "Avenir", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: 14px;
    line-height: 1.45;
    -webkit-font-smoothing: antialiased;
  }}

  /* Main content padding — match mockup's 24/32/40 */
  [data-testid="stMain"] .stMainBlockContainer,
  section.main > div.block-container,
  [data-testid="stAppViewBlockContainer"] {{
    padding: 24px 32px 40px !important;
    max-width: none !important;
  }}

  /* Remove default vertical gap between Streamlit elements so our HTML carries the spacing */
  [data-testid="stVerticalBlock"] {{ gap: 0 !important; }}

  /* -------- SIDEBAR -------- */
  [data-testid="stSidebar"] {{
    background: var(--panel) !important;
    border-right: 1px solid var(--border);
    width: 240px !important;
    min-width: 240px !important;
  }}
  [data-testid="stSidebar"] > div:first-child {{
    background: var(--panel) !important;
    padding: 20px 0 !important;
  }}
  [data-testid="stSidebarContent"] {{ padding: 20px 0 !important; }}
  [data-testid="stSidebarHeader"] {{ display: none !important; }}
  [data-testid="stSidebarCollapseButton"] {{ display: none !important; }}

  .gb-brand {{
    padding: 0 20px 24px;
    border-bottom: 1px solid var(--border);
    margin-bottom: 16px;
  }}
  .gb-brand .logo {{
    font-size: 15px;
    font-weight: 600;
    letter-spacing: 0.02em;
    color: var(--text);
  }}
  .gb-brand .sub {{
    font-size: 11px;
    color: var(--text-dim);
    margin-top: 2px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
  }}

  .gb-nav {{ padding: 0 12px; }}
  .gb-nav-item {{
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 9px 12px;
    border-radius: 6px;
    color: var(--text-muted);
    font-size: 13px;
    margin-bottom: 2px;
    transition: all 0.15s;
  }}
  .gb-nav-item.active {{
    background: rgba(74, 158, 255, 0.12);
    color: var(--accent);
    font-weight: 500;
  }}
  .gb-nav-item.disabled {{ color: var(--text-dim); cursor: not-allowed; }}
  .gb-nav-item .dot {{
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--text-dim);
  }}
  .gb-nav-item.active .dot {{ background: var(--accent); }}

  /* Style Streamlit's st.page_link to match our custom nav items. */
  [data-testid="stSidebar"] a[data-testid="stPageLink"],
  [data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"] {{
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    padding: 9px 12px !important;
    border-radius: 6px !important;
    color: var(--text-muted) !important;
    font-size: 13px !important;
    margin-bottom: 2px !important;
    text-decoration: none !important;
    background: transparent !important;
    transition: all 0.15s !important;
  }}
  [data-testid="stSidebar"] a[data-testid="stPageLink"]:hover,
  [data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"]:hover {{
    background: var(--panel-hover) !important;
    color: var(--text) !important;
  }}
  [data-testid="stSidebar"] a[data-testid="stPageLink"][aria-current="page"],
  [data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"][aria-current="page"] {{
    background: rgba(74, 158, 255, 0.12) !important;
    color: var(--accent) !important;
    font-weight: 500 !important;
  }}
  /* Leading dot injected via ::before so labels match the HTML mockup. */
  [data-testid="stSidebar"] a[data-testid="stPageLink"]::before,
  [data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"]::before {{
    content: "";
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--text-dim);
    flex-shrink: 0;
  }}
  [data-testid="stSidebar"] a[data-testid="stPageLink"][aria-current="page"]::before,
  [data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"][aria-current="page"]::before {{
    background: var(--accent);
  }}
  /* Streamlit sometimes wraps page_link labels in an extra span — strip its own padding. */
  [data-testid="stSidebar"] a[data-testid="stPageLink"] > div,
  [data-testid="stSidebar"] a[data-testid="stPageLink"] p,
  [data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"] > div,
  [data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"] p {{
    margin: 0 !important;
    padding: 0 !important;
    font-size: 13px !important;
    line-height: 1 !important;
  }}

  /* -------- TOPBAR -------- */
  .gb-topbar {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 28px;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--border);
  }}
  .gb-topbar h1 {{
    font-size: 20px;
    font-weight: 500;
    letter-spacing: -0.01em;
    margin: 0;
    color: var(--text);
  }}
  .gb-topbar .meta {{
    font-size: 12px;
    color: var(--text-dim);
  }}
  .gb-topbar .meta .sep {{ margin: 0 8px; color: var(--border); }}

  /* -------- TILE GRID -------- */
  .gb-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
  }}
  .gb-tile {{
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 20px;
    min-height: 160px;
    display: flex;
    flex-direction: column;
    cursor: pointer;
    transition: all 0.18s;
  }}
  .gb-tile:hover {{
    background: var(--panel-hover);
    border-color: var(--border-bright);
    transform: translateY(-1px);
  }}
  .gb-tile .label {{
    font-size: 10.5px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-dim);
    margin-bottom: 14px;
  }}
  .gb-tile .primary {{
    font-size: 36px;
    font-weight: 300;
    letter-spacing: -0.02em;
    color: var(--text);
    line-height: 1.1;
  }}
  .gb-tile .primary .unit {{
    font-size: 14px;
    color: var(--text-muted);
    margin-left: 6px;
    font-weight: 400;
  }}
  .gb-tile .footer {{
    margin-top: auto;
    padding-top: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .gb-trend {{
    font-size: 12px;
    display: flex;
    align-items: center;
    gap: 5px;
  }}
  .gb-trend.up {{ color: var(--green); }}
  .gb-trend.down {{ color: var(--red); }}
  .gb-trend.flat {{ color: var(--neutral); }}
  .gb-horizon {{
    font-size: 11px;
    color: var(--text-dim);
    letter-spacing: 0.04em;
  }}

  /* Status dots */
  .gb-status-row {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 8px;
  }}
  .gb-status-dot {{
    width: 8px;
    height: 8px;
    border-radius: 50%;
  }}
  .gb-status-dot.green {{
    background: var(--green);
    box-shadow: 0 0 8px rgba(63, 209, 127, 0.3);
  }}
  .gb-status-dot.yellow {{
    background: var(--yellow);
    box-shadow: 0 0 8px rgba(245, 196, 81, 0.3);
  }}
  .gb-status-dot.red {{
    background: var(--red);
    box-shadow: 0 0 8px rgba(255, 90, 90, 0.3);
  }}
  .gb-status-text {{
    font-size: 12px;
    color: var(--text-muted);
  }}

  /* M&A stacked tile list */
  .gb-ma-list {{
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 6px 14px;
    margin-top: 4px;
  }}
  .gb-ma-label {{
    font-size: 12.5px;
    color: var(--text-muted);
  }}
  .gb-ma-value {{
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
    text-align: right;
    font-variant-numeric: tabular-nums;
  }}

  .gb-page-note {{
    margin-top: 32px;
    font-size: 11px;
    color: var(--text-dim);
    text-align: center;
    letter-spacing: 0.04em;
  }}

  /* -------- PAGE SUBTITLE -------- */
  .gb-subtitle {{
    font-size: 13px;
    color: var(--text-muted);
    margin-top: -16px;
    margin-bottom: 24px;
  }}
  .gb-subtitle .highlight {{ color: var(--text); font-weight: 500; }}

  /* -------- SUMMARY STRIP -------- */
  .gb-summary {{
    display: flex;
    gap: 28px;
    padding: 10px 0 20px;
    font-size: 12px;
    color: var(--text-muted);
    flex-wrap: wrap;
  }}
  .gb-summary .num {{
    color: var(--text);
    font-weight: 500;
    margin-right: 5px;
    font-variant-numeric: tabular-nums;
  }}

  /* -------- FILTER BAR -------- */
  .gb-filter-bar {{
    display: flex;
    gap: 10px;
    align-items: center;
    margin-bottom: 20px;
    padding-bottom: 20px;
    border-bottom: 1px solid var(--border);
    flex-wrap: wrap;
  }}
  .gb-filter-tabs {{ display: flex; gap: 4px; }}
  .gb-filter-tab {{
    padding: 6px 12px;
    font-size: 12px;
    color: var(--text-muted);
    background: transparent;
    border: 1px solid var(--border);
    border-radius: 6px;
    transition: all 0.15s;
  }}
  .gb-filter-tab.active {{
    background: rgba(74, 158, 255, 0.1);
    border-color: var(--accent);
    color: var(--accent);
  }}
  .gb-filter-select {{
    padding: 6px 10px;
    font-size: 12px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 6px;
    color: var(--text-muted);
    font-family: inherit;
  }}
  .gb-filter-search {{
    flex: 1;
    max-width: 260px;
    padding: 6px 12px;
    font-size: 12px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 6px;
    color: var(--text);
    font-family: inherit;
  }}
  .gb-filter-search::placeholder {{ color: var(--text-dim); }}

  /* -------- DATA TABLE -------- */
  .gb-table-wrap {{
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
  }}
  .gb-table {{ width: 100%; border-collapse: collapse; }}
  .gb-table thead th {{
    text-align: left;
    padding: 12px 14px;
    font-size: 10.5px;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-dim);
    border-bottom: 1px solid var(--border);
    background: rgba(255,255,255,0.01);
  }}
  .gb-table tbody td {{
    padding: 14px;
    font-size: 13px;
    border-bottom: 1px solid var(--border-soft);
    color: var(--text);
    vertical-align: middle;
  }}
  .gb-table tbody tr {{ transition: background 0.15s; }}
  .gb-table tbody tr:hover {{ background: var(--row-hover); }}
  .gb-table tbody tr:last-child td {{ border-bottom: none; }}

  .gb-company {{ font-weight: 500; }}
  .gb-industry-tag {{
    display: inline-block;
    font-size: 11px;
    padding: 2px 8px;
    background: rgba(176, 132, 240, 0.12);
    color: var(--purple);
    border-radius: 4px;
    margin-top: 3px;
    letter-spacing: 0.02em;
  }}
  .gb-owner, .gb-location {{ color: var(--text-muted); }}
  .gb-location {{ font-variant-numeric: tabular-nums; }}
  .gb-num {{
    font-variant-numeric: tabular-nums;
    text-align: right;
  }}
  .gb-num.dim {{ color: var(--text-dim); }}

  .gb-source-tag {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    color: var(--text-muted);
  }}
  .gb-source-tag .src-dot {{
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--accent);
  }}
  .gb-source-tag .src-dot.axial      {{ background: var(--green); }}
  .gb-source-tag .src-dot.bizbuysell {{ background: var(--accent); }}
  .gb-source-tag .src-dot.email      {{ background: var(--yellow); }}
  .gb-source-tag .src-dot.assoc      {{ background: var(--purple); }}
  .gb-source-tag .src-dot.dealsx     {{ background: var(--red); }}
  .gb-source-tag .src-dot.other      {{ background: var(--neutral); }}

  .gb-status-badge {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 11.5px;
    padding: 3px 10px;
    border-radius: 12px;
    font-weight: 500;
  }}
  .gb-status-badge.new      {{ background: rgba(74, 158, 255, 0.12); color: var(--accent); }}
  .gb-status-badge.reviewed {{ background: rgba(139, 147, 167, 0.14); color: var(--text-muted); }}
  .gb-status-badge.pursuing {{ background: rgba(63, 209, 127, 0.12); color: var(--green); }}
  .gb-status-badge.passed   {{ background: rgba(107, 114, 128, 0.14); color: var(--text-dim); }}

  .gb-link-cell {{ text-align: center; width: 40px; }}
  .gb-link-icon {{
    display: inline-block;
    color: var(--text-dim);
    font-size: 14px;
    transition: color 0.15s;
    text-decoration: none;
  }}
  .gb-link-icon:hover {{ color: var(--accent); }}

  .gb-empty {{
    padding: 40px 20px;
    text-align: center;
    color: var(--text-dim);
    font-size: 13px;
  }}
</style>
"""

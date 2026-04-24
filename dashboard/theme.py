"""Visual tokens and CSS for G&B Command Center.

Palette and type scale mirror dashboard/mockup-landing.html — validated 2026-04-24.
Do not diverge without Kay's sign-off (see memory/feedback_dashboard_visual_language_locked.md).
"""

REFRESH_SECONDS = 60

PALETTE = {
    "bg": "#0B0D12",
    "panel": "#141821",
    "panel_hover": "#1A1F2A",
    "border": "#242A36",
    "border_bright": "#2E3647",
    "divider": "#1C212C",
    "text": "#E8ECF3",
    "text_muted": "#8B93A7",
    "text_dim": "#5B6378",
    "accent": "#4A9EFF",
    "green": "#3FD17F",
    "yellow": "#F5C451",
    "red": "#FF5A5A",
    "neutral": "#6B7280",
}

NAV_ITEMS = [
    ("Dashboard", True),
    ("Deal Aggregator", False),
    ("Deal Pipeline", False),
    ("C-Suite & Skills", False),
    ("Infrastructure", False),
    ("M&A Analytics", False),
    ("Tech Stack", False),
]


GLOBAL_CSS = f"""
<style>
  :root {{
    --bg: {PALETTE["bg"]};
    --panel: {PALETTE["panel"]};
    --panel-hover: {PALETTE["panel_hover"]};
    --border: {PALETTE["border"]};
    --border-bright: {PALETTE["border_bright"]};
    --divider: {PALETTE["divider"]};
    --text: {PALETTE["text"]};
    --text-muted: {PALETTE["text_muted"]};
    --text-dim: {PALETTE["text_dim"]};
    --accent: {PALETTE["accent"]};
    --green: {PALETTE["green"]};
    --yellow: {PALETTE["yellow"]};
    --red: {PALETTE["red"]};
    --neutral: {PALETTE["neutral"]};
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
</style>
"""

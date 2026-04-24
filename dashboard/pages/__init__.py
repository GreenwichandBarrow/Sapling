"""Page renderers for the G&B Command Center.

Each module exports a `render()` function that Streamlit calls via
`st.navigation`. Using callable targets (rather than file paths) keeps
Streamlit's legacy pages/ auto-discovery inert — st.navigation in
command_center.py takes precedence.
"""

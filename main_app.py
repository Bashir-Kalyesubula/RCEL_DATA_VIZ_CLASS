
import streamlit as st
import plotly.graph_objects as go

# Set up page config
st.set_page_config(
    page_title="Where the World Gets Its A.I.",
    layout="centered"
)

st.title("Where the World Gets Its A.I.")
st.caption("A recreation of the New York Times Sankey diagram detailing the global A.I. divide.")

# --- DATA CONFIGURATION ---
# Define nodes (Left Side Providers -> Right Side Regions)
nodes = [
    # Left Side: Companies based here (Indices 0 to 3)
    "China",          # 0
    "United States",  # 1
    "Switzerland",    # 2
    "France",         # 3
    # Right Side: Operating A.I. facilities here (Indices 4 to 10)
    "Asia",           # 4
    "Europe",         # 5
    "Middle East",    # 6
    "North America",  # 7
    "South Africa",   # 8
    "South America",  # 9
    "Australia"       # 10
]

# Define Custom Colors matching the original NYT graphic palette
color_china = "rgba(226, 126, 129, 0.7)"       # Muted Coral/Pink
color_us = "rgba(134, 182, 207, 0.7)"          # Soft Blue
color_swiss = "rgba(35, 77, 121, 0.8)"         # Deep Dark Blue
color_france = "rgba(235, 203, 102, 0.8)"       # Mustard Yellow

# Define flows: (Source, Target, Value, Color Override)
# Values represent proportional infrastructure counts based on the visual weight of the flows.
flows = [
    # China Flows
    (0, 4, 30, color_china),   # China -> Asia (Main thick link)
    (0, 5, 4, color_china),    # China -> Europe
    (0, 6, 2, color_china),    # China -> Middle East
    (0, 8, 1, color_china),    # China -> South Africa
    (0, 9, 2, color_china),    # China -> South America

    # United States Flows
    (1, 4, 15, color_us),      # US -> Asia
    (1, 5, 25, color_us),      # US -> Europe (Thick link)
    (1, 6, 6, color_us),       # US -> Middle East
    (1, 7, 35, color_us),      # US -> North America (Thick domestic link)
    (1, 8, 1, color_us),       # US -> South Africa
    (1, 9, 3, color_us),       # US -> South America
    (1, 10, 4, color_us),      # US -> Australia

    # Switzerland Flows
    (2, 6, 2, color_swiss),    # Switzerland -> Middle East

    # France Flows
    (3, 6, 2, color_france),   # France -> Middle East
]

# Unpack flows for Plotly consumption
sources = [f[0] for f in flows]
targets = [f[1] for f in flows]
values = [f[2] for f in flows]
link_colors = [f[3] for f in flows]

# Assign uniform gray colors to the nodes to emphasize flow connections
node_colors = ["#4A5568"] * len(nodes)

# --- PLOTLY SANKEY BUILD ---
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=20,
        thickness=15,
        line=dict(color="black", width=0.5),
        label=nodes,
        color=node_colors,
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        color=link_colors
    )
)])

# Style the figure layout to emulate the dark presentation theme
fig.update_layout(
    font_size=12,
    font_family="Arial, sans-serif",
    font_color="#E2E8F0",
    paper_bgcolor="#22252A",
    plot_bgcolor="#22252A",
    height=650,
    margin=dict(l=20, r=20, t=40, b=40)
)

# Display inside Streamlit window
st.plotly_chart(fig, use_container_width=True)

# Metadata details
st.markdown("""
<div style="font-size:0.85em; color:#A0AEC0;">
    <strong>Source:</strong> Oxford University / The New York Times.<br>
    <em>Note: Flow thicknesses have been approximated visually based on published data graphics.</em>
</div>
""", unsafe_allow_html=True)

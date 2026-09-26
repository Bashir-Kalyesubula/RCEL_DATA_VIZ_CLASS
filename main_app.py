
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(layout="wide", page_title="AI World Graph Analysis")

st.title("AI World Graph Sankey Visualization")

# Generate synthetic network/data layout
np.random.seed(42)
n_nodes = 50
nodes_df = pd.DataFrame({
    'category': np.random.choice(['Infrastructure', 'Models', 'Applications', 'Policy'], n_nodes),
    'impact_score': np.random.uniform(10, 100, n_nodes)
})

# Aggregate flows from Global AI Hub to Categories
flow_df = nodes_df.groupby('category')['impact_score'].sum().reset_index()

# Define Sankey Nodes and Links
labels = ["Global AI Hub"] + flow_df['category'].tolist()
sources = [0] * len(flow_df)
targets = list(range(1, len(flow_df) + 1))
values = flow_df['impact_score'].tolist()

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values
    )
)])

fig.update_layout(title_text="Global AI Impact Allocation", font_size=12)

# Display metrics and plot
col1, col2, col3 = st.columns(3)
col1.metric("Total Nodes", n_nodes)
col2.metric("Categories", len(flow_df))
col3.metric("Max Impact Score", f"{nodes_df['impact_score'].max():.1f}")

st.plotly_chart(fig, use_container_width=True)

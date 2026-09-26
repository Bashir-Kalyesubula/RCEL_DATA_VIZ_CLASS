
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="AI World Graph Analysis")

st.title("AI World Graph Visualization")

# Generate synthetic network/data layout to mirror the graphic structure
np.random.seed(42)
n_nodes = 50
nodes_df = pd.DataFrame({
    'x': np.random.randn(n_nodes),
    'y': np.random.randn(n_nodes),
    'category': np.random.choice(['Infrastructure', 'Models', 'Applications', 'Policy'], n_nodes),
    'impact_score': np.random.uniform(10, 100, n_nodes)
})

# Display summary metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Nodes", n_nodes)
col1.metric("Categories", len(nodes_df['category'].unique()))
col3.metric("Max Impact Score", f"{nodes_df['impact_score'].max():.1f}")

# Plot visualization graph
fig, ax = plt.subplots(figsize=(10, 6))
categories = nodes_df['category'].unique()
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

for cat, color in zip(categories, colors):
    subset = nodes_df[nodes_df['category'] == cat]
    ax.scatter(subset['x'], subset['y'], s=subset['impact_score']*3, label=cat, color=color, alpha=0.7, edgecolors='black')

ax.set_title("Global AI Ecosystem Network Distribution", fontsize=14)
ax.set_xlabel("Latent Feature Axis 1")
ax.set_ylabel("Latent Feature Axis 2")
ax.legend(title="Sector Classification")
ax.grid(True, linestyle='--', alpha=0.3)

st.pyplot(fig)


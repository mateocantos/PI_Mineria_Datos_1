"""Utilidades compartidas por las páginas de la app (carga de datos y estilo oscuro)."""
from pathlib import Path
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Paleta del tema oscuro (estilo streaming)
ACCENT  = "#A855F7"   # violeta
ACCENT2 = "#EC4899"   # magenta
TEXT    = "#EDEAF5"
MUTED   = "#9A93B0"
PALETTE = ["#A855F7", "#EC4899", "#6366F1", "#D946EF", "#F472B6", "#8B5CF6", "#22D3EE", "#FB7185", "#818CF8"]


def processed_path() -> Path:
    # utils.py está en app/ ; el dataset en <repo>/data/processed/
    return Path(__file__).resolve().parents[1] / "data" / "processed" / "streaming_users_processed.csv"


@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.read_csv(processed_path())


def style_axes(ax):
    ax.set_facecolor("none")
    for s in ax.spines.values():
        s.set_color(MUTED); s.set_alpha(0.35)
    ax.tick_params(colors=MUTED, labelsize=9)
    ax.xaxis.label.set_color(TEXT); ax.yaxis.label.set_color(TEXT)
    ax.title.set_color(TEXT)
    ax.grid(True, color=MUTED, alpha=0.13)
    return ax


def new_fig(w=8, h=4):
    fig, ax = plt.subplots(figsize=(w, h))
    fig.patch.set_alpha(0)
    style_axes(ax)
    return fig, ax

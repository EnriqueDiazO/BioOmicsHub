
from __future__ import annotations
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def volcano_plot(df: pd.DataFrame, lfc_col: str, pval_col: str, lfc_thr: float = 1.0, pval_thr: float = 0.05):
    x = df[lfc_col].values
    y = -np.log10(df[pval_col].values.clip(lower=np.finfo(float).tiny))
    plt.figure()
    plt.scatter(x, y, s=10, alpha=0.6)
    plt.axvline(lfc_thr, linestyle="--")
    plt.axvline(-lfc_thr, linestyle="--")
    plt.axhline(-np.log10(pval_thr), linestyle="--")
    plt.xlabel("log2 Fold Change")
    plt.ylabel("-log10 p-value")
    plt.title("Volcano Plot")
    plt.tight_layout()
    return plt.gcf()

def radar_plot(df: pd.DataFrame, category_col: str, value_cols: list[str]):
    grouped = df.groupby(category_col)[value_cols].mean()
    labels = list(grouped.columns)
    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    plt.figure()
    for idx, (cat, row) in enumerate(grouped.iterrows()):
        values = row.values.tolist()
        values += values[:1]
        plt.polar(angles, values, label=str(cat))
    plt.thetagrids(np.degrees(angles[:-1]), labels)
    plt.legend(loc="best")
    plt.title("Radar Plot (promedios por categoría)")
    plt.tight_layout()
    return plt.gcf()

def bubble_plot(df: pd.DataFrame, x: str, y: str, size: str):
    plt.figure()
    plt.scatter(df[x], df[y], s=df[size], alpha=0.6)
    plt.xlabel(x); plt.ylabel(y); plt.title("Bubble Plot")
    plt.tight_layout()
    return plt.gcf()


from __future__ import annotations
import pandas as pd
import networkx as nx

def build_correlation_network(
    df_mrna: pd.DataFrame, df_mirna: pd.DataFrame,
    method: str = "spearman", threshold: float = 0.3
) -> nx.Graph:
    """
    Construye red bipartita miRNA-mRNA basada en correlación (negativa esperada).
    Placeholder para matriz cruzada real; aquí solo estructura.
    """
    common_samples = sorted(set(df_mrna.columns) & set(df_mirna.columns))
    A = df_mrna[common_samples]
    B = df_mirna[common_samples]

    G = nx.Graph()
    for gene in A.index:
        G.add_node(gene, type="mRNA")
    for mir in B.index:
        G.add_node(mir, type="miRNA")
    # TODO: calcular correlación cruzada real y agregar aristas con peso
    return G

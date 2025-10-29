
from __future__ import annotations
import pandas as pd

def summarize_by_group(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """Estadística descriptiva por grupo."""
    return df.groupby(group_col).describe().T

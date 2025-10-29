
from __future__ import annotations
import pandas as pd

def integrate_variant_tables(clinvar: pd.DataFrame, gnomad: pd.DataFrame, cosmic: pd.DataFrame) -> pd.DataFrame:
    """Unifica variantes por identificador (ej. chrom:pos:ref:alt) y armoniza campos clave."""
    def norm(df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df.columns = [c.lower().strip() for c in df.columns]
        return df
    cv = norm(clinvar)
    gn = norm(gnomad)
    cs = norm(cosmic)
    merged = cv.merge(gn, on="variant_id", how="outer", suffixes=("_clinvar", "_gnomad"))
    merged = merged.merge(cs, on="variant_id", how="outer")
    return merged

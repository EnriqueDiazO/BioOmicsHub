from __future__ import annotations
from pathlib import Path
import pandas as pd

from bioomicshub.core.preprocessing import standardize_columns
from bioomicshub.core.visualization import bubble_plot
from pathlib import Path

def get_desktop_dir() -> Path:
    """
    Devuelve una ruta válida al Escritorio del usuario.
    Compatible con Windows / macOS / Linux.
    Incluye soporte para OneDrive Desktop en Windows.
    """
    home = Path.home()

    candidates = [
        # Windows con OneDrive
        home / "OneDrive" / "Desktop",
        home / "OneDrive" / "Escritorio",

        # Escritorio normal
        home / "Desktop",
        home / "Escritorio",
    ]

    for d in candidates:
        if d.exists() and d.is_dir():
            return d

    return home


def main():
    df = pd.DataFrame({
        "Category": ["A", "A", "B", "B", "C"],
        "x": [1, 2, 3, 4, 5],
        "y": [5, 4, 3, 2, 1],
        "size": [10, 30, 50, 40, 20],
    })

    df = standardize_columns(df)
    fig = bubble_plot(df, "x", "y", "size")

    out_dir = get_desktop_dir()
    out_path = out_dir / "bubble_example.png"

    fig.savefig(out_path, dpi=200, bbox_inches="tight")
    print(f"OK -> {out_path}")


if __name__ == "__main__":
    main()


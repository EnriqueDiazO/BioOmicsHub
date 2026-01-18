print("TK_LAUNCHER: module import")
print(f"TK_LAUNCHER: __name__ = {__name__!r}")
"""
BioOmicsHub - Tkinter Script Launcher (MVP)

Objetivo:
GUI sencilla en Tkinter para ejecutar scripts existentes del proyecto
"""
import os
import subprocess
import sys
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox


class TkLauncher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BioOmicsHub - Tk Launcher")
        self.geometry("900x500")

        self.scripts_dir = Path(__file__).parent
        self.script_var = tk.StringVar()

        self._build_ui()
        self._load_scripts()

    def _build_ui(self):
        top = ttk.Frame(self, padding=10)
        top.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(top, text="Script:").pack(side=tk.LEFT)

        self.combo = ttk.Combobox(
            top,
            textvariable=self.script_var,
            state="readonly",
            width=40
        )
        self.combo.pack(side=tk.LEFT, padx=5)

        ttk.Button(
            top,
            text="Ejecutar",
            command=self.run_script
        ).pack(side=tk.LEFT, padx=10)

        ttk.Button(
            top,
            text="Limpiar salida",
            command=self.clear_output
        ).pack(side=tk.LEFT)

        output_frame = ttk.Frame(self, padding=10)
        output_frame.pack(fill=tk.BOTH, expand=True)

        self.output = tk.Text(
            output_frame,
            wrap="word",
            state="disabled"
        )
        self.output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(
            output_frame,
            orient="vertical",
            command=self.output.yview
        )
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.output.config(yscrollcommand=scrollbar.set)

    def _load_scripts(self):
        scripts = [
            f.name
            for f in self.scripts_dir.glob("*.py")
            if f.name not in {"__init__.py", "tk_launcher.py"}
        ]

        if not scripts:
            messagebox.showwarning(
                "Sin scripts",
                "No se encontraron scripts ejecutables."
            )
            return

        self.combo["values"] = scripts
        self.combo.current(0)

    def log(self, text):
        self.output.configure(state="normal")
        self.output.insert(tk.END, text)
        self.output.see(tk.END)
        self.output.configure(state="disabled")

    def clear_output(self):
        self.output.configure(state="normal")
        self.output.delete("1.0", tk.END)
        self.output.configure(state="disabled")

    def run_script(self):
        script = self.script_var.get()
        if not script:
            return

        self.clear_output()
        self.log(f"> Ejecutando {script}\n\n")

        # --- Diagnóstico portable (Windows/macOS/Linux) ---
        self.log(f"Launcher sys.executable: {sys.executable}\n")
        self.log(f"VIRTUAL_ENV: {os.environ.get('VIRTUAL_ENV')}\n")
        self.log(f"CONDA_PREFIX: {os.environ.get('CONDA_PREFIX')}\n")
        self.log(f"PYTHONPATH: {os.environ.get('PYTHONPATH')}\n")
        self.log(f"CWD: {Path.cwd()}\n")
        self.log(f"SCRIPTS_DIR: {self.scripts_dir}\n\n")

        script_path = self.scripts_dir / script
        if not script_path.exists():
            messagebox.showerror("Error", f"No existe el script: {script_path}")
            return

        try:
            # Ejecutar usando el Python del entorno actual (portable)
            cmd = [sys.executable, str(script_path)]

            # Importante: setear cwd para resultados consistentes (cross-platform)
            # Aquí elegimos ejecutar "desde scripts_dir" para que archivos salgan ahí.

            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=str(self.scripts_dir),
                )
            
            stdout, stderr = process.communicate()

            if stdout:
                self.log(stdout)
            
            if stderr:
                self.log("\n[stderr]\n" + stderr)
            

            if process.returncode != 0:
                self.log(f"\n[exit code] {process.returncode}\n")
                
                # Heurística útil para dependencias faltantes
                if "ModuleNotFoundError" in stderr:
                    self.log(
                    "\n[Sugerencia]\n"
                    "Faltan dependencias en el entorno activo.\n"
                    "Si usas Poetry, ejecuta:\n"
                    "  poetry install\n"
                    "o:\n"
                    "  poetry add <paquete>\n"
                )

        except Exception as e:
            messagebox.showerror("Error", str(e))


def main():
    app = TkLauncher()
    app.mainloop()

if __name__ == "__main__":
    main()


# BioOmicsHub

**BioOmicsHub** es una plataforma modular en Python para análisis exploratorio y visualización de datos ómicos.  
El proyecto está diseñado para ser **extensible**, **didáctico** y **orientado a investigación**, utilizando un entorno reproducible gestionado con **Poetry**.

Actualmente el repositorio integra **tres módulos principales**, desarrollados de forma independiente:

1. **miRNA_mRNA_networks**  
   Construcción y análisis de redes miRNA–mRNA.  
   Responsable: Carolina.

2. **variant_classification**  
   Clasificación de variantes y evaluación de riesgo clínico en leucemia linfoblástica aguda pediátrica (LLA).  
   Responsable: Francisco.

3. **noncoding_RNA**  
   Análisis exploratorio y visualización de RNAs no codificantes.  
   Responsable: Violeta.

---

## Requisitos

- Python 3.10 o superior  
- `pip`  
- `poetry`

---

## Instalación (entorno reproducible con Poetry)

1. Instalar Poetry (si no está instalado):

```bash
pip install poetry
poetry install
poetry run python -m ipykernel install --user --name bioomicshub
```


## Estructura
```
BioOmicsHub/
├── data/
│   └── raw/               # Datos crudos (no versionados)
├── notebooks/             # Notebooks exploratorios
├── src/
│   └── bioomicshub/
│       ├── core/          # Funciones base (preprocesamiento, visualizacion, utilidades)
│       ├── modules/       # Modulos de analisis (miRNA, variantes, ncRNA)
│       └── scripts/       # Scripts ejecutables (demos, utilidades)
├── tests/
├── pyproject.toml
└── README.md

```

## Uso rápido
```bash
poetry run python -m bioomicshub.scripts.demo_run
```
> Genera `bubble_example.png` como ejemplo.

## Uso de visualización
Ejecutar launcher gráfico (Tkinter)

El proyecto incluye un launcher sencillo en Tkinter para ejecutar scripts desde una interfaz gráfica básica, con fines didácticos.

```bash
poetry run python -m bioomicshub.scripts.demo_run
```
Este comando genera un archivo de ejemplo: bubble_example.png

© 2025 BioOmicsHub – MIT License.

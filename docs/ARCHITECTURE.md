
# Arquitectura

- `core/`: funciones compartidas (preprocesamiento, visualización, ML)
- `modules/miRNA_mRNA_networks/`: construcción y análisis de redes bipartitas
- `modules/variant_classification/`: integración de bases y modelos
- `modules/noncoding_RNA/`: exploración y gráficas

## Diagrama (texto)
core -> (preprocessing, visualization, ml_utils)
modules -> (usa core y define flujos propios)
scripts -> demos y CLI ligera

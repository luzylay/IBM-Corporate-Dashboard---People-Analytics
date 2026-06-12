# Grupo 09 - Guayerd IBM SkillsBuild

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Data Analysis](https://img.shields.io/badge/Data%20Analysis-Pandas%20%7C%20Seaborn-green)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)

Proyecto de análisis de datos enfocado en un escenario de e-commerce, con el objetivo de evaluar la relación entre inventario, tiempos de envío y reputación del negocio a partir de reseñas de clientes.

## Resumen ejecutivo

El proyecto analiza información transaccional, logística y de satisfacción del cliente para detectar patrones que expliquen la calidad del servicio y su posible impacto en la reputación digital del e-commerce.

## Objetivos

- Evaluar si el nivel de inventario influye en la calificación de los clientes.
- Analizar si los retrasos en envíos se asocian con reseñas negativas.
- Consolidar una estructura de datos clara para exploración, limpieza y visualización.

## Metodología

1. Recolección y organización de documentos, notebooks y datos fuente.
2. Limpieza y preparación de la base de datos en Python.
3. Cruce de tablas para construir una vista maestra de análisis.
4. Exploración estadística y visualización de patrones.
5. Documentación de hallazgos y conclusiones de negocio.

## Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Jupyter Notebook
- Power BI

## Estructura del repositorio

```text
Grupo-09-Guayerd-IBM-2025/
├── assets/
│   └── images/
├── data/
│   └── raw/
├── docs/
├── archive/
├── notebooks/
├── reports/
│   └── powerbi/
├── src/
└── README.md
```

## Contenido principal

- `docs/Documentacion.md`: documentación general del proyecto.
- `docs/Documentación3.md`: versión ampliada de la documentación.
- `src/main_ent3.py`: script de consola para leer y mostrar la documentación por secciones.
- `notebooks/modelo_aprendizaje.ipynb`: notebook de análisis y exploración.
- `notebooks/Readme.ipynb`: notebook complementario de presentación.
- `data/raw/Clientes.xlsx`: base de clientes.
- `data/raw/Detalle_ventas.xlsx`: detalle de ventas.
- `data/raw/Envíos.xlsx`: registros logísticos de envío.
- `data/raw/Productos.xlsx`: catálogo de productos e inventario.
- `data/raw/Reseña.xlsx`: calificaciones y reseñas.
- `data/raw/Ventas.xlsx`: ventas registradas.
- `reports/powerbi/Grupo 9 - IBM (Camada 19).pbix`: reporte de Power BI.

## Instalación y Uso

1. Clonar o abrir el repositorio en VS Code.
2. Instalar las dependencias recomendadas:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar el script interactivo para navegar la documentación desde consola:
   ```bash
   python src/main_ent3.py
   ```
4. Abrir los notebooks en `notebooks/` para explorar el análisis.
5. Usar los archivos de `data/raw/` como fuente de datos de entrada.

## Entregables originales

La carpeta `archive/` conserva copias completas de los entregables originales tal como estaban en Descargas. Se mantiene como respaldo para trazabilidad y revisión histórica.

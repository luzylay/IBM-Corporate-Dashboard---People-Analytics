# Documentación del Proyecto: Análisis de E-commerce

## 1. Información General
* **Tema:** Tienda E-commerce
* **Título:** Análisis de la Gestión de inventarios y su impacto en la reputación.
* **Contexto:** Trabajo en equipo - 2.ª Demo Sincrónica (IBM Skills Build).

## 2. Definición del Problema
Los procesos internos del comercio electrónico muestran fallas en áreas críticas como la gestión de pedidos, la logística y la atención al cliente. Esto genera insatisfacción y reseñas negativas, limitando el crecimiento del negocio y afectando su reputación digital.

## 3. Solución Propuesta (Enfoque de Datos)
Se realizó un análisis estadístico descriptivo utilizando Python para validar si existe una relación directa entre la precisión del inventario, los tiempos de envío y la percepción del servicio (rating).

**Objetivos Específicos:**
1.  **Optimización de la Demanda:** Analizar si el nivel de stock influye en la calificación del cliente.
2.  **Análisis de Reputación:** Determinar si la demora en los envíos es la causa principal de las reseñas negativas.

## 4. Base de Datos (Estructura)
El análisis se realizó sobre un dataset consolidado proveniente de 6 entidades relacionales:

1.  **CLIENTES (100 registros):** Datos demográficos y ubicación.
2.  **PRODUCTOS (100 registros):** Categoría, precio, inventario y frecuencia de reposición.
3.  **VENTAS (120 registros):** Historial transaccional y medios de pago.
4.  **DETALLE_VENTAS (120 registros):** Desglose de productos por ticket.
5.  **ENVIO (120 registros):** Fechas de despacho, entrega y estado.
6.  **RESEÑA (120 registros):** Calificación (1-5 estrellas) y comentarios.

## 5. Metodología de Análisis (Proceso ETL con Python)

Para garantizar la calidad de los resultados, se implementó un pipeline de datos en Python (`main.py`):

### A. Limpieza y Preparación
* **Detección de errores:** Se identificaron registros con fechas de entrega anteriores a la fecha de envío.
* **Corrección:** Se eliminaron registros incoherentes y valores nulos que afectaban la integridad matemática.
* **Ingeniería de Variables:** Se creó la variable calculada `Dias_Demora` = (*Fecha_Entrega* - *Fecha_Envio*).

### B. Fusión de Datos (Merge)
Se unificaron las 5 fuentes de datos (Ventas, Detalle, Envíos, Productos, Reseñas) en un "Master Dataset" para permitir el cruce de variables (Ej: Relacionar *Stock* con *Calificación*).

## 6. Resultados del Análisis Estadístico

A continuación se presentan los hallazgos derivados de los 6 puntos de control del proyecto:

### 1. Estadísticas Básicas
* **Variable Principal (Tiempo):** El tiempo promedio de entrega detectado es de **23.0 días**.
* **Variable Secundaria (Calificación):** El promedio de satisfacción general es moderado.

### 2. Identificación de Distribución
* **Herramienta:** Histograma de Frecuencias.
* **Hallazgo:** Los tiempos de entrega muestran una distribución con tendencia a ciclos largos (logística extendida), no concentrada en entregas "express".

### 3. Análisis de Correlaciones
* **Variables:** `Dias_Demora` vs `Rating`.
* **Resultado:** Coeficiente de correlación cercano a **0.00**.
* **Interpretación:** No existe una correlación lineal directa. Los clientes no están castigando la calificación proporcionalmente al tiempo de espera, lo que sugiere una demanda inelástica al tiempo (tolerancia a la espera).

### 4. Análisis de Valores Atípicos (Outliers)
* **Herramienta:** Diagrama de Caja (Boxplot).
* **Detección:** Se identificaron y filtraron envíos con demoras superiores a 60 días (considerados errores de sistema o casos extremos no representativos).

## 7. Interpretación de Resultados (Business Insights)

Basado en la evidencia de los datos, se concluye lo siguiente para el problema de negocio:

**Hallazgo 1: Eficiencia en Control de Stock**
El análisis de productos con **Stock Crítico (<10 unidades)** arrojó un resultado nulo (sin ventas registradas).
* **Conclusión de Negocio:** El sistema cuenta con un bloqueo efectivo ("Safety Stock"). La empresa no vende productos que no tiene, evitando cancelaciones y protegiendo la reputación por falta de disponibilidad.

**Hallazgo 2: Riesgo Logístico Latente**
Aunque la correlación actual es baja (los clientes toleran los 23 días de espera), este tiempo promedio representa un **riesgo competitivo alto**.
* **Conclusión de Negocio:** La satisfacción actual se sostiene probablemente por la calidad del producto, no por la eficiencia logística.

## 8. Recursos Visuales Generados
El script de Python genera 3 gráficos clave para la toma de decisiones:
1.  **Histograma:** Distribución de los tiempos de demora.
2.  **Boxplot:** Relación entre Calificación y Días de Demora (Detección de outliers).
3.  **Gráfico de Barras:** Calificación promedio agrupada por Nivel de Stock (Crítico, Normal, Alto).

## 9. Lógica del Algoritmo (Pseudocódigo Actualizado)

INICIO PROGRAMA (Python)

    1. CARGAR librerías (Pandas, Seaborn, Matplotlib)
    2. INTENTAR leer archivos Excel (Ventas, Envíos, Productos, Reseñas)
    
    3. PROCESO ETL (Limpieza):
       SI hay fechas inválidas O nulos:
          Eliminar registros corruptos
       CALCULAR Dias_Demora = Fecha_Entrega - Fecha_Envio
       FILTRAR Outliers (Demora < 0 o Demora > 100)
       
    4. UNIFICACIÓN (Merge):
       CREAR Tabla_Maestra uniendo Ventas + Detalle + Envíos + Productos + Reseñas
       
    5. ANÁLISIS:
       CALCULAR Promedios y Desviación Estándar
       CALCULAR Matriz de Correlación (Pearson)
       
    6. VISUALIZACIÓN:
       GENERAR Histograma (Demoras)
       GENERAR Boxplot (Rating vs Tiempo)
       GENERAR Barplot (Rating vs Stock)
       
    7. EXPORTACIÓN:
       CREAR carpeta "archivos_limpios"
       GUARDAR Excel procesado
       
    8. IMPRIMIR Conclusiones de Negocio

FIN PROGRAMA
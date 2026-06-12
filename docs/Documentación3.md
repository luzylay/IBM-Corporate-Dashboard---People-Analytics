Proyecto IBM IA - Guayerd Grupo 9

Tema
Análisis de la Gestión de inventarios y su impacto en la reputación de un E-commerce.

Problema
Durante un mes se pudo observar que los retrasos en las entregas tenian un impacto negativo en la reputacion del ecommerce basado en las reseñas sobre los pedidos que cada cliente realizaba luego de recibir su pedido.

La gestión de inventarios presenta problemas debido a los retrasos en las entregas y el impacto que esto tiene en la reputación del e-commerce basado en las reseñas sobre pedidos de los clientes.
Se ha observado que los retrasos en las entregas pueden estar vinculados a la mala planificación y gestión de inventarios. Como consecuencia, esto genera malestar en los clientes.

Solucion
Se plantea analizar si existe una relación directa entre la precisión del inventario y la percepción negativa del servicio. Para ello se llevara a cabo:
1. Optimización de la previsión de la demanda utilizando técnicas de la Ciencia de datos para crear un modelo predictivo, para anticipar de este modo que productos necesitan mayor stock en ciertos periodos de tiempo para evitar problemas de oferta y demanda.
2. Mediante el análisis de datos de las reseñas, averiguar que tienen en común los pedidos que poseen reseñas negativas, para de este modo identificar patrones y realizar las respectivas correcciones del proceso.

Base de datos
Contiene 6 entidades.

Entidad: CLIENTES
Registros: 100
Campos:
1. ID_cliente - int - nominal
2. nombre_cliente - str - nominal
3. email - str - nominal
4. ciudad - str - nominal
5. fecha_alta - date - intervalo

Entidad: DETALLE_VENTAS
Registros: 120
Campos:
1. ID_venta - int - nominal
2. ID_producto - int - nominal
3. nombre_producto - str - nominal
4. cantidad - int - razón
5. precio_unitario - int - razón
6. importe - int - razón

Entidad: PRODUCTOS
Registros: 100
Campos:
1. ID_producto - int - nominal
2. nombre_producto - str - nominal
3. categoría - str - nominal
4. precio_unitario - int - razón
5. Inventario - int - nominal
6. Frecuencia_dias - int - nominal

Entidad: VENTAS
Registros: 120
Campos:
1. ID_venta - int - nominal
2. fecha - date - intervalo
3. ID_cliente - int - nominal
4. nombre_cliente - str - nominal
5. email - str - nominal
6. medio_pago - str - nominal

Entidad: ENVIO
Registros: 120
Campos:
1. ID_envio - int - nominal
2. ID_venta - int - nominal
3. ID_seguimiento - int - nominal
4. estado - str - nominal
5. Fecha_hora_envio - date - intervalo
6. Fecha_hora_entrega - date - intervalo

Entidad: RESEÑA
Registros: 120
Campos:
1. ID_resena - int - nominal
2. ID_producto - int - nominal
3. ID_cliente - int - nominal
4. Calificación - int - ordinal

Informacion
El programa necesitará consultar varias tablas para relacionar el inventario, los pedidos, el envío y la percepción del cliente.
OBJETIVOS DE ANÁLISIS
1. Objetivo: Optimización de la demanda
   Tablas clave: Pedido, ProductoDetalle, Inventario
   Columnas relevantes: Fecha, IDProducto, Cantidad del detalle e inventario
2. Objetivo: Análisis de Reseñas Negativas
   Tablas clave: Reseña, Pedido, Envío, Usuario
   Columnas relevantes: Calificación, Comentario, Fecha del pedido y envío, Estado del envío

Pasos
1. Conexión a la base de datos.
2. Preparación de datos para la predicción.
3. Análisis de la información obtenida tras la revisión.
4. Modelado predictivo para análisis de la demanda futura de los productos.
5. Análisis de las reseñas para diagnosticar los problemas.
6. Visualización de los datos mediante un reporte.

Pseudocodigo
INICIO

#Revisar Información – Corregir y eliminar datos innecesarios en el archivo documentación.md
REVISAR ARCHIVO Documentación.MD
VALIDAR LINE
REVISAR LINE <>BLANCO

SI LINE = BLANCO
OMITIR LINE
SINO MOSTRAR LINE
#Menú Inicial – Información contenida en el archivo documentación.md
MOSTRAR INFORMACIÓN CONTENIDA EN EL ARCHIVO
1. Tema
2. Problema
3. Solucion
4. Base de datos
5. Información
6. Pasos
7. Pseudocodigo
8. Integrantes
0. Salir

#Mostrar Información – De acuerdo a la opción seleccionada
Mostrar mensaje = “¿Qué desea revisar??” 
SELECCIONAR X (Opción)

SI selecciona punto del menú = X
MOSTRAR X
SINO MOSTRAR Mensaje = “Ingrese 0 para salir del programa”

#Confirmar Selección – Notificar si no se selecciona una opción válida
EVALUAR X (Opción) 

SI X = OPCION EN MENÚ
MOSTRAR X
SINO MOSTRAR Mensaje  = “Intentelo de nuevo o seleccione SALIR (opcion 0)”
SINO Volver a Buscar

FINAL

Analisis ecomerce
Proceso por medio del cual se realiza un proceso para identificar de manera númerica y grafica.
1. Realizar la limpieza de las bases de datos con el fin de que estas puedan ser usadas y que permitan usar datos reales que no vayan a sesgar nuestros resultados.
2. Revisión del estado de las bases de datos desde un análisis estadístico que permita determinar las tendencias que tenemos por la fuente de información principal de nuestros datos.
3. Proyectar gráficos que evidencien el comportamiento de los datos, para de esta manera generar conclusiones y comentarios claves acerca del comportamiento que tienen los datos.

Modelo de aprendizaje
Enfoque en los puntos clave del proyecto para identificar como se podría ver a futuro el comportamiento de nuestros datos clave
1. Identificar el problema y enfoque que se busca
2. Hacer preguntas sobre la solución que se requiere solucionar y para la cual sería apto implementar un modelo

Sugerencias
1. Se consulto a copilot una forma sencilla de como se podría visualizar la información y categorizarla al cargarla desde un archivo de texto lo que nos llevo a iterar las lineas del documento y comprar su contenido con palabras clave para reconocer las secciones dentro del mismo
2. Se consulto a copilot de que forma se podría manejar las entradas de usuario para evitar problemas de entradas de usuarios sea que se ingrese texto o números y manejarlo correctamente para dar un paso extra en la ejecucion del proyecto

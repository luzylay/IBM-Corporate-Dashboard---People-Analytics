Tema
Tienda E-commerce
Análisis de la Gestión de inventarios y su impacto en la reputación de un E-commerce.

Problema
Los procesos internos del comercio electrónico muestran fallas en áreas como la gestión de pedidos, la logística y la atención al cliente, generando insatisfacción y reseñas negativas. Este problema limita el crecimiento del negocio y afecta su reputación digital.

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
1. Obtener la información sobre el proyecto del archivo .md.
2. mostrar las opciones de menu para que el usuario seleccione que quiere visualizar
2. Validar que opcion quiere ver el usuario para poder mostrarle el resultado por consola
4. Imprimir la información que visualizar el usuario 
5. Redirigir al menu para permitir salir al usuario

Sugerencias
1. Se consulto a copilot una forma sencilla de como se podria visualizar la informacion y categorizarla al cargarla desde un archivo de texto lo que nos llevo a iterar las lineas del documento y comprar su contenido con palabras clave para reconocer las secciones dentro del mismo
2. Se consulto a copilot de que forma se podria manejar las entradas de usuario para evitar problemas de entradas de usuarios sea que se ingrese texto o numeros y manejarlo correctamente para dar un paso extra en la ejecucion del proyecto

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
import os

option = 1
datos = {
    "Tema": "",
    "Problema": "",
    "Solucion": "",
    "BD": "",
    "Informacion": "",
    "Pasos": "",
    "Codigo": "",
    "Analisis ecomerce": "",
    "Modelo de aprendizaje": "",
    "Integrantes": "- Lady_Loaiza\n- Laura_Gavidia\n- Julian_Torres",
    "Sugerencias": ""
}

secciones = {
        "Tema": "Tema",
        "Problema": "Problema",
        "Solucion": "Solucion",
        "Base de datos": "BD",
        "Informacion": "Informacion",
        "Pasos": "Pasos",
        "Pseudocodigo": "Codigo",
        "Analisis ecomerce": "Analisis ecomerce",
        "Modelo de aprendizaje": "Modelo de aprendizaje",
        "Sugerencias": "Sugerencias"

    }

def read_docs(path:str):
    with open(path, 'r', encoding='utf-8') as f:
        actual = None
        for line in f.readlines():
            line_strip = line.strip()
            if not line_strip:
                continue #linea vacia

            if line_strip in secciones:
                actual = secciones[line_strip]
                continue

            if actual:
                datos[actual] += line

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def greeting():
    print("--------------------------------")
    print("|          Bienvenido          |")
    print("--------------------------------\n")

def menu():
    print("--------------------------------")
    print("|            MENU              |")
    print("--------------------------------")
    print("1. Tema")
    print("2. Problema")
    print("3. Solucion")
    print("4. Base de datos")
    print("5. Informacion")
    print("6. Pasos")
    print("7. Pseudocodigo")    
    print("8. Analisis ecomerce")
    print("9. Modelo de aprendizaje")
    print("10. Sugerencias")
    print("11. Integrantes")
    print("0. Salir")
    print("--------------------------------")

def processInput(value: str) -> int | None:
    _option = value.strip().upper()
    try:
        num = int(value)
    except ValueError:
        num = None

    if _option == "SALIR" or num == 0:
        return 0
    elif num == 1 or _option == "TEMA":
        return 1
    elif num == 2 or _option == "PROBLEMA":
        return 2
    elif num == 3 or _option == "SOLUCION":
        return 3
    elif num == 4 or _option in ["BASE DE DATOS", "BD"]:
        return 4
    elif num == 5 or _option in ["INFORMACION", "INFORMACIÓN"]:
        return 5
    elif num == 6 or _option == "PASOS":
        return 6
    elif num == 7 or _option in ["PSEUDOCODIGO", "CÓDIGO", "CODIGO", "PSEUDOCÓDIGO"]:
        return 7
    elif num == 8 or _option == "ANALISIS ECOMERCE":
        return 8
    elif num == 9 or _option == "MODELO DE APRENDIZAJE":
        return 9
    elif num == 10 or _option == "SUGERENCIAS":
        return 10
    elif num == 11 or _option == "INTEGRANTES":
        return 11
    else:
        return None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_PATH = os.path.join(BASE_DIR, "..", "docs", "Documentación3.md")


read_docs(DOCS_PATH)
greeting()
while True:
    menu()
    option = input("¿Que deseas revisar?: ")
    result = processInput(option)

    match result:
        case 0:
            break
        case 1:
            clear_console()
            print("\n")
            print("Tema:")
            print(datos["Tema"])
            print("\n")
        case 2:
            clear_console()
            print("\n")
            print("Problema:")
            print(datos["Problema"])
            print("\n")
        case 3:
            clear_console()
            print("\n")
            print("Solucion:")
            print(datos["Solucion"])
            print("\n")
        case 4:
            clear_console()
            print("\n")
            print("Base de datos:")
            texto = datos["BD"]
            # Dividir cuando aparece "Entidad:" y volver a unir con un salto doble
            secciones = texto.split("Entidad:")
            texto_formateado = "\n\nEntidad:".join(secciones)

            print(texto_formateado)
            #print(datos["BD"])
            print("\n")
        case 5:
            clear_console()
            print("\n")
            print("Informacion:")
            print(datos["Informacion"])
            print("\n")
        case 6:
            clear_console()
            print("\n")
            print("Pasos:")
            print(datos["Pasos"])
            print("\n")
        case 7:
            clear_console()
            print("\n")
            print("Codigo:")
            print(datos["Codigo"])
            print("\n")
        
        case 8:
            clear_console()
            print("\n")
            print("Analisis ecomerce:")
            print(datos["Analisis ecomerce"])
            print("\n")
        case 9:
            clear_console()
            print("\n")
            print("Modelo de aprendizaje:")
            print(datos["Modelo de aprendizaje"])
            print("\n")
        case 10:
            clear_console()
            print("\n")
            print("Sugerencias de Copilot:")
            print(datos["Sugerencias"])
            print("\n")
        case 11:
            clear_console()
            print("\n")
            print("Integrantes:")
            print(datos["Integrantes"])
            print("\n")
        case _:
            clear_console()
            print("\n")
            print("\033[31m¡la opcion seleccionada no es valida!\033[0m")
            print("Intentelo de nuevo o seleccione SALIR (opcion 0)")
            print("\n")
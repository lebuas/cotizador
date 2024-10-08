def ingresar_datos_ventana():
    estilos_ventana = {
        "1": "O",
        "2": "XO",
        "3": "OXO",
        "4": "OXXO",
    }

    while True:
        print("\n== Tipos de ventana ==")
        print("1. O")
        print("2. XO")
        print("3. OXO")
        print("4. OXXO")

        estilo = input("Ingrese el estilo de la ventana (1-4): ")

        if estilo not in estilos_ventana:
            print("Error: Estilo no válido. Intente de nuevo.\n")
            continue

        try:
            ancho = float(
                input("Ingrese el ancho de la ventana (en cm): "))
            alto = float(input("Ingrese el alto de la ventana (en cm): "))
            cant = int(input("Ingrese cantidad de ventanas que desea hacer: "))
        except ValueError:
            print("Error: Por favor ingrese un número válido.\n")
            continue

        return {
            "estilo": estilos_ventana[estilo],
            "ancho": ancho,
            "alto": alto,
            "cantidad": cant
        }


def ingresar_datos_nave():
    acabados = {
        1: "Pulido",
        2: "Lacado Brillante",
        3: "Lacado Mate",
        4: "Anodizado"
    }

    while True:
        print("\n== Tipos de acabado para las naves ==")
        print("1. Pulido")
        print("2. Lacado Brillante")
        print("3. Lacado Mate")
        print("4. Anodizado")

        try:
            tipo_acabado = int(input("Seleccione el tipo de acabado (1-4): "))
            if tipo_acabado not in acabados:
                raise ValueError(
                    "Opción inválida. Seleccione un número entre 1 y 4.")
        except ValueError as e:
            print(e, "\n")
            continue

        return acabados[tipo_acabado]


def ingresar_datos_vidrio():
    tipo_vidrio = {
        "1": "Transparente",
        "2": "Bronce",
        "3": "Azul"
    }

    print("\n== Tipos de Vidrio ==")
    print("1. Transparente")
    print("2. Bronce")
    print("3. Azul")

    while True:
        try:
            seleccion = input("Seleccione el tipo de vidrio (1-3): ").strip()
            if seleccion not in tipo_vidrio:
                raise ValueError(
                    "Opción inválida. Seleccione un número entre 1 y 3.")

            tipo = tipo_vidrio[seleccion]

            esmerilado = input(
                "El vidrio es esmerilado? (si/no): ").strip().lower()
            if esmerilado not in ["si", "no"]:
                raise ValueError("Respuesta inválida. Ingrese 'si' o 'no'.")

            return tipo, esmerilado == "si"

        except ValueError as e:
            print(e, "\n")

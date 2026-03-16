print("SPA LUNA\n")

while True:
    try:
        print("\n======== SPA MENU ========\n")
        print("MASAJE")
        print("FACIAL")
        print("MANICURE")
        print("*. SALIR DEL MENU")
        print("\n======== 👀 ==========\n")

        opcion = input("INTRODUZCA EL NOMBRE DEL SERVICIO: ").upper()

        if opcion == "*":
            break

        if not opcion.isalpha():
            print("ERROR: SOLO SE PERMITEN LETRAS")

        elif opcion == "MASAJE":
            print("SERVICIO DE MASAJE DISPONIBLE")

        elif opcion == "FACIAL":
            print("SERVICIO DE FACIAL DISPONIBLE")

        elif opcion == "MANICURE":
            print("SERVICIO DE MANICURE DISPONIBLE")

        else:
            print("SERVICIO NO DISPONIBLE")

    except ValueError:
        print("ERROR EN EL SISTEMA")
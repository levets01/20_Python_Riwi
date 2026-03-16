print("===== CONTROL DE GIMNASIO =====")

# con for se estable el rango de validacion en ese caso sera 5 veces que se repetira para el ingreso de los usarios
for i in range(5):

    nombre = input("\nIngrese el nombre del usuario: ")

    while True:
        try:
            dias = int(input("Ingrese los días que asistió: "))
            
            if dias < 0:
                print("No se permiten números negativos")
            else:
                break

        except ValueError:
            print("Error: solo números")

    while True:
        try:
            minutos = int(input("Ingrese minutos entrenados: "))
            
            if minutos < 0:
                print("No se permiten números negativos")
            else:
                break

        except ValueError:
            print("Error: solo números")

    if dias < 3:
        print(nombre, "tiene bajo compromiso")

    elif dias <= 4:
        print(nombre, "tiene compromiso medio")

    else:
        print(nombre, "tiene alto compromiso")
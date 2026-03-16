
while True:
   try:
    clase = int(input("INGRESE LA CANTIDAD DE CLASES ASISTIDAS: "))

    if clase < 0 :

        print("ERROR: SOLO NUMEROS POSITIVOS")
        continue
    elif clase < 5 :
        print("Asistencia Baja")

        break

    elif clase <= 8:

        print("Asistencia Media")

        break

    else:

        print("Asistencia Alta")

    break
   
   except ValueError:
        print("ERROR: SOLO SE PERMITEN NUMEROS")
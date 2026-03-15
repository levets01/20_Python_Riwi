print("PELUQUERIA\n")

while True:
    try:
        hora = int(input("INGRESE LA HORA DE LLEGARA (0-23):"))
        if 0 <= hora <= 23:
            break
        else:
            print("ERROR:SOLO VALORES POSITIVOS")
    

    except ValueError:
            print("SOLO VALORES NUMERICOS")

if 6 <= hora <= 11 :
    print("TURNO DE MAÑANA")

elif 12 <= hora <= 17:

    print("TURNO DE TARDE")

elif 18 <= hora <= 22:

    print("TURNO DE NOCHE")
else:
 print("FUERA DE TURNO")
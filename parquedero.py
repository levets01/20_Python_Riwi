print("PARQUEADERO ULTRA SEGURO\n")

while True:
 try:
    horas = int(input("INGRESE LAS HORAS EN EL PARQUEADERO: "))
    if horas == 1:
        total = 5000
    else:
        total = 5000 + (horas - 1) * 3000

        print("Total a pagar: ", total)

    break
 
 except ValueError:
    print("ERROR:SOLO VALORES NUMERICOS")

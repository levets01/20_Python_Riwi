print("===== PARQUEADERO =====")

mayor_pago = 0
vehiculo_mayor = ""

for i in range(8):

    tipo = input("Ingrese tipo de vehículo (carro/moto): ").lower()
    horas = int(input("Ingrese horas estacionado: "))

    if tipo == "carro":
        pago = horas * 2000

    elif tipo == "moto":
        pago = horas * 1000

    else:
        print("Tipo inválido")
        continue

    print("Pago:", pago)

    if pago > mayor_pago:
        mayor_pago = pago
        vehiculo_mayor = tipo

print("\nEl vehículo que más pagó fue:", vehiculo_mayor)
print("Pago:", mayor_pago)
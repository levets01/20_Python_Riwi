print("XXXX> PELUQUERÍA <XXXXX")

#ACA ESTAN LOS CONTADORES
corte = 0
cepillado = 0
tintura = 0

# CICLO FOR CON UN RANGO ESTABLECIDO DE 7
for i in range(7):

    servicio = input("Ingrese servicio (corte/cepillado/tintura): ").lower()

    if servicio == "corte":
        corte += 1

    elif servicio == "cepillado":
        cepillado += 1

    elif servicio == "tintura":
        tintura += 1

if corte > cepillado and corte > tintura:
    print("Servicio más solicitado: corte")

elif cepillado > tintura:
    print("Servicio más solicitado: cepillado")

else:
    print("Servicio más solicitado: tintura")
print("===== HELADERIA =====")

#AQUI ESTARAN LOS PRECIOS EN VARIABLES

vainilla = 5000
chocolate = 6000
fresa = 5500

#AQUI ESTARAN LOS CONTADORES

total_ventas = 0
clientes = 0

cont_vainilla = 0
cont_chocolate = 0
cont_fresa = 0

#AQUI ESTA LA CONDICIÓN Y EL MENU DE LA HELADERIA

while True:
    print("\n1.Vainilla ")
    print("2.Chocolate  ")
    print("3.Fresa      ")
    print("4.Salir      ")

    try:
        option = int(input("Selecione el numero del sabor: "))

    except ValueError:

        print("ERROR: SOLO NUMEROS")
        continue

    if option == "4":
        break
    
    try:
        cantidad = int(input("Ingrese la cantidad : "))

        if cantidad <= 0:
            print("Cantidad invalida")
            continue
# (continue) es por si el usuario sigue ingresando un valor errado repita la opcion
    except ValueError:
        print("ERROR:SOLO SE PERMITEN NUMEROS")
        continue

    if option == "1":
        total = vainilla * cantidad
        cont_vainilla += cantidad

    elif option == "2":
        total = chocolate * cantidad
        cont_chocolate += cantidad

    elif option == "3":
        total = fresa * cantidad
        cont_fresa += cantidad
    
    else:
        print("Opcion invalida")
        continue
    print("total a pagar :", total)

    total_ventas += total
    clientes += 1

    print("\n======= RESUMEN DEL DÍA =======")
    print("CLIENTES ATENDIDOS:", clientes)
    print("TOTAL VENDIDO :", total_ventas)

    #Aqui se definira cual fue el producto mas vendido

    if cont_vainilla > cont_chocolate and cont_vainilla > cont_fresa:

        print("El sabor mas vendido fue Vainilla")

    elif cont_chocolate > cont_fresa :

        print("El sabor mas vendido fue Chocolate")

    else:
       
       print("El sabor mas vendido fue Fresa")


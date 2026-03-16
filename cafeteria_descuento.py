print("===== CAFETERÍA =====")

total = 0

while True:

    print("\nMenú:")
    print("1. Café - 4000")
    print("2. Té - 3000")
    print("3. Jugo - 5000")
    print("4.salir para ver el descuento aplicado ")
    print("========================")
    opcion = input("Seleccione un producto: ").lower()

    if opcion == "4":
        break

    try:
        cantidad = int(input("Ingrese la cantidad: "))

        if cantidad <= 0:
            print("Cantidad inválida")
            continue

    except ValueError:
        print("Error: solo números")
        continue

    if opcion == "1":
        total += 4000 * cantidad

    elif opcion == "2":
        total += 3000 * cantidad

    elif opcion == "3":
        total += 5000 * cantidad

    else:
        print("Opción no válida")

if total > 20000:

    descuento = total * 0.10

    total_final = total - descuento

    print("\nSe aplicó un descuento del 10%")

else:

    total_final = total

print("Total a pagar:", total_final)
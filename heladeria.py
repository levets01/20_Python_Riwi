print("\nBienvenido al sistema de pedidos de la heladeria ")

vainilla = 0
chocolate = 0
fresa = 0

for i in range(1,6):
    print(f"Pedido {i}")
    sabor = input("Ingrese el sabor (vainilla, chocolate, fresa): ").lower()

    if sabor == "vainilla":
        vainilla += 1
        
    elif sabor == "chocolate":
        chocolate += 1
        
    elif sabor == "fresa":
        fresa += 1
        
    else:
        print("Sabor no válido")

print("\n==== RESUMEN DE PEDIDOS ====")
print("Vainilla:", vainilla)
print("Chocolate:", chocolate)
print("Fresa:", fresa)
print("======= FOR RIWI ============")


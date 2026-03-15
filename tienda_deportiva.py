contador = 0

# Con el for defino las cantidades que queriero que se repita el ciclo
for i in range (6):
  precio = float(input("INGRESE EL PRECIO DEL PRODUCTO: "))

  if precio > 100000:
    contador += 1

    print("PRODUCTO QUE CUESTAN MÁS DE 100000:", contador)
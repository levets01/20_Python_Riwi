cafe = 4000
te = 35000
jugo = 5000
print(" WELCOME CAFETERIA IGLESIAS ")

bebida = input("¿QUE BEBIDA QUIERES? CAFE , TÉ O JUGUO: ").lower()


cantidad = int(input("¿CUANTAS UNIDADES DESEA ?: "))

if bebida == "cafe":
    
     total = cafe * cantidad
     
elif bebida == "te":
    
   total = te * cantidad

elif bebida == "jugo":
    
    total = jugo * cantidad
else:
     
    print("BEBIDA NO DISPONIBLE")
    
    total = 0
    
print("\n ===== TOTAL A PAGAR ====")

print(total)

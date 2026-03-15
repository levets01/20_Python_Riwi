print("WELCOME CINE COLOMBIA")

while True:
    try:
        edad = int(input("POR FAVOR INGRESE SU EDAD : "))

        if edad < 0:
            print ("ERROR: la edad no puede ser negativa.")

            continue 

      
            break
        
    except ValueError:
        
        print("ERROR: por favor ingrese un número válido para la edad.")
    
    if edad <=12 :
        print ("EL VALOR DE SU ENTRADA ES DE $8.000")

    elif edad >= 59:
        print ("EL VALOR DE SU ENTRADA ES DE $12.000")

    else:
        print ("EL VALOR DE SU ENTRADA ES DE $9.000")
print("TIENDA DE MASCOTAS\n")

while True:
    mascotas = input("INGRESE EL TIPO DE MASCOTA (perro, gato, conejo): ").lower()
    
# EL ISALPHA ES PARA QUE SOLO SE PERMITAN LETRAS Y NO VALORES NUMERICOS EN EL INPUT 
    if mascotas.isalpha():
        break
    else:
        print("ERROR: SOLO SE PERMITEN LETRAS")

if mascotas == "perro":
    print("RECOMENDACION: ALIMENTOS BALANCEADOS PARA PERRO")

elif mascotas == "gato":
    print("RECOMENDACION: CONCENTRADO PARA GATOS")

elif mascotas == "conejo":
    print("RECOMENDACION: HENO Y VERDURAS FRESCAS")

else:
    print("NO TENEMOS RECOMENDACION PARA ESE ANIMAL.")
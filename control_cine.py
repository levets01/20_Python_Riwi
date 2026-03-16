print("===== CINE COLOMBIA =====")

capacidad = 5

ninos = 0
adultos = 0
mayores = 0

for i in range(capacidad):

    edad = int(input("Ingrese la edad de la persona: "))

    if edad < 18:
        ninos += 1

    elif edad < 60:
        adultos += 1

    else:
        mayores += 1

print("\n==== Resumen de la sala ===")
print("Niños:", ninos)
print("Adultos:", adultos)
print("Adultos mayores:", mayores)
print("=============================")
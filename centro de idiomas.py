print("##### CENTRO DE IDIOMAS ####### ")

mejor_promedio = 0
mejor_estudiante = ""

for i in range(3):

    nombre = input("Nombre del estudiante: ")

    speaking = float(input("Nota speaking: "))
    listening = float(input("Nota listening: "))
    reading = float(input("Nota reading: "))

    promedio = (speaking + listening + reading) / 3

    print("Promedio:", promedio)

    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_estudiante = nombre

print("\nMejor estudiante:", mejor_estudiante)
print("Promedio:", mejor_promedio)
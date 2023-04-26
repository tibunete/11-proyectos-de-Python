significado_completo = input("Ingrese palabra para convertir en acronimo: ")

palabras = significado_completo.split()

acronimo = ""

for palabra in palabras:
    acronimo += palabra[0]

print("El acrónimo de ", significado_completo, " es: ", acronimo.upper())

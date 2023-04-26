canciones = {
    "1": "Canción 1: Letra de la canción 1",
    "2": "Canción 2: Letra de la canción 2",
    "3": "Canción 3: Letra de la canción 3",
    "4": "Canción 4: Letra de la canción 4",
    "5": "Canción 5: Letra de la canción 5",
    "6": "Canción 6: Letra de la canción 6",
    "7": "Canción 7: Letra de la canción 7",
    "8": "Canción 8: Letra de la canción 8",
    "9": "Canción 9: Letra de la canción 9",
    "10": "Canción 10: Letra de la canción 10",
}

print("Elige una canción del 1 al 10:")
for key, value in canciones.items():
    print(key + ". " + value)
eleccion = input("Ingresa un numero de la lista: ")

if eleccion in canciones.keys():
    print("\nLetra de la canción seleccionada:\n" + canciones[eleccion])
else:
    print("Selección no válida. Elige un número del 1 al 10.")

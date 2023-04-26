import random

def juego():
    opciones = ["Piedra", "Papel", "Tijeras"]
    jugador = input("Elige piedra, papel o tijeras: ").capitalize()
    computadora = random.choice(opciones)
    print(f"\nTu elegiste {jugador}.")
    print(f"La computadora eligió {computadora}.\n")
    if jugador == computadora:
        print(f"Ambos eligieron {jugador}. ¡Es un empate!")
    elif jugador == "Piedra":
        if computadora == "Papel":
            print("El papel envuelve a la piedra. ¡Perdiste!")
        else:
            print("La piedra aplasta las tijeras. ¡Ganaste!")
    elif jugador == "Papel":
        if computadora == "Tijeras":
            print("Las tijeras cortan el papel. ¡Perdiste!")
        else:
            print("El papel envuelve la piedra. ¡Ganaste!")
    elif jugador == "Tijeras":
        if computadora == "Piedra":
            print("La piedra aplasta las tijeras. ¡Perdiste!")
        else:
            print("Las tijeras cortan el papel. ¡Ganaste!")
    else:
        print("Esa no es una opción válida. Inténtalo de nuevo.")
    jugar_de_nuevo()

def jugar_de_nuevo():
    jugar_otra_vez = input("¿Quieres jugar de nuevo? (Si/No): ").capitalize()
    if jugar_otra_vez == "Si":
        juego()
    elif jugar_otra_vez == "No":
        print("¡Gracias por jugar!")
    else:
        print("No entendí tu respuesta. Por favor, responde con Si o No.")
        jugar_de_nuevo()

juego()

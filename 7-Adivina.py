import random

def guess_number():
    # Generamos un número aleatorio entre 1 y 50
    number = random.randint(1, 50)
    max_attempts = 5
    attempts = 0
    
    # Empezamos el juego
    while attempts < max_attempts:
        guess = int(input("Adivina el número entre 1 y 50: "))
        
        # Verificamos si el número está dentro del rango adecuado
        if guess < 1 or guess > 50:
            print("Número inválido. Debe estar entre 1 y 50.")
            continue
        
        attempts += 1
        
        # Verificamos si el usuario adivinó el número
        if guess == number:
            print(f"Felicidades, adivinaste el número en {attempts} intentos.")
            return
        else:
            # El usuario no adivinó el número, informamos cuántos intentos quedan
            remaining_attempts = max_attempts - attempts
            print(f"Número incorrecto. Te quedan {remaining_attempts} intentos.")
    
    # Si el usuario no adivina el número dentro del número máximo de intentos, pierde
    print(f"Lo siento, no adivinaste el número en {max_attempts} intentos. El número era {number}.")

# Llamamos a la función para ejecutar el juego
guess_number()


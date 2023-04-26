# Solicitar información personal
nombre = input("Ingresa tu nombre completo: ")

# Verificar si el nombre ingresado contiene solo letras y espacios
while not nombre.replace(' ', '').isalpha():
    nombre = input("Ingresa un nombre válido (solo letras y espacios): ")

# Solicitar información adicional
edad = input("Ingresa tu edad: ")
telefono = input("Ingresa tu número de teléfono: ")
correo = input("Ingresa tu correo electrónico: ")

# Imprimir resumen de la información ingresada
print("\nResumen de la información ingresada:")
print("Nombre: ", nombre)
print("Edad: ", edad)
print("Teléfono: ", telefono)
print("Correo electrónico: ", correo)


import re
popular_domains = ["gmail.com", "uabc.edu.com", "outlook.com"]

email = input("Introduce tu dirección de correo electrónico: ")

match = re.search(r'(?<=@)[^.@][^@]+', email)
if match:
    domain = match.group(0)
else:
    print("Dirección de correo electrónico no válida")

if domain in popular_domains:
    print("Este es un correo electrónico con un dominio popular")
else:
    print("Este es un correo electrónico con un dominio personalizado")

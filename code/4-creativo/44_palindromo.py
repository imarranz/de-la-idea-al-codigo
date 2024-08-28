# Pedimos al usuario que ingrese una palabra o frase
texto = input("Ingresa una palabra o frase: ").replace(" ", "").lower()  # Eliminamos espacios y convertimos a minúsculas

# Verificamos si el texto es un palíndromo
if texto == texto[::-1]:  # Comparamos el texto con su versión invertida
    print("Es un palíndromo.")  # Imprime si el texto es un palíndromo
else:
    print("No es un palíndromo.")  # Imprime si el texto no es un palíndromo

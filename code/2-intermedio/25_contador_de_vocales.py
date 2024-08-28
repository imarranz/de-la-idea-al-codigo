# Pedimos al usuario que ingrese una cadena de texto
texto = input("Ingresa una cadena de texto: ")  # Guardamos la entrada del usuario

# Definimos un conjunto de vocales para comparar
vocales = "aeiouAEIOU"  # Incluimos tanto mayúsculas como minúsculas
contador = 0  # Inicializamos un contador

# Iteramos a través de cada carácter en la cadena
for char in texto:
    if char in vocales:  # Verificamos si el carácter es una vocal
        contador += 1  # Aumentamos el contador si es una vocal

# Mostramos el número total de vocales encontradas
print("El número de vocales en la cadena es:", contador)  # Imprime el conteo de vocales

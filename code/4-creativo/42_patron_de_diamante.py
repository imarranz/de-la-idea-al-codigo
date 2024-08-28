# Pedimos al usuario que ingrese el número de filas para la mitad del diamante
filas = int(input("Ingresa el número de filas para la mitad del diamante: "))  # Convertimos la entrada a un número entero

# Construimos la mitad superior del diamante
for i in range(1, filas + 1):  # Iteramos desde 1 hasta el número de filas
    print(" " * (filas - i) + "*" * (2 * i - 1))  # Imprime los espacios y los asteriscos

# Construimos la mitad inferior del diamante
for i in range(filas - 1, 0, -1):  # Iteramos de regreso desde el número de filas menos 1 hasta 1
    print(" " * (filas - i) + "*" * (2 * i - 1))  # Imprime los espacios y los asteriscos

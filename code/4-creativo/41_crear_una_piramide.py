# Pedimos al usuario que ingrese el número de filas para la pirámide
filas = int(input("¿Cuántas filas tendrá la pirámide? "))  # Convertimos la entrada a un número entero

# Usamos un bucle for para construir la pirámide
for i in range(1, filas + 1):  # Iteramos desde 1 hasta el número de filas
    print(" " * (filas - i) + "*" * (2 * i - 1))  # Imprime los espacios y los asteriscos correspondientes en cada fila

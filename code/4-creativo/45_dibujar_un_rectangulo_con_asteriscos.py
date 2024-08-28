# Pedimos al usuario que ingrese la longitud y el ancho del rectángulo
longitud = int(input("Ingresa la longitud del rectángulo: "))  # Convertimos la entrada a un número entero
ancho = int(input("Ingresa el ancho del rectángulo: "))  # Convertimos la entrada a un número entero

# Dibujamos el rectángulo usando un bucle for
for i in range(ancho):  # Iteramos tantas veces como el ancho
    print("*" * longitud)  # Imprimimos una fila de asteriscos de longitud dada

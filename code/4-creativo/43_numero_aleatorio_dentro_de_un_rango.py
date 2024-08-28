import random  # Importamos la biblioteca random para generar un número aleatorio

# Pedimos al usuario que ingrese los límites inferior y superior del rango
limite_inferior = int(input("Ingresa el límite inferior del rango: "))  # Convertimos la entrada a un número entero
limite_superior = int(input("Ingresa el límite superior del rango: "))  # Convertimos la entrada a un número entero

# Generamos un número aleatorio dentro del rango dado
numero_aleatorio = random.randint(limite_inferior, limite_superior)  # Genera un número aleatorio dentro del rango

# Mostramos el número aleatorio
print(f"El número aleatorio entre {limite_inferior} y {limite_superior} es: {numero_aleatorio}")  # Imprime el número aleatorio

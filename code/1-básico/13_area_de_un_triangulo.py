# Pedimos al usuario que ingrese la base y la altura del triángulo
base = float(input("Ingresa la base del triángulo: "))  # Convertimos la entrada a un número decimal
altura = float(input("Ingresa la altura del triángulo: "))  # Convertimos la entrada a un número decimal

# Calculamos el área usando la fórmula: (base * altura) / 2
area = (base * altura) / 2  # Multiplicamos base por altura y dividimos por 2

# Mostramos el resultado al usuario
print("El área del triángulo es:", area)  # Imprime el área calculada


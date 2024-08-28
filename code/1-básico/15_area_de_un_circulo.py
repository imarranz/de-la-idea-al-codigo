import math  # Importamos la biblioteca math para usar el valor de pi

# Pedimos al usuario que ingrese el radio del círculo
radio = float(input("Ingresa el radio del círculo: "))  # Convertimos la entrada a un número decimal

# Calculamos el área usando la fórmula: pi * radio^2
area = math.pi * radio * radio  # Multiplicamos pi por el radio elevado al cuadrado

# Mostramos el resultado al usuario
print("El área del círculo es:", area)  # Imprime el área calculada

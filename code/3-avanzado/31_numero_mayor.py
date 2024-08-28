# Pedimos al usuario que ingrese tres números
num1 = float(input("Ingresa el primer número: "))  # Convertimos la entrada a un número decimal
num2 = float(input("Ingresa el segundo número: "))  # Convertimos la entrada a un número decimal
num3 = float(input("Ingresa el tercer número: "))  # Convertimos la entrada a un número decimal

# Usamos la función max para encontrar el número mayor
mayor = max(num1, num2, num3)  # Encuentra el mayor de los tres números

# Mostramos el número mayor
print("El número mayor es:", mayor)  # Imprime el mayor número

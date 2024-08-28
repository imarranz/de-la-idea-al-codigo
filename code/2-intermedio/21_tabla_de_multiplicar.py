# Pedimos al usuario que ingrese un número para calcular su tabla de multiplicar
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))  # Convertimos la entrada a un número entero

# Usamos un bucle for para iterar desde 1 hasta 10
for i in range(1, 11):  # Recorremos los números del 1 al 10
    # Mostramos el resultado de la multiplicación en cada iteración
    print(f"{numero} x {i} = {numero * i}")  # Imprime el resultado de la multiplicación

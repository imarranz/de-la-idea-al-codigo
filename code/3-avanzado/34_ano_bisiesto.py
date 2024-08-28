# Pedimos al usuario que ingrese un año
ano = int(input("Ingresa un año: "))  # Convertimos la entrada a un número entero

# Verificamos si el año es bisiesto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"El año {ano} es bisiesto.")  # Imprime si el año es bisiesto
else:
    print(f"El año {ano} no es bisiesto.")  # Imprime si el año no es bisiesto

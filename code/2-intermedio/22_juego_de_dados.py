import random  # Importamos la biblioteca random para generar números aleatorios

# Generamos dos números aleatorios entre 1 y 6, como si fueran dados
dado1 = random.randint(1, 6)  # Genera un número aleatorio para el primer dado
dado2 = random.randint(1, 6)  # Genera un número aleatorio para el segundo dado

# Mostramos los valores de los dados
print(f"El primer dado sacó: {dado1}")  # Imprime el valor del primer dado
print(f"El segundo dado sacó: {dado2}")  # Imprime el valor del segundo dado

# Determinamos quién ganó o si fue un empate
if dado1 > dado2:
    print("El primer dado gana!")  # Imprime si el primer dado es mayor
elif dado1 < dado2:
    print("El segundo dado gana!")  # Imprime si el segundo dado es mayor
else:
    print("¡Es un empate!")  # Imprime si ambos dados tienen el mismo valor

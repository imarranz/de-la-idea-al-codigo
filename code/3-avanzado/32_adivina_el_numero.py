import random  # Importamos la biblioteca random para generar un número aleatorio

# Generamos un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)  # Guardamos el número aleatorio

intentos = 0  # Inicializamos un contador de intentos

# Creamos un bucle para que el usuario adivine el número
while True:
    intento = int(input("Adivina el número (entre 1 y 100): "))  # Pedimos un número al usuario
    intentos += 1  # Aumentamos el contador de intentos

    # Comparamos el intento con el número secreto
    if intento < numero_secreto:
        print("Muy bajo, intenta de nuevo.")  # El número es menor al secreto
    elif intento > numero_secreto:
        print("Muy alto, intenta de nuevo.")  # El número es mayor al secreto
    else:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")  # El número es correcto
        break  # Salimos del bucle

from datetime import datetime  # Importamos la biblioteca datetime para manejar fechas

# Pedimos al usuario que ingrese su año de nacimiento
ano_nacimiento = int(input("¿En qué año naciste? "))  # Convertimos la entrada a un número entero

# Obtenemos el año actual usando datetime
ano_actual = datetime.now().year  # Obtenemos el año actual

# Calculamos la edad restando el año de nacimiento al año actual
edad = ano_actual - ano_nacimiento  # Calculamos la diferencia de años

# Mostramos la edad del usuario
print(f"Tienes {edad} años.")  # Imprime la edad calculada

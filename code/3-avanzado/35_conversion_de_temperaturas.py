# Pedimos al usuario que elija la conversión que desea hacer
opcion = input("¿Deseas convertir de Celsius a Fahrenheit (C) o de Fahrenheit a Celsius (F)? ").strip().upper()

# Dependiendo de la opción, hacemos la conversión correspondiente
if opcion == "C":
    celsius = float(input("Ingresa la temperatura en Celsius: "))  # Pedimos la temperatura en Celsius
    fahrenheit = (celsius * 9/5) + 32  # Convertimos a Fahrenheit usando la fórmula
    print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")  # Mostramos el resultado
elif opcion == "F":
    fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))  # Pedimos la temperatura en Fahrenheit
    celsius = (fahrenheit - 32) * 5/9  # Convertimos a Celsius usando la fórmula
    print(f"{fahrenheit} grados Fahrenheit son {celsius} grados Celsius.")  # Mostramos el resultado
else:
    print("Opción no válida. Por favor elige 'C' o 'F'.")  # Mensaje si la opción es inválida

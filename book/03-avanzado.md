
\clearpage
\newpage

## Capítulo 3: Programación Avanzada

¡Bienvenido al tercer capítulo de nuestro viaje en el mundo de la programación! Hasta ahora, has aprendido los conceptos básicos y has explorado cómo las computadoras pueden tomar decisiones y realizar tareas repetitivas. En este capítulo, vamos a profundizar un poco más en la programación y enfrentarnos a desafíos más complejos. Este es el momento de combinar lo que has aprendido y aplicarlo a problemas que requieren un pensamiento más avanzado.

Trabajaremos con cálculos más sofisticados, como determinar el número mayor entre tres valores, crear un juego para adivinar números, calcular la edad basándonos en el año de nacimiento, y verificar si un año es bisiesto. Estos ejercicios no solo te ayudarán a mejorar tus habilidades de programación, sino que también te mostrarán cómo la programación puede ser útil en situaciones prácticas de la vida real.

### 3.1 Número Mayor

#### El Reto

En este ejercicio, necesitamos determinar cuál es el número mayor entre tres valores proporcionados por el usuario. Este tipo de problema es útil cuando se trabaja con comparaciones y decisiones basadas en condiciones.

#### Cómo Resolverlo

Para resolver este problema, utilizaremos la función `max()` de Python, que nos permite encontrar el valor máximo entre varios números. Pediremos al usuario que ingrese tres números, los compararemos y luego mostraremos el número mayor.

#### Pseudocódigo

1. Empezar el programa.
2. Pedir al usuario que ingrese el primer número.
3. Pedir al usuario que ingrese el segundo número.
4. Pedir al usuario que ingrese el tercer número.
5. Comparar los tres números usando la función `max`.
6. Mostrar el número mayor en la pantalla.
7. Finalizar el programa.

#### Código

```python
# Pedimos al usuario que ingrese tres números
num1 = float(input("Ingresa el primer número: "))  # Convertimos la entrada a un número decimal
num2 = float(input("Ingresa el segundo número: "))  # Convertimos la entrada a un número decimal
num3 = float(input("Ingresa el tercer número: "))  # Convertimos la entrada a un número decimal

# Usamos la función max para encontrar el número mayor
mayor = max(num1, num2, num3)  # Encuentra el mayor de los tres números

# Mostramos el número mayor
print("El número mayor es:", mayor)  # Imprime el mayor número
```

#### Desafío

¿Y si ampliamos el programa para que funcione con más de tres números? Modifica el código para que el usuario pueda ingresar tantos números como quiera, y el programa le diga cuál es el mayor.

---

### 3.2 Adivina el Número

#### El Reto

Vamos a crear un juego sencillo en el que la computadora elige un número al azar entre 1 y 100, y el usuario tiene que adivinarlo. Después de cada intento, la computadora dará pistas indicando si el número es mayor o menor que el intento del usuario.

#### Cómo Resolverlo

Para resolver este problema, utilizaremos la función `randint()` de la biblioteca `random` para generar un número aleatorio. Luego, usaremos un bucle `while` para permitir al usuario hacer intentos hasta que adivine correctamente. En cada intento, compararemos el número ingresado por el usuario con el número secreto y daremos una pista.

#### Pseudocódigo

1. Empezar el programa.
2. Generar un número aleatorio entre 1 y 100 y guardarlo como `numero_secreto`.
3. Inicializar un contador de intentos en 0.
4. Repetir hasta que el usuario adivine el número:
   - Pedir al usuario que ingrese un número.
   - Aumentar el contador de intentos.
   - Si el número es menor que `numero_secreto`, mostrar "Muy bajo, intenta de nuevo".
   - Si el número es mayor que `numero_secreto`, mostrar "Muy alto, intenta de nuevo".
   - Si el número es igual a `numero_secreto`, mostrar "Felicidades" y salir del bucle.
5. Mostrar el número de intentos realizados.
6. Finalizar el programa.

#### Código

```python
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
        print(f"Felicidades, adivinaste el número en {intentos} intentos.")  # El número es correcto
        break  # Salimos del bucle
```

#### Desafío

¿Qué tal si hacemos el juego un poco más difícil? ¿Puedes limitar el número de intentos que tiene el usuario? Modifica el programa para que, si no adivina el número en un número determinado de intentos, pierda el juego.

---

### 3.3 Calcula la Edad

#### El Reto

En este ejercicio, vamos a calcular la edad de una persona basándonos en su año de nacimiento. Este ejercicio es útil para aprender a trabajar con fechas y operaciones aritméticas básicas.

#### Cómo Resolverlo

Para resolver este problema, primero pediremos al usuario que ingrese su año de nacimiento. Luego, obtendremos el año actual utilizando la biblioteca `datetime`, restaremos el año de nacimiento del año actual, y así obtendremos la edad de la persona.

#### Pseudocódigo

1. Empezar el programa.
2. Pedir al usuario que ingrese su año de nacimiento.
3. Obtener el año actual utilizando la biblioteca `datetime`.
4. Calcular la edad restando el año de nacimiento del año actual.
5. Mostrar la edad en la pantalla.
6. Finalizar el programa.

#### Código

```python
from datetime import datetime  # Importamos la biblioteca datetime para manejar fechas

# Pedimos al usuario que ingrese su año de nacimiento
ano_nacimiento = int(input("¿En qué año naciste? "))  # Convertimos la entrada a un número entero

# Obtenemos el año actual usando datetime
ano_actual = datetime.now().year  # Obtenemos el año actual

# Calculamos la edad restando el año de nacimiento al año actual
edad = ano_actual - ano_nacimiento  # Calculamos la diferencia de años

# Mostramos la edad del usuario
print(f"Tienes {edad} años.")  # Imprime la edad calculada
```

#### Desafío

¿Y si además de calcular la edad, calculamos cuántos días ha vivido la persona? Intenta modificar el programa para mostrar tanto la edad en años como en días.

---

### 3.4 Año Bisiesto

#### El Reto

Un año bisiesto es aquel que tiene un día adicional (29 de febrero), y ocurre cada cuatro años, con algunas excepciones. En este ejercicio, escribiremos un programa que determine si un año ingresado por el usuario es bisiesto o no.

#### Cómo Resolverlo

Para resolver este problema, aplicaremos las reglas de los años bisiestos: un año es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400. Usaremos estas condiciones en un bloque `if-elif-else`.

#### Pseudocódigo

1. Empezar el programa.
2. Pedir al usuario que ingrese un año.
3. Verificar si el año es divisible por 4 y no divisible por 100, o si es divisible por 400:
   - Si es así, mostrar que el año es bisiesto.
   - De lo contrario, mostrar que el año no es bisiesto.
4. Finalizar el programa.

#### Código

```python
# Pedimos al usuario que ingrese un año
ano = int(input("Ingresa un año: "))  # Convertimos la entrada a un número entero

# Verificamos si el año es bisiesto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"El año {ano} es bisiesto.")  # Imprime si el año es bisiesto
else:
    print(f"El año {ano} no es bisiesto.")  # Imprime si el año no es bisiesto
```

#### Desafío

¿Qué tal si hacemos que el programa muestre todos los años bisiestos desde el año 1 hasta el año actual? Modifica el programa para que muestre una lista de años bisiestos en ese rango.


---

### 3.5 Conversión de Temperaturas

#### El Reto

En este ejercicio, vamos a crear un programa que convierta temperaturas de Celsius a Fahrenheit y viceversa. La conversión de temperaturas es un ejercicio práctico que refuerza el uso de fórmulas matemáticas y toma de decisiones en programación.

#### Cómo Resolverlo

Para resolver este problema, primero pediremos al usuario que elija qué conversión desea realizar. Dependiendo de su elección, realizaremos la conversión utilizando las fórmulas correspondientes. Mostraremos el resultado final al usuario.

#### Pseudocódigo

1. Empezar el programa.
2. Pedir al usuario que elija entre convertir de Celsius a Fahrenheit o de Fahrenheit a Celsius.
3. Si elige Celsius a Fahrenheit:
   - Pedir la temperatura en Celsius.
   - Convertirla a Fahrenheit usando la fórmula correspondiente.
   - Mostrar el resultado.
4. Si elige Fahrenheit a Celsius:
   - Pedir la temperatura en Fahrenheit.
   - Convertirla a Celsius usando la fórmula correspondiente.
   - Mostrar el resultado.
5. Si la opción no es válida, mostrar un mensaje de error.
6. Finalizar el programa.

#### Código

```python
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
```

#### Desafío

¿Puedes hacer que el programa convierta también de Kelvin a Celsius y de Celsius a Kelvin? Añade estas opciones al menú de conversiones para que el usuario tenga más posibilidades.

---

¡Y con esto, hemos completado nuestro tercer capítulo! Estos ejercicios avanzados te han mostrado cómo resolver problemas más complejos y te han dado una idea de cómo la programación puede aplicarse a situaciones del mundo real. En el próximo capítulo, exploraremos la programación creativa, donde tendrás la oportunidad de usar todo lo que has aprendido para crear programas divertidos y originales. ¡Sigue adelante y no dejes de practicar!

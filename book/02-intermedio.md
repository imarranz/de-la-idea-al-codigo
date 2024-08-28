
## Capítulo 2: Programación Intermedia

¡Felicidades por completar el primer capítulo! Ahora que ya tienes una base sólida en los conceptos básicos de programación, es momento de dar un paso más y explorar algunas ideas más complejas. En este capítulo, nos centraremos en cómo las computadoras pueden tomar decisiones y realizar tareas repetitivas automáticamente. Estos conceptos son fundamentales en la programación, ya que nos permiten escribir programas más útiles y dinámicos.

Vamos a explorar cómo podemos crear tablas de multiplicar, jugar a los dados de manera automática, y cómo hacer que la computadora nos salude de manera personalizada. Además, trabajaremos con cadenas de texto para realizar tareas más interesantes, como contar vocales. Este capítulo está diseñado para que practiques y consolides lo que has aprendido, mientras te introduces en conceptos más avanzados que te prepararán para los desafíos que vendrán en los siguientes capítulos.

### 2.1 Tabla de Multiplicar

#### El Reto

Una de las primeras cosas útiles que podemos hacer con la programación es automatizar cálculos repetitivos. En este ejercicio, vamos a crear un programa que genere la tabla de multiplicar de cualquier número que el usuario elija. Esto es útil no solo para practicar matemáticas, sino también para entender cómo funcionan los bucles en programación.

#### Cómo Resolverlo

Para resolver este problema, utilizaremos un bucle `for` que recorre los números del 1 al 10. En cada iteración del bucle, multiplicaremos el número ingresado por el usuario por el número de la iteración, y mostraremos el resultado.

#### Pseudocódigo

1. Empezar el programa.
2. Pedir al usuario que ingrese un número.
3. Para cada número del 1 al 10:
   - Multiplicar el número del usuario por el número actual del bucle.
   - Mostrar el resultado de la multiplicación.
4. Finalizar el programa.

#### Código

```python
# Pedimos al usuario que ingrese un número para calcular su tabla de multiplicar
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))  # Convertimos la entrada a un número entero

# Usamos un bucle for para iterar desde 1 hasta 10
for i in range(1, 11):  # Recorremos los números del 1 al 10
    # Mostramos el resultado de la multiplicación en cada iteración
    print(f"{numero} x {i} = {numero * i}")  # Imprime el resultado de la multiplicación
```

---

### 2.2 Juego de Dados

#### El Reto

¡Hora de divertirnos un poco! En este ejercicio, vamos a simular el lanzamiento de dos dados y determinar cuál de los dos tiene el valor más alto. Esto es una excelente práctica para trabajar con números aleatorios, un concepto muy útil en la programación de juegos.

#### Cómo Resolverlo

Para resolver este problema, usaremos la función `randint()` de la biblioteca `random` para simular el lanzamiento de los dados. Luego, compararemos los valores obtenidos para determinar el ganador.

#### Pseudocódigo

1. Empezar el programa.
2. Generar un número aleatorio entre 1 y 6 para el primer dado.
3. Generar un número aleatorio entre 1 y 6 para el segundo dado.
4. Mostrar los valores de ambos dados.
5. Comparar los valores:
   - Si el primer dado es mayor, mostrar que el primer dado gana.
   - Si el segundo dado es mayor, mostrar que el segundo dado gana.
   - Si los dos dados son iguales, mostrar que es un empate.
6. Finalizar el programa.

#### Código

```python
import random  # Importamos la biblioteca random para generar números aleatorios

# Generamos dos números aleatorios entre 1 y 6, como si fueran dados
dado1 = random.randint(1, 6)  # Genera un número aleatorio para el primer dado
dado2 = random.randint(1, 6)  # Genera un número aleatorio para el segundo dado

# Mostramos los valores de los dados
print(f"El primer dado sacó: {dado1}")  # Imprime el valor del primer dado
print(f"El segundo dado sacó: {dado2}")  # Imprime el valor del segundo dado

# Determinamos quién ganó o si fue un empate
if dado1 > dado2:
    print("El primer dado gana")  # Imprime si el primer dado es mayor
elif dado1 < dado2:
    print("El segundo dado gana")  # Imprime si el segundo dado es mayor
else:
    print("Es un empate")  # Imprime si ambos dados tienen el mismo valor
```

---

### 2.3 Saludo Personalizado

#### El Reto

En este ejercicio, vamos a hacer que el programa sea más interactivo. Queremos que el programa pregunte el nombre del usuario y luego lo salude de manera personalizada. Esto es un gran ejemplo de cómo los programas pueden interactuar con las personas y hacer que la experiencia sea más personal y divertida.

#### Cómo Resolverlo

Para resolver este problema, usaremos la función `input()` para obtener el nombre del usuario y luego usaremos la función `print()` para mostrar un mensaje personalizado.

#### Pseudocódigo

1. Empezar el programa.
2. Pedir al usuario que ingrese su nombre.
3. Mostrar un saludo personalizado usando el nombre del usuario.
4. Finalizar el programa.

#### Código

```python
# Pedimos al usuario que ingrese su nombre
nombre = input("¿Cuál es tu nombre? ")  # Guardamos la entrada del usuario

# Saludamos al usuario usando su nombre
print(f"Hola, {nombre}")  # Imprime un saludo personalizado
```

---

### 2.4 Cadenas de Texto

#### El Reto

Las cadenas de texto son una parte fundamental de la programación. En este ejercicio, vamos a trabajar con cadenas para aprender cómo podemos manipular texto en Python. Específicamente, vamos a pedir al usuario que ingrese una cadena de texto, y luego vamos a realizar algunas operaciones básicas con esa cadena.

#### Cómo Resolverlo

Trabajaremos con varias funciones incorporadas en Python para manipular la cadena de texto. Veremos cómo contar la longitud de la cadena, convertirla a mayúsculas y mostrarla al revés.

#### Pseudocódigo

1. Empezar el programa.
2. Pedir al usuario que ingrese una cadena de texto.
3. Mostrar la longitud de la cadena.
4. Convertir la cadena a mayúsculas y mostrarla.
5. Invertir la cadena y mostrarla.
6. Finalizar el programa.

#### Código

```python
# Pedimos al usuario que ingrese una cadena de texto
texto = input("Ingresa una cadena de texto: ")  # Guardamos la entrada del usuario

# Mostramos la longitud de la cadena
print("La longitud de la cadena es:", len(texto))  # Imprime el número de caracteres en la cadena

# Convertimos la cadena a mayúsculas y la mostramos
print("La cadena en mayúsculas es:", texto.upper())  # Convierte la cadena a mayúsculas

# Invertimos la cadena y la mostramos
print("La cadena al revés es:", texto[::-1])  # Imprime la cadena invertida
```

---

### 2.5 Contador de Vocales

#### El Reto

En este ejercicio, vamos a trabajar con cadenas de texto para contar cuántas vocales contiene una cadena. Este es un excelente ejercicio para practicar el trabajo con bucles y condiciones en programación.

#### Cómo Resolverlo

Para resolver este problema, recorreremos cada carácter de la cadena y verificaremos si es una vocal. Si lo es, aumentaremos un contador. Al final, mostraremos el número total de vocales encontradas.

#### Pseudocódigo

1. Empezar el programa.
2. Pedir al usuario que ingrese una cadena de texto.
3. Inicializar un contador de vocales en 0.
4. Recorrer cada carácter de la cadena:
   - Si el carácter es una vocal, aumentar el contador.
5. Mostrar el número total de vocales encontradas.
6. Finalizar el programa.

#### Código

```python
# Pedimos al usuario que ingrese una cadena de texto
texto = input("Ingresa una cadena de texto: ")  # Guardamos la entrada del usuario

# Definimos un conjunto de vocales para comparar
vocales = "aeiouAEIOU"  # Incluimos tanto mayúsculas como minúsculas
contador = 0  # Inicializamos un contador

# Iteramos a través de cada carácter en la cadena
for char in texto:
    if char in vocales:  # Verificamos si el carácter es una vocal
        contador += 1  # Aumentamos el contador si es una vocal

# Mostramos el número total de vocales encontradas
print("El número de vocales en la cadena es:", contador)  # Imprime el conteo de vocales
```

---

¡Y con esto, hemos completado nuestro segundo capítulo! Estos ejercicios intermedios te han enseñado a trabajar con bucles, condiciones y cadenas de texto, lo que te permitirá escribir programas más interactivos y útiles. En el próximo capítulo, profundizaremos aún más y te enfrentaremos a desafíos más avanzados que te ayudarán a convertirte en un programador aún más habilidoso. ¡Sigue así!


\clearpage
\newpage

## Capítulo 4: Programación Creativa

¡Bienvenido al capítulo más divertido de este manual! Hasta ahora, has aprendido los conceptos básicos, intermedios y avanzados de la programación en Python. En este último capítulo, vamos a liberar toda tu creatividad. La programación no solo es una herramienta poderosa para resolver problemas, sino que también es una forma de arte. Aquí, tendrás la oportunidad de usar todo lo que has aprendido para crear programas que no solo son funcionales, sino también visualmente interesantes y divertidos de usar.

Desde construir pirámides con asteriscos hasta diseñar patrones de diamantes, estos ejercicios te animarán a pensar de manera creativa y a experimentar con el código. ¡Prepárate para jugar, explorar y dejar volar tu imaginación en el mundo de la programación creativa!

### 4.1 Crear una Pirámide

#### El Reto

Nuestro primer ejercicio creativo es construir una pirámide utilizando asteriscos (`*`). La altura de la pirámide será determinada por el usuario, y el programa imprimirá una pirámide con el número de filas especificado. Este ejercicio es ideal para practicar el uso de bucles y cómo manipular la salida en la consola.

#### Cómo Resolverlo

Para resolver este problema, usaremos un bucle `for` que se ejecutará tantas veces como filas tenga la pirámide. En cada iteración, imprimiremos un número creciente de asteriscos, precedidos por los espacios necesarios para centrar la pirámide.

#### Pseudocódigo

1. Empezar el programa.
2. Pedir al usuario que ingrese el número de filas de la pirámide.
3. Para cada número desde 1 hasta el número de filas:
   - Calcular el número de espacios para centrar la fila.
   - Calcular el número de asteriscos a imprimir.
   - Mostrar la fila con los espacios y asteriscos correspondientes.
4. Finalizar el programa.

#### Código

```python
# Pedimos al usuario que ingrese el número de filas para la pirámide
filas = int(input("¿Cuántas filas tendrá la pirámide? "))  # Convertimos la entrada a un número entero

# Usamos un bucle for para construir la pirámide
for i in range(1, filas + 1):  # Iteramos desde 1 hasta el número de filas
    print(" " * (filas - i) + "*" * (2 * i - 1))  # Imprime los espacios y los asteriscos correspondientes en cada fila
```

---

### 4.2 Patrón de Diamante

#### El Reto

En este ejercicio, vamos a crear un patrón de diamante utilizando asteriscos. La altura del diamante será determinada por el usuario. Este ejercicio es una extensión del ejercicio anterior y te permitirá practicar más el uso de bucles y el control de la salida en la consola.

#### Cómo Resolverlo

Para resolver este problema, dividiremos el patrón en dos partes: la mitad superior y la mitad inferior del diamante. Utilizaremos dos bucles `for`: uno para construir la mitad superior y otro para la mitad inferior.

#### Pseudocódigo

1. Empezar el programa.
2. Pedir al usuario que ingrese el número de filas para la mitad del diamante.
3. Para la mitad superior del diamante:
   - Para cada número desde 1 hasta el número de filas:
     - Calcular el número de espacios.
     - Calcular el número de asteriscos.
     - Mostrar la fila con los espacios y asteriscos correspondientes.
4. Para la mitad inferior del diamante:
   - Para cada número desde el número de filas menos 1 hasta 1:
     - Calcular el número de espacios.
     - Calcular el número de asteriscos.
     - Mostrar la fila con los espacios y asteriscos correspondientes.
5. Finalizar el programa.

#### Código

```python
# Pedimos al usuario que ingrese el número de filas para la mitad del diamante
filas = int(input("Ingresa el número de filas para la mitad del diamante: "))  # Convertimos la entrada a un número entero

# Construimos la mitad superior del diamante
for i in range(1, filas + 1):  # Iteramos desde 1 hasta el número de filas
    print(" " * (filas - i) + "*" * (2 * i - 1))  # Imprime los espacios y los asteriscos

# Construimos la mitad inferior del diamante
for i in range(filas - 1, 0, -1):  # Iteramos de regreso desde el número de filas menos 1 hasta 1
    print(" " * (filas - i) + "*" * (2 * i - 1))  # Imprime los espacios y los asteriscos
```

---

### 4.3 Número Aleatorio dentro de un Rango

#### El Reto

Este ejercicio es perfecto para aquellos que quieren explorar cómo generar números aleatorios en un rango específico. Vamos a crear un programa que genere un número aleatorio dentro de un rango definido por el usuario. Este ejercicio es útil en muchas aplicaciones, como juegos o simulaciones.

#### Cómo Resolverlo

Para resolver este problema, usaremos la función `randint()` de la biblioteca `random`. El usuario proporcionará los límites inferior y superior, y el programa generará un número aleatorio dentro de esos límites.

#### Pseudocódigo

1. Empezar el programa.
2. Pedir al usuario que ingrese el límite inferior del rango.
3. Pedir al usuario que ingrese el límite superior del rango.
4. Generar un número aleatorio dentro del rango dado.
5. Mostrar el número aleatorio generado en la pantalla.
6. Finalizar el programa.

#### Código

```python
import random  # Importamos la biblioteca random para generar un número aleatorio

# Pedimos al usuario que ingrese los límites inferior y superior del rango
limite_inferior = int(input("Ingresa el límite inferior del rango: "))  # Convertimos la entrada a un número entero
limite_superior = int(input("Ingresa el límite superior del rango: "))  # Convertimos la entrada a un número entero

# Generamos un número aleatorio dentro del rango dado
numero_aleatorio = random.randint(limite_inferior, limite_superior)  # Genera un número aleatorio dentro del rango

# Mostramos el número aleatorio
print(f"El número aleatorio entre {limite_inferior} y {limite_superior} es: {numero_aleatorio}")  # Imprime el número aleatorio
```

---

### 4.4 Palíndromo

#### El Reto

Un palíndromo es una palabra o frase que se lee igual de adelante hacia atrás. En este ejercicio, vamos a crear un programa que verifique si una palabra o frase ingresada por el usuario es un palíndromo. Este ejercicio es una excelente práctica para trabajar con cadenas de texto y manipulación de caracteres.

#### Cómo Resolverlo

Para resolver este problema, eliminaremos los espacios y convertiremos la cadena a minúsculas para que la verificación no sea sensible a mayúsculas o minúsculas. Luego, compararemos la cadena con su versión invertida.

#### Pseudocódigo

1. Empezar el programa.
2. Pedir al usuario que ingrese una palabra o frase.
3. Eliminar los espacios de la cadena y convertirla a minúsculas.
4. Invertir la cadena.
5. Comparar la cadena original con la cadena invertida.
   - Si son iguales, mostrar que es un palíndromo.
   - Si no son iguales, mostrar que no es un palíndromo.
6. Finalizar el programa.

#### Código

```python
# Pedimos al usuario que ingrese una palabra o frase
texto = input("Ingresa una palabra o frase: ").replace(" ", "").lower()  # Eliminamos espacios y convertimos a minúsculas

# Verificamos si el texto es un palíndromo
if texto == texto[::-1]:  # Comparamos el texto con su versión invertida
    print("Es un palíndromo.")  # Imprime si el texto es un palíndromo
else:
    print("No es un palíndromo.")  # Imprime si el texto no es un palíndromo
```

---

### 4.5 Dibujar un Rectángulo con Asteriscos

#### El Reto

Nuestro último ejercicio creativo consiste en dibujar un rectángulo utilizando asteriscos. La longitud y el ancho del rectángulo serán determinados por el usuario. Este ejercicio es útil para practicar la manipulación de la salida en la consola y para trabajar con bucles anidados.

#### Cómo Resolverlo

Para resolver este problema, utilizaremos un bucle `for` para controlar las filas del rectángulo y otro para imprimir los asteriscos en cada fila. El número de asteriscos en cada fila será determinado por la longitud del rectángulo.

#### Pseudocódigo

1. Empezar el programa.
2. Pedir al usuario que ingrese la longitud del rectángulo.
3. Pedir al usuario que ingrese el ancho del rectángulo.
4. Para cada fila desde 1 hasta el ancho:
   - Imprimir una línea de asteriscos con la longitud dada.
5. Finalizar el programa.

#### Código

```python
# Pedimos al usuario que ingrese la longitud y el ancho del rectángulo
longitud = int(input("Ingresa la longitud del rectángulo: "))  # Convertimos la entrada a un número entero
ancho = int(input("Ingresa el ancho del rectángulo: "))  # Convertimos la entrada a un número entero

# Dibujamos el rectángulo usando un bucle for
for i in range(ancho):  # Iteramos tantas veces como el ancho
    print("*" * longitud)  # Imprimimos una fila de asteriscos de longitud dada
```

---

¡Felicidades! Has completado el capítulo de Programación Creativa y, con ello, el último capítulo de este manual. Los ejercicios de este capítulo te han permitido experimentar con patrones y generar contenido visual interesante utilizando código. La programación es una herramienta poderosa no solo para resolver problemas, sino también para expresar tu creatividad. Ahora que has aprendido tanto, estás listo para seguir explorando y creando con Python. ¡El límite es tu imaginación!

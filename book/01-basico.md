
\clearpage
\newpage

## Capítulo 1: Conceptos Básicos de Programación

¡Bienvenidos al primer capítulo de nuestro viaje por el mundo de la programación! Aquí es donde todo comienza. En este capítulo, aprenderemos los conceptos fundamentales de la programación en Python, un lenguaje que es tan poderoso como fácil de aprender. Si nunca has programado antes, no te preocupes. Este capítulo está diseñado para llevarte de la mano, paso a paso, desde lo más básico hasta que tengas las herramientas necesarias para crear tus propios programas.

Empezaremos con algo muy sencillo: hacer que la computadora nos salude. A partir de ahí, veremos cómo realizar operaciones matemáticas básicas, calcular áreas de formas geométricas y más. Estos conceptos son la base de todo lo que haremos en los capítulos siguientes, así que presta mucha atención y, sobre todo, ¡diviértete mientras aprendes!

### 1.1 Hola Mundo

#### El Reto

El primer programa que todos los programadores escriben es el famoso "Hola Mundo". Se trata de un programa muy sencillo que simplemente muestra un mensaje en la pantalla. Es el equivalente en programación a dar el primer paso en un largo viaje.

#### Cómo Resolverlo

Para resolver este problema, usaremos la función `print()` en Python. Esta función es utilizada para mostrar mensajes en la pantalla. Es muy simple: solo necesitamos escribir el mensaje que queremos mostrar entre comillas dentro de la función `print()`.

#### Pseudocódigo

1. Empezar el programa.
2. Escribir el mensaje "Hola Mundo".
3. Mostrar el mensaje en la pantalla.
4. Finalizar el programa.

#### Código

```python
# Imprime un saludo simple en la pantalla
print("Hola Mundo")  # Esto imprimirá "Hola Mundo" en la consola
```

---

### 1.2 Calculadora Sencilla

#### El Reto

Nuestro siguiente paso es crear un programa que pueda realizar operaciones matemáticas básicas como suma, resta, multiplicación y división. Este es un excelente ejercicio para aprender a manejar números y operaciones aritméticas en Python.

#### Cómo Resolverlo

Para resolver este problema, pediremos al usuario que ingrese dos números. Luego, realizaremos las operaciones aritméticas con esos números y mostraremos los resultados. Usaremos la función `input()` para obtener los números y `print()` para mostrar los resultados.

#### Pseudocódigo

1. Empezar el programa.
2. Pedir al usuario que ingrese el primer número.
3. Pedir al usuario que ingrese el segundo número.
4. Sumar los dos números y mostrar el resultado.
5. Restar el segundo número del primero y mostrar el resultado.
6. Multiplicar los dos números y mostrar el resultado.
7. Dividir el primer número por el segundo y mostrar el resultado.
8. Finalizar el programa.

#### Código

```python
# Pedimos al usuario que ingrese dos números
num1 = float(input("Ingresa el primer número: "))  # Convertimos la entrada a un número decimal
num2 = float(input("Ingresa el segundo número: "))  # Convertimos la entrada a un número decimal

# Realizamos operaciones aritméticas básicas y mostramos los resultados
print("Suma:", num1 + num2)  # Imprime la suma de los dos números
print("Resta:", num1 - num2)  # Imprime la resta del segundo número del primero
print("Multiplicación:", num1 * num2)  # Imprime el producto de los dos números
print("División:", num1 / num2)  # Imprime la división del primer número por el segundo
```

---

### 1.3 Área de un Triángulo

#### El Reto

En este ejercicio, vamos a calcular el área de un triángulo. Esto es útil para aprender a trabajar con fórmulas matemáticas en un programa y para practicar el uso de variables y operaciones aritméticas.

#### Cómo Resolverlo

Para calcular el área de un triángulo, necesitamos la base y la altura. La fórmula para el área de un triángulo es:

$$\text{Área} = \frac{\text{base} \times \text{altura}}{2}$$

Pediremos al usuario que ingrese la base y la altura, y luego utilizaremos esta fórmula para calcular el área.

#### Pseudocódigo

1. Empezar el programa.
2. Pedir al usuario que ingrese la base del triángulo.
3. Pedir al usuario que ingrese la altura del triángulo.
4. Calcular el área del triángulo utilizando la fórmula: (base * altura) / 2.
5. Mostrar el área calculada en la pantalla.
6. Finalizar el programa.

#### Código

```python
# Pedimos al usuario que ingrese la base y la altura del triángulo
base = float(input("Ingresa la base del triángulo: "))  # Convertimos la entrada a un número decimal
altura = float(input("Ingresa la altura del triángulo: "))  # Convertimos la entrada a un número decimal

# Calculamos el área usando la fórmula: (base * altura) / 2
area = (base * altura) / 2  # Multiplicamos base por altura y dividimos por 2

# Mostramos el resultado al usuario
print("El área del triángulo es:", area)  # Imprime el área calculada
```

---

### 1.4 Área de un Cuadrado

#### El Reto

Ahora, vamos a calcular el área de un cuadrado. Este es un ejercicio sencillo pero importante para reforzar el concepto de cómo usar variables y realizar operaciones matemáticas básicas en Python.

#### Cómo Resolverlo

Para calcular el área de un cuadrado, solo necesitamos la longitud de uno de sus lados. La fórmula para el área de un cuadrado es:

$$\text{Área} = \text{lado} \times \text{lado}$$

Pediremos al usuario que ingrese la longitud del lado y luego calcularemos el área.

#### Pseudocódigo

1. Empezar el programa.
2. Pedir al usuario que ingrese la longitud de un lado del cuadrado.
3. Calcular el área del cuadrado utilizando la fórmula: lado * lado.
4. Mostrar el área calculada en la pantalla.
5. Finalizar el programa.

#### Código

```python
# Pedimos al usuario que ingrese la longitud de un lado del cuadrado
lado = float(input("Ingresa la longitud de un lado del cuadrado: "))  # Convertimos la entrada a un número decimal

# Calculamos el área usando la fórmula: lado * lado
area = lado * lado  # Elevamos al cuadrado el valor ingresado

# Mostramos el resultado al usuario
print("El área del cuadrado es:", area)  # Imprime el área calculada
```

---

### 1.5 Área de un Círculo

#### El Reto

Finalmente, vamos a calcular el área de un círculo. Este ejercicio es un poco más avanzado porque involucra el uso de la constante matemática $\pi$ (pi).

#### Cómo Resolverlo

Para calcular el área de un círculo, necesitamos el radio. La fórmula para el área de un círculo es:

$$\text{Área} = \pi \times \text{radio}^2$$

Python tiene una biblioteca llamada `math` que incluye el valor de $\pi$. Usaremos esta biblioteca para hacer nuestro cálculo.

#### Pseudocódigo

1. Empezar el programa.
2. Importar la biblioteca `math` para usar $\pi$.
3. Pedir al usuario que ingrese el radio del círculo.
4. Calcular el área del círculo utilizando la fórmula: $\pi \times \text{radio}^2$.
5. Mostrar el área calculada en la pantalla.
6. Finalizar el programa.

#### Código

```python
import math  # Importamos la biblioteca math para usar el valor de pi

# Pedimos al usuario que ingrese el radio del círculo
radio = float(input("Ingresa el radio del círculo: "))  # Convertimos la entrada a un número decimal

# Calculamos el área usando la fórmula: pi * radio^2
area = math.pi * radio * radio  # Multiplicamos pi por el radio elevado al cuadrado

# Mostramos el resultado al usuario
print("El área del círculo es:", area)  # Imprime el área calculada
```

---

¡Y con esto, hemos completado nuestro primer capítulo sobre conceptos básicos de programación! Estos ejercicios te han enseñado cómo interactuar con la computadora, realizar cálculos simples y trabajar con variables. En el próximo capítulo, avanzaremos un poco más, explorando cómo las computadoras pueden tomar decisiones y repetir tareas automáticamente. ¡Sigue adelante y sigue aprendiendo!

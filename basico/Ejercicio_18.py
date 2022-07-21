# EJERCICIO 1

"""
    Definir una función maximo()
    que tome como argumento dos números y devuelva el mayor de ellos. 
    (Es cierto que python tiene una función max() incorporada,
    pero hacerla nosotros mismos es un muy buen ejercicio).
"""

from ast import IsNot, NotIn


def maximo():
    x = int(input('Introduce un valor para la variable x:....'))
    y = int(input('Introduce un valor para la variable y:....'))

    if x > y:
        return print(f'La variable "x" {x} es mayor que la variable "y" {y}')
    elif x < y:
        return print(f'La variable "y" {y} es mayor que la variable "x" {x}')
    else:
        return 'La variable "x" {x} es mayor que la variable "y" {y}'

#maximo()

# EJERCICIO 2

"""
    Definir una función max_de_tres(), 
    que tome tres números como argumentos y 
    devuelva el mayor de ellos.
"""

def max_de_tres():
    x = int(input('Ej2. Introduce un valor para la variable x:....'))
    y = int(input('Ej2. Introduce un valor para la variable y:....'))
    z = int(input('Ej2. Introduce un valor para la variable z:....'))
    

    if ((x > y) and (x > z)) == True:
        return print(f'Ej2. La variable "x" {x} es mayor que la variable "y" {y} y que la variable "z" {z}')
    elif ((y > x) and (y > z)) == True:
        return print(f'Ej2. La variable "y" {y} es mayor que las variables "x" {x} y "z" {z}')
    else:        
        return print(f'Ej2. La variable "z" {z} es mayor que las variables "x" {x} e "y" {y}')
#max_de_tres()

# EJERCICIO 3

"""
    Definir una función que calcule la longitud de una lista 
    o una cadena dada. 
    (Es cierto que python tiene la función len() incorporada, 
    pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""

def longitud():
    palabra = input('Ej3. Introduce una palabra para conocer su longitud: ....')
    contador = 0

    for i in palabra:
            contador += 1
    
    return print(f"Ej3. La palabra tiene {contador} letras")

#longitud()

# EJERCICIO 4

"""
    Escribir una función que tome un carácter y devuelva True si es una vocal,
    de lo contrario devuelve False.
"""


def es_vocal(inp):
    if (inp) in 'AEIOUaeiou':
        return print(f'Ej4. Retorna: {True}')
    else:
        return print(f'Ej4. Retorna: {False}')

es_vocal('p')

# EJERCICIO 5

"""
    Escribir una función suma() y una función multip() que sumen y multipliquen
    respectivamente todos los números de una lista.
    Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""
def suma(lista):
    sum = 0
    for i in lista:
        sum += i
    return print(f'Ej5. La suma es {sum}')

def multip(lista):
    mul = 1
    for i in lista:
        mul *= i
    return print(f'Ej5. La multiplicación es {mul}')

suma([1,2,3,4])
multip([1,2,3,4])

print("Enhorabuena acabaste los ejercicios")
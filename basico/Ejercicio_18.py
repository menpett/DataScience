# EJERCICIO 1

"""
    Definir una función maximo()
    que tome como argumento dos números y devuelva el mayor de ellos. 
    (Es cierto que python tiene una función max() incorporada,
    pero hacerla nosotros mismos es un muy buen ejercicio).
"""

def max():
    x = int(input('Introduce un valor para la variable x:....'))
    y = int(input('Introduce un valor para la variable y:....'))

    if x > y:
        return print(f'La variable "x" {x} es mayor que la variable "y" {y}')
    else:
        return print(f'La variable "x" {x} es mayor que la variable "y" {y}')

# EJERCICIO 2

"""
    Definir una función max_de_tres(), 
    que tome tres números como argumentos y 
    devuelva el mayor de ellos.
"""

def max_de_tres():
    x = int(input('Introduce un valor para la variable x:....'))
    y = int(input('Introduce un valor para la variable y:....'))
    z = int(input('Introduce un valor para la variable z:....'))
    

    if ((x > y) and (x > z)) == True:
        return print(f'La variable "x" {x} es mayor que la variable "y" {y} y que la variable "z" {z}')
    elif ((y > x) and (y > z)) == True:
        return print(f'La variable "y" {y} es mayor que las variables "x" {x} y "z" {z}')
    else:        
        return print(f'La variable "z" {z} es mayor que las variables "x" {x} e "y" {y}')

# EJERCICIO 3

"""
    Definir una función que calcule la longitud de una lista 
    o una cadena dada. 
    (Es cierto que python tiene la función len() incorporada, 
    pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""

def longitud():
    palabra = input('Introduce una palabra para conocer su longitud: ....')
    contador = 0

    for i in palabra:
        contador += 1
    
    return print(f"La palabra tiene {contador} letras")


print("Enhorabuena acabaste los ejercicios")
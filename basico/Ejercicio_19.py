# Ejercicio 1

"""
    Definir una función inversa() que calcule la inversion de una cadena. 
    Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse".
"""

def inversa(cadena):
    cadena = str(cadena)
    print(cadena[::-1])

inversa('estoy probando')


# Ejercicio 2

"""
    Definir una funcion es_palindromo() que reconoce palindromo 
    palabras  que tiene el mismo aspecto escritas invertidas), ejemplo: es_palindromo("radar")
    tendría que devolver True.
"""

def es_palindromo(cadena):
    cadena1 = cadena[::-1]
    # print(cadena,cadena1)
    if cadena == cadena1:
        return print(f'La palabra {cadena} es palindromo')
    else:
        return print(f'La palabra {cadena} no es palindromo')

es_palindromo('radar')

# Ejercicio 3

"""
    Definir una funcion superposicion() que tome dos listas y devuelva True si tiene al
    menos  o devuelva False en caso contrario. Escribe la función usando el bucle for 
    aninado.
"""

def superposicion(lista1, lista2):
    for i in lista1:
        print(i)
        if i in lista2:
            return print(f'El carácter "{i}" es común en ambas listas')
        

    return print(f'Las listas no tienen carácteres comunes')

superposicion([98,8,6,'a','mi',10], ['lista2','mi',2,10,'mi'])
"""
    Basándote en la teoría explicada en clase sobre Python
    realiza los siguientes ejercicios
"""

# EJERCICIO 1

"""
    Definir una función generar_n_caracteres() que tome un entero n
    y devuelva el caracter multiplicado por n.
    Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""


from posixpath import split
from random import randint


def generar_n_caracteres(n, caracter):
    # tome un entero n
    # devuelva el caracter multiplicado por n
    if n == 1 :
        return caracter
    else:
        return caracter + generar_n_caracteres(n-1, caracter)

# resp1 = generar_n_caracteres(1,'caracter')
# print(f'El caracter multiplicado por n es: {resp1}')


# EJERCICIO 2

"""
    Definir un diagrama procedimiento() que tome una lista de números enteros
    e imprima un diagrama en la pantalla. Ejemplo: procedimiento([4, 9, 7])
    debería imprimir lo siguiente:
"""

def procedimiento(lista):
    # tome una lista de numeros enteros
    # imprimir en la pantalla:

    # XXXX
    # XXXXXXXXX
    # XXXXXXX
    
    for i in lista:
        num = ''
        if i == 1:
            print('X')
        elif i == 0:
            print(' ')
        else:
            while i > 0:
                num += 'X'
                i -= 1
            print(num)

# procedimiento([1, 0, 7])

# EJERCICIO 3

"""
    Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
"""

def mas_larga(lista_p):
    # tome una lista de palabras
    # devolver la más larga
    
    lista_len = []

    for i in lista_p:
        num = len(i)
        lista_len.append(num)   

    mayor = max(lista_len)
    ind = lista_len.index(max(lista_len))
    
    return mayor,ind 

lista_p = ['tome', 'una', 'lista', 'de', 'palabras']
resp3 = list(mas_larga(lista_p))
print(resp3,type(resp3))
print(f'La palabra más larga es: "{lista_p[resp3[1]]}" con "{resp3[0]}" carateres')   

# EJERCICIO 4

"""
    Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n,
    y devuelva las palabras que tengan mas de n caracteres.
"""

def filtrar_palabras(lista, n):
    # tome una lista de palabras y un entero n
    # devolver las palabras que tengan n caracteres
    pass

# EJERCICIO 5

"""
    Escribir un programa que ingrese una cadena de texto.
    El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""

def c_mayusculas(cadena):
    # TODO: ingrese una cadena de texto
    # TODO: evaluar la cadena
    # TODO: returnar cuantas letras mayúsculas tiene
    # contar = 0
    # cadena1 = cadena.upper()
    print('La cadena a contar mayusculas es: ',cadena, 'con nº caracteres, ', len(cadena))

    # for ind,value in enumerate(cadena):
    #     for ind1,value1 in enumerate(cadena1):
    #         if cadena[ind] == cadena1[ind1]:
    #             print(value, value1)
    #             contar += 1
    # return contar
    cadena1 = cadena.upper()
    contar = 0
    n = 1
    while n <= len(cadena):     
        # print(cadena[n-1],cadena1[n-1])    
        if ((cadena[n-1]==cadena1[n-1]) and (cadena[n-1] != ' ')) == True:
            contar += 1
        n += 1
    return contar


resp5 = c_mayusculas('Mayúsculas tiene')
print('La cadena tiene nº de letras mayúsculas igual a: ', resp5)


# EJERCICIO 6

"""
    Definir una tupla con 10 edades de personas.
        * Imprimir la cantidad de personas con edades superiores a 20.
"""

def mayores(tup):
    # definir una tupla de 10 edades de personas
    # imprimir la cantidad de personas con edades superiores a 20
    n = 1
    contar = 0

    while n <= len(tup):        
        if tup[n-1] > 20:
            contar += 1
        n += 1
    return contar
        
resp6 = mayores((10,95,25,45,77,65,25,35,65,37))
print('La cantidad de personas con edades superiores a 20 es:', resp6)


# EJERCICIO 7

"""
    Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
    También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
"""

def main():
    # definir cuantos nombres quieres ingresar
    # definir una lista con el numero de elementos
    # pedir los nombres que pertenecen a la lista
    # definir por que letra comienza el nombre
    # imprimir la cantidad de nombres que empiezan por la letra
    n_nombres = int(input('Cuantos nombres quieres ingresar:'))
    nombres = []

    for i in range(0,n_nombres+1):
        nombre = input('Nombres que pertenecen a la lista: ')
        nombres.append(nombre)
    
    ini = input('Definir por que letra comienza el nombre:')
    contar = 0
    for i in nombres:
        if (i.startswith(ini.upper()) == True) or (i.startswith(ini.lower())) == True:
            contar += 1
            
    return print('Cantidad de nombres que empiezan por la letra ', contar)
main()    


# EJERCICIO 8

"""
    Crear una función contar_vocales(),
    que reciba una palabra y cuente cuantas letras "a" tiene,
    cuantas letras "e" tiene y así hasta completar todas las vocales.
    Se puede hacer que el usuario sea quien elija la palabra.
"""

def contar_vocales(cadena):
    # recibir una palabra
    # contabilizar cuantas letras tiene de "a"
    # contabilizar cuantas letras tiene de "e"
    # contabilizar cuantas letras tiene de "i"
    # contabilizar cuantas letras tiene de "o"
    # contabilizar cuantas letras tiene de "u"
    contarA = 0
    contarE = 0
    contarI = 0
    contarO = 0
    contarU = 0
    for i in cadena:
        if (i == 'A') or (i == 'a'):
            contarA += 1
        elif (i == 'E') or (i == 'e'):
            contarE += 1
        elif (i == 'I') or (i == 'i'):
            contarI += 1
        elif (i == 'O') or (i == 'o'):
            contarO += 1
        elif (i == 'U') or (i == 'u'):
            contarU += 1
    return contarA, contarE, contarI, contarO, contarU

resp6 = contar_vocales('Se puede hacer que el usuario sea quien elija la palabra')
print('Contabilizar cuantas letras "a":', resp6[0])
print('Contabilizar cuantas letras "e":', resp6[1])
print('Contabilizar cuantas letras "i":', resp6[2])
print('Contabilizar cuantas letras "o":', resp6[3])
print('Contabilizar cuantas letras "u":', resp6[4])


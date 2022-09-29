
""" 
Ejemplo 1
La altura promedio de un jugador de baloncesto profesional fue de 2,00 metros con una desviación estándar de0,02 metros. Harrison Barnes es un jugador de baloncesto que mide 2,03 metros. ¿Cuántas desviaciones estándar de la media es la altura de Barnes?
"""
mu1 = 2
s1 = 0.02
x1 = 2.03

def Zscore(mu,s,x):
    return round(((x-mu)/s),2)

Zscore_harry = Zscore(mu1,s1,x1)

print(f'La altura de Harrison Barnes está a {Zscore_harry} desviaciones estándar de la media')

""" 
Ejemplo 2
La altura promedio de un jugador de hockey profesional es de 1,86 metros con una desviación estándar de 0,06 metros. Tyler Myers, un profesional de hockey, tiene la misma altura que Harrison Barnes. ¿Cuál de los dos es más alto en su respectiva liga?
"""
mu2 = 1.86
s2 = 0.06
x2 = 2.03

Zscore_Tyler = Zscore(mu2,s2,x2)

print(f'La altura de Tyler Myers está a {Zscore_Tyler} desviaciones estándar de la media')

if Zscore_Tyler > Zscore_harry:
    print('Hay más jugadores de hockey más bajos que Myers que jugadores de baloncesto más bajos que Barnes')
else:
    print('Hay más jugadores de baloncesto más bajos que Barnes que jugadores de hockey más bajos que Myers')

""" 
Ejercicios:
"""  
""" 1) Calcula la Z score para los siguientes casos:
a) μ = 54, s = 12, x = 68
b) μ = 25, s = 3.5, x = 20
c) μ = 0.01, s = 0.002, x = 0.01  """

a = Zscore(54,12,68)
print('El Zscore_a es:', a)
b = Zscore(25,3.5,20)
print('El Zscore_a es:', b)
c = Zscore(0.01,0.002,0.01)
print('El Zscore_a es:', c)

""" 2) El GPA promedio de los estudiantes en una escuela secundaria local es 3.2 con una desviación estándar de 0.3. Jenny tiene un GPA de 2.8. ¿A cuántas desviaciones estándar de la media está el GPA de Jenny? """

Zscore_jenny = Zscore(3.2,0.3,2.8)
print(f'Jenny está a {Zscore_jenny} desviaciones estándar de la media')

""" 3) Jenny está tratando de demostrarles a sus padres que le va mejor en la escuela que a su prima. Su prima asiste a una escuela secundaria diferente donde el GPA promedio es 3.4 con una desviación estándar de 0.2.El primo de Jenny tiene un GPA de 3.0. ¿Se está desempeñando Jenny mejor que su prima según los puntajesestándar? """

Zscore_primo = Zscore(3.4,0.2,3)
print(f'El primo está a {Zscore_primo} desviaciones estándar de la media')

if Zscore_jenny > Zscore_primo:
    print('Como el Zscore de jenny es mayor que el de su primo, por encima de la media, jenny se está desempeñando mejor')
else:
    print('Como el Zscore de jenny es menor que el de su primo, , jenny se está desempeñando peor')

""" 4) La puntuación de Kyle en una prueba de matemáticas reciente fue de 2.3 desviaciones estándar por encima de la puntuación media del 78%. Si la desviación estándar de los puntajes de la prueba fue del 8%, ¿qué puntaje obtuvo Kyle en su prueba? """

Zscore_kyle = 2.3
mu3 = 0.78
s = 0.08
X_kyle = (Zscore_kyle*s) + mu3
print(f'La puntuación de Kyle es de {X_kyle}')

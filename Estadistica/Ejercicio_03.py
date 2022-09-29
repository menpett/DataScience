# EJERCICIO 1

"""En 2007-2008, la altura promedio de un jugador de baloncesto profesional fue de 2,00 metros con una desviación estándar de 0,02 metros. 
    Harrison Barnes es un jugador de baloncesto que mide 2,03 metros. ¿Qué porcentaje de jugadores son más altos que Barnes?"""
def Zscore(mu,s,x):
    return round(((x-mu)/s),2)

Zscore_barnes = Zscore(2,0.02,2.03)

prob_barnes = 0.9332*100

print(f'El Zscore de Barnes es {Zscore_barnes} cuyo porcentaje de jugadores mas altos que Harrison Barnes es {round(100-prob_barnes,2)}')

# EJERCICIO 2

"""Chris Paul mide 1,83 metros. ¿Qué proporción de jugadores de baloncesto se encuentran entre las alturas de Paul y Barnes? """

Zscore_chris = Zscore(2,0.02,1.83)

print(f'Para el Zscore de Chris de {Zscore_chris}, La proporción de jugadores de baloncesto se encuentran entre las alturas de Paul y Barnes es de {round(prob_barnes,2)}')

# EJERCICIO 3

"""El 92 % de los candidatos obtuvo una puntuación tan buena o peor que la de Steve. Si la puntuación promedio fue 55 con una desviación estándar de 6 puntos, ¿cuál fue el puntuación de Steve?"""
Zscore_steve = 1.40 # Según tabla 
X_steve = 55 + (6*Zscore_steve)

print(f'La puntuación de Steve es de {X_steve}')
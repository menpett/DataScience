# EJERCICIO 1

"""
    Crearemos una clase llamada NumeroComplejo.
    Este tipo tiene un atributo x para la coordenada en x e y para la coordenada en y.
    Representa un número complejo de la forma (x, y).
"""
class NumeroComplejo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

# EJERCICIO 2

"""
    Ahora defina dentro de la clase NumeroComplejo un función imprimir
    donde muestre los valores de x e y.
"""
class NumeroComplejo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def imprimir(self):
        print(f'El valor real es: {self.x}')
        print('\n')
        print(f'El valor imaginario es: {self.y}')

# EJERCICIO 3

"""
    Define la función str para la clase NumeroComplejo
    para poder imprimir usando la función print.
"""
class NumeroComplejo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '('+ str(self.x) + ', ' + str(self.y) + ')'
    def imprimir(self):
        print(f'El valor real es: {self.x}')
        print('\n')
        print(f'El valor imaginario es: {self.y}')

# EJERCICIO 4

"""
    Define una función que compara dos números complejos,
    ya que si dos objetos distintos tienen sus atributos iguales,y
    sino NO se consideran iguales.
"""
class NumeroComplejo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '('+ str(self.x) + ', ' + str(self.y) + ')'
    def imprimir(self):
        print(f'El valor real es: {self.x}')
        print('\n')
        print(f'El valor imaginario es: {self.y}')
    def compara(self,other):
        if (self.x == self.other) and (self.y == self.other):
            return 'Los dos objetos son iguales'
        else:
            return 'Los dos objetos NO son iguales'
    



# EJERCICIO 5

"""
    Realiza un método que sume dos numeros complejos sin modificiar los objetos originales,
    ya que se retorna un nuevo numero NumeroComplejo.
"""
class NumeroComplejo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '('+ str(self.x) + ', ' + str(self.y) + ')'
    def imprimir(self):
        print(f'El valor real es: {self.x}')
        print('\n')
        print(f'El valor imaginario es: {self.y}')
    def compara(self,other):
        if (self.x == other.x) and (self.y == other.y):
            return 'Los dos objetos son iguales'
        else:
            return 'Los dos objetos NO son iguales'
    def suma(self,other):
        suma_r = self.x + other.x
        suma_i = self.x + other.y

        return f'El nuevo numero complejo es ({str(suma_r)},{str(suma_i)})'



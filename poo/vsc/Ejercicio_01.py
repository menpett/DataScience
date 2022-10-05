# EJERCICIO 1
"""
    1) Crea el siguiente programa:

    Una clase de nombre Librería
    Inicia los siguientes atributos: nombre, sección, editorial y año
    Crea una segunda clase con nombre Rosalia que herede la clase librería.
    En esta clase Rosalia, crea una función "result" cuyo resultado sea los datos de los libros.
    declara los Objetos siguientes:
    libro1 --> Oceanarium, Ciencia, Impedimenta, 2021
    libro2 --> 33 Botones, Novela negra, Atlantis, 2022
    libro3 --> Venganza en Compostela, Historia, Universo de letras, 2022
"""
class Libreria:
    def __init__(self, nombre, seccion, editorial, ano):
        self.nombre = nombre
        self.seccion = seccion
        self.editorial = editorial
        self.ano = ano
    class Rosalia(Libreria):
        def result(self):   
            return f'Nombre: {self.nombre } \n Sección: {self.seccion} \n Editorial: {self.editorial} \n Año: {self.ano}'
libro1 = Libreria('Oceanarium', 'Ciencia', 'Impedimenta', 2021)
libro2 = Libreria('33 Botones', 'Novela negra', 'Atlantis', 2022)
libro3 = Libreria('Venganza en Compostela', 'Historia', 'Universo de letras', 2022)

# EJERCICIO 2
"""
    2) Crea otra libraría de nombre MiLibro, que corresponde a una nueva clase,
    define una función de nombre misLibros, cuyo resultado sea los datos de los libros:

    libro4 --> Mi primera Novela, Novela, Bruño, 2019
    libro5 --> Gatos, Literatura, Listado, 2018
"""
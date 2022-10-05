# EJERCICIO 1

"""
    Crea una clase persona. Sus atributos deben ser su nombre y su edad.
    Además crea un método cumpleaños, que aumente en 1 la edad de la persona.
"""

# EJERCICIO 2

"""
    Para la clase anterior definir el método str.
    Debe retornar al menos el nombre de la persona.
"""

# EJERCICIO 3

"""
    Extender la clase persona agregando un atributo saldo y un método transferencia(self, persona2, monto).
    El saldo representa el dinero que tiene la persona.
    El método transferencia hace que la Persona que llama el método le transfiera la cantidad monto al objeto persona2.
    Si no tiene el dinero suficiente no se ejecuta la acción.
"""

# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def cumpleanos(self):
#         return self.edad + 1

#     def __str__(self):
#         return 'Nombre:' + str(self.nombre)

class Persona:
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo

    def cumpleanos(self):
        return self.edad + 1

    def __str__(self):
        return ' ' + '\n' + 'Nombre:' + str(self.nombre) + '\n' + 'Edad:' + str(self.edad) + '\n' + 'Saldo:' + str(self.saldo) + '\n' + ' '
    
    def transferencia(self, persona2, monto):

        if self.saldo >= monto:
            self.saldo = self.saldo - monto
            persona2.saldo = persona2.saldo + monto
            print(f'Se realiza la transferencia con exito')
            print(f'{self.nombre} tiene un saldo actual de {self.saldo}')
            print(f'{persona2.nombre} tiene un saldo actual de {persona2.saldo}')
            return 'Finalizada la operación'
        return 'Saldo insuficiente'

persona1 = Persona('Pedro',22,22000)
persona2 = Persona('Juan',54,45000)
persona3 = Persona('Luis',41,14000)

print(persona1)
print(persona2)
print(persona3)

persona3.cumpleanos()
print(persona3)

persona3.transferencia(persona1,7000)
print(persona1)
print(persona3)

persona3.transferencia(persona2,100000)
print(persona3)
print(persona2)
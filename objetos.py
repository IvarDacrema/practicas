from token import EQUAL


print("hola mundo")

class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def cambiar_nombre(self):
        nombre = input("Ingrese su nombre:")
        self.nombre = nombre
    def ingresar_dni(self):
        dni = input("ingrese su dni")
        self.dni = dni
    def imprimir(self):
        print(f"Buenas soy {self.nombre} y mi dni es {self.dni}")

yo = Persona("maxi", 34785653)

yo.imprimir()

a = yo

a.imprimir()

b = a

b.imprimir()

print(id(a) == id(b))
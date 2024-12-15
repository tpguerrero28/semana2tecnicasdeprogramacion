# Clase base
class Animal:

    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("El animal hace un sonido.")

# Clase derivada
class Perro(Animal):

    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    # Sobrescribir el método de la clase base
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")

# Crear un objeto de la clase Perro
mi_perro = Perro("lana", "Labrador")
mi_perro.hacer_sonido()
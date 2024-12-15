# Clase base Animal
class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

# Clase derivada Perro
class LOBO(Animal):
    def hacer_sonido(self):
        print("El LOBO dice: ¡Auú, auú!")

# Clase derivada Gato
class CERDO(Animal):
    def hacer_sonido(self):
        print("El CERDO dice: ¡OING!")

# Clase derivada Vaca
class Vaca(Animal):
    def hacer_sonido(self):
        print("La vaca dice: ¡Muu!")

# Función que usa polimorfismo
def hacer_sonido_del_animal(animal: Animal):
    animal.hacer_sonido()

# Crear objetos de las clases
perro = LOBO()
gato = CERDO()
vaca = Vaca()

# Llamamos a la función para hacer los sonidos
hacer_sonido_del_animal(perro)  # El perro dice: ¡Guau!
hacer_sonido_del_animal(gato)   # El gato dice: ¡Miau!
hacer_sonido_del_animal(vaca)   # La vaca dice: ¡Muu!
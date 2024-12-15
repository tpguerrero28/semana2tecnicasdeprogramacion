from abc import ABC, abstractmethod
#clase abstracta

class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


    def moverse(self):
        pass


class Coche(Vehiculo):
    def moverse(self):
        print(f"El coche {self.marca} {self.modelo} está conduciendo por la carretera.")


class Bicicleta(Vehiculo):
    def moverse(self):
        print(f"La bicicleta {self.marca} {self.modelo} está pedaleando en la montaña de Ecuador.")


# Crear instancias de las clases
coche = Coche("Renault", "sandero")
bicicleta = Bicicleta("Trek bike", "Mountain")

coche.moverse()
bicicleta.moverse()
class CuentaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def obtener_saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("Cantidad a depositar no válida.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Saldo insuficiente o cantidad no válida.")

# Crear una cuenta bancaria
cuenta = CuentaBancaria("MAGNO MUÑOZ", 2800)
print("Saldo inicial:", cuenta.obtener_saldo())

# Depositar dinero
cuenta.depositar(850)
print("Saldo después del depósito:", cuenta.obtener_saldo())

# Retirar dinero
cuenta.retirar(500)
print("Saldo después del retiro:", cuenta.obtener_saldo())
from movimiento import Movimiento

class Cuenta:
    def __init__(self, numero, titular, saldo):
        self.__numero = numero
        self.__titular = titular
        self.__movimientos = []
        self.__saldo = saldo

    def set_movimientos(self, movimiento):
        self.__movimiento = Movimiento(movimiento)
        self.__movimientos.append([self.__movimiento.concepto, self.__movimiento.cantidad])
        __set_saldo(self.__movimento.cantidad)

    def movimientos(self):
        return self.__movimientos

    def __set_saldo(self, cantidad):
        self.__saldo += cantidad

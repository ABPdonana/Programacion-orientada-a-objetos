from movimiento import Movimiento

class Cuenta:
    def __init__(self, numero, titular, saldo):
        self.__numero = numero
        self.__titular = titular
        self.__movimientos = []
        self.__saldo = saldo

    def anyadir_movimientos(self, movimiento):
        self.__movimientos.append(Movimiento(movimiento))
        self.__set_saldo(self.movimiento.cantidad())

    def movimientos(self):
        return self.__movimientos

    def __set_saldo(self, cantidad):
        self.__saldo += cantidad

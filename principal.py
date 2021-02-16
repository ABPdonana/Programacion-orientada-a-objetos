from cliente import Cliente
from movimiento import Movimiento
from cuenta import Cuenta

cliente1 = Cliente("12345678A", "Antonio", "Martinez")
cuenta1 = Cuenta(cliente1, 100)
cuenta2 = Cuenta(cliente1, 1000)
cuenta1.anyadir_movimientos()

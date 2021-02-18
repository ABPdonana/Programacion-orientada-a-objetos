from cliente import Cliente
from movimiento import Movimiento
from cuenta import Cuenta

cliente1 = Cliente("12345678A", "Antonio", "Martinez")
cuenta1 = Cuenta(cliente1, 100)
cuenta2 = Cuenta(cliente1, 1000)
cuenta1.anyadir_movimientos(Movimiento("Compras", -50))
cuenta1.anyadir_movimientos(Movimiento("Transferencia", 100))
cuenta1.anyadir_movimientos(Movimiento("Compras", -65))
cuenta2.anyadir_movimientos(Movimiento("Nomina", 1200))
cuenta2.anyadir_movimientos(Movimiento("Paga extra", 1200))
cuenta2.anyadir_movimientos(Movimiento("Hipoteca", -500))
print(cuenta1.saldo)
print(cuenta2.saldo)

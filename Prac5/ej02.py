class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

    def ingresar(self,importe):
        self.saldo += importe

    def reintegrar(self,importe):
        self.saldo -= importe

    def consultar_saldo(self):
        return self.saldo

saldo = float(input('Introduce cuántos euros quieres como saldo inicial de tu cuenta: '))
cuenta = Cuenta(saldo)

opcion = int(input('\n1. Hacer un ingreso\n2. Pedir un reintegro\n3. Consultar el saldo\n4. Salir\nElige una opción: '))
while opcion != 4:
    if opcion == 1:
        ingreso = float(input('Introduce cuántos euros quieres ingresar: '))
        cuenta.ingresar(ingreso)
    if opcion == 2:
        reintegro = float(input('Introduce cuántos euros quieres que se te reintegren: '))
        cuenta.reintegrar(reintegro)
    if opcion == 3:
        print('El saldo actual es {0:.2f} euros'.format(cuenta.consultar_saldo()))

    opcion = int(input('\n1. Hacer un ingreso\n2. Pedir un reintegro\n3. Consultar el saldo\n4. Salir\nElige una opción: '))
print('¡Adiós!')
class Coche:
    def __init__(self):
        self.tiempo = 0
        self.distancia = 0
        self.velocidad = 0

    def acelerar(self,aumento):
        self.velocidad += aumento

    def decelerar(self,decremento):
        self.velocidad -= decremento

    def actualizar(self,tiempo):
        self.tiempo += tiempo
        self.distancia += self.velocidad*tiempo

    def consultar_tiempo(self):
        return self.tiempo

    def consultar_distancia(self):
        return self.distancia

    def consultar_velocidad_actual(self):
        return self.velocidad

    def consultar_velocidad_media(self):
        if self.tiempo != 0:
            return self.distancia / self.tiempo



print('Tu coche está inicialmente parado')
coche = Coche()
opcion = int(input('\n1. Acelerar\n2. Decelerar\n3. Actualizar\n4. Consultar\n5. Salir\nElige una opción: '))
while opcion != 5:
    if opcion == 1:
        cantidad = float(input('Introduce cuántos km/h quieres acelerar: '))
        coche.acelerar(cantidad)
    elif opcion == 2:
        decremento = float(input('Introduce cuántos km/h quieres decelerar: '))
        coche.decelerar(decremento)
    elif opcion == 3:
        tiempo = float(input('Introduce cuántas horas han pasado: '))
        coche.actualizar(tiempo)
    elif opcion == 4:
        print("El tiempo trascurrido es {0:.2f} h".format(coche.consultar_tiempo()))
        print("La distancia recorrida es  {0:.2f} km".format(coche.consultar_distancia()))
        print("La velocidad actual es {0:.2f} km/h".format(coche.consultar_velocidad_actual()))
        velocidad_media = coche.consultar_velocidad_media()
        if velocidad_media != None:
            print("La velocidad media es {0:.2f} km/h".format(coche.consultar_velocidad_media()))
        else:
            print('no puedo calcular la velocidad media si no ha trascurrido tiempo')

    opcion = int(input('\n1. Acelerar\n2. Decelerar\n3. Actualizar\n4. Consultar\n5. Salir\nElige una opción: '))

print('¡Adiós!')
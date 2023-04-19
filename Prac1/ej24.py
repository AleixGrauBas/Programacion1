#Importamos pi y seno del bloque math

from math import pi

from math import sin

#Pedida de datos

lado1 = float(input('Introduce el primer lado: '))

lado2 = float(input('Introduce el segundo lado: '))

angulo = float(input('Introduce el ángulo (en grados): '))

#Pasamos los grados a radianes

angulo = angulo * pi / 180

#Calculamos el area y la mostramos

print('El área del triángulo es: {0:.2f}'.format(lado1*lado2/2*sin(angulo)))
#Importamos la función sqrt del bloque math

from math import sqrt

#Pedida de datos

numeroA = int(input('Introduce a: '))

numeroB = int(input('Introduce b: '))

numeroC = int(input('Introduce c: '))

#Calculamos x1 y x2

x1 = (-numeroB + sqrt(numeroB**2 - 4*numeroA*numeroC)) / (2*numeroA)

x2 = (-numeroB -sqrt(numeroB**2 - 4*numeroA*numeroC)) / (2*numeroA)

#Mostramos los resultados

print('x1 = {0}'.format(x1))

print('x2 = {0}'.format(x2))

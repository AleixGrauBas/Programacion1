#Importamos pi del bloque math

from math import pi

#Pedida de datos

radio = float(input('Introduce el radio: '))

#Calculamos el area del circulo mediante la funcion y la mostramos

def área_círculo(radio):

    return pi * radio ** 2

print('Área: {0:.2f}'.format(área_círculo(radio)))

print('Longitud: {0:.2f}'.format(2*pi*radio))
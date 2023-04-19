#Autor: Aleix Grau Bas
#Pedida de datos
radio = float(input('Introduce el radio: '))
#Función que calcula el área
def área_círculo(radio):
    from math import pi
    area = radio**2 * pi
    return area
#Función que calcula la longitud de una circumferencia
def longitud_circunferencia(radio):
    from math import pi
    longitud = 2*pi*radio
    return longitud

#mostrar resultados

print('Área: {0:.2f}'.format(área_círculo(radio)))
print('Longitud: {0:.2f}'.format(longitud_circunferencia(radio)))
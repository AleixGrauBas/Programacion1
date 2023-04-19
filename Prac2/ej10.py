#Autor = Aleix Grau Bas
# #pedida de datos
a = int(input('Introduce el primer número: '))

b = int(input('Introduce el segundo número: '))

#El producto es positivo, negativo o nulo
if a*b > 0:
    print('Su producto es positivo')
if a*b <0:
    print('Su producto es negativo')
if a*b == 0:
    print('Su producto es nulo')
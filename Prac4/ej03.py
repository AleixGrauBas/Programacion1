#Autor: Aleix Grau Bas
#Creamos las cadenas vacías
lista_pares = []
lista_impares = []

print('Ve introduciendo números enteros positivos, o un número negativo para acabar...')#Inicio del programa

número = int(input('Nuevo número: ')) #Primera pedida de dato

while número >= 0:#Mientras el número introducido sea positivo seguimos clasificándolos en pares e impares
    if número % 2 == 0:
        lista_pares.append(número)
    else:
        lista_impares.append(número)
    número = int(input('Nuevo número: '))

print('Números pares: {0}'.format(lista_pares))
print('Números impares: {0}'.format(lista_impares))
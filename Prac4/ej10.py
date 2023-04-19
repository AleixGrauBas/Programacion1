#Autor:Aleix Grau Bas
def leer_lista_enteros():
    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')  # Inicio del programa
    lista = []
    número = input('Nuevo número: ')
    while número != '':
        lista.append(int(número))
        número = input('Nuevo número: ')
    return lista

def posición_menor(lista):#Función que devuelve la posición del número más pequeño de una lista
    pos_mínimo = 0
    min = lista[pos_mínimo]
    for i in range(len(lista)):
        if lista[i] < min:
            pos_mínimo = i
            min = lista[i]
    return pos_mínimo

def intercambiar(lista,i,j):#Función que intercambia los valores de dos posiciones
    if i !=j:
        aux = lista[j]
        lista[j] = lista[i]
        lista[i] = aux


lista = leer_lista_enteros()

if len(lista) > 0:
    print('Lista leída: {0}'.format(lista))
    intercambiar(lista, 0, posición_menor(lista))
    print('Modificada: {0}'.format(lista))

else:
    print('Lista leída: []')
    print('Modificada: []')
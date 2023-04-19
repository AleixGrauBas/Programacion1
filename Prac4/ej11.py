#Autor: Aleix Grau Bas
def leer_lista_enteros():
    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')  # Inicio del programa
    lista = []
    número = input('Nuevo número: ')
    while número != '':
        lista.append(int(número))
        número = input('Nuevo número: ')
    return lista

def posición_menor(lista,desde):#Función que devuelve la posición del número más pequeño de una lista
    pos_mínimo = desde #Posición desde la que empieza a comparar
    min = lista[pos_mínimo]
    for i in range(pos_mínimo,len(lista)):
        if lista[i] < min:
            pos_mínimo = i
            min = lista[i]
    return pos_mínimo

def intercambiar(lista,i,j):#Función que intercambia los valores de dos posiciones
    if i !=j:
        aux = lista[j]
        lista[j] = lista[i]
        lista[i] = aux

def ordenar_lista(lista): #Ordena la lista de menor a mayor
    for posición in range(len(lista)):
        intercambiar(lista,posición,posición_menor(lista,posición))


lista = leer_lista_enteros()

print('Lista leída: {0}'.format(lista))
ordenar_lista(lista)
print('Lista ordenada: {0}'.format(lista))
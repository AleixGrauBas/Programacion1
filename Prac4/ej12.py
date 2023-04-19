#Autor: Aleix Grau Bas
def leer_lista_enteros():
    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')  # Inicio del programa
    lista = []
    número = input('Nuevo número: ')
    while número != '':
        lista.append(int(número))
        número = input('Nuevo número: ')
    return lista

def repetidos_lista(lista):
    repetidos = []
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i!= j and lista[i] == lista[j]: #Lista[i] está repetido
                if lista[i] not in repetidos:#Solo apuntamos una vez aunque aparezca más
                    repetidos.append(lista[i])
    return repetidos

def suma_lista(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma

lista = leer_lista_enteros()
print('Números leídos más de una vez (suman {0}): {1}'.format(suma_lista(repetidos_lista(lista)),repetidos_lista(lista)))
print('Todos los números leídos: {0}'.format(lista))
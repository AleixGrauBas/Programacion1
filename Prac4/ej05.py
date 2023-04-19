def leer_lista_enteros():
    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')  # Inicio del programa
    lista = []
    número = input('Nuevo número: ')
    while número != '':
        lista.append(int(número))
        número = input('Nuevo número: ')
    return lista

def borrar_elemento(lista,posición): #Función que borra de la lista un número en dicha posición
    pos_valida = False
    if posición >= 0 and posición < len(lista):
        del lista[posición]
        pos_valida = True
    return pos_valida

lista = leer_lista_enteros()

while len(lista) > 0:
    posición = int(input('¿Qué posición debo eliminar de {0}? '.format(lista)))
    if not borrar_elemento(lista,posición):
        print('Posición incorrecta')

print('La lista ha quedado vacía')
#Autor:Aleix Grau Bas
def leer_lista_enteros():
    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')  # Inicio del programa
    lista = []
    número = input('Nuevo número: ')
    while número != '':
        lista.append(int(número))
        número = input('Nuevo número: ')
    return lista

def borrar_elemento(lista,valor): #Función que borra de la lista el último número indicado
    for i in range(len(lista)-1,-1,-1,):#Buscamos si esta el número
        if lista[i] == valor:
            del lista[i]
            return True
    return False

lista = leer_lista_enteros()

while len(lista) > 0:#Se borran elementos hasta que la lista quede vacía
    número = int(input('¿Qué número debo eliminar de {0}? '.format(lista)))
    if not borrar_elemento(lista,número):#Si el número no se encuentra en la lista
        print('Número no encontrado')

print('La lista ha quedado vacía')
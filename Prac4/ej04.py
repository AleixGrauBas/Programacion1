#Autor: Aleix Grau Bas
#Función para leer_lista_enteros
def leer_lista_enteros():
    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')  # Inicio del programa
    lista = []
    número = input('Nuevo número: ')
    while número != '':
        lista.append(int(número))
        número = input('Nuevo número: ')
    return lista

lista = leer_lista_enteros()#almacenamos la lista que nos devuelve la función en lista
lista_cuadrados = lista*1
for i in range(len(lista)):
    lista_cuadrados[i] = lista[i]**2

print('Cuadrados de los números leídos: {0}'.format(lista_cuadrados))
print('Números leídos: {0}'.format(lista))
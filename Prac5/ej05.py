fichero = open('hola.txt','r',)

lista = fichero.readline().split('#')
print(lista)
lista = fichero.readline()
print(lista)
#Autor: Aleix Grau Bas
#función que muestra una cadena repetida n veces con un separador
def mostrar_cadena_repetida(c,n,s):
    cadena = (c+s)*(n-1) +c
    print(cadena)
#Pedida de datos
c = str(input('Introduce una cadena: '))
s = str(input('Introduce un separador: '))
n = int(input('Introduce un máximo de repeticiones: '))

for i in range(1,n+1):
    mostrar_cadena_repetida(c,i,s)
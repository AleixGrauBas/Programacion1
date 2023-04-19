#Autor: Aleix Grau Bas
#función que calcula una cadena repetida n veces con un separador
def calcular_cadena_repetida(c,n,s):
    cadena = (c + s) * (n - 1) + c
    return cadena

c = str(input('Introduce una cadena: '))
s = str(input('Introduce un separador: '))
n = int(input('Introduce un máximo de repeticiones: '))

for i in range(1,n+1):
    print(calcular_cadena_repetida(c,i,s))

#Autor: Aleix Grau Bas
#Función
def contar_divisores(n):
    candidato = 1
    divisores = 1
    while candidato < n:
        if n % candidato == 0:
            divisores += 1
            candidato += 1
        else:
            candidato += 1
    return divisores

n = int(input('Introduce un número entero: '))
max = 0
num = 1
num_max = 0
while num <= n: #Calculamos los divisores de los números hasta n y nos quedamos con el que más divisores tiene
    if contar_divisores(num) >= max:
        max = contar_divisores(num)
        num_max = num
    num += 1

print('El número con más divisores es {0} ({1} divisores)'.format(num_max,max))
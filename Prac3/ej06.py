#Autor: Aleix Grau Bas
# #Función que cuenta los divisores de un número
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
print('El número {0} tiene {1} divisores'.format(n,contar_divisores(n)))
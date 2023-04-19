#Pedida de datos

n = int(input('Introduce un número entero: '))

#Calculamos la cantidad de divisores que tiene n

candidato = 1
divisores = 1
while candidato < n:
    if n % candidato == 0:
        divisores += 1
        candidato += 1
    else:
        candidato += 1

print('El número {0} tiene {1} divisores'.format(n,divisores))
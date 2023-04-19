#Pedida de datos

n = int(input('Introduce un número entero: '))

#Calculamos la suma  de los números comprendidos entre 1 y n que no sean múltiplos de 3 ni de 5

candidato = 1
if n == 1:
    suma = 1
else:
    suma = 0

while candidato <n:
    if candidato % 3 == 0 or candidato % 5 == 0:
        candidato += 1
    else:
        suma += candidato
        candidato += 1

print('La suma es {0}'.format(suma))
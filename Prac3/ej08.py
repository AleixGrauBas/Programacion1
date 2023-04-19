#Autor: Aleix Grau Bas
#Funcion
def sumar_divisores_propios(n):
    candidato = 1
    sum_divisores = 0
    while candidato < n:
        if n % candidato == 0:
            sum_divisores += candidato
            candidato += 1
        else:
            candidato += 1
    return sum_divisores

#Función que calcula si en número es abundante o no
def es_abundante(n):
    return sumar_divisores_propios(n) > n

n  = int(input('Introduce un número entero: '))
print('Los números abundantes menores que {0} son: '.format(n),end=" ")
for i in range (1, n ):
    if es_abundante(i):
        print('{0}'.format(i),end= " ")

#Autor: Aleix Grau Bas
#Funciones
def es_primo(n):
    return  contar_divisores(n) == 2

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

candidato_primos = 0
n1 = int(input('Introduce un entero estrictamente positivo: '))
n2 = int(input('Introduce un entero mayor que {0}: '.format(n1)))
print('Voy a buscar primos entre {0} y {1}...'.format(n1,n2))
print('Encontrados: ',end=" ")
for i in range(n1,n2+1):
    if es_primo(i):
        print(i,end=" ")
        candidato_primos +=1

if candidato_primos == 0:
    print('ninguno',end="")
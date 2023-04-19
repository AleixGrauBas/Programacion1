1#Autor = Aleix Grau Bas
# #Pedida de datos

n = int(input('Introduce un número entero: '))

candidato = 1
#Mostramos los números pares hasta n

while candidato <= n:

    if candidato % 2 == 0:
        print(candidato)

    candidato +=1
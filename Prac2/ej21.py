#Autor = Aleix Grau Bas
# #Pedida de datos

n = int(input('Introduce un número entero: '))

#Calculamos el cuadrado de los número menores de n

cuadrado = 1
candidato = 1

while cuadrado < n:

    print('El cuadrado de {0} es {1}'.format(candidato,cuadrado))
    candidato +=1
    cuadrado = candidato * candidato
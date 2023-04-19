#Autor = Aleix Grau Bas
# #Pedida de datos y aignación de mayor
n1 = int(input('Introduce el primer número: '))
menor = n1

n2 = int(input('Introduce el segundo número: '))
if n2 < n1:
    menor = n2

print('El menor es: {0}'.format(menor))
#Autor = Aleix Grau Bas
# #Pedida de datos y aignación de mayor
n1 = int(input('Introduce el primer número: '))
menor = n1

n2 = int(input('Introduce el segundo número: '))
if n2 < menor:
    menor = n2

n3 = int(input('Introduce el tercer número: '))
if n3 < menor:
    menor = n3

n4 = int(input('Introduce el cuarto número: '))
if n4 < menor:
    menor = n4

print('El menor es: {0}'.format(menor))
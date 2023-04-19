#Autor = Aleix Grau Bas
#Pedida de datos
a = int(input('Introduce el lado a: '))

b = int(input('Introduce el lado b: '))

c = int(input('Introduce el lado c: '))

#Comprobar si es equilátero
if a == b and b==c:
    print('Es equilátero')
else:
    print('No es equilátero')
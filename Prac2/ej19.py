#Autor = Aleix Grau Bas
# #Pedida de datos
a = int(input('Introduce el lado a: '))

b = int(input('Introduce el lado b: '))

c = int(input('Introduce el lado c: '))

#Comprobamos si es un triangulo

while a + b <= c or a+c <= b or c + b <= a:
    print('No es un triángulo')
    a = int(input('Introduce el lado a: '))
    b = int(input('Introduce el lado b: '))
    c = int(input('Introduce el lado c: '))

if a == b and b==c:
    print('Es equilátero')

elif (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
    print('Es isósceles')

elif a != b and b != c and a != c:
    print('Es escaleno')
#Pedida de valores

a = int(input('Introduce el número a: '))

b = int(input('Introduce el número b: '))

c = int(input('Introduce el número c: '))

#Comprobar si es triangulo

if a + b > c and a+c > b and c + b > a:
    print('Es un triángulo')
else:
    print('No es un triángulo')
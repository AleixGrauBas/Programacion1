#Definicion de funciones
#Autor: Aleix Grau Bas
def es_triángulo(a,b,c):
    if a + b > c and a + c > b and c + b > a:
        return True
    else:
        return False

#Pedida de datos
a = int(input('Introduce el número a: '))

b = int(input('Introduce el número b: '))

c = int(input('Introduce el número c: '))

if es_triángulo(a,b,c):#Comprobamos si es triángulo
    print('Es un triángulo')

else:
    print('No es un triángulo')
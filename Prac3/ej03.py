#Autor: Aleix Grau Bas
#Funciones
#Función que dice si es triángulo
def es_triángulo(a,b,c):
    if a + b > c and a + c > b and c + b > a:
        return True
    else:
        return False

#Función que dice que tipo de triángulo es
def tipo_triángulo(a,b,c):
    if es_triángulo(a,b,c):
        if a == b and b == c:
            return 'equilátero'
        elif a != b and b != c and a != c:
            return 'escaleno'
        elif a == b or b == c or a == c:
            if a == b and b == c:
                print('No es isósceles')
            else:
                return 'isósceles'

    else:
        return None

#Pedida de datos

a = int(input('Introduce el lado a: '))
b = int(input('Introduce el lado b: '))
c = int(input('Introduce el lado c: '))

while tipo_triángulo(a,b,c) == None: #Mientras no sea un triángulo seguimos pidiendo datos
    print('No es un triángulo')
    a = int(input('Introduce el lado a: '))
    b = int(input('Introduce el lado b: '))
    c = int(input('Introduce el lado c: '))

print('Es {0}'.format(tipo_triángulo(a,b,c)))
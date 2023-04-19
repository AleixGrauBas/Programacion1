#Pedida de datos
a = int(input('Introduce el lado a: '))

b = int(input('Introduce el lado b: '))

c = int(input('Introduce el lado c: '))

#Comprobar si es escaleno
if a != b and b != c and a != c:
    print('Es escaleno')
else:
    print('No es escaleno')
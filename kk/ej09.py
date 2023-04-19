#Pedida de datos
a = int(input('Introduce el lado a: '))

b = int(input('Introduce el lado b: '))

c = int(input('Introduce el lado c: '))

#Comprobar si es rectángulo
if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
    print('Es rectángulo')
else:
    print('No es rectángulo')
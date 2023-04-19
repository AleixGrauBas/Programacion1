#Autor = Aleix Grau Bas
# #Pedida de datos
a = int(input('Introduce el lado a: '))

b = int(input('Introduce el lado b: '))

c = int(input('Introduce el lado c: '))

#Comprobar si es equilátero
if a == b or  b == c or a == c:
    if a == b and b == c:
        print('No es isósceles')
    else:
        print('Es isósceles')
else:
    print('No es isósceles')
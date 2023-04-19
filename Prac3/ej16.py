#Autor: Aleix Grau Bas
#Pedir cadena
cadena = input('Introduce una cadena de caracteres: ')
son_digitos = True
#Bucle para comprobar si son números
for i in range(len(cadena)):
    if cadena[i] not in '1234567890':
        son_digitos = False
        print('No todos los caracteres son dígitos')
        break
if son_digitos == True:
    print('Todos los caracteres son dígitos')


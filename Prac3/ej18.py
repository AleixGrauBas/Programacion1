#Autor: Aleix Grau Bas
#Pedir cadena
cadena = input('Introduce una cadena de caracteres: ')
son_digitos = True
i = 0
suma = 0

#Bucle para comprobar si son números
while i < len(cadena) and son_digitos:
    if cadena[i] not in '1234567890':
        son_digitos = False
        print('Primer "no dígito": \'{0}\' en posición {1}'.format(cadena[i],i))
    else:
        suma += int(cadena[i])
    i += 1
if son_digitos == True:
    print('Todos los caracteres son dígitos')
    print('¿Cuántos dígitos? {0}'.format(i))
    print('¿Suma de dígitos? {0}'.format(suma))

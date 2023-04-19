#Autor: Aleix Grau Bas

cadena = input('Introduce un texto (vacío para acabar): ')

if cadena != '':
    palabra_max = cadena
    max = len(cadena)
    palabra_min = cadena
    min = len(cadena)
    while cadena != '':
        if len(cadena) >= max:
            palabra_max = cadena
            max = len(palabra_max)
        if len(cadena) <= min:
            palabra_min = cadena
            min = len(palabra_min)
        cadena = input('Introduce otro texto (vacío para acabar): ')

    print('Última cadena de mínima longitud, {0}: =>{1}<='.format(min,palabra_min))
    print('Última cadena de máxima longitud, {0}: =>{1}<='.format(max,palabra_max))
else:
    print('no se ha introducido ningún texto')
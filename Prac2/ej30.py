#Autor = Aleix Grau Bas
# #Pedimos un número real

n = float(input('Introduce un número: '))
suma = 0
minimo = n
maximo = n
divisores = 0

if n < 0:
    print('No se han introducido datos')
else:
    while n >= 0:
        if n < minimo:
            minimo = n
        if n > maximo:
            maximo = n
        divisores += 1
        suma += n
        n = float(input('Introduce otro número: '))

    print('Media: {0}'.format(suma / divisores))
    print('Mínimo: {0}'.format(minimo))
    print('Máximo: {0}'.format(maximo))
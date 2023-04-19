#pedida de datos

cadena = input('Introduce una cadena: ')

separador = input('Introduce un separador: ')

numero = int(input('Introduce un número entero: '))

#Multiplicamos la cadena n veces y la mostramos

resultado = (cadena + separador) * (numero - 1) + cadena

print(resultado)
#Autor = Aleix Grau Bas
# #Pedida del número n

numero = int(input('Introduce un número entero: '))
n = 1
separador = ', '
#Mostramos la cadena de n hasta 0
cadena = ""
while n <= numero:
    cadena += str(n)
    n += 1
    if n <= numero:
        cadena += separador

print(cadena)
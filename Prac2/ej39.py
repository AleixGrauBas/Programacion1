#Autor = Aleix Grau Bas
# #Pedida de datos
n = int(input('Introduce un número entero: '))

#Números primos
print('Los números primos menores que {0} son: '.format(n),end= '')
número = 1
while número < n:
    # Determinar si número es primo (2 divisores)
    cantidad_divisores = 0
    divisor = 1
    while divisor <= número:
        if número % divisor == 0:  # Divisor encontrado
            cantidad_divisores += 1
        divisor += 1

        es_primo = cantidad_divisores == 2

    if es_primo:
        print(número, end=' ')

    número += 1






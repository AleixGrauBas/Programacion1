#Pedida de número
n = int(input('Introduce un número entero: '))
i = n
factorial = 0
#Calcular el factorial
if n == 1 or n == 0:
    factorial = 1
else:
    while i > 0:
        factorial += i * i-1
        i -= 1
print('{0}! = {1}'.format(n,factorial))
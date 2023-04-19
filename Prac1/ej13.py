#Pedida de datos

numeroA = int(input('Introduce el número a: '))

numeroB = int(input('Introduce el número b: '))

#Calculamos las operaciones (2^a) + b y 2^(a+b) y mostramos los resultados

print('{0}'.format(2**numeroA + numeroB))
print('{0}'.format(2**(numeroA + numeroB)))
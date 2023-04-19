#Autor = Aleix Grau Bas
# #Pedida de datos

importe = float(input('Introduce el importe de la compra: '))

zona = input('Introduce la zona de envío (A/B/C): ')

socio = input('¿Eres socio (S/N)? ')

gastos = 0
#Calcular importes

if importe <= 150:
    if socio == 'S':
        gastos = 19
    if socio == 'N':
        gastos = 25
elif importe > 150 and importe <= 750:
    if socio == 'S':
        gastos = 49
    if socio == 'N':
        gastos = 60
elif importe > 750 and importe <= 1500:
    if socio == 'S':
        gastos = 89
    if socio == 'N':
        gastos = 120
elif importe > 1500:
    if socio == 'S':
        gastos = importe * 0.06
    if socio == 'N':
        gastos = importe * 0.08

#Zona A
if zona == 'A':
    envio = gastos

#Zona B
if zona == 'B':
    envio = gastos + 30

#Zona C
if zona == 'C':
    envio = gastos + 69

print('Gastos de envío: {0:.2f} euros'.format(envio))
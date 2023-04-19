#Pedida de datos

angulo = int(input('Introduce un ángulo (en grados): '))

#Comprobar que tipo de ángulo es
if angulo == 0:
    print('Nulo')
if angulo > 0 and angulo < 90:
    print('Agudo')
if angulo == 90:
    print('Recto')
if angulo > 90 and angulo < 180:
    print('Obtuso')
if angulo == 180:
    print('Llano')
if angulo > 180 and angulo < 360:
    print('Cóncavo')
if angulo == 360:
    print('Completo')
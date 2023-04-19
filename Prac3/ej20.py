#Autor: Aleix Grau Bas
#Función que nos dice si es una letra castellana
def es_letra_castellana(letra):
    return (letra >= 'A' and letra <= 'Z') or (letra >= 'a' and letra <= 'z') or letra in 'ÑñÁáÉéÍíÓóÚúü'

#Pedimos una palabra
print('Ve introduciendo palabras, o vacío para acabar...')
palabra = input('Nueva palabra: ')

while palabra != '':
    es_correcta = True
    i = 0
    while i < len(palabra) and es_correcta:
        if not es_letra_castellana(palabra[i]):
            print('Contiene un carácter que no es del alfabeto castellano: \'{0}\''.format(palabra[i]))
            es_correcta = False
        i += 1
    if es_correcta:
        print('Podría ser una palabra correcta')
    palabra = input('Nueva palabra: ')

print('¡Adiós!')
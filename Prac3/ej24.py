#Autor: Aleix Grau Bas
cadena = input('Introduce una cadena de caracteres A: ')
sufijo = input('Introduce una cadena de caracteres B: ')
i = 1
es_sufijo = True
if len(sufijo) > len(cadena):
    print('b no es sufijo de a')
else:
    while i <= len(sufijo) and es_sufijo:
        if sufijo[-i] == cadena[-i]:
            es_sufijo = True
        else:
            es_sufijo = False
        i+=1
    if es_sufijo:
        print('B es sufijo de A')
    else:
        print('b no es sufijo de a')

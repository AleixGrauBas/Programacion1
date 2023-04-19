#Autor: Aleix Grau Bas
#Pedimos los resultados del test
resultados = input('Introduce la plantilla de respuestas correctas: ')
print('Ve introduciendo respuestas de alumnos, o vacío para acabar...')
respuestas = input('Nuevas respuestas: ')
corregidos = 0
i = 0
bien = 0
mal = 0
ns = 0
while respuestas != '':  #Mientras la respuesta introducida no sea un espacio seguimos corrigiendo

    while len(respuestas) < len(resultados): #Si la respuesta introducida es menor que la respuesta no es válida
        print('La cadena introducida es de longitud {0} (se esperaba {1})'.format(len(respuestas),len(resultados)))
        respuestas = input('Nuevas respuestas: ')
        if respuestas == '':
            break
    if len(resultados) == len(respuestas):
        while i < len(respuestas): #Comprobamos uno a uno los resultados para ver los aciertos, errores y sin contestar
            if respuestas[i] == resultados[i]:
                bien += 1
            elif respuestas[i] == '*':
                ns += 1
            elif respuestas[i] != resultados[i]:
                mal += 1
            i += 1
        print('Resultados: {0} BIEN; {1} MAL; {2} NS/NC'.format(bien,mal,ns))
        respuestas = input('Nuevas respuestas: ')
        corregidos += 1
        bien = 0
        mal = 0
        ns = 0
print('Alumnos corregidos: {0}'.format(corregidos))
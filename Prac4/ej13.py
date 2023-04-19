#Autor: Aleix Grau Bas
print('Ve introduciendo candidaturas, o vacío para acabar...')

candidatura = input('Nueva candidatura: ')
lista_candidaturas = []
lista_candidaturas.append(candidatura)
while candidatura != '': #Mientras no se introduzca un espacio pedimos nuevas candidaturas
    candidatura = input('Nueva candidatura: ')
    lista_candidaturas.append(candidatura)

votos_candidaturas = []

for i in range(len(lista_candidaturas)-1):
    votos = int(input('Votos para {0}: '.format(lista_candidaturas[i])))
    votos_candidaturas.append(votos)

suma = 0
for i in range(len(votos_candidaturas)):
    suma += votos_candidaturas[i]

for i in range(len(votos_candidaturas)):
    print('{0:.2f}% de los votos a candidaturas para {1}'.format((votos_candidaturas[i]/suma)*100,lista_candidaturas[i]))

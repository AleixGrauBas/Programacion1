#Autor: Aleix Grau Bas
def evaluación_test(plantilla,resultado):
    for i in range(len(plantilla)):
        bien = 0
        mal = 0
        ns = 0
        if plantilla[i] == resultado[i]:
            bien +=1
        elif plantilla[i] == "":
            ns += 1
        else:
            mal += 1
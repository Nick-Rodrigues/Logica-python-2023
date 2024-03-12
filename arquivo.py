import random

def criar_matriz():
    matriz = []
    linha = int(input("Diga o numero de linhas: "))
    coluna = int(input("Diga o numero de colunas: "))
    for i in range(linha):
        linha_matriz = []
        matriz.append(linha_matriz)
        for j in range(coluna):
            matriz[i].append(random.randint(1,9))
    #printar linhas:
    for m in range(linha):
        print(matriz[m])
    return matriz 

def somar_matriz(matriz1, matriz2):
    if len(matriz1) == len(matriz2):
        nova_matriz = []
        for i in range(len(matriz1)): 
            nova_matriz.append([])
            for j in range(len(matriz1[i])):
                nova_matriz[i].append((matriz1[i][j] + matriz2[i][j]))
    for m in range(len(matriz1)):
        print(nova_matriz[m])
    return nova_matriz




# math.round(random()*10) + 1 
matriz1 = criar_matriz()
matriz2 = criar_matriz()
# print("\n")
# somar_matriz(matriz1, matriz2)


def multiplar_matriz(matriz1, matriz2):
    #condição existencial
    if len(matriz1[0]) == len(matriz2):
        nova_matriz = []
        for i in range(len(matriz1)):
            nova_matriz.append(([]))
            for j in range(len(matriz2[0])):
                acumulador = 0
                for m in range(len(matriz2[0])):
                    acumulador += matriz1[i][m] * matriz2[m][j]
                nova_matriz[i].append(acumulador)
    return nova_matriz

print(multiplar_matriz(matriz1, matriz2))

        
            
def printa_elementos_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j])
    return

def printa_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return


# for i in range(len(matriz1)):
#     for j in range (len(matriz1[0])):
#         matriz1[i][j] = 0
# printa_elementos_matriz(matriz1)
#matriz1 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
# for i in range(len(matriz1)):
#     for j in range(len(matriz1[0])):
#         if j < i:
#             matriz1[i][j] = 1
#         else:
#             matriz1[i][j] = 0

#print pares
# for j in range(0,len(matriz1),2):
#     print(f'coluna {j}:')
#     for i in range(len(matriz1[0])):
#         print(matriz1[i][j])

#print impares
# for i in range(1,len(matriz1),2):
#     print(f"Linha {i}")
#     for j in range(len(matriz1[0])):
#         print(matriz1[i][j], end=' ')
#     print("\n")


# for i in range(len(matriz1)):
#     print(" "*2*i,end=' ')
#     print(matriz1[i][i])

# def cria_matriz(linhas,colunas):
#     matriz = []
#     for i in  range(linhas):
#         matriz.append([])
#         for j in range(colunas):
#             matriz[i].append(1)
#     return matriz
# identidade = cria_matriz(5,5)
# identidade2 = cria_matriz(5,5)
# printa_matriz(identidade)
# print("\n")
# printa_matriz(identidade2)

# def soma_matriz(m1,m2):
#     linhas = len(m1)
#     colunas = len(m1[0])
#     soma = cria_matriz(linhas,colunas)
#     for i in range(linhas):
#         for j in range(colunas):
#             soma[i][j] = m1[i][j]+m2[i][j]
#     return soma

# matriz1 = cria_matriz(3,4)
# printa_matriz(matriz1)
# print("\n")
# matriz2 = cria_matriz(3,4)
# printa_matriz*matriz2
# print("\n")
# soma_matriz

matriz = [[1,2,3],[4,5,6],[7,8,9]]

def transposta(matriz):
    if len(matriz) == len(matriz[0]):
        for i in range(len(matriz)):
            for j in range(len(matriz[0])//2):
                aux = matriz[i][j]
                matriz[i][j] = matriz[j][i]
                matriz[j][i] = aux
    return matriz

matriz1 = [[1,2,3],[4,5,6],[7,8,9]]
matriz1 = transposta(matriz1)
printa_matriz(matriz1)

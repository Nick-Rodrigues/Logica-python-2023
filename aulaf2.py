# matriz = [[1,2,3],[4,5,6],[7,8,9]]
def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

def printa_elemento(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"matriz[{i}][{j}]= {matriz[i][j]}")
    return


colunas = 4
linhas = 3
def cria_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            matriz[i].append(0)
    return matriz

# tam = int(input("tam matriz : "))
# matriz1 = cria_matriz(tam,tam)

# import matplotlib.pyplot as plt

# matriz1 = [[1,2,3],[4,5,6],[7,8,9]]
# mostra_matriz(matriz1)

# def soma_matriz(m1,m2):
#     linhas1 = len(m1)
#     linhas2 = len(m2)
#     cols1 = len(m1[0])
#     cols2 = len(m2[0])
#     if linhas2 != linhas1 or cols2 != cols1:
#         print("Impossível somar matrizees de dimensões diferentes")
#         return
#     else: 
#         for i in range(linhas2):
#             for j in range(cols1):
#             m1[i][j] += m2[i][j]
#     return m1

# matriz1 = cria_matriz(3,4,1)
# matriz2 = cria_matriz(3,4,2)
# matriz3 = soma(matriz1,matriz2)
# mostra_matriz(matriz1)

matriz = [[1,2,3],[4,5,6],[7,8,9]]

def transpor_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i>j:
                aux = matriz[i][j]
                matriz[i][j] = matriz[j][i]
                matriz[j][i] = aux
    return 

def transpor_rapido(matriz):
    for i in range(len(matriz)):
        for j in (i):
            if i>j:
                aux = matriz[i][j]
                matriz[i][j] = matriz[j][i]
                matriz[j][i] = aux
    return


    
# print()
# mostra_matriz(matriz)

#multiplicando
matriz1 = [[1,2,3],[4,5,6],[7,8,9]]
matriz2 = [[10,20,30],[40,50,60],[70,80,90]]
m3= cria_matriz(3,3)

for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        m3[i][j] += matriz1[i][j]*matriz2[j][i]
mostra_matriz(m3)
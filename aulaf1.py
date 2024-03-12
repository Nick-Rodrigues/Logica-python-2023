# nomes = ["KA", "Fusca", "Celta", "UP", "Kombi"]
# precos = [50, 60, 1000000, 200, 30]

# maior = precos[0]
# indice_maior = 0

# for i in range(len(precos)):
#         if precos[i] > maior:
#             maior = precos[i]
#             indice_maior = i

# print(f"O carro mais caro é o {nomes[indice_maior]} e vale {precos[indice_maior]}$")
    
# def acha_maior(lista):
#     indice_maior = 0
#     maior = precos[indice_maior]

#     for i in range(len(lista)):
#         if lista[i] > maior:
#             maior = lista[i]
#             indice_maior = i
#     return indice_maior

# lista = [2,24,54,43,67]
# local_maior = acha_maior(lista)
# print(lista[local_maior])

# matriz = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
# print(matriz)
# for i in range(len(matriz)):
#     for j in range(len(matriz[0])):
#         if i==j:
#             print(matriz[i][j])

n = 0
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        n=1
        linha.append(n)
    matriz.append(linha)
    print(matriz)
    


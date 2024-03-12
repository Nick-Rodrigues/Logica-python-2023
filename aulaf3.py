# def cria_matriz(linhas,colunas):
#     matriz = []
#     for i in range(linhas):
#         matriz.append([])
#         for j in range(colunas):
#             matriz[i].append(i+j)
#     return matriz

# def mostra_matriz(matriz):
#     for i in range(len(matriz)):
#         print(matriz[i])
#     return

# def soma_elementos(vetor):
#     soma = 0
#     for i in range(len(vetor)):
#         soma += vetor[i]
#     return soma

# alunos = 10
# notas = cria_matriz(5,alunos)
# mostra_matriz(notas)
# pesos = [1,2,3,2,1]
# medias = []
# for j in range(alunos):
#     soma = 0
#     soma_pesos = soma_elementos(pesos)
#     for i in range(len(pesos)):
#         soma += pesos[i]*notas[i][j]
#     media = soma/soma_pesos
#     medias.append(media)
# print(medias)

# dic = {'são paulo' : 'vencedor', 
#        'corinthians' : 'perdedor', 
#        'palmeiras' : 'sem mundial', 
#        'santos' : 'charlie brown jr sk8'}
# time = input("Que time voce torce? ")
# print(f"voce é um {dic[time]}")

# dic= {"chave1" : "valor1"}
# #print(dic)
# #print(dic["chave1"])
# dic["chave2"] = "valor2"
# dic["chave1"] = "novo valor"
# #print(dic)
# #print(dic.keys())

# for key in dic.keys():
#     print(dic[key])

# numeros = {}
# numeros["pares"] = []
# numeros["impares"] = []
# for i in range(100):
#     if i%2 == 0:
#         numeros["pares"].append(i)
#     else:
#         numeros["impares"].append(i)
# print(numeros)
# for key in numeros.keys():
#     print(numeros[key])

# def local_maior(lista):
#     indice_maior = 0
#     maior = lista[indice_maior]
#     for i in range(len(lista)):
#         if lista[i] > maior:
#             indice_maior = i
#             maior = lista[i]
#     return indice_maior

# carros = {"modelo" : ["uno", "fusca", "celtinha brabo", "supra"], "valor" : [100, 50, 1000, 300]}

# indice_mais_caro = local_maior(carros["valor"])
# print(f"O carro mais caro é o {carros['modelo'][indice_mais_caro]}, e custa {carros['valor'][indice_mais_caro]}")

# potencias = []
# for carro in carros['modelo']:
#     potencia = int(input(f"Digite a potencia do {carro}: "))
#     potencias.append(potencia)
# print(potencias)

# carros = {
#     'modelo' : ["uno", "fusca", "celtinha brabo", "supra"], 
#     'valor' : [100, 50, 1000, 300],
#     'potencia' : [30, 20, 70, 50]
# }

# while True:
#     pergunta = input("Voce gostaria de cadastrar um novo carro? (s/n)")

#     if pergunta == 's':
#         print('Diga as informações ')
#         for key in carros.keys():
#             info = input(f'{key} : ')
#             carros[key].append(info)
#     else:
#         print('Cadastro finalizado')
#     break
# print(carros)

# carros_tecnico = {
#     'modelo' : ["uno", "fusca", "celtinha brabo", "supra"], 
#     'valor' : [100, 50, 1000, 300],
#     'potencia' : [30, 20, 70, 50]
# }

# carros_conforto = {
#     'modelo' : ["uno", "fusca", "celtinha brabo", "supra"], 
#     'nº portas' : [2, 2, 4, 2],
#     'ar condicionado' : ['n', 'n', 's', 'n']
# }

# uniao_carros = {}
# for key in carros_tecnico.keys():
#     uniao_carros[key] = carros_tecnico[key]
# for key in carros_conforto.keys():
#     if key not in uniao_carros.keys():
#         uniao_carros[key] = carros_conforto[key]
# print(uniao_carros)

frase = 'A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha.'
frase = frase.lower()
frase = frase.replace('.','')
frase = frase.split(' ')
print(frase)
# print(frase)

palavras = {}
for palavra in frase:
    if palavra not in palavras.keys():
        palavras[palavra] = 1
    else:
        palavras[palavra] += 1 
print(palavras)
for key in palavras.keys():
    for palavra in frase:
        if palavra == key:
            palavras[palavra] += 1
print(palavras)

# matriz1 = cria_matriz(3,3)
# mostra_matriz(matriz1)
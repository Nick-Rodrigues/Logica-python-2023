# jogo = {'são paulo' : 'vencedor', 'corinthians' : 'perdedor'}
# jogo['palmeiras'] = 'mor avião hein kk'
# jogo['corinthians'] = [jogo['corinthians']]
# jogo['corinthians'].append('eliminado')
# print(jogo)

# numeros = {'pares' : [], 'impares' : []}
# for i in range(10):
#     if i%2==0:
#         numeros['pares'].append(i)
#     else:
#         numeros['impares'].append(i)
# print(numeros)

def local_maior(lista):
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        if lista[i] > maior:
            indice_maior = i
            maior = lista[i]
    return indice_maior

carros = {"modelo" : ["uno", "fusca", "celtinha brabo", "supra"], "valor" : [100, 50, 1000, 300]}
indice_mais_caro = local_maior(carros["valor"])
print(f"O carro mais caro é o {carros['modelo'][indice_mais_caro]}, e custa {carros['valor'][indice_mais_caro]}")

potencias = []
for carro in carros['modelo']:
    potencia = int(input(f"Digite a potencia do {carro}: "))
    potencias.append(potencia)
print(potencias)

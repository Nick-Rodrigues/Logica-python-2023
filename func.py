# def acha_maior(numeros):
#     maior = numeros[0]
#     indice_maior = 0
#     for i in range(len(numeros)):
#         if numeros[i] > maior:
#             maior = numeros[i]
#             indice_maior = i
#     return [indice_maior,maior]
# lista = [123,321,456,564,111,898]
# carros = ["ka", "fusca", "up", "celta","uno","supra"]
# resultado = acha_maior(lista)
# print(resultado)
# indice_do_maior = resultado[0]
# print(carros[indice_do_maior])

def valida_numero(frase):
    num = input(frase)
    while not num.isnumeric():
        num = input(frase)
    return int(num)

def cadastra_vinho():
    qtd = valida_numero("Quantos vinhos quer adicionar? ")
    vinhos = []
    precos = []
    for i in range(qtd):
        nome = input("Diga o nome do vinho: ")
        preco = valida_numero("Diga o preço do vinho: ")
        vinhos.append(nome)
        precos.append(preco)
    return[precos,vinhos]

precos_e_vinhos = cadastra_vinho()
precos = precos_e_vinhos[0]
vinhos = precos_e_vinhos[1]
print(precos)
print(vinhos)
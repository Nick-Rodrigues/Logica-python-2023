# jogo = {'são paulo': 'vencedor', 'corinthians': 'perdedor'}
# print(jogo['são paulo'])
# jogo['palmeiras'] = 'sem mundial'
# print(jogo)
# jogo['são paulo'] = [jogo['são paulo']]
# print(jogo)
# jogo['são paulo'].append('tricolor')
# print(jogo)

def forca_opcao(msg,lista_opcoes):
    resposta = input(msg)
    while resposta not in lista_opcoes:
        print("Digite uma opção cadastrada!")
        resposta = input(msg)
    return resposta


vinhos = {'tipo': ['tinto','seco','doce','suave','branco'], 
        'preço': [10,30,50,15,20],
        'safra': [1927,1935,1910,1951,1941],
        'porc alcoolico': [10,15,13,11,16]
        }

valor_total = 0
compra = {}
while True:
    print("Bem vindo a vinheria")
    s_ou_n = forca_opcao('Você gostaria de conhecer vinhos? (s/n) ', ['s','n'])
    if s_ou_n =='s':
        if not compra:
            endereco = input("Diga o endereço de entrega")
            compra["endereco"] = endereco
        i = 0
        for tipo in vinhos['tipo']:
            print(f"{i} - {tipo} ")
            i+=1
        opcao = int(forca_opcao("Digite a opção desejada: ", ['0','1','2','3','4']))
        for key in vinhos.keys():
            print(f"{key} : {vinhos[key][opcao]}")
        comprar = forca_opcao('Voce gostaria de adquirir esta iguaria sem igual? (s/n)', ['s','n'])
        if comprar == 's':
            valor_total+=vinhos['preço'][opcao]
            print(f"Voce comprou o vinho {vinhos['tipo'][opcao]}")
            print(f"Seu carrinho está em R${valor_total}")
    else:
        print(f"Seu pedido ficou em R${valor_total}")
        print("Volte sempre")
        break
print(compra)

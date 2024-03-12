# import pandas as pd
# lista = [54,3,56,2,4,7,6,34]
# tentativa = 0
# while tentativa < 3:
#     try:
#         tentativa+=1
#         indice = int(input("Diga um numero : "))
#         print(lista[indice])
#         print('1'+2)
#         break
#     except IndexError as e:
#         print(e)
#         print(f"Este indice nÃ£o existe! o mÃ¡ximo Ã© {len(lista)-1}")
#     except ValueError as e:
#         print(e)
#         print("Deve ser um valor numerico!")
#     except TypeError:
#         print("alguma coisa aconteceu")
#     finally:
#         print(f"Voce estÃ¡ na {tentativa} tentativa")


#pergunte ao usuÃ¡rio se ele Ã© cliente ou funcionÃ¡rio
#se for cliente, de as opÃ§Ãµes de vinhos da casa e pergunte seu endereÃ§o
#pergunte informaÃ§Ãµes a respeito de qual ele quer ver
#pergunte se ele vai comprar o vinho escolhido no item anterior
#caso queira, adicione ao carrinho dele o vinho e seu preÃ§o
def login():
    usuario = obriga_opcao("Diga seu usuario : ",["Danilo"],3)
    if usuario:
        senha = obriga_opcao("Diga sua senha : ",['1234'],3)
    else:
        return False

    return senha and usuario

def altera_preco():
    for i in range(len(vinhos['tipo'])):
        print(f"{i} - {vinhos['tipo'][i]}")
    vinho = int(obriga_opcao("De que vinho vc vai alterar ? ",lista_vinhos))
    while True:
        try:
            preco = float(input("Diga o novo preÃ§o : "))
            break
        except ValueError:
            print("Deve ser um nÃºmero")
    vinhos['preço'][vinho] = preco
    return
def remove_produto():
    for i in range(len(vinhos['tipo'])):
        print(f"{i} - {vinhos['tipo'][i]}")
    vinho = int(obriga_opcao("Qual vinho vc vai remover ? ",lista_vinhos))
    for key in vinhos.keys():
        vinhos[key].pop(vinho)
    return
def cadastra_produto():
    for key in vinhos.keys():
        if types[key] is not str:
            while True:
                try:
                    if types[key] is float:
                        flag = "com ponto ao invÃ©s de virgula"
                        info = float(input(f"Diga o/a novo/a {key} : "))
                    else:
                        flag = "sem virgulas"
                        info = int(input(f"Diga o/a novo/a {key} : "))
                    break
                except ValueError:
                    print(f"Deve ser um valor {flag}!")
        else:
            info = input(f"Diga o/a novo/a {key} : ")
        vinhos[key].append(info)

    return
def obriga_opcao(msg,lista_opcoes,max_tentativas = None):
    resposta = input(msg)
    tentativas = 1
    while resposta not in lista_opcoes:
        print("Digite uma opção válida! ")
        resposta = input(msg)
        if max_tentativas:
            if tentativas>=max_tentativas-1:
                print("Sai Hacker")
                return False
            tentativas +=1
    return resposta
def printa_dicionarios(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            printa_dicionarios(dic[key])
        else:
            print(f"{key} : {dic[key]}")
    return
vinhos = {
    'tipo' : ['tinto', 'rose', 'seco', 'branco', 'suave'],
    '% alcoólico' : [11.0,15.0,12.0,13.0,10.0],
    'safra' : [1958,1962,1970,1994,2002],
    'preço' : [100.0,130.0,20.0,25.0,50.0],
    'Nacionalidade' : ['chileno','argentino','frances','italiano','jundiaiense'],
    'estoque' : [1,20,30,40,50]
}
types = {key:type(vinhos[key][0]) for key in vinhos.keys()}
print(types)
compra = {
    'valor total' : 0,
    'endereÃ§o' : {
        'cep' : '',
        'numero' : ''
    },
    'vinhos' : {}
}
printa_dicionarios(compra)
print(pd.DataFrame(vinhos))
c_f = obriga_opcao("Voce é cliente ou funcionáio ? (c/f) ",['c','f'])
lista_vinhos = [str(i) for i in range(len(vinhos['tipo']))]
#lista_opcoes = []
#for i in range(len(vinhos['tipo'])):
#    lista_opcoes.append(str(i))

if c_f == 'c':
    print("Seja bem vindo!!! ")
    for key in compra['endereço'].keys():
        info = input(f"Diga seu {key} : ")
        compra['endereÃ§o'][key] = info
    while True:
        print("Essas são nossas opções de vinhos: ")
        for i in range(len(vinhos['tipo'])):
            print(f"{i} - {vinhos['tipo'][i]}")
        opcao = int(obriga_opcao("Por qual vc se interesou ?",lista_vinhos))
        for key in vinhos.keys():
            print(f"{key} : {vinhos[key][opcao]}")
        comprar = obriga_opcao("Voce quer levar ?(s/n)",['s','n'])
        if comprar == 's':
            if vinhos['estoque'][opcao]==0:
                print(f"Desculpa, nÃ£o temos mais estoque de {vinhos['tipo'][opcao]}")
                continue
            else:
                vinhos['estoque'][opcao]-=1
            compra['valor total'] += vinhos['preÃ§o'][opcao]
            nome = vinhos['tipo'][opcao]
            if nome not in compra['vinhos'].keys():
                compra['vinhos'][nome] = 1
            else:
                compra['vinhos'][nome] += 1

        continuar = obriga_opcao("Vc quer ver mais vinhos?(s/n) ",['s','n'])
        if continuar == 'n':
            print("Obrigado pela sua compra:")
            printa_dicionarios(compra)
            break
else:
    if login():
        while True:
            operacao = obriga_opcao("Qual operacao vc deseja realizar ?\n0-Alterar preÃ§o"
                                    "\n1-Remover produto\n2-Cadastrar produto"
                                    "\n3-Sair\n-> ",['0','1','2','3'])
            if operacao == '0':
                altera_preco()
            elif operacao == '1':
                remove_produto()
                lista_vinhos = [str(i) for i in range(len(vinhos['tipo']))]
            elif operacao == '2':
                cadastra_produto()
                lista_vinhos = [str(i) for i in range(len(vinhos['tipo']))]
            else:
                print("Operação realizada com sucesso!")
                print(pd.DataFrame(vinhos))
                break
    else:
        print("Encerrando programa!")

import requests
url = "https://yahoo-weather5.p.rapidapi.com/weather"
querystring = {"location":"São Paulo","format":"json","u":"c"}
headers = {
	"X-RapidAPI-Key": "d9ebb4af2amshe17ab90a1f24cebp11e7c9jsn147c38d73b9e",
	"X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring)
print(response.json())
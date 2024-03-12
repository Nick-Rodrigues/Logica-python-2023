import requests

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
# def login():
#     cadastro = forca_opcao("Voce ja possui cadastro? (s/n)", ['s','n'])
#     if cadastro == 'n':
#         cadastrar_usuario = forca_opcao("Deseja se cadastrar? (s/n)", ['s','n'])
#         if cadastrar_usuario == 'n':
#             print("Tchau")
#         else:
#             user = input("Digite seu usuário: ")
#             senha = input("Digite sua senha: ")
#             print("Cadastro realizado com sucesso!")
#             tentativas = 1
#     else: 
#         user_login = input("Digite seu usuário")
#         senha_login = input("Digite sua senha")
#         while not (user_login == user and senha_login == senha) and tentativas <3:
#             tentativas +=1
#             print("Usuário ou senha inválidos.")
#         else:
#             print("Login efetuado com sucesso!")

def login():
    usuario = obriga_opcao("Diga seu usuario : ",["Danilo"],3)
    if usuario:
        senha = obriga_opcao("Diga sua senha : ",['1234'],3)
    else:
        return False

    return senha and usuario

def verifica_endereco():
    while True:
        cep = input("Diga seu cep: ")
        url = (f"https://viacep.com.br/ws/{cep}/json/")
        response = requests.get(url)
        if response.status_code == 200:
            print(" Essas são as informações a respeito do seu cep: ")
            response = response.json()
            for key in response.keys():
                print(f"{key} : {response[key]}")
            correto = forca_opcao("Estão corretas ? (s/n)", ['s','n'])
            if correto == 's':
                numero = input("Diga o seu numero da residencia: ")
                response['numero'] = numero
                return response
        else:
            print("Cep inválido!")

def alterar_vinho():
    for i in range(len(vinhos['tipo'])):
        print(f"{i} - {vinhos['tipo'][i]}")
    alterar = forca_opcao("Qual vinho será alterado ? ",lista_vinhos)
    novo_valor = float(input("Diga o novo valor : "))
    vinhos['preço'][alterar] = novo_valor
    print(pd.DataFrame(vinhos))
    return

def remover():
    for i in range(len(vinhos['tipo'])):
        print(f"{i} - {vinhos['tipo'][i]}")
    removido = int(forca_opcao("Qual vinho será removido ? ",lista_vinhos))
    for key in vinhos.keys():
        vinhos[key].pop(removido)
    print(pd.DataFrame(vinhos))
    return

def cadastrar():
    for key in vinhos.keys():
        cep = input(f"Diga o/a novo/a {key} : ")
        vinhos[key].append(cep)
    print(pd.DataFrame(vinhos))
    return

def forca_opcao(msg,lista_opcoes):
    resposta = input(msg)
    while resposta not in lista_opcoes:
        print("Digite uma resposta cadastrada! ")
        resposta = input(msg)
    return resposta
def printa_dicionario(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            printa_dicionario(dic[key])
        else:
            print(f"{key} : {dic[key]}")
    return
vinhos = {
    'tipo' : ['tinto', 'rosé', 'seco', 'branco', 'suave'],
    '% alcoólico' : [11,15,12,13,10],
    'safra' : [1958,1962,1970,1994,2002],
    'preço' : [100,130,20,25,50],
    'Nacionalidade' : ['chileno','argentino','françês','italiano','jundiaiense']
}
# import pandas as pd
# 
lista_vinhos = [str(i) for i in range(len(vinhos['tipo']))]
'''
lista_vinhos = []
for i in range(len(vinhos['tipo'])):
    lista_vinhos.append(str(i))
'''
compra = {
    'endereco' : {},
    'valor total' : 0,
    'vinhos' : {}
}
papel = forca_opcao("Você é cliente ou funcionário ? (c/f) ",['c','f'])
if papel == 'c':
    compra['endereco'] = verifica_endereco()

    while True:
        print('Essas são as nossas opções de vinhos :')
        for i in range(len(vinhos['tipo'])):
            print(f"{i} - {vinhos['tipo'][i]}")
        opcao = int(forca_opcao("Qual vinho lhe interessou mais ? ",lista_vinhos))
        for key in vinhos.keys():
            print(f"{key} : {vinhos[key][opcao]}")
        comprar = forca_opcao("Vai levar ? (s/n) ",['s','n'])
        if comprar == 's':
            compra['valor total'] += vinhos['preço'][opcao]
            nome = vinhos['tipo'][opcao]
            if nome not in compra['vinhos'].keys():
                compra['vinhos'][nome] = 1
            else:
                compra['vinhos'][nome] += 1
        continuar = forca_opcao("Voce gostaria de ver mais vinhos ? (s/n)",['s','n'])
        if continuar == 's':
            continue
        else:
            print("Obrigado pela compra : ")
            printa_dicionario(compra)
            break
else:
    if login():
        while True:
            acoes = ['alterar preço','remover','cadastrar','sair']
            print("Essas são as opções de ação: ")
            for i in range(len(acoes)):
                print(f"{i} - {acoes[i]}")
            opcao = forca_opcao('O que vc deseja fazer ? ',['0','1','2','3'])
            if opcao == '0':
                alterar_vinho()
            elif opcao == '2':
                cadastrar()
            elif opcao == '1':
                remover()
            else:
                break
    else:
        print("Sai hacker")
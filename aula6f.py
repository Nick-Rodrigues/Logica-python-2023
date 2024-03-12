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
    'tipo':['tinto','rose','seco','branco','suave'],
    'porc alcoolico': [11,15,12,13,10],
    'safra': [1958,1962,1970,1994,2002],
    'preco': [100,130,20,25,50],
    'nacionalidade': ['chileno','argentino','frances','italiano','jundiniense']
}

compra = {
    'endereco' : {'rua': '',
                  'bairro':'',
                  'cidade':'',
                  'numero': '',
                  'cep': '',
                  'estado': ''
            },
            'valor total': 0, 
            'vinhos': {}}
lista_vinhos = [str(i) for i in range(len(vinhos['tipo']))]
papel = forca_opcao("Voce é um cliente ou funcionario? (c/f)",['c','f'])
if papel == "c":
    print("Seja bem vindo")
    for key in compra['endereco'].keys():
        info = input(f"Diga seu/a {key}: ")
        compra['endereco'][key] = info
    while True:
        print("Essas são as opções de vinhos: ")
        for i in range(len(vinhos['tipo'])):
            print(f"{i} - {vinhos['tipo'][i]}")
        opcao = int(forca_opcao("Qual vinho lhe interessou mais? ", lista_vinhos))
        for key in vinhos.keys():
            print(f"{key} : {vinhos[key][opcao]}")
        comprar = forca_opcao("vai levar? (s/n)", ['s','n'])
        if comprar == 's': 
            compra['valor total'] += vinhos['preco'][opcao]
            nome = vinhos['tipo'][opcao]
            if nome not in compra['vinhos'].keys():
                compra['vinhos'][nome] = 1
            else:
                compra['vinhos'][nome] += 1
        continuar = forca_opcao("Voce gostaria de ver masi vinhos? (s/n)",['s','n'])
        if continuar == 's':
            continue        
        else: 
            print("Obrigado ela compra")
            printa_dicionario(compra)
            break
else:
    func = forca_opcao("O que voce gostaria de realizar? \n 1-Adicionar vinho \n 2-Alterar vinho \n 3-Remover vinho \n", ['1','2','3'])
    if func == '2':
        while True:
            print("Essas são as opções de vinhos: ")
            for i in range(len(vinhos['tipo'])):
                print(f"{i} - {vinhos['tipo'][i]}")
            opcao = int(forca_opcao("Qual vinho deseja alterar? ", lista_vinhos))
            for key in vinhos.keys():
                print(f"{key} : {vinhos[key][opcao]}")
            novo_valor = int(input("Digite o novo valor do vinho: "))
            vinhos['preco'][opcao] = novo_valor
            for key in vinhos.keys():
                print(f"{key} : {vinhos[key][opcao]}")
            break
    elif func == '1':
        for key in vinhos.keys():
            info = input(f"Diga o/a {key}: ")
            vinhos[key].append(info)
        printa_dicionario(vinhos)
    else:
        print("Essas são as opções de vinhos: ")
        for i in range(len(vinhos['tipo'])):
            print(f"{i} - {vinhos['tipo'][i]}")
        opcao = int(forca_opcao("Qual vinho deseja remover? ", lista_vinhos))
        for key in vinhos.keys():
            vinhos[key].pop(opcao)
        printa_dicionario(vinhos)
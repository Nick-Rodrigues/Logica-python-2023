
# def baskara(a,b,c,):
#     delta = b**2 - 4*a*c
#     if delta<0:
#         print(f"Não há raízes")
#         return
#     elif delta == 0:
#         print(f"As duas raízes são iguais a {-b/(2*a)}")
#         return
#     else:
#         x1 = (-b + delta**0.5)/(2*a)
#         x2 = (-b - delta**0.5)/(2*a)
#         print(f"As raízes são {x1} e {x2}")
#         return [x1,x2]
# raizes = baskara(1,-5,6)
# print(raizes)

# def qtd_pares(numeros):
#     qtd = 0
#     for num in numeros:
#         if num%2==0:
#             print(f"{num} é par")
#             qtd+=1
#         else:
#             print(f"{num} é impar")
#     return qtd

# lista = [1,2,543,543321,31256,432,32]
# pares = qtd_pares([31,765,432876,2,6,78,123])
# print(pares)

def acha_maior(numeros):
    maior = numeros[0]
    indice_maior = 0
    for i in range(len(numeros)):
        #print(f"{lista[i]}>{maior}")
        if numeros[i] > maior:
            maior = numeros[i]
            indice_maior = i
            #print(f"Agora o maior é {maior} no indice {indice_maior}")
    return[indice_maior, maior]

# lista = [213,312,12321,54,123,123002]
# #lista2 = [123,312,521,31232,12,32]
# carros = ["ka", "fusca", "up", "supra", "celtinha","kombi", "fiorino", "polo", "civicao"]
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
    qtd = valida_numero("Quantos vinhos? ")
    vinhos = []
    precos = []
    for i in range(qtd):
        nome = input("Diga o nome do vinho: ")
        preco = valida_numero("Diga o preco do vinho: ")
        vinhos.append(nome)
        precos.append(preco)
    return [precos, vinhos]

precos_e_vinhos = cadastra_vinho()
#print(precos_e_vinhos)
precos = precos_e_vinhos[0]
vinhos = precos_e_vinhos[1]
print(precos)
print(vinhos)

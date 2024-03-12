# lista = ['a','b','c']
# while True:
#     try: 
#         i = int(input("Diga um numero : "))
#         print(lista[i])
#         #print('1' + 2)
#     except ValueError:
#         print("Deve ser um número inteiro")
#     except IndexError:
#         print(f"Alem de ser um inteiro, deve ser entre 0 e {len(lista)-1}")
#         raise
#     except Exception as e:
#         print(e) 
#     else:
#         print("Voce fez as operações de forma coerente!")
#         break
#     finally:
#         print("Não sirvo pra muita coisa")


##divisão
# while True:
#     try:
#         a = int(input("Diga o primeiro número: "))
#         b = int(input("Diga o segundo número: "))
#         print(b/a)
#         break
#     except ZeroDivisionError:
#         print("O primeiro número não pode ser 0")
#     except ValueError:
#         print("Tem que um ser número")

##times      
# dic = {
#     'são paulo': 'campeão',
#     'palmeiras':'não tem mundial',
#     'corinthians':'sem estádio',
#     'santos':'idoso'
# }
# while True:
#     try:
#         time = input("Diga seu time: ")
#         print(f"Essas são as informações do seu time: {dic[time]}")
#     except KeyError:
#         print(f"Não temos infos a respeito do {time}")
#     else:
#         print("Até mais")
#         break


# dic = {
#     1:'um',
#     2:'dois',
#     3:'tres'
# }
# while True:
#     num = input("Diga um numero para eu escrever por extenso: ")
#     while not num.isnumeric():
#         print("deve ser um numero!")
#         num = input("Diga um numero para eu escrever por extenso: ")
#     num = int(num)
#     if num in dic.keys():
#         print(dic[num])
#         break
#     else:
#         print("Digite um numero entre 1 2 e 3")

# dic = {
#     1:'um',
#     2:'dois',
#     3:'tres'
# }

# while True:
#     num = input("Diga um numero para eu escrever por extenso: ")
#     try: 
#         num = int(num)
#         extenso = (dic[num])
#     except ValueError:
#         print("Deve ser um int")
#     except KeyError:
#         print(f"Deve ser um desses: {dic.keys()}")
#     else:
#         print(f"O {num} por extenso é {extenso}")
#         break

dic = {
    1:['um','one','uno'],
    2:['dois','two','dos'],
    3:['tres','three','tres']
}

while True:
    try:
        flag = "O numero deve ser 1, 2 ou 3"
        num = int(input("Diga o numero a ser digitado por extenso: "))
        flag = "\n 0 - pt\n 1 - en\n 2 - es"
        lingua = int(input("Diga a lingua na qual voce quer ver por extenso: "
                            "\n 0 - pt\n 1 - en\n 2 - es"))
        extenso = dic[num][lingua]
    except ValueError:
        print(flag)
    except KeyError:
        print(f"Deve ser um desses: {dic.keys()}")
    except IndexError:
        print(flag)
    else:
        print(f"O numero {num} por extenso é {extenso}")
        break

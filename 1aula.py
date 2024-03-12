# num = int(input("Diga um número: "))
# if num > 10:
#     print(f"O {num} é maior que 10!")
# elif num < 10:
#     print(f"O {num} é menor que 10!")
# else:
#     print("Voce digitou 10")

# soma = 0 
# while soma<100:
#     num = int(input("Diga um número: "))
#     soma += num
#     print(f"Atualmente a soma vale {soma}")

# senha = "123456"
# input_usuario = input("Diga a senha: ")
# tentativas = 1
# while not input_usuario == "123456" and tentativas < 3:
#     input_usuario = input("Diga a senha: ")
#     tentativas += 1
# if tentativas < 3:  
#     print("Voce acertou!")
# else:
#     print("Sai hacker")

#lista = [1,2,3,4,5,6]
# for elem in lista:
#     if elem == "danilo":
#         print("Danilo está na lista")

# lista = ["danilo", "luis", "matheus", "renata"]
# for i in range(len(lista)):
#     if lista [i] == "luis":
#         print(f"O {lista[i]} está no indice {i}, ou seja, posição {i+1}")
    # print(f"lista[{i}] = {lista[i]}")

# i = 0
# soma = 0
# while i<10:
#     numeros = int(input("Digite um número: "))
#     soma += numeros 
#     i+=1

# print(f"A soma é{soma}")
# print(f"A média é {soma/i}")

# soma = 0
# for i in range(10):
#     num = int(input("Digite um numero: "))
#     soma += num

# print(f"A soma é {soma}")
# print(f"A média é {soma/(i+1)}")

# soma = 0
# lista = []
# for i in range(10):
#     num = int(input("Digite um número: "))
#     soma += num
#     lista.append(num)
# print(lista)
# print(f"A soma é {soma}")
# print(f"A média é {soma/len(lista)}")


# lista1 = [1,65,324,541,23,54,87,90,3,2]
# lista2 = [321,74,3,65,87,564,9,76,20,91]
# iguais = 0

#opção1
# for num1 in lista1:
#     for num2 in lista2:
#         if num1 == num2:
#             iguais += 1
# print(iguais)

#opção2
# for num1 in lista1: 
#     if num1 in lista2:
#         iguais+=1
# print(iguais)

#método 3 com tamanho de listas diferentes
# lista1 = [1,65,324,541,23,54,87]
# lista2 = [321,74,3,65,87,564,9,76,20,91]
# comuns = 0

# for i in range (len(lista2)):
#     for j in range(len(lista1)):
#         if lista1[j] == lista2[i]:
#             comuns+=1
# print(comuns)

def verifica_maior (lista):
    indice_do_maior = 0
    maior = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i] 
            indice_do_maior = i
    return indice_do_maior
numeros = [312, 311, 765, 312, 653, 89, 1001]
local_maior = verifica_maior(numeros)
print(f"O maior elemento é {numeros[local_maior]}")

        
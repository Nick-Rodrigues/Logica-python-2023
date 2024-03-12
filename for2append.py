# lista_pares = [2,4,6,8,10,"danilo","rodrigo"]
# for num in lista_pares:
#     print(num)
# i=0
# professores = ["ale", "allen","dan dan","erick", "joao","rita"]
# for i in professores:
#     if i == "dan dan":
#         print(f"O {i} é o melhor professor")
#     elif i == "allen":
#         print(f"O {i} é forgado")
#     else:
#         print(f"O/A prof {i} é legal")
#     if i == "rita":
#         indice_da_rita = 1
#     i+=1
# print[professores(indice_da_rita)]

# numeros = [43,65,76,654,234,65,12,65,12,90]
# par = 0
# impar = 0
# soma = 0
# for i in range (len(numeros)):
#     if numeros[i]%2 == 0:
#         par+=1
#     else:
#         impar+=1
#     soma+=numeros[i]
# print(f"tem {par} pares")
# print(f"tem {impar} impares")
# print(f"A soma é {soma} e a media é {soma/len(numeros)}.")

# professores = ["ale", "allen","dan dan","erick", "joao","rita"]
# novos = int(input("Quantos professores vc quer adicionar? "))
# for i in range(novos):
#     nome = input(f"Digite o nome do novo {i+1}º professor: ")
#     professores.append(nome)
# print(professores)
# print(f"Há {len(professores)}professores no total agora")

# frase = f"Agora os professores"
# for nome in professores:
#     frase += f" {nome}, "
# frase += "são professores"
# print(frase)

#indicar numero do 100
#metodo1  
# indice = 0
# numeros = [43,65,76,654,234,100,12,65,12,90]
# for num in numeros:
#     print(f"nomes [{indice}] = {numeros[indice]}")
#     if num == 100:
#         indice_100 = indice
#     indice+=1
# print(f"o numero {numeros[indice_100]} está no indice {indice_100}")
   
#metodo2
# numeros = [43,65,76,654,234,100,12,65,12,90]
# for indice in range(len(numeros)):
#     print(f"numeros[{indice}] = {numeros[indice]}")
#     if numeros[indice] == 100:
#         indice_100 = indice
# print(f"o numero {numeros[indice_100]} está no indice {indice_100}")

#qnts pares e impares
# numeros = [43,65,76,654,234,65,12,65,12,90]
# par = 0
# impar = 0
# for num in numeros:
#     if num%2==0:
#         par+=1
#         continue
#     impar+=1
# print(f"qnt par {par} e qtd impar {impar}")

#se danilo estiver na lista print que ele é professor
# qtd = int(input("Quantos nomes vc quer cadastrar? "))

# nomes = []
# for i in range(qtd):
#     nome = input(f"Diga o {i+1}º nome: ")
#     nomes.append(nome)
#     if nome == "danilo":
#         print(f"o {nome} é professor")



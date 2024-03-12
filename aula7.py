# lista = [ 0, 0, 0, 0, 0,]
# for i in range(len(lista)):
#     usuario = int(input("digite um numero: "))
#     lista[i] = usuario
#     print(lista)

# lista = []
# lista_par = []
# lista_impar = []

# qtd = int(input("Quantos itens deseja adicionar na lista? "))
# for i in range(qtd):
#     num = int(input("Diga o numero: "))
#     lista.append(num)
#     if num%2 == 0:
#         lista_par.append(num)
#     else:
#         lista_impar.append(num)
# print(lista)
# print(lista_par)
# print(lista_impar)

#meu
# lista = []
# q = input("Voce gostaria de adicionar elementos nessa lista? ")
# if q == 'sim':
#     q1 = input("Diga o elemento: ")
#     while q1 != "sair":
#         q1 = input("Diga o elemento: ")
#         lista.append(q1)
# else:
#     print("tchau")
# print(lista)

#professor
lista = []
resposta = input("Voce quer adicionar elementos na lista? ")
while resposta != 'sim' and resposta != 'nao':
    resposta = input("Voce quer adicionar elementos na lista? ")
if resposta == 'sim':
    while True:
        elem = input("Diga o elemento ou sair: ")
        if elem == "sair":
            break
        else:
            lista.append(elem)
else:
    print("Seu bobo")
print(lista)


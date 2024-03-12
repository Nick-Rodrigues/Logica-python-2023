# preco = 0.5
# cadastro = input("Voce tem cadastro? ")
# qtd = int(input("Quantos amaciantes voce deseja comprar? "))

# if cadastro == "sim" and qtd > 100:
#     preco = 0.3
# elif cadastro == "sim" or qtd > 100:
#     preco = 0.35
     
# total = qtd*preco
# print(f"Para comprar {qtd} amaciantes, vc gastou {total}")

# i=2
# while i<10:
#     if i%2==0:
#         print(f"{i} é par")
#     i+=1

# i = 0
# while i<3:
#     letra = input("Digite uma letra: ")
#     if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
#         print(f"{letra} é uma vogal")
#     else:
#         print(f"{letra} é uma consoante")
#     i+=1
#     if i == 3:
#         print("tchau")

# pergunta = input("Voce gostaria de saber os números pares entre 1 e 20? ")
# i = 1
# if pergunta == "sim":
#     while i < 20:
#         if i%2==0:
#             print(f"{i} é par")
#         i+=1
# else:
#     print("Voce é chato")

i = 0
palavra = ""
while i<3:
    palavra += input("Diga uma palavra : ") + " "
    i+=1
print(palavra)

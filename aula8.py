profs = []
# print(profs)
# profs.append("danilo")
# print(profs)
# profs.append("allen")
# print(profs)
# profs.append("danilo")
# print(profs)

# qtd = int(input("Quanto novos professores existem? "))
# for i in range(qtd):
#     novo_profs = input("Digite o nome do novo professor: ")
#     profs.append(novo_profs)
#     print(profs)


# carros = ["fusca", "golf", "celtinha brabo", "uno com escada", "Kombosa da feira"]
# precos = [2000,200000,1000000,300000,500000]
# #para encontrar o carro mais caro eu preciso encontrar a posição do maior valor na lista de preços
# maior = precos[0]
# for i in range(len(precos)):
#     if precos[i] > maior:
#         maior = precos[i]
#         indice_maior = i
#     print(f"O maior valor até agora é {maior}")
# print(f"O preço mais alto é {maior} e foi encontrado no indice {indice_maior}")
# print(f"O carro mais caro é o {carros[indice_maior]}")

# def print_oi():
#     print("olá")

# print_oi()
# print_oi()
# print_oi()

# def checa_numero(a):
#     a = input("Diga um numero: ")
#     while not a.isnumeric():
#         a = input("Diga um número: ")
#     a = int(a)
#     return a

# qtd = checa_numero(input("qdt profs? "))
# preco = checa_numero(input("Diga o maior preço: "))

# def checa_par(x):
#     if x%2 == 0:
#         return True
#     return False

# for i in range(10):
#     numero = int(input("Por favor, digite um número: "))
#     if checa_par(numero):
#         print(f"{numero} é par")
#         continue
#     print(f"{numero} é impar")

def sneaky(lista):
    i=0
    while(i<len(lista)):
        i+=1
    return i

def ordenar(lista):
    i=0
    tamanho = sneaky(lista)
    while(i<tamanho-1):
        if(lista[i]>lista[i+1]):
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux
        i+=1

def trocaValor(valor):
    if(valor ==10):
        return valor
    valor +=1
    return trocaValor(valor)

lista = [3,1,5,6,7,8]
valor = 4
ordenar(lista)
valor=trocaValor(valor)
print(lista,valor)

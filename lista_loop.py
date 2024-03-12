# t = 9
# valor = 0
# while t<17:
#     print(f"o valor é {valor} e o tempo é {t}")
#     if t>=12 and t<14:
#         t+=1
#         continue
#     valor+=100
#     t+=1
# print(f"o valor é {valor} e o tempo é {t}")

# nota = float(input("Digite uma nota entre 0 e 10: "))
# while nota<0 or nota>10:
#     nota = float(input("Digite uma nota entre 0 e 10: "))
#print("acertou")

# nome = input("Digite seu nome: ")
# while len(nome) <= 3:
#     nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# while idade < 0 or idade > 150:
#     idade = int(input("Digite sua idade: "))
# salario = int(input("Digite seu salario: "))
# while salario < 0:
#     salario = int(input("Digite seu salario: "))
# sexo = input("Digite seu sexo (f ou m): ")
# while sexo != 'f' and sexo != 'm':
#     sexo = input("Digite seu sexo (f ou m): ")

# ec = input("Digite seu estado civil (s, c, v, d): ")
# while ec != 's' and ec !='c' and ec != 'v' and ec != 'd':
#     ec = input("Digite seu estado civil (s, c, v, d): ")

# a = 80000
# b = 200000
# taxa_a = 0.03
# taxa_b = 0.015
# anos = 0

# while a < b:
#     a = a + a*taxa_a
#     b = b + b*taxa_b
#     anos +=1
#     print(f"a população de A ira ultrapassar a população de B em {anos} anos")

# i = 0
# soma = 0
# while i<5:
#     num = float(input(f"Diga o {i+1}º número: "))
#     soma+=num
#     i+=1
# media = soma/i
# print(f"A soma dos número é {soma} e a média é {media}")

# nr1 = int(input("Digite o primeiro número: "))
# nr2 = int(input("Digite o segundo número: "))
# menor = nr1
# maior = nr2
# if nr1>nr2:
#     menos = nr2
#     maior = nr1
# else:
#     print("interalo zero")
# while menor<maior:
#     print(menor)
#     menor+=1



# login = input("Digite seu login: ")
# senha = input("Digite sua senha: ")
# while senha == login:
#     print("Ação indiponível. O login deve ser diferente da senha.")
#     login = input("Digite seu login: ")
#     senha = input("Digite sua senha: ")

# numero = int(input("Digite o número que deseja saber a tabuada: "))
# i = 1
# while i <= 10:
#     print(f"{numero} x {i} = {numero*i}")
#     i+=1

#tabuada de todos os números
# num=1
# while num<=10:
#     print(f"A tabuada do {num} é: ")
#     i = 1
#     while i <= 10:
#         print(f"{num} x {i} = {num*i}")
#         i+=1
#     print("\n")
#     num+=1

#fibonacci
# qtd = int(input("Quanos números de fibonacci vc quer saber? "))
# a=1
# b=1
# i=2
# print(a)
# print(b)
# while i <= qtd:
#     c=a+b
#     a=b
#     b=c
#     print(c)
#     i+=1

#faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e impares.
# i=0
# qtd_pares = 0
# qtd_impares = 0
# while True:
#     num = int(input("Diga um número: "))
#     if num%2==0:
#         qtd_pares+=1
#     else:
#         qtd_impares+=1

#     if i == 10:
#         break
#     i+=1
# print(f"Voce digitou {qtd_impares} impares e {qtd_pares} pares")

# qtd = int(input("Quanos números de fibonacci vc quer saber? "))
# a=1
# b=1
# i=2
# qtd_pares = 0
# qtd_impares = 0
# while i<=qtd:
#     c=a+b
#     a=b
#     b=c
#     i+=1
#     if c%2==0:
#         qtd_pares+=1
#     else:
#         qtd_impares+=1
# print(f"Dentre os {qtd} primeiros números de fibonacci há {qtd_pares} pares e {qtd_impares} impares")

i=2
num = int(input("diga um número: "))
while i<num:
    resultado = num%i
    print(f"{num}%{i}={resultado}")
    if resultado==0:
        print(f"{num} não é primo pois {num}%{i}=0")
        break
    elif i==num-1:
        print(f"{num} é primo")
    i+=1

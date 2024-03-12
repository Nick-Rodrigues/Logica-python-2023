# num = input("digite um número: ")
# while not num.isnumeric():
#     num = input("ce é burro? digita um número porra: ")
# print("boa krl")
 
# pergunta = input("Voce gostaria de conhecer a calculadora?(S/N): ")

# while pergunta != "S" and pergunta != "N":
#    pergunta = input("Voce gostaria de conhecer a calculadora?(S/N): ")
# if pergunta == "S":
#    num1 = input("digite um número: ")
#    while not num1.isnumeric():
#       num1 = input("digita um número krl: ")
#    num1 = int(num1)
   
#    num2 = input("digite outro número: ")
#    while not num2.isnumeric():
#       num2 = input("d novo? responde número porra: ")
#    num2 = int(num2)

#    operacao = input("Digite uma operação: \nsoma \nsubtração \n sair")
#    while operacao != "soma" and operacao != "subtração" and operacao != "sair":
#       operacao = input("Digite uma operação válida \nsoma \nsubtração \n sair \n")
    
#    if operacao == "soma":
#       resultado = num1 + num2
#       print(f"a {operacao} é {resultado}")
#    elif operacao == "subtração":
#       resultado = num1 - num2
#       print(f"a {operacao} é {resultado}")  
#    else:
#       print("tmj cria flw")
# else:
#    print("chatao")

num = "4.5"
i = 0
while i < len(num):
    if num[i] == ".":
        indice = i
    i += 1
print(num[2])
     
      






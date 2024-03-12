resposta = input("Bem vindo a calculadora! Voce gostaria de conhece-la? (s/n) ")
while resposta != "s" and resposta != "n": #not (resposta == 'sim' or resposta == 'nao')
    resposta = input("Voce gostaria de conhece-la? (s/n) ")
if resposta == "n":
    print("tchau arrombado")
else:
    while True:
        escolha = input("Qual das opções vc gostaria de usar? \n+\n-\n*\n/\nsair \n")
        while escolha != "+" and escolha != "-" and escolha != "*" and escolha != "/" and escolha != "sair":
            escolha = input("Qual das opções vc gostaria de usar? \n+\n-\n*\n/\nsair \n")
        if escolha == "sair":
            print("Foi bom te conhecer!")
            break
        else:
            num1 = input("Diga um número: ")
            while not num1.isnumeric():
                num1 = input("Tem que ser um número: ")
            num2 = input("Diga um número: ")
            while not num2.isnumeric():
                num2 = input("Tem que ser um número: ")
            num1 = int(num1)
            num2 = int(num2)

            if escolha == "+":
                resultado = num1+num2
                print(f"A {escolha} entre {num1} e {num2} é {resultado}")
            elif escolha == "-":
                resultado = num1-num2
                print(f"A {escolha} entre {num1} e {num2} é {resultado}")

            elif escolha == "*":
                resultado = num1*num2
                print(f"A {escolha} entre {num1} e {num2} é {resultado}")
            else: 
                resultado = num1/num2
                print(f"A {escolha} entre {num1} e {num2} é {resultado}")

login = "nicolas"
senha = "rodrigues"

q1 = input("Digite seu login ")
q2 = input("Digite sua senha ")

if q1 == login and q2 == senha:
    print("Acesso liberado.")
elif q1 == login and q2 != senha:
    escolha = input("Senha incorreta. Gostaria de redefinir? ")
    if escolha == "sim":
        senha = input("Digite sua nova senha ")
        print("Senha alterada com sucesso.")
    else:
        print("Sai daqui irmão")
else:
    print("hacker")
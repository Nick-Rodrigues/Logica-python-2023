num1 = float(input("Me diga o primeiro numero : "))
num2 = float(input("Me diga o segundo numero : "))
var = str(input("Qual resultado voce gostaria de saber entre soma, subtração, divisão e multiplicação? "))

if var == "soma":
    print(f"o resultado dessa conta é {num1+num2}")
elif var == "subtração":
    print(f"o resultado dessa conta é {num1-num2}")
elif var == "divisão":
    print(f"o resultado dessa conta é {num1/num2}")
elif var == "multiplicação":
    print(f"o resultado dessa conta é {num1*num2}")
else:
    print("ta maluco porra? escreve direito")
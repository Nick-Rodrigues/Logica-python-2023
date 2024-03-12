num1 = float(input("Me diga o primeiro numero : "))
num2 = float(input("Me diga o segundo numero : "))
num3 = float(input("Me diga o terceiro numero : "))
p = str(input("Voce gostaria de saber o maior ou o menor entre os numeros listados? "))

if p == "maior":
    if num1>num3 and num1>num2:
        print(f"o numero {num1} é o maior entre eles")
    elif num2>num3 and num2>num1:
        print(f"o numero {num2} é o maior entre eles")
    elif num3>num1 and num3>num2:
        print(f"o numero {num3} é o maior entre eles")
elif p == "menor":
    if num1<num3 and num1<num2:
        print(f"o numero {num1} é o menor entre eles")
    elif num2<num3 and num2<num1:
        print(f"o numero {num2} é o menor entre eles")
    elif num3<num1 and num3<num2:
        print(f"o numero {num3} é o menor entre eles")      
else:
    print("ta maluco porra? responde direito")
# num1 = int(input("Me diga o primeiro valor "))
# num2 = int(input("Me diga o segundo valor "))
# num3 = int(input("Me diga o terceiro valor "))

# if num1<num2 and num2<num3:
#     print(f"a ordem crescente é {num1},{num2},{num3}")
# elif num2<num3 and num3<num1:
#     print(f"a ordem crescente é {num2},{num3},{num1}")
# elif num3<num1 and num1<num2:
#     print(f"a ordem crescente é {num3},{num1},{num2}")
# elif num3<num2 and num2<num1:
#     print(f"a ordem crescente é {num3},{num2},{num1}")
# elif num2<num1 and num1<num3:
#     print(f"a ordem crescente é {num2},{num1},{num3}")
# elif num1<num3 and num3<num2:
#     print(f"a ordem crescente é {num1},{num3},{num2}")

# sexo = input("Qual seu sexo? \n feminino = 1 \n masculino = 2 \n")
# altura = float(input("qual sua altura? "))
# if sexo == '1':
#     print ("seu peso ideal é", 62.1*altura - 44.7)
# else:
#     print ("seu peso ideal é", 72.7*altura - 58)

# lado = input("quantos lados tem o poligono? ")
# if lado == '3':
#     triangulo = int(input("qual a medida do lado em cm?"))
#     print("o polígono é um triangulo e a área é equivalente a ")
# elif lado == '4':
#     quadrado = int(input("qual a medida do lado em cm?"))
#     print("o polígono é um quadrado e a área é equivalente a", quadrado*quadrado, "centímetros")
# elif lado == '5':
#     print("o polígono é um pentagono")
# elif lado == '2' or lado == '1':
#     print("não é um polígono")
# else:
#     print("polígono não identificado.")

# a = int(input("Me diga o primeiro lado "))
# b = int(input("Me diga o segundo lado "))
# c = int(input("Me diga o terceiro lado "))
# if a == b == c:
#     print("equilatero")
# elif a != b and a !=c and b !=c:
#     print("escaleno")
# else:
#     print("isoceles")

a = int(input("Me diga o primeiro angulo "))
b = int(input("Me diga o segundo angulo "))
c = int(input("Me diga o terceiro angulo "))

if a == 90 or b == 90 or c == 90:
    print("triangulo retangulo")
elif a >= 90 or b >= 90 or c >= 90:
    print("triangulo obtusangulo")
elif a < 90 and b < 90 and c < 90:
    print("triangulo acutangulo")

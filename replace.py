frase = 'A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha.'
frase = frase.lower()
frase = frase.replace('.','')
frase = frase.split(' ')
print(frase)
# print(frase)

palavras = {}
for palavra in frase:
    if palavra not in palavras.keys():
        palavras[palavra] = 1
    else:
        palavras[palavra] += 1 
print(palavras)
for key in palavras.keys():
    for palavra in frase:
        if palavra == key:
            palavras[palavra] += 1
print(palavras)
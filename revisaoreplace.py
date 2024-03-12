travaLinguas = "A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha."

travaLinguas = travaLinguas.lower()
print(travaLinguas)
travaLinguas = travaLinguas.replace(".",'')
print(travaLinguas)
travaLinguas = travaLinguas.split(" ")
print(travaLinguas)
palavras = {}

for palavra in travaLinguas:
    palavras[palavra] = 0
    print(palavras)
for palavra in travaLinguas:
    palavras[palavra] += 1 
    print(palavras)

def conta_palavras(texto):
    texto = texto.lower()
    texto = texto.split(" ")
    palavras = {}
    for palavra in texto:
        if palavra not in palavras.keys():
            palavras[palavra] = 1
        else:
            palavras[palavra] += 1
    return
#NLTK - natural language toolkit
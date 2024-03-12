import requests     

pokemon = input("Qual pokemon voce quer saber as informações?: ")
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

response = requests.get(url).json()
print(f"Nome do pokemon: {response['name'].capitalize()}")
print(f"ID do pokemon: {response['id']}")

# habilidades = response['move'][]
# print(habilidades)

for i in range(0,2,1):
    print(f"{i+1}º habilidade do pokemon: {response['moves'][i]['move']['name']}")

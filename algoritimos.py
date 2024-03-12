# selection sort

def menor_valor(array):
    indice_menor = 0
    menor = array[indice_menor]
    for i in range(len(array)):
        candidatdo = array[i]
        if candidatdo < menor:
            menor = candidatdo
            indice_menor = i
    return indice_menor

#precisa do indice para remoção da lista original 
#precisa do indice para colocar o valor certo no novo array

# lista = [2,1,7,3,5,6,4,9,0]
# lista_ordenada = []

def selection_sort_pior(lista):
    lista_ordenada = []
    for i in range(len(lista)):
        local_menor = menor_valor(lista)
        menor_elemento = lista[local_menor]
        lista.pop(local_menor)
        lista_ordenada.append(menor_elemento)
        print(f"Menor = {menor_elemento}")
        print(f"Lista = {lista}")
        print(f"Lista ordenada = {lista_ordenada}")
        print()
    return lista_ordenada

lista = [2,1,7,3,5,6,4,9,0]
lista = selection_sort_pior(lista)
print(lista)


def selection_sort(array):
    for i in range(len(array)):
        print(array[i:])
        j = menor_valor(array[i:])+i
        aux = array[i]
        array[i] = array[j]
        array[j] = aux
    return array
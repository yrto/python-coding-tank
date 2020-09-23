# Faça um programa que, dadas duas listas de mesmo tamanho,
# crie uma nova lista com cada elemento igual a soma dos elementos
# da lista 1 com os da lista 2, na mesma posição.

lista1 = [1, 4, 5]
lista2 = [2, 2, 3]
lista3 = []

for i in range(len(lista1)):
    lista3.append(lista1[i] + lista2[i])

print(lista3)

# Agora faça um script que recebe uma palavra e informa se é um
# palíndromo, ou seja, se a palavra é igual a ela mesma ao contrário.

palavra = input("Digite algo: ")

palavra_lista = list(palavra)

if palavra_lista == palavra_lista[::-1]:
    print(palavra, "é um palíndromo")
else:
    print(palavra, "não é um palíndromo")

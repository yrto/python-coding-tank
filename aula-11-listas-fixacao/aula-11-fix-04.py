nome = ""
idade = 0
contador = 0

lista_nomes = []
lista_idades = []

while contador < 3:
    nome = input("Digite seu nome: ")
    lista_nomes.append(nome)

    idade = int(input("Digite sua idade: "))
    lista_idades.append(idade)

    contador += 1

print(lista_nomes)
print(lista_idades)

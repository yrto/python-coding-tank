numero = 0
contador = 0
media = 0
maiores = 0
lista = []

while contador < 10:
    numero = int(input("Digite um número: "))
    media += numero
    lista.append(numero)
    contador += 1

media = media / contador

for i in lista:
    if i > media:
        maiores += 1

print(lista)
print(media)
print(maiores, "números são maiores que a média")

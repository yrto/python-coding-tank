lista = []
contador = 0

while contador < 10:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    contador += 1

pares = 0

for i in lista:
    if i % 2 == 0:
        pares += 1

print(pares, "números são pares")

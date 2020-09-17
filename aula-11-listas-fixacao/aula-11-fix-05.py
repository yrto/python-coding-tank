contador = 0
lista = []

while contador < 10:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    contador += 1

lista.reverse()

print(lista)

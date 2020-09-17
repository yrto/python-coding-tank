lista = []
contador = 0
numero = int(input("Digite um número: "))

while numero != 0:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    lista.append(numero)
    contador += 1

print(lista)
print(contador, "números foram digitados")

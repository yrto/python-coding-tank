contador = 0
numeros = []

while contador < 10:
    numeros.append(int(input("Digite um número: ")))
    contador += 1

maior = 0
menor = numeros[0]

for i in numeros:
    if i > maior:
        maior = i
    elif i < menor:
        menor = i

print("O maior número é", maior)
print("O menor número é", menor)

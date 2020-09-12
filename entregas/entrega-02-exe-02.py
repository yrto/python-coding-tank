contador = 0
numeros = []
entradas_impares = []
resultado = 0

while contador < 10:
    numeros.append(int(input("Digite um número: ")))
    contador += 1

for i in numeros:
    if contador % 2 != 0:
        entradas_impares.append(i)
    contador -= 1

for i in entradas_impares:
    resultado += i

print(entradas_impares, "=", resultado)

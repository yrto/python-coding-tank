numero = int(input("Digite um número: "))

contador = 1
mult = 0

while contador <= 10:
    mult = numero * contador
    print(numero, "x", contador, "=", mult)
    contador = contador + 1

print("Fim")

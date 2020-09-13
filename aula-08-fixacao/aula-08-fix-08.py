numero = int(input("Digite um número: "))

numero_neg = numero * -1

while numero >= numero_neg:
    if numero % 2 == 0:
        print(numero)
    numero -= 1

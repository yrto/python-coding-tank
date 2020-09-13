numero_1 = int(input("Digite um número: "))

while numero_1 <= 10 or numero_1 % 2 != 0:
    numero_1 = int(input("Número inválido. Digite um número: "))

numero_2 = int(input("Digite outro número: "))

while numero_2 <= 10 or numero_2 % 2 != 0:
    numero_2 = int(input("Número inválido. Digite outro número: "))

print(numero_1, "+", numero_2, "=", (numero_1 + numero_2))

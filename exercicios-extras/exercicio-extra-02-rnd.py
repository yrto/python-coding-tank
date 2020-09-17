import random

numero_aleatorio = random.randint(1, 40)

numero_aleatorio_menos = numero_aleatorio - 3
numero_aleatorio_mais = numero_aleatorio + 3

numero = int(input("Digite um número de 1 a 40: "))

while numero != numero_aleatorio:
    if numero > numero_aleatorio_menos and numero < numero_aleatorio_mais:
        print("Você está quente!")
    numero = int(input("Digite um número de 1 a 40: "))

print(numero, "- Você acertou!")

# numero aleatorio entre 1 e 40
# peça número para usuário
# dizer se está quente ou frio

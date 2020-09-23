# Implemente um script que leia 10 números do usuário e informe se ali há algum número repetido.

lista = []
repetidos = []
contador = 0

for i in range(10):
    numero = int(input("Digite um número: "))
    lista.append(numero)
    if lista.count(numero) == 2:
        repetidos.append(numero)
        contador += 1

print("Temos", contador, "números repetidos:", repetidos)

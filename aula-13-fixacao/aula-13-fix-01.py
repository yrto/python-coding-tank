lista = []
repetidos = []
contador = 0

for i in range(5):
    numero = int(input("Digite um número: "))
    lista.append(numero)
    if lista.count(numero) == 2:
        repetidos.append(numero)
        contador += 1

print("Temos", contador, "números repetidos:", repetidos)

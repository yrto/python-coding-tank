numero = float(input("Digite um número: "))

total = 0
contador = 0

while numero != 0:
    total = total + numero
    contador += 1
    numero = float(input("Digite um número: "))

resultado = total / contador

print("A média dos números digitados é", resultado)

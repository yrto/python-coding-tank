lista = []
contador = 0

while contador < 10:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    contador += 1

lista_pares = []
lista_impares = []

for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)

print("Lista com pares:", lista_pares)
print("Lista com ímpares:", lista_impares)

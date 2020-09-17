# let's soccer

idades = [22, 24, 32, 18, 20, 28, 26, 25, 30, 40]
alturas = [1.78, 9.60, 1.90, 1.82, 1.77, 1.65, 1.79, 4.94, 2.01, 1.81]

maior_altura = 0
maior_indice = 0

for indice, valor_altura in enumerate(alturas):
    if valor_altura > maior_altura:
        maior_altura = valor_altura
        maior_indice = indice

print("O jogador mais alto tem",
      idades[maior_indice], "anos e", maior_altura, "metros de altura.")

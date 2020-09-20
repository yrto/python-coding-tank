precos = []
quantidade_vendida = []
total = 0

for i in range(3):
    precos.append(float(input("Digite o preço do produto: ")))
    quantidade_vendida.append(int(input("Digite a quantidade vendida: ")))

print(precos)
print(quantidade_vendida)

for i in range(len(precos)):
    total_por_produto = precos[i] * quantidade_vendida[i]
    print("Total arrecadado com o produto", (i + 1), ":", total_por_produto)
    total += total_por_produto

print("Total arrecadado:", total)

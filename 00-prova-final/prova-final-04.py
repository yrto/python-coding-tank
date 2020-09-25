# Crie um programa que pede para o usuário digitar o nome de cinco produtos
# e o respectivo preço deles. Salve o nome e o preço em um dicionário.

# Depois, peça para o usuário informar o nome de um produto e uma quantidade;
# em seguida, imprima o valor total.

produtos = {}

for i in range(5):

    print()
    nome_produto = input("Digite o nome do produto (ex: batata): ")
    preco_produto = float(input("Digite o preço do produto (ex: 14.99): "))

    produtos.update({nome_produto: preco_produto})

print()
print(produtos)
print()
nome_produto_consulta = input("Digite um nome de produto para consulta: ")
qtd_produto_consulta = int(input("Digite uma quantidade para consulta: "))

resultado = produtos[nome_produto] * qtd_produto_consulta
resultado_formatado = "{:.2f}".format(resultado)

print()
print(qtd_produto_consulta, "unidades de", nome_produto_consulta,
      "custarão", ("R$" + resultado_formatado))

perg_1 = "Mora perto da vítima? (s/n): "
perg_2 = "Já trabalhou com a vítima? (s/n): "
perg_3 = "Telefonou para a vítima? (s/n): "
perg_4 = "Esteve no local do crime? (s/n): "
perg_5 = "Devia para a vítima? (s/n): "
erro_0 = "Resposta inválida."

deducao = 0

# pergunta 1

resposta = input(perg_1)

while resposta != "s" and resposta != "n":
    print(erro_0)
    resposta = input(perg_1)

if resposta == "s":
    deducao += 1

# pergunta 2

resposta = input(perg_2)

while resposta != "s" and resposta != "n":
    print(erro_0)
    resposta = input(perg_2)

if resposta == "s":
    deducao += 1

# pergunta 3

resposta = input(perg_3)

while resposta != "s" and resposta != "n":
    print(erro_0)
    resposta = input(perg_3)

if resposta == "s":
    deducao += 1

# pergunta 4

resposta = input(perg_4)

while resposta != "s" and resposta != "n":
    print(erro_0)
    resposta = input(perg_4)

if resposta == "s":
    deducao += 1

# pergunta 5

resposta = input(perg_5)

while resposta != "s" and resposta != "n":
    print(erro_0)
    resposta = input(perg_5)

if resposta == "s":
    deducao += 1

# dedução

print("Seu índice de dedução é", deducao)

if deducao == 5:
    print("Você é o assassino!")
elif deducao >= 3:
    print("Você é um cúmplice!")
elif deducao == 2:
    print("Você é um suspeito!")
else:
    print("Você é inocente.")

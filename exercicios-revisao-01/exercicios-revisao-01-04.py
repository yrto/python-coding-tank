nome = []
idade = []

contador = 0

while contador < 10:
    nome.append(input("Digite seu nome: "))
    idade.append(int(input("Digite sua idade: ")))
    contador += 1

maior_idade = 0
menor_idade = 0

for i in idade:
    if i >= 18:
        maior_idade += 1
    else:
        menor_idade += 1

print(maior_idade, "pessoas são maiores de idade")
print(menor_idade, "pessoas são menores de idade")

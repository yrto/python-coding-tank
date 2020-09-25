# Crie um programa que peça o peso e a altura do usuário e, em seguida, calcule o IMC. Com base
# no valor do IMC, informe em qual classificação a pessoa se encontra, utilizando a tabela abaixo.

# IMC	                                CLASSIFICAÇÃO

# MENOR QUE 18,5	                    MAGREZA
# MAIOR OU IGUAL A 18,5 E MENOR QUE 25	NORMAL
# MAIOR OU IGUAL A 25,0 E MENOR QUE 30	SOBREPESO
# MAIOR OU IGUAL A 30,0 E MENOR QUE 40	OBESIDADE
# MAIOR OU IGUAL A 40,0	                OBESIDADE GRAVE

# Exemplo de Entrada	    Exemplo de Saída

# Peso: 70.5 Altura: 1.77	Classificação: Normal
# Peso: 50 Altura: 1.77	    Classificação: Magreza
# Peso: 86.9 Altura: 1.62	Classificação: Obesidade

peso = float(input("Digite o seu peso em (ex: 70.5): "))
altura = float(input("Digite a sua altura (ex: 1.75): "))

imc = peso / altura ** 2
imc_formatado = "{:.2f}".format(imc)

if imc < 18.5:
    classificacao = "Magreza"
elif imc < 25:
    classificacao = "Normal"
elif imc < 30:
    classificacao = "Sobrepeso"
elif imc < 40:
    classificacao = "Obesidade"
elif imc >= 40:
    classificacao = "Obesidade grave"
else:
    classificacao = "Não foi possívelcalcular"

print("Seu IMC é", imc_formatado)
print("Classificação:", classificacao)

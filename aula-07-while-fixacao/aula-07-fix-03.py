idade = int(input("Digite sua idade (ex. 32): "))

while idade < 0 or idade > 150:
    idade = int(input("Digite sua idade (ex. 32): "))

salario = float(input("Digite seu salário (ex. 2100,50): "))

while salario < 0:
    salario = float(input("Digite seu salário (ex. 2100,50): "))

genero = input("Informe seu genero (ex. M, F, ou outro): ")

while genero != "M" and genero != "F" and genero != "outro":
    genero = str(input("Informe seu genero (ex. M, F, ou outro): "))

print(idade, salario, genero)

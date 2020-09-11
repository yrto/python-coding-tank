salario = float(input("Digite o salário: "))

msg1 = "Seu salário atual é "
msg2 = "Seu reajuste será de "
msg3 = "Seu aumento foi de "
msg4 = "Seu novo salário será de "

if salario <= 2800:
    reajuste = 10
elif salario < 7000:
    reajuste = 15
elif salario < 15000:
    reajuste = 10
else:
    reajuste = 5

novoSalario = salario * (1 + (reajuste / 100))
aumento = novoSalario - salario
print(msg1 + "R$ " + str(salario))
print(msg2 + str(reajuste) + "%")
print(msg3 + "R$ " + str(aumento))
print(msg4 + "R$ " + str(novoSalario))

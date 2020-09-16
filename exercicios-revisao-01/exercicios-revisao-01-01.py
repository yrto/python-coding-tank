kwh = float(input("Digite a quantidade de kWh: "))
tarifa = 0.79
total_minimo = 27.90

total_consumido = kwh * tarifa

if total_consumido <= total_minimo:
    print("Valor a ser pago: R$", total_minimo, "(tarifa mínima)")
else:
    print("Valor a ser pago: R$", (total_consumido))

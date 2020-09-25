# Crie um código em Python para ler 3 valores de ponto flutuante (float) e efetuar o cálculo das raízes de uma equação de segundo grau (utilizando a fórmula de Bhaskara). Se não for possível calcular as raízes, mostre a mensagem “Impossível calcular” (você vai precisar verificar se vai aparecer algum denominador igual a 0 ou se o número da raiz quadrada será negativo).

# 10.0   20.1  5.1      R1 = -0.29788 R2 = -1.71212
# 10.3  203.0  5.0      R1 = -0.02466 R2 = -19.68408
#  0.0   20.0  5.0	    Impossível calcular
# 10.0   3.0   5.0	    Impossível calcular

a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

delta = b ** 2 - 4 * a * c

raiz_delta = delta ** 0.5

print(a, b, c)
print(raiz_delta)

while a == 0 or b == 0 or c == 0 or delta < 0:

    print("Impossível calcular! Tente novamente...")

    a = float(input("Informe o valor de A: "))
    b = float(input("Informe o valor de B: "))
    c = float(input("Informe o valor de C: "))

    delta = b ** 2 - 4 * a * c

    raiz_delta = delta ** 0.5

    print(a, b, c)
    print(raiz_delta)

xis_1 = (-(b) + raiz_delta) / (2 * a)
xis_2 = (-(b) - raiz_delta) / (2 * a)

print("x1 =", xis_1)
print("x2 =", xis_2)

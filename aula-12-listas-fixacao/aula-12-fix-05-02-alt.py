# let's soccer

idades = [22, 24, 32, 18, 20, 28, 26, 25, 30, 40]
alturas = [1.78, 9.60, 1.90, 1.82, 1.77, 1.65, 1.79, 4.94, 2.01, 1.81]

mais_alto = 0
idade = 0

for i in range(len(alturas)):
    print(i, idades[i], alturas[i])
    if alturas[i] > mais_alto:
        mais_alto = alturas[i]
        idade = idades[i]

print(idade)

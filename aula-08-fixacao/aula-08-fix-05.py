numero_inicial = 0
numero_final = 1000
contagem = 0

while numero_inicial <= numero_final:
    numero_inicial += 1
    if numero_inicial % 2 == 0:
        contagem += 1
        print(numero_inicial)

print("Temos", contagem, "números pares entre 0 e", numero_final)

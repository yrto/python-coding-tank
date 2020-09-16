numero_principal = 1
contador = 1
divisor = 1
soma = 0

while contador <= 1000:
    # print(numero_principal, "/", divisor)
    soma = soma + (numero_principal / divisor)
    divisor = divisor * 2
    contador += 1

print("Total:", soma)

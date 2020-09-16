seletor = 0
saldo = 1000.00

while seletor != 4:
    print("Bem-vindo ao Let's Bank")
    print("1. Depósito")
    print("2. Retirada")
    print("3. Saldo")
    print("4. Sair")
    seletor = int(input("Escolha uma opção: "))

    if seletor == 1:
        deposito = float(input("Quanto você gostaria de depositar? R$ "))
        saldo = saldo + deposito
        print("Seu saldo é R$", saldo)

    elif seletor == 2:
        retirada = float(input("Quanto você gostaria de retirar? R$ "))
        saldo = saldo - retirada
        print("Seu saldo é R$", saldo)

    elif seletor == 3:
        print("Seu saldo é R$", saldo)

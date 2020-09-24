def print_menu():
    print("Let's Cadastro")
    print()
    print("1. Novo cadastro")
    print("2. Exibir cadastros")
    print("3. Buscar cadastro por CPF")
    print("4. Sair")
    print()


opcao = 0

cadastros = {'4444': {'nome': 'Maria',
                      'email': 'maria@ig.com'}}

while opcao != 4:

    print_menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        print()
        print("1. Novo cadastro")
        print()
        novo_cpf = input("Digite o CPF (ex: 1234): ")
        novo_nome = input("Digite o nome (ex: João): ")
        novo_email = input("Digite o email (ex: joao@ig.com): ")
        cadastros.update({novo_cpf: {'nome': novo_nome, 'email': novo_email}})
        print()

    elif opcao == 2:

        print()
        print("2. Exibir cadastros")
        print()
        for cpf in cadastros:
            dados_cadastrais = cadastros[cpf]
            print(cpf, dados_cadastrais)
        print()

    elif opcao == 3:

        print()
        print("3. Buscar cadastro por CPF")
        print()
        cpf_buscado = input("Digite o número CPF (ex: 1234): ")
        print()
        if cpf_buscado in cadastros:
            print(cpf_buscado, cadastros[cpf_buscado])
        else:
            print("CPF não encontrado no cadastro")
        print()

print()
print("Saindo...")
print()

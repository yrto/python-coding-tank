# Bem-vindo ao PyTodo

# 1. visualizar tarefas
# 2. adicionar tarefas
# 3. atualizar tarefas   # escolher o id da tarefa, depois descricao, data, categoria
# 4. remover tarefas
# 0. fechar

def print_menu():
    print()
    print("Bem-vindo ao PyTodo")
    print()
    print("1. Visualizar tarefas")
    print("2. Adicionar tarefa")
    print("3. Atualizar tarefa")
    print("4. Remover tarefas")
    print("0. Sair")
    print()


opcao = 99

tarefas = {'00': ['Exemplo de tarefa', '10/09/20', 'exemplos']}

while opcao != 0:

    print_menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        print()
        print("1. Visualizar tarefas")
        print()

        for tarefa in tarefas:

            print("Tarefa", (tarefa + ":"),
                  tarefas[tarefa][0],
                  "|",
                  tarefas[tarefa][1],
                  "| Tags:",
                  tarefas[tarefa][2])

    elif opcao == 2:

        print()
        print("2. Adicionar tarefa")
        print()

        id_tarefa = input("Digite um ID para a tarefa (ex: 78): ")

        while id_tarefa in tarefas:
            id_tarefa = input("ID já existe, digite outro ID: ")

        descricao_tarefa = input("Descreva a tarefa: ")
        data_tarefa = input("Data da tarefa: ")
        categoria_tarefa = input("Categoria da tarefa: ")
        tarefas.update({id_tarefa: [
                        descricao_tarefa,
                        data_tarefa,
                        categoria_tarefa]})

        print()
        print("Tarefa adicionada!")

    elif opcao == 3:

        print()
        print("3. Atualizar tarefa")
        print()

        for tarefa in tarefas:

            print("Tarefa", (tarefa + ":"),
                  tarefas[tarefa][0],
                  "|",
                  tarefas[tarefa][1],
                  "| Tags:",
                  tarefas[tarefa][2])

        print()
        id_tarefa = input("Qual tarefa (ID) você gostaria de atualizar? ")
        print()

        if id_tarefa in tarefas:

            descricao_tarefa = input("Descreva novamente esta tarefa: ")
            data_tarefa = input("Data da tarefa: ")
            categoria_tarefa = input("Categoria da tarefa: ")
            tarefas.update({id_tarefa: [
                            descricao_tarefa,
                            data_tarefa,
                            categoria_tarefa]})

        else:

            print("ID inválido!")

    elif opcao == 4:

        print()
        print("4. Remover tarefas")
        print()

        for tarefa in tarefas:

            print("Tarefa", (tarefa + ":"),
                  tarefas[tarefa][0],
                  "|",
                  tarefas[tarefa][1],
                  "| Tags:",
                  tarefas[tarefa][2])

        print()
        id_tarefa = input("Qual tarefa (ID) você gostaria de remover? ")
        print()

        if id_tarefa in tarefas:

            tarefas.pop(id_tarefa)
            print("Tarefa", id_tarefa, "removido com sucesso!")

        else:

            print("ID inválido!")

    elif opcao == 0:

        print()
        print("Saindo...")
        print()
        break

    else:

        print()
        print("!!! Opção inválida !!!")

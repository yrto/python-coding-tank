# crie um script para gerenciar uma lista de tarefas

# Bem-vindo ao PyTodo

# 1. visualizar tarefas
# 2. adicionar tarefas
# 3. atualizar tarefas   # escolher o id da tarefa, depois descricao, data, categoria
# 4. remover tarefas
# 0. fechar

# Escolha sua opção:

# ---

# Digite o número da tarefa:  # verificar se existe com "in" ou não pedir o número
# Descrição:
# Data:
# Categoria:

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
        for tarefa in tarefas:
            print("Lista de tarefas")
            print("Tarefa", (tarefa + ":"),
                  tarefas[tarefa][0],
                  "|",
                  tarefas[tarefa][1],
                  "|",
                  tarefas[tarefa][2])

    elif opcao == 2:

        print("2.")

    elif opcao == 3:

        print("3.")

    elif opcao == 4:

        print("4.")

print()
print("Saindo...")
print()

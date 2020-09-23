# Faça um programa que simule uma pilha de livros, que inicialmente começa vazio. Um livro só poderá ser incluído no topo da pilha, assim como sua retirada, respeitando o tamanho máximo do vetor (10 livros). Usando laços, implemente opções de inserção, retirada, listagem da pilha e saida do programa.

# 1: Inserir livro (se a opção escolhida for essa, perguntar o nome do livro)
# 2: Remover livro
# 3: Listar livros
# 4: Sair do programa

pilha_livros = []
seletor = 0

while seletor != 4:
    print("\nLet's Books\n\n1 : Inserir livro\n2 : Remover livro\n3 : Listar livros\n4 : Sair\n")
    seletor = int(input("Digite uma opção: "))
    print()
    if seletor == 1:
        pilha_livros.append(input("Qual livro deseja adicionar? "))
        if pilha_livros == []:
            print("Sua pilha está vazia!")
        else:
            print()
            for i in pilha_livros:
                print((pilha_livros.index(i) + 1), i)
    elif seletor == 2:
        remover = int(input("Qual livro deseja remover? "))
        while remover > (len(pilha_livros)):
            remover = int(input("Qual livro deseja remover? "))
        pilha_livros.pop(remover - 1)
        if pilha_livros == []:
            print("Sua pilha está vazia!")
        else:
            print()
            for i in pilha_livros:
                print((pilha_livros.index(i) + 1), i)
    elif seletor == 3:
        if pilha_livros == []:
            print("Sua pilha está vazia!")
        else:
            for i in pilha_livros:
                print((pilha_livros.index(i) + 1), i)
    elif seletor == 4:
        print("Saindo...\n")
        break
    else:
        print("\nOpção inválida")

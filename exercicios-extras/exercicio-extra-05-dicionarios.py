alunos = {'nomes': ['Ayrton', 'Dandara', 'Felipe', 'Gustavo', 'Jeferson'],
          'cpf': [],
          'idades': [25, 20, 50, 19, 32]}

for chave in alunos:

    # "lista" é o "valor" da "chave" do dicionário "alunos"

    lista = alunos[chave]

    print(lista)

    for elemento_da_lista in lista:
        print(elemento_da_lista)

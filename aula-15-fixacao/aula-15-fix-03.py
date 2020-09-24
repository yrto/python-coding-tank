# Faça um script que receba os valores do nome, idade e e-mail de uma pessoa e
# guarde-os em um dicionário com as chaves ‘nome’, ‘idade’ e ‘email’, respectivamente.
# Exiba as informações desse dicionário.

dados_pessoais = {}

dados_pessoais['nome'] = input("Digite seu nome: ")
dados_pessoais['idade'] = int(input("Digite sua idade: "))
dados_pessoais['email'] = input("Digite seu email: ")

print(dados_pessoais)

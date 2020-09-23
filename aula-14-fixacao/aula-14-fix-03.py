# Escreva um programa que recebe um texto do
# usuário e retorna o número de espaços existentes.

# Exemplo 1
# input: "bom dia"
# output: texto contém 1 espaço

# Exemplo 2
# input: "hoje é quinta-feira"
# output: texto contém 2 espaços

texto = input("Digite algo: ")

print(texto, "contém", (texto.count(" ")), "espaços")

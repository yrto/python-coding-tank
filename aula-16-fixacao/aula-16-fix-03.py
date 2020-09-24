# Faça um script que leia uma frase do usuário e use um dicionário
# que apresente as palavras e a frequêcia de sua aparição na frase.

# input: bom dia dia
# output: {'bom':1 'dia':2}

frase_recebida = input("Digite uma frase: ")

frase_recebida_lista = frase_recebida.split(" ")

contagem = {}

for i in frase_recebida_lista:
    if i not in contagem:
        qtd = frase_recebida_lista.count(i)
        contagem.update({i: qtd})

print(contagem)

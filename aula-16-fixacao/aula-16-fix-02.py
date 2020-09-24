# Faça um script que leia uma frase do usuário e use um dicionário que
# apresente as letras e a frequência de aparição desta letra na frase.

# input: coding tank
# output: {'c':1, 'o':1, 'd':1, 'i':1, 'n':2, 'g':1, 't':1, 'a':1, 'k':1}

texto_recebido = input("Digite algo: ")

texto_recebido = list(texto_recebido.replace(' ', ''))

contagem = {}

for i in texto_recebido:
    if i not in contagem:
        qtd = texto_recebido.count(i)
        contagem.update({i: qtd})

print(contagem)

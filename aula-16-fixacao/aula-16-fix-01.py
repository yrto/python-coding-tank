# Faça um script usando dicionários que peça para um usuário
# digitar um número entre 0 e 9 e imprima o número por extenso.

por_extenso = {0: 'zero',
               1: 'um',
               2: 'dois',
               3: 'três',
               4: 'quatro',
               5: 'cinco',
               6: 'seis',
               7: 'sete',
               8: 'oito',
               9: 'nove'}

numero = int(input("Digite um número: "))

print(por_extenso[numero])

# Faça um script que receba um texto de entrada e informe:
# (i) quantas letras totais (sem espaço)
# (ii) quantas vogais
# (iii) quantas consoantes existem.

texto = input("Digite algo: ")
texto = texto.lower()

sem_espacos = texto.replace(" ", "")

vogais = ["a", "e", "i", "o", "u"]
qtd_vogais = 0

for i in vogais:
    qtd_vogais += texto.count(i)

qtd_consoantes = len(sem_espacos) - qtd_vogais

print("Seu texto tem", len(sem_espacos), "letras, sendo",
      qtd_vogais, "vogais e", qtd_consoantes, "consoantes")

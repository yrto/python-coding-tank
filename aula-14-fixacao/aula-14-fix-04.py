texto = input("Digite algo: ")
texto_lista = texto.split(" ")

maior_palavra = ''
contador = 0

for i in texto_lista:
    qtd_caracteres = len(i)
    if qtd_caracteres > contador:
        contador = qtd_caracteres
        maior_palavra = i

print(maior_palavra, "é a maior palavra")

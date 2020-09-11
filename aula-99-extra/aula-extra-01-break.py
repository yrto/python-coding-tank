while True:
    genero = input("Informe seu gênero: ")
    if genero == "M" or genero == "F" or genero == "outro":
        break
    else:
        print("Genero inválido.")

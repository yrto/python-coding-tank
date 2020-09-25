# Crie um script que pergunte ao usuário quantos cursos ele já fez na Let’s Code. Depois disso, pergunte o nome de cada curso que ele fez e sua respectiva carga horária. Salve os cursos em uma lista e a carga horária deles em outra lista.

# Por fim, imprima a lista dos cursos que ele já fez e, em seguida, a carga horária total (soma da carga horária de todos os cursos feitos).

qtd_cursos = int(input("Olá! Quantos cursos você já fez na Let's Code? "))

i = 1

cursos = []
carga_horaria = []

if qtd_cursos == 1:

    print("Qual o nome do curso?")
    cursos.append(input("Digite: "))
    print("Qual foi a carga horária do curso?")
    carga_horaria.append(int(input("Digite: ")))

elif qtd_cursos > 1:

    while i <= qtd_cursos:

        print("Qual o nome do", (str(i) + "º"), "curso?")
        cursos.append(input("Digite: "))
        print("Qual foi a carga horária do", (str(i) + "º"), "curso?")
        carga_horaria.append(int(input("Digite: ")))
        i += 1

print()
print("Você realizou o(s) curso(s):")
print()
for i in cursos:
    print(i)
print()
print("A carga horária total foi de", sum(carga_horaria), "horas")

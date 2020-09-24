# Dado o dicionário abaixo, descubra as médias de "homework", "quizzes"
# e "tests" dos três alunos. Ao final, apresente quem foi aprovado
# (caso média de "tests" maior que 65)

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

alunos = [lloyd, alice, tyler]

for i in alunos:
    print(i['name'])

    media_homework = sum(i['homework']) / len(i['homework'])
    print("Média homework:", media_homework)

    media_quizzes = sum(i['quizzes']) / len(i['quizzes'])
    print("Média quizzes:", media_quizzes)

    media_tests = sum(i['tests']) / len(i['tests'])
    print("Média tests:", media_tests)

    if media_tests >= 65:
        status = "Aprovado!"
    else:
        status = "Reprovado!"

    print("Status:", status)

    print()

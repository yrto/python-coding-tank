perg_1 = input("Sente dor no corpo? (s/n): ")
perg_2 = input("Você tem febre? (s/n): ")
perg_3 = input("Você tem tosse? (s/n): ")
perg_4 = input("Está com congestão nasal? (s/n): ")
perg_5 = input("Tem manchas pelo corpo? (s/n): ")

sintomas = [perg_1, perg_2, perg_3, perg_4, perg_5]

if sintomas == ["s", "s", "n", "n", "s"]:
    print("Você tem Dengue!")
elif sintomas == ["s", "s", "s", "s", "n"]:
    print("Você tem Gripe!")
elif sintomas == ["n", "s", "s", "s", "n"]:
    print("Você tem Gripe!")
elif sintomas == ["s", "s", "s", "s", "n"]:
    print("Você tem Gripe!")
elif sintomas == ["s", "n", "n", "n", "n"]:
    print("Você não tem doenças!")
elif sintomas == ["n", "n", "n", "n", "n"]:
    print("Você não tem doenças!")
else:
    print("Não consegui realizar o diagnóstico...")

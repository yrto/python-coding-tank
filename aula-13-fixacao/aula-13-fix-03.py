# Dada a lista abaixo (L), faça um script
# que informe o somatório dos números em L.

L = [[1, 2], [3, 4], [5, 6], [7, 8]]
M = []

for i in L:
    M.append(sum(i))

print(L)
print(M)

print("A soma dos números em L é", sum(M))

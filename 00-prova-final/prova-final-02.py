# Crie um script para calcular a área de uma figura geométrica:
# quadrado, retângulo, triângulo ou círculo.

# Para isso, peça para o usuário digitar qual é a figura geométrica e,
# em seguida, peça os dados necessários para calcular a área da figura.

# quadrado = lado²
# retangulo = base x altura
# triangulo = (base x altura) / 2
# circulo = pi x raio²

# O valor de pi é, aproximadamente, 3.1415.

figura = input("Gostaria de calcular a área de qual figura? ")

if figura == "quadrado":

    lado = float(input("Qual a medida do lado do quadrado? "))

    resultado = lado ** 2

elif figura == "retangulo":

    base = float(input("Qual a medida da base do retângulo? "))
    altura = float(input("Qual a medida da altura do retângulo? "))

    resultado = base * altura

elif figura == "triangulo":

    base = float(input("Qual a medida da base do triângulo? "))
    altura = float(input("Qual a medida da altura do triângulo? "))

    resultado = (base * altura) / 2

elif figura == "circulo":

    raio = float(input("Qual a medida do raio do círculo? "))

    resultado = 3.1415 * (raio ** 2)

resultado_formatado = "{:.2f}".format(resultado)

print("A área do seu", figura, "é", resultado_formatado)

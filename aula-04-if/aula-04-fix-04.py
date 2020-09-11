usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if usuario == "admin" and senha == "admin123":
    print("Você está logado")
else:
    print("Credenciais inválidas")

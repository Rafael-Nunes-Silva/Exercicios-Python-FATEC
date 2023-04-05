nome = input("Insira seu nome de usuário: ")
senha = input("Insira sua senha: ")

while nome == senha:
    senha = input("A senha não pode ser igual ao nome de usuário, insira a senha novamente: ")

print("Usuário criado com sucesso")

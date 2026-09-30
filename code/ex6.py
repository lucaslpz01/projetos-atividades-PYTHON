print(">>> VERSAO NOVA <<<")

usuario = "lucas@gmail"
senha = "lucas123"

while True:
    usuarios = input("Digite seu usuario: ")
    if usuarios == usuario:
        break
    print("usuario incorreto...")

while True:
    senhas = input("Digite sua senha: ")
    if senhas == senha:
        print("login bem sucedido!")
        break
    print("senha incorreta!")
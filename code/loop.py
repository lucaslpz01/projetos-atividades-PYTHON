# uso do while: repetidor/loop ou enquanto!

contador_numero = 15
while contador_numero >=1:
    print(f"contagem: {contador_numero}")
    contador_numero -=1


senha = "seucu123"
tentativa_senha = ""
while senha != tentativa_senha:
    tentativa_senha = input("digite sua senha: ")
    if tentativa_senha != senha:
        print("senha incorreta! tente novamente")
    else:
        print("senha correta!")
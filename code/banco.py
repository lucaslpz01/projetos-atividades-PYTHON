usuario = "lucas@gmail"
senha = "lucas123"
saldo = 1000.00

#----------------------------------------------------------

Sacar = 1
Depositar = 2
Fazer_pix = 3
Cartoes = 4
Pagamentos = 5
Saldo = 6
Sair = 0

print("-------------BANCO---------------")
print("")

while True:
    if input("Digite seu usuario: ") == usuario:
        break
    print("usuario incorreto...")

while True:
    if input("Digite sua senha: ") == senha:
        print("")
        print("login bem sucedido!")
        break
    print("senha incorreta!")



# ---------------- MENU (dentro do loop) ----------------
while True:
    print("")
    print("Escolha o serviço desejado: ")
    print("")
    print("1. sacar")
    print("2. depositar")
    print("3. fazer pix")
    print("4. cartões")
    print("5. pagamentos")
    print("6. saldo")
    print("0. sair")
    print("")

    escolha = int(input("digite o número do serviço: "))
    print("")



    if escolha == Sacar:
        valor = float(input("Digite o valor do saque: "))
        saldo -= valor
        print("")
        print(f"DINHEIRO SACADO: R$ {valor:.2f}")
        print("")
        print("--------------------------------------------")
        print("")



    elif escolha == Depositar:
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor
        print("")
        print(f"DINHEIRO DEPOSITADO: R$ {valor:.2f}")
        print("")
        print("--------------------------------------------")
        print("")



    elif escolha == Fazer_pix:
        chave = input("Digite a chave pix: ")
        valor = float(input("Digite o valor: "))
        saldo -= valor
        print("")
        print("TRANSAÇÃO BEM SUCEDIDA!")
        print("")
        print("--------------------------------------------")
        print("")



    elif escolha == Cartoes:
        print("Cartões cadastrados: ")
        print("")
        print("master 9900")
        print("master 0011")
        print("master 2200")
        print("")
        print("--------------------------------------------")
        print("")



    elif escolha == Pagamentos:
        print("Em construção...")



    elif escolha == Saldo:
        print(f"SALDO ATUAL: R$ {saldo:.2f}")
        print("")
        print("--------------------------------------------")
        print("")



    elif escolha == Sair:
        print("Até logo!")
        break

    else:
        print("Opção inválida.")
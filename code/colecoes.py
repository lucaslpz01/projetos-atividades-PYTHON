# uso do append, insert e remove e a troca de variavel!

nomes = ["lucas", "pedro", "marcelo"] #LISTA
nomes[0] = "linux"
nomes.append("vitor")
nomes.insert(1, "gui")
nomes.remove("marcelo")

if "joao" in nomes:
    print("tem o nome joao")
else:
    print("nao tem joao")

print(nomes)
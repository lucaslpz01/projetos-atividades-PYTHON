# uso do for e in com repetiçap de 5 vezes na aplicação!

notas = []

for numero in range(5):
    codigo_aluno = input("RM: ")
    nota = float(input("nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    print("quantidade de notas", len(notas))

    for n in notas:
        codigo_aluno = [0]
        nota = n[1]
        print("O RM", codigo_aluno, "tirou a nota: ", nota)
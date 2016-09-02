qtdTurma = eval(input(" Digite a quantidade de turmas: "))
soma = 0

for qtdAlunos in range(1, qtdTurma + 1):
    qtdAlunos = int(input(" Qual a quantidade de alunos em casa turma? "))

    if (qtdAlunos <= 40):
        somaA = soma +  qtdAlunos

    else:
        print("Essa turma é muito grande, o maximo permitido é 40 alunos por turma")
mediaDaTurma = somaA / qtdTurma

print(" Média de alunos por turma:", mediaDaTurma)

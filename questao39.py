numAluno = eval(input(" Digite o número do aluno: "))
AltAluno = eval(input(" Digite a altura do aluno: "))
AltMaior = AltAluno
AltMenor = AltAluno
numMaior = 0
numMenor = 0

for a in range(0, 10):

    if(AltAluno > AltMaior):
        AltMaior = AltAluno
        numMaior = numAluno

    elif(AltAluno < AltMenor):
        AltMenor = AltAluno
        numMenor = numAluno

    if(a != 10):
        numAluno = eval(input(" Digite o número do aluno: "))
        AltAluno = eval(input(" Digite a altura do aluno: "))

print(" O maior aluno é o:", numMaior, " Sua altura é = ", AltMaior)
print(" O menor aluno é o:", numMenor, " Sua altura é = ", AltMenor)

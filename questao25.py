numPessoas = eval(input(" Qual o numero de pessoas na turma? "))
aux = 0

for media in range(1, numPessoas+1):
    idade = eval(input(" Digite sua idade: "))
    soma = aux + idade
    aux = soma

media = soma / numPessoas

if (media >= 0 and media <= 25):
    print("Essa turma é jovem")

elif (media <= 60):
    print("Essa turma é adulta")

elif (media > 60):
    print("Essa turma é idosa")

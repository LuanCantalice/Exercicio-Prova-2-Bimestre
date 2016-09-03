qtdNotas = eval(input(" Digite a quantidade de notas: "))
nota = eval(input(" Digite a nota: "))
a = 0
aux = 0

for media in range(1, qtdNotas):
    soma = nota + a
    a = nota
    aux = aux + 1
    nota = eval(input(" Digite a nota: "))

mediaN = ((soma + nota) / qtdNotas)
print(" A média dessas notas é ", mediaN)

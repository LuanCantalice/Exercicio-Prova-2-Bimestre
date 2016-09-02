qtdNotas = eval(input(" Digite a quantidade de notas: "))
nota = eval(input(" Digite as notas: "))
a = 0
aux = 0

for media in range(1, qtdNotas+1):
    soma = nota + a
    a = nota
    aux = aux + 1
media = soma / qtdNotas

print(" A média dessas notas é ", media)
    
    
    

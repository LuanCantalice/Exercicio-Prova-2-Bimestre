qtdCd = eval(input("Qual a quantidade de CD's? "))
somaTotal = 0

for total in range(qtdCd):
    total = eval(input(" Qual o valor deste CD? "))
    somaTotal = somaTotal + total
mediaTotal = somaTotal / qtdCd

print(" Investimento total = ", somaTotal)
print(" Média de quanto gastou em cada CD: ", mediaTotal)

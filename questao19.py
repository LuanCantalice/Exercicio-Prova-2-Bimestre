numQtd = eval(input(" Qual a quantidade de números que você quer comparar? "))
num = eval(input(" Digite um número: "))
numMaior = num
numMenor = num
aux = 1
soma = 0

if(num > 0 and num <= 1000 or num == 1):
    while (numQtd >= aux):

        if(numQtd > aux):
            num = eval(input(" Digite um número: "))

        if(numMaior < num):
            numMaior = num

        elif(numMenor > num):
            numMenor = num
        aux = aux + 1
        soma = numMaior + numMenor

    print(" O maior número é o:", numMaior)
    print(" O menor número é o:", numMenor)
    print(" A soma desses números é:", soma)

else:
    print(" Os valores digitados foram inválidos(São menores que 0 ou maiores que 1000) ")

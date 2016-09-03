vzsFator = eval(input(" Quantas vezes irá fazer o vetorial? "))
num = eval(input(" Digite o número: "))
fator = 1

for a in range(0, vzsFator):
    if(num < 16):

        for b in range(1, num):
            fator = fator * num
            num = num - 1
        print(fator)

    else:
        print(" O valor é maior que 16, portanto, não é permitido. ")
    fator = 1

    if(a < (vzsFator - 1)):
        num = eval(input(" Digite o número: "))

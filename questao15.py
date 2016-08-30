num = eval(input(" Digite quantos números você quer: "))
num1 = 1
numUltimo = 0
numPenultimo = 0

for n in range(0, num):
    print(num1)
    numPenultimo = numUltimo
    numUltimo = num1
    num1 = numPenultimo + numUltimo

numFator = eval(input(" Qual o numero a ser fatorado? "))
fator = 1
numExtra = numFator

while(numFator > 1):
    fator = fator * numFator
    numFator = numFator - 1
print(" O fatorial de:", numExtra)

for i in range(1, numExtra + 1):
    print(numExtra)
    print("X")
    numExtra = numExtra - 1
print("=")
print(fator)

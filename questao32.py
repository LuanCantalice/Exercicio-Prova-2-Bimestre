numFator = eval(input(" Qual o numero a ser fatorado? "))
fatorAux = 1
numFator2 = numFator

while(numFator > 1):
    fatorAux = fatorAux * numFator
    numFator = numFator - 1
print(" O fatorial de:", numFator2)

for i in range(1, numFator2 + 1):
    print(numFator2)
    print("x")
    numFator2 = numFator2 - 1
print(" = ")
print(fatorAux)

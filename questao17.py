numFator = eval(input(" Digite o numero a ser fatorado: "))
fator = 1

while(numFator > 1):
    fator = fator * numFator
    numFator = numFator - 1
print(fator, " é o fatorial do numero digitado.")

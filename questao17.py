numFator = eval(input(" Qual numero você quer fatorar? "))
auxFator = 1

while(numFator > 1):
    auxFator = numFator * auxFator
    numFator = numFator - 1
print(" O numero digitado fatorado é igual a:", auxFator)

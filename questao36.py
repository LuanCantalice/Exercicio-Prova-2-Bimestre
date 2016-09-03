numTab = eval(input(" Digite o número que você quer ver a tabuada: "))
numInicial = eval(input(" Por qual numero a tabuada deve começar? "))
numFinal = eval(input(" Em que número ela deve acabar? "))
multip = 0

if(numFinal > numInicial):
    if(numFinal > numInicial):
        while(numInicial < numFinal + 1):
            multip = numInicial * numTab
            print(numTab, " X ", numInicial, " = ", multip)
            numInicial = numInicial + 1
    else:
        print(" O numero do início é maior que o número do final ")
else:
    print()

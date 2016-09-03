num = eval(input(" Digite um número: "))
a = 0
b = 0
aux = 1

while(aux <= num):
    resultado = num / aux

    if(resultado == int(resultado)):
        print(" Esse número é divisivel por:", aux)
        a = a + 1

    else:
        b = b + 1
    aux = aux + 1

if(a == 2):
    print("O número digitado é primo (divisível por 1 e por ele mesmo)")

else:
    print("O número digitado não é primo")

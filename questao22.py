num = eval(input(" Digite um número: "))
aux = 1
a = 0

while(aux <= num):
    b = 0
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

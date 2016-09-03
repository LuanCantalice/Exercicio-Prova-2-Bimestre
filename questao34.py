num = eval(input(" Qual o número? "))
a = 0
b = 0
aux = 1

for c in range(num+1):
    resultado = num / aux

    if(resultado == int(resultado)):
        a = a + 1

    else:
        b = b + 1
    aux = aux + 1

if(a == 2):
    print(" O número digitado é primo")
else:
    print(" O número digitado não é primo")

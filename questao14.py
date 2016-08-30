par = 0
impar = 0
for n in range(10):
    num = eval(input(" Digite um número: "))

    if (num % 2 == 0):
        par = par + 1

    else:
        impar = impar + 1

print(" Números pares =", par, " números ímpares =", impar)

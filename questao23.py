num = eval(input(" Digite um número: "))
aux = 1

while (num > aux):
    a = 0
    b = 0
    resultado = num / aux

    if (resultado == int(resultado)):
        print(aux)
    aux = aux + 1

print("Esse foi o número total de divisões.")

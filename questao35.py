num = eval(input(" Qual o número? "))
a = 0
b = 0
aux = 1

while(aux < num):
    resultado = (num / aux)
    if(resultado == int(resultado)):
        print(aux)
    aux = aux + 1

print("Os números acima é a quantidade de números primos que existe de 1 até", num)

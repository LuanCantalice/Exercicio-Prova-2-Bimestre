num = eval(input(" Digite o número: "))
verif = 4

while(num >= verif or num <= verif):

    if(num % verif == 0):
        print("Esse número não é primo")
        break

    else:
        print("Esse numero é primo")
        break

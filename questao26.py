eleitor = int(input("Qual a quantidade de eleitores? "))
candidato1 = 0
candidato2 = 0
candidato3 = 0

for voto in range(1, eleitor+1):
    voto = eval(input("Qual seu voto? "))

    if (voto == 1):
        candidato1 = candidato1 + 1

    elif (voto == 2):
        candidato2 = candidato2 + 1

    elif (voto == 3):
        candidato3 = candidato3 + 1

    else:
        while (voto != 1 and votos != 2 and votos != 3):
            print("O voto que você digitou foi invalido. Repita.")
            voto = eval(input("Qual seu voto? (1, 2 OU 3) "))
        
print("O candidato 1 teve", candidato1, " votos ")
print("O candidato 2 teve", candidato2, " votos ")
print("O candidato 3 teve", candidato3, " votos ")

if (candidato1 > candidato2 > candidato3):
    print(" O candidato 1 ganhou")

elif (candidato2 > candidato1 > candidato3):
    print(" O candidato 2 ganhou")

elif (candidato3 > candidato2 > candidato1):
    print(" O candidato 3 ganhou")
    

    

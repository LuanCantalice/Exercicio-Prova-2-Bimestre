tempQtd = eval(input(" Digite a quantidade de temperaturas: "))
temper = eval(input(" Digite o valor da temperatura: "))
aux = 1
soma = 0
tempMaior = temper
tempMenor = temper

while(aux <= tempQtd):

    if(aux < tempQtd):
        temper = eval(input(" Digite o valor da temperatura: "))

    if(temper > tempMaior):
        tempMaior = temper

    if(temper < tempMenor):
        temMenor = temper

    aux = aux + 1
    soma = soma + temper
mediaTemp = soma / tempQtd

print(" A maior temperatura registrada foi", tempMaior)
print(" A menor temperatura registrada foi", tempMenor)
print(" A média dessas temperaturas é", mediaTemp)

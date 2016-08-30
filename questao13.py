base = eval(input(" Digite a base: "))
expo = eval(input(" Digite o expoente: "))

if (expo != 0): 
    result = base
    for i in range(1, expo, 1):
        result = result * base
else:
    result = 0

print(result)

valorProduto = eval(input(" Digite o produto: "))
valorTotal = 0

while(valorTotal != 0):
    valorTotal = valorTotal + valorProduto
    valorProduto = eval(input(" Digite o produto: "))
print(" Valor total =", valorTotal)

din = eval(input(" Digite o dinheiro: "))
troco = din - valorTotal

print("Troco a ser recebido:", troco)
